"""Request routing primitives for the Tidewater runtime gateway."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Route:
    name: str
    weight: int = 1


class RequestRouter:
    """Weighted round-robin router with deterministic fallbacks."""

    def __init__(self, routes: List[Route]):
        if not routes:
            raise ValueError("at least one route is required")
        self._routes = list(routes)
        self._total = sum(r.weight for r in self._routes)

    def pick(self, key: str) -> Route:
        bucket = (hash(key) % self._total) + 1
        running = 0
        for route in self._routes:
            running += route.weight
            if bucket <= running:
                return route
        return self._routes[-1]

    def weights(self) -> Dict[str, int]:
        return {route.name: route.weight for route in self._routes}

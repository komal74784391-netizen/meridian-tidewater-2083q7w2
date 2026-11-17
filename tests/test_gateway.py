from tidewater.gateway import RequestRouter, Route


def test_pick_returns_configured_route():
    router = RequestRouter([Route("primary", 2), Route("shadow", 1)])
    assert router.pick("request-1").name in {"primary", "shadow"}


def test_weights_are_exposed():
    router = RequestRouter([Route("primary", 3)])
    assert router.weights() == {"primary": 3}

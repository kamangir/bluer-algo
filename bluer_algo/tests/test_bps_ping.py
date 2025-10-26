import random

from bluer_algo.bps.ping import Ping


def test_bps_ping():
    ping = Ping(Ping.simulate().as_dict())

    assert isinstance(ping.as_str(), str)

    as_dict = ping.as_dict()
    for keyword, value in as_dict.items():
        assert isinstance(keyword, str)
        assert isinstance(value, float)

    # ---

    ping = Ping.simulate()

    assert isinstance(ping.as_str(), str)

import random

from bluer_algo.bps.ping import Ping


def test_bps_ping():
    ping = Ping(Ping.simulate().as_dict())

    assert isinstance(ping.id, str)

    assert isinstance(ping.x, float)
    assert isinstance(ping.y, float)
    assert isinstance(ping.z, float)
    assert isinstance(ping.sigma, float)
    assert isinstance(ping.tx_power, float)

    assert isinstance(ping.as_str(), str)

    as_dict = ping.as_dict()
    for keyword, value in as_dict.items():
        assert isinstance(keyword, str)
        assert isinstance(value, float)


def test_bps_ping_simulation():
    ping = Ping.simulate()

    assert isinstance(ping, Ping)


def test_bps_ping_id_uniqueness():
    ping_1 = Ping()
    ping_2 = Ping()

    assert ping_1.id != ping_2.id

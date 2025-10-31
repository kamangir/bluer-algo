from bluer_algo.bps.simulation.timing.specs import Specs


def test_bps_simulation_node():
    specs = Specs()

    assert isinstance(specs.as_str(), str)

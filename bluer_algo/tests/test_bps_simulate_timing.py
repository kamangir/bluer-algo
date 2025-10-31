from bluer_objects import objects
from bluer_algo.bps.utils.simulation.functions import simulate


def test_bps_simulate_timing():
    object_name = objects.unique_object("test_bps_simulate_timing")

    assert simulate(object_name)

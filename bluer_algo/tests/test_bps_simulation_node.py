from bluer_algo.bps.utils.simulation.node import SimulatedBPSNode


def test_bps_simulation_node():
    node = SimulatedBPSNode()

    assert node.simulate()

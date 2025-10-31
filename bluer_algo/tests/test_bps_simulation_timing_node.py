from bluer_algo.bps.simulation.timing.node import Node


def test_bps_simulation_node():
    node = Node()

    assert node.simulate()

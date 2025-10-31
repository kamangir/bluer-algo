from tqdm import tqdm

from blueness import module
from bluer_options import string

from bluer_algo import NAME
from bluer_algo.bps.utils.simulation.node import SimulatedBPSNode
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def simulate(
    object_name: str,
    length: int = 120,
    nodes: int = 3,
    ta1: float = 30,
    ta2: float = 30,
    tr1: float = 24,
    tr2: float = 36,
) -> bool:
    logger.info(
        "{}.simulating for {} on {} node(s): "
        "ta: {} - {}, "
        "tr: {} - {} "
        "-> {}".format(
            NAME,
            string.pretty_minimal_duration(length),
            nodes,
            string.pretty_minimal_duration(ta1),
            string.pretty_minimal_duration(ta2),
            string.pretty_minimal_duration(tr1),
            string.pretty_minimal_duration(tr2),
            object_name,
        )
    )

    list_of_nodes = [
        SimulatedBPSNode(
            ta1=ta1,
            ta2=ta2,
            tr1=tr1,
            tr2=tr2,
        )
        for _ in range(nodes)
    ]

    for node in tqdm(list_of_nodes):
        if not node.simulate(length=length):
            return False

    logger.info("🪄")

    return True

from tqdm import tqdm

from blueness import module
from bluer_options import string

from bluer_algo import NAME
from bluer_algo.bps.simulation.timing.specs import Specs
from bluer_algo.bps.simulation.timing.node import Node
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def simulate(
    object_name: str,
    length: int = 120,
    nodes: int = 3,
    specs: Specs = Specs(),
) -> bool:
    logger.info(
        "{}.simulating for {} on {} node(s): {} -> {}".format(
            NAME,
            string.pretty_minimal_duration(length),
            nodes,
            specs.as_str(),
            object_name,
        )
    )

    list_of_nodes = [Node(specs) for _ in range(nodes)]

    for node in tqdm(list_of_nodes):
        if not node.simulate(length=length):
            return False

    logger.info("🪄")

    return True

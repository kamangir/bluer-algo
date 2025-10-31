from tqdm import tqdm
import numpy as np
import cv2

from blueness import module
from bluer_options import string
from bluer_objects import file, objects
from bluer_objects.graphics.signature import add_signature
from bluer_objects.metadata import post_to_object

from bluer_algo import NAME
from bluer_algo.host import signature
from bluer_algo.bps.simulation.timing.specs import Specs
from bluer_algo.bps.simulation.timing.state import State
from bluer_algo.bps.simulation.timing.node import Node
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def simulate(
    object_name: str,
    length: int = 1200,
    nodes: int = 3,
    specs: Specs = Specs(),
    verbose: bool = False,
    line_width: int = 80,
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

    logger.info("simulating...")
    list_of_nodes = [Node(specs) for _ in range(nodes)]

    for node in tqdm(list_of_nodes):
        if not node.simulate(
            length=length,
            verbose=verbose,
        ):
            return False

    # ---

    logger.info("estimating overlaps...")
    overlap = np.zeros((nodes, nodes))
    for node_index_a in range(nodes):
        for node_index_r in range(nodes):
            if node_index_a == node_index_r:
                continue

            overlap[node_index_a, node_index_r] = np.mean(
                [
                    state_a == State.A and state_r == State.R
                    for state_a, state_r in zip(
                        list_of_nodes[node_index_a].history,
                        list_of_nodes[node_index_r].history,
                    )
                ]
            )

            logger.info(
                "node #{} -> node #{}: {:.2f} %".format(
                    node_index_a,
                    node_index_r,
                    100 * overlap[node_index_a, node_index_r],
                )
            )

    mean_overlap = np.sum(overlap) / nodes / (nodes - 1)
    logger.info("mean overlap: {:.2f} %".format(100 * mean_overlap))

    # ---

    logger.info("generating the legend...")
    legend: np.ndarray = np.concatenate(
        [node.legend for node in list_of_nodes],
        axis=0,
    )

    legend = cv2.resize(
        legend,
        (
            legend.shape[1],
            legend.shape[0] * 20,
        ),
        interpolation=cv2.INTER_NEAREST_EXACT,
    )

    legend = add_signature(
        legend,
        header=[
            " | ".join(
                ["bps timing simulation"]
                + objects.signature(object_name)
                + [
                    f"{nodes} node(s)",
                    "length: {}".format(string.pretty_minimal_duration(length)),
                    "specs: {}".format(specs.as_str()),
                    "green: advertising, blue: receiving",
                    "mean overlap: {:.2f} %".format(100 * mean_overlap),
                ]
            )
        ],
        footer=[" | ".join(signature())],
        line_width=line_width,
    )

    if not file.save_image(
        objects.path_of(
            object_name=object_name,
            filename="bps-timing-simulation-legend.png",
        ),
        legend,
        log=True,
    ):
        return False

    # ---

    return post_to_object(
        object_name,
        "bps-timing-simulation",
        {
            "overlap": overlap.tolist(),
            "mean-overlap": float(mean_overlap),
        },
    )

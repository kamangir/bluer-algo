from typing import List

from blueness import module
from bluer_options import env
from bluer_objects.host import shell

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def start(
    log: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.start{}".format(
            NAME,
            " (verbose)" if verbose else "",
        )
    )

    list_of_commands: List[str] = []

    logger.info("starting bluetooth...")

    if env.abcli_is_rpi4 == "true":
        logger.info("rpi4b detected.")
        list_of_commands += [
            "sudo rfkill unblock bluetooth",
            "sudo hciconfig hci0 up",
        ]

    list_of_commands += ["sudo systemctl start bluetooth"]

    if verbose:
        list_of_commands += ["sudo systemctl status --no-pager bluetooth"]

    list_of_commands += [
        "sudo bluetoothctl power on",
        "sudo bluetoothctl discoverable on",
    ]

    if verbose:
        list_of_commands += ["sudo bluetoothctl show"]

    return all(
        shell(
            command=command,
            log=log,
        )
        for command in list_of_commands
    )

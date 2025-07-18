from blueness.pypi import setup

from bluer_algo import NAME, VERSION, DESCRIPTION, REPO_NAME

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.help",
        f"{NAME}.help.image_classifier",
        f"{NAME}.image_classifier",
        f"{NAME}.image_classifier.dataset",
        f"{NAME}.image_classifier.dataset.ingest",
        f"{NAME}.image_classifier.dataset.ingest.fruits_360",
        f"{NAME}.image_classifier.model",
        f"{NAME}.tracker",
        f"{NAME}.tracker.classes",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            ".abcli/**/*.sh",
        ],
    },
)

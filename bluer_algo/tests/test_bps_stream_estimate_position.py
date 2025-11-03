import pytest

from bluer_objects.storage.policies import DownloadPolicy
from bluer_objects import storage

from bluer_algo.bps.position import Position
from bluer_algo.bps.stream import Stream


@pytest.mark.parametrize(
    ["object_name"],
    [
        ["2025-11-02-20-53-13-45ycwm"],
    ],
)
def test_bps_stream_estimate_position(object_name: str):
    assert storage.download(
        object_name=object_name,
        policy=DownloadPolicy.DOESNT_EXIST,
    )

    stream = Stream.load(object_name=object_name)
    assert isinstance(stream, Stream)

    success, position = stream.estimate_position(object_name=object_name)
    assert success
    assert isinstance(position, Position)

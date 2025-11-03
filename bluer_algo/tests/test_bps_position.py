from bluer_objects import objects

from bluer_algo.bps.position import Position


def test_bps_position():
    object_name = objects.unique_object("test_bps_position")

    position = Position(1, 2, 3, 4)

    assert isinstance(position, Position)
    assert isinstance(position.as_dict(), dict)
    assert isinstance(position.as_str(), str)

    assert position.save(object_name)

    success, position = Position.load(object_name)
    assert success
    assert isinstance(position, Position)

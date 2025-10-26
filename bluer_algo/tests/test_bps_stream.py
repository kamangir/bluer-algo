from bluer_objects import objects

from bluer_algo.bps.ping import Ping
from bluer_algo.bps.stream import Stream


def test_bps_stream():
    object_name = objects.unique_object("test_bps_stream")

    stream = Stream()

    assert isinstance(stream.filename(object_name), str)
    assert isinstance(stream.ping, Ping)

    # ---

    stream = Stream.generate()
    assert isinstance(stream, Stream)

    # ---

    stream = Stream.generate(Ping.simulate().as_dict())
    assert isinstance(stream, Stream)

    # ---

    stream = Stream.generate(simulate=True)
    assert isinstance(stream, Stream)

    assert stream.save(object_name)

    # ---

    stream = Stream.load(object_name)
    assert isinstance(stream, Stream)

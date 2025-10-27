from bluer_objects import objects

from bluer_algo.bps.ping import Ping
from bluer_algo.bps.stream import Stream


def test_bps_stream():
    object_name = objects.unique_object("test_bps_stream")

    stream = Stream()

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

    # ---
    ping = Ping()

    assert stream.append(ping)
    # no repeat ping
    assert not stream.append(ping)

    ping = Ping()

    assert stream.append(ping)

    # ---

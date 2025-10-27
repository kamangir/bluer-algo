from bluer_objects import objects

from bluer_algo.bps.ping import Ping
from bluer_algo.bps.stream import Stream


def test_bps_stream():
    object_name = objects.unique_object("test_bps_stream")

    stream = Stream()

    assert isinstance(stream.ping, Ping)

    assert isinstance(stream.signature(), list)
    for item in stream.signature():
        assert isinstance(item, str)

    assert isinstance(stream.list_of_hostnames(), list)
    for hostname in stream.signature():
        assert isinstance(hostname, str)

    # ---

    stream.generate()

    assert isinstance(stream.ping, Ping)

    # ---

    stream.generate(Ping.simulate().as_dict())

    assert isinstance(stream.ping, Ping)

    # ---

    stream.generate(simulate=True)

    assert isinstance(stream.ping, Ping)
    assert stream.save(object_name)
    assert stream.export(object_name)

    # ---

    stream = Stream.load(object_name)

    assert isinstance(stream, Stream)

    # ---

    ping = Ping.simulate()

    assert stream.append(ping)
    # no repeat ping
    assert not stream.append(ping)

    ping = Ping.simulate()

    assert stream.append(ping)

# aliases: bps

```bash
@bps \
	beacon \
	[~start_bluetooth] \
	[-|<object-name>] \
	[--generate 1] \
	[--sigma <4.0>] \
	[--simulate 1] \
	[--spacing <2.0>] \
	[--timeout <10.0 | -1>] \
	[--x <1.0>] \
	[--y <2.0>] \
	[--z <3.0>]
 . start beacon.
@bps \
	generate \
	[-] \
	[-|<object-name>] \
	[--sigma <4.0>] \
	[--simulate 1] \
	[--x <1.0>] \
	[--y <2.0>] \
	[--z <3.0>]
 . generate a ping.
@bps \
	install
 . install bps.
@bps \
	introspect \
	[~start_bluetooth,verbose,unique_bus_name=<1:234>]
 . introspect <1:234>.
@bps \
	loop \
	start \
	[simulate,upload] \
	[-|<object-name>]
 . start bps loop.
@bps \
	loop \
	stop \
	[rpi,wait] \
	[<machine-name>]
 . stop bps loop.
@bps \
	receiver \
	[~start_bluetooth,upload,verbose] \
	[-|<object-name>] \
	[--grep <sparrow+swallow>] \
	[--timeout <10>]
 . start receiver.
@bps \
	receiver \
	[~python,~start_bluetooth,verbose]
 . start receiver.
@bps \
	review \
	[~download,upload] \
	[.|<object-name>]
 . review <object-name>.
@bps \
	simulate \
	timing \
	[upload] \
	[-|<object-name>] \
	[--length <1200>] \
	[--anchors <4>] \
	[--nodes <3>] \
	[--ta1 <20>] \
	[--ta2 <40>] \
	[--tr1 <20>] \
	[--tr2 <40>] \
	[--verbose 1]
 . simulate timing.
@bps \
	start_bluetooth \
	[verbose]
 . start bluetooth.
@bps \
	test \
	[~start_bluetooth,verbose]
 . d-bus ping test.
```

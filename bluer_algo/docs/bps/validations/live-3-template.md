title:::

on 3 rpis, continues [live-2b](./live-2.md) with an anchor.

on the anchor run,

```bash
@bps set_anchor 0,0,0,1
```

on the 

🔥

```bash
@select; @session start
```

set:::object_1_name TBA
set:::object_2_name TBA

details:::publication

```bash
runme() {
	local object_name
	for object_name in \
		get:::object_1_name \
		get:::object_2_name; do
			@assets publish \
				download,extensions=png,push \
				$object_name

			@upload public,zip \
				$object_name

	done
}

runme
```
details:::

| object:::get:::object_1_name | object:::get:::object_2_name |
|-|-|
| assets:::get:::object_1_name/bps.png | assets:::get:::object_2_name/bps.png |
| assets:::get:::object_1_name/ultrasonic-sensor-pulse-ms.png | assets:::get:::object_2_name/ultrasonic-sensor-pulse-ms.png | 
| assets:::get:::object_1_name/ultrasonic-sensor-state.png | assets:::get:::object_2_name/ultrasonic-sensor-state.png |
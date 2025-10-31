title:::

on 2 rpis,

```bash
@select; @session start
```

set:::object_1_name 2025-10-31-12-38-32-ot09o0
set:::object_2_name 2025-10-31-12-42-34-gg91z6

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
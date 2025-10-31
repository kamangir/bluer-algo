title:::

on 2 rpis, continues [live-2](./live-2.md) after timing adjustments.

```bash
@select; @session start
```

set:::object_1_name 2025-10-31-18-28-08-m702u0
set:::object_2_name 2025-10-31-18-28-24-mz7tk4

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
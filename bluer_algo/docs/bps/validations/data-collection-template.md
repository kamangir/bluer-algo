title:::

on 1 rpi:

```
@select bps-stream-$(@timestamp)
@bps generate - . \
	--sigma 1.0 \
	--x 0 \
	--y 0 \
	--z 0
@bps loop start upload .
```

on 2 rpis,

```bash
@bps loop start upload
```

in another terminal after a few minutes,

```bash
@bps loop stop [rpi <machine-name>]
```

set:::object_1_name bps-stream-2025-10-30-19-27-48-vr7so6
set:::object_2_name bps-stream-2025-10-30-19-27-56-kqbt2z
set:::object_3_name bps-stream-2025-10-30-19-27-58-pqxfee

details:::publication
```bash
runme() {
	local object_name
	for object_name in \
		get:::object_1_name \
		get:::object_2_name \
		get:::object_3_name; do
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

| object:::get:::object_1_name | object:::get:::object_2_name | object:::get:::object_3_name |
|-|-|-|
| assets:::get:::object_1_name/bps.png | assets:::get:::object_2_name/bps.png | assets:::get:::object_3_name/bps.png |

details:::get:::object_1_name/metadata
metadata:::get:::object_1_name:::bps
details:::

details:::get:::object_2_name/metadata
metadata:::get:::object_2_name:::bps
details:::

details:::get:::object_3_name/metadata
metadata:::get:::object_3_name:::bps
details:::

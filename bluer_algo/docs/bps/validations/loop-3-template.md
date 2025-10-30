title:::

on 3 rpis,

```bash
@bps loop start simulate,upload
```

in another terminal after a few minutes,

```bash
@bps loop stop
```

set:::object_1_name bps-loop-2025-10-30-18-03-01-l6ulkz
set:::object_2_name bps-loop-2025-10-30-18-02-44-jajwbj
set:::object_3_name bps-loop-2025-10-30-18-28-48-4e4g65

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
	done
}

runme
```
details:::

| | | |
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

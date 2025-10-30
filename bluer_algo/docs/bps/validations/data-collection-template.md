title:::

on 3 rpis,

```bash
@bps loop start upload
```

in another terminal after a few minutes,

```bash
@bps loop stop
```

set:::object_1_name TBA
set:::object_2_name TBA
set:::object_3_name TBA

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

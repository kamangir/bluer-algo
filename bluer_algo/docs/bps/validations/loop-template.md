title:::

on multiple rpis,

```bash
@bps loop start simulate,upload
```

in another terminal after a few minutes,

```bash
@bps loop stop
```

set:::object_1_name bps-loop-2025-10-27-19-44-19-2orply
set:::object_2_name bps-loop-2025-10-27-19-44-52-sf78j1

```bash
@assets publish \
	download,extensions=png,push \
	get:::object_1_name

@assets publish \
	download,extensions=png,push \
	get:::object_2_name
```

| | |
|-|-|
| assets:::get:::object_1_name/bps.png | assets:::get:::object_2_name/bps.png |

details:::get:::object_1_name/metadata
metadata:::get:::object_1_name:::bps
details:::

details:::get:::object_2_name/metadata
metadata:::get:::object_2_name:::bps
details:::

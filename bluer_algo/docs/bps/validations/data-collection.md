# bps: validations: data-collection

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
@bps loop stop
```



<details>
<summary>publication</summary>

```bash
runme() {
	local object_name
	for object_name in \
		TBA \
		TBA \
		TBA; do
			@assets publish \
				download,extensions=png,push \
				$object_name
	done
}

runme
```

</details>


| | | |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/TBA/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/TBA/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/TBA/bps.png?raw=true) |


<details>
<summary>TBA/metadata</summary>

```yaml
{}

```

</details>



<details>
<summary>TBA/metadata</summary>

```yaml
{}

```

</details>



<details>
<summary>TBA/metadata</summary>

```yaml
{}

```

</details>


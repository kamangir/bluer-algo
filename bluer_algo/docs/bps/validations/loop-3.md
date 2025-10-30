# bps: validations: loop-3

on 2 rpis,

```bash
@bps loop start simulate,upload
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


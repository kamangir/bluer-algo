# bps: validations: live-3

on 3 rpis, continues [live-2b](./live-2.md) with an anchor.

```bash
@bps set_anchor 0,0,0,1
```

🔥

```bash
@select; @session start
```



<details>
<summary>publication</summary>


```bash
runme() {
	local object_name
	for object_name in \
		TBA \
		TBA; do
			@assets publish \
				download,extensions=png,push \
				$object_name

			@upload public,zip \
				$object_name

	done
}

runme
```

</details>


| [TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz) | [TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz) |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/TBA/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/TBA/bps.png?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/TBA/ultrasonic-sensor-pulse-ms.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/TBA/ultrasonic-sensor-pulse-ms.png?raw=true) | 
| ![image](https://github.com/kamangir/assets/blob/main/TBA/ultrasonic-sensor-state.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/TBA/ultrasonic-sensor-state.png?raw=true) |

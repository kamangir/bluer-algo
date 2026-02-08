# bps: validations: live-2

on 2 rpis,

```bash
@select; @session start
```



<details>
<summary>publication</summary>


```bash
runme() {
	local object_name
	for object_name in \
		2025-10-31-12-38-32-ot09o0 \
		2025-10-31-12-42-34-gg91z6; do
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


| [2025-10-31-12-38-32-ot09o0.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-10-31-12-38-32-ot09o0.tar.gz) | [2025-10-31-12-42-34-gg91z6.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-10-31-12-42-34-gg91z6.tar.gz) |
|-|-|
| ![image](../../../../../assets/2025-10-31-12-38-32-ot09o0/bps.png?raw=true) | ![image](../../../../../assets/2025-10-31-12-42-34-gg91z6/bps.png?raw=true) |
| ![image](../../../../../assets/2025-10-31-12-38-32-ot09o0/ultrasonic-sensor-pulse-ms.png?raw=true) | ![image](../../../../../assets/2025-10-31-12-42-34-gg91z6/ultrasonic-sensor-pulse-ms.png?raw=true) | 
| ![image](../../../../../assets/2025-10-31-12-38-32-ot09o0/ultrasonic-sensor-state.png?raw=true) | ![image](../../../../../assets/2025-10-31-12-42-34-gg91z6/ultrasonic-sensor-state.png?raw=true) |

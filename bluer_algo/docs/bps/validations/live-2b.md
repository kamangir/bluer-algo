# bps: validations: live-2b

on 2 rpis, continues [live-2](./live-2.md) after timing adjustments.

```bash
@select; @session start
```



<details>
<summary>publication</summary>


```bash
runme() {
	local object_name
	for object_name in \
		2025-10-31-18-28-08-m702u0 \
		2025-10-31-18-28-24-mz7tk4; do
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


| [2025-10-31-18-28-08-m702u0.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-10-31-18-28-08-m702u0.tar.gz) | [2025-10-31-18-28-24-mz7tk4.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-10-31-18-28-24-mz7tk4.tar.gz) |
|-|-|
| ![image](../../../../../assets/2025-10-31-18-28-08-m702u0/bps.png?raw=true) | ![image](../../../../../assets/2025-10-31-18-28-24-mz7tk4/bps.png?raw=true) |
| ![image](../../../../../assets/2025-10-31-18-28-08-m702u0/ultrasonic-sensor-pulse-ms.png?raw=true) | ![image](../../../../../assets/2025-10-31-18-28-24-mz7tk4/ultrasonic-sensor-pulse-ms.png?raw=true) | 
| ![image](../../../../../assets/2025-10-31-18-28-08-m702u0/ultrasonic-sensor-state.png?raw=true) | ![image](../../../../../assets/2025-10-31-18-28-24-mz7tk4/ultrasonic-sensor-state.png?raw=true) |

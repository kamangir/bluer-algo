# bps: validations: live-3

on 3 rpis (1 anchor), continues [live-2b](./live-2.md) with an anchor.

on the anchor run,

```bash
@bps set_anchor 0,0,0,1
```

on all run,

```bash
@select; @session start
```



<details>
<summary>publication</summary>


```bash
runme() {
	local object_name
	for object_name in \
		2025-11-02-20-22-29-9o4nca \
		2025-11-02-20-22-27-g3a833 \
		2025-11-02-20-22-28-j8wwhs; do
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


| [2025-11-02-20-22-29-9o4nca](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-11-02-20-22-29-9o4nca.tar.gz) | [2025-11-02-20-22-27-g3a833](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-11-02-20-22-27-g3a833.tar.gz) | [2025-11-02-20-22-28-j8wwhs](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-11-02-20-22-28-j8wwhs.tar.gz) |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-29-9o4nca/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-27-g3a833/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-28-j8wwhs/bps.png?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-29-9o4nca/ultrasonic-sensor-pulse-ms.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-27-g3a833/ultrasonic-sensor-pulse-ms.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-28-j8wwhs/ultrasonic-sensor-pulse-ms.png?raw=true) | 
| ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-29-9o4nca/ultrasonic-sensor-state.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-27-g3a833/ultrasonic-sensor-state.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-22-28-j8wwhs/ultrasonic-sensor-state.png?raw=true) |

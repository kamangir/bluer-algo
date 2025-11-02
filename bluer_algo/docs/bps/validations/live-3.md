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
		2025-11-02-20-53-41-gpl909 \
		2025-11-02-20-53-13-45ycwm \
		2025-11-02-20-53-13-11qxlz; do
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


| [2025-11-02-20-53-41-gpl909](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-11-02-20-53-41-gpl909.tar.gz) | [2025-11-02-20-53-13-45ycwm](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-11-02-20-53-13-45ycwm.tar.gz) | [2025-11-02-20-53-13-11qxlz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-11-02-20-53-13-11qxlz.tar.gz) |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-41-gpl909/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-13-45ycwm/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-13-11qxlz/bps.png?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-41-gpl909/ultrasonic-sensor-distance-mm.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-13-45ycwm/ultrasonic-sensor-distance-mm.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-13-11qxlz/ultrasonic-sensor-distance-mm.png?raw=true) | 
| ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-41-gpl909/ultrasonic-sensor-state.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-13-45ycwm/ultrasonic-sensor-state.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/2025-11-02-20-53-13-11qxlz/ultrasonic-sensor-state.png?raw=true) |

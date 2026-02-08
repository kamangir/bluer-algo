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

after a few minutes,

```bash
@bps loop stop [rpi <machine-name>]
```



<details>
<summary>publication</summary>

```bash
runme() {
	local object_name
	for object_name in \
		bps-stream-2025-10-30-19-27-48-vr7so6 \
		bps-stream-2025-10-30-19-27-56-kqbt2z \
		bps-stream-2025-10-30-19-27-58-pqxfee; do
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


| [bps-stream-2025-10-30-19-27-48-vr7so6.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/bps-stream-2025-10-30-19-27-48-vr7so6.tar.gz) | [bps-stream-2025-10-30-19-27-56-kqbt2z.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/bps-stream-2025-10-30-19-27-56-kqbt2z.tar.gz) | [bps-stream-2025-10-30-19-27-58-pqxfee.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/bps-stream-2025-10-30-19-27-58-pqxfee.tar.gz) |
|-|-|-|
| ![image](../../../../../assets/bps-stream-2025-10-30-19-27-48-vr7so6/bps.png?raw=true) | ![image](../../../../../assets/bps-stream-2025-10-30-19-27-56-kqbt2z/bps.png?raw=true) | ![image](../../../../../assets/bps-stream-2025-10-30-19-27-58-pqxfee/bps.png?raw=true) |


<details>
<summary>bps-stream-2025-10-30-19-27-48-vr7so6/metadata</summary>

```yaml
history:
- hostname: sparrow2
  rssi: -66
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -49
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -50
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -52
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -53
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -76
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -58
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -55
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -57
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -56
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -57
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -68
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -71
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -53
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -54
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -70
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -52
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -67
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -51
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -66
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -71
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -69
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -55
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -50
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -72
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
ping:
  hostname: sparrow3-back
  rssi: -1.0
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0

```

</details>



<details>
<summary>bps-stream-2025-10-30-19-27-56-kqbt2z/metadata</summary>

```yaml
history:
- hostname: sparrow3-back
  rssi: -59
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -56
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -58
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -50
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -51
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -57
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -52
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -53
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -58
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -54
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -37
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -55
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -36
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -60
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -43
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -44
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -59
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow
  rssi: -42
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
ping:
  hostname: sparrow2
  rssi: -1.0
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0

```

</details>



<details>
<summary>bps-stream-2025-10-30-19-27-58-pqxfee/metadata</summary>

```yaml
history:
- hostname: sparrow3-back
  rssi: -58
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -59
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -74
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -54
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -55
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -51
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -53
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -69
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -52
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -43
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -44
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -37
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -50
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -36
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -60
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -57
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow3-back
  rssi: -56
  sigma: 1.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -52
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
- hostname: sparrow2
  rssi: -49
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0
ping:
  hostname: sparrow
  rssi: -1.0
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0

```

</details>


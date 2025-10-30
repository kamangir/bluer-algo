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


| [bps-stream-2025-10-30-19-27-48-vr7so6](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/bps-stream-2025-10-30-19-27-48-vr7so6.tar.gz) | [bps-stream-2025-10-30-19-27-56-kqbt2z](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/bps-stream-2025-10-30-19-27-56-kqbt2z.tar.gz) | [bps-stream-2025-10-30-19-27-58-pqxfee](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/bps-stream-2025-10-30-19-27-58-pqxfee.tar.gz) |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/bps-stream-2025-10-30-19-27-48-vr7so6/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/bps-stream-2025-10-30-19-27-56-kqbt2z/bps.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/bps-stream-2025-10-30-19-27-58-pqxfee/bps.png?raw=true) |


<details>
<summary>bps-stream-2025-10-30-19-27-48-vr7so6/metadata</summary>

```yaml
{}

```

</details>



<details>
<summary>bps-stream-2025-10-30-19-27-56-kqbt2z/metadata</summary>

```yaml
{}

```

</details>



<details>
<summary>bps-stream-2025-10-30-19-27-58-pqxfee/metadata</summary>

```yaml
{}

```

</details>


title:::

on one rpi,

```bash
@swallow env set bps 1
```

```bash
@env HAS_BPS
```

```text
BLUER_SBC_SWALLOW_HAS_BPS=1
```

```bash
@select; @session start
```

set:::object_name 2025-10-31-11-47-47-c2b6d9

details:::publication

```bash
@select get:::object_name

@assets publish \
    download,extensions=png,push .
    
@upload public,zip .
```
details:::

object:::get:::object_name

| | | |
|-|-|-|
| assets:::get:::object_name/bps.png | assets:::get:::object_name/ultrasonic-sensor-pulse-ms.png | assets:::get:::object_name/ultrasonic-sensor-state.png |
title:::

> ℹ️ tx-power is not implemented in rpi. nominal value: 10-12 dBm. -1: indicates unknown.

title:::

```bash
@bps beacon - - \
    --generate 1 \
    --sigma $(@random --float 1) \
    --x $(@random --float 1) \
    --y $(@random --float 1) \
    --z $(@random --float 1) \
    --timeout 60
```

on another pi,

```bash
@bps receiver upload - \
    --grep sparrow \
    --timeout 10
```

set:::object_name bps-receiver-2025-10-27-09-52-06-l3u3uy

metadata:::get:::object_name:::bps
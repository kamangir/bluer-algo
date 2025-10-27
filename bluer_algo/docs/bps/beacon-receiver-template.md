title:::

> ℹ️ tx-power is not implemented in rpi. nominal value: 10-12 dBm. -1: indicates unknown.

title:::

```bash
@select bps-$(@timestamp)
@bps beacon - . \
    --generate 1 \
    --sigma $(@random --float 1) \
    --x $(@random --float 1) \
    --y $(@random --float 1) \
    --z $(@random --float 1) \
    --timeout 60
```

on another pi,

```bash
@select bps-2025-10-27-09-18-25-wy7y93
@bps receiver upload . \
    --grep sparrow \
    --timeout 10
```

set:::object_name bps-2025-10-27-09-18-25-wy7y93

metadata:::get:::object_name
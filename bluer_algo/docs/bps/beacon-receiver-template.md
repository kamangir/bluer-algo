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

set:::object_name bps-receiver-2025-10-27-11-20-09-5e9kl1

metadata:::get:::object_name:::bps
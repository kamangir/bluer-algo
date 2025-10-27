title:::

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

on another rpi,

```bash
@bps receiver upload - \
    --grep sparrow+swallow \
    --timeout 10
```

set:::object_name bps-receiver-2025-10-27-13-13-32-9kjzvb

metadata:::get:::object_name:::bps
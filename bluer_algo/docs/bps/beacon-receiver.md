# bps: beacon-receiver

> ℹ️ tx-power is not implemented in rpi. nominal value: 10-12 dBm. -1: indicates unknown.

# bps: beacon-receiver

```bash
@select bps-$(@timestamp)
@bps beacon upload . \
    --generate 1 \
    --sigma $(@random --float 1) \
    --x $(@random --float 1) \
    --y $(@random --float 1) \
    --z $(@random --float 1) \
    --timeout 60
```

on another pi,

```bash
@select bps-2025-10-27-09-10-15-g9krir
@bps receiver - . \
    --grep sparrow \
    --timeout 10
```


```yaml
{}

```

# bps: beacon-receiver

> ℹ️ tx-power is not implemented in rpi. nominal value: 10-12 dBm. -1: indicates unknown.

# bps: beacon-receiver

```bash
@select bps-$(@@timestamp)
@bps beacon simulate,upload . \
    --x $(@random --float 1) \
    --y $(@random --float 1) \
    --z $(@random --float 1) \
    --sigma $(@random --float 1)
    --timeout 10
```

on another pi,

```bash
@select TBA
@bps receiver - . \
    --grep sparrow \
    --timeout 10
```


```yaml
{}

```

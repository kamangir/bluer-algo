# bps: beacon-receiver

> ℹ️ tx-power is not implemented in rpi. nominal value: 10-12 dBm. -1: indicates unknown.

# bps: beacon-receiver

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
@select bps-2025-10-27-09-23-57-93cqeh
@bps receiver upload . \
    --grep sparrow \
    --timeout 10
```


```yaml
history:
- sigma: 90.8095932006836
  x: 29.607803344726562
  y: 8.820128440856934
  z: 92.3553466796875
- sigma: 90.8095932006836
  x: 29.607803344726562
  y: 8.820128440856934
  z: 92.3553466796875
- sigma: 90.8095932006836
  x: 29.607803344726562
  y: 8.820128440856934
  z: 92.3553466796875
- sigma: 90.8095932006836
  x: 29.607803344726562
  y: 8.820128440856934
  z: 92.3553466796875
- sigma: 90.8095932006836
  x: 29.607803344726562
  y: 8.820128440856934
  z: 92.3553466796875
- sigma: 90.8095932006836
  x: 29.607803344726562
  y: 8.820128440856934
  z: 92.3553466796875
ping:
  sigma: 1000.0
  x: 0.0
  y: 0.0
  z: 0.0

```

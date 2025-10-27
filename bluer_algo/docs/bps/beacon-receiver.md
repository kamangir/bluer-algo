# bps: beacon-receiver

> ℹ️ tx-power is not implemented in rpi. nominal value: 10-12 dBm. -1: indicates unknown.

# bps: beacon-receiver

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


```yaml
history:
- sigma: 20.304895401000977
  x: 18.71828842163086
  y: 23.830392837524414
  z: 74.55341339111328
- sigma: 20.304895401000977
  x: 18.71828842163086
  y: 23.830392837524414
  z: 74.55341339111328
- sigma: 20.304895401000977
  x: 18.71828842163086
  y: 23.830392837524414
  z: 74.55341339111328
- sigma: 20.304895401000977
  x: 18.71828842163086
  y: 23.830392837524414
  z: 74.55341339111328
- sigma: 20.304895401000977
  x: 18.71828842163086
  y: 23.830392837524414
  z: 74.55341339111328
ping:
  sigma: 1000.0
  x: 0.0
  y: 0.0
  z: 0.0

```

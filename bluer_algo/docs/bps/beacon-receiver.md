# bps: beacon-receiver

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

on another rpi,

```bash
@bps receiver upload - \
    --grep sparrow+swallow \
    --timeout 10
```


```yaml
history:
- hostname: sparrow3-back
  rssi: -52
  sigma: 88.34217834472656
  tx_power: -1.0
  x: 33.44688415527344
  y: 45.99796676635742
  z: 94.80066680908203
- hostname: sparrow3-back
  rssi: -51
  sigma: 88.34217834472656
  tx_power: -1.0
  x: 33.44688415527344
  y: 45.99796676635742
  z: 94.80066680908203
ping:
  hostname: sparrow2
  rssi: -1.0
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0

```

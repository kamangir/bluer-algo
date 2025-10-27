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
- hostname: sparrow3-back
  rssi: -40
  sigma: 52.450531005859375
  tx_power: -1.0
  x: 46.10905456542969
  y: 58.41487121582031
  z: 33.19328308105469
- hostname: sparrow3-back
  rssi: -59
  sigma: 52.450531005859375
  tx_power: -1.0
  x: 46.10905456542969
  y: 58.41487121582031
  z: 33.19328308105469
- hostname: sparrow3-back
  rssi: -42
  sigma: 52.450531005859375
  tx_power: -1.0
  x: 46.10905456542969
  y: 58.41487121582031
  z: 33.19328308105469
- hostname: sparrow3-back
  rssi: -57
  sigma: 29.233020782470703
  tx_power: -1.0
  x: 55.4078369140625
  y: 46.344886779785156
  z: 89.33736419677734
- hostname: sparrow3-back
  rssi: -40
  sigma: 29.233020782470703
  tx_power: -1.0
  x: 55.4078369140625
  y: 46.344886779785156
  z: 89.33736419677734
- hostname: sparrow3-back
  rssi: -49
  sigma: 29.233020782470703
  tx_power: -1.0
  x: 55.4078369140625
  y: 46.344886779785156
  z: 89.33736419677734
- hostname: sparrow3-back
  rssi: -41
  sigma: 29.233020782470703
  tx_power: -1.0
  x: 55.4078369140625
  y: 46.344886779785156
  z: 89.33736419677734
- hostname: sparrow3-back
  rssi: -60
  sigma: 29.233020782470703
  tx_power: -1.0
  x: 55.4078369140625
  y: 46.344886779785156
  z: 89.33736419677734
- hostname: sparrow3-back
  rssi: -42
  sigma: 29.233020782470703
  tx_power: -1.0
  x: 55.4078369140625
  y: 46.344886779785156
  z: 89.33736419677734
- hostname: sparrow3-back
  rssi: -44
  sigma: 29.233020782470703
  tx_power: -1.0
  x: 55.4078369140625
  y: 46.344886779785156
  z: 89.33736419677734
ping:
  hostname: sparrow2
  rssi: -1.0
  sigma: 1000.0
  tx_power: -1.0
  x: 0.0
  y: 0.0
  z: 0.0

```

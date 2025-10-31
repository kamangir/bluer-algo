title:::

## 3 nodes

```bash
@select bps-timing-simulation-$(@@timestamp)

@bps simulate timing upload .

@assets publish extensions=png,push .
```

set:::object_name bps-timing-simulation-2025-10-31-zi9675

mean overlap: metadata:::get:::object_name:::bps-timing-simulation.mean-overlap

details:::metadata
metadata:::get:::object_name:::bps-timing-simulation
details:::

assets:::get:::object_name/bps-timing-simulation-legend.png

## 12 nodes

```bash
@select bps-timing-simulation-$(@@timestamp)

@bps simulate timing upload . \
    --nodes 12

@assets publish extensions=png,push .
```

set:::object_name bps-timing-simulation-2025-10-31-gdy4m0

mean overlap: metadata:::get:::object_name:::bps-timing-simulation.mean-overlap

details:::metadata
metadata:::get:::object_name:::bps-timing-simulation
details:::

assets:::get:::object_name/bps-timing-simulation-legend.png

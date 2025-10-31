title:::

> continues [v1](./timing-simulation-v1.md).

## 3 nodes

```bash
@select bps-timing-simulation-$(@@timestamp)

@bps simulate timing upload .

@assets publish extensions=png,push .
```

set:::object_name bps-timing-simulation-2025-10-31-qae3gy

mean overlap: metadata:::get:::object_name:::bps-timing-simulation.mean-overlap

details:::metadata
metadata:::get:::object_name:::bps-timing-simulation
details:::

assets:::get:::object_name/bps-timing-simulation-overlap.png

assets:::get:::object_name/bps-timing-simulation-legend.png

## 12 nodes

```bash
@select bps-timing-simulation-$(@@timestamp)

@bps simulate timing upload . \
    --nodes 12

@assets publish extensions=png,push .
```

set:::object_name bps-timing-simulation-2025-10-31-1kq018

mean overlap: metadata:::get:::object_name:::bps-timing-simulation.mean-overlap

details:::metadata
metadata:::get:::object_name:::bps-timing-simulation
details:::

assets:::get:::object_name/bps-timing-simulation-overlap.png

assets:::get:::object_name/bps-timing-simulation-legend.png
# bps: mathematics-timing

> Optimizing Advertise/Receive Cycle Timing

## Problem Setup

Each machine runs the following infinite loop:

1. **Advertise** for $t$ seconds  
2. **Receive** (scan) for a random duration $U(t_1, t_2)$ seconds

Each process (advertise or receive) takes:

- $t_o$ seconds to open  
- $t_c$ seconds to close  

Define the total per-phase overhead:


$$
s = t_o + t_c
$$

**Goal:** Choose $t$, $t_1$, and $t_2$ to maximize the expected number of advertisements received among all machines.

---

## Derivation

Useful (effective) durations:

$$
A = max(0, t - s) : \text{advertise}
$$

$$
R = max(0, m - s) : \text{receive}
$$

$$
m = (t_1 + t_2) / 2 : \text{mean receive time}
$$

Total cycle duration:

$$
C = t + m + 2s
$$

For many unsynchronized machines, the expected overlap fraction between “me listening” and “others advertising” is proportional to:

$$
P ∝ (R / C) * (A / C)
= ((m - s) * (t - s)) / (t + m + 2s)²
$$

## Optimal Relationship

1. For fixed $(t + m)$, $P$ is maximized when $t = m$.  
   → **The advertise time equals the mean receive time.**

2. With $t = m$, $P$ increases as $t$ grows relative to the overhead $s$.  
   → **Make both durations much longer than the open/close time.**

Therefore, the optimal condition is:

$$
t = (t_1 + t_2) / 2 - t, m >> s
$$

## Practical Recommendation

For:

$$
t_o = t_c = 5 s → s = 10 s
$$

Choose parameters so that $t ≥ 5s$ (i.e., at least 50 s) for good efficiency.

| Mode | Parameters | Notes |
|------|-------------|-------|
| **Balanced** | $t = 60 s$, $t_1 = 48 s$, $t_2 = 72 s$ | Mean listen time = 60 s, ±20% jitter |
| **High overlap (preferred)** | $t = 90 s$, $t_1 = 72 s$, $t_2 = 108 s$ | Best for throughput if latency allows |
| **Low latency** | $t = 50 s$, $t_1 = 40 s$, $t_2 = 60 s$ | Minimum practical balance |

---

## Summary

- Match advertise and mean receive times: $t = (t_1 + t_2) / 2$  
- Keep both much longer than $t_o + t_c$  
- Add 10–30% jitter to $t_1$/$t_2$ to avoid synchronization collisions  
- This maximizes the overlap between advertising and receiving phases across all machines.

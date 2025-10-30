title:::

> optimizing advertise/receive cycle timing - continues [v1](v1.md).

## problem setup

each machine runs the following infinite loop:

1. **advertise** for $t_a$ seconds  
2. **receive** (scan) for a random duration $U(t_{r1}, t_{r2})$ seconds

each process, advertise ($x=a$) or receive ($x=r$), takes:

- $t_{xo}$ seconds to open  
- $t_{xc}$ seconds to close  

define the total per-phase overhead:


$$
t_{as} = t_{ao} + t_{ac}
$$

$$
t_{rs} = t_{ro} + t_{rc}
$$


**goal:** Choose $t_a$, $t_{r1}$, and $t_{r2}$ to maximize the expected number of advertisements received among all machines.

---

## derivation

total cycle duration:

$$
T = t_a + t_{as} + t_{rm} + t_{rs}
$$

where,

$$
t_{rm} = \frac{1}{2}(t_{r1} + t_{r2}) : \text{mean receive time}
$$

for many unsynchronized machines, the expected overlap fraction between “me listening” and “others advertising” is proportional to:

$$
P ∝ \frac{t_a}{T} * \frac{t_{rm}}{T}
$$

## optimal relationship

for a fixed $T$,

$$
t_a + t_{rm} = T  - (t_{as} + t_{rs})
$$

is fixed and $P$ is maximized when,


$$
t_a = t_{rm} = \frac{1}{2}(T - t_{as} - t_{rs})
$$

$$
P ∝ \frac{1}{4} \left(1 - \frac{t_{as} + t_{rs}}{T}\right)^2
$$

therefore larger $T$ is more optimal for higher overlap.

the expected reaction time is,

$$
R ∝ T - t_a = \frac{1}{2}(T + t_{as} + t_{rs})
$$

therefore, smaller $T$ is more optimal for faster reaction.

## summary

- match advertise and mean receive times: $t_a = (t_{r1} + t_{r2}) / 2$  
- keep both much longer than $t_{as} + t_{rs}$  
- add 10–30% jitter to $t_{r1}/t_{r2}$ to avoid synchronization collisions  
- choose smaller $t_a$ to for faster reaction.

## practical choices

system parameters,

| $t_{ao}$ | $t_{ac}$ | $t_{as}$ | $t_{ro}$ | $t_{rc}$ | $t_{rs}$ |
|-|-|-|-|-|-|
| ~1 s | ~0 s | ~1 s| ~3 s | ~0.5 s | ~ 3s |

chose:

- $t_a$ = 30 s
- $r_{r1}$ = 24 s
- $r_{r2}$ = 36 s
- jitter: 20 %
- $T$: 64 s
- $P$: ~ 22%
- $R$: 34 s
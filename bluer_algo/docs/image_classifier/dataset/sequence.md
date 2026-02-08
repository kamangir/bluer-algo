# image-classifier: dataset: sequence

uses [bluer-ugv/swallow/digital/dataset/combination](../../../../../bluer-ugv/bluer_ugv/docs/swallow/digital/algo/navigation/dataset/combination).

```bash
@select 2025-07-09-11-16-52-4zo4zc

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid

@select sequence-$(@timestamp)

@algo image_classifier dataset sequence \
    ~download,length=3 .. .

@upload public,zip .
@assets publish \
    extensions=png,push . \
    --prefix grid
```



| | |
|-|-|
| ![image](../../../../../assets/2025-07-09-11-16-52-4zo4zc/grid.png?raw=true) | ![image](../../../../../assets/sequence-2025-07-12-21-58-04-0wmt6d/grid.png?raw=true) |
| ![image](../../../../../assets/2025-07-09-11-16-52-4zo4zc/grid-timeline.png?raw=true) | ![image](../../../../../assets/sequence-2025-07-12-21-58-04-0wmt6d/grid-timeline.png?raw=true) |

---

[2025-07-09-11-16-52-4zo4zc.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/2025-07-09-11-16-52-4zo4zc.tar.gz)

```yaml
dataset:
  class_count: 3
  classes:
    0: no_action
    1: left
    2: right
  count: 740
  shape:
  - 100
  - 100
  - 3
  source: 00000000c74cf7d2
  subsets:
    eval: 0
    test: 0
    train: 740

```

---

[sequence-2025-07-12-21-58-04-0wmt6d.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/sequence-2025-07-12-21-58-04-0wmt6d.tar.gz)

```yaml
dataset:
  class_count: 3
  classes:
    0: no_action
    1: left
    2: right
  count: 738
  length: 3
  shape:
  - 100
  - 300
  - 3
  source: 2025-07-09-11-16-52-4zo4zc
  subsets:
    eval: 0
    test: 0
    train: 738

```

# [image classifier](./image-classifier.md): Dataset: Sequence

```bash
@select 2025-07-09-11-16-52-4zo4zc
@select sequence-$(@timestamp)

@algo image_classifier dataset sequence \
    ~download,length=3 .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/sequence-2025-07-12-21-39-51-x5s756/grid.png?raw=true)

[sequence-2025-07-12-21-39-51-x5s756](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/sequence-2025-07-12-21-39-51-x5s756.tar.gz)

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
  - 700
  - 3
  source: 2025-07-09-11-16-52-4zo4zc
  subsets:
    eval: 0
    test: 0
    train: 738

```

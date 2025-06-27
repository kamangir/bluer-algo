# [image classifier](./image-classifier.md): ingest

- continues https://github.com/kamangir/image-classifier-2.
- uses https://github.com/fruits-360/fruits-360-100x100

```bash
@select fruits-365-$(@@timestamp)

@algo image_classifier ingest \
    clone,count=100,source=fruits_360 . \
    --class_count 10

@upload filename=metadata.yaml .
@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/fruits-365-2025-06-27-jvb4m9/grid.png?raw=true)

[fruits-365-2025-06-27-jvb4m9](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-2025-06-27-jvb4m9.tar.gz)

```yaml
dataset:
  class_count: 10
  classes:
    0: Cherry 4
    1: Nut 4
    2: Pear Monster 1
    3: Strawberry 1
    4: Tangelo 1
    5: Tomato 10
    6: Tomato 4
    7: Tomato 8
    8: Tomato Cherry Maroon 1
    9: Tomato Cherry Yellow 1
  count: 100
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 7
    test: 16
    train: 77

```

- 🔥

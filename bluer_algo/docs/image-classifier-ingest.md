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
```


[fruits-365-2025-06-27-ualwd6](TBA/fruits-365-2025-06-27-ualwd6.tar.gz)

```yaml
dataset:
  class_count: 10
  classes:
    0: Cabbage white 1
    1: Eggplant long 1
    2: Nectarine 1
    3: Orange 1
    4: Pear Red 1
    5: Pear Stone 1
    6: Pear Williams 1
    7: Pepper Green 1
    8: Raspberry 1
    9: Strawberry Wedge 1
  count: 100
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 7
    test: 14
    train: 79

```

- 🔥

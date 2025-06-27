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


[fruits-365-2025-06-27-9x6jtq](TBA/fruits-365-2025-06-27-9x6jtq.tar.gz)

```yaml
dataset:
  class_count: 10
  classes:
    0: Apple Core 1
    1: Avocado 1
    2: Cherry Rainier 2
    3: Cucumber 3
    4: Fig 1
    5: Nut Forest 1
    6: Onion Red Peeled 1
    7: Pear Monster 1
    8: Raspberry 1
    9: Tomato Maroon 1
  count: 100
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 17
    test: 14
    train: 69

```

- 🔥

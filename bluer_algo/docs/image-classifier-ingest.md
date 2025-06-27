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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-2025-06-27-9h7ksc/grid.png?raw=true)

[fruits-365-2025-06-27-9h7ksc](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-2025-06-27-9h7ksc.tar.gz)

```yaml
dataset:
  class_count: 10
  classes:
    0: Apple Granny Smith 1
    1: Apple Red 3
    2: Blackberrie 2
    3: Cabbage red 1
    4: Cherry Wax Black 1
    5: Clementine 1
    6: Corn Husk 1
    7: Salak 1
    8: Strawberry Wedge 1
    9: Tomato 5
  count: 100
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 6
    test: 7
    train: 87

```

- 🔥

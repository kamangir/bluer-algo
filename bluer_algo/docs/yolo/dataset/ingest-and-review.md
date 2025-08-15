# yolo: dataset: ingest-and-review

## full

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest \
    upload . \
    --verbose 1

@yolo dataset review \
	~download .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/coco128-2025-08-15-4nez2o/review.png?raw=true)

[coco128-2025-08-15-4nez2o](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/coco128-2025-08-15-4nez2o.tar.gz)

```yaml
dataset:
  count: 126
  source: coco_128
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush
path: ./coco128
train: images/train2017
val: images/train2017

```

## select classes

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest \
    upload . \
    --verbose 1 \
    --classes person

@yolo dataset review \
	~download .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main//review.png?raw=true)

[](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/.tar.gz)

```yaml
api_count: 2167
created_by: bluer_geo-5.15.1-bluer_flow-5.16.1-bluer_ai-12.136.1-bluer_objects-6.96.1-bluer_options-5.86.1-torch-2.2.2-Python
  3.12.9-Darwin 23.6.0--Jupyter-Notebook
creation_date: 23 April 2025, 10:33:49
dataset:
  class_count: 10
  classes:
    0: Apple 8
    1: Apple Braeburn 1
    2: Apple Golden 1
    3: Apple hit 1
    4: Cactus fruit red 1
    5: Cherry 4
    6: Nut 3
    7: Pear Red 1
    8: Tomato Cherry Orange 1
    9: Zucchini 1
  count: 10
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 2
    test: 0
    train: 8
description: Civilian Harm in Ukraine TimeMap
failure_count: 0
ingested_count: 2167
range:
- 2022-02-24
- 2025-04-06

```

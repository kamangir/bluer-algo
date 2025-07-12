# [image classifier](./image-classifier.md): Dataset: Sequence

uses [bluer-ugv/bluer-swallow-digital-dataset-combination.md](https://github.com/kamangir/bluer-ugv/blob/main/bluer_ugv/docs/bluer-swallow-digital-dataset-combination.md).

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

set:::source_object_name 2025-07-09-11-16-52-4zo4zc

assets:::get:::source_object_name/grid.png

object:::get:::source_object_name

metadata:::get:::source_object_name

---

set:::destination_object_name sequence-2025-07-12-21-58-04-0wmt6d

assets:::get:::destination_object_name/grid.png

object:::get:::destination_object_name

metadata:::get:::destination_object_name
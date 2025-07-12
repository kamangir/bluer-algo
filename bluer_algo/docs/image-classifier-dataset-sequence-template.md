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

set:::object_name sequence-2025-07-12-21-39-51-x5s756

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name
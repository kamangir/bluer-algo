# yolo: dataset: ingest

🔥

```bash
@select coco128-$(@@timestamp)

@algo yolo dataset ingest \
    ~upload . \
    --verbose 1

🔥

@upload public,zip .
@assets publish \
    extensions=png,push .
```

~upload -> upload 🚧


![image](https://github.com/kamangir/assets/blob/main/TBA/grid.png?raw=true)

[TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

```yaml
{}

```

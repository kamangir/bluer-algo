# tracker: kcf

# on a video file

```bash
@select tracker-kcf-$(@timestamp)

@algo tracker \
    algo=kcf . \
    --log 1

@assets publish \
    extensions=gif,push .
```

# on camera feed

```bash
@select tracker-kcf-$(@timestamp)

@algo tracker \
    algo=kcf,camera . \
    --log 1 \
    --show_gui 1

@assets publish \
    extensions=gif,push .
```



| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/tracker-kcf-2025-12-12-14-25-59-86f48h/tracker.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/tracker-kcf-2025-12-12-14-27-15-zuhu25/tracker.gif?raw=true) |

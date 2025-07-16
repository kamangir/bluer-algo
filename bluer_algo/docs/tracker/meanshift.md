# tracker: meanshift

# on a video file

```bash
@select tracker-meanshift-$(@timestamp)

@algo tracker \
    algo=meanshift . \
    --log 1

@assets publish \
    extensions=gif,push .
```

# on camera feed

```bash
@select tracker-meanshift-$(@timestamp)

@algo tracker \
    algo=meanshift,camera . \
    --log 1 \
    --show_gui 1

@assets publish \
    extensions=gif,push .
```



| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/tracker-meanshift-2025-07-16-10-43-31-v1u3k8/tracker.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/tracker-meanshift-2025-07-16-10-44-39-k9z4d7/tracker.gif?raw=true) |

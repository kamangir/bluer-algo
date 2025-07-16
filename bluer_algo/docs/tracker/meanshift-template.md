title:::

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

set:::video_object_name tracker-meanshift-2025-07-16-10-43-31-v1u3k8

set:::camera_object_name tracker-meanshift-2025-07-16-10-44-39-k9z4d7

| | |
|-|-|
| assets:::get:::video_object_name/tracker.gif | assets:::get:::camera_object_name/tracker.gif |
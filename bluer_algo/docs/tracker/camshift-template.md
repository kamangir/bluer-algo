title:::

# on a video file

```bash
@select tracker-camshift-$(@timestamp)

@algo tracker \
    algo=camshift . \
    --log 1

@assets publish \
    extensions=gif,push .
```

# on camera feed

```bash
@select tracker-camshift-$(@timestamp)

@algo tracker \
    algo=camshift,camera . \
    --log 1 \
    --show_gui 1

@assets publish \
    extensions=gif,push .
```

set:::video_object_name tracker-camshift-2025-07-16-11-06-21-xhs1i7

set:::camera_object_name tracker-camshift-2025-07-16-11-07-52-4u3nu4

| | |
|-|-|
| assets:::get:::video_object_name/tracker.gif | assets:::get:::camera_object_name/tracker.gif |
title:::

# on a video file

```bash
@select tracker-camshift-$(@timestamp)

@algo tracker \
    algo=meanshift . \
    --log 1

@assets publish \
    extensions=gif,push .
```

set:::video_object_name tracker-camshift-2025-07-16-10-16-25-uz0u94

assets:::get:::video_object_name/tracker.gif

# on camera feed

```bash
@algo tracker \
    algo=meanshift,camera
```

| | |
|-|-|
| assets:::tracker/meanshift-roi.png | assets:::tracker/meanshift-tracker.png |
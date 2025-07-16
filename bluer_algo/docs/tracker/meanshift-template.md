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

set:::video_object_name tracker-meanshift-2025-07-16-11-07-28-va2m1b

set:::camera_object_name abcli/tracker-meanshift-2025-07-16-11-08-44-jts0ho

| | |
|-|-|
| assets:::get:::video_object_name/tracker.gif | assets:::get:::camera_object_name/tracker.gif |
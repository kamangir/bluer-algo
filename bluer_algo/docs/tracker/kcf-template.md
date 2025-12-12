title:::

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

set:::video_object_name tracker-kcf-2025-12-12-14-04-37-vcuhwq

set:::camera_object_name tracker-kcf-2025-12-12-14-02-23-90e2yt

| | |
|-|-|
| assets:::get:::video_object_name/tracker.gif | assets:::get:::camera_object_name/tracker.gif |
title:::

# on a video file

```bash
@select tracker-klt-$(@timestamp)

@algo tracker \
    algo=klt . \
    --log 1

@assets publish \
    extensions=gif,push .
```

# on camera feed

```bash
@select tracker-KLT-$(@timestamp)

@algo tracker \
    algo=KLT,camera . \
    --log 1 \
    --show_gui 1

@assets publish \
    extensions=gif,push .
```

🔥

set:::video_object_name tracker-klt-2025-12-12-10-44-45-tn1w78

set:::camera_object_name TBA

| | |
|-|-|
| assets:::get:::video_object_name/tracker.gif | assets:::get:::camera_object_name/tracker.gif |
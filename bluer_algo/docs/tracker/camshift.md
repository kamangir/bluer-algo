# tracker: camshift

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



| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/tracker-camshift-2025-07-16-11-06-21-xhs1i7/tracker.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/tracker-camshift-2025-07-16-11-07-52-4u3nu4/tracker.gif?raw=true) |

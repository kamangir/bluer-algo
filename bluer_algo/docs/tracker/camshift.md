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
| ![image](https://github.com/kamangir/assets/blob/main/tracker-camshift-2025-07-16-10-35-46-lttkot/tracker.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/tracker-camshift-2025-07-16-10-36-48-o3rlnu/tracker.gif?raw=true) |

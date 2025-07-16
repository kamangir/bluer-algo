# tracker: meanshift

# on a video file

```bash
@select tracker-camshift-$(@timestamp)

@algo tracker \
    algo=meanshift . \
    --log 1

@assets publish \
    extensions=gif,push .
```

# on camera feed

```bash
@select tracker-camshift-$(@timestamp)

@algo tracker \
    algo=meanshift,camera . \
    --log 1 \
    --show_gui 1

@assets publish \
    extensions=gif,push .
```



| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/tracker-camshift-2025-07-16-10-20-49-58e83y/tracker.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/tracker-camshift-2025-07-16-10-32-14-ug1lr2/tracker.gif?raw=true) |

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
| ![image](https://github.com/kamangir/assets/blob/main/tracker-meanshift-2025-07-16-11-07-28-va2m1b/tracker.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/abcli/tracker-meanshift-2025-07-16-11-08-44-jts0ho/tracker.gif?raw=true) |

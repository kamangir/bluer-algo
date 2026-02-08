# tracker: klt

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
@select tracker-klt-$(@timestamp)

@algo tracker \
    algo=klt,camera . \
    --log 1 \
    --show_gui 1

@assets publish \
    extensions=gif,push .
```



| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/tracker-klt-2025-12-12-12-21-33-z7zg7x/tracker.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/tracker-klt-2025-12-12-12-25-01-8wl040/tracker.gif?raw=true) |

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
@select tracker-KLT-$(@timestamp)

@algo tracker \
    algo=KLT,camera . \
    --log 1 \
    --show_gui 1

@assets publish \
    extensions=gif,push .
```

🔥



| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/tracker-klt-2025-12-12-10-44-45-tn1w78/tracker.gif?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/TBA/tracker.gif?raw=true) |

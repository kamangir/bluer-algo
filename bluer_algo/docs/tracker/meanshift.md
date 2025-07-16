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


![image](https://github.com/kamangir/assets/blob/main/tracker-camshift-2025-07-16-10-16-25-uz0u94/tracker.gif?raw=true)

# on camera feed

```bash
@algo tracker \
    algo=meanshift,camera
```

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/tracker/meanshift-roi.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/tracker/meanshift-tracker.png?raw=true) |

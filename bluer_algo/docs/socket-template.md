title:::

# mac

both on mac.

```bash
@algo socket test - \
    --what receiving
```

```bash
@algo socket test - \
    --host dev.local \
    --what sending
```

✅

# rpi -> mac

on mac:

```bash
@algo socket test - \
    --what receiving
```

on rpi:

```bash
@algo socket test - \
    --host dev.local \
    --what sending
```

✅

# mac -> rpi

on rpi:

```bash
@algo socket test - \
    --what receiving
```

on mac:

```bash
@algo socket test - \
    --host swallow2.local \
    --what sending
```

✅
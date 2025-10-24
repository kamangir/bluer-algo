# bps: test-introspect

```bash
@bps install
```

```bash
@bps test
```

```text
🪄  bluer_algo.bps.utils.test: connected to system bus with unique name: :1.29
🪄  exported org.example.Hello at /org/example/Hello
🪄  run in another terminal: "@bps introspect unique_bus_name=:1.29"
```

in another terminal,

```bash
@bps introspect unique_bus_name=:1.29
```

```text
s "Pong"
```

validate in the first window,

```text
🪄  bluer_algo.bps.utils.test.ping() called by busctl!
```

tested on 2 rpis.

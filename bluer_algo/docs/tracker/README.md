# tracker

target tracking for a [ugv](https://github.com/kamangir/bluer-ugv/tree/main/bluer_ugv/docs/swallow/digital/algo) using [mean/cam-shift](https://docs.opencv.org/4.11.0/d7/d00/tutorial_meanshift.html).

- sandbox: [sandbox/mean-cam-shift](../../../sandbox/mean-cam-shift)
- [camshift](./camshift.md)
- [meanshift](./meanshift.md)
- [KLT](./klt.md)
- [KCF](./kcf.md)

> ℹ️ conclusion: `camshift` tracks distinct colors more robustly than `meanshift` and adjusts to object size.

> ⚠️ neither `camshift` nor `meanshift` are operationally relevant.

> ⚠️ `klt` loses a moving target on a busy background.

> ✅ kcf looks promising. ✅

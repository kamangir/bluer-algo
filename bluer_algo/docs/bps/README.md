# bps

bluer-positioning system.

> A distributed, serverless positioning mesh where every Raspberry Pi acts as both a tag and a local estimator.

> Each node continuously advertises a compact BLE packet containing its node ID, mobility flag, and its current best-estimate pose (x, y, σ, seq), and simultaneously scans for neighbor adverts to collect RSSI + neighbor poses. Anchors are marked static with known coordinates and low uncertainty; mobiles fuse anchors + neighbor pseudo-ranges (RSSI→distance, calibrated per site) with a lightweight weighted least-squares + EKF/Covariance-Intersection step, adapting advertising/scan rates when moving, and using short rolling HMAC tokens to prevent simple spoofing.

> On top of this short-range BLE layer, each node also maintains a long-range LoRa link for resilient, low-bitrate telemetry and command exchange. Nodes periodically broadcast a minimal LoRa frame (node ID, mobility state, coarse pose, health, seq), enabling the system to preserve connectivity and coarse localization even when BLE neighborhoods fragment or mobility exceeds local coverage. Gateways or elevated anchors can aggregate LoRa packets to extend system reach to tens or hundreds of kilometers across a region, without altering the peer-to-peer logic of the BLE layer.

> The result is a dual-layer gossiping swarm:
- fine-grained, high-rate positioning over BLE;
- persistent, long-range coordination over LoRa.
> The mesh converges locally to consistent poses, degrades gracefully to coarse regional awareness under sparse connectivity, and remains forward-compatible with future UWB or GNSS integration without changing the core serverless protocol.


- AI convo: [1️⃣](https://chatgpt.com/c/68e79d65-e938-8327-b1e1-2536f7b6fb41) [2️⃣](https://chatgpt.com/c/693131aa-6448-8325-9e6e-4ed49035a5f9)
- [literature](./literature.md) 
- [mathematics](./mathematics)
- [sandbox](../../../../bluer-sandbox/sandbox/bps)
- [bluer_algo.bps](../../bps)
- [validations](./validations)
- [simulations](./simulations)

|   |   |
| --- | --- |
| [![image](../../../../assets2/bps/01.png?raw=true)](../../../../assets2/bps/01.png?raw=true) | [![image](../../../../assets2/bps/03.png?raw=true)](../../../../assets2/bps/03.png?raw=true) |
| [![image](../../../../assets2/bps/02.png?raw=true)](../../../../assets2/bps/02.png?raw=true) | [![image](../../../../assets2/bps/05.png?raw=true)](../../../../assets2/bps/05.png?raw=true) |

> ℹ️ works on rpi only.

> ℹ️ tx-power is not implemented in rpi. nominal value: 10-12 dBm. -1: indicates unknown.

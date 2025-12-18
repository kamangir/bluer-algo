# ai-agent: speech-to-text: validation

```bash
@select ai-agent-speech-to-text-$(@@timestamp)
```


# farsi

```bash
@agent validate \
	filename=farsi.wav,language=fa,record,upload .
```

```yaml
{}

```

[ai-agent-speech-to-text-2025-12-18-r5hbwu/farsi.wav](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/ai-agent-speech-to-text-2025-12-18-r5hbwu/farsi.wav.tar.gz)

# english

```bash
@agent validate \
	filename=english.wav,language=en,record,upload .
```

```yaml
{}

```

[ai-agent-speech-to-text-2025-12-18-r5hbwu/english.wav](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/ai-agent-speech-to-text-2025-12-18-r5hbwu/english.wav.tar.gz)

---


<details>
<summary>code</summary>

```bash
@upload filename=farsi.wav,public
@upload filename=english.wav,public
```

</details>



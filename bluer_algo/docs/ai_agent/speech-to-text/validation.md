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

[farsi.wav](https://github.com/kamangir/assets/blob/main/ai-agent-speech-to-text-2025-12-18-r5hbwu/farsi.wav)

# english

```bash
@agent validate \
	filename=english.wav,language=en,record,upload .
```

```yaml
{}

```

[english.wav](https://github.com/kamangir/assets/blob/main/ai-agent-speech-to-text-2025-12-18-r5hbwu/english.wav)

---


<details>
<summary>code</summary>

```bash
@assets publish extensions=wav,push
```

</details>



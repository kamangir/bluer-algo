title:::

```bash
@select ai-agent-speech-to-text-$(@@timestamp)
```

set:::object_name env:::BLUER_ALGO_AI_AGENT_S2T_TEST_OBJECT

# farsi

```bash
@agent speech_to_text validate \
	filename=farsi.wav,language=fa,record,upload .
```

metadata:::get:::object_name:::farsi

assets:::get:::object_name/farsi.wav

# english

```bash
@agent speech_to_text validate \
	filename=english.wav,language=en,record,upload .
```

metadata:::get:::object_name:::english

assets:::get:::object_name/english.wav

---

details:::code
```bash
@metadata upload
@assets publish extensions=wav,push
```
details:::


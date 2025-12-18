title:::

```bash
@select ai-agent-speech-to-text-$(@@timestamp)
```

set:::object_name env:::BLUER_ALGO_AI_AGENT_TEST_OBJECT

# farsi

```bash
@agent validate \
	filename=farsi.wav,language=fa,record,upload .
```

metadata:::get:::object_name:::farsi.wav

object:::get:::object_name/farsi.wav

# english

```bash
@agent validate \
	filename=english.wav,language=en,record,upload .
```

metadata:::get:::object_name:::english.wav

object:::get:::object_name/english.wav

---

details:::code
```bash
@upload filename=farsi.wav,public
@upload filename=english.wav,public
```
details:::


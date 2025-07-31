```python
import whisper

model = whisper.load_model("base")

def transcribe(video_path: str):
    result = model.transcribe(video_path)
    return result['text']
```

---

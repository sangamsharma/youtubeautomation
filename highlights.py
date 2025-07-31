```python
import openai
openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_clips(transcript):
    prompt = f"""
    You're a YouTube content editor.
    Extract 3 interesting moments (less than 60s) from the transcript below.
    Return a list of JSON with `start`, `end`, and `description`.

    Transcript:
    {transcript}
    """
    res = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message['content']
```

---

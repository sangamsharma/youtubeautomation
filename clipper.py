```python
import subprocess
import os

def create_clip(input_video, start, end, output_path):
    duration = end - start
    cmd = [
        'ffmpeg', '-ss', str(start), '-i', input_video,
        '-t', str(duration), '-vf', 'scale=1080:1920',
        '-c:v', 'libx264', '-preset', 'ultrafast',
        '-c:a', 'aac', '-y', output_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path
```

---

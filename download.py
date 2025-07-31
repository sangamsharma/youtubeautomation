```python
import yt_dlp

def download_video(youtube_url: str, output_path: str = "video.mp4"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': output_path,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    return output_path
```

---

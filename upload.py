```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

def upload_to_youtube(title, description, video_path):
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/youtube.upload'])
    youtube = build('youtube', 'v3', credentials=creds)

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['Shorts'],
            'categoryId': '22'
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    media = MediaFileUpload(video_path, mimetype='video/*', resumable=True)
    req = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
    resp = req.execute()
    return resp.get('id')
```

---

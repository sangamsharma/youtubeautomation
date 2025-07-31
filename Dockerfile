```Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY backend/ ./
COPY requirements.txt ./

RUN apt-get update && apt-get install -y ffmpeg && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "download.py"]
```

---

from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.post("/trigger-download")
async def trigger_download(request: Request):
    body = await request.json()
    url = body.get("url")
    if url:
        subprocess.Popen(["python3", "backend/download.py", url])
        return {"status": "Started download for " + url}
    return {"error": "No URL provided"}

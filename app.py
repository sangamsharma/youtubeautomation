from fastapi import FastAPI, Request
import subprocess
import os

app = FastAPI()

@app.post("/trigger-download")
async def trigger_download(request: Request):
    try:
        body = await request.json()
        url = body.get("url")
        if not url:
            return {"error": "No URL provided"}, 400

        # Run download.py and wait for completion
        result = subprocess.run(
            ["python3", "backend/download.py", url],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode != 0:
            return {"error": "Download failed", "details": result.stderr}, 500

        filename = result.stdout.strip().split("Downloaded: ")[1] if "Downloaded:" in result.stdout else None
        if not filename:
            return {"error": "No filename returned"}, 500

        return {"status": "success", "filename": filename}
    except Exception as e:
        return {"error": str(e)}, 500

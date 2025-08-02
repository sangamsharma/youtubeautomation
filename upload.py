# upload.py
import os
from flask import jsonify, request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_short(request):
    data = request.get_json()
    filename = data.get("filename")
    if not filename or not os.path.exists(filename):
        return jsonify({"error": "Invalid file"}), 400

    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/youtube.upload"])
    youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {"title": "Auto-Generated Short", "description": "", "tags": ["Shorts"], "categoryId": "22"},
        "status": {"privacyStatus": "public"}
    }

    media = MediaFileUpload(filename, mimetype="video/mp4", resumable=True)
    req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = req.execute()

    return jsonify({"message": "Uploaded", "videoId": resp.get("id")})

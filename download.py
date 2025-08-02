# download.py
from flask import jsonify
from pytube import YouTube

def download_video(request):
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    out_path = "input.mp4"
    stream.download(filename=out_path)

    return jsonify({"message": "Downloaded", "filename": out_path})

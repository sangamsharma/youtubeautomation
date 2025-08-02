# clipper.py
import subprocess
import json
from flask import jsonify, request

def clip_video(request):
    data = request.get_json()
    clips_json = data.get("clips")
    if not clips_json:
        return jsonify({"error": "No clips JSON"}), 400

    clips = json.loads(clips_json)

    output_clips = []
    for idx, c in enumerate(clips):
        start = c["start"]
        end = c["end"]
        outfile = f"short_{idx}.mp4"
        subprocess.run([
            "ffmpeg", "-ss", str(start), "-i", "input.mp4", "-t", str(end - start),
            "-vf", "scale=1080:1920", "-c:v", "libx264", "-c:a", "aac", "-y", outfile
        ], check=True)
        output_clips.append(outfile)

    return jsonify({"message": "Clips created", "clips": output_clips})

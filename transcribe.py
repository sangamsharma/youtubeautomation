# transcribe.py
import whisper
from flask import jsonify

model = whisper.load_model("base")

def transcribe_audio(request):
    data = request.get_json()
    filename = data.get("filename")
    if not filename:
        return jsonify({"error": "No filename"}), 400

    result = model.transcribe(filename)
    transcript = result["text"]

    with open("transcript.txt", "w") as f:
        f.write(transcript)

    return jsonify({"message": "Transcribed", "transcript_file": "transcript.txt"})

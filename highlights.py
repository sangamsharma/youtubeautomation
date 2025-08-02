# highlights.py
import openai
from flask import jsonify, request

openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_highlights(request):
    data = request.get_json()
    transcript_file = data.get("transcript_file")
    if not transcript_file:
        return jsonify({"error": "No transcript path"}), 400

    with open(transcript_file) as f:
        transcript = f.read()

    prompt = f"Extract best moment timestamps from this transcript under 60s: {transcript}"

    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    clip_info = resp.choices[0].message["content"]

    return jsonify({"message": "Highlights extracted", "clips": clip_info})

from flask import Flask, request, jsonify
from download import download_video
from transcribe import transcribe_audio
from highlights import extract_highlights
from clipper import clip_video
from upload import upload_short

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def handle_download():
    return download_video(request)

@app.route('/transcribe', methods=['POST'])
def handle_transcribe():
    return transcribe_audio(request)

@app.route('/highlights', methods=['POST'])
def handle_highlights():
    return extract_highlights(request)

@app.route('/clip', methods=['POST'])
def handle_clip():
    return clip_video(request)

@app.route('/upload', methods=['POST'])
def handle_upload():
    return upload_short(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

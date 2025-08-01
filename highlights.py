# highlights.py - updated with pyannote speaker diarization
highlight_code = """
import os
from pyannote.audio import Pipeline
from moviepy.editor import VideoFileClip

# Configuration
VIDEO_PATH = "videos/input_video.mp4"
OUTPUT_DIR = "videos/clips"
MIN_DURATION = 3  # seconds

def extract_highlights(video_path, diarization_result, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    clip = VideoFileClip(video_path)
    speaker_idx = 0
    for turn, _, speaker in diarization_result.itertracks(yield_label=True):
        start, end = turn.start, turn.end
        duration = end - start
        if duration < MIN_DURATION:
            continue
        speaker_idx += 1
        filename = f"{output_dir}/speaker_{speaker_idx}_{speaker}_{int(start)}s_{int(end)}s.mp4"
        clip.subclip(start, end).write_videofile(filename, codec="libx264")
        print(f"Exported: {filename}")

if __name__ == "__main__":
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
    diarization = pipeline(VIDEO_PATH)
    extract_highlights(VIDEO_PATH, diarization, OUTPUT_DIR)
"""

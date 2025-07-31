import yt_dlp
import sys
import os

def download_video(youtube_url: str, output_path: str = "video.mp4"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
        'quiet': True,
        'noplaylist': True,
    }

    print(f"[INFO] Downloading video from: {youtube_url}")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"[SUCCESS] Downloaded video to {output_path}")
    except Exception as e:
        print(f"[ERROR] Failed to download video: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download.py <YouTube_URL>")
        sys.exit(1)

    url = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "video.mp4"

    # Remove existing file to avoid overwrite issues
    if os.path.exists(output):
        os.remove(output)

    download_video(url, output)

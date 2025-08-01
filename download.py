import sys
import yt_dlp
import os

if len(sys.argv) < 2:
    print("Usage: python download.py <youtube_url>")
    sys.exit(1)

youtube_url = sys.argv[1]
def download_video(url, output_dir="videos"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if not filename.endswith('.mp4'):
            filename = os.path.splitext(filename)[0] + '.mp4'
        print(f"Downloaded: {filename}")
        return filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download.py <youtube_url>")
        sys.exit(1)

    url = sys.argv[1]
    download_video(url)

import yt_dlp
import sys
import os

def ensure_download_folder(folder='downloads'):
	os.makedirs(folder, exist_ok=True)
	return folder

def download_url(url, download_folder):
	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'quiet': False,
		'noplaylist': False,
	}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("❌ Usage: python downloader.py <url_or_file.txt>")
		sys.exit(1)

	input_arg = sys.argv[1]
	folder = ensure_download_folder()

	if input_arg.endswith('.txt') and os.path.isfile(input_arg):
		with open(input_arg, 'r') as f:
			urls = [line.strip() for line in f if line.strip()]
		for url in urls:
			download_url(url, folder)
	else:
		download_url(input_arg, folder)

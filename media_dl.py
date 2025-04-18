import yt_dlp
import sys
import os
import requests
import datetime
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, USLT

WITH_LYRICS = '--with-lyrics' in sys.argv

def ensure_download_folder(folder='downloads'):
	os.makedirs(folder, exist_ok=True)
	return folder

def log_download(title, url, media_type, format, folder='downloads'):
	with open(os.path.join(folder, 'log.txt'), 'a') as log_file:
		now = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M]")
		log_file.write(f"{now} Downloaded ({media_type.upper()}, {format.upper()}): \"{title}\" from {url}\n")

def update_yt_dlp():
	os.system(f"{sys.executable} -m pip install --upgrade yt-dlp")
	print("✅ yt-dlp updated successfully.")
	sys.exit(0)

def list_formats_and_subtitles(url):
	ydl_opts = {'quiet': True}
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=False)
		formats = info.get('formats', [])
		subtitles = info.get('subtitles', {})
	return formats, subtitles, info

def extract_lyrics_text(subtitle_file):
	try:
		with open(subtitle_file, 'r', encoding='utf-8') as f:
			lines = f.readlines()
		lyrics = []
		for line in lines:
			if line.strip() == '' or '-->' in line or line.strip().isdigit():
				continue
			lyrics.append(line.strip())
		return '\n'.join(lyrics)
	except Exception as e:
		print(f"⚠️ Failed to process subtitles: {e}")
		return None

def embed_metadata(audio_path, title, artist, album, thumbnail_url, lyrics_text=None):
	try:
		audio = EasyID3(audio_path)
		audio['title'] = title
		audio['artist'] = artist
		audio['album'] = album
		audio.save()

		id3 = ID3(audio_path)
		if thumbnail_url:
			img_data = requests.get(thumbnail_url).content
			id3['APIC'] = APIC(
				encoding=3,
				mime='image/jpeg',
				type=3, desc=u'Cover',
				data=img_data
			)
		if lyrics_text:
			id3.add(USLT(encoding=3, lang='eng', desc='desc', text=lyrics_text))
		id3.save()
	except Exception as e:
		print(f"⚠️ Failed to embed metadata: {e}")

def download_audio(url, download_folder, audio_format='mp3', embed=True):
	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': audio_format,
			'preferredquality': '192',
		}],
		'writesubtitles': WITH_LYRICS,
		'subtitlesformat': 'vtt',
		'subtitleslangs': ['en'],
		'quiet': False,
	}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=True)
		filename = ydl.prepare_filename(info).rsplit('.', 1)[0] + f".{audio_format}"

		lyrics_text = None
		if WITH_LYRICS:
			subtitle_path = filename.rsplit('.', 1)[0] + '.en.vtt'
			if os.path.exists(subtitle_path):
				lyrics_text = extract_lyrics_text(subtitle_path)
				os.remove(subtitle_path)
			else:
				print("🎵 No lyrics available.")

		if embed and audio_format == 'mp3':
			embed_metadata(
				filename,
				info.get('title', 'Unknown Title'),
				info.get('uploader', 'Unknown Artist'),
				'Universal Media Downloader',
				info.get('thumbnail'),
				lyrics_text=lyrics_text
			)
		log_download(info.get('title', 'Unknown Title'), url, 'audio', audio_format)

def download_video(url, download_folder, quality, video_format='mp4', subtitles=False, sub_lang='en'):
	ydl_opts = {
		'format': f'bestvideo[height<={quality}]+bestaudio/best/best',
		'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
		'merge_output_format': video_format,
		'writesubtitles': subtitles,
		'subtitleslangs': [sub_lang] if subtitles else [],
		'quiet': False,
	}
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=True)
		log_download(info.get('title', 'Unknown Title'), url, 'video', video_format)

def safe_input(prompt, options):
	while True:
		response = input(prompt).strip().lower()
		if response in options:
			return response
		print(f"❌ Invalid input. Expected: {', '.join(options)}.")

def safe_number_input(prompt, max_val):
	while True:
		response = input(prompt).strip()
		if response.isdigit() and 1 <= int(response) <= max_val:
			return int(response)
		print(f"❌ Invalid number. Please choose between 1 and {max_val}.")

def process_url(url, download_folder, silent=False):
	formats, subtitles, info = list_formats_and_subtitles(url)
	title = info.get('title', 'Unknown Title')

	if silent:
		download_audio(url, download_folder)
		return

	print(f"\n🎬 Found content: {title}")
	print("❓ What do you want to download?")
	print("1 - Audio only")
	print("2 - Video only")
	print("3 - Video + Subtitles")
	print("4 - Skip this URL")
	choice = safe_input("Your choice (1/2/3/4): ", {'1', '2', '3', '4'})

	if choice == '1':
		print("Available formats: mp3, m4a, flac, opus, wav")
		audio_format = safe_input("Choose audio format: ", {'mp3', 'm4a', 'flac', 'opus', 'wav'})
		download_audio(url, download_folder, audio_format=audio_format)

	elif choice in {'2', '3'}:
		available_heights = sorted(set(f['height'] for f in formats if f.get('height')), reverse=True)
		print("Available qualities:")
		for idx, height in enumerate(available_heights):
			print(f"{idx+1} - {height}p")

		selected_quality = available_heights[safe_number_input("Choose quality (number): ", len(available_heights)) - 1]

		print("Available formats: mp4, mkv, webm")
		video_format = safe_input("Choose video format: ", {'mp4', 'mkv', 'webm'})

		subs = False
		lang = 'en'
		if choice == '3' and subtitles:
			print("Available subtitles:")
			sub_keys = list(subtitles.keys())
			for idx, lang_key in enumerate(sub_keys):
				print(f"{idx+1} - {lang_key}")
			lang = sub_keys[safe_number_input("Choose subtitle language (number): ", len(sub_keys)) - 1]
			subs = True

		download_video(url, download_folder, selected_quality, video_format=video_format, subtitles=subs, sub_lang=lang)

	else:
		print("⏩ Skipped.")

def main():
	if '--update' in sys.argv:
		update_yt_dlp()

	if len(sys.argv) < 2:
		print("❌ Usage: python media_dl.py <url_or_file.txt> [--silent] [--with-lyrics]")
		sys.exit(1)

	input_arg = sys.argv[1]
	silent_mode = '--silent' in sys.argv

	folder = ensure_download_folder()

	if input_arg.endswith('.txt') and os.path.isfile(input_arg):
		with open(input_arg, 'r') as f:
			urls = [line.strip() for line in f if line.strip()]
		for url in urls:
			process_url(url, folder, silent=silent_mode)
	else:
		process_url(input_arg, folder, silent=silent_mode)

if __name__ == "__main__":
	main()

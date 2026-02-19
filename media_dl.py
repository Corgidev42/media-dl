import yt_dlp
import sys
import os
import requests
import datetime
import json
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, USLT

# Couleurs pour l'interface
class Colors:
	RESET = '\033[0m'
	BOLD = '\033[1m'
	RED = '\033[91m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	BLUE = '\033[94m'
	MAGENTA = '\033[95m'
	CYAN = '\033[96m'
	WHITE = '\033[97m'
	BG_BLUE = '\033[44m'

# Configuration par défaut
DEFAULT_CONFIG = {
	'audio_format': 'mp3',
	'audio_quality': 'high',
	'video_format': 'mp4',
	'video_quality': 'high',
	'with_lyrics': False,
	'embed_metadata': True,
	'download_folder': 'downloads'
}

CONFIG_FILE = 'config.json'
WITH_LYRICS = '--with-lyrics' in sys.argv

# Presets de qualité
QUALITY_PRESETS = {
	'audio': {
		'low': {'bitrate': '128', 'name': 'Basse (128kbps)'},
		'medium': {'bitrate': '192', 'name': 'Moyenne (192kbps)'},
		'high': {'bitrate': '256', 'name': 'Haute (256kbps)'},
		'max': {'bitrate': '320', 'name': 'Maximale (320kbps)'}
	},
	'video': {
		'low': {'height': 480, 'name': '480p'},
		'medium': {'height': 720, 'name': '720p'},
		'high': {'height': 1080, 'name': '1080p'},
		'max': {'height': 2160, 'name': '4K (2160p)'}
	}
}

def print_header(text):
	"""Affiche un en-tête stylisé"""
	width = len(text) + 4
	print(f"\n{Colors.CYAN}{Colors.BOLD}{'=' * width}")
	print(f"  {text}  ")
	print(f"{'=' * width}{Colors.RESET}\n")

def print_success(text):
	"""Affiche un message de succès"""
	print(f"{Colors.GREEN}✅ {text}{Colors.RESET}")

def print_error(text):
	"""Affiche un message d'erreur"""
	print(f"{Colors.RED}❌ {text}{Colors.RESET}")

def print_info(text):
	"""Affiche un message d'information"""
	print(f"{Colors.BLUE}ℹ️  {text}{Colors.RESET}")

def print_warning(text):
	"""Affiche un avertissement"""
	print(f"{Colors.YELLOW}⚠️  {text}{Colors.RESET}")

def load_config():
	"""Charge la configuration depuis le fichier JSON"""
	if os.path.exists(CONFIG_FILE):
		try:
			with open(CONFIG_FILE, 'r') as f:
				config = json.load(f)
				return {**DEFAULT_CONFIG, **config}
		except:
			print_warning("Configuration corrompue, utilisation des valeurs par défaut")
	return DEFAULT_CONFIG.copy()

def save_config(config):
	"""Sauvegarde la configuration dans le fichier JSON"""
	try:
		with open(CONFIG_FILE, 'w') as f:
			json.dump(config, f, indent=2)
		print_success("Préférences sauvegardées")
	except Exception as e:
		print_error(f"Impossible de sauvegarder la configuration: {e}")

def ensure_download_folder(folder='downloads'):
	os.makedirs(folder, exist_ok=True)
	return folder

def log_download(title, url, media_type, format, folder='downloads'):
	with open(os.path.join(folder, 'log.txt'), 'a') as log_file:
		now = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M]")
		log_file.write(f"{now} Downloaded ({media_type.upper()}, {format.upper()}): \"{title}\" from {url}\n")

def update_yt_dlp():
	print_info("Mise à jour de yt-dlp...")
	os.system(f"{sys.executable} -m pip install --upgrade yt-dlp")
	print_success("yt-dlp mis à jour avec succès")
	sys.exit(0)

def progress_hook(d):
	"""Hook pour afficher la progression du téléchargement"""
	if d['status'] == 'downloading':
		try:
			percent = d.get('_percent_str', 'N/A').strip()
			speed = d.get('_speed_str', 'N/A').strip()
			eta = d.get('_eta_str', 'N/A').strip()
			
			# Barre de progression
			if '_percent_str' in d:
				percent_num = float(percent.replace('%', ''))
				bar_length = 40
				filled = int(bar_length * percent_num / 100)
				bar = '█' * filled + '░' * (bar_length - filled)
				print(f'\r{Colors.CYAN}[{bar}] {percent} | Vitesse: {speed} | ETA: {eta}{Colors.RESET}', end='', flush=True)
		except:
			pass
	elif d['status'] == 'finished':
		print(f'\n{Colors.GREEN}✓ Téléchargement terminé, traitement...{Colors.RESET}')

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

def download_audio(url, download_folder, audio_format='mp3', quality='high', embed=True):
	"""Télécharge l'audio avec la qualité spécifiée"""
	bitrate = QUALITY_PRESETS['audio'].get(quality, QUALITY_PRESETS['audio']['high'])['bitrate']
	
	print_info(f"Téléchargement en cours... (Format: {audio_format.upper()}, Qualité: {bitrate}kbps)")
	
	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': audio_format,
			'preferredquality': bitrate,
		}],
		'writesubtitles': WITH_LYRICS,
		'subtitlesformat': 'vtt',
		'subtitleslangs': ['en'],
		'quiet': True,
		'no_warnings': True,
		'progress_hooks': [progress_hook],
	}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		try:
			info = ydl.extract_info(url, download=True)
			filename = ydl.prepare_filename(info).rsplit('.', 1)[0] + f".{audio_format}"

			lyrics_text = None
			if WITH_LYRICS:
				subtitle_path = filename.rsplit('.', 1)[0] + '.en.vtt'
				if os.path.exists(subtitle_path):
					lyrics_text = extract_lyrics_text(subtitle_path)
					os.remove(subtitle_path)
					print_success("Paroles intégrées")
				else:
					print_warning("Aucune parole disponible")

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
			print_success(f"Audio téléchargé: {info.get('title', 'Unknown Title')}")
			return True
		except Exception as e:
			print_error(f"Erreur lors du téléchargement: {e}")
			return False

def download_video(url, download_folder, quality='high', video_format='mp4', subtitles=False, sub_lang='en'):
	"""Télécharge la vidéo avec la qualité spécifiée"""
	# Si quality est un preset, récupère la hauteur
	if quality in QUALITY_PRESETS['video']:
		height = QUALITY_PRESETS['video'][quality]['height']
		quality_name = QUALITY_PRESETS['video'][quality]['name']
	else:
		height = quality
		quality_name = f"{height}p"
	
	print_info(f"Téléchargement en cours... (Format: {video_format.upper()}, Qualité: {quality_name})")
	
	ydl_opts = {
		'format': f'bestvideo[height<={height}]+bestaudio/best/best',
		'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
		'merge_output_format': video_format,
		'writesubtitles': subtitles,
		'subtitleslangs': [sub_lang] if subtitles else [],
		'quiet': True,
		'no_warnings': True,
		'progress_hooks': [progress_hook],
	}
	
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		try:
			info = ydl.extract_info(url, download=True)
			log_download(info.get('title', 'Unknown Title'), url, 'video', video_format)
			print_success(f"Vidéo téléchargée: {info.get('title', 'Unknown Title')}")
			return True
		except Exception as e:
			print_error(f"Erreur lors du téléchargement: {e}")
			return False

def safe_input(prompt, options):
	"""Demande une entrée sécurisée avec validation"""
	while True:
		response = input(f"{Colors.YELLOW}{prompt}{Colors.RESET}").strip().lower()
		if response in options:
			return response
		print_error(f"Entrée invalide. Choix possibles : {', '.join(options)}")

def safe_number_input(prompt, max_val):
	"""Demande un nombre avec validation"""
	while True:
		response = input(f"{Colors.YELLOW}{prompt}{Colors.RESET}").strip()
		if response.isdigit() and 1 <= int(response) <= max_val:
			return int(response)
		print_error(f"Nombre invalide. Veuillez choisir entre 1 et {max_val}")

def show_quality_menu(media_type):
	"""Affiche le menu de sélection de qualité"""
	presets = QUALITY_PRESETS[media_type]
	print(f"\n{Colors.BOLD}Choisissez la qualité :{Colors.RESET}")
	options = list(presets.keys())
	for idx, key in enumerate(options, 1):
		print(f"  {Colors.CYAN}{idx}.{Colors.RESET} {presets[key]['name']}")
	
	choice = safe_number_input("Votre choix (1-4): ", len(options))
	return options[choice - 1]

def show_format_menu(media_type):
	"""Affiche le menu de sélection de format"""
	if media_type == 'audio':
		formats = ['mp3', 'm4a', 'flac', 'opus', 'wav']
		print(f"\n{Colors.BOLD}Choisissez le format audio :{Colors.RESET}")
	else:
		formats = ['mp4', 'mkv', 'webm']
		print(f"\n{Colors.BOLD}Choisissez le format vidéo :{Colors.RESET}")
	
	for idx, fmt in enumerate(formats, 1):
		print(f"  {Colors.CYAN}{idx}.{Colors.RESET} {fmt.upper()}")
	
	choice = safe_number_input(f"Votre choix (1-{len(formats)}): ", len(formats))
	return formats[choice - 1]

def show_main_menu():
	"""Affiche le menu principal"""
	print_header("📥 UNIVERSAL MEDIA DOWNLOADER")
	print(f"{Colors.BOLD}Que voulez-vous télécharger ?{Colors.RESET}\n")
	print(f"  {Colors.GREEN}1.{Colors.RESET} Audio seulement")
	print(f"  {Colors.GREEN}2.{Colors.RESET} Vidéo seulement")
	print(f"  {Colors.GREEN}3.{Colors.RESET} Vidéo avec sous-titres")
	print(f"  {Colors.GREEN}4.{Colors.RESET} Passer cette URL")
	print(f"  {Colors.GREEN}5.{Colors.RESET} Configurer les préférences")
	print()

def configure_preferences(config):
	"""Configure les préférences utilisateur"""
	print_header("⚙️  CONFIGURATION DES PRÉFÉRENCES")
	
	print(f"{Colors.BOLD}Configuration actuelle :{Colors.RESET}")
	print(f"  Audio: {config['audio_format'].upper()} - {QUALITY_PRESETS['audio'][config['audio_quality']]['name']}")
	print(f"  Vidéo: {config['video_format'].upper()} - {QUALITY_PRESETS['video'][config['video_quality']]['name']}")
	print(f"  Paroles: {'Oui' if config['with_lyrics'] else 'Non'}")
	print(f"  Métadonnées: {'Oui' if config['embed_metadata'] else 'Non'}")
	print()
	
	if safe_input("Modifier la configuration ? (o/n): ", {'o', 'n'}) == 'n':
		return config
	
	print("\n--- Audio par défaut ---")
	config['audio_quality'] = show_quality_menu('audio')
	config['audio_format'] = show_format_menu('audio')
	
	print("\n--- Vidéo par défaut ---")
	config['video_quality'] = show_quality_menu('video')
	config['video_format'] = show_format_menu('video')
	
	config['with_lyrics'] = safe_input("\nTélécharger les paroles quand disponibles ? (o/n): ", {'o', 'n'}) == 'o'
	config['embed_metadata'] = safe_input("Intégrer les métadonnées (pochette, artiste, etc.) ? (o/n): ", {'o', 'n'}) == 'o'
	
	save_config(config)
	print_success("Configuration sauvegardée !")
	return config

def process_url(url, download_folder, config, silent=False, batch_mode=False, batch_settings=None):
	"""Traite une URL avec les paramètres configurés"""
	try:
		formats, subtitles, info = list_formats_and_subtitles(url)
		title = info.get('title', 'Unknown Title')
	except Exception as e:
		print_error(f"Impossible d'extraire les informations de l'URL: {e}")
		return False

	if silent:
		return download_audio(url, download_folder, config['audio_format'], config['audio_quality'], config['embed_metadata'])

	print(f"\n{Colors.CYAN}{Colors.BOLD}🎬 Contenu trouvé:{Colors.RESET} {title}")
	
	# Mode batch : utilise les paramètres sauvegardés
	if batch_mode and batch_settings:
		if batch_settings['type'] == 'audio':
			return download_audio(url, download_folder, batch_settings['format'], batch_settings['quality'], config['embed_metadata'])
		else:
			return download_video(url, download_folder, batch_settings['quality'], batch_settings['format'], 
			                     batch_settings.get('subtitles', False), batch_settings.get('sub_lang', 'en'))
	
	# Mode interactif
	show_main_menu()
	choice = safe_input("Votre choix (1/2/3/4/5): ", {'1', '2', '3', '4', '5'})

	if choice == '5':
		config = configure_preferences(config)
		return process_url(url, download_folder, config, silent, batch_mode, batch_settings)
	
	if choice == '4':
		print_info("URL ignorée")
		return True

	if choice == '1':
		quality = show_quality_menu('audio')
		audio_format = show_format_menu('audio')
		return download_audio(url, download_folder, audio_format, quality, config['embed_metadata'])

	elif choice in {'2', '3'}:
		quality = show_quality_menu('video')
		video_format = show_format_menu('video')

		subs = False
		lang = 'en'
		if choice == '3' and subtitles:
			print(f"\n{Colors.BOLD}Sous-titres disponibles :{Colors.RESET}")
			sub_keys = list(subtitles.keys())
			for idx, lang_key in enumerate(sub_keys, 1):
				print(f"  {Colors.CYAN}{idx}.{Colors.RESET} {lang_key}")
			lang = sub_keys[safe_number_input(f"Choix (1-{len(sub_keys)}): ", len(sub_keys)) - 1]
			subs = True
		elif choice == '3':
			print_warning("Aucun sous-titre disponible pour ce contenu")

		return download_video(url, download_folder, quality, video_format, subtitles=subs, sub_lang=lang)
	
	return False

def main():
	"""Fonction principale"""
	if '--update' in sys.argv:
		update_yt_dlp()

	if len(sys.argv) < 2 or '--help' in sys.argv:
		print_header("📥 UNIVERSAL MEDIA DOWNLOADER")
		print(f"{Colors.BOLD}Usage:{Colors.RESET}")
		print(f"  python media_dl.py <url_ou_fichier.txt> [options]")
		print(f"\n{Colors.BOLD}Options:{Colors.RESET}")
		print(f"  --silent        Mode silencieux (télécharge sans interaction)")
		print(f"  --with-lyrics   Télécharge et intègre les paroles")
		print(f"  --batch         Mode batch (même choix pour toutes les URLs)")
		print(f"  --update        Met à jour yt-dlp")
		print(f"  --config        Configure les préférences par défaut")
		print(f"  --help          Affiche cette aide")
		print()
		sys.exit(0 if '--help' in sys.argv else 1)

	# Chargement de la configuration
	config = load_config()
	
	# Configuration interactive si demandée
	if '--config' in sys.argv:
		configure_preferences(config)
		sys.exit(0)

	input_arg = sys.argv[1]
	silent_mode = '--silent' in sys.argv
	batch_mode = '--batch' in sys.argv

	folder = ensure_download_folder(config['download_folder'])

	# Traitement des URLs
	if input_arg.endswith('.txt') and os.path.isfile(input_arg):
		with open(input_arg, 'r') as f:
			urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
		
		if not urls:
			print_error("Aucune URL trouvée dans le fichier")
			sys.exit(1)
		
		print_info(f"{len(urls)} URL(s) détectée(s)")
		
		# Mode batch : demande la configuration une fois
		batch_settings = None
		if batch_mode and not silent_mode and len(urls) > 1:
			print_info("Mode batch activé - Les mêmes paramètres seront appliqués à toutes les URLs")
			print(f"\n{Colors.BOLD}Type de téléchargement :{Colors.RESET}")
			print(f"  {Colors.CYAN}1.{Colors.RESET} Audio")
			print(f"  {Colors.CYAN}2.{Colors.RESET} Vidéo")
			print(f"  {Colors.CYAN}3.{Colors.RESET} Vidéo avec sous-titres")
			
			batch_choice = safe_input("Votre choix (1/2/3): ", {'1', '2', '3'})
			
			if batch_choice == '1':
				quality = show_quality_menu('audio')
				fmt = show_format_menu('audio')
				batch_settings = {'type': 'audio', 'quality': quality, 'format': fmt}
			else:
				quality = show_quality_menu('video')
				fmt = show_format_menu('video')
				batch_settings = {
					'type': 'video',
					'quality': quality,
					'format': fmt,
					'subtitles': batch_choice == '3',
					'sub_lang': 'en'
				}
			
			print_success(f"Configuration batch enregistrée pour {len(urls)} URL(s)")
		
		# Téléchargement de toutes les URLs
		success_count = 0
		for idx, url in enumerate(urls, 1):
			print(f"\n{Colors.MAGENTA}{Colors.BOLD}[{idx}/{len(urls)}]{Colors.RESET}")
			if process_url(url, folder, config, silent_mode, batch_mode, batch_settings):
				success_count += 1
		
		print(f"\n{Colors.GREEN}{Colors.BOLD}═══════════════════════════════════{Colors.RESET}")
		print_success(f"Téléchargements terminés : {success_count}/{len(urls)} réussis")
		
	else:
		# URL unique
		process_url(input_arg, folder, config, silent_mode)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print(f"\n\n{Colors.YELLOW}Interruption par l'utilisateur{Colors.RESET}")
		sys.exit(0)
	except Exception as e:
		print_error(f"Erreur inattendue: {e}")
		sys.exit(1)

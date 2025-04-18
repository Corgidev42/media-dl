# 🕷 Universal Music Downloader (YouTube + SoundCloud)

## 📌 Description

**Universal Music Downloader** est un outil Python pour télécharger de la musique depuis **YouTube**, **SoundCloud**, ou **des playlists entières**, avec conversion automatique en MP3.

---

## 🎮 Features

- 🎵 Supporte SoundCloud et YouTube
- 📄 Télécharge une musique ou une playlist entière
- 🎧 Conversion automatique en MP3 (192 kbps)
- 📂 Organisation dans un dossier `downloads/`
- ⚙️ Utilisation ultra simple : `make run`

---

## 🛠 Requirements

- Python 3
- `ffmpeg` installé

### Installer ffmpeg

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

---

## ▶️ Usage

1. Mettez toutes vos URLs dans `urls.txt`, une par ligne.

```
https://soundcloud.com/user/track1
https://youtube.com/watch?v=track2
...
```

2. Lancez le téléchargement :
```bash
make run
```

Les fichiers MP3 seront enregistrés dans le dossier `downloads/`.

---

## 📂 Structure

```
universal-music-downloader/
├── downloader.py
├── Makefile
├── README.md
├── .gitignore
├── urls.txt
├── downloads/
```

---

## 👤 Author

- Vincent B. (vbonnard.dev@gmail.com)

---

## 📜 License & Disclaimer

For personal and educational use only.
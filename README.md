# 🎵 Universal Media Downloader - `media-dl`

## 📌 Description

**Universal Media Downloader** is a professional-grade tool for downloading audio and video content from YouTube, SoundCloud, and any platform supported by `yt-dlp`.

- Automatic download of playlists or single files.
- Choose your preferred audio and video formats.
- Automatically embeds cover art, artist, and album metadata into MP3 files.
- Optionally embed lyrics if available using `--with-lyrics`.
- Interactive mode **or** ultra-fast silent mode.
- Fully compatible with Linux / macOS / Windows (Python 3.7+).

---

## 🔧 Installation

```bash
make all
```

This will:
- Create a Python virtual environment `.venv`
- Install all required dependencies automatically (`yt-dlp`, `mutagen`, `requests`)

---

## 🔄 Update `yt-dlp`

```bash
make update
```
- Easily update `yt-dlp` to the latest version without breaking the project.

---

## ▶️ Usage

### 1. Interactive Mode (manual choice)

```bash
make run
```

- For each URL listed in `urls.txt`, you can choose:
  - Audio only (choose the format: mp3, m4a, flac, opus, wav)
  - Video only (choose the quality: 1080p, 720p, etc.)
  - Video + Subtitles (choose the language)

### 2. Silent Mode (automatic download)

```bash
make silent
```

- Automatically downloads everything as MP3 or MP4 without any prompts.
- `downloads/` folder is created automatically.

### 3. With Lyrics (optional)

```bash
make run ARGS="--with-lyrics"
```
or
```bash
make silent ARGS="--with-lyrics"
```

- Fetches and embeds subtitles as lyrics into the MP3 if available.

---

## 📂 Project Structure

```
media-dl/
├── Makefile
├── media_dl.py
├── urls.txt         # List of URLs to download
├── downloads/
│   ├── *.mp3 / *.mp4
│   └── log.txt      # Download history
└── README.md
```

---

## 📁 Available Commands

| Command | Description |
|:---|:---|
| `make all` | Create the virtual environment and install dependencies |
| `make run` | Run the downloader in interactive mode |
| `make silent` | Run the downloader in silent mode |
| `make update` | Update yt-dlp |
| `make clean` | Remove only the virtual environment |
| `make fclean` | Remove the virtual environment and downloads folder |
| `make re` | Full clean and reinstall |
| `make help` | Display the available commands |

---

## 🛠️ Supported Options

| Option | Effect |
|:------|:------|
| `--silent` | No user interaction, automatic mode |
| `--with-lyrics` | Download and embed lyrics into MP3 if available |
| `--update` | Update `yt-dlp` easily |

---

## 👤 Author

- **Project developed by** Vincent B.
- Contact: [vbonnard.dev@gmail.com](mailto:vbonnard.dev@gmail.com)

---

## 🗓 License

**For personal and educational use only.**
Not affiliated with YouTube, SoundCloud, or any other platform.

---

# ✅ Ready to use and fully operational.

---

# 📣 Professional Notes
- **Audio formats** supported: `mp3`, `m4a`, `flac`, `opus`, `wav`
- **Video formats** supported: `mp4`, `mkv`, `webm`
- **`downloads/` folder** is auto-created if missing
- **Automatic logging** of all downloads in `downloads/log.txt`

---

Enjoy your downloading experience!


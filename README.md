# 🎧 Universal Media Downloader - `media-dl`

## 📌 Description

**Universal Media Downloader** est un outil professionnel pour télécharger facilement de l'audio et de la vidéo depuis YouTube, SoundCloud et d'autres plateformes supportées par `yt-dlp`.

- Téléchargement automatique de playlists ou de fichiers uniques.
- Format audio et vidéo au choix.
- Incrustation automatique de la pochette, artiste, album dans les fichiers MP3.
- Option d'incruster les paroles si disponibles via `--with-lyrics`.
- Mode interactif **ou** mode silencieux ultra-rapide.
- Compatible Linux / macOS / Windows (avec Python 3).

---

## 🔧 Installation

```bash
make all
```

Cela va :
- Créer un environnement virtuel Python.
- Installer toutes les dépendances automatiquement (`yt-dlp`, `mutagen`, `requests`).

---

## 🔄 Mise à jour de `yt-dlp`

```bash
make update
```

---

## ▶️ Utilisation

### 1. Mode Interactif

```bash
make run
```

- Le programme te proposera de choisir pour chaque URL :
  - Audio seulement (avec choix du format)
  - Vidéo seulement (avec choix de qualité)
  - Vidéo + Sous-titres (avec choix de langue)

**Exemple :**
- Dossier `downloads/` créé automatiquement.
- Logs complets disponibles dans `downloads/log.txt`.

### 2. Mode Silencieux (rapide)

```bash
make silent
```

- Tout sera téléchargé en MP3 par défaut sans aucune question.

### 3. Mode Avec Paroles Incrustées (optionnel)

```bash
make run ARGS="--with-lyrics"
```

- Cherche automatiquement les sous-titres.
- Les nettoie et les intègre dans le fichier MP3 si disponibles.

---

## 📂 Structure du projet

```
media-dl/
├── Makefile
├── media_dl.py
├── urls.txt (liste d'URLs à télécharger)
└── downloads/
    ├── *.mp3 / *.mp4
    └── log.txt
```

---

## 👀 Options Supportées

| Option | Effet |
|:------|:------|
| `--silent` | Mode silencieux, pas d'interaction. |
| `--with-lyrics` | Télécharge et incruste les paroles si disponibles. |
| `--update` | Met à jour automatiquement `yt-dlp`. |

---

## 👤 Auteur

- **Projet par** Vincent B.
- Contact : [vbonnard.dev@gmail.com](mailto:vbonnard.dev@gmail.com)

---

## 📅 Licence

Projet open-source pour un usage personnel et éducatif uniquement.

**Not affiliated with YouTube, SoundCloud, or any other platform.**


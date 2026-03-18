# 📥 StreamGrab

**StreamGrab** (anciennement Universal Media Downloader) est un outil professionnel de téléchargement de contenu audio et vidéo, supportant YouTube, SoundCloud, Twitch (VOD/Clips) et toutes les plateformes compatibles avec `yt-dlp`.

---

## ⚡ Démarrage Rapide

### 1. Installation

```bash
make all
```

Cela crée l'environnement virtuel et installe les dépendances nécessaires (`yt-dlp`, `mutagen`, `requests`).

### 2. Utilisation Simple

Ajoutez vos liens dans `urls.txt` (un par ligne) :
```text
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.twitch.tv/videos/123456789
```

Lancez le téléchargement interactif :
```bash
make run
```

---

## ✨ Fonctionnalités Principales

- 🎨 **Interface Moderne** : Menus colorés, barres de progression, et navigation intuitive.
- 🔐 **Support Twitch Avancé** : Téléchargement de VODs abonnés via cookies (Brave, Chrome, Firefox, etc.).
- 🚀 **Mode Batch** : Appliquez les mêmes paramètres à une liste d'URLs.
- 🎵 **Audio & Métadonnées** : Conversion MP3/M4A/FLAC avec intégration automatique des pochettes et tags.
- 📝 **Paroles** : Téléchargement optionnel des paroles intégrées.
- ⚙️ **Configuration Persistante** : Sauvegarde de vos préférences (qualité, format, dossier).
- 🗑️ **Liste auto-nettoyante** : Chaque URL traitée (téléchargée ou ignorée) est automatiquement supprimée de `urls.txt`.

---

## 🎮 Configuration Twitch (VOD Abonnés)

Pour télécharger des contenus réservés aux abonnés Twitch, StreamGrab utilise les cookies de votre navigateur :

1. Lancez la configuration :
   ```bash
   make config
   ```
2. Allez dans le menu **Twitch**.
3. Sélectionnez votre navigateur (ex: **Brave**, **Chrome**, **Firefox**).
4. Assurez-vous d'être connecté à Twitch sur ce navigateur.
5. Lancez vos téléchargements normalement !

---

## 📖 Guide d'Utilisation

### Commandes Principales

| Commande | Description |
|:---|:---|
| `make run` | Mode interactif (choix par URL) |
| `make batch` | Mode batch (mêmes réglages pour tout) |
| `make silent` | Mode automatique (utilise la config sauvegardée) |
| `make config` | Modifier les préférences et l'authentification |
| `make update` | Mettre à jour `yt-dlp` |
| `make help` | Voir toutes les commandes |

### Exemples

**Télécharger une playlist musicale :**
```bash
make batch
# Choisissez "Audio" -> "MP3" -> "Haute"
```

**Télécharger automatiquement sans questions :**
```bash
make silent
```

**Avec les paroles :**
```bash
make run-lyrics
```

---

## 📂 Structure du Projet

```
streamgrab/
├── Makefile         # Commandes simplifiées
├── streamgrab.py    # Script principal
├── config.json      # Vos préférences (généré aut.)
├── urls.txt         # Liste des liens à télécharger
├── downloads/       # Dossier de destination
├── CHANGELOG.md     # Historique des versions
└── README.md        # Documentation
```

---

## 🛠️ Options Avancées

Vous pouvez aussi utiliser le script directement avec python :
```bash
source .venv/bin/activate
python streamgrab.py urls.txt --silent --batch
```


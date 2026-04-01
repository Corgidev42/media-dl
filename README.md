# 📥 StreamGrab

**StreamGrab** (anciennement Universal Media Downloader) est un outil professionnel de téléchargement de contenu audio et vidéo, supportant YouTube, SoundCloud, Twitch (VOD/Clips) et toutes les plateformes compatibles avec `yt-dlp`.

---

## ⚡ Démarrage Rapide

### 1. Installation

```bash
make all
```

Cela crée l'environnement virtuel et installe les dépendances (`yt-dlp[default]` inclut les scripts EJS pour YouTube, `mutagen`, `requests`).

**YouTube (obligatoire sur la machine) :** installez aussi un moteur JavaScript, par exemple [Deno](https://docs.deno.com/runtime/getting_started/installation/) (recommandé par yt-dlp) :

```bash
brew install deno
```

Sans cela, vous pouvez voir des erreurs du type « Signature solving failed » ou « Only images are available ».

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

## 🎮 Cookies navigateur (Twitch, YouTube privé)

Le même réglage sert aux **VOD Twitch réservés aux abonnés** et aux **vidéos YouTube privées / restreintes** (vous devez y avoir accès avec votre compte) : yt-dlp lit les cookies du navigateur choisi.

1. Lancez la configuration :
   ```bash
   make config
   ```
2. Choisissez **Navigateur (Twitch / YouTube privé)**.
3. Sélectionnez le navigateur où vous êtes connecté (ex. **Brave**, **Chrome**, **Firefox**).
4. Restez connecté à **Twitch** et/ou **YouTube** dans ce navigateur.
5. Relancez vos téléchargements.

**Dépannage YouTube :** si vous voyez « Signature solving failed » ou « Only images are available », installez **Deno** (voir section Démarrage rapide) et réexécutez `make install` pour avoir `yt-dlp[default]`. Détails : [wiki EJS yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/EJS).

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


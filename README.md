# 🎵 Universal Media Downloader - `media-dl`

## 📌 Description

**Universal Media Downloader** est un outil professionnel de téléchargement de contenu audio et vidéo depuis YouTube, SoundCloud et toutes les plateformes supportées par `yt-dlp`.

### ✨ Fonctionnalités principales

- 🎨 **Interface utilisateur fluide** avec menus colorés et intuitifs
- ⚙️ **Système de préférences** pour sauvegarder vos choix
- 📊 **Barre de progression** en temps réel avec vitesse et ETA
- 🎯 **Presets de qualité** simplifiés (Basse, Moyenne, Haute, Maximale)
- 🚀 **Mode batch intelligent** pour appliquer les mêmes paramètres à plusieurs URLs
- 🎵 **Support des paroles** (optionnel) intégrées dans les fichiers MP3
- 🖼️ **Métadonnées automatiques** : pochette d'album, artiste, titre
- 📝 **Journal de téléchargement** détaillé
- 🌐 Entièrement compatible Linux / macOS / Windows (Python 3.7+)

---

## 🔧 Installation

```bash
make all
```

Cette commande va :
- Créer un environnement virtuel Python `.venv`
- Installer automatiquement toutes les dépendances (`yt-dlp`, `mutagen`, `requests`)

---

## 🔄 Mise à jour de `yt-dlp`

```bash
make update
```
Met à jour `yt-dlp` vers la dernière version disponible.

---

## ▶️ Utilisation

### 1. Mode Interactif (par défaut)

```bash
make run
```

Pour chaque URL dans `urls.txt`, vous pouvez choisir :
- **Audio seulement** avec choix de :
  - Qualité : Basse (128kbps), Moyenne (192kbps), Haute (256kbps), Maximale (320kbps)
  - Format : MP3, M4A, FLAC, OPUS, WAV
- **Vidéo seulement** avec choix de :
  - Qualité : 480p, 720p, 1080p, 4K
  - Format : MP4, MKV, WEBM
- **Vidéo + Sous-titres** avec sélection de la langue

### 2. Mode Batch Intelligent

```bash
make batch
```

**Nouveau !** Configurez une fois, appliquez à toutes les URLs :
- Définissez vos paramètres (qualité, format) au début
- Tous les téléchargements utilisent automatiquement ces paramètres
- Idéal pour télécharger plusieurs vidéos/musiques avec les mêmes réglages

### 3. Mode Silencieux (automatique)

```bash
make silent
```

Télécharge automatiquement tous les contenus en utilisant vos préférences par défaut.
- Aucune interaction requise
- Utilise la configuration sauvegardée

### 4. Configuration des Préférences

```bash
make config
```

Configurez vos préférences par défaut :
- Format audio/vidéo préféré
- Qualité par défaut
- Téléchargement automatique des paroles
- Intégration des métadonnées

Les préférences sont sauvegardées dans `config.json` et réutilisées automatiquement.

### 5. Avec Paroles (optionnel)

```bash
make run-lyrics
```
ou
```bash
make silent-lyrics
```

Télécharge et intègre les paroles (sous-titres) dans les fichiers MP3 quand disponibles.

---

## 📂 Structure du Projet

```
media-dl/
├── Makefile
├── media_dl.py      # Script principal amélioré
├── config.json      # Configuration personnalisée (créé automatiquement)
├── urls.txt         # Liste des URLs à télécharger
├── downloads/
│   ├── *.mp3 / *.mp4
│   └── log.txt      # Historique des téléchargements
└── README.md
```

---

## 📁 Commandes Disponibles

| Commande | Description |
|:---|:---|
| `make all` | Créer l'environnement virtuel et installer les dépendances |
| `make run` | Lancer le téléchargeur en mode interactif |
| `make batch` | Lancer en mode batch intelligent (mêmes paramètres pour toutes les URLs) |
| `make silent` | Lancer en mode silencieux (utilise les préférences) |
| `make config` | Configurer les préférences par défaut |
| `make run-lyrics` | Mode interactif avec paroles |
| `make silent-lyrics` | Mode silencieux avec paroles |
| `make update` | Mettre à jour yt-dlp |
| `make clean` | Supprimer uniquement l'environnement virtuel |
| `make fclean` | Supprimer l'environnement virtuel et le dossier downloads |
| `make re` | Nettoyage complet et réinstallation |
| `make help` | Afficher l'aide des commandes |

---

## 🛠️ Options de Ligne de Commande

| Option | Effet |
|:------|:------|
| `--silent` | Mode automatique sans interaction utilisateur |
| `--with-lyrics` | Télécharge et intègre les paroles dans les MP3 |
| `--batch` | Mode batch : mêmes paramètres pour toutes les URLs |
| `--config` | Configure les préférences par défaut |
| `--update` | Met à jour yt-dlp facilement |
| `--help` | Affiche l'aide complète |

---

## 💡 Exemples d'Utilisation

### Télécharger une seule vidéo en mode interactif
```bash
python media_dl.py "https://www.youtube.com/watch?v=..."
```

### Télécharger plusieurs URLs avec les mêmes paramètres
```bash
python media_dl.py urls.txt --batch
```

### Télécharger en mode silencieux avec paroles
```bash
python media_dl.py urls.txt --silent --with-lyrics
```

### Configurer les préférences
```bash
python media_dl.py --config
```

---

## 🎨 Aperçu de l'Interface

Le script offre une interface colorée et intuitive avec :
- ✅ Messages de succès en vert
- ❌ Messages d'erreur en rouge
- ℹ️ Informations en bleu
- ⚠️ Avertissements en jaune
- 📊 Barre de progression en temps réel
- 🎯 Menus numérotés faciles à utiliser

---

## 📝 Format du Fichier URLs

Le fichier `urls.txt` peut contenir :
```text
# Ceci est un commentaire (ignoré)
https://www.youtube.com/watch?v=...
https://soundcloud.com/...

# Une autre vidéo
https://www.youtube.com/watch?v=...
```

- Une URL par ligne
- Les lignes vides sont ignorées
- Les lignes commençant par `#` sont des commentaires

---

## 🔍 Qualités Disponibles

### Audio
- **Basse** : 128 kbps (idéal pour les podcasts)
- **Moyenne** : 192 kbps (bon compromis)
- **Haute** : 256 kbps (très bonne qualité)
- **Maximale** : 320 kbps (qualité audiophile)

### Vidéo
- **Basse** : 480p (économise l'espace disque)
- **Moyenne** : 720p HD (recommandé)
- **Haute** : 1080p Full HD (excellente qualité)
- **Maximale** : 4K 2160p (meilleure qualité disponible)

---

## 👤 Auteur

- **Projet développé par** Vincent B.
- Contact: [vbonnard.dev@gmail.com](mailto:vbonnard.dev@gmail.com)

---

## 🗓 Licence

**Pour usage personnel et éducatif uniquement.**
Non affilié à YouTube, SoundCloud ou toute autre plateforme.

---

## 📣 Notes Professionnelles

- **Formats audio** supportés : `mp3`, `m4a`, `flac`, `opus`, `wav`
- **Formats vidéo** supportés : `mp4`, `mkv`, `webm`
- **Dossier `downloads/`** créé automatiquement si manquant
- **Journal automatique** de tous les téléchargements dans `downloads/log.txt`
- **Configuration** sauvegardée dans `config.json`
- **Barre de progression** affiche vitesse de téléchargement et temps restant
- **Gestion d'erreurs** robuste avec messages clairs

---

## 🚀 Nouveautés de cette Version

### ✨ Améliorations UX
- Interface colorée et intuitive
- Menus simplifiés avec navigation numérique
- Barre de progression en temps réel
- Messages d'erreur plus clairs

### ⚙️ Nouvelles Fonctionnalités
- Système de configuration persistante
- Presets de qualité simplifiés
- Mode batch intelligent
- Validation des entrées améliorée
- Support des commentaires dans urls.txt

### 🎯 Optimisations
- Gestion d'erreurs améliorée
- Interruption propre avec Ctrl+C
- Messages multilingues (français)
- Récapitulatif de fin de téléchargement

---

# ✅ Prêt à l'emploi et entièrement opérationnel !

Profitez de votre expérience de téléchargement améliorée ! 🎉


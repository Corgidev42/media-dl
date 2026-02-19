# 📖 Guide d'Utilisation et Exemples

## 🚀 Démarrage Rapide

### Installation initiale
```bash
# Cloner ou télécharger le projet
cd media-dl

# Installer les dépendances
make all

# Afficher l'aide
make help
```

---

## 📝 Préparer vos URLs

Éditez le fichier `urls.txt` pour ajouter vos URLs :

```text
# Mes musiques préférées
https://www.youtube.com/watch?v=dQw4w9WgXcQ

# Playlist de cours
https://www.youtube.com/watch?v=AbCdEfGhIjK

# Podcast
https://soundcloud.com/user/track-name
```

**Conseils :**
- Une URL par ligne
- Utilisez `#` pour des commentaires
- Les lignes vides sont ignorées

---

## 🎯 Scénarios d'Utilisation

### Scénario 1 : Télécharger une playlist musicale
```bash
# 1. Ajoutez toutes les URLs dans urls.txt
# 2. Lancez le mode batch pour des paramètres uniformes
make batch

# 3. Choisissez :
#    - Type : Audio (1)
#    - Qualité : Haute - 256kbps (3)
#    - Format : MP3 (1)
```

**Résultat** : Tous les morceaux téléchargés en MP3 haute qualité avec métadonnées.

---

### Scénario 2 : Télécharger des vidéos de cours
```bash
# 1. Ajoutez les URLs des cours dans urls.txt
# 2. Mode batch pour appliquer les mêmes paramètres
make batch

# 3. Choisissez :
#    - Type : Vidéo (2)
#    - Qualité : 720p (2)
#    - Format : MP4 (1)
```

**Résultat** : Vidéos en 720p, optimales pour l'apprentissage.

---

### Scénario 3 : Téléchargement automatique quotidien
```bash
# 1. Configurez vos préférences par défaut
make config

# 2. Choisissez vos paramètres préférés
#    (ils seront sauvegardés dans config.json)

# 3. Ensuite, utilisez simplement :
make silent

# Pas de questions posées, tout est automatique !
```

**Résultat** : Téléchargement automatisé avec vos préférences.

---

### Scénario 4 : Télécharger avec paroles pour karaoké
```bash
# Pour un fichier interactif
make run-lyrics

# Ou en mode silent si configuré
make silent-lyrics
```

**Résultat** : MP3 avec paroles intégrées (visible dans les lecteurs supportant les paroles).

---

## ⚙️ Configuration Avancée

### Modifier config.json manuellement

Après la première configuration, vous pouvez éditer `config.json` :

```json
{
  "audio_format": "flac",
  "audio_quality": "max",
  "video_format": "mkv",
  "video_quality": "high",
  "with_lyrics": true,
  "embed_metadata": true,
  "download_folder": "downloads"
}
```

**Options disponibles :**
- `audio_quality` : `low`, `medium`, `high`, `max`
- `video_quality` : `low`, `medium`, `high`, `max`
- `audio_format` : `mp3`, `m4a`, `flac`, `opus`, `wav`
- `video_format` : `mp4`, `mkv`, `webm`

---

## 🎨 Interface Utilisateur

### Menu Principal
```
═══════════════════════════════════
  📥 UNIVERSAL MEDIA DOWNLOADER  
═══════════════════════════════════

Que voulez-vous télécharger ?

  1. Audio seulement
  2. Vidéo seulement
  3. Vidéo avec sous-titres
  4. Passer cette URL
  5. Configurer les préférences
```

### Barre de Progression
```
[████████████████████░░░░░░░░░░░░] 65.3% | Vitesse: 2.5MB/s | ETA: 00:15
✓ Téléchargement terminé, traitement...
✅ Audio téléchargé: Nom de la vidéo
```

---

## 🔧 Résolution de Problèmes

### Le téléchargement échoue
```bash
# Vérifiez que yt-dlp est à jour
make update

# Relancez le téléchargement
make run
```

### Erreur de format non disponible
- Essayez un autre format (MKV au lieu de MP4 par exemple)
- Choisissez une qualité inférieure

### Les paroles ne s'intègrent pas
- Les paroles ne sont disponibles que si la vidéo a des sous-titres
- Vérifiez que le format cible est MP3
- Assurez-vous que `mutagen` est installé : `pip install mutagen`

---

## 💡 Astuces Pro

### 1. Téléchargement en arrière-plan
```bash
# Lancez en arrière-plan (Linux/macOS)
nohup make silent &

# Vérifiez la progression
tail -f downloads/log.txt
```

### 2. Télécharger une URL spécifique directement
```bash
python media_dl.py "https://youtube.com/watch?v=..." --batch
```

### 3. Organiser vos téléchargements
Créez différents fichiers d'URLs :
- `music.txt` pour la musique
- `podcasts.txt` pour les podcasts
- `videos.txt` pour les vidéos

Puis :
```bash
python media_dl.py music.txt --batch
```

### 4. Qualité automatique optimale
Configurez `max` pour audio et `high` (1080p) pour vidéo :
```bash
make config
# Choisissez max/high
# Puis utilisez toujours :
make silent
```

---

## 📊 Comparaison des Qualités

### Audio

| Qualité | Bitrate | Taille (5 min) | Usage recommandé |
|---------|---------|----------------|------------------|
| Basse | 128 kbps | ~5 MB | Podcasts, voix |
| Moyenne | 192 kbps | ~7 MB | Usage quotidien |
| Haute | 256 kbps | ~9 MB | Musique de qualité |
| Maximale | 320 kbps | ~12 MB | Audiophiles, archivage |

### Vidéo

| Qualité | Résolution | Taille (5 min) | Usage recommandé |
|---------|------------|----------------|------------------|
| Basse | 480p | ~50 MB | Économie d'espace |
| Moyenne | 720p HD | ~150 MB | Streaming, partage |
| Haute | 1080p FHD | ~300 MB | Visionnage haute qualité |
| Maximale | 4K 2160p | ~1 GB | Archivage, grand écran |

---

## 🎓 Workflows Recommandés

### Workflow 1 : Collectionneur de musique
1. `make config` → Configurer en FLAC/Max quality
2. Ajouter URLs dans `urls.txt`
3. `make batch` → Télécharger tout en batch
4. Organiser manuellement après téléchargement

### Workflow 2 : Étudiant
1. `make config` → MP4/720p par défaut
2. Mode interactif pour choisir au cas par cas
3. `make run` → Choisir vidéo/sous-titres selon besoin

### Workflow 3 : Archiviste
1. `make config` → Formats sans perte (FLAC/MKV/Max)
2. `make silent-lyrics` → Tout télécharger automatiquement
3. Vérifier `downloads/log.txt` pour l'historique

---

## 📞 Support

Pour tout problème :
1. Vérifiez que yt-dlp est à jour : `make update`
2. Consultez `downloads/log.txt` pour les erreurs
3. Vérifiez votre connexion internet
4. Contactez : vbonnard.dev@gmail.com

---

**Bon téléchargement ! 🎉**

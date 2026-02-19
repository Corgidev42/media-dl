# 📋 Changelog - Universal Media Downloader

## Version 2.0.0 - Février 2026 🎉

### ✨ Nouvelles Fonctionnalités Majeures

#### 🎨 Interface Utilisateur Complètement Refaite
- **Interface colorée et intuitive** avec codes couleurs clairs :
  - ✅ Vert pour les succès
  - ❌ Rouge pour les erreurs
  - ℹ️ Bleu pour les informations
  - ⚠️ Jaune pour les avertissements
- **Menus numérotés** pour une navigation simple et rapide
- **En-têtes stylisés** pour une meilleure lisibilité
- **Messages en français** pour une meilleure compréhension

#### ⚙️ Système de Configuration Persistante
- **Fichier config.json** pour sauvegarder vos préférences
- **Commande `make config`** pour configurer interactivement
- **Préférences par défaut** appliquées automatiquement en mode silencieux
- Configuration modifiable manuellement dans `config.json`

#### 🎯 Presets de Qualité Simplifiés
**Audio** :
- Basse : 128 kbps (podcasts, voix)
- Moyenne : 192 kbps (usage quotidien)
- Haute : 256 kbps (musique de qualité)
- Maximale : 320 kbps (audiophiles)

**Vidéo** :
- Basse : 480p (économie d'espace)
- Moyenne : 720p HD (recommandé)
- Haute : 1080p Full HD (excellente qualité)
- Maximale : 4K 2160p (meilleure qualité)

#### 📊 Barre de Progression en Temps Réel
- **Affichage visuel** avec barre de progression animée
- **Vitesse de téléchargement** en temps réel
- **Temps restant estimé** (ETA)
- **Pourcentage de progression** précis

#### 🚀 Mode Batch Intelligent
- **Nouvelle commande `make batch`**
- Configurez **une seule fois** vos paramètres (type, qualité, format)
- S'applique **automatiquement** à toutes les URLs du fichier
- Idéal pour télécharger des playlists ou collections

#### 🛡️ Gestion d'Erreurs Améliorée
- **Messages d'erreur clairs** et explicites
- **Validation des entrées** utilisateur renforcée
- **Interruption propre** avec Ctrl+C (pas de crash)
- **Gestion des exceptions** pour chaque téléchargement
- **Compteur de succès/échecs** en fin d'exécution

---

### 🔧 Améliorations Techniques

#### Code
- Refactorisation complète pour meilleure maintenabilité
- Classe `Colors` pour gérer les couleurs de terminal
- Fonctions de messages typées (`print_success`, `print_error`, etc.)
- Fonction `progress_hook` personnalisée pour yt-dlp
- Meilleure séparation des responsabilités

#### Nouvelles Options CLI
- `--batch` : Active le mode batch intelligent
- `--config` : Ouvre la configuration interactive
- `--help` : Affiche l'aide complète
- Support des commentaires dans `urls.txt` avec `#`

#### Makefile
- **Nouvelle commande `make batch`** : Mode batch
- **Nouvelle commande `make config`** : Configuration
- **Nouvelle commande `make batch-lyrics`** : Batch avec paroles
- Menu d'aide (`make help`) complètement refondu et stylisé
- Messages colorés dans toutes les commandes

---

### 📚 Documentation

#### Nouveaux Fichiers
- **QUICKSTART.md** : Guide de démarrage ultra-rapide (< 5 min)
- **EXAMPLES.md** : Guide complet avec exemples et scénarios
- **CHANGELOG.md** : Ce fichier, historique des versions
- **.gitignore** : Ignore les fichiers générés et configuration locale

#### README.md Amélioré
- Section "Fonctionnalités" complète
- Exemples d'utilisation concrets
- Tableau comparatif des qualités audio/vidéo
- Section "Nouveautés de cette version"
- Format du fichier `urls.txt` expliqué
- Résolution de problèmes courants

#### urls.txt Amélioré
- Template avec instructions claires
- Exemples de commentaires
- En-tête explicatif

---

### 🎨 Expérience Utilisateur

#### Avant (v1.x)
```
❌ Usage: python media_dl.py <url_or_file.txt> [--silent] [--with-lyrics]

❓ What do you want to download?
1 - Audio only
2 - Video only
3 - Video + Subtitles
4 - Skip this URL
Your choice (1/2/3/4):
```

#### Après (v2.0)
```
═══════════════════════════════════
  📥 UNIVERSAL MEDIA DOWNLOADER  
═══════════════════════════════════

🎬 Contenu trouvé: Nom de la vidéo

Que voulez-vous télécharger ?

  1. Audio seulement
  2. Vidéo seulement
  3. Vidéo avec sous-titres
  4. Passer cette URL
  5. Configurer les préférences

Votre choix (1/2/3/4/5):

[████████████████░░░░░░░░] 80.5% | Vitesse: 3.2MB/s | ETA: 00:08
✓ Téléchargement terminé, traitement...
✅ Audio téléchargé: Nom de la vidéo
```

---

### 🐛 Corrections de Bugs
- Correction de la gestion des erreurs lors de l'extraction d'informations
- Meilleure gestion des sous-titres manquants
- Validation robuste des entrées utilisateur
- Gestion des interruptions clavier (KeyboardInterrupt)

---

### 🚀 Performance
- Téléchargements plus rapides avec optimisations yt-dlp
- Messages de progression en temps réel (pas de lag)
- Mode silencieux vraiment silencieux (quiet=True)

---

### 📦 Compatibilité
- Python 3.7+ (inchangé)
- Linux / macOS / Windows (inchangé)
- Toutes les plateformes supportées par yt-dlp

---

### 🔮 Améliorations Futures Possibles

- [ ] Interface graphique (GUI) optionnelle
- [ ] Support des playlists avec détection automatique
- [ ] Téléchargement parallèle de plusieurs URLs
- [ ] Notifications desktop en fin de téléchargement
- [ ] Intégration avec des gestionnaires de médias (Plex, Jellyfin)
- [ ] Export de la configuration vers d'autres machines
- [ ] Support de profils multiples (musique, vidéo, podcast)
- [ ] Historique de téléchargement consultable
- [ ] API REST pour contrôle à distance

---

### 💝 Remerciements

Merci à tous les utilisateurs pour leurs retours qui ont permis ces améliorations !

**Contributeurs** : Vincent B.

---

## Version 1.0.0 - Version Initiale

### Fonctionnalités de Base
- Téléchargement audio/vidéo avec yt-dlp
- Mode interactif
- Mode silencieux
- Support des paroles (--with-lyrics)
- Métadonnées et pochettes d'album
- Journal de téléchargement
- Makefile pour faciliter l'utilisation

---

**Pour la version actuelle, voir le haut de ce fichier.**

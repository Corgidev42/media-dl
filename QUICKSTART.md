# ⚡ Démarrage Rapide - Universal Media Downloader

## Installation (30 secondes)

```bash
make all
```

Voilà ! Le projet est prêt à l'emploi.

---

## Premier Téléchargement

### Étape 1 : Ajoutez une URL
Ouvrez `urls.txt` et ajoutez une URL YouTube ou SoundCloud :
```text
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Étape 2 : Lancez le téléchargeur
```bash
make run
```

### Étape 3 : Suivez le menu
```
1. Audio seulement     ← Pour la musique
2. Vidéo seulement     ← Pour les vidéos
3. Vidéo + sous-titres ← Pour les vidéos avec sous-titres
```

**C'est tout ! 🎉**

---

## Modes d'Utilisation Rapide

### Je veux télécharger PLUSIEURS vidéos avec les MÊMES paramètres
```bash
make batch
```
➜ Configurez une fois, s'applique à tout

### Je veux télécharger AUTOMATIQUEMENT sans questions
```bash
# D'abord, configurez vos préférences
make config

# Ensuite, téléchargez automatiquement
make silent
```
➜ Zéro interaction requise

### Je veux des PAROLES dans mes MP3
```bash
make run-lyrics
```
ou
```bash
make silent-lyrics
```
➜ Les paroles s'intègrent automatiquement si disponibles

---

## Commandes Essentielles

| Commande | Quoi |
|----------|------|
| `make run` | Mode interactif classique |
| `make batch` | Même config pour toutes les URLs |
| `make silent` | Automatique avec vos préférences |
| `make config` | Changer les préférences par défaut |
| `make update` | Mettre à jour yt-dlp |
| `make help` | Voir toutes les commandes |

---

## Astuces Éclair ⚡

**URLs multiples ?** → Mettez-les toutes dans `urls.txt` (une par ligne)

**Paroles disponibles ?** → Ajoutez `--with-lyrics` ou utilisez `make run-lyrics`

**Téléchargement bloqué ?** → Faites `make update` puis réessayez

**Besoin d'aide ?** → `make help` affiche tout

---

## Structure Simple

```
media-dl/
├── urls.txt          ← ✏️ Modifiez ici (vos URLs)
├── config.json       ← ⚙️ Configuration (créé automatiquement)
├── downloads/        ← 📥 Vos fichiers téléchargés
│   ├── *.mp3
│   ├── *.mp4
│   └── log.txt       ← 📝 Historique
└── media_dl.py       ← 🚀 Le script (ne touchez pas)
```

---

## Exemple Concret

**Objectif** : Télécharger 10 musiques en MP3 haute qualité

```bash
# 1. Ajoutez 10 URLs dans urls.txt

# 2. Lancez le mode batch
make batch

# 3. Dans le menu :
#    - Choisissez : Audio (1)
#    - Qualité : Haute - 256kbps (3)
#    - Format : MP3 (1)

# ✅ Les 10 musiques se téléchargent automatiquement !
```

---

## Vous êtes prêt ! 🚀

Pour des exemples plus détaillés, consultez [EXAMPLES.md](EXAMPLES.md)

Pour la documentation complète, consultez [README.md](README.md)

**Bon téléchargement !** 🎵🎬

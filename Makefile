# 🎨 Colors
RESET   = \033[0m
GREEN   = \033[32m
RED     = \033[31m
YELLOW  = \033[33m
CYAN    = \033[36m
BOLD    = \033[1m

VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(PYTHON) -m pip
SCRIPT = streamgrab.py
URLS_FILE = urls.txt

all: venv install

venv:
	@echo "$(CYAN)🐍 Creating virtual environment...$(RESET)"
	@python3 -m venv $(VENV_DIR)

install: venv
	@echo "$(YELLOW)📦 Installing Python dependencies...$(RESET)"
	@$(PIP) install --upgrade pip
	@$(PIP) install yt-dlp mutagen requests

run: all
	@echo "$(GREEN)▶️  Lancement du téléchargeur en mode interactif...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE)

batch: all
	@echo "$(GREEN)🚀 Lancement du téléchargeur en mode batch...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE) --batch

config: all
	@echo "$(CYAN)⚙️  Configuration des préférences...$(RESET)"
	@$(PYTHON) $(SCRIPT) --config

silent: all
	@echo "$(GREEN)⚡ Lancement du téléchargeur en mode silencieux...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE) --silent

run-lyrics: all
	@echo "$(GREEN)🎵 Lancement du téléchargeur avec paroles...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE) --with-lyrics

batch-lyrics: all
	@echo "$(GREEN)🎵🚀 Lancement du téléchargeur en mode batch avec paroles...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE) --batch --with-lyrics

silent-lyrics: all
	@echo "$(GREEN)🎵⚡ Lancement du téléchargeur en mode silencieux avec paroles...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE) --silent --with-lyrics

update:
	@echo "$(YELLOW)🔄 Updating yt-dlp...$(RESET)"
	@$(PYTHON) $(SCRIPT) --update

clean:
	@echo "$(RED)🧹 Cleaning virtual environment...$(RESET)"
	@rm -rf $(VENV_DIR)

fclean: clean
	@echo "$(RED)🧹 Removing downloads folder...$(RESET)"
	@rm -rf downloads

re: fclean all

help:
	@echo ""
	@echo "$(BOLD)═══════════════════════════════════════════════════════════════$(RESET)"
	@echo "$(BOLD)$(CYAN)        📥 UNIVERSAL MEDIA DOWNLOADER - Commandes$(RESET)"
	@echo "$(BOLD)═══════════════════════════════════════════════════════════════$(RESET)"
	@echo ""
	@echo "$(BOLD)$(YELLOW)🔧 Installation:$(RESET)"
	@echo "  $(CYAN)make all$(RESET)                → Créer l'environnement virtuel et installer les dépendances"
	@echo "  $(CYAN)make install$(RESET)            → Installer ou mettre à jour les dépendances Python"
	@echo ""
	@echo "$(BOLD)$(YELLOW)▶️  Modes d'exécution:$(RESET)"
	@echo "  $(CYAN)make run$(RESET)                → Mode interactif (choix pour chaque URL)"
	@echo "  $(CYAN)make batch$(RESET)              → Mode batch intelligent (mêmes paramètres pour toutes les URLs)"
	@echo "  $(CYAN)make silent$(RESET)             → Mode silencieux (utilise les préférences par défaut)"
	@echo ""
	@echo "$(BOLD)$(YELLOW)🎵 Avec paroles:$(RESET)"
	@echo "  $(CYAN)make run-lyrics$(RESET)         → Mode interactif avec téléchargement des paroles"
	@echo "  $(CYAN)make batch-lyrics$(RESET)       → Mode batch avec paroles"
	@echo "  $(CYAN)make silent-lyrics$(RESET)      → Mode silencieux avec paroles"
	@echo ""
	@echo "$(BOLD)$(YELLOW)⚙️  Configuration:$(RESET)"
	@echo "  $(CYAN)make config$(RESET)             → Configurer les préférences par défaut"
	@echo "  $(CYAN)make update$(RESET)             → Mettre à jour yt-dlp vers la dernière version"
	@echo ""
	@echo "$(BOLD)$(YELLOW)🧹 Nettoyage:$(RESET)"
	@echo "  $(CYAN)make clean$(RESET)              → Supprimer uniquement l'environnement virtuel"
	@echo "  $(CYAN)make fclean$(RESET)             → Supprimer l'environnement virtuel et le dossier downloads"
	@echo "  $(CYAN)make re$(RESET)                 → Nettoyage complet et réinstallation"
	@echo ""
	@echo "$(BOLD)$(YELLOW)ℹ️  Aide:$(RESET)"
	@echo "  $(CYAN)make help$(RESET)               → Afficher ce message d'aide"
	@echo ""
	@echo "$(BOLD)═══════════════════════════════════════════════════════════════$(RESET)"
	@echo ""

.PHONY: all venv install run batch config silent run-lyrics batch-lyrics silent-lyrics clean fclean re help update

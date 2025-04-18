# 🎨 Colors
RESET   = \033[0m
GREEN   = \033[32m
RED     = \033[31m
YELLOW  = \033[33m
CYAN    = \033[36m
BOLD    = \033[1m

# 🐍 Python & Virtualenv
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

# 📁 Script
SCRIPT = downloader.py
# 📄 Fichier contenant les URLs
URLS_FILE = urls.txt

# 🧱 Main targets
all: venv install

venv:
	@echo "$(CYAN)🐍 Creating virtual environment...$(RESET)"
	@python3 -m venv $(VENV_DIR)

install: venv
	@echo "$(YELLOW)📦 Installing Python dependencies...$(RESET)"
	@$(PIP) install --upgrade pip
	@$(PIP) install yt-dlp

run: all
	@echo "$(GREEN)▶️ Running downloader...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE)

clean:
	@echo "$(RED)🧹 Cleaning virtual environment...$(RESET)"
	@rm -rf $(VENV_DIR)

fclean: clean
	@echo "$(RED)🧹 Removing downloads folder...$(RESET)"
	@rm -rf downloads

re: fclean all

help:
	@echo ""
	@echo "$(BOLD)Available commands:$(RESET)"
	@echo "$(CYAN)make run$(RESET)      → Run downloader using urls.txt"
	@echo "$(CYAN)make clean$(RESET)    → Remove virtual environment only"
	@echo "$(CYAN)make fclean$(RESET)   → Full clean (venv + downloads)"
	@echo "$(CYAN)make re$(RESET)       → Full reset (clean + reinstall)"
	@echo ""

.PHONY: all venv install run clean fclean re help
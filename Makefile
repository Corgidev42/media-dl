# 🎨 Colors
RESET   = \033[0m
GREEN   = \033[32m
RED     = \033[31m
YELLOW  = \033[33m
CYAN    = \033[36m
BOLD    = \033[1m

VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
SCRIPT = media_dl.py
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
	@echo "$(GREEN)▶️ Running downloader interactively...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE)

silent: all
	@echo "$(GREEN)⚡ Running downloader silently...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE) --silent

run-lyrics: all
	@echo "$(GREEN)🎵 Running downloader with lyrics...$(RESET)"
	@$(PYTHON) $(SCRIPT) $(URLS_FILE) --with-lyrics

silent-lyrics: all
	@echo "$(GREEN)🎵⚡ Running downloader silently with lyrics...$(RESET)"
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
	@echo "$(BOLD)Available commands:$(RESET)"
	@echo "$(CYAN)make all$(RESET)             → Create virtual environment and install dependencies"
	@echo "$(CYAN)make venv$(RESET)            → Create only the virtual environment"
	@echo "$(CYAN)make install$(RESET)         → Install or upgrade Python dependencies"
	@echo "$(CYAN)make run$(RESET)             → Run downloader in interactive mode"
	@echo "$(CYAN)make silent$(RESET)          → Run downloader in silent mode (auto)"
	@echo "$(CYAN)make run-lyrics$(RESET)      → Run downloader interactively with lyrics"
	@echo "$(CYAN)make silent-lyrics$(RESET)   → Run downloader silently with lyrics"
	@echo "$(CYAN)make update$(RESET)          → Update yt-dlp"
	@echo "$(CYAN)make clean$(RESET)           → Remove only the virtual environment"
	@echo "$(CYAN)make fclean$(RESET)          → Remove the virtual environment and downloads folder"
	@echo "$(CYAN)make re$(RESET)              → Full reset (clean everything and reinstall)"
	@echo "$(CYAN)make help$(RESET)            → Show this help message"
	@echo ""

.PHONY: all venv install run silent run-lyrics silent-lyrics clean fclean re help update

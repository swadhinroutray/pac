.PHONY: setup clean run test

# Python settings
PYTHON := python3.11
VENV := venv
PIP := $(VENV)/bin/pip

# Default values
AUDIO_FILE ?= $(shell pwd)/podcasts/sample.mp3
VAULT_PATH ?= $(shell pwd)/pac-summarized

setup: $(VENV)/bin/activate

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run:
	$(VENV)/bin/python main.py --audio-file $(AUDIO_FILE) --vault-path $(VAULT_PATH)

test:
	$(VENV)/bin/python -m pytest

# Recreate config.py if it was deleted
config:
	@echo "Creating config.py..."
	@echo 'import os\nfrom pathlib import Path\n\n# Default Obsidian vault path - should be configured by user\nOBSIDIAN_VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH", "")\n\n# Models configuration\nWHISPER_MODEL = "base"  # Options: tiny, base, small, medium, large\nSUMMARY_MODEL = "facebook/bart-large-cnn"\n\n# Output configuration\nDEFAULT_OUTPUT_DIR = Path("output")\nDEFAULT_OUTPUT_DIR.mkdir(exist_ok=True)\n\n# Markdown template for Obsidian notes\nMARKDOWN_TEMPLATE = """---\ncreated: {timestamp}\ntype: transcript\nsource: {audio_file}\n---\n\n# {title}\n\n## Summary\n{summary}\n\n## Full Transcript\n{transcript}\n"""' > config.py

.DEFAULT_GOAL := setup
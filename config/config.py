import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Default Obsidian vault path - configured via .env file
OBSIDIAN_VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH", "./pac-summarized")

# Models configuration
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")  # Options: tiny, base, small, medium, large
SUMMARY_MODEL = "facebook/bart-large-cnn"

# Output configuration
DEFAULT_OUTPUT_DIR = Path(OBSIDIAN_VAULT_PATH)
DEFAULT_OUTPUT_DIR.mkdir(exist_ok=True)

# Markdown template for Obsidian notes
MARKDOWN_TEMPLATE = """---
created: {timestamp}
type: transcript
source: {audio_file}
---

# {title}

## Summary
{summary}

## Full Transcript
{transcript}
"""

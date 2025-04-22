# PAC (Personal Audio Companion)

A Python tool that transcribes audio using an open-source speech-to-text model, summarizes the content, and writes it to a local markdown folder (compatible with Obsidian).

## Features

- Speech-to-text transcription using Whisper
- Text summarization using transformers
- Automatic export to markdown files

## Setup

1. Install dependencies:

```bash
make setup
```

2. Install yt-dlp (if you need to download YouTube podcasts):

```bash
brew install yt-dlp  # on macOS
# or
pip install yt-dlp   # using pip
```

3. Configure Environment:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your preferred settings
# OBSIDIAN_VAULT_PATH: Where to save the transcripts (default: ./pac-summarized)
# WHISPER_MODEL: Model size to use (default: base)
```

## Usage

### 1. Download Podcasts

Create a `podcasts` directory and download your podcasts there:

```bash
# Create podcasts directory
mkdir -p podcasts

# Download a podcast from YouTube
yt-dlp -x --audio-format mp3 -o "podcasts/%(title)s.%(ext)s" "YOUR_YOUTUBE_URL"

# Example:
yt-dlp -x --audio-format mp3 -o "podcasts/musk-friedman.%(ext)s" "https://www.youtube.com/watch?v=Kbk9BiPhm7o"
```

### 2. Transcribe and Summarize

The tool will create transcripts and summaries in the `pac-summarized` directory:

```bash
# Using default paths from Makefile
make run

# Or specify custom paths
make run AUDIO_FILE=/path/to/audio.mp3 VAULT_PATH=/path/to/output/dir
```

## Project Structure

- `podcasts/` - Directory for storing downloaded audio files
- `pac-summarized/` - Directory where transcripts and summaries are saved
- `config/` - Configuration files
- `main.py` - Main application logic

## Notes

- The default Whisper model is "base". You can change this in `config/config.py` to other options: tiny, base, small, medium, large
- Larger models provide better transcription but require more computational resources
- Audio files are not tracked in git to keep the repository size manageable

## License

MIT License

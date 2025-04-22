import argparse
from datetime import datetime
from pathlib import Path
import whisper
from transformers import pipeline
from config.config import *

def transcribe_audio(audio_file: str) -> str:
    """Transcribe audio file using Whisper."""
    model = whisper.load_model(WHISPER_MODEL)
    result = model.transcribe(audio_file)
    return result["text"]

def summarize_text(text: str) -> str:
    """Summarize text using transformers."""
    summarizer = pipeline("summarization", model=SUMMARY_MODEL)
    
    # Split text into chunks if it's too long (max 1024 tokens)
    max_chunk_size = 1024
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    return " ".join(summaries)

def write_to_obsidian(audio_file: str, transcript: str, summary: str, vault_path: str):
    """Write the transcript and summary to Obsidian vault."""
    vault_path = Path(vault_path)
    if not vault_path.exists():
        raise ValueError(f"Obsidian vault path does not exist: {vault_path}")
    
    # Create output file name from audio file name
    audio_name = Path(audio_file).stem
    output_file = vault_path / f"{audio_name}.md"
    
    # Format the markdown content
    content = MARKDOWN_TEMPLATE.format(
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        audio_file=audio_file,
        title=audio_name,
        summary=summary,
        transcript=transcript
    )
    
    # Write to file
    output_file.write_text(content)
    print(f"Written to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio and create Obsidian notes")
    parser.add_argument("--audio-file", required=True, help="Path to audio file")
    parser.add_argument("--vault-path", required=True, help="Path to Obsidian vault")
    
    args = parser.parse_args()
    
    print("Transcribing audio...")
    transcript = transcribe_audio(args.audio_file)
    
    print("Generating summary...")
    summary = summarize_text(transcript)
    
    print("Writing to Obsidian...")
    write_to_obsidian(args.audio_file, transcript, summary, args.vault_path)
    
    print("Done!")

if __name__ == "__main__":
    main()

from pydub import AudioSegment
import argparse

def merge_audio(file1, file2, output_file):
    # Load audio files
    audio1 = AudioSegment.from_file(file1)
    audio2 = AudioSegment.from_file(file2)

    # Merge audio files (Concatenation)
    combined = audio1 + audio2

    # Export merged audio file
    combined.export(output_file, format="mp3")
    print(f"Merged audio saved as {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge two audio files.")
    parser.add_argument("--file1", required=True, help="Path to first audio file")
    parser.add_argument("--file2", required=True, help="Path to second audio file")
    parser.add_argument("--output", required=True, help="Output merged audio file")
    
    args = parser.parse_args()
    merge_audio(args.file1, args.file2, args.output)

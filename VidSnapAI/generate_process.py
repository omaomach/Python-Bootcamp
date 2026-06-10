# This file looks for new folders inside user uploads and converts them to reels if they are not already converted
import os
from text_to_audio import text_to_speech_file

base_path = "VidSnapAI/user_uploads"

def text_to_audio(folder):
    print("TTA - ", folder)
    with open(f"VidSnapAI/user_uploads/{folder}/description.txt") as f:
        text = f.read()
    # text_to_speech_file(text, folder)
    print(text, folder)

def create_reel(folder):
    print("CR - ", folder)

if __name__ == "__main__":
    file_path = os.path.join(base_path, "done.txt")
    with open(file_path, "r") as f:
        content = f.read()

    # Filter to include only items that are directories
    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    for folder in folders:
        if (folder not in content):
            text_to_audio(folder) # Generate the audio.mp3 from description.txt
            create_reel(folder) # Convert the images and audio inside the folder to a reel

            # FIXED: Writing to the correct file path inside user_uploads
            with open(file_path, "a") as f:
                f.write(folder + "\n")
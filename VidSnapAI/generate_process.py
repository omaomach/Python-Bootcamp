# For directory scanning and path work.
import os
# Pull in the real TTS worker from another file i.e text_to_audio.py
from text_to_audio import text_to_speech_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(BASE_DIR, 'user_uploads')

def text_to_audio(folder):
    print("TTA - ", folder)
    with open(os.path.join(base_path, folder, 'description.txt')) as f:
        text = f.read()
    # text_to_speech_file(text, folder)
    print(text, folder)

def create_reel(folder):
    print("CR - ", folder)

if __name__ == "__main__":

    # Builds the ledger path and reads the whole file into the "done" variable as one string
    file_path = os.path.join(base_path, "done.txt")
    if not os.path.exists(file_path):
        open(file_path, "w").close()
    with open(file_path, "r") as f:
        done = {line.strip() for line in f}

    # List compression: list everything in base_path, keep only the directories. in this case "done.txt" is kicked to the curb
    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    for folder in folders:
        if (folder not in done):
            text_to_audio(folder) # Generate the audio.mp3 from description.txt
            create_reel(folder) # Convert the images and audio inside the folder to a reel

            # FIXED: Writing to the correct file path inside user_uploads
            with open(file_path, "a") as f:
                f.write(folder + "\n")
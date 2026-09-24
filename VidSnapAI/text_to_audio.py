
import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(BASE_DIR, "user_uploads")

def text_to_speech_file(text: str, folder: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    # "response" is not a finished mp3 sitting in memory. Its a generator --
    # a stream that hands you the audio in pieces, one at a time as ElevenLabs produces it
    response = elevenlabs.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_flash_v2_5", # use the flash model for low latency
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    # uncomment the line below to play the audio back (needs: from elevenlabs import play)
    # play(response)

    # Adding the file name to the folder path
    save_file_path = os.path.join(base_path, folder, "audio.mp3")

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response: # catch each segment as it streams in
            if chunk: # skip any empty segment
                f.write(chunk) # append that segment onto the file on disk

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path


# text_to_speech_file("Hey, I love God. He has given me everything that I have", "4a8a2116-6474-11f1-ba8f-10683893eb3b")
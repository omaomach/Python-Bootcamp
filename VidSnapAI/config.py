import os

from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

if not ELEVENLABS_API_KEY:
    raise RuntimeError("ELEVENLABS_API_KEY is not set. Check you .env file.")
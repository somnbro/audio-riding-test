import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from utils.audio import load_audio
from analysis.voice_detection import is_voice


audio, sr = load_audio(
    "audio/input/test.wav"
)


chunk_size = sr


first_chunk = audio[5*sr:6*sr]


result = is_voice(first_chunk)


print("Voice detected:", result)
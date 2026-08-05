import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from utils.audio import load_audio, save_audio
from processing.vocal_rider import ride_volume


audio, sr = load_audio(
    "audio/input/test.wav"
)

processed = ride_volume(
    audio,
    sr
)

save_audio(
    "audio/output/test_smart_rider4.wav",
    processed,
    sr
)

print("Smart rider finished!")
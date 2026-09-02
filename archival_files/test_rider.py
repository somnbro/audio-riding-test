import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)


from utils.audio import load_audio, save_audio
from processing.vocal_rider import apply_gain


audio, sr = load_audio(
    "audio/input/test.wav"
)


louder_audio = apply_gain(
    audio,
    6
)


save_audio(
    "audio/output/test_louder.wav",
    louder_audio,
    sr
)


print("Finished")
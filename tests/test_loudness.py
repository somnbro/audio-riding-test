import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from utils.audio import load_audio
from analysis.loudness import analyze_loudness

audio, sr = load_audio("audio/input/test.wav")

results = analyze_loudness(audio, sr)

print(results["average"])

print(results["peak"])
import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from utils.audio import load_audio
from analysis.wind_detection import wind_severity, low_frequency_energy


audio, sr = load_audio(
    "audio/input/test.wav"
)


chunk_size = int(sr * 0.05)


for i in range(0, len(audio)//3, chunk_size):

    chunk = audio[i:i+chunk_size]

    if len(chunk) == 0:
        continue

    energy = low_frequency_energy(
        chunk,
        sr
    )

    severity = wind_severity(
        chunk,
        sr
    )

    time = i / sr

    if energy > 25:
        print(
            f"{time:.2f}s  LOW ENERGY: {energy:.3f} SEVERITY: {severity:.2f}"

        )
import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from utils.audio import load_audio
from analysis.airflow_detection import airflow_ratio

audio, sr = load_audio("audio/input/test.wav")

chunk_size = int(sr * 0.05)   # 50 ms

for i in range(0, (len(audio))//3, chunk_size):

    chunk = audio[i:i + chunk_size]

    if len(chunk) == 0:
        continue

    ratio = airflow_ratio(chunk, sr)

    if ratio>=2.0:
        print(i / sr, ratio)
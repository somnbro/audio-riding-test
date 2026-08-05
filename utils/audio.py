import soundfile as sf
import numpy as np


def load_audio(path):
    audio, sample_rate = sf.read(path)

    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1)

    return audio, sample_rate


def save_audio(path, audio, sample_rate):
    sf.write(path, audio, sample_rate)
import soundfile as sf
import numpy as np

audio, sample_rate = sf.read("audio/test.wav")

duration = len(audio) / sample_rate

volume = np.max(np.abs(audio))

print("Audio loaded!")
print("Sample rate:", sample_rate)
print("Duration:", duration, "seconds")
print("Peak volume:", volume)
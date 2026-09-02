import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

audio, sample_rate = sf.read("audio/test.wav")

# Stereo → mono
if len(audio.shape) > 1:
    audio = np.mean(audio, axis=1)

plt.figure(figsize=(12,6))

plt.specgram(
    audio,
    Fs=sample_rate,
    NFFT=1024,
    noverlap=512
)

plt.title("Spectrogram")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.ylim(0,8000)

plt.colorbar(label="Intensity")

plt.show()
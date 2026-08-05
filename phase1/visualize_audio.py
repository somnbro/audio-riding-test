import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

audio, sample_rate = sf.read("audio/test.wav")

if len(audio.shape)> 1:
    audio = np.mean(audio, axis=1)

time = np.linspace(
    0,
    len(audio)/sample_rate,
    num=len(audio)
)

plt.figure(figsize=(12, 4))

plt.plot(time, audio)

plt.title("Vocal Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.show()
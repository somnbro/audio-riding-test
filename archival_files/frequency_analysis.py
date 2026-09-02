import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

# Load audio
audio, sample_rate = sf.read("audio/test.wav")

# Convert stereo to mono
if len(audio.shape) > 1:
    audio = np.mean(audio, axis=1)

# Use only the first 5 seconds (keeps the graph clean)
audio = audio[:sample_rate * 5]

# Compute FFT
fft = np.fft.rfft(audio)

# Magnitude of each frequency
magnitude = np.abs(fft)

# Frequency labels
frequencies = np.fft.rfftfreq(len(audio), d=1/sample_rate)

# Plot
plt.figure(figsize=(12,5))
plt.plot(frequencies, magnitude)

plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

# Focus on vocal range
plt.xlim(0, 8000)

plt.show()

top_indices = np.argsort(magnitude)[-10:]

print("\nStrongest frequencies:")

for i in reversed(top_indices):
    print(f"{frequencies[i]:7.1f} Hz : {magnitude[i]:.2f}")
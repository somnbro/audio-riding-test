import soundfile as sf
import numpy as np


audio, sample_rate = sf.read("audio/test.wav")


# Convert stereo to mono
if len(audio.shape) > 1:
    audio = np.mean(audio, axis=1)


# How long each measurement should be
chunk_seconds = 1

chunk_size = sample_rate * chunk_seconds


print("Loudness over time:")
print("-------------------")


for i in range(0, len(audio), chunk_size):

    chunk = audio[i:i+chunk_size]

    if len(chunk) == 0:
        continue

    # RMS = average energy of the sound
    rms = np.sqrt(np.mean(chunk**2))

    # Convert to decibels
    db = 20 * np.log10(rms + 1e-8)

    timestamp = i / sample_rate

    print(
        round(timestamp, 1),
        "seconds:",
        round(db, 2),
        "dB"
    )
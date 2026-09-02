#OLD CODE
from analysis.voice_detection import is_voice
import numpy as np


def db_to_gain(db):
    return 10 ** (db / 20)


def ride_volume(audio, sample_rate, target_db=-18):

    chunk_seconds = 1
    chunk_size = sample_rate * chunk_seconds

    gains = []

    processed = np.copy(audio)

    for i in range(0, len(audio), chunk_size):

        chunk = audio[i:i+chunk_size]

        if len(chunk) == 0:
            continue

        if not is_voice(chunk):
            continue

        # Measure loudness
        rms = np.sqrt(np.mean(chunk**2))

        current_db = 20 * np.log10(rms + 1e-8)

        # Difference between current and target
        difference = target_db - current_db


        # Limit the amount of adjustment
        difference = np.clip(
            difference,
            -6,
            6
        )


        gain = db_to_gain(difference)

        gains.append(gain)

    smoothed_gains = []

    for i in range(len(gains)):

        if i == 0:
            smoothed_gains.append(gains[i])

        else:

            smooth = (
                smoothed_gains[-1] * 0.8
                + gains[i] * 0.2
            )

            smoothed_gains.append(smooth)

    for index, i in enumerate(range(0, len(audio), chunk_size)):

        chunk = processed[i:i+chunk_size]

        if len(chunk) == 0:
            continue

        chunk *= smoothed_gains[index]

    return processed
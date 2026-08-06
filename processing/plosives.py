import numpy as np


def reduce_plosives(audio, sample_rate):

    processed = np.copy(audio)

    window_ms = 30
    window_size = int(sample_rate * window_ms / 1000)

    threshold = 0.7

    for start in range(0, len(audio), window_size):

        end = start + window_size
        chunk = processed[start:end]

        if len(chunk) == 0:
            continue

        peak = np.max(np.abs(chunk))

        if peak > threshold:

            processed[start:end] *= 0.8

    return processed
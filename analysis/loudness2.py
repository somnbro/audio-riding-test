import numpy as np


def calculate_loudness(audio):

    # Apply simple ear-weighting
    weighted = audio * 0.8

    rms = np.sqrt(
        np.mean(weighted ** 2)
    )

    loudness_db = 20 * np.log10(
        rms + 1e-8
    )

    return loudness_db
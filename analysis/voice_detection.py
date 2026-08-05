import numpy as np


def is_voice(chunk, threshold_db=-40):

    rms = np.sqrt(np.mean(chunk**2))

    db = 20 * np.log10(rms + 1e-8)

    if db > threshold_db:
        return True

    return False
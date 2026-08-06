import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

import numpy as np
#from processing.gain_envelope import apply_gain_smooth

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

            processed[start:end] *= 0.2
            # apply_gain_smooth(
            #     processed,
            #     start,
            #     end,
            #     0.2
            # )

    return processed
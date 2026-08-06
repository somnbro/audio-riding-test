import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
import numpy as np

from analysis.wind_detection import wind_severity
#from processing.gain_envelope import apply_gain_smooth


def reduce_wind(audio, sample_rate):

    processed = np.copy(audio)

    chunk_seconds = 0.05
    chunk_size = int(sample_rate * chunk_seconds)


    for start in range(0, len(audio), chunk_size):

        end = start + chunk_size

        chunk = audio[start:end]


        if len(chunk) == 0:
            continue


        severity = wind_severity(
            chunk,
            sample_rate
        )


        if severity > 0.5:

            reduction = 1 - (severity * 0.92)

            processed[start:end] *= reduction
            # apply_gain_smooth(
            #     processed,
            #     start,
            #     end,
            #     reduction
            # )


    return processed
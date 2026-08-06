import os
import sys

# Finds the absolute path to AI-PROJECT and adds it to Python's search path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from scipy.signal import butter, sosfilt


def low_pass_filter(audio, sample_rate, cutoff=150):

    sos = butter(
        4,
        cutoff,
        btype="lowpass",
        fs=sample_rate,
        output="sos"
    )

    filtered = sosfilt(
        sos,
        audio
    )

    return filtered

def deesser_filter(audio, sample_rate):

    sos = butter(
        4,
        cutoff=[3000, 4000],
        btype="bandstop",
        fs=sample_rate,
        output="sos"
    )
    
    filtered = sosfilt(
        sos,
        audio
    )
    
    return filtered
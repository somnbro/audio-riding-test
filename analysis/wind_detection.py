import numpy as np


def low_frequency_energy(chunk, sample_rate):

    #creates an absolute value of the fft of a chunk
    spectrum = np.abs(
        np.fft.rfft(chunk)
    )

    #creates a frequencyies in the fft of the sound
    frequencies = np.fft.rfftfreq(
        len(chunk),
        1 / sample_rate
    )

    low = spectrum[
        frequencies < 200
    ]

    return np.mean(low)

def wind_severity(chunk, sample_rate):

    energy = low_frequency_energy(
        chunk,
        sample_rate
    )

    severity = energy / 60

    severity = np.clip(
        severity,
        0,
        1
    )

    return severity
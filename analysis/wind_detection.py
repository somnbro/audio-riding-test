import numpy as np


def low_frequency_energy(chunk, sample_rate):

    spectrum = np.abs(
        np.fft.rfft(chunk)
    )

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
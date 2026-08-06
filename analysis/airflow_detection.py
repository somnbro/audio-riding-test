import numpy as np


def airflow_ratio(chunk, sample_rate):

    spectrum = np.abs(np.fft.rfft(chunk))

    frequencies = np.fft.rfftfreq(
        len(chunk),
        d=1 / sample_rate
    )

    low = spectrum[frequencies < 1000]
    high = spectrum[frequencies > 3000]

    low_energy = np.mean(low)
    high_energy = np.mean(high)

    return high_energy / (low_energy + 1e-8)
import numpy as np


def is_breath(chunk, sample_rate):

    # High frequency emphasis
    spectrum = np.abs(
        np.fft.rfft(chunk)
    )

    frequencies = np.fft.rfftfreq(
        len(chunk),
        1 / sample_rate
    )


    high_freq = spectrum[
        frequencies > 3000
    ]


    low_freq = spectrum[
        frequencies < 1000
    ]


    high_energy = np.mean(high_freq)
    low_energy = np.mean(low_freq)


    ratio = high_energy / (low_energy + 1e-8)


    return ratio > 2.0
import numpy as np


def apply_gain_smooth(audio, start, end, gain):

    length = end - start

    fade_length = int(length * 0.05)

    envelope = np.ones(length)


    # fade down
    envelope[:fade_length] = np.linspace(
        1,
        gain,
        fade_length
    )


    # hold reduction
    envelope[fade_length:-fade_length] = gain


    # fade back up
    envelope[-fade_length:] = np.linspace(
        gain,
        1,
        fade_length
    )


    audio[start:end] *= envelope
import numpy as np


def apply_gain_smooth(audio, start, end, gain):

    length = end - start

    attack = int(length * 0.1)
    release = int(length * 0.2)

    envelope = np.ones(length)


    # Attack
    envelope[:attack] = np.linspace(
        1,
        gain,
        attack
    )


    # Hold
    envelope[attack:length-release] = gain


    # Release
    envelope[length-release:] = np.linspace(
        gain,
        1,
        release
    )


    audio[start:end] *= envelope
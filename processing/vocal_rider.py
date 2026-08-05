from analysis.voice_detection import is_voice
from analysis.breath_detection import is_breath

import numpy as np
from analysis.loudness2 import calculate_loudness


def db_to_gain(db):
    return 10 ** (db / 20)

def calculate_gain_adjustment(current_db, target_db):

    difference = target_db - current_db


    # Ignore tiny differences
    if abs(difference) < 1:
        return 1.0


    # Limit correction
    difference = np.clip(
        difference,
        -4,
        4
    )


    return db_to_gain(difference)


def interpolate_gains(chunk_data, audio_length):

    gain_curve = np.ones(audio_length)


    for i in range(len(chunk_data) - 1):

        start = chunk_data[i]["start"]
        end = chunk_data[i]["end"]

        start_gain = chunk_data[i]["gain"]
        end_gain = chunk_data[i + 1]["gain"]


        length = end - start

        if length <= 0:
            continue


        transition = np.linspace(
            start_gain,
            end_gain,
            length
        )


        gain_curve[start:end] = transition


    return gain_curve


def smooth_gains(gains, smoothing=0.2):

    if len(gains) == 0:
        return []

    smoothed = [gains[0]]

    for i in range(1, len(gains)):

        new_gain = (
            smoothed[-1] * (1 - smoothing)
            + gains[i] * smoothing
        )

        smoothed.append(new_gain)

    return smoothed


def ride_volume(audio, sample_rate, target_db=-18):

    chunk_seconds = 0.25
    chunk_size = int(sample_rate * chunk_seconds)

    hop_size = int(chunk_size * 0.5)

    processed = np.copy(audio)

    chunk_data = []
    gains = []


    # ---------- Analysis ----------
    for start in range(0, len(audio), hop_size):

        end = min(start + chunk_size, len(audio))
        chunk = audio[start:end]

        if len(chunk) == 0:
            continue


        if not is_voice(chunk):

            chunk_data.append({
                "start": start,
                "end": end,
                "gain": 1.0
            })

            gains.append(1.0)

            continue

        if is_breath(chunk, sample_rate):

            gains.append(0.7)
            continue

        current_db = calculate_loudness(chunk)

        gain = calculate_gain_adjustment(
            current_db,
            target_db
        )


        chunk_data.append({
            "start": start,
            "end": end,
            "gain": gain
        })

        gains.append(gain)



    # ---------- Smooth gains ----------
    smoothed = smooth_gains(gains)



    # Replace old gains with smoothed gains

    for index, info in enumerate(chunk_data):

        info["gain"] = smoothed[index]



    # ---------- Apply ----------

    gain_curve = interpolate_gains(
        chunk_data,
        len(audio)
    )

    processed *= gain_curve
    return processed


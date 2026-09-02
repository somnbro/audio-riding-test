from analysis.voice_detection import is_voice
import numpy as np


def db_to_gain(db):
    return 10 ** (db / 20)


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

    chunk_seconds = 1
    chunk_size = int(sample_rate * chunk_seconds)

    processed = np.copy(audio)

    chunk_data = []
    gains = []


    # ---------- Analysis ----------
    for start in range(0, len(audio), chunk_size):

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


        rms = np.sqrt(np.mean(chunk ** 2))

        current_db = 20 * np.log10(rms + 1e-8)


        difference = target_db - current_db


        difference = np.clip(
            difference,
            -6,
            6
        )


        gain = db_to_gain(difference)


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
    for info in chunk_data:

        processed[
            info["start"]:info["end"]
        ] *= info["gain"]


    return processed
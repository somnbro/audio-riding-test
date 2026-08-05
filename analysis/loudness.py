import numpy as np


def analyze_loudness(audio, sample_rate):

    chunk_seconds = 1

    chunk_size = sample_rate * chunk_seconds

    chunks = []

    for i in range(0, len(audio), chunk_size):

        chunk = audio[i:i+chunk_size]

        if len(chunk) == 0:
            continue

        rms = np.sqrt(np.mean(chunk**2))

        db = 20*np.log10(rms + 1e-8)

        chunks.append({
            "time": i/sample_rate,
            "db": db
        })

    peak = np.max(np.abs(audio))

    average = np.mean([c["db"] for c in chunks])

    return {
        "peak": peak,
        "average": average,
        "chunks": chunks
    }
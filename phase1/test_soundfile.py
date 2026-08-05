import soundfile as sf

data, samplerate = sf.read("audio/test.wav")

print("Success!")
print("Sample rate:", samplerate)
print("Samples:", len(data))
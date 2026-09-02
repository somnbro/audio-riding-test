import soundfile as sf
from df.enhance import enhance, init_df


# Load pretrained model
model, df_state, _ = init_df()


# Load audio
audio, sr = sf.read("experiments/ai_only_demo/input.wav")


# AI enhancement
enhanced = enhance(
    model,
    df_state,
    audio,
    sr
)


# Save result
sf.write(
    "experiments/ai_only_demo/output.wav",
    enhanced,
    sr
)


print("AI cleanup complete")
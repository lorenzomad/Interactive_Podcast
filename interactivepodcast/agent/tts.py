from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

# download and load all models
preload_models()

class TTS():
     """class to allow the creation and reproduction of audio
     text to speech for the ai agent"""
     def __init__(self) -> None:
        self.audio_array = None


     def generate_audio(self, prompt):
        """generates audio from the text"""
        self.audio_array = generate_audio(prompt)

     def play_audio(self):
        """plays the audio saved in the audio_array variable"""
        Audio(self.audio_array, rate=SAMPLE_RATE)

# save audio to disk
# write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

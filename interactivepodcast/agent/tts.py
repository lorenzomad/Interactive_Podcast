"""contains the Text to speech models to use in the ai agent system"""

# from bark import SAMPLE_RATE, generate_audio, preload_models
# from IPython.display import Audio
# from TTS.api import TTS

from gtts import gTTS
import os

# download and load all models
# preload_models()

# class BarkTTS():
#      """class to allow the creation and reproduction of audio
#      text to speech for the ai agent"""
#      def __init__(self) -> None:
#         self.audio_array = None


#      def generate_audio(self, prompt):
#         """generates audio from the text"""
#         self.audio_array = generate_audio(prompt)

#      def play_audio(self):
#         """plays the audio saved in the audio_array variable"""
#         Audio(self.audio_array, rate=SAMPLE_RATE)

# save audio to disk
# write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)



# wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# # Text to speech to a file
# tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")


# class FrogTTS():
#    def __init__(self) -> None:
#       self.model_name = TTS.list_models()[0]
#       self.tts = TTS(self.model_name)
#       self.audio = None

   
#    def generate_audio(self, prompt):
#       """generates an audio of the input prompt"""
#       self.audio = self.tts.tts(
#          prompt, 
#          speaker=self.tts.speakers[0], 
#          language=self.tts.languages[0]
#          )

#    def play_audio(self):
#       """plays the generated audio"""
#       Audio(self.audio, rate=SAMPLE_RATE)
   
class GTTS():
   def __init__(self) -> None:
      self.language = 'en'
      self.tts = None
      self.audio_path = "audio/file.mp3"

   def generate_audio(self, prompt):
      self.tts = gTTS(text=prompt, lang=self.language, slow=False)

   def save_audio(self):
      self.tts.save(self.audio_path)

   def play_audio(self):
      os.system("mpg321 " + self.audio_path)


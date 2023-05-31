"""contains the Text to speech models to use in the ai agent system"""

from gtts import gTTS
import os


class GTTS():
   """class to instantiate the audio generator"""
   def __init__(self) -> None:
      self.language = 'en'
      self.tts = None
      self.audio_path = "audio/file.mp3"

   def generate_audio(self, prompt):
      """creates the audio form"""
      self.tts = gTTS(text=prompt, lang=self.language, slow=False)

   def save_audio(self):
      """saves the audio to the audio_path"""
      self.tts.save(self.audio_path)

   def play_audio(self):
      """plays the audio file generated"""
      os.system("mpg321 " + self.audio_path)


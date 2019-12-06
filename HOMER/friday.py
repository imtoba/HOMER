import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
# engine = pyttsx3.init('espeak')
# voices = engine.getProperty()
# print(voices)

def speak(text):
    tts = gTTS(text= text, lang='en')
    tts.save("voice.mp3")
    playsound.playsound("voice.mp3")

speak('Hello SIR........ Welcome back!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! I am FRIDAY. Systems online! What shall I do for you? ')

def get_Audio(tes)






















# from gtts import gTTS
# from io import BytesIO
# mp3fp = BytesIO()
# tts = gTTS(text='Hello SIR........ Welcome back!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Does My voice sound natural to you?', lang='en')
# tts.write_to_fp(mp3fp)
# #playsound.playsound(mp3fp)# Play f
# import musicplayer
# class Song:
#     def __init__(self, f):
#         self.f = f
#     def readPacket(self, size):
#         return self.f.read(size)
#     def seekRaw(self, offset, whence):
#         self.f.seek(offset, whence)
#         return f.tell()
# player = musicplayer.createPlayer()
# player.queue = [Song(mp3_fp)]
# player.playing = True
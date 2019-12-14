import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    
    r = sr.Recognizer()
    print("Recognizer initialized")
    with sr.Microphone(device_index=7) as source:
        print("Getting Ambiance")
        r.adjust_for_ambient_noise(source,duration=5)
        print("Done Ambiance")
        print("Listening...")
        audio = r.listen(source)
        said = ""
        print("Listening Complete!")
        try:
            print("Recognizing...")
            said = r.recognize_google(audio,language='en-in')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()
to_say = []

print("1ts",to_say)
if "hello" in text:
    to_say.append("Hello, How are you...... ")
    print("ts hello \n",to_say)
if "what is your name"  in text or "what's your name" in text :
     print("whats \n")
     to_say.append("My Name is Friday!!")
if "the time" in text:
    to_say.append(" The current time is "+str(time.ctime()))



print("\n",to_say)
speak(''.join(to_say))
#it is important to install pyaudio to work with microphones
#pip install pyaudio

import speech_recognition as sr
import pyttsx3 as tts
import gtts
import pyaudio

r = sr.Recognizer()
your_voice = tts.init()

with sr.Microphone() as source:
    record = r.record(source, duration = 5)
    try:
        print("Recognizing...")
        
        text = r.recognize_google(record)
        print(text)
        
        your_voice.say(f"You said {text}")
        your_voice2 = gtts.gTTS(text)
        your_voice2.save("YourMic.mp3")
          
    except:
        print("I guess! Network Error")

your_voice.runAndWait()

pyaudio.PyAudio()
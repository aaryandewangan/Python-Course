import speech_recognition as sr 

file = "test.mp3"

sound = sr.Recognizer()

with sr.AudioFile(file) as source:
    record = sound.record(source)
    text = sound.recognize_google(record)
    print(text)
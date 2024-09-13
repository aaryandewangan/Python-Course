import speech_recognition as sr 

file_name = "test.mp3"

a = sr.Recognizer()

with sr.AudioFile(file_name) as source:
    recorder = a.record(source)
    text = a.recognize_google(recorder)
    print(text)
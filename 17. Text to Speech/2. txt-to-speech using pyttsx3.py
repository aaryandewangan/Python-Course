#the key difference between gtts and pyttsx3 is that gtts uses internet to run but pyttsx3 is offline and pyttsx3 is fast

import pyttsx3 as tts

a = tts.init()
text = input("Text you want to Convert: ")

#Volume
a.setProperty('volume', 100)
a.say(text)
#Voice
voices = a.getProperty('voices') 
for voice in voices: 
	# to get the info. about various voices in our PC 
	print("Voice:") 
	print(f"ID: {voice.id}") 
	print(f"Name: {voice.name}") 
	print(f"Age: {voice.age}") 
	print(f"Gender: {voice.gender}") 
	print(f"Languages Known: {voice.languages}")

a.runAndWait()
# to change voice
b = tts.init()
b.setProperty('volume', 100)

voice = b.getProperty('voices')
b.setProperty('voice', voice[1].id)  #1 for female voice and 0 for male voice

b.say("Hello world")


b.runAndWait()
# for text to speech recognition, there is a module package called 'gtts' which states Google Text to Speech
#we will use 'gTTS library' inside 'gtts package'
#pip instal gtts
#playsound is a module used to play the speech that are already in mp3 format
#all modules that can be used for text to speech - gTTS, pyttsx3, playsound, soundfile, transformers, datasets, sentencepiece, openai

import gtts   
import gtts.lang
from playsound import playsound

text = input("Enter your Text that need to be Converted: ")
a = gtts.gTTS(text, lang='ja', slow=False)   #gtts creates text to speech in mp3 format so it is important to save the file in mp3 format
a.save("text.mp3")

# all available languages along with their IETF tag
print(gtts.lang.tts_langs())

b = playsound("./text.mp3")   #and to play gtts you need playsound module
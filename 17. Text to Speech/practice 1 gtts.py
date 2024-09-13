import gtts
import playsound as ps

text = gtts.gTTS("Hello World", lang = 'en')
text.save("Hello.mp3")

ps.playsound("./Hello.mp3")
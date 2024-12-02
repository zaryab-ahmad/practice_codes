import gtts 
import playsound

# make request to google to get synthesis
tts = gtts.gTTS("Hello world")
tts.save("hello.mp3")
# play the audio file
#playsound("hello.mp3")
zaryab = gtts.gTTS(" my name is zaryab ahmad khan ")
zaryab.save("zaryab.mp3")
playsound("zaryab.mp3")
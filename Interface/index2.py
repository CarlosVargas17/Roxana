import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)
engine.say("P.M")
# engine.save_to_file(text,"voz.mp3")
engine.runAndWait()
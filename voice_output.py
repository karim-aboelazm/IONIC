import pyttsx3
import datetime

def Say(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print(f'Ionic : {text}\n')
    engine.say(str(text))
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         Say("Good Morning!")
     elif hour>=12 and hour<18:
         Say("Good Afternoon!")
     else:
        Say("Good Evening!")



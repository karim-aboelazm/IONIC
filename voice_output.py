import pyttsx3

def Say(text):
    
    engine = pyttsx3.init('sapi5')

    # Setting up voice rate
    engine.setProperty('rate', 160)

    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(str(text))
    engine.runAndWait()

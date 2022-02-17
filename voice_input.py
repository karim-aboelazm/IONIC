import speech_recognition as sr

def Listen():
    mic = sr.Recognizer()   # Recognizer object
    with sr.Microphone() as source: # Microphone object
        mic.pause_threshold = 1 # wait for a second
        audio = mic.listen(source) # listen to the voice input 
    try:
        query = mic.recognize_google(audio,language='en') # Query of Listened   
    except:
       return   # None
    query = str(query)
    return query.lower()

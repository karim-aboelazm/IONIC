from functions_1 import *
from functions_2 import *

def singleCommand(query): 
    query = str(query)
    if 'time' in query:
        get_time()
    elif 'date' in query:
        get_date()
    elif 'day' in query:
        get_day()
    elif "break" in query:
        break_assistant()
    elif "open word" in query:
        open_word()
    elif "open powerpoint" in query:
        open_powerpoint()
    elif "open vscode" in query:
        open_vscode()
    elif "open chrome" in query:
        open_chrome()
    elif "open notepad" in query:
        open_notepad()
    elif "open access" in query:
        open_access()
    elif "open excel" in query:
        open_excel()
    elif "open zoom" in query:
        open_zoom()
    elif "open cmd" in query:
        open_cmd()
    elif "close word" in query:
        close_word()
    elif "close powerpoint" in query:
        close_powerpoint()
    elif "close vscode" in query:
        close_vscode()
    elif "close chrome" in query:
        close_chrome()
    elif "close notepad" in query:
        close_notepad()
    elif "close access" in query:
        close_access()
    elif "close excel" in query:
        close_excel()
    elif "close zoom" in query:
        close_zoom()
    elif "close cmd" in query:
        close_cmd()
    # elif "internet speed" in query:
    #     check_internet_speed()
    elif "nasa news" in query:
        Nasa_News()
    elif "egy news" in query:
        egy_news()  
    elif "introduction" in query:
        introduction()

def multiCommand(tag,query):

    if "wikipedia" in tag:
       wiki(query)
        
    elif "google" in tag:
        google()
    
    elif "YouTube" in tag:
        youtube(query)

    elif "website" in tag:
        website(query)

    elif "playvideo" in tag:
        playmusic(query)

    elif "remember that" in tag:
       remember(query)

    elif "what do you remember" in tag:
        remind()

    elif "weather" in tag:
        get_weather(query)

    elif "temperature" in tag:
        get_temperature(query)

    elif "calculate" in tag:
        calc(query)

    elif "whatsapp massage" in tag:
        whatsapp_messaging()

    elif "whatsapp call" in tag:
        whatsapp_calling()

    elif "whatsapp video" in tag:
       whatsapp_video_call()

    elif "whatsapp chat" in tag:
       whatsapp_chatting()

    elif "how to" in tag:
        how_to_make(query)
    
    elif "recognize" in tag:
        recognize_peace(query)

    elif "corona" in tag:
        covid(query)

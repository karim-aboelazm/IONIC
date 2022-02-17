import time
import datetime
import wikipedia
import webbrowser
import pywhatkit
from os import startfile,system,rename
from pywikihow import search_wikihow
import requests
from PIL import Image # pillow
from newscatcherapi import NewsCatcherApiClient
import speedtest
import wolframalpha
from pyautogui import click, position
from keyboard import write , press
from voice_input import Listen
from voice_output import Say

# this function for getting time now
def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    Say(f"Time Now Is : {time}")

# this function for getting datetime now
def get_date():
    date = datetime.date.today()
    Say(f"Today Is : {date}")

# this function for getting today name
def get_day():
    day = datetime.datetime.now().strftime("%A")
    Say(f"Today Is : {day}")

def open_word():
    click(x=13, y=754)
    time.sleep(3)
    write('word')
    time.sleep(3)
    press('enter')

def close_word():
    time.sleep(1)
    system('taskkill /f /im WINWORD.EXE')

def open_chrome():
    click(x=13, y=754)
    time.sleep(3)
    write('google chrome')
    time.sleep(3)
    press('enter')

def close_chrome():
    time.sleep(1)
    system('taskkill /f /im chrome.exe')

def open_excel():
    click(x=13, y=754)
    time.sleep(3)
    write('excel')
    time.sleep(3)
    press('enter')

def close_excel():
    time.sleep(1)
    system('taskkill /f /im EXCEL.EXE')

def open_access():
    click(x=13, y=754)
    time.sleep(3)
    write('access')
    time.sleep(3)
    press('enter')

def close_access():
    time.sleep(1)
    system('taskkill /f /im MSACCESS.EXE')

def open_zoom():
    click(x=13, y=754)
    time.sleep(3)
    write('zoom')
    time.sleep(3)
    press('enter')

def close_zoom():
    time.sleep(1)
    system('taskkill /f /im zoom.exe')

def open_vscode():
    click(x=13, y=754)
    time.sleep(3)
    write('vscode')
    time.sleep(3)
    press('enter')

def close_vscode():
    time.sleep(1)
    system('taskkill /f /im Code.exe')

def open_powerpoint():
    click(x=13, y=754)
    time.sleep(3)
    write('powerpoint')
    time.sleep(3)
    press('enter')

def close_powerpoint():
    time.sleep(1)
    system('taskkill /f /im POWERPNT.EXE')

def open_notepad():
    click(x=13, y=754)
    time.sleep(3)
    write('notepad')
    time.sleep(3)
    press('enter')

def close_notepad():
    time.sleep(1)
    system('taskkill /f /im notepad.exe')

def open_downloads():
    time.sleep(1)
    startfile('C:\\Users\\Karim Aboelazm\\Downloads')
   
def open_cmd():
    click(x=13, y=754)
    time.sleep(3)
    write('cmd')
    time.sleep(3)
    press('enter')

def close_cmd():
    time.sleep(1)
    system('taskkill /f /im cmd.exe')

def check_internet_speed():
    Say('Checking Sir ...')
    speed = speedtest.Speedtest()
    download_speed = speed.download()
    correct_Dspeed = int(download_speed/800000)
    upload_speed = speed.upload()
    correct_Uspeed = int(upload_speed/800000)
    Say(f'Download speed is {correct_Dspeed} m/s , upload speed is {correct_Uspeed} m/s')

def break_assistant():   
    Say("Ok Sir , You Can Call Me At Anytime ..")
    Say("Just Say Wake Up !")
    exit()  

def Nasa_News():
    Say('Getting Data from Nasa ....')
    Api_key = "TDhA4g5vdtJFf41rQdx1pRfrNJiT2CneJVgwEVLs"
    url = "https://api.nasa.gov/planetary/apod?api_key="+str(Api_key)
    
    today = datetime.date.today()
    date = today
    # for i in range(10):
    #     date = today - datetime.timedelta(days=i+1)
    parameters = {'date':str(date)}
    request = requests.get(url,params=parameters)
    Data = request.json()
    Info = Data['explanation']
    title = Data['title']

    image_url = Data['url']
    image_request = requests.get(image_url)

    filename = str(date)+'.jpg'
    with open(filename,'wb') as f:
        f.write(image_request.content)

    p1 = "E:\\AI_Voice_Project\\Project\\Coding\\"+str(filename)
    p2 = "E:\\AI_Voice_Project\\Project\\Coding\\NASA_DATA\\"+str(filename)
    rename(p1,p2)
    img = Image.open(p2)
    img.show()
    Say(f"title : {title}")
    Say(f"According to Nasa : {Info}")

def egy_news():
    Say("Getting News from The internet..")
    api_key = 'v2KkHYXP67qO2Y29E0420Mx-idWH1wrHqt-cCCopW04'
    newscatcherapi = NewsCatcherApiClient(x_api_key=api_key)

    all_articles = newscatcherapi.get_search(q='*',
                                            lang='en',
                                            countries='EG',
                                            page_size=100)
    Say(f"Title [1] {all_articles['articles'][0]['title']}:\n{all_articles['articles'][0]['excerpt']}")

    i = 1
    stm = ''
    while i<16:
        stm = Listen()
        if stm == 'next':
            Say(f"Title [{i+1}] {all_articles['articles'][i]['title']}:\n{all_articles['articles'][i]['excerpt']}")
            i+=1
        else:
            break

def get_error(query): 
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
    elif "internet speed" in query:
        check_internet_speed()
    elif "nasa news" in query:
        Nasa_News()
    elif "egy news" in query:
        egy_news()  

def wolframalpha_setting(query):
    api_key = "WY8246-963Y55UH56"
    request = wolframalpha.Client(api_key)
    response = request.query(query)
    try:
        return next(response.results).text
    except:
        Say("Something went wrong Sir..")

def whatsapp_msg(name,message):
    click(x=688, y=756)
    time.sleep(20)
    click(x=80, y=102)
    time.sleep(2)
    write(name)
    time.sleep(2)
    click(x=279, y=248)
    time.sleep(2)
    click(x=862, y=703)
    time.sleep(2)
    write(message)
    time.sleep(2)
    press('enter')

def whatsapp_call(name):
    click(x=688, y=756)
    time.sleep(20)
    click(x=80, y=102)
    time.sleep(2)
    write(name)
    time.sleep(2)
    click(x=279, y=248)
    time.sleep(2)
    click(x=1203, y=44)

def whatsapp_video(name):
    click(x=688, y=756)
    time.sleep(20)
    click(x=80, y=102)
    time.sleep(2)
    write(name)
    time.sleep(2)
    click(x=279, y=248)
    time.sleep(2)
    click(x=1147, y=51)

def whatsapp_chat(name):
    click(x=688, y=756)
    time.sleep(20)
    click(x=80, y=102)
    time.sleep(2)
    write(name)
    time.sleep(2)
    click(x=279, y=248)
    time.sleep(2)

def get_input_error(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        Say(wikipedia.summary(name))
    
    elif "google" in tag:
        name = str(query).replace("google","")
        name = name.replace("search for","")
        name = name.replace("search","")
        pywhatkit.search(name)
    
    elif "YouTube" in tag:
        query = str(query).replace("YouTube","").replace("Open Youtube","").replace("in YouTube","").replace(" ","")
        youtube = "https://www.youtube.com/results?search_query="+query
        webbrowser.open(youtube)

    elif "website" in tag:
        query = str(query).replace("open","").replace(" ","")
        site = "https://www."+str(query)+".com/"
        webbrowser.open(site)

    elif "playvideo" in tag:
        query = str(query).replace("open video","")
        query = query.replace("start video","")
        query = query.replace("YouTube video","")
        query = query.replace("play on YouTube","")
        query = query.replace(" ","")
        query = query.replace("play","")
        pywhatkit.playonyt(query)

    elif "remember that" in tag:
        rmsg = str(query).replace("remember that","")
        rmsg = rmsg.replace("remind me that","")
        Say(f"You Told me to remind you that {rmsg}")
        remember = open('remind.txt','w')
        remember.write(rmsg)
        remember.close()

    elif "what do you remember" in tag:
        remember_message = open('remind.txt','r')
        Say(f"You Told me to remember you that {str(remember_message.read())}")

    elif "weather" in tag:
        query = str(query).replace("weather in","")
        query = query.replace("what is weather in","")
        query = query.replace("weather for","")
        api_key = "382898aca8ccf36781e1452584f5d79a"
        root_url = "http://api.openweathermap.org/data/2.5/weather?"
        url = f"{root_url}appid={api_key}&q={query}"
        r = requests.get(url)
        data = r.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            weather_stat = data["weather"][0]["description"]
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            wind_speed = data["wind"]["speed"]
            Say(f"Weather Information in {query}")
            Say(f"The Weather conditions is {weather_stat}")
            Say(f"The temperature is {temp} Kelvin")
            Say(f"The pressure is {pressure} hpa")
            Say(f"The humidity is {humidity} %")
            Say(f"The wind speed is {wind_speed} m/s")
        else:
            Say("Something went wrong sir Check Again..")

    elif "temperature" in tag:
        query = str(query).replace("what is the temperature","temperature in")
        query = query.replace("temperature for","temperature in")
        Say(wolframalpha_setting(query))

    elif "calculate" in tag:
        query = str(query).replace("multiply","*")
        query = query.replace("in","*")
        query = query.replace("into","*")
        query = query.replace("power","**")
        query = query.replace("to the power","**")
        query = query.replace("plus","+")
        query = query.replace("minus","-")
        query = query.replace("divide","/")
        query = query.replace("over","/")
        query = query.replace("div","/")
        try:
            Say(f'The result is : {wolframalpha_setting(query)}')
        except:
            Say("I Can Not Calculate This Query")

    elif "whatsapp massage" in tag:
        Say('For Whom Sir ..')
        name = Listen()
        Say('Ok Sir , Tell me The Message..')
        query = Listen()
        whatsapp_msg(str(name),str(query))

    elif "whatsapp call" in tag:
        Say('For Whom Sir ..')
        query = Listen()
        Say(f'Ok Sir , Calling now to {query} ..')
        whatsapp_call(str(query))

    elif "whatsapp video" in tag:
        Say('For Whom Sir ..')
        query = Listen()
        Say(f'Ok Sir , Making Video With {query} ..')
        whatsapp_video(str(query))

    elif "whatsapp chat" in tag:
        Say('For Whom Sir ..')
        query = Listen()
        Say(f'Ok Sir , Opening whatsapp chat With {query} ..')
        whatsapp_chat(str(query))

    elif "how to" in tag:
        Say('Getting Data from The Internet...')
        max_result = 1
        how_to = search_wikihow(query, max_result)
        assert len(how_to) == max_result
        Say(how_to[0].summary)
    
    
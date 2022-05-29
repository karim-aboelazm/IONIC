import time
import wikipedia
import webbrowser
import pywhatkit
from pywikihow import search_wikihow
import requests
import wolframalpha
import bs4
from pyautogui import click
from keyboard import write , press
from voice_input import Listen
from voice_output import Say

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

def wiki(query):
    name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
    Say(wikipedia.summary(name))

def google():
    Say("Searching for What Sir ...")
    search = Listen()
    pywhatkit.search(str(search))

def youtube(query):
    query = str(query).replace("YouTube","").replace("Open Youtube","").replace("in YouTube","").replace(" ","")
    youtube = "https://www.youtube.com/results?search_query="+query
    webbrowser.open(youtube)

def website(query):
    query = str(query).replace("open","").replace(" ","")
    site = "https://www."+str(query)+".com/"
    webbrowser.open(site)

def playmusic(query):
    query = str(query).replace("open video","")
    query = query.replace("start video","")
    query = query.replace("YouTube video","")
    query = query.replace("play on YouTube","")
    query = query.replace(" ","")
    query = query.replace("play","")
    pywhatkit.playonyt(query)

def remember(query):
    rmsg = str(query).replace("remember that","")
    rmsg = rmsg.replace("remind me that","")
    Say(f"You Told me to remind you that {rmsg}")
    rem = open('remind.txt','w')
    rem.write(rmsg)
    rem.close()

def get_temperature(query):
    query = str(query).replace("what is the temperature","temperature in")
    query = query.replace("temperature for","temperature in")
    Say(wolframalpha_setting(query))


def remind():
    remember_message = open('remind.txt','r')
    Say(f"You Told me to remember you that {str(remember_message.read())}")

def get_weather(query):
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

def calc(query):
    query = str(query).replace("multiply","*")
    query = query.replace("in","*")
    query = query.replace("into","*")
    query = query.replace("plus","+")
    query = query.replace("minus","-")
    query = query.replace("divide","/")
    query = query.replace("over","/")
    query = query.replace("div","/")
    result = eval(str(query))
    Say(f'The result is : {result}')

def whatsapp_messaging():
    Say('For Whom Sir ..')
    name = Listen()
    Say('Ok Sir , Tell me The Message..')
    query = Listen()
    whatsapp_msg(str(name),str(query))

def whatsapp_calling():
    Say('For Whom Sir ..')
    query = Listen()
    Say(f'Ok Sir , Calling now to {query} ..')
    whatsapp_call(str(query))

def whatsapp_video_call():
    Say('For Whom Sir ..')
    query = Listen()
    Say(f'Ok Sir , Making Video With {query} ..')
    whatsapp_video(str(query))

def whatsapp_chatting():
    Say('For Whom Sir ..')
    query = Listen()
    Say(f'Ok Sir , Opening whatsapp chat With {query} ..')
    whatsapp_chat(str(query)) 

def how_to_make(query):
    Say('Getting Data from The Internet...')
    max_result = 1
    how_to = search_wikihow(query, max_result)
    assert len(how_to) == max_result
    Say(how_to[0].summary)

def recognize_peace(query):
    query = str(query).replace("he is ","").replace("she is ","")
    query = str(query)
    Say(f"Welcome to You {query} \nNice to meet you !")

def covid(query):
    command = str(query).replace(" ","")
    Say("Tell Me Which Country You Want To Know It's Data ...")
    country = Listen()
    country = str(country).lower()
    url = f"https://www.worldometers.info/coronavirus/country/{country.lower()}/"
    results = requests.get(url)
    soups = bs4.BeautifulSoup(results.text,'lxml')
    corona = soups.find_all('div',class_="maincounter-number")
    Data = []
    for case in corona:
        span = case.find('span')
        Data.append(span.string)
    cases ,Death, recovored = Data
    Say(f"The corona virus in {country} Statistics are..")
    Say(f"The Number of all Cases     is      {cases} person")
    Say(f"The Number of all Death     is      {Death} person")
    Say(f"The Number of all Recovered is  {recovored} person")
    webbrowser.open(f"https://www.google.com/search?q={country.lower()}+coronavirus")
    

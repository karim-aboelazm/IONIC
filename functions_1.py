import time
import datetime
import webbrowser
import bs4
from os import startfile,system
import requests
import speedtest
from pyautogui import click
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
    Say("Online Or Local Sir ...")
    stm = Listen()
    if str(stm) == "local":
        click(x=13, y=754)
        time.sleep(3)
        write('word')
        time.sleep(3)
        press('enter')
    elif str(stm) == "online":
        webbrowser.open("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=637851054783314025.NDQzZjQ3YmYtNzEwOS00ODRlLWE0M2EtOGIxNDI4MmM3MGE4ODRkNjFkOTQtYjNmZi00NTY2LTgzODktN2Y4YjRjNTM3N2Ri&ui_locales=en-US&mkt=en-US&state=hQjvNARizXjF5CFEQqRkWO7ZWRwmZnnr_FrC5CB-xii4Jgn8a1zBVSScfHn6sIZolgH1IQO9JFyiRbTsZcT_N59eAGCLYIx6KQ60KF2kedv81S2YApMdi9l3ISNPjt54gZjHWZeOWoYk26zaifK6PAl64pRcZflM-ErG9MycKjGq-mAPMHgbZ-1i1mSoW6TjLdl-qleSyUfvKUn55AzfhEI0Xs4WPm8CTZ_q8hzwEvK9km_5k0SJkRr-sMMB9Mi_VWmbmaqNlpGV-CTyrcEPcAUy7rL65oeLIFfbD2wnmWneTz466woigXPT6ixHAucj&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.12.1.0")
    else:
        return None

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
    Say("Online Or Local Sir ...")
    stm = Listen()
    if str(stm) == "local":
        click(x=13, y=754)
        time.sleep(3)
        write('excel')
        time.sleep(3)
        press('enter')
    elif str(stm) == "online":
        webbrowser.open("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=637851054783314025.NDQzZjQ3YmYtNzEwOS00ODRlLWE0M2EtOGIxNDI4MmM3MGE4ODRkNjFkOTQtYjNmZi00NTY2LTgzODktN2Y4YjRjNTM3N2Ri&ui_locales=en-US&mkt=en-US&state=hQjvNARizXjF5CFEQqRkWO7ZWRwmZnnr_FrC5CB-xii4Jgn8a1zBVSScfHn6sIZolgH1IQO9JFyiRbTsZcT_N59eAGCLYIx6KQ60KF2kedv81S2YApMdi9l3ISNPjt54gZjHWZeOWoYk26zaifK6PAl64pRcZflM-ErG9MycKjGq-mAPMHgbZ-1i1mSoW6TjLdl-qleSyUfvKUn55AzfhEI0Xs4WPm8CTZ_q8hzwEvK9km_5k0SJkRr-sMMB9Mi_VWmbmaqNlpGV-CTyrcEPcAUy7rL65oeLIFfbD2wnmWneTz466woigXPT6ixHAucj&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.12.1.0")
    else:
        return None

def close_excel():
    time.sleep(1)
    system('taskkill /f /im EXCEL.EXE')

def open_access():
    Say("Online Or Local Sir ...")
    stm = Listen()
    if str(stm) == "local":
        click(x=13, y=754)
        time.sleep(3)
        write('access')
        time.sleep(3)
        press('enter')
    elif str(stm) == "online":
        webbrowser.open("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=637851054783314025.NDQzZjQ3YmYtNzEwOS00ODRlLWE0M2EtOGIxNDI4MmM3MGE4ODRkNjFkOTQtYjNmZi00NTY2LTgzODktN2Y4YjRjNTM3N2Ri&ui_locales=en-US&mkt=en-US&state=hQjvNARizXjF5CFEQqRkWO7ZWRwmZnnr_FrC5CB-xii4Jgn8a1zBVSScfHn6sIZolgH1IQO9JFyiRbTsZcT_N59eAGCLYIx6KQ60KF2kedv81S2YApMdi9l3ISNPjt54gZjHWZeOWoYk26zaifK6PAl64pRcZflM-ErG9MycKjGq-mAPMHgbZ-1i1mSoW6TjLdl-qleSyUfvKUn55AzfhEI0Xs4WPm8CTZ_q8hzwEvK9km_5k0SJkRr-sMMB9Mi_VWmbmaqNlpGV-CTyrcEPcAUy7rL65oeLIFfbD2wnmWneTz466woigXPT6ixHAucj&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.12.1.0")
    else:
        return None

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
    Say("Online Or Local Sir ...")
    stm = Listen()
    if str(stm) == "local":
        click(x=13, y=754)
        time.sleep(3)
        write('powerpoint')
        time.sleep(3)
        press('enter')
    elif str(stm) == "online":
        webbrowser.open("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=637851054783314025.NDQzZjQ3YmYtNzEwOS00ODRlLWE0M2EtOGIxNDI4MmM3MGE4ODRkNjFkOTQtYjNmZi00NTY2LTgzODktN2Y4YjRjNTM3N2Ri&ui_locales=en-US&mkt=en-US&state=hQjvNARizXjF5CFEQqRkWO7ZWRwmZnnr_FrC5CB-xii4Jgn8a1zBVSScfHn6sIZolgH1IQO9JFyiRbTsZcT_N59eAGCLYIx6KQ60KF2kedv81S2YApMdi9l3ISNPjt54gZjHWZeOWoYk26zaifK6PAl64pRcZflM-ErG9MycKjGq-mAPMHgbZ-1i1mSoW6TjLdl-qleSyUfvKUn55AzfhEI0Xs4WPm8CTZ_q8hzwEvK9km_5k0SJkRr-sMMB9Mi_VWmbmaqNlpGV-CTyrcEPcAUy7rL65oeLIFfbD2wnmWneTz466woigXPT6ixHAucj&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.12.1.0")
    else:
        return None

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
    parameters = {'date':str(date)}
    request = requests.get(url,params=parameters)
    Data = request.json()
    Info = Data['explanation']
    title = Data['title']

    image_url = Data['url']
    webbrowser.open(image_url)
    Say(f"title : {title}")
    Say(f"According to Nasa : {Info}")

def egy_news():
    Say("Getting News from The internet..")
    url = "https://english.ahram.org.eg/Portal/1/Egypt.aspx"
    results = requests.get(url)
    soup = bs4.BeautifulSoup(results.text,'lxml')
    titles = []
    descriptions = []
    div = soup.find_all('div',class_="portal-section")
    for h in div:
        title = h.find('h3')
        des = h.find('p')
        titles.append(title.string)
        descriptions.append(des.string)
    Say(f"Category [1] : {titles[0]}")
    Say(f"Description : {descriptions[0][2:-2]}")
    print("="*50)
    stm = ''
    i = 0
    while i < (len(titles)-1):
        stm = Listen()
        if stm == 'next':
            print()
            Say(f"Category [{i+2}] : {titles[i+1]}")
            Say(f"Description : {descriptions[i+1][2:-2]}")
            print("="*50)
            i+=1
        else:
            break

            


from re import T
import cv2 # webcam access
from numpy import number # numpy
import pyttsx3 # text to speech
import requests # request urls
import scipy as sp
import speech_recognition as sr # speech to text
import datetime # return current date time
import os # helps to perform os actions
import random # gives random elements
from requests import get
import wikipedia # wikipedia
import webbrowser
import pywhatkit as kit # sent message through whatsapp web
import smtplib # creates interface between to mails
import sys # to perform action related the system
import time # return current date/time
import pyjokes # return jokes
import pyautogui # gui auto actions
import shutil
import json
from unittest import result
from urllib import request
from urllib.request import urlopen
import PyPDF2 # used to read pdf
from bs4 import BeautifulSoup # weather api
import operator # used for calculations
import subprocess
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Virtual_UI import QMainWindow


class MainThread(QThread):
    def __init__(self) -> None:
        super(MainThread, self).__init__()
    
    def run(self):
        self.TaskExecution()


# creating engine for voice of our virtual assistant [0] for female voice and [1] for male voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[0].id)


# converts text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# this function used to take command from the user and convert speech into text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listning....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        Query = r.recognize_google(audio, language="en-in")
        print(f"user said: {Query}")
        print(f"\nWorking on....\n")

    except Exception as e:
        speak('say that again please..')
        take_command()
        return None
    
    Query = Query.lower()
    return Query


# with this function vi wishes us
def wish():
    hour = int(datetime.datetime.now().hour)
    
    strTime = datetime.datetime.now().strftime("%H:%M")

    if hour >= 0 and hour <= 12:
        speak(f"\nHellow, Good Morning Sir ! it's {strTime} AM")
    elif hour >= 12 and hour <= 18:
        speak(f"\nHellow, Good Afternoon Sir ! it's {strTime} PM")
    else:
        speak(f"\nHellow, Good Evening Sir ! it's {strTime} PM")


# set username function
def set_username():
    # speak("\nsir, what should i call you?")
    # uname = take_command()
    # speak(f"wellcome mister {uname}")

    speak('\n\tThis is Prince Your Virtual Assistant, How may i help You sir ?\n')


# basic function for sending email: it will be advanced
def sendEmail(mail_to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'password')
    server.sendmail('your email id', mail_to, content)
    server.close()


# function for news gathering using API
def news():
    try:
        main_url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=API_KEY=9236ddf4565e44c4992011ba9aa93679"

        main_page = requests.json(main_url).load()
        # fetch main page ^
        articles = main_page["articles"]
        # fetch articles >
        head = []
        for ar in articles:
            head.append(ar['title'])
        for i in range(len()):
            speak(f"today's news is: {head[1]}")

    except Exception as e:
        speak("sorry sir, there is some technical issues with news api, please try again after some time!")


# function for forecasting the weather conditions of given locations
def weather():
    try:
        speak("Tell me the City Name !")
        city = take_command().lower()
        speak('please wait sir, i am finding the weather conditions on given location............')
        search = f"temperature in {city}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"weather cunditions in {city} is: {temp}")

    except Exception as e:
        speak("Sorry sir !\n\tthere is some technical issues, please try again after sometime\n")


# this function is used to read an pdf or document
def read_pdf():
    speak("please enter the path of the document")
    doc_path = input("\nEnter the Path of the Document: ")
    document = open(f"{doc_path}",'rb')
    pdfReader = PyPDF2.PdfFileReader(document)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this document is {pages}")
    speak("sir, please enter the page number i have to read")
    pg = int(input("\nPage Number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


# functions : part of calculation action
def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        'divided' : operator.__truediv__,
    }[op]
def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
            
    return get_operator_fn(oper)(op1, op2)


# calcution function
def calculations():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("say! what you want to calculate ?, example: 5 + 5")
            print('Listning....')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        my_stringe = r.recognize_google(audio)
        print(my_stringe)
        
        speak(f"Your result is: {eval_binary_expr(*(my_stringe.split()))}")

    except Exception as e:
        speak("\ni am unable to understand, what are you saying....tell me again please\n")
        calculations()


# function used to find locatiion through ip
def location_find():
    speak("\nwait sir!, let me check the correct data......")

    try:
        response = requests.get('https://api64.ipify.org?format=json').json()
        ip_add = response["ip"]

        response = requests.get(f'https://ipapi.co/{ip_add}/json/').json()
        location_data = {
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }

        speak(location_data)

    except Exception as e:
        speak("sorry sir, we are suffering from network issue, please try again!")






if __name__ == "__main__":
    clear = lambda:os.system('cls')

    clear()
    wish()
    set_username()
    while True:

        Query = take_command().lower()

        #..................................logic building for tasks......................................
        if "open notepad" in Query:
            path1 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(path1)

        elif ("open browser" or "browser") in Query:
            speak('what do you want to search on browser ?')
            search = take_command().lower()
            webbrowser.open(f"{search}")

        elif ("search") in Query:
            speak('what do you want to search ?')
            search = take_command().lower()
            webbrowser.open(f"{search}")

        elif ("open google" or "google") in Query:
            # speak('what do you want to search on google ?')
            # search = take_command().lower()
            # webbrowser.open(f"{search}")
            path2 = "https://www.google.com/"
            os.startfile(path2)

        elif ("open youtube" or "youtube") in Query:
            # webbrowser.open(f"www.youtube.com")
            path3 = "https://www.youtube.com/"
            os.startfile(path3)

        elif ("open firefox" or "firefox") in Query:
            path4 = "https://support.mozilla.org/en-US/products/firefox"
            os.startfile(path4)

        elif "wikipedia" in Query:
            speak('Searching Wikipedia...')
            Query = Query.replace('wikipedia', "")
            results = wikipedia.summary(Query, sentences=4)
            speak('according to wikipedia.......')
            speak(results)
            print(results)

        elif ("open facebook" or "facebook") in Query:
            path6 = "https://www.facebook.com/"
            os.startfile(path6)

        elif ("open twitter" or "twitter") in Query:
            path7 = "https://twitter.com/"
            os.startfile(path7)

        elif ("open amazon" or "twitter") in Query:
            path8 = "https://www.amazon.com/"
            os.startfile(path8)

        elif 'open stackoverflow' in Query:
            speak("Opening Stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "open camera" in Query or "camera" in Query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)

                if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to quit.
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "command prompt" in Query or "cmd" in Query:
            os.system('start cmd')

        elif ("play music" or "play song") in Query:
            music_dir = "C:\\music_dir"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)

            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in Query:
            ip = get('https://api.ipify.org').text
            speak(f'Your IP Address is: {ip}')

        elif ("send message" or "message") in Query:
            speak("Enter a mobile number to send message: ")
            number = take_command()
            speak("Enter a text message to be send")
            msg = take_command().lower()
            kit.sendwhatmsg_instantly(f"+{number}", f"{msg}", 10)

        elif ("play song on youtube" or "play on youtube") in Query:
            speak("Please tell me a song name?")
            song_name = take_command().lower()
            kit.playonyt(f"{song_name}")

        elif ("email") in Query:

            try:
                speak("Enter a email address to send message: ")
                mail_to = input()
                speak("Enter a text message to be send")
                content = take_command().lower()
                sendEmail(mail_to, content)
                speak(f"Your Email has been sent successfully to {mail_to}")

            except Exception as e:
                print(e)
                speak("Sorry sir ! i am unable to sent message to this address please try again after some time")
        
        elif "prince" in Query:
            wish()
            speak(f"Prince in your service ! please tell me How may i help you sir ?")
            take_command()

        elif ("tell me a joke" or "joke") in Query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif ("shut down" or "shutdown") in Query:
            speak("ok, shutting down the system.....")
            os.system("shutdown /s /t 6")

        elif "restart" in Query:
            speak("ok, restarting down the system.....")
            os.system("shutdown /r /t 6")

        elif "sleep" in Query:
            os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")

        elif "switch the window" in Query:
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "who i am" in Query:
            speak("If you talk then definitely you r human.")

        elif 'reason for you' in Query:
            speak("I was created as a Minor project by Rathod ")

        elif "don't listen" in Query or "stop listening" in Query:
            speak("for how much time you want to stop me from listening commands")
            a = int(take_command())
            time.sleep(a)
            print(a)

        elif "close notepad" in Query:
            speak("okey sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        
        elif "close camera" in Query:
            speak("okey sir closing camera")
            os.system('wmic process where name="camera.exe" delete')

        elif "news" in Query:
            speak("please wait sir, fetching the latest trendings.....")
            news()

        elif "current location" in Query or "where i am" in Query or "where are you" in Query or "location" in Query:
            location_find()

        elif "calculate" in Query or "calculations" in Query or "mathematics" in Query or "calculation" in Query:
            calculations()

        elif "weather" in Query:
            weather()

        elif ("read pdf" or "read document") in Query:
            read_pdf()

        elif "hide current directory" in Query or "hide files" in Query or "hide this folder" in Query or "visible for everyone" in Query or "visible to everyone" in Query:
            speak("sir, please tell me, you want to hide this folder or make it visible for everyone ?")
            Condition = take_command().lower()
            if "hide" in Condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in this folder is now hidden!")
            elif "visible" in Condition:
                os.system("attrib -h /s /d")
            elif "leave it" in Condition or "leave for now" in Condition:
                speak("ok sir!")

        elif ("thank you" or "thanks") in Query:
            speak("it's my pleasure, sir")

        elif "how are you" in Query:
            speak("i am well thanks, and what about you ?")
            take_command()

        elif ("good" or "fine") in Query:
            speak("ok!")

        elif "your name" in Query:
            my_name = "Prince"
            speak(f'sir, my name is {my_name} A Virtual Assistant & i am working under my owner, thank you !')

        elif ("who made you" or "who created you") in Query:
            speak("I have been created by Shivam Singh Rathod")

        elif "your owner" in Query:
            owner = "shivam , a college student of Rewa Engineering College"
            speak(f'my owner is : {owner}')

        elif ("no thanks" or "no") in Query:
            speak("thanks for using me sir!, have a good day")
            sys.exit()

        elif ("by" or "bye") in Query:
            speak("thanks for using me sir!, have a good day")
            sys.exit()

        elif "i love you" in Query:
            speak("sorry, i want to be single and it is against our policy")

        elif "time" in Query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the current time is: {strTime}")

        elif "date" in Query:
            strDate = datetime.datetime.now().strftime("%m/%d/%Y")
            speak(f"sir, the current date is: {strDate}")

        elif ('ppt' or 'presentation') in Query:
            speak("Opening Virtual Assistant ppt")
            power = r""
            os.startfile(power)

        else:
            speak("I am unable to understant what you want to say, tell me again please....")
            take_command()

        speak("sir! do you have any other Query? ")
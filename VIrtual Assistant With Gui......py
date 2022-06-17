# developer rights : Shivam Singh Rathod (Rewa Engineering College - MP2)
# please install all required modules before execution
# it may be possible that some included API would Not Work properly
# in this case please replace with new API.
# it is a progressive Project : So for updated virsion please kepp eyes on repos.
# please check directories positions or paths on your devise before exec.

from re import T
from socket import timeout
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
import smtplib, ssl # creates interface between to mails
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
from PyQt5 import QtWidgets, QtCore, QtGui # modules used to implement Qt tools
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Virtual_UI import Ui_Virtual_UI





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
    try:
        speak("Enter sender Email Address")
        sender_email = input("\nEnter sender email: ")
        speak("Enter Your Password: ")
        password = input("\nEnter your password:")
    
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, mail_to, content)
    
    except Exception as e:
            print(e)
            print("Sorry sir, we can not send message at this email address")
    finally:
            server.quit()
   

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
def weather(self,):
    try:
        speak("Tell me the City Name !")
        city = self.take_command().lower()
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



class MainThread(QThread):
    def __init__(self) -> None:
        super(MainThread, self).__init__()


    def run(self):
        self.TaskExecution() #dont give self : it gives more than one positional argument bug

    # this function used to take command from the user and convert speech into text
    def take_command(self):
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
            # speak('say that again please..')
            # self.take_command()
            return self.take_command()
            
        Query = Query.lower()
        return Query
    
    
    def TaskExecution(self):
        clear = lambda:os.system('cls')
    
        clear()
        wish()
        set_username()
        while True:
            self.Query = self.take_command().lower()
    
            #..................................logic building for tasks......................................
            if "open notepad" in self.Query:
                path1 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                os.startfile(path1)
    
            elif ("open browser" or "browser") in self.Query:
                speak('what do you want to search on browser ?')
                search = self.take_command().lower()
                webbrowser.open(f"{search}")
    
            elif ("search") in self.Query:
                speak('what do you want to search ?')
                search = self.take_command().lower()
                webbrowser.open(f"{search}")
    
            elif ("open google" or "google") in self.Query:
                # speak('what do you want to search on google ?')
                # search = take_command().lower()
                # webbrowser.open(f"{search}")
                path2 = "https://www.google.com/"
                os.startfile(path2)
    
            elif ("open youtube" or "youtube") in self.Query:
                # webbrowser.open(f"www.youtube.com")
                path3 = "https://www.youtube.com/"
                os.startfile(path3)
    
            elif ("open firefox" or "firefox") in self.Query:
                path4 = "https://support.mozilla.org/en-US/products/firefox"
                os.startfile(path4)
    
            elif "wikipedia" in self.Query:
                speak('Searching Wikipedia...')
                Query = Query.replace('wikipedia', "")
                results = wikipedia.summary(Query, sentences=4)
                speak('according to wikipedia.......')
                speak(results)
                print(results)
    
            elif ("open facebook" or "facebook") in self.Query:
                path6 = "https://www.facebook.com/"
                os.startfile(path6)
    
            elif ("open twitter" or "twitter") in self.Query:
                path7 = "https://twitter.com/"
                os.startfile(path7)
    
            elif ("open amazon" or "twitter") in self.Query:
                path8 = "https://www.amazon.com/"
                os.startfile(path8)
    
            elif 'open stackoverflow' in self.Query:
                speak("Opening Stackoverflow")
                webbrowser.open("stackoverflow.com")
    
            elif "open camera" in self.Query or "camera" in self.Query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
    
                    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to quit.
                        break
                cap.release()
                cv2.destroyAllWindows()
    
            elif "command prompt" in self.Query or "cmd" in self.Query:
                os.system('start cmd')
    
            elif ("play music" or "play song") in self.Query:
                music_dir = "C:\\music_dir"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
    
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
    
            elif "ip address" in self.Query:
                ip = get('https://api.ipify.org').text
                speak(f'Your IP Address is: {ip}')
    
            elif ("send message" or "message") in self.Query:
                speak("Enter a mobile number to send message: ")
                number = self.take_command()
                speak("Enter a text message to be send")
                msg = self.take_command().lower()
                kit.sendwhatmsg_instantly(f"+{number}", f"{msg}", 10)
    
            elif ("play song on youtube" or "play on youtube") in self.Query:
                speak("Please tell me a song name?")
                song_name = self.take_command()
                kit.playonyt(f"{song_name}")
    
            elif ("email") in self.Query:
                    speak("Enter a email address to send message: ")
                    mail_to = input()
                    speak("Enter a text message to be send")
                    content = self.take_command().lower()
                    sendEmail(mail_to, content)
                    speak(f"Your Email has been sent successfully to {mail_to}")
            
            elif "prince" in self.Query:
                wish()
                speak(f"Prince in your service ! please tell me How may i help you sir ?")
                self.take_command()
    
            elif ("tell me a joke" or "joke") in self.Query:
                joke = pyjokes.get_joke()
                speak(joke)
    
            elif ("shut down" or "shutdown") in self.Query:
                speak("ok, shutting down the system.....")
                os.system("shutdown /s /t 6")
    
            elif "restart" in self.Query:
                speak("ok, restarting down the system.....")
                os.system("shutdown /r /t 6")
    
            elif "sleep system" in self.Query:
                os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
    
            elif "switch the window" in self.Query:
                pyautogui.keyDown("alt")
                pyautogui.keyDown("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
    
            elif "who i am" in self.Query:
                speak("If you talk then definitely you r human.")
    
            elif 'reason for you' in self.Query:
                speak("I was created as a Minor project by Rathod ")
    
            elif "don't listen" in self.Query or "stop listening" in self.Query:
                speak("for how much time you want to stop me from listening commands")
                a = int(self.take_command())
                time.sleep(a)
                print(a)
    
            elif "close notepad" in self.Query:
                speak("okey sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
            
            elif "close camera" in self.Query:
                speak("okey sir closing camera")
                os.system('wmic process where name="camera.exe" delete')
    
            elif "news" in self.Query:
                speak("please wait sir, fetching the latest trendings.....")
                news()
    
            elif "current location" in self.Query or "where i am" in self.Query or "where are you" in self.Query or "location" in self.Query:
                location_find()
    
            elif "calculate" in self.Query or "calculations" in self.Query or "mathematics" in self.Query or "calculation" in self.Query:
                calculations()
    
            elif "weather" in self.Query:
                weather()
    
            elif ("read pdf" or "read document") in self.Query:
                read_pdf()
    
            elif "hide current directory" in self.Query or "hide files" in self.Query or "hide this folder" in self.Query or "visible for everyone" in self.Query or "visible to everyone" in self.Query:
                speak("sir, please tell me, you want to hide this folder or make it visible for everyone ?")
                Condition = self.take_command().lower()
                if "hide" in Condition:
                    os.system("attrib +h /s /d")
                    speak("sir, all the files in this folder is now hidden!")
                elif "visible" in Condition:
                    os.system("attrib -h /s /d")
                elif "leave it" in Condition or "leave for now" in Condition:
                    speak("ok sir!")
    
            elif ("thank you" or "thanks") in self.Query:
                speak("it's my pleasure, sir")
    
            elif "how are you" in self.Query:
                speak("i am well thanks, and what about you ?")
                self.take_command()
    
            elif ("good" or "fine") in self.Query:
                speak("ok!")
    
            elif "your name" in self.Query:
                my_name = "Prince"
                speak(f'sir, my name is {my_name} A Virtual Assistant & i am working under my owner, thank you !')
    
            elif ("who made you" or "who created you") in self.Query:
                speak("I have been created by Shivam Singh Rathod")
    
            elif "your owner" in self.Query:
                owner = "shivam , a college student of Rewa Engineering College"
                speak(f'my owner is : {owner}')
    
            elif ("no thanks" or "no") in self.Query:
                speak("thanks for using me sir!, have a good day")
                sys.exit()
    
            elif ("by" or "bye") in self.Query:
                speak("thanks for using me sir!, have a good day")
                sys.exit()
    
            elif "i love you" in self.Query:
                speak("sorry, i want to be single and it is against our policy")
    
            elif "time" in self.Query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the current time is: {strTime}")
    
            elif "date" in self.Query:
                strDate = datetime.datetime.now().strftime("%m/%d/%Y")
                speak(f"sir, the current date is: {strDate}")
    
            elif ('ppt' or 'presentation') in self.Query:
                speak("Opening Virtual Assistant ppt")
                power = r""
                os.startfile(power)
    
            elif "you can sleep" in self.Query or "can sleep" in self.Query or "sleep now" in self.Query:
                speak("okey sir, i am going to sleep you can call me anytime!")
                break

            elif "who is mentor" in self.Query or "mentor" in self.Query or "mentor" in self.Query:
                speak("Our Metor is Ms. Preeti Mamm, We Developed this project under the guidance of Preeti mamm")
    
            elif "wake up" in self.Query:
                self.take_command()

            elif "goodbye" in self.Query or "by" in self.Query or "bye" in self.Query:
                speak("thanks for using me sir!, have a good day")
      
            else:
                speak("I am unable to understant what you want to say, tell me again please....")
                self.take_command()
    
            speak("sir! do you have any other Query? ")

startExecution = MainThread()    

# creating main window of UI
class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Virtual_UI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Git hub Projects or Gits in Python//Gui-Based Virtual Assistant_ PROGRESSIVE//Black and Blue Simple Technology Business Plan Presentation.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("Git hub Projects or Gits in Python//Gui-Based Virtual Assistant_ PROGRESSIVE//joinblink-blink-unscreen.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("Git hub Projects or Gits in Python/Gui-Based Virtual Assistant_ PROGRESSIVE//microphone-ui-animation-unscreen.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("Git hub Projects or Gits in Python//Gui-Based Virtual Assistant_ PROGRESSIVE//pngtree-neon-frame-design-material-png-image_4413994-removebg-preview.png")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)

        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
Virtual_Ui = Main()
Virtual_Ui.show()
exit(app.exec_())
sys.exit()


if __name__ == "__main__":
    while True:
        Permission = self.take_command()
        if "wake up" in Permission:
            TaskExecution()
        elif "goodbye" in Permission or "bye" in Permission:
            speak("thanks for using me sir!, have a good day")
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak("This is Moody knight an AI assistant")
def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is")
    speak(Time)
# time()
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)
# date()
def wishme():
    speak("Welcome Back Sir")
    time()
    date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    elif hour>=18 and hour<24:
        speak("Good Afternoon sir")
    else:
        speak("Good night sir")
    speak("Jarvis at your service Please tell me how can I help you?")
# wishme()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query
# takeCommand()

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mayank.sinha1999@gmail.com', 'aniketsingh1306')
    server.sendmail('kshivam0905@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What message you want to send?")
                content=takeCommand()
                to="kshivam0905@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            quit()

        elif 'logout' in query:
            os.system('shutdown -l')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        # elif 'play songs' in query:
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak('You said me to remember that'+remember.read())

        elif 'offline' in query:
            speak("Good Bye Sir!!")
            quit()
import pyttsx3  # pip install pyttsx3
import datetime  # importing the datetime library
import pyaudio  # for listening and recognition
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import re
import pyautogui
# used foir taking screenshots in python
import psutil
import pyjokes  # jokes python library


engine = pyttsx3.init()  # varisble=engine


def speak(audio):  # whatever we need to convert to audio we will pass that to this function
    engine.say(audio)
    engine.runAndWait()


# speak('This is jarvis AI assistant')

def time():
    # gives the current date time .str is for converting to str ("Hours:Minutes:seconds")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)  # speak function in which we are passing the time variable


def date():  # gives the day month and the year
    # we are soring that in the iinteger format
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    # to get the exact greeting according to time
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Goodmorning sir!")
    elif hour >= 12 and hour < 18:
        speak("Goodafternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Goodevening Sir!")
    else:
        speak("Goodnight sir!")
    time()
    date()
    speak("Jarvis at your service sir. Please tell me how can I help you")

# for recognition of the voice internet connection is need as it uses google for it.


def takeCommand():
    r = sr.Recognizer()  # initializing the recognizer in the r variable
    with sr.Microphone() as source:  # to get the input from the user through the microphone
        print("Listening..")
        r.pause_threshold = 1  # take a pause foer 1 second and then listen to the audio
        # Listen top the microphone.. Passing the source variable in the r.listen function
        audio = r.listen(source)
# we need try and except for different conditions that we are using
    try:
        print("Recognizing..")
        # what ever input we give will go in the query variable. we are using google for recognizing this thing. Language to english
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please!")
        return "None"
    return query


# wishme()
# takeCommand()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('faizansari15478@gmail.com', '')
    server.sendmail('faizansari15478@gmail.com', to, content)
    server.close()  # close the session


def screenshot():
    img = pyautogui.screenshot()
    # saving thescreenshot in the current folder
    img.save('File_Location')


def cpu():
    usage = str(psutil.cpu_percent())
    # we have type casted it in the format of string hence we have taken str
    speak("The CPU is at" + usage)
    battery = psutil.sensors_battery()  # List of things related to our CPU
    speak("The battery is at")
    speak(battery.percent)
    speak("%")


def jokes():
    speak("Get ready for a laughter")
    speak(pyjokes.get_jokes())


# coding the main function
if __name__ == '__main__':
    wishme()  # C everytime it loads we want the greeting
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
# Wikipedia search jarvis.... First we need to install the wikipedia search
        elif 'search on wikipedia' in query:
            speak("Searching...")
            # removing the wikipedia word and searching the query
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What do you want to send ?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendemail(to, content)
                sendemail("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email, check the information once again")
        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            # automatically add .com at the end for ex: youtube.com
            wb.get(chromepath).open_new_tab(search + '.com')
       # importing a python built in library OS i.e operating system, to perform various operations including start restart shutdown
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play song' in query:
            # name of the music directory will come here
            songs_dir = r'File_Location'
            # getting all the names of the song in the song variable
            songs = os.listdir(songs_dir)
            # starting the songs at the 0th index
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'remember that' in query:
            speak("what should I remember for you sir?")
            data = takeCommand()  # takeing a data variable
            speak("Sir you asked me to remember that" + data)
            # repeating what I askwed to remember
            remember = open('data.txt', 'w')  # opening file data in write mode
            remember.write(data)  # writing the content
            remember.close()  # closing the file after things arte done
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            # reading the content of the files saved
            speak("you asked me to remember that" + remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("The screenshot has been taken sir")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'sleep' in query:
            quit()

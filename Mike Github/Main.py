import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import requests
import subprocess
import spotipy

#import everything needed using pip

username = 'yourusername' #add your computer username
wolf_id = 'yourwolfram alpha api key here' #you can get wolfram aplha api key here : https://products.wolframalpha.com/api/
open_id = 'your open weather api key here' # you can get openweather api key here : https://openweathermap.org/api
your_email = 'your email address here' # add your email address here to sent email via voice

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # voice library


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("A Very Fresh Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Very Happy Good Afternoon")
    else:
        speak("Good Evening to You")
    speak("Hey It's Mike Your Personal Assistant")

    # this function wishes you

def takequery(): #this are listening and processing lines
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # threshold is the time assistant should wait until you finish your speaking
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as _:

        print("Could You Kindly Repeat Yourself")
        return "None"
    return query


def sendEmail(to, content): # sends email as you speak to any and as many receivers you want
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email', 'YourPasswordHere') #add your email credentials here to use email service
    server.sendmail('AddReceiversEmail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
while True:
    query = takequery().lower()

    if 'wikipedia' in query: # this searches your query to wikipedia and gives results
        print("Searching On Wikipedia For You")
        query = query.repalce("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open amazon' in query:
        webbrowser.open("amazon.in")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'open gmail' in query:
        webbrowser.open("gmail.com")
    elif 'open news' in query:
        webbrowser.open("news.google.co.in") # add any website using this elif template

    elif 'the time' in query: # shows you time
        strTime = datetime.datetime.now().strftime("%H,%M,%S")
        speak(f"The Time Currently is {strTime}")
    elif 'open epic games' in query:
        codePath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
        os.startfile(codePath)
    elif 'open minecraft' in query:
        codePath = "C:\\Users\\'username'\\yourminecraftpathhere"
        os.startfile(codePath)

    elif 'email a person' in query:
        try:
            speak("What should I say?")
            content = takequery() # speak your email now
            to = "receiversemail@gmail.com" #add receivers email here
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry, Could not send Email now")

    elif 'calculate' in query: # this helps you do maths

        app_id = "wolf_id" #this is your wolframaplha api key
        client = wolframalpha.Client(app_id)

        indx = query.split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        speak("The answer is " + answer)

    elif "who made you" in query or "who created you" in query:
        speaks = "Asher Carneiro has Made me Possible."
        speak(speaks)

    elif "weather" in query:
        api_key = "open_id" #your open api weather api key here
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("what's your city?")
        city_name = takequery()
        complete_url = base_url+"appid="+api_key+"&q="+city_name #this makes query add up to api url
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                  str(current_temperature) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
            print(" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))

        else:
            speak(" City Not Found ")

    elif "good bye" in query or "ok bye" in query or "stop" in query: # IMP: to stop the assistant say 'stop'
        speak('I am here if you need me,Bye')
        print('I am here if you need me,Bye')
        break

    elif 'answer' in query or 'homework' in query: #ask any homework questions and get answers
        speak('What Can I Help You With?')
        question = takequery()
        app_id = "wolf_id"
        client = wolframalpha.Client('wolf_id')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        print(answer)

    elif "shutdown" in query or "sign out" in query: #This shutdowns your computer
        speak(
            "Ok, your pc will shutdown in 10 seconds make sure you exit all applications")
        subprocess.call(["shutdown", "/l"])

    elif "where am i" in query: #this tells you your location in google maps
        query = query.split(" ")
        location = query[2]
        speak("Hold on, I will check.")
        # change directory to your browser
        #chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
        webbrowser.open(
            "https://www.google.nl/maps/place/" + "/&amp;" + location)

    elif "spotify" in query:
        exec(open('spotipyy.py').read())
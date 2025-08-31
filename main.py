import speech_recognition as sr
import webbrowser
import pyttsx3
import sphinx 
import musiclibrary
import dateandtime
import requests
from datetime import datetime
import random
import pyjokes

recognizer = sr.Recognizer()
newsapi = "59fd3c85c1284b119b0ba194af0274ad"
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print(c)
    if "google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "joke" in c.lower():
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif "time" in c.lower():
       from dateandtime import date_str
       from dateandtime import time_str
       print(f"Today's date is {date_str}")
       speak(f"Today's date is {date_str}")
       print(f"The current time is {time_str}")
       speak(f"The current time is {time_str}")
    elif "news" in c.lower():
        #newsapi = 59fd3c85c1284b119b0ba194af0274ad
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the json response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            #print the headlines
            for article in articles:
                print(article['title'])
                speak(article['title'])
    elif "coin" in c.lower():
        choice = random.choice(["Heads", "Tails"])
        speak(choice)
        print(choice)

if __name__ == "__main__":
    speak("initializing jarvis...")

    #Listen for the wake word jarvis
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Sphinx
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening")  
                recognizer.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Yes boss...")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = r.listen(source,timeout=5, phrase_time_limit=5)
                    recognizer.adjust_for_ambient_noise(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print(f"error; {e}")
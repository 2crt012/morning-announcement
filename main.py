# import necessary libaries
import pyttsx3
import datetime
import random
import requests

# set up TTS
tts = pyttsx3.init()

def sayGM(phrase):
    phrases = ["Good Morning, have a nice day!", "Rise and shine, it's a new day!"]
    if phrase == 0:
        phrase = random.choice(phrases)
    tts.say(phrase)
    tts.runAndWait()

def sayDate(): # get the current date and let the TTS engine say it
    cur_date = datetime.datetime.now().strftime("%A, %B %d")
    tts.say("Today's date is " + cur_date)
    tts.runAndWait()

def sayTime(): # get the current time and let the TTS engine say it
    cur_time = datetime.datetime.now().strftime("%I:%M %p")
    tts.say("The current time is " + cur_time)
    tts.runAndWait()

def sayJoke():
    joke = requests.get("https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single")
    joke_content = joke.text
    tts.say(joke_content)
    tts.runAndWait()

# settings (comment out to disable option)
sayGM(0) # say good morning. 0 = random, 1 = good morning, 2 = rise and shine
sayDate() # say the current date
sayTime()
sayJoke() # say a joke from the joke API
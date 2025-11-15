# import necessary libaries
import pyttsx3
import datetime
import random
import requests

# set up TTS
tts = pyttsx3.init()

def sayGM(phrase): # say good morning. 0 = random, 1 = good morning, 2 = rise and shine
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

def sayJoke(): # get a joke from the joke API and let the TTS engine say it. if there is no response within one second, a local joke will be used instead
    # add or remove local jokes in this array
    local_jokes = [
    "Two fish in a tank. One turns to the other and says, 'Do you know how to drive this thing?'",
    "I was going to tell a dead baby joke. But I decided to abort.",
    "I was reading a great book about an immortal dog the other day. It was impossible to put down.",
    "I have a fish that can breakdance! Only for 20 seconds though, and only once.",
    "I was struggling to figure out how lightning works, but then it struck me."
]
    tts.say("Here's today's joke for you!")
    tts.runAndWait()
    try:
        joke = requests.get("https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single", timeout=(1, 1))
        joke.raise_for_status()
        joke_content = joke.text
        tts.say(joke_content)
        tts.runAndWait()
    except (requests.exceptions.Timeout, requests.exceptions.RequestException, requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.URLRequired, requests.exceptions.TooManyRedirects):
        tts.say(random.choice(local_jokes))
        tts.runAndWait()
        return

# settings (comment out to disable option)
sayGM(0) # say good morning. 0 = random, 1 = good morning, 2 = rise and shine
sayDate() # say the current date
sayTime() # say the current time
sayJoke() # say a joke from the joke API
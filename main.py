# import necessary libaries
import pyttsx3
import datetime
import random

# set up TTS
tts = pyttsx3.init()

def sayGM(phrase): # say good morning with the TTS engine
    if phrase == 0:
        phrase = random.randint(1, 2)
    if phrase == 1:
        tts.say("Good Morning, havea  nice day!")
    elif phrase == 2:
        tts.say("Rise and shine, it's a new day!")
    tts.runAndWait()

def sayDate(): # get the current date and let the TTS engine say it
    cur_date = str(datetime.date.today())
    cur_date = cur_date.replace("-", " and ")
    tts.say("Today's date is " + cur_date)
    tts.runAndWait()

# settings (comment out to disable option)
sayGM(0) # say good morning. 0 = random, 1 = good morning, 2 = rise and shine
sayDate() # say the current date
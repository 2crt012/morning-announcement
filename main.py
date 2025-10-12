# import necessary libaries
import pyttsx3
import datetime

# set up TTS
tts = pyttsx3.init()

def sayGM(): # say good morning with the TTS engine
    tts.say("Good Morning!")
    tts.runAndWait()

def sayDate(): # get the current date and let the TTS engine say it
    cur_date = str(datetime.date.today())
    cur_date = cur_date.replace("-", " and ")
    tts.say("Today's date is " + cur_date)
    tts.runAndWait()

# settings (comment out to disable option)
sayGM() # say "good morning"
sayDate() # say the current date
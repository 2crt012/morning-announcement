import pyttsx3
import datetime

tts = pyttsx3.init()

def sayGM():
    tts.say("Good Morning!")
    tts.runAndWait()

def sayDate():
    cur_date = str(datetime.date.today())
    cur_date = cur_date.replace("-", " and ")
    tts.say("Today's date is " + cur_date)
    tts.runAndWait()

#settings (comment out to disable option)
sayGM()
sayDate()
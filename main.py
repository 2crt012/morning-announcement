#imports
import pyttsx3
import datetime

#setup
tts = pyttsx3.init()

#code
cur_date = str(datetime.date.today())
tts.say("Good Morning! Today is " + cur_date)
tts.runAndWait()
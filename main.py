#imports
import pyttsx3
import datetime

#setup
tts = pyttsx3.init()

#code
cur_date = str(datetime.date.today())
cur_date = cur_date.replace("-", " and ")
tts.say("Good Morning! Today is " + cur_date)
tts.runAndWait()
print(cur_date)
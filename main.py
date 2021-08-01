#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

#import hours_notifications_main
from hours_notifications import modules as time_modules
from modules import activate, activate_jarvis, speech_recognition

import speech_recognition as sr
import pyttsx3

#choose between fr and en
language = "fr"

while True :
    jarvis = activate()

#time
hours = time_modules.get_time()[1]
minutes = time_modules.get_time()[2]
print("{0} h {1} min".format(hours, minutes))

#text to speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[26].id)
engine.setProperty("voice", voices[10].id)
engine.say(vocal)
engine.runAndWait()

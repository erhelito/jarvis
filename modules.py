#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import speech_recognition as sr
import pyttsx3

def activate() :
    r = sr.Recognizer()

    with sr.Microphone() as source :
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        print("...")
        audio = r.listen(source)
        try :
            #vocal = r.recognize_google(audio, language = "en-US")
            vocal = r.recognize_google(audio, language = "fr-FR")
            print(vocal)
        except  :
            print("raté")    

#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import speech_recognition as sr
from os import system
import pyttsx3

def activate_jarvis(user_language):
    system("clear")

    jarvis = False

    r = sr.Recognizer()

    with sr.Microphone() as source :
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7

        if user_language == "fr" :
            print("Dites \"Hey Jarvis\" pour m'activer")

        elif user_language == "en" :
            print("Say \"Hey Jarvis\" to activate me")

        print("...")
        audio = r.listen(source)

        try :
            vocal = r.recognize_google(audio, language = "en-US")

            vocal = vocal.lower()

            jarvis = vocal == "hey jarvis"

            if jarvis :
                jarvis_activated(user_language)

        except :
            if user_language == "fr" :
                print("Essayez à nouveau")
            elif user_language == "en" :
                print("Try again")


        return jarvis

    

def jarvis_activated(user_language):
    if user_language == "fr" :
        jarvis_speaks(26, "Je vous écoutes.")

    elif user_language == "en" :
        jarvis_speaks(10, "I'm listening to you")

def jarvis_speaks(voice_id, text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 175)

    engine.setProperty("voice", voices[voice_id].id)
    engine.say(text)
    engine.runAndWait()

def jarvis_listens(user_language):
    r = sr.Recognizer()

    with sr.Microphone() as source :
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7

        print("...")
        audio = r.listen(source)

        try :

            if user_language == "fr" :
                vocal = r.recognize_google(audio, language = "en-US")

            elif user_language == "en" :
                vocal = r.recognize_google(audio, language = "fr-FR")

            vocal = vocal.lower()

        except :
            if user_language == "fr" :
                print("Essayez à nouveau")
            elif user_language == "en" :
                print("Try again")

            vocal = ""

    return vocal
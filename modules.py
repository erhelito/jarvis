#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import speech_recognition as sr
import pyttsx3

def activate_jarvis(user_language) :
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
            print(vocal)

            vocal = vocal.lower()

            jarvis = vocal == "hey jarvis"

        except :
            if user_language == "fr" :
                print("Essayez à nouveau")
            elif user_language == "en" :
                print("Try again")

        return jarvis

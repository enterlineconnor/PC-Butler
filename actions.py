import speech_recognition as sr
import pyttsx3 
import os
import winapps
import windowsapps
import config



def start(param,speak_to_text):
    param = param.strip()
    param = param.lower()
    try:
        windowsapps.open_app(param)
    except:
        response = 'Could not find application '+ param
        print(response)
        speak_to_text(response)

def restart(param,speak_to_text):
    param = param.strip()
    param = param.lower()
    try:
        os.system("shutdown /r /t 0")
    except:
        response = 'wah wah'
        print(response)
        speak_to_text(response)
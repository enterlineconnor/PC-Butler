import speech_recognition as sr
import pyttsx3 
import os
import winapps
import windowsapps
import config



def start(param):
    param = param.strip()
    param = param.lower()
    try:
        windowsapps.open_app(param)
        response = 'Starting Application '+ param
        print(response)
        return response
    except:
        response = 'Could not find application '+ param
        print(response)
        return response

def restart(param):
    param = param.strip()
    param = param.lower()
    try:
        os.system("shutdown /r /t 0")
    except:
        response = 'Something went wrong'
        print(response)
        return response

def shutdown(param):
    param = param.strip()
    param = param.lower()
    try:
        os.system("shutdown /s /t 0")
    except:
        response = 'Something went wrong'
        print(response)
        return response
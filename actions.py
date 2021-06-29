import speech_recognition as sr
import os
import windowsapps
import requests
import json

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

def kayne_quote():
    result = requests.get('https://api.kanye.rest/')
    quote = result.text
    json_val = json.loads(quote)
    kayne_quote = json_val['quote']
    return kayne_quote
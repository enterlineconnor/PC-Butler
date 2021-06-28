# Python program to translate
# speech to text and text to speech
  
import speech_recognition as sr
import pyttsx3 
import os
import winapps
import windowsapps
import config
import actions

# Name of Butler and Owner
name = config.butler['name']
owner = config.owner['name']
addressed = False

# Command List

commands = [
    'play',
    'start',
    'restart',
    ]

# Initialize the recognizer 
r = sr.Recognizer() 
  
# Function to convert text to
# speech
def speak_to_text(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      
   
# Loop infinitely for user to
# speak
while(1):    
      
    # Exception handling to handle
    # exceptions at the runtime
    try:
          
        # use the microphone as source for input.
        with sr.Microphone() as source:

                     
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.2)
              
            #listens for the user's input 
            audio = r.listen(source)
              
            # Using ggogle to recognize audio
            input = r.recognize_google(audio)
            input = input.lower()
            name = name.lower()
            owner = owner.lower()

            phrase = input.split(' ')

            param = ''

            print(phrase)

            if addressed == False:
                for word in phrase:
                    if word == name:
                        response = 'Hello '+owner,', how can I help you?'
                        print(response)
                        speak_to_text(response)
                        addressed = True
            
            else:
                for word in phrase:
                    if word == phrase[0]:
                        if word in commands:
                            response = 'Sure thing, ','give me one moment'
                            print(response)
                            speak_to_text(response)
                        else:
                            response = 'wah wahh'
                            print(response)
                            speak_to_text(response)
                            # speeds program by not iterating over rest of sentence
                    else:
                        param += word+' '
                        print(param)
                    
                    if word == phrase[len(phrase)-1] and (phrase[0] == 'play' or phrase[0] == 'start'):
                        actions.start(param,speak_to_text)
                        

                addressed = False
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")
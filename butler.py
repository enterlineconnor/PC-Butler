import speech_recognition as sr
import pyttsx3 
import config
import actions

# Name of Butler and Owner
name = config.butler['name']
owner = config.owner['name']
addressed = False
phrase_after_name = []
last_element = ''

# Initialize the recognizer 
r = sr.Recognizer() 
  
# Function to convert text to
# Speech
def speak_to_text(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

def sanatize_param(param):
    param = param.strip()
    param = param.lower()
    return param
      
   
# Loop infinitely for user to
# Speak
while(1):    
      
    # Exception handling to handle
    # Exceptions at the runtime
    try:
          
        # Use the microphone as source for input.
        with sr.Microphone() as source:

                     
            # Wait for a second to let the recognizer
            # Adjust the energy threshold based on
            # The surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.2)
              
            # Listens for the user's input 
            audio = r.listen(source)
              
            # Using Google to recognize audio
            input = r.recognize_google(audio)
            input = input.lower()
            name = name.lower()
            owner = owner.lower()
            phrase = input.split(' ')
            param = ''
            print(phrase)

            for word in phrase:
                # If name of both is heard, trigger listener for words after the name
                if word == name and addressed == False:
                    # Split array by name call, so phrase_after_name is the command sentence
                    name_index = phrase.index(word) + 1
                    if name_index >= len(phrase):
                        break
                    phrase_after_name = phrase[name_index:]
                    last_element = len(phrase_after_name)-1
                    addressed = True

                # Use first word after name as command type
                if addressed and word == phrase_after_name[0]:
                    response = 'Sure thing, ','give me one moment'
                    print(response)
                    speak_to_text(response)

                if addressed and word == phrase_after_name[last_element]:
                    skip = 0
                    for p in phrase_after_name:
                        if skip > 0:
                            param += p+' '
                        skip += 1

                # Function Calls
                if addressed and word == phrase_after_name[last_element] and (phrase_after_name[0] == 'play' or phrase_after_name[0] == 'start'):
                    sanatize_param(param)
                    speak_to_text(actions.start(param))
                
                elif addressed and word == phrase_after_name[last_element] and (phrase_after_name[0] == 'restart'):
                    sanatize_param(param)
                    speak_to_text(actions.restart(param))
                
                elif addressed and word == phrase_after_name[last_element] and (phrase_after_name[0] == 'shut' and phrase_after_name[1] == 'down'):
                    sanatize_param(param)
                    speak_to_text(actions.shutdown(param))

                elif addressed and word == phrase_after_name[last_element] and (param == 'what would kayne do'):
                    speak_to_text(actions.kayne_quote())
                    
            addressed = False

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")
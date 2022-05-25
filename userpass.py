import sys
import pyttsx3
voice = pyttsx3.init()

def passw():
    voice.say("enter your username")
    voice.runAndWait()
    user=input("enter your username")
    voice.say("enter your password")
    voice.runAndWait()
    passw=input("enter your password")
    a=0
    while a==0:
        try:
        
            if user=='GameOnSpotYt' and passw=='gayonspot':
                voice.say("you are on user - GameOnSpot")
                voice.runAndWait()
                print("you are on user - GameOnSpot")
                
            elif user=='KeeneeyeYt' and passw=='hello':
                voice.say("you are on user - KeeneeyeYt")
                voice.runAndWait()
                print("you are on user - KeeneyeYt ")
               
            else:
                1/0
            
        except:
            voice.say("please enter a valid username or password")
            voice.runAndWait()
            print("please enter a valid username or password")
            a=0
      

voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)

passw()

from pickle import TRUE
from time import time
import webbrowser
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pwk 
import imp
import datetime 
import wikipedia as wkp
import pyjokes as pj
from googlesearch import search 
import os
import subprocess as sb
import smtplib 

listener = sr.Recognizer()
eng = pt.init('sapi5') #initialises the text to speech 
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)

def talk(text): #talks back
    eng.say(text)
    eng.runAndWait()

def takeCmd():
    try:
        with sr.Microphone() as src:  #using microphone as src
            print('listening') 
            voice = listener.listen(src)
            cmd = listener.recognize_google(voice) #audio is passed to google api and text is returned 
            print(cmd)
            return cmd
    except:
        #print('Sorry could not hear you. Please try again')
        pass
        

def salutation():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  
        
    talk('I am Jenice, your personal bot. What can I do for you?')

def run():
    try:
        cd = takeCmd() #takes a cmd  

        if 'play' in cd: #for a mp3 or mp4 on yt
            media = cd.replace('play', '')
            talk('playing ' + media)
            pwk.playonyt(media)

        elif 'the time' in cd: #to get the current time in curernt loc
            hour = datetime.datetime.now().strftime('%I:%M %p')
            print('currently ' + hour)
            talk('Currently it\'s' + hour)

        elif 'what' in cd or 'who' in cd or 'why' in cd or 'when' in cd or 'search' in cd:
            pwk.search(cd)

        elif 'joke' in cd:
            talk(pj.get_joke())
            
        elif 'wikipedia' in cd:
            cd = cd.replace('wikipedia', '')
            res = wkp.summary(cd, sentences = 3)
            talk('According to Wikipedia')
            print(res)
            talk(res)

        elif 'stop' in cd:
            talk('Thankyou! It was nice meeting you! Bye')
        
        else:
            talk('Sorry! Could not understand you')
    
    except:
        talk('Sorry could not hear you. Please try again')


if __name__=="__main__" :
    salutation()
    # talk('Do you want my help?')
    # if(takeCmd()=='yes'):
    #     run()
    # elif(takeCmd=='no'):
    #     print('No')
    run()
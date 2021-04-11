# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:56:00 2021

@author: HP
"""


import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser #for youtube
import os
#import random
import smtplib
import sys
#Qr code
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import pyjokes
from pycricbuzz import Cricbuzz
import json
import threading
import alarm #alarm.py in folder
import pywhatkit
import datefinder
c = Cricbuzz()

#matches = c.livescore(1)


name=''

import wolframalpha 
try:
    app=wolframalpha.Client("Q96JH8-P9AUYH8E6W")
except Exception:
    print("Not working")

#text to speech
engine = pyttsx3.init('sapi5')#sapi5 for microsoft voice recogn. api system
voices= engine.getProperty('voices') #getting details of current voice
#print(voices)#two voice available, one is male(0) and another female(1)
engine.setProperty('voice',voices[1].id)#setting female voice

def speak(audio):
    engine.say(audio)#engine will speak the string
    engine.runAndWait()#runnin purpose
    
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    elif hour>=17 and hour<20:
        speak("Good Evening")
    speak("I am your smart assistant! how can i help You. ting ting tung tang")
    

#it takes microphone input from user and return string output
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1;#setting the time after command( 1s )
        audio=r.listen(source)#audio keep the listened voice
        #upto here audio takes as i/p
    try:
        print("Recognizing...")
        #Performs speech recognition on audio_data (an AudioData instance),
        #using the Google Speech Recognition API. 
        query=r.recognize_google(audio, language='en-in')
        print("User said: ",query)

    except Exception as e:
        #print(e)
        speak("Say that again")
        takeCommand()
        return "None"#returning none string if problem occur 
    return query


#mail sending
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('subhratanu.jisce@gmail.com','password')
    server.sendmail('subhratanu.jisce@gmail.com',to,content)
    server.close()


def scan():
    i=0
    cap=cv2.VideoCapture(0)
    while i<1:
        _,frame= cap.read()
        decode=pyzbar.decode(frame)
        for obj in decode:
            print(obj.data)
            i=i+1
        cv2.imshow('Qr code',frame)
        if cv2.waitKey(1)==13:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return obj.data

def selfie():
    count=0
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        count=count+1
        ret,frame=cap.read()   
    cv2.imshow("Pic",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return frame,count

 


if __name__=='__main__':
    wishme()
    
    #speak("I love my bobbo very much. i love you bobbo")
    while 1:
        
            
        query=takeCommand().lower()
        #many times query transformed into capital and raise an error
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            #query=query.replace('Wikipedia','')
            results=wikipedia.summary(query,sentences=2)#it return wikipedia result
            speak("According to wikipedia")
            speak(results)
            print(results)
            
        
            
        elif 'open youtube' in query:
            
            webbrowser.open('youtube.com')
            
        
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif 'play music' in query or 'play a song' in query:
            music_dir= "D:\\Assistant\\music" #music directory
            song=os.listdir(music_dir) #list of music in the directory
            os.startfile(os.path.join(music_dir,song[0])) #start first song
            break
            
        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {time}")
            
        elif 'my mother' in query:
            speak("Your mother name is Debjani Saha")
            
        elif 'my father' in query:
            speak("Your father name is Subrata kumar Saha")
            
        elif 'my girlfriend' in query:
            speak("Your girlfriend name is Susmita Das")
            
        elif 'my name' in query:
            if name=='':
                speak("What is your name")
                name=takeCommand().lower()
                speak(f"Hi {name}")
            else:
                speak(f"Hi {name}")
                
        elif 'open compiler' in query:
            speak("Opening DEV C++")
            codePath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
            
        elif 'send mail' in query:
            try:
                speak("What should i say")
                content= takeCommand()
                to = "susmita14022000@gmail.com"
                sendEmail(to, content)
                speak("Email sent")
                
            except Exception as e:
                print("e")
                speak("Unable to send email")
                
        elif 'temperature' in query:
            try:
                response=app.query(query)
                speak(next(response.results).text)
            except Exception:
                print("Internet error")
        
             
       
            
            
        elif 'open camera' in query:
            print(query)
            speak("Opening camera")
            url=scan()
            webbrowser.open(url)
            
        elif 'take photo' in query:
            speak("Taking selfie")
            frame,count=selfie()
            file_name_path='D:/Assistant/selfie'+str(count)+'.png'
            cv2.imwrite(file_name_path,frame)
            
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you "+name)
            
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Subhratanu.")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
            
        elif "I am fine" in query:
            speak("Glad to hear")
            
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            
        elif query in ['quit','bye','good bye']:
            speak("Bye")
            sys.exit("Ok!Bye")
            
        elif "read me" in query:
            speak("Reading myself")
            file = open("bio.txt", "r") 
            speak(file.read())
            
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")
            break
        
        elif 'alarm' in query:
            alarm.alarm(query)
            
        elif 'message' in query:
            try:
                speak("Tell me the number")
                no=input('>>>')
                speak("tell me the message")
                txt=takeCommand().lower()
                speak("Tell me the time")
                tm=takeCommand().lower()
                a=datefinder.find_dates(tm)#a is a object
                for x in a:
                    pass
                strA=str(x)
                timeA=strA[11:]
                
                hor=timeA[:2]
                hor=int(hor)
                print(hor)
                minut=timeA[3:5]
                minut=int(minut)
                print(minut)
                pywhatkit.sendwhatmsg('+91'+no,txt,hor,minut)
                
            except:
                speak('internet error')
                
        
                
        elif "what is" in query or "who is" in query:
             
            # Use the same API key 
            # that we have generated earlier
            
             
            try:
                response = app.query(query)
                print (next(response.results).text)
                speak (next(response.results).text)
            except StopIteration:
                speak("No results")
                print ("No results")
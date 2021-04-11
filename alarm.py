# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:20:39 2021

@author: HP
"""


import datefinder
import winsound
import datetime
import assistant
import time

def alarm(text):
    a=datefinder.find_dates(text)#a is a object
    for x in a:
        print(x)
    strA=str(x)
    timeA=strA[11:]
    
    hourA=timeA[:2]
    hourA=int(hourA)
    
    minu=timeA[3:5]
    minu=int(minu)
    
    sec=timeA[6:]
    sec=int(sec)
    
    print(hourA,minu,sec)
    
    while True:
        if hourA==datetime.datetime.now().hour:
            if minu==datetime.datetime.now().minute:
                print("Alarm on")
                #winsound.PlaySound('D://Assistant//music//',winsound.SND_LOOP)
                assistant.speak("Here is Your alarm sir!Do needful")
                time.sleep(1)
                
            elif minu<datetime.datetime.now().minute:
                break
            
            elif minu>datetime.datetime.now().minute:
                assistant.takeCommand()
        else:
            break
#alarm('Set alarm at 4:56 pm')
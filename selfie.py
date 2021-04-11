# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:03:12 2021

@author: HP
"""

dictt={}
i=1
while(i<3):
    a=input().split(',')
    dictt[a[0]]=a[1]
    i=i+1
print(dictt['a'])

if alarm() in alarm_dict.keys():
            mt=int(datetime.datetime.now().minute)
            speak("Here is your alarm for")
            try:
                while(mt<mt+1):
                    speak(alarm_dict[alarm()])
                    
            except Exception:
                continue
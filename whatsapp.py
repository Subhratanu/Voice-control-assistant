# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 00:35:51 2021

@author: HP
"""


import pywhatkit 
'''  
# using Exception Handling to avoid  
# unprecedented errors 
try: 
    
  # sending message to reciever 
  # using pywhatkit 
  pywhatkit.sendwhatmsg("+919088180701",  
                        "o bobbo janooo! ei message ta ekta bot pathache.. tomar bobbo pathay ni... sob python kore dilo",  
                        00, 44) 
  pywhatkit.playonyt("uma jukebox") 
  pywhatkit.info("who is Sourav ganguly", lines = 4) 
  print("Successfully Sent!") 
  
except: 
    
  # handling exception  
  # and printing error message 
  print("An Unexpected Error!")
'''  

try:
    
    pywhatkit.sendwhatmsg("+916291957700","Hey, I am bot",21,40)
except:
    
    print('unexpected error')
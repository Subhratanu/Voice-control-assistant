# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:44:04 2021

@author: HP
"""


import threading
import datetime
  
'''def gfg(): 
    print("GeeksforGeeks\n") 
  
timer = threading.Timer(5.0, gfg) 
timer.start() 
print("Cancelling timer\n") 
#timer.cancel() 
print("Exit\n") 

time=datetime.datetime.now().strftime('%H%M')
print(time)
from datetime import datetime
s1 = '10:33:26'
s2 = '11:15:49' # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print(tdelta.strftime('%M'))'''

import datetime as dt
start=datetime.datetime.now().strftime('%H:%M:%S')
end="13:39:00"#from alarm
start_dt = dt.datetime.strptime(start, '%H:%M:%S')
end_dt = dt.datetime.strptime(end, '%H:%M:%S')
diff = (end_dt - start_dt) 
diff=diff.seconds
print(diff) 
def gfg(): 
    print("GeeksforGeeks\n") 
timer = threading.Timer(diff, gfg) 
timer.start()
    
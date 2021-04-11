# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:55:22 2021

@author: HP
"""


import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

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
        
if __name__=='__main__':
    scan()
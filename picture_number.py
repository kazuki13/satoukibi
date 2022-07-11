import cv2
import datetime
import tkinter as tk
import os
import move_True2
import picture

def picture_number():
    cap = cv2.VideoCapture(0)  
\


    number =int(input("写真を撮る枚数を半角で入力"))
    m = 1
    for i in range(number):
        ret, img = cap.read()
        cv2.imshow('video image', img)
        m1  = str(m)
        fileName = "photo_" + m1 + ".png"
        cv2.imwrite('satoukibi' +'/' +  'picture_number' + '/' + fileName, img)
        m += 1

    cap.release()
    cv2.destroyAllWindows()
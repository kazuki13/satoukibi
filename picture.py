import cv2
import datetime
import tkinter as tk
import os
import move_True2
import picture

def picture():
    cap = cv2.VideoCapture(0) 
    m = 1 
    while True:

        ret, img = cap.read()
        cv2.imshow('video image', img)
        m1 = str(m)
        fileName = "photo_" + m1 + ".png"
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):

        
            #  ーーpng形式での保存ーー
            cv2.imwrite('satoukibi' +'/' +  'picture' + '/' + fileName, img)
            m += 1
        key2 = cv2.waitKey(1)
        if key2 == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
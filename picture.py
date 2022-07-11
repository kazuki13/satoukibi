import cv2
import datetime
import tkinter as tk
import os
import move_True2
import picture
def picture():
    cap = cv2.VideoCapture(0)  
    while True:

        ret, img = cap.read()
        cv2.imshow('video image', img)
        fileName = "photo_" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):

        
            #  ーーpng形式での保存ーー
            cv2.imwrite('サトウキビプロジェクト' +'/' +  '写真' + '/' + fileName, img)
        key2 = cv2.waitKey(1)
        if key2 == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
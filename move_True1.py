import cv2
# 動画ファイルを取得7
import datetime
import tkinter as tk
import os

def move_True1():
    # 動画ファイルを取得
    cap = cv2.VideoCapture(0)   

    # FPSを取得
    fps = int(cap.get(cv2.CAP_PROP_FPS)) 
    
    # カメラの横幅を取得               
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
    # カメラの縦幅を取得
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))        

    # 動画保存時のfourcc設定（mp4用）
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv2.VideoWriter('satoukibi' +'/' +  'move' + '/' + 'video.m4v', fourcc, fps, (w, h))
    while True:
        ret, img = cap.read()
        cv2.imshow('video', img)

        # フレームを画面に表示    
        cv2.imshow('video', img)
        # 動画を保存
        # key2 = cv2.waitKey(10)
        
        writer.write(img)
        # キー操作があればwhileループを抜ける

        key2 = cv2.waitKey(1)
        if key2 == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
        # key = cv2.waitKey(5)
        # if key == 13:
        #     while True:  
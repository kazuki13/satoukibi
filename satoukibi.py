import cv2
import datetime
import tkinter as tk
import os
import move_True1
import move_True2
import picture
import picture_number


# # 動画ファイルを取得
# cap = cv2.VideoCapture(0)   

# # FPSを取得
# fps = int(cap.get(cv2.CAP_PROP_FPS)) 
  
# # カメラの横幅を取得               
# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
# # カメラの縦幅を取得
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))        

# # 動画保存時のfourcc設定（mp4用）
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 

# 動画の仕様をまとめる（ファイル名、fourcc, FPS, サイズ）


cap = cv2.VideoCapture(0)
if not os.path.exists('satoukibi'):
    os.mkdir('satoukibi')
if not os.path.exists('./satoukibi/picture'):
    os.mkdir('./satoukibi/picture')
if not os.path.exists('./satoukibi/move'):
    os.mkdir('./satoukibi/move')
if not os.path.exists('./satoukibi/move_time'):
    os.mkdir('./satoukibi/move_time')
if not os.path.exists('./satoukibi/picture_number'):
    os.mkdir('./satoukibi/picture_number')
# writer = cv2.VideoWriter('test' +'/' +  'test2' + '/' + 'video.m4v', fourcc, fps, (w, h))  
# writer2 = cv2.VideoWriter('test' +'/' +  'test3' + '/' + 'video2.m4v', fourcc, fps, (w, h))

# sample.py
import tkinter as tk
import tkinter.ttk as ttk


def search():
    text.set("Finish")
# rootメインウィンドウの設定
root = tk.Tk()
root.title("tkinter application")
root.geometry("200x200")

# メインフレームの作成と設置
frame = ttk.Frame(root)
frame.pack(fill = tk.BOTH, padx=20,pady=10)

# StringVarのインスタンスを格納する変数textの設定
text = tk.StringVar(frame)
text.set("動画撮影")
text2 = tk.StringVar(frame)
text2.set("動画撮影:秒数指定")
text3 = tk.StringVar(frame)
text3.set("写真")
text4 = tk.StringVar(frame)
text4.set("写真:枚数指定")
# 各種ウィジェットの作成

button = tk.Button(frame, textvariable=text, command=move_True1.move_True1)
button2 = tk.Button(frame, textvariable=text2, command=move_True2.move_True2)
button3 = tk.Button(frame, textvariable=text3, command=picture.picture)
button4 = tk.Button(frame, textvariable=text4, command=picture_number.picture_number)

# 各種ウィジェットの設置
button.pack()
button2.pack()
button3.pack()
button4.pack()


root.mainloop()
# while True:
# #   ファイルの名前
#   fileName = "photo_" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"
# #   画像の読み込み
#   ret, img = cap.read()
#   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   key = cv2.waitKey(5)
#   if key == 13:
#     while True:  
#       print(12)
#       # フレームを画面に表示    
#       cv2.imshow('video', img)
#       # 動画を保存
#       # key2 = cv2.waitKey(10)
      
#       writer.write(img)
#       # キー操作があればwhileループを抜ける
#       key2 = cv2.waitKey(5)
#       if key2 == 27:
#           break
#   key = cv2.waitKey(5) & 0xFF
#   if key == ord('s'):
#     roop = int(fps * 15)
#     for i in range(roop):
#       print(13)
#       writer2.write(img)#1フレーム保存する
#   key = cv2.waitKey(10) & 0xFF
#   if key == ord('c'):

  
#     #  ーーpng形式での保存ーー
#     cv2.imwrite('test' +'/' +  'test1' + '/' + fileName, img)
#   #   # time.sleep(3)
#   #   # ーーーーーーーーーーーー
#   cv2.imshow('video image', img)
#   # if faces :
#   #   cv2.imwrite(fileName, img)

#   key2 = cv2.waitKey(5)
#   if key2 == 27:
#     break
# cap.release()
# cv2.destroyAllWindows()
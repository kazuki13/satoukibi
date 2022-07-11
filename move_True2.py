import cv2
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
# writer2 = cv2.VideoWriter('test' +'/' +  'test3' + '/' + 'video2.m4v', fourcc, fps, (w, h))
def move_True2():    
    writer2 = cv2.VideoWriter('satoukibi' +'/' +  'move_time' + '/' + 'video2.m4v', fourcc, fps, (w, h))
    roop = int(fps * 15)
    for i in range(roop):
        ret, img = cap.read()
        cv2.imshow('video image', img)
        cv2.waitKey(1)
        writer2.write(img)#1フレーム保存する
        # print(img)
  
        
    cap.release()
    cv2.destroyAllWindows()
        #     key = cv2.waitKey(5)
        # if key == ord('s'):
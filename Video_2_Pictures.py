import cv2
import os

os.chdir( r'C:\Users\xkh\Desktop\sample\img')
filename = r'C:\Users\xkh\Desktop\sample\WIN_20210416_14_30_37_Pro.mp4'

videoCapture1 = cv2.VideoCapture(filename)

status, frame = videoCapture1.read()
index = 0
while True:
    status, frame = videoCapture1.read()
    cv2.imwrite('img_'+str(index)+'.jpg', frame)
    index += 1

    if not status:
        print('video is all read')
        break
    
    

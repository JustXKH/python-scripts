import cv2
import os

os.chdir( r'C:\Users\xkh\Desktop\20210721_162126\img')
filename = r'C:\Users\xkh\Desktop\20210721_162126\20210721_162126_VIS_H264.MOV'

videoCapture1 = cv2.VideoCapture(filename)

status, frame = videoCapture1.read()
index = 0
while True:
    status, frame = videoCapture1.read()
    if not status:
        print('video is all read')
        break

    cv2.imwrite('img_'+str(index)+'.jpg', frame)
    index += 1


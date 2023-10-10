import cv2
import os

# os.chdir( r'C:\Users\xkh\Desktop\20210721_162126\img')
filename = r'F:\keypoint\VID_20221018_114142.mp4'
video_path = r'F:\keypoint\video1109'
total = 0
for i, video in enumerate(os.listdir(video_path)):
    videoCapture1 = cv2.VideoCapture(video_path + os.sep + video)

    status, frame = videoCapture1.read()
    index = 0
    cur_frame = 0
    save_img_path = r'F:\keypoint\video_frame_1109'
    while True:
        status, frame = videoCapture1.read()
        if not status:
            print('video is all read')
            break
        frame_fps = videoCapture1.get(cv2.CAP_PROP_FPS)

        cur_frame += 1
        if cur_frame % int(frame_fps) == 0:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(f'{save_img_path + os.sep}video_11_09_{i}_{str(index)}.jpg', frame)
            index += 1
            total += 1
            print(f'{i}, index :{index}, total :{total}, video_name:{video}')

    # exit(0)



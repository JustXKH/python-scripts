import json
import cv2
import os
import shutil
import numpy as np

json_path = r'F:\pseudo_label\part3\dst.json'
img_path = r'F:\pseudo_label\part3\imgs'
save_dir_path = r'F:\pseudo_label\part3\vis'

if os.path.exists(save_dir_path):
    shutil.rmtree(save_dir_path)
os.makedirs(save_dir_path, exist_ok=True)

categoryId_to_name = {1: 'person', 44: 'bottle', 62: 'chair', 64: 'potted plant', 100: 'camera'}
text_width = 15
text_height = 20
with open(json_path, 'r') as json_fp:
    json_data = json.load(json_fp)
    images = json_data['images']
    for image in images:
        image_file_name = image['file_name']
        image_name = image_file_name.split('/')[-1]
        save_image_path = os.path.join(save_dir_path, image_name)
        image_path = os.path.join(img_path, image_name)
        img = cv2.imread(image_path)
        image_id = image['id']
        for anno in json_data['annotations']:
            if anno['image_id'] == image_id:
                x1, y1, w, h = map(int, anno['bbox'])
                category_id = anno['category_id']
                cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), thickness=3)

                text = f"{categoryId_to_name[category_id]}"
                print(text, len(text))
                width = (len(text) - 1) * text_width
                img[y1:y1 + text_height, x1:x1 + width, :] = (0, 0, 0)
                cv2.putText(img, text, (x1, y1 + text_height - 2), cv2.FONT_ITALIC,
                            fontScale=0.7, color=(200, 200, 200))

        cv2.imwrite(save_image_path, img)


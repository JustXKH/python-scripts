import cv2
import os
import json
import matplotlib.pyplot as plt
from PIL import Image
import scipy.io as scio

set = 'validation'     # training, test, validation
root_path = 'F:\\Dataset\\hand_detect\\hand_dataset'
img_pathDir = root_path + os.sep + set + '_dataset' + os.sep + set + '_data' + os.sep + 'images'    # 图片文件夹
label_pathDir = root_path + os.sep + set + '_dataset' + os.sep + set + '_data' + os.sep + 'annotations'    # 标签文件夹
coco_pathDir = root_path + os.sep + set + '_dataset' + os.sep + set + '_data'    # 要生成的标准coco格式标签所在文件夹

categories = [{'id': 1, 'name': 'hand', 'supercategory': 'hand'}]

write_json_context = dict()                                          # 写入.json文件的大字典
write_json_context['info'] = {'description': '', 'url': '', 'version': '', 'year': 2022, 'contributor': '', 'date_created': '2022-07-25'}
write_json_context['licenses'] = [{'id': 1, 'name': None, 'url': None}]
write_json_context['categories'] = categories
write_json_context['images'] = []
write_json_context['annotations'] = []

# 接下来的代码主要添加 'images' 和 'annotations' 的key值
imageFileList = os.listdir(img_pathDir)     # 遍历该文件夹下的所有文件，并将所有文件名添加到列表中
imageFileList = [img for img in imageFileList if 'jpg' in img]

for i, imageFile in enumerate(imageFileList):
    imagePath = os.path.join(img_pathDir, imageFile)                             # 获取图片的绝对路径
    print(imagePath, i)
    image = Image.open(imagePath)                                               # 读取图片，然后获取图片的宽和高
    W, H = image.size

    img_context = {'file_name': 'images' + '/' + imageFile.lower(), 'height': H, 'width': W,
                   'date_captured': '2022-07-25', 'id': i, 'license': 1, 'color_url': '',
                   'flickr_url': ''}  # 使用字典存储该图片信息
    # img_name=os.path.basename(imagePath)                                       # 返回path最后的文件名。如果path以/或\结尾，那么就会返回空值
    write_json_context['images'].append(img_context)                            # 将该图片信息添加到 'image' 列表中

    dataFile = imagePath.replace("images", "annotations").split('.')[0] + '.mat'      # 获取该图片的标注文件路径
    data = scio.loadmat(dataFile)
    box = data['boxes'][0]
    for k in range(len(box)):
        box_data = box[k][0]
        # print(box_data)
        coord = box_data[0]
        # print(len(coord))
        x, y = [], []
        for j in range(4):
            point = coord[j][0]
            if j == 0:
                end_x = point[1]
                end_y = point[0]
            # print(point)
            y.append(point[0])
            x.append(point[1])
        x.append(end_x)
        y.append(end_y)

        upper_left_x = min(x)
        upper_left_y = min(y)
        bottom_right_x = max(x)
        bottom_right_y = max(y)
        width = abs(bottom_right_x - upper_left_x)
        height = abs(bottom_right_y - upper_left_y)
        # rect = plt.Rectangle((upper_left_x, upper_left_y), width, height)  # 左下角坐标和宽高

        bbox_dict = {'id': i * 10000 + k, 'image_id': i, 'category_id': 1, 'iscrowd': 0, 'area': height * width,
                     'bbox': [upper_left_x, upper_left_y, width, height], 'segmentation': []}
        write_json_context['annotations'].append(bbox_dict)

name = os.path.join(coco_pathDir, set + '.json')
with open(name, 'w') as fw:                                                                # 将字典信息写入.json文件中
    json.dump(write_json_context, fw, indent=2)
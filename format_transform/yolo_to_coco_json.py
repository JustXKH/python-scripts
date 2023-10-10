import os
import json
import cv2

img_id = 0
anno_id = 0

jsonFile = r'F:\pseudo_label\part4\full_part.json'
anno_path = r'F:\pseudo_label\part4\annotations'
img_dir = r'F:\pseudo_label\part4\imgs'

annoId_to_cocoId = {'0': 1, '1': 62, '2': 44}
with open(jsonFile, 'w') as fp:
    json_context = dict()
    json_context['images'] = []
    json_context['annotations'] = []
    json_context['categories'] = [{'id': 1, 'name': 'person', 'supercategory': 'person'},
                                  {'id': 44, 'name': 'bottle', 'supercategory': 'kitchen'},
                                  {'id': 62, 'name': 'chair', 'supercategory': 'furniture'},
                                  {'id': 64, 'name': 'potted plant', 'supercategory': 'furniture'},
                                  {'id': 100, 'name': 'camera', 'supercategory': 'furniture'}]
    for txt in os.listdir(anno_path):
        anno_dict = {}
        img_path = img_dir + os.sep + txt.split('.')[0] + '.jpg'    # 后缀有jpg和png
        img = cv2.imread(img_path)
        JPG = True
        if img is None:
            JPG = False
            img_path = img_dir + os.sep + txt.split('.')[0] + '.png'
            img = cv2.imread(img_path)
        img_height, img_width, _ = img.shape
        print(f'img_path: {img_path}  width：{img_width}, height:{img_height}')
        # continue
        img_dict = {'width': img_width, 'height': img_height}
        if JPG:
            img_name = txt.split('.')[0].lower() + '.jpg'
        else:
            img_name = txt.split('.')[0].lower() + '.png'
        img_dict['file_name'] = 'images/' + img_name
        img_dict['id'] = img_id
        img_id += 1
        json_context['images'].append(img_dict)
        txt_path = anno_path + os.sep + txt
        # anno_dict['image_id'] = img_dict['id']
        # anno_dict['category_id'] = 1
        # anno_dict['iscrowd'] = 0
        # anno_dict['segmentation'] = []
        with open(txt_path, 'r') as f_txt:
            lines = f_txt.read().splitlines()
            print(len(lines))
            for line in lines:
                anno_dict = {'image_id': img_dict['id'], 'iscrowd': 0, 'segmentation': [], 'id': anno_id}
                anno_id += 1
                anno_dict['bbox'] = []
                # print(line)
                print(img_name)
                cls, x_center, y_center, width, height = line.split(' ')
                anno_dict['category_id'] = annoId_to_cocoId[cls]
                bbox_width = float(width) * img_width
                bbox_height = float(height) * img_height
                bbox_top_left_x = float(x_center) * img_width - bbox_width/2
                bbox_top_left_y = float(y_center) * img_height - bbox_height/2
                bbox_area = bbox_height * bbox_width
                anno_dict['area'] = bbox_area
                anno_dict['bbox'].append(bbox_top_left_x)
                anno_dict['bbox'].append(bbox_top_left_y)
                anno_dict['bbox'].append(bbox_width)
                anno_dict['bbox'].append(bbox_height)
                print(anno_dict)
                json_context['annotations'].append(anno_dict)
                print(json_context['annotations'][-1])
                # anno_dict['bbox'] = []
                # anno_dict['area'] = 1

    json.dump(json_context, fp, indent=2)

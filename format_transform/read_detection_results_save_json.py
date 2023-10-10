import json
import os
import cv2
import numpy as np

json_paths = r'D:\head_pose\test_data\tmp\preds'
save_json_path = r'D:\head_pose\test_data\tmp\tmp.json'

json_context = dict()
json_context['images'] = []
json_context['annotations'] = []
json_context['categories'] = [{'id': 1, 'name': 'person', 'supercategory': 'person'},
                              {'id': 44, 'name': 'bottle', 'supercategory': 'kitchen'},
                              {'id': 62, 'name': 'chair', 'supercategory': 'furniture'},
                              {'id': 64, 'name': 'potted plant', 'supercategory': 'furniture'},
                              {'id': 100, 'name': 'camera', 'supercategory': 'furniture'}]
annoId_to_cocoId = {0: 1, 1: 62, 2: 62, 3: 64, 4: 100}
img_id = 0
anno_id = 0

with open(save_json_path, 'w') as fp_json:
    for json_path_li in os.listdir(json_paths):
        json_path = os.path.join(json_paths, json_path_li)
        img_path = json_path.replace('json', 'jpg').replace('preds', 'vis')
        img = cv2.imread(img_path)
        img_height, img_width, _ = img.shape

        img_dict = {'width': img_width, 'height': img_height,
                    'file_name': 'images/' + os.path.basename(img_path), 'id': img_id}

        json_context['images'].append(img_dict)

        with open(json_path, 'r') as fp_read:
            json_data = json.load(fp_read)
            for i, bbox in enumerate(json_data['bboxes']):
                score = float(json_data['scores'][i])
                if score < 0.3:   # threshold
                    continue
                x1, y1, x2, y2 = bbox
                cls_id = json_data['labels'][i]
                print(cls_id)
                anno_dict = {'image_id': img_id, 'category_id': annoId_to_cocoId[cls_id], 'iscrowd': 0, 'id': anno_id,
                             'bbox': [], 'segmentation': []}
                bbox_width = x2 - x1
                bbox_height = y2 - y1
                bbox_area = bbox_height * bbox_width
                anno_dict['area'] = bbox_area
                anno_dict['bbox'].append(x1)
                anno_dict['bbox'].append(y1)
                anno_dict['bbox'].append(bbox_width)
                anno_dict['bbox'].append(bbox_height)
                json_context['annotations'].append(anno_dict)
                anno_id += 1
        img_id += 1

    json.dump(json_context, fp_json, indent=2)



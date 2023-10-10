import os
import cv2
import xml.etree.ElementTree as ET

xml_dir = r'F:\pseudo_label\stage2_round1\annotations'
save_dir = r'F:\person_dataset\stage2_round1\anno'
name_2_id = {'person': 0, 'chair': 1, 'bottle': 2}
for xml_file in os.listdir(xml_dir):
    xml_path = os.path.join(xml_dir, xml_file)
    jpg_path = xml_path.replace('annotations', 'imgs').replace('xml', 'jpg')
    txt_path = xml_path.replace('annotations', 'anno').replace('xml', 'txt')
    fp = open(txt_path, 'w')
    img = cv2.imread(jpg_path)
    img_height, img_width, c = img.shape
    tree = ET.parse(xml_path)
    root = tree.getroot()
    objs = root.findall('object')
    for obj in objs:
        name = obj[0].text
        for box in obj.findall('bndbox'):
            xmin = box[0].text
            ymin = box[1].text
            xmax = box[2].text
            ymax = box[3].text
            bbox_heigth = float(ymax) - float(ymin)
            bbox_width = float(xmax) - float(xmin)
            bbox_center_x = float(xmin) + bbox_width / 2
            bbox_center_y = float(ymin) + bbox_heigth / 2
            line = f'{name_2_id[name]} {bbox_center_x / img_width} {bbox_center_y / img_height}' \
                   f' {bbox_width / img_width} {bbox_heigth / img_height}'
            fp.write(line + '\n')
    fp.close()



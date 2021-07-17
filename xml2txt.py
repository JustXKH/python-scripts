import os
import random
from lxml.etree import Element, SubElement, tostring, ElementTree
import xml.etree.ElementTree as ET

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


xmlfilepath = 'C:\\Users\\xkh\\Desktop\\cen\\0412label\\04100714(120)\\annotations'
txtsavepath = 'C:\\Users\\xkh\\Desktop\\cen\\0412label\\04100714(120)\\annotation'
# if not os.path.exists(txtsavepath):
#     os.mkdir(txtsavepath)
os.makedirs(txtsavepath, exist_ok=True)
classes = ['person']
total_xml = os.listdir(xmlfilepath)
for xmlfile in total_xml:
    xmlfilename = xmlfilepath + '\\' + xmlfile
    with open(xmlfilename, 'r') as xmlf:
        txtname = xmlfile.split('.')[0]  + '.txt'
        outfile = txtsavepath + '\\' + txtname
        txtfile = open(outfile, 'w') 
        tree=ET.parse(xmlf)
        root = tree.getroot()
        size = root.find('size')  
        w = int(size.find('width').text)
        h = int(size.find('height').text)
    
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes :
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')   
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
            txtfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    txtfile.close()
    print(f'{outfile}写入成功！')

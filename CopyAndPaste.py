import cv2

def issmallobject(bbox, thresh):
    if bbox[0] * bbox[1] <= thresh:
        return True
    else:
        return False

def read_label_txt(label_dir):
    labels = []
    with open(label_dir) as fp:
        for f in fp.readlines():
            labels.append(f.strip().split(' '))
    return labels

def rescale_yolo_labels(labels, img_shape):
    height, width, nchannel = img_shape
    rescale_boxes = []
    for box in list(labels):
        x_c = float(box[1]) * width
        y_c = float(box[2]) * height
        w = float(box[3]) * width
        h = float(box[4]) * height
        x_left = x_c - w * .5
        y_left = y_c - h * .5
        x_right = x_c + w * .5
        y_right = y_c + h * .5
        rescale_boxes.append([box[0], int(x_left), int(y_left), int(x_right), int(y_right)])
    return rescale_boxes

def random_add_patches(bbox, rescale_boxes, shape, paste_number, iou_thresh):
    temp = []
    for rescale_bbox in rescale_boxes:
        temp.append(rescale_bbox)
    cl, x_left, y_left, x_right, y_right = bbox
    bbox_w, bbox_h = x_right - x_left, y_right - y_left
    center_search_space = sampling_new_bbox_center_point(shape, bbox)
    success_num = 0
    new_bboxes = []
    while success_num < paste_number:
        new_bbox_x_center, new_bbox_y_center = norm_sampling(center_search_space)
        print(norm_sampling(center_search_space))
        new_bbox_x_left, new_bbox_y_left, new_bbox_x_right, new_bbox_y_right = new_bbox_x_center - 0.5 * bbox_w, \
                                                                               new_bbox_y_center - 0.5 * bbox_h, \
                                                                               new_bbox_x_center + 0.5 * bbox_w, \
                                                                               new_bbox_y_center + 0.5 * bbox_h
        new_bbox = [cl, int(new_bbox_x_left), int(new_bbox_y_left), int(new_bbox_x_right), int(new_bbox_y_right)]
        ious = [bbox_iou(new_bbox, bbox_t) for bbox_t in rescale_boxes]
        if max(ious) <= iou_thresh:
            # for bbox_t in rescale_boxes:
            # iou =  bbox_iou(new_bbox[1:],bbox_t[1:])
            # if(iou <= iou_thresh):
            success_num += 1
            temp.append(new_bbox)
            new_bboxes.append(new_bbox)
        else:
            continue
    return new_bboxes


def copysmallobjects(image_dir, label_dir, save_base_dir, save_crop_base_dir=None,
                     save_annoation_base_dir=None):
    image = cv2.imread(image_dir)

    labels = read_label_txt(label_dir)
    if len(labels) == 0: return
    rescale_labels = rescale_yolo_labels(labels, image.shape)  # 转换坐标表示
    all_boxes = []

    for idx, rescale_label in enumerate(rescale_labels):

        all_boxes.append(rescale_label)
        # 目标的长宽
        rescale_label_height, rescale_label_width = rescale_label[4] - rescale_label[2], rescale_label[3] - \
                                                    rescale_label[1]

        if (issmallobject((rescale_label_height, rescale_label_width), thresh=64 * 64) and rescale_label[0] == '1'):
            roi = image[rescale_label[2]:rescale_label[4], rescale_label[1]:rescale_label[3]]

            new_bboxes = random_add_patches(rescale_label, rescale_labels, image.shape, paste_number=2, iou_thresh=0.2)
            count = 0

            # 将新生成的位置加入到label,并在相应位置画出物体
            for new_bbox in new_bboxes:
                count += 1
                all_boxes.append(new_bbox)
                cl, bbox_left, bbox_top, bbox_right, bbox_bottom = new_bbox[0], new_bbox[1], new_bbox[2], new_bbox[3], \
                                                                   new_bbox[4]
                try:
                    if (count > 1):
                        roi = flip_bbox(roi)
                    image[bbox_top:bbox_bottom, bbox_left:bbox_right] = roi
                except ValueError:
                    continue

    dir_name = find_str(image_dir)
    save_dir = join(save_base_dir, dir_name)
    check_dir(save_dir)
    yolo_txt_dir = join(save_dir, basename(image_dir.replace('.jpg', '_augment.txt')))
    cv2.imwrite(join(save_dir, basename(image_dir).replace('.jpg', '_augment.jpg')), image)
    convert_all_boxes(image.shape, all_boxes, yolo_txt_dir)
import os
import time

import cv2
import random
import math
import numpy as np
from PIL import Image


def blur_img_by_block(img, by_block=True):
    h, w, c = img.shape
    h_step = 8
    w_step = 8
    if by_block:
        for i in range(0, h, h_step):
            for j in range(0, w, w_step):
                # Create ROI coordinates
                block_h_max = min(h, i + h_step)
                block_w_max = max(w, j + w_step)
                # Grab ROI with Numpy slicing and blur
                block = img[i:block_h_max, j:block_w_max]
                kernel = random.randint(1, 12)
                # kernel = 7
                blur = cv2.GaussianBlur(block, (kernel if kernel % 2 == 1 else 3, kernel + 2 if kernel % 2 == 1 else 3), 0)
                # blur = cv2.GaussianBlur(block, (3, 3), 0)
                # blur = cv2.blur(block, (3, 3))
                # blur = cv2.medianBlur(block, 3)
                # blur = cv2.filter2D(block, ddepth=-1, kernel=1)
                # blur = cv2.filter2D(block, ddepth=-1, kernel=None)  # MotionBlur, AdvancedBlur
                # Insert ROI back into image
                img[i:block_h_max, j:block_w_max] = blur
    else:
        kernel = random.randint(1, 3)
        kernel = 7
        # img = cv2.GaussianBlur(img, (kernel if kernel % 2 == 1 else 1, kernel if kernel % 2 == 1 else 1), 0)
        img = cv2.blur(img, (kernel if kernel % 2 == 1 else 1, kernel if kernel % 2 == 1 else 1))
        # img = cv2.medianBlur(img, kernel if kernel % 2 == 1 else 1)
    return img




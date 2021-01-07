# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:36:56 2021

@author: kuanyu
"""
import os
import cv2

path = 'training_hr_images'
output_path = path+'x8'

if(not os.path.exists(output_path)):
    os.mkdir(output_path)
for img in os.listdir(path):
    src = cv2.imread(path+'/'+img)
    (filename, extension) = os.path.splitext(img)
    cv2.imwrite(os.path.join(output_path, filename+'_0'+extension), src)

    rot90 = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(output_path, filename+'_1'+extension), rot90)

    hor_flip = cv2.flip(rot90, 1)
    cv2.imwrite(os.path.join(output_path, filename+'_2'+extension), hor_flip)

    rot180 = cv2.rotate(src, cv2.ROTATE_180)
    cv2.imwrite(os.path.join(output_path, filename+'_3'+extension), rot180)

    hor_flip = cv2.flip(rot180, 1)
    cv2.imwrite(os.path.join(output_path, filename+'_4'+extension), hor_flip)

    hor_flip = cv2.flip(src, 1)
    cv2.imwrite(os.path.join(output_path, filename+'_5'+extension), hor_flip)

    ver_flip = cv2.flip(src, 0)
    cv2.imwrite(os.path.join(output_path, filename+'_6'+extension), ver_flip)

    flip = cv2.flip(src, -1)
    cv2.imwrite(os.path.join(output_path, filename+'_7'+extension), flip)

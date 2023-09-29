from paths import train_coco, val_coco
import json
from collections import defaultdict
import numpy as np
import cv2
import os

os.mkdir('labels_t')

with open(train_coco, encoding="utf-8") as file:
    gt_train = json.load(file)

im_anns_gt_train = defaultdict(list)
for ann in gt_train["annotations"]:
    im_anns_gt_train[ann["image_id"]].append(ann)

gt_mask_train = np.zeros((1001, 512, 512), np.int32)
for id, im in im_anns_gt_train.items():
    for ann in im:
        points = np.array([ann["segmentation"][0][::2], ann["segmentation"][0][1::2]], np.int32).T
        points = points.reshape((-1, 1, 2))
        tmp = np.zeros((512, 512), np.int32)
        color = 0
        if ann["category_id"] == 1 or ann["category_id"] == 2 or ann["category_id"] == 3 or ann["category_id"] == 4 or \
                ann["category_id"] == 5 or ann["category_id"] == 6 or ann["category_id"] == 7 or ann[
            "category_id"] == 8:
            color = ann["category_id"]
        elif ann["category_id"] == 13:
            color = 9
        elif ann["category_id"] == 16:
            color = 10
        else:
            color = 11
        cv2.fillPoly(tmp, [points], color)
        gt_mask_train[id, tmp > 0] = color
    cv2.imwrite("labels_t/" + str(id) + ".png", gt_mask_train[id])


with open(val_coco, encoding="utf-8") as file:
    gt_val = json.load(file)

im_anns_gt_val = defaultdict(list)
for ann in gt_val["annotations"]:
    im_anns_gt_val[ann["image_id"]].append(ann)

gt_mask_val = np.zeros((1001, 512, 512), np.int32)
for id, im in im_anns_gt_val.items():
    for ann in im:
        points = np.array([ann["segmentation"][0][::2], ann["segmentation"][0][1::2]], np.int32).T
        points = points.reshape((-1, 1, 2))
        tmp = np.zeros((512, 512), np.int32)
        if ann["category_id"] == 1 or ann["category_id"] == 2 or ann["category_id"] == 3 or ann["category_id"] == 4 or \
                ann["category_id"] == 5 or ann["category_id"] == 6 or ann["category_id"] == 7 or ann[
            "category_id"] == 8:
            color = ann["category_id"]
        elif ann["category_id"] == 13:
            color = 9
        elif ann["category_id"] == 16:
            color = 10
        else:
            color = 11
        cv2.fillPoly(tmp, [points], color)
        gt_mask_val[id, tmp > 0] = color
    cv2.imwrite("labels_t/" + str(id + 1000) + ".png", gt_mask_val[id])

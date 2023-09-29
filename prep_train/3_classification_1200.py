import json
import os
from shutil import copyfile
from paths import train_coco, train_img, val_coco, val_img

f = open(train_coco, encoding="utf-8")
dict_train = json.load(f)

f = open(val_coco, encoding="utf-8")
dict_val = json.load(f)

a = [[0 for ii in range(25)] for jj in range(1000)]
b = [[0 for ii in range(25)] for jj in range(200)]

for i in dict_train['annotations']:
    a[i['image_id'] - 1][i['category_id'] - 1] = i['category_id']

for i in dict_val['annotations']:
    b[i['image_id'] - 1][i['category_id'] - 1] = i['category_id']

os.mkdir('classification_1200')
os.mkdir('classification_1200/images')
os.mkdir('classification_1200/labels')
os.mkdir('classification_1200/images/c1')
os.mkdir('classification_1200/images/c2')
os.mkdir('classification_1200/images/c3')
os.mkdir('classification_1200/labels/c1')
os.mkdir('classification_1200/labels/c2')
os.mkdir('classification_1200/labels/c3')

for x in range(1000):
    type = 0

    for y in range(25):
        if a[x][y] == 1 or a[x][y] == 2 or a[x][y] == 3 or a[x][y] == 4 or a[x][y] == 20 or a[x][y] == 21 or a[x][y] == 22 or a[x][y] == 23:
            type = 1
    if a[x][0] != 1 and a[x][1] != 2 and a[x][2] != 3 and a[x][3] != 4 and a[x][19] != 20 and a[x][20] != 21 and \
            a[x][21] != 22 and a[x][22] != 23 and a[x][5] != 6 and a[x][6] != 7 and a[x][7] != 8 and a[x][
        8] != 9 and a[x][9] != 10 and a[x][10] != 11 and a[x][11] != 12:
        type = 2
    if (a[x][5] == 6 and a[x][12] == 13) or (a[x][8] == 9 and a[x][12] == 13) or (a[x][5] == 6 and a[x][15] == 16) or (a[x][5] == 6 and a[x][17] == 18) or (a[x][5] == 6 and a[x][13] == 14):
        type = 2
    if a[x][0] != 1 and a[x][1] != 2 and a[x][2] != 3 and a[x][3] != 4 and a[x][19] != 20 and a[x][20] != 21 and \
            a[x][21] != 22 and a[x][22] != 23 and a[x][12] != 13 and a[x][13] != 14 and a[x][14] != 15 and a[x][
        15] != 16 and a[x][16] != 17 and a[x][17] != 18 and a[x][18] != 19 and a[x][23] != 24 and a[x][24] != 25:
        type = 3

    copyfile(train_img + "/" + str(x + 1) + ".png", "classification_1200/images/c" + str(type) + "/" + str(x + 1) + ".png")
    copyfile("labels/" + str(x + 1) + ".png", "classification_1200/labels/c" + str(type) + "/" + str(x + 1) + ".png")
    # RCA LCX LAD LAD+LCX

for x in range(200):
    type = 0

    for y in range(25):
        if b[x][y] == 1 or b[x][y] == 2 or b[x][y] == 3 or b[x][y] == 4 or b[x][y] == 20 or b[x][y] == 21 or b[x][y] == 22 or b[x][y] == 23:
            type = 1
    if b[x][0] != 1 and b[x][1] != 2 and b[x][2] != 3 and b[x][3] != 4 and b[x][19] != 20 and b[x][20] != 21 and \
            b[x][21] != 22 and b[x][22] != 23 and b[x][5] != 6 and b[x][6] != 7 and b[x][7] != 8 and b[x][
        8] != 9 and b[x][9] != 10 and b[x][10] != 11 and b[x][11] != 12:
        type = 2
    if (b[x][5] == 6 and b[x][12] == 13) or (b[x][8] == 9 and b[x][12] == 13) or (b[x][5] == 6 and b[x][15] == 16) or (b[x][5] == 6 and b[x][17] == 18) or (b[x][5] == 6 and b[x][13] == 14):
        type = 2
    if b[x][0] != 1 and b[x][1] != 2 and b[x][2] != 3 and b[x][3] != 4 and b[x][19] != 20 and b[x][20] != 21 and \
            b[x][21] != 22 and b[x][22] != 23 and b[x][12] != 13 and b[x][13] != 14 and b[x][14] != 15 and b[x][
        15] != 16 and b[x][16] != 17 and b[x][17] != 18 and b[x][18] != 19 and b[x][23] != 24 and b[x][24] != 25:
        type = 3

    copyfile(val_img + "/" + str(x + 1) + ".png", "classification_1200/images/c" + str(type) + "/" + str(x + 1001) + ".png")
    copyfile("labels/" + str(x + 1001) + ".png", "classification_1200/labels/c" + str(type) + "/" + str(x + 1001) + ".png")
    # RCA LCX LAD LAD+LCX

os.rename('classification_1200/images/c1', 'classification_1200/images/RCA')
os.rename('classification_1200/images/c2', 'classification_1200/images/LCX')
os.rename('classification_1200/images/c3', 'classification_1200/images/LAD')
os.rename('classification_1200/labels/c1', 'classification_1200/labels/RCA')
os.rename('classification_1200/labels/c2', 'classification_1200/labels/LCX')
os.rename('classification_1200/labels/c3', 'classification_1200/labels/LAD')

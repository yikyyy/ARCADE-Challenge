import json
import os
from shutil import copyfile
from paths import train_coco, train_img

f = open(train_coco, encoding="utf-8")
dict_train = json.load(f)

a = [[0 for ii in range(25)] for jj in range(1000)]

for i in dict_train['annotations']:
    a[i['image_id'] - 1][i['category_id'] - 1] = i['category_id']

os.mkdir('classification')
os.mkdir('classification/images')
os.mkdir('classification/labels')
os.mkdir('classification/images/c1')
os.mkdir('classification/images/c2')
os.mkdir('classification/images/c3')
os.mkdir('classification/labels/c1')
os.mkdir('classification/labels/c2')
os.mkdir('classification/labels/c3')

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

    copyfile(train_img + "/" + str(x + 1) + ".png", "classification/images/c" + str(type) + "/" + str(x + 1) + ".png")
    copyfile("labels/" + str(x + 1) + ".png", "classification/labels/c" + str(type) + "/" + str(x + 1) + ".png")
    # RCA LCX LAD LAD+LCX

os.rename('classification/images/c1', 'classification/images/RCA')
os.rename('classification/images/c2', 'classification/images/LCX')
os.rename('classification/images/c3', 'classification/images/LAD')
os.rename('classification/labels/c1', 'classification/labels/RCA')
os.rename('classification/labels/c2', 'classification/labels/LCX')
os.rename('classification/labels/c3', 'classification/labels/LAD')

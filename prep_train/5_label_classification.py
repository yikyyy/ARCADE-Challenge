import cv2
import os

path1 = 'classification_1000/labels/RCA'
path2 = 'classification_1000/labels/LCX'
path3 = 'classification_1000/labels/LAD'
path4 = 'classification_1200/labels/RCA'
path5 = 'classification_1200/labels/LCX'
path6 = 'classification_1200/labels/LAD'

def changeRCA(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        file_path = os.path.join(dir_path, file)
        img = cv2.imread(file_path, 0)
        img[img == 20] = 5
        img[img == 21] = 6
        img[img == 22] = 7
        img[img == 23] = 8
        cv2.imwrite(file_path, img)

def changeLCX(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        file_path = os.path.join(dir_path, file)
        img = cv2.imread(file_path, 0)
        img[img == 5] = 1
        img[img == 6] = 2
        img[img == 7] = 3
        img[img == 8] = 4
        img[img == 9] = 5
        img[img == 10] = 6
        img[img == 11] = 7
        img[img == 12] = 8
        img[img == 13] = 9
        img[img == 14] = 10
        img[img == 15] = 11
        img[img == 16] = 12
        img[img == 17] = 13
        img[img == 18] = 14
        img[img == 19] = 15
        img[img == 24] = 16
        img[img == 25] = 17
        cv2.imwrite(file_path, img)

def changeLAD(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        file_path = os.path.join(dir_path, file)
        img = cv2.imread(file_path, 0)
        img[img == 5] = 1
        img[img == 6] = 2
        img[img == 7] = 3
        img[img == 8] = 4
        img[img == 9] = 5
        img[img == 10] = 6
        img[img == 11] = 7
        img[img == 12] = 8
        cv2.imwrite(file_path, img)

changeRCA(path1)
changeRCA(path4)
changeLCX(path2)
changeLCX(path5)
changeLAD(path3)
changeLAD(path6)

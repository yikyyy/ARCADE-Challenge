import os
from shutil import copyfile
from paths import train_img, val_img

if os.path.exists('labels_t_1000') is False:
    os.mkdir('labels_t_1000')
if os.path.exists('imgs_1000') is False:
    os.mkdir('imgs_1000')
if os.path.exists('imgs_1200') is False:
    os.mkdir('imgs_1200')

for i in range(1000):
    copyfile("labels_t/" + str(i+1) + ".png", "labels_t_1000/" + str(i+1) + ".png")
    copyfile(train_img + "/" + str(i+1) + ".png", "imgs_1000/" + str(i+1) + ".png")
    copyfile(train_img + "/" + str(i+1) + ".png", "imgs_1200/" + str(i+1) + ".png")

for i in range(200):
    copyfile(val_img + "/" + str(i+1) + ".png", "imgs_1200/" + str(i+1001) + ".png")

os.rename('labels_t', 'labels_t_1200')
os.rename('classification', 'classification_1000')

path1_i = 'imgs_1000'
path2_i = 'imgs_1200'
path3_i = 'classification_1000/images/RCA'
path4_i = 'classification_1000/images/LCX'
path5_i = 'classification_1000/images/LAD'
path6_i = 'classification_1200/images/RCA'
path7_i = 'classification_1200/images/LCX'
path8_i = 'classification_1200/images/LAD'
path1_l = 'labels_t_1000'
path2_l = 'labels_t_1200'
path3_l = 'classification_1000/labels/RCA'
path4_l = 'classification_1000/labels/LCX'
path5_l = 'classification_1000/labels/LAD'
path6_l = 'classification_1200/labels/RCA'
path7_l = 'classification_1200/labels/LCX'
path8_l = 'classification_1200/labels/LAD'

def rename_dir_img(dir_path, task_name):
    files = os.listdir(dir_path)
    for file in files:
        name_int = int(os.path.splitext(file)[0])
        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, task_name + "_" + "{:0>4d}".format(name_int) + "_0000.png"))

def rename_dir_label(dir_path, task_name):
    files = os.listdir(dir_path)
    for file in files:
        name_int = int(os.path.splitext(file)[0])
        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, task_name + "_" + "{:0>4d}".format(name_int) + ".png"))

rename_dir_img(path1_i, "trunk")
rename_dir_img(path2_i, "trunk")
rename_dir_img(path3_i, "rca")
rename_dir_img(path4_i, "lcx")
rename_dir_img(path5_i, "lad")
rename_dir_img(path6_i, "rca")
rename_dir_img(path7_i, "lcx")
rename_dir_img(path8_i, "lad")
rename_dir_label(path1_l, "trunk")
rename_dir_label(path2_l, "trunk")
rename_dir_label(path3_l, "rca")
rename_dir_label(path4_l, "lcx")
rename_dir_label(path5_l, "lad")
rename_dir_label(path6_l, "rca")
rename_dir_label(path7_l, "lcx")
rename_dir_label(path8_l, "lad")

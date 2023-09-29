from PIL import Image
import os
from shutil import copyfile
from paths import train_img, val_img

for i in range(0, 1000):
    img_path = os.path.join(train_img, str(i+1) + '.png')
    img = Image.open(img_path)
    if img.getbands() == ('R', 'G', 'B'):
        img = img.convert('L')
        print(img.getbands(), str(i + 1))
        os.remove(img_path)
        img.save(img_path)

for i in range(0, 200):
    img_path = os.path.join(val_img, str(i+1) + '.png')
    img = Image.open(img_path)
    if img.getbands() == ('R', 'G', 'B'):
        img = img.convert('L')
        print(img.getbands(), str(i + 1001))
        os.remove(img_path)
        img.save(img_path)

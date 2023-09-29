if __name__ == '__main__':
    from nnUNet.nnunetv2.paths import nnUNet_raw
    import os
    import cv2
    import numpy as np
    from shutil import copyfile

    trunk_res_path = os.path.join(nnUNet_raw, 'Dataset001_Trunk', 'imagesTs_pred')
    trunk_img_path = os.path.join(nnUNet_raw, 'Dataset001_Trunk', 'imagesTs')
    out_path_rca = os.path.join(nnUNet_raw, 'Dataset002_RCA', 'imagesTs')
    out_path_lcx = os.path.join(nnUNet_raw, 'Dataset003_LCX', 'imagesTs')
    out_path_lad = os.path.join(nnUNet_raw, 'Dataset004_LAD', 'imagesTs')

    if os.path.exists(out_path_rca) is False:
        os.mkdir(out_path_rca)
    if os.path.exists(out_path_lcx) is False:
        os.mkdir(out_path_lcx)
    if os.path.exists(out_path_lad) is False:
        os.mkdir(out_path_lad)

    files = os.listdir(trunk_res_path)

    for i in range(len(files)):
        flag = 0
        img_name_load = "test_" + "{:0>4d}".format(i + 1) + ".png"
        img_name_save = "test_" + "{:0>4d}".format(i + 1) + "_0000.png"
        in_path = os.path.join(trunk_res_path, img_name_load)
        out_path = os.path.join(trunk_img_path, img_name_save)
        if os.path.exists(in_path) is False:
            break
        img = cv2.imread(in_path, 0)
        img = np.uint8(img)

        if 9 in img or 10 in img:
            flag = flag + 1
        if 6 in img or 7 in img or 8 in img:
            flag = flag + 10
        if 1 in img or 2 in img or 3 in img or 4 in img:
            flag = 100
        
        if flag == 100:
            copyfile(out_path, os.path.join(out_path_rca, img_name_save))
        elif flag == 10:
            copyfile(out_path, os.path.join(out_path_lad, img_name_save))
        else:
            copyfile(out_path, os.path.join(out_path_lcx, img_name_save))
        
        print(str(i+1) + " classification done!")

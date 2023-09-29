if __name__ == "__main__":
    import os

    os.system('python 1_prep_data.py')
    os.system('python 2_pred_trunk.py')
    os.system('python 3_classification.py')
    os.system('python 4_pred_rca.py')
    os.system('python 5_pred_lcx.py')
    os.system('python 6_pred_lad.py')
    os.system('python 7_mask2coco.py')

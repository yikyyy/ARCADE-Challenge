if __name__ == '__main__':
    from nnUNet.nnunetv2.paths import nnUNet_results, nnUNet_raw
    import torch
    from batchgenerators.utilities.file_and_folder_operations import join
    from nnUNet.nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
    import os
    import cv2
    import numpy as np

    # instantiate the nnUNetPredictor
    predictor = nnUNetPredictor(
        tile_step_size=0.5,
        use_gaussian=True,
        use_mirroring=True,
        perform_everything_on_gpu=True,
        device=torch.device('cuda' if torch.cuda.is_available() else 'cpu'),
        verbose=False,
        verbose_preprocessing=False,
        allow_tqdm=True
    )
    # initializes the network architecture, loads the checkpoint
    predictor.initialize_from_trained_model_folder(
        join(nnUNet_results, 'Dataset004_LAD/nnUNetTrainer__nnUNetPlans__2d'),
        use_folds=(0, 1, 2, 3, 4),
        checkpoint_name='checkpoint_final.pth',
    )
    # variant 1: give input and output folders
    predictor.predict_from_files(join(nnUNet_raw, 'Dataset004_LAD/imagesTs'),
                                join(nnUNet_raw, 'Dataset004_LAD/imagesTs_pred'),
                                save_probabilities=False, overwrite=True,
                                num_processes_preprocessing=2, num_processes_segmentation_export=2,
                                folder_with_segs_from_prev_stage=None, num_parts=1, part_id=0)

    npy_path = os.path.join(nnUNet_results, 'npy')
    if os.path.exists(npy_path) is False:
        os.mkdir(npy_path)

    rca_res_path = os.path.join(nnUNet_raw, 'Dataset004_LAD/imagesTs_pred')
    files = os.listdir(rca_res_path)

    for file in files:
        if file.endswith('.png') is False:
            continue

        img_id = int(file[5:9])
        npy_name = str(img_id) + '.npy'
        file_path = os.path.join(rca_res_path, file)
        save_path = os.path.join(npy_path, npy_name)
        img = cv2.imread(file_path, 0)
        img = np.uint8(img)
        mask = np.zeros((27, 512, 512))

        mask[5][img == 1] = 1
        mask[6][img == 2] = 1
        mask[7][img == 3] = 1
        mask[8][img == 4] = 1
        mask[9][img == 5] = 1
        mask[10][img == 6] = 1
        mask[11][img == 7] = 1
        mask[12][img == 8] = 1

        np.save(save_path, mask)
        print('save ' + npy_name)

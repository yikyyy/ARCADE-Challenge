if __name__ == '__main__':
    from skimage import measure
    from shapely.geometry import Polygon
    import json
    import numpy as np
    from nnUNet.nnunetv2.paths import nnUNet_results
    import os

    num = 300

    gt_mask = np.zeros([num+1, 27, 512, 512])

    ss = []
    for i in range(num):
        ss.append(str(i+1))
    ss.sort()
    nn = [1]*num
    for i in range(num):
        nn[int(ss[i])-1] = i+1

    npy_path = os.path.join(nnUNet_results, 'npy')
    ea_path = os.path.join('empty_annotations.json')
    folderpath_write = r'/output/'
    sub_path = os.path.join(folderpath_write, 'coronary-artery-segmentation.json')

    files = os.listdir(npy_path)

    for i in range(len(files)):
        in_path = os.path.join(npy_path, str(i+1) + '.npy')
        mask = np.load(in_path)
        gt_mask[i+1] = mask
        print(str(i+1) + " ok!")

    with open(ea_path) as file:
        gt = json.load(file)

    empty_submit = dict()
    empty_submit["info"] = gt["info"]
    empty_submit["licenses"] = gt["licenses"]
    empty_submit["images"] = gt["images"]
    empty_submit["categories"] = gt["categories"]
    empty_submit["annotations"] = []

    count_anns = 1
    for img_id, img in enumerate(gt_mask, 0):
        for cls_id, cls in enumerate(img, 0):
            contours = measure.find_contours(cls)
            for contour in contours:
                for i in range(len(contour)):
                    row, col = contour[i]
                    contour[i] = (col - 1, row - 1)

                # Simplify polygon
                poly = Polygon(contour)
                poly = poly.simplify(1.0, preserve_topology=False)

                if poly.area < 600:
                    continue
                if cls_id == 6 and poly.area < 1000:
                    continue
                if cls_id == 9 and (poly.area < 800 or poly.area > 1900):
                    continue
                if cls_id == 10 or cls_id == 15 or cls_id == 17 or cls_id == 24 or cls_id == 25:
                    continue
                if cls_id == 14 and poly.area > 900:
                    continue
                if cls_id == 16 and poly.area < 800:
                    continue
                if cls_id == 21 or (cls_id == 22 and poly.area < 1000):
                    continue
                if (poly.is_empty):
                    continue

                segmentation = np.array(poly.exterior.coords).ravel().tolist()
                new_ann = dict()
                new_ann["id"] = count_anns
                new_ann["image_id"] = nn[img_id-1]
                new_ann["category_id"] = cls_id
                new_ann["segmentation"] = [segmentation]
                new_ann["area"] = poly.area
                x, y = contour.min(axis=0)
                w, h = contour.max(axis=0) - contour.min(axis=0)
                new_ann["bbox"] = [int(x), int(y), int(w), int(h)]
                new_ann["iscrowd"] = 0
                new_ann["attributes"] = {
                    "occluded": False
                }
                print("count_anns: " + str(count_anns))
                count_anns = count_anns + 1
                empty_submit["annotations"].append(new_ann.copy())

    with open(sub_path, "w", encoding='ascii') as file:
        json.dump(empty_submit, file)

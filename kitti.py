#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-24 15:18:47
# @Author  : Tuo Feng (fengt@stu.xidian.edu.cn)
# @Link    : https://blog.csdn.net/taifengzikai/
# @Version : $1.0$

import json
import pickle
import numpy as np
import os.path as osp

class kittidataset(object):
    def __init__(self, detection_file):
        self.detection_file =detection_file
        self.fp = open(self.detection_file,"rb+")
        self.detection = pickle.load(self.fp)
    "dict_keys(['name', 'truncated', 'occluded', 'alpha', 'bbox', " \
    "'dimensions', 'location', 'rotation_y', 'score', 'metadata'])"

    # def analysis_detection(self):
    #     self.data = self.detection
    def __len__(self):
        return len(self.detection)

    # def save_kitti(self, kitti_infos_test_video):
    #     # file = "kitti_infos_train.pkl"
    #     filename = './results/000002/test/output_test_video_kalman.pkl'#self.output_path
    #     print(f"Kitti info test video file is saved to {filename}")
    #     with open('./results/000002/test/output_test_video_kalman.pkl', "wb") as f:
    #         pickle.dump(kitti_infos_test_video, f)

    def get_label_anno(self, tracking_results):
        annotations = {}
        annotations.update(
            {
                "name": [],
                "truncated": [],
                "occluded": [],
                "alpha": [],
                "bbox": [],
                "dimensions": [],
                "location": [],
                "rotation_y": [],
                "score": [],
            }
        )

        ind = 0
        for gt in tracking_results:
            name = gt['tracking_name']
            truncated = -1
            occluded = -1
            alpha = -1
            bbox = [-1, -1, -1, -1]
            dimensions = np.array([float(dim) for dim in gt['size']])
            location = np.array([float(loc) for loc in gt['translation']])
            rotation_y = float(gt['rotation'])
            score = float(gt['tracking_score'])

            annotations['name'].append(name)
            annotations['truncated'].append(truncated)
            annotations['occluded'].append(occluded)
            annotations['alpha'].append(alpha)
            annotations['bbox'].append(bbox)
            annotations['dimensions'].append(dimensions)
            annotations['location'].append(location)
            annotations['rotation_y'].append(rotation_y)
            annotations['score'].append(score)

        annotations['name'] = np.array(annotations['name'])
        annotations['truncated'] = np.array(annotations['truncated'])
        annotations['occluded'] = np.array(annotations['occluded'])
        annotations['alpha'] = np.array(annotations['alpha'])
        annotations['bbox'] = np.array(annotations['bbox'])
        annotations['dimensions'] = np.array(annotations['dimensions'])
        annotations['location'] = np.array(annotations['location'])
        annotations['rotation_y'] = np.array(annotations['rotation_y'])
        annotations['score'] = np.array(annotations['score'], np.int32)

        return annotations


    # def get_kitti_image_info(
    #         path,
    #         label_info=True,
    #         velodyne=True,
    #         calib=True,
    #         txt_name='train_filter.txt'
    # ):
    #     config_txt = osp.join(path, 'labels_filer', txt_name)
    #     image_infos = []
    #     with open(config_txt, 'r') as wf:
    #         lines = wf.readlines()
    #         for line in lines:
    #             # parse line
    #             record = json.loads(line.strip())
    #             idx = record['id']
    #
    #             info = {}
    #             pc_info = {"num_features": 4}
    #             calib_info = {}
    #
    #             image_info = {"image_idx": idx}
    #             annotations = None
    #             if velodyne:
    #                 pc_info["velodyne_path"] = osp.join(path, record['path'])
    #             if label_info:
    #                 annotations = self.get_label_anno(record['gts'])
    #             info["image"] = image_info
    #             info["point_cloud"] = pc_info
    #             if calib:
    #                 P0 = np.eye(4)
    #                 P1 = np.eye(4)
    #                 P2 = np.eye(4)
    #                 P3 = np.eye(4)
    #                 rect_4x4 = np.eye(4)
    #                 Tr_velo_to_cam = np.eye(4)
    #                 Tr_imu_to_velo = np.eye(4)
    #
    #                 calib_info["P0"] = P0
    #                 calib_info["P1"] = P1
    #                 calib_info["P2"] = P2
    #                 calib_info["P3"] = P3
    #                 calib_info["R0_rect"] = rect_4x4
    #                 calib_info["Tr_velo_to_cam"] = Tr_velo_to_cam
    #                 calib_info["Tr_imu_to_velo"] = Tr_imu_to_velo
    #                 info["calib"] = calib_info
    #
    #             if annotations is not None:
    #                 info["annos"] = annotations
    #             image_infos.append(info)
    #
    #     return image_infos

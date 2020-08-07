import cv2
import numpy as np
from depthai_helpers.tensor_utils import get_tensor_output, get_tensor_outputs_list, get_tensor_outputs_dict


def decode_landmarks_recognition(nnet_packet, **kwargs):
    landmarks_tensor = get_tensor_output(nnet_packet, 0)
    landmarks = []
    for i in landmarks_tensor[0]:
        landmarks.append(i[0][0])
    
    landmarks = list(zip(*[iter(landmarks)]*2))
    return landmarks

def show_landmarks_recognition(entries_prev, frame, **kwargs):
    img_h = frame.shape[0]
    img_w = frame.shape[1]

    if len(entries_prev) != 0:
        for i in entries_prev:
            try:
                x = int(i[0]*img_h)
                y = int(i[1]*img_w)
            except:
                continue
            # # print(x,y)
            cv2.circle(frame, (x,y), 3, (0, 0, 255))

    frame = cv2.resize(frame, (300, 300))

    return frame
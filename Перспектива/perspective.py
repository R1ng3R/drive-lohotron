import cv2
import numpy as np
import time
# Turn on Laptop's webcam

def perspective(path, image_coords):
    img = cv2.imread(path)
    w_res, h_res = img.shape[:2]
    coords = [image_coords[0:2], image_coords[2:4], image_coords[4:6], image_coords[6:8], image_coords[8:10], image_coords[10:12]]
    zero_coord = min(coords[4:], key=lambda x: x[0])
    biggest_coord = max(coords[4:], key=lambda x: x[0])
    biggest_coord = [biggest_coord[0] - zero_coord[0], biggest_coord[1] - zero_coord[1]]
    coords = coords[:4]
    for i in range(len(coords)):
        coords[i] = [(coords[i][0] - zero_coord[0]) * h_res / biggest_coord[0], (coords[i][1] - zero_coord[1]) * w_res / biggest_coord[1]]
    sr_X = sum(map(lambda x: x[0], coords))/4
    sr_Y = sum(map(lambda x: x[1], coords))/4
    lup = []
    ldown = []
    rup = []
    rdown = []
    for i in coords:
        if i[0] < sr_X and i[1] < sr_Y:
            lup = i
        if i[0] > sr_X and i[1] < sr_Y:
            rup = i
        if i[0] < sr_X and i[1] > sr_Y:
            ldown = i
        if i[0] > sr_X and i[1] > sr_Y:
            rdown = i
    pts1 = np.float32([lup, rup,
                       ldown, rdown])
    pts2 = np.float32([[0, 0], [h_res, 0],
                       [0, h_res], [h_res, h_res]])
    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (h_res,h_res))
    # Wrap the transformed image
    cv2.imshow('frame', img)  # Initial Capture
    cv2.imshow('frame1', result)  # Transformed Capture

    if cv2.waitKey(24) == 27:
        return
    print(f'static/images/perspectived/{path.split("/")[-1].split(".")[0] + "ready." + path.split("/")[-1].split(".")[1]}')
    cv2.imwrite(f'static/images/perspectived/{path.split("/")[-1].split(".")[0] + "ready." + path.split("/")[-1].split(".")[1]}', result)

#perspective('static\\unzip\\RealTime.zip\\RealTime\\17\\RealTime\\17_87f1b34d-f188-439d-bd9f-65188e4cde23.png', (304, 163, 703, 163, 319, 522, 621, 651, 126, 88, 754, 607))
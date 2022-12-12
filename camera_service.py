import os
import time
from datetime import datetime
from multiprocessing import Process
import logging
import json

import numpy as np
import cv2


import logger as logger


logger.setup_logging('camera.log')
cache_dir = '/home/andrew/cache'
cam = cv2.VideoCapture(0)
initial_state = None


def in_excluded_region(contour, configs_path=os.path.join(os.getcwd(), 'config.json')):
    M = cv2.moments(contour)
    
    exclusion_contours = []
    with open(configs_path, 'r') as f:
        configs = json.load(f)
        for ex_contour in configs['exclusion_zones']:
            ctr = np.array(ex_contour).reshape((-1, 1, 2)).astype(np.int32)
            exclusion_contours.append(ctr)

    in_excluded_contour = False
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        for ex_cnt in exclusion_contours:
            result = cv2.pointPolygonTest(ex_cnt, (cx, cy), False)
            if result >= 0:
                in_excluded_contour = True
                logging.info(f"({cx}, {cy}) found in exclusion contours.")
                break
    return in_excluded_contour


def detect_motion(frame):
    global initial_state
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)

    if initial_state is None:
        initial_state = gray_frame
        return

    now = datetime.now() # current date and time
    date_time = now.strftime("%m%d%Y_%H%M%S.%f")[:-3]

    differ_frame = cv2.absdiff(initial_state, gray_frame)
    
    # the change between static or initial background and current gray frame are highlighted 
    thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # For the moving object in the frame finding the coutours 
    cont, _ = cv2.findContours(thresh_frame.copy(),
                               cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)
    num_moving_obj = 0
    for cur in cont:
        if cv2.contourArea(cur) < 10000:
            continue

        color = (255, 0, 0)
        if not in_excluded_region(cur):
            num_moving_obj += 1
            color = (0, 255, 0)

        (cur_x, cur_y, cur_w, cur_h) = cv2.boundingRect(cur)

        # To create a rectangle of green color around the moving object  
        cv2.rectangle(frame, (cur_x, cur_y), (cur_x + cur_w, cur_y + cur_h), color, 3)

    if num_moving_obj > 0:
        logging.info(f"Found {num_moving_obj} moving objects.")
        cv2.imwrite(f"{os.path.join(cache_dir, date_time)}.jpg", frame.astype('uint8'))


def start():
    global initial_state
    count = 0
    while(1):
        return_val, image = cam.read()
        if count == 10:
            initial_state = None
            count = 0
        detect_motion(image)
        time.sleep(0.3)
        count = count + 1
    cam.release()


if __name__ == '__main__':
    logger = logging.getLogger('camera_service')
    logger.info('Hello from cam.py main... starting')
    start()
    logger.info('cam process ended.')

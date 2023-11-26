import cv2
import os
import matplotlib.pyplot as plot


def show_webcam():
    vid = cv2.VideoCapture(0)
    while True:
        ret_val, img = vid.read()  # img feed taken frame by frame (passed over to yolo)
        # os.system('')
        if not ret_val:
            print("Could not read frame")
            break
        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_webcam()



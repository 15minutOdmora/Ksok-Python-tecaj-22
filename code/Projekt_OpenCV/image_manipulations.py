"""
Module for helper functions regarding images.
"""

import cv2
import numpy as np


def get_image(file_path):
    """
    Reads image and returns array of pixels.
    """
    return cv2.imread(file_path)


def get_grayscale_image(image):
    """
    Reads image and returns grayscale array of pixels.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def show_image(image, window_title="Title"):
    """
    Displayes image on window based on passed title.
    """
    cv2.imshow(window_title, image)


def await_key():
    """
    Waits for key input.
    """
    cv2.waitKey()


def quit():
    """
    Destroys all opened windows.
    """
    cv2.destroyAllWindows()


def save_image(image_path, image):
    """
    Saved image to passed path.
    """
    cv2.imwrite(image_path, image)


def camera_input():
    """
    Example of how to get computers camera frames.
    """
    video = cv2.VideoCapture(0)

    while True:

        _, frame = video.read() 

        show_image(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # save_image(RELATIVE_PATH + "jaz.png", frame)
            break

    video.release()
    quit()

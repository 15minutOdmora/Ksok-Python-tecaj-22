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


def resize_image(image, width, height):
    """
    Resizes image to specified width and height.
    """
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


def get_rgb_from_grayscale(image):
    """
    Converts grayscale image back to RGB.
    """
    return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)


def get_image_size(image):
    """
    Returns width and height of image
    """
    width = int(image.shape[1])
    height = int(image.shape[0])
    return width, height


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

        ret, frame = video.read() 

        if ret:

            show_image(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                # save_image(RELATIVE_PATH + "jaz.png", frame)
                break

    video.release()
    quit()

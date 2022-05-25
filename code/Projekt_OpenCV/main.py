"""
File for converting normal mp4 videos into squared-effect ones.
"""

import os
import sys

import cv2
import numpy as np

from image_manipulations import *
import console

# Set paths for videos (used when testing)
VIDEOS_FOLDER_PATH = "code/Projekt_OpenCV/videos"
SAMPLE_IMAGE_PATH = os.path.join(VIDEOS_FOLDER_PATH, "sample.png")
DANCING_VIDEO_PATH = os.path.join(VIDEOS_FOLDER_PATH, "SvenOtten_just_some_motion_Trim.mp4")


def get_appropriate_size(image, square_size):
    """
    Calculate closest (lower bound) image width and height so it can be divided by square_size.
    """
    width, height = get_image_size(image)  # Get size of image
    # Resize to appropriate size
    width -= width % square_size 
    height -= height % square_size
    return width, height


def create_image_with_squares(image, square_size=10):
    """
    Creates new image based average pixel values in square_size sized regions.
    If average value in region:
        255 -> Full square while color
        0 -> No square
        127 -> Square half of the size with 127 grayness
    """
    image = get_grayscale_image(image)  # Convert to grayscale
    width, height = get_appropriate_size(image, square_size)
    image = resize_image(image, width, height)

    processed_image = np.zeros([height, width], np.uint8)

    for i in range(0, height, square_size):
        for j in range(0, width, square_size):
            average_value = np.average(image[i:i+square_size, j:j+square_size])
            square_size_factored = int((average_value / 255) * square_size)
            processed_image[i:i+square_size_factored, j:j+square_size_factored] = int(average_value)

    return get_rgb_from_grayscale(processed_image)


def video(file_path, out_path, square_size=10):
    """
    Read original video and create squared video as output.
    Square size determins max size of each square.
    """
    # Get video object
    video = cv2.VideoCapture(file_path)
    # Get fps and frame count, calculate duration
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = round(frame_count / fps, 2)
    # Get filename and output conversion started
    filename = os.path.basename(file_path)
    print(f"Started converting video {filename} of duration {duration}s")
    # Read first frame to get size
    ret, frame = video.read()
    width, height = get_appropriate_size(frame, square_size)
    # Video writer to save each processed frame, file exstension must be .mp4
    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
    print(f"Video will be resized to {width} x {height}")
    # Set progress bar and initial count
    progress_bar = console.ProgressBar(total=frame_count - 1)
    count = 0
    # Main loop, iterate over videos frames
    while True:
        ret, frame = video.read()
        if ret == True:
            # Process frame here
            processed_frame = create_image_with_squares(frame, square_size)
            # Save to output
            out.write(processed_frame)
            # Update progress bar
            count += 1
            progress_bar.update(count)
            # Quit check, quits if q key pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Mark progress bar as completed
    progress_bar.complete()
    # Release everything
    video.release()
    out.release()
    quit()


def check_file_exists(file_path):
    """
    Checks if file exists.
    """
    return os.path.isfile(file_path)


def main():
    """
    Main function to run processing from console.

    When running from console there are three parameters separated by space:
        - video -> key-word "video", to know we will be processing a video (image processing can be added later)
        - file_path -> path to mp4 file to convert
        - out_path -> path to save file, must include mp4 exstension
    """
    args = sys.argv[1:]  # Get arguments from console
    
    if args[0] == "video":  # If first argument is video
        file_path = args[1]
        out_path = args[2]

        if check_file_exists(file_path):
            video(file_path, out_path, 10)  # Execute processing if file exists
        else:
            print(f"File {file_path} does not exist.")
    else:
        print("Invalid arguments.")


if __name__ == "__main__":
    main()

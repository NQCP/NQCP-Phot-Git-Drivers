import os
from time import time

import cv2 as cv

from vision import Vision
from windowcapture import WindowCapture

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
window_name = 'Live Window - CS165CU1'
window_capture = WindowCapture(window_name)

# load the trained model
classifier = cv.CascadeClassifier('cascade/cascade.xml')


# load an empty Vision class
vision = Vision(None)

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = window_capture.get_screenshot()

    # do object detection
    #rectangles = classifier.detectMultiScale(screenshot)

    # draw the detection results onto the original image
    #detection_image = vision.draw_rectangles(screenshot, rectangles)

    # display the images
    cv.imshow('Screen Capture', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.p
    # press 'f' to save screenshot as a positive image, press 'd' to 
    # save as a negative image.
    # waits 1 ms every loop to process key presses
    path = ('N:/SCI-NBI-NQCP/Phot/rawData/microwave_resonator'
            '/MWresonators_NQCP_ResOnly_NoCapacitor_18032024_A001004A02/Photos/TrainingData/Resonator/26042024/')
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('p'):
        cv.imwrite(path + 'positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('n'):
        cv.imwrite(path + 'negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')

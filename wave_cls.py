try:
    import shytlight
except:
    import shytlight_simulator as shytlight
import time
import cv2
import numpy as np
import threading

class WavePattern(threading.Thread):
    def __init__(self):
        super(WavePattern, self).__init__()

        self.stopping = False

        self.base_color = (0x44, 0x64, 0x55) # stromboli
        # self.base_color = (0x0, 0x0, 0x0)
        self.highlight_color = (0xfd, 0xd2, 0x62) # cream can
        self.bpm = 124.

    def stop(self):
        self.stopping = True

    def run(self):
        while not self.stopping:
            for i in range(10):
              for j in range(100):
                # create image on large basis
                circles = np.zeros((500,800, 3), np.uint8)
                circles[:,:]= np.flipud(base_color) # numpy ordering is reversed, BGR
                # draw a line
                cv2.line(circles, (j*10,0), (j*10,500), highlight_color, 80)
                # blur circle
                bl_circles = cv2.blur(circles, (301,301))
                # resize image to our real led size
                test_geometry = cv2.resize(bl_circles,(8,5))
                # add frame to buffer
                shytlight.add_frame(1, test_geometry)

 

class WavePatternFast(WavePattern):
    def __init__(self):
        super(WavePatternFast, self).__init__()
        self.bpm = 124.

class WavePatternSlow(WavePattern):
    def __init__(self):
        super(WavePatternSlow, self).__init__()
        self.bpm = 64.

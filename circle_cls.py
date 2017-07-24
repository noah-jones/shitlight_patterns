try:
    import shytlight
except:
    import shytlight_simulator as shytlight
import time
import cv2
import numpy as np
import threading
from palettable import wesanderson

class CirclePattern(threading.Thread):
    def __init__(self):
        super(CirclePattern, self).__init__()
        self.stopping = False
        self.color = (255, 0, 0)
        self.colors = wesanderson.Zissou_5.colors
        self.n_colors = len(self.colors)
        self.inv = False

    def stop(self):
        self.stopping = True

    def random_color(self):
        """Pick a color from the colormap at random."""
        current_color = self.colors[np.random.randint(self.n_colors)]
        while np.mean(current_color) < 64:
            current_color = self.colors[np.random.randint(self.n_colors)]
        return current_color



    def run(self):
        while (self.stopping == False):
            self.color = self.random_color()
            for j in range(70):
              if self.inv:
                 x = int(((69-j)/10.)**2)
              else:
                 x = int(((j)/10.)**2)
              # create image on large basis
              circles = np.zeros((50,80,3))
              # draw a circle with increasing radius
              cv2.circle(circles, (40,25),x, self.color, 8)
              # blur circle
              bl_circles = cv2.blur(circles, (21,21))
              # resize image to our real led size
              test_geometry = cv2.resize(bl_circles,(8,5))
              # add frame to buffer
              if not self.stopping:
                  shytlight.add_frame(1, test_geometry)



class CirclePatternInv(CirclePattern):
    def __init__(self):
        super(CirclePatternInv, self).__init__()
        self.inv = True

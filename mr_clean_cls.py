import threading

try:
    import shytlight
except:
    import shytlight_simulator as shytlight

import numpy as np
from palettable import wesanderson


class MrCleanPattern(threading.Thread):

    def __init__(self, n_rows=5, n_led=8, rep_rate=100):
        super(MrCleanPattern, self).__init__()

        self.stopping = False

        self.n_led = n_led
        self.n_rows = n_rows
        colors = wesanderson.Zissou_5.colors
        self.colors = colors
        self.n_colors = len(colors)
        self.rep_rate = rep_rate

    def mr_clean(self, current_color):
        
        is_active = np.zeros((self.n_rows, self.n_led), dtype=bool)
        for _ in range(self.n_rows):
            is_active[_, _ % 2::2] = True

        for _ in range(100):
            brightness = np.zeros((self.n_rows, self.n_led, 3))
            brightness[is_active] = current_color
            is_active = is_active == False
            for __ in range(self.rep_rate):
                shytlight.add_frame(rep=1, frame=brightness) 

            if self.stopping:
                return


    def random_color(self):
        """Pick a color from the colormap at random."""
        current_color = self.colors[np.random.randint(self.n_colors)]
        while np.mean(current_color) < 64:
            current_color = self.colors[np.random.randint(self.n_colors)]
        return current_color


    def run(self):
        while(self.stopping == False):
            current_color = self.random_color()
            self.mr_clean(current_color)

    def stop(self):
        self.stopping = True


class MrCleanFast(MrCleanPattern):

    def __init__(self, n_rows=5, n_led=8, rep_rate=50):
#        super(MrCleanPattern, self).__init__()
        super(MrCleanFast, self).__init__()

        self.stopping = False

        self.n_led = n_led
        self.n_rows = n_rows
        colors = wesanderson.Zissou_5.colors
        self.colors = colors
        self.n_colors = len(colors)
        self.rep_rate = rep_rate

class MrCleanSuperfast(MrCleanPattern):

    def __init__(self, n_rows=5, n_led=8, rep_rate=25):
#        super(MrCleanPattern, self).__init__()
        super(MrCleanSuperfast, self).__init__()

        self.stopping = False

        self.n_led = n_led
        self.n_rows = n_rows
        colors = wesanderson.Zissou_5.colors
        self.colors = colors
        self.n_colors = len(colors)
        self.rep_rate = rep_rate


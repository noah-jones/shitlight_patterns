

import time
import random
import threading


from cross_cls import CrossPattern
from unicolor_cls import UnicolorPattern
from raindrop_cls import RaindropPattern
from klapp_cls import KlappPatternSlow
from klapp_cls import KlappPatternFast
from mr_clean_cls import MrCleanPattern, MrCleanFast, MrCleanSuperfast
from wave_cls import WavePatternSlow, WavePatternFast
from propeller_cls import PropellerPattern, PropellerPatternSlow

from circle_cls import CirclePattern, CirclePatternInv

class RandomPattern(threading.Thread):

    def __init__(self):
        super(RandomPattern, self).__init__()
        self.patterns = [ CrossPattern, RaindropPattern ]
        self.stopping = False


    def stop(self):
        self.stopping = True



    def run(self):
        
        while not self.stopping:
            cls = random.choice(self.patterns)
            self.pattern = cls()
            
            self.pattern.start()
            for i in range(10*100):
                if not self.stopping:
                    time.sleep(0.01)
            self.pattern.stop()
            self.pattern.join()


class RandomSetLorenzFast(RandomPattern):
    def __init__(self):
        super(RandomSetLorenzFast, self).__init__()
        self.patterns = [ WavePatternFast, KlappPatternFast, PropellerPatternFast ]
        # self.patterns = [ WavePatternFast, KlappPatternFast ]


class RandomSetLorenzSlow(RandomPattern):
    def __init__(self):
        super(RandomSetLorenzSlow, self).__init__()
        self.patterns = [ WavePatternSlow, KlappPatternSlow, PropellerPatternSlow ]
        # self.patterns = [ WavePatternSlow, KlappPatternSlow ]


class RandomSetAll(RandomPattern):
    def __init__(self):
        super(RandomSetAll, self).__init__()
        self.patterns = [ WavePatternSlow, KlappPatternSlow,
                PropellerPatternSlow, CrossPattern, RaindropPattern,
                CirclePattern, CirclePatternInv ]
        # self.patterns = [ WavePatternSlow, KlappPatternSlow, CrossPattern, RaindropPattern ]

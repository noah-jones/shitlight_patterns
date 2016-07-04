

import time
import random
import threading


from cross_cls import CrossPattern
from unicolor_cls import UnicolorPattern
from raindrop_cls import RaindropPattern


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
            

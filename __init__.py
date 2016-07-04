

from cross_cls import CrossPattern
from shooting_star_cls import ShootingStarPattern
from unicolor_cls import UnicolorPattern
from raindrop_cls import RaindropPattern
from klapp_cls import KlappPatternSlow
from klapp_cls import KlappPatternFast
from mr_clean_cls import MrCleanPattern, MrCleanFast, MrCleanSuperfast
from wave_cls import WavePatternSlow, WavePatternFast
from propeller_cls import PropellerPattern, PropellerPatternSlow

patterns = [ ('Cross', CrossPattern),
             ('Shooting Star', ShootingStarPattern),
             ('Unicolor', UnicolorPattern),
             ('Raindrops', RaindropPattern),
             ('Propeller - Fast', PropellerPattern),
             ('Propeller - Slow', PropellerPatternSlow),
             ('Klapp - Fast',  KlappPatternFast),
             ('Klapp - Slow', KlappPatternSlow),
             ('Wave - Fast',  WavePatternFast),
             ('Wave - Slow', WavePatternSlow),
             ('MR. Clean classic', MrCleanPattern),
             ('MR. Clean on drugs', MrCleanFast),
             ('MR. Clean on speed', MrCleanSuperfast),
             ]



from cross_cls import CrossPattern

from shooting_star_cls import ShootingStarPattern

from unicolor_cls import UnicolorPattern
from raindrop_cls import RaindropPattern
from klapp_cls import KlappPatternSlow
from klapp_cls import KlappPatternFast
from mr_clean_cls import MrCleanPattern, MrCleanFast, MrCleanSuperfast
from wave_cls import WavePatternSlow, WavePatternFast

from circle_cls import CirclePattern, CirclePatternInv

from propeller_cls import PropellerPattern, PropellerPatternSlow   

from random_cls import RandomPattern, RandomSetLorenzFast, RandomSetLorenzSlow, RandomSetAll

from champagne_cls import ChampagnePattern

patterns = [ ('Cross', CrossPattern),
             ('Shooting Star', ShootingStarPattern),
             ('Unicolor', UnicolorPattern),
             ('Raindrops', RaindropPattern),
             ('Klapp - Fast',  KlappPatternFast),
             ('Klapp - Slow', KlappPatternSlow),
             ('Wave - Fast',  WavePatternFast),
             ('Wave - Slow', WavePatternSlow),
             ('Propeller - Fast', PropellerPattern),
             ('Propeller - Slow', PropellerPatternSlow),
             ('Circles', CirclePattern),
             ('Circles Inv', CirclePatternInv),
             ('MR. Clean classic', MrCleanPattern),
             ('MR. Clean on drugs', MrCleanFast),
             ('MR. Clean on speed', MrCleanSuperfast),
             ('Random Set Marc', RandomPattern),
             ('Random Set Lorenz Fast', RandomSetLorenzFast),
             ('Random Set Lorenz Slow', RandomSetLorenzSlow),
             ('Random Set All', RandomSetAll),
             ('Champagne', ChampagnePattern)
             ]

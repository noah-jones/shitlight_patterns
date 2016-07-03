

from cross_cls import CrossPattern

from shooting_star_cls import ShootingStarPattern

from unicolor_cls import UnicolorPattern

from raindrop_cls import RaindropPattern

from circle_cls import CirclePattern
from circle_cls import CirclePatternInv

from klapp_cls import KlappPatternFast
from klapp_cls import KlappPatternSlow


patterns = [ ('Cross', CrossPattern),
             ('Shooting Star', ShootingStarPattern),
             ('Unicolor', UnicolorPattern),
             ('Raindrop', RaindropPattern),
             ('Klapp (fast)', KlappPatternFast),
             ('Klapp (slow)', KlappPatternSlow),
             ('Circles (in2out)', CirclePattern),
             ('Circles (out2in)', CirclePatternInv) ]




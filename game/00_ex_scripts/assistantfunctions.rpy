init -999 python:


    def gMakePos( aXPos, aYPos ):
        return Transform( pos = ( aXPos, aYPos ) )

    def gSumPos( aPos1, aPos2 ):
        return Transform( pos = ( aPos1.xpos + aPos2.xpos, aPos1.ypos + aPos2.ypos ) )


    POS_410 = gMakePos( 410, 0 )
    POS_410h = gMakePos( 120, 0 )
    POS_370 = gMakePos( 370, 0 )
    POS_340l = gMakePos( 120, 0 )
    POS_340s = gMakePos( 110, 0 )
    POS_320 = gMakePos( 320, 0 )
    POS_320g = gMakePos( 110, -81 )
    POS_120 = gMakePos( 120, 0 )
    POS_140 = gMakePos( 140, 0 )
    POS_520f = gMakePos( 520, 114 )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
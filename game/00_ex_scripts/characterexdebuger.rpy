init -999 python:
    class CharacterExDebuger:
        
        @staticmethod
        def Log( aDebugMessage ):
            if 'debug' in globals():
                
                debug.SaveString( aDebugMessage, 0 )
            else:
                None
        
        @staticmethod
        def LogE( aDebugMessage ):
            if 'debug' in globals():
                
                debug.SaveString( 'ERROR: ' + aDebugMessage, 0 )
            else:
                None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
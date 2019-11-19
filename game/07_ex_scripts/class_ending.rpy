label Ending_constants:

    define const_ENDING_PUBLIC_WHORE = 2
    define const_ENDING_YOUR_WHORE = 1
    define const_ENDING_STRONG_GIRL = 3


    return

init -999 python:


    class Ending(store.object):
        
        def __init__( self ):
            self.Index = const_ENDING_YOUR_WHORE 
            self.Values = {const_ENDING_YOUR_WHORE : 1, const_ENDING_PUBLIC_WHORE : 0, const_ENDING_STRONG_GIRL : 0} 
        
        
        def SetEndingValue( self, iIndex, iValue ):
            self.Values[iIndex]=iValue
            self.Index = iIndex
            for key in self.Values:
                if self.Values[key] > self.Values[iIndex]:
                    self.Index = key
        
        
        def IncEndingValue( self, iIndex, iIncValue ):
            self.SetEndingValue( iIndex, self.Values[iIndex]+iIncValue )
        
        
        def IsEnding( self, iIndex ):
            if self.Index==iIndex:
                return True
            else:
                return False
        
        
        def GetEnding( self ):
            return self.Index
        
        
        def GetEndingValue( self, iIndex ):
            return self.Values[iIndex]
        
        
        
        def Congratulation ( self ):
            return tr("{size=+7}{color=#cbcbcb}Поздравляем с прохождением игры!{/color}{/size}\n\n{size=+5}{color=#cbcbcb}Это концовка \"0") +str(self.Index)+ tr("\" из \"0") +str(len(self.Values))+ "\".{/color}{/size}"
        
        
        
        def UpdatePersistent ( self ):
            if persistent.endings is None:
                persistent.endings = set()
            persistent.endings.update({self.Index});
        
        
        def IsPersistent ( self, iIndex ):
            return iIndex in persistent.endings
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
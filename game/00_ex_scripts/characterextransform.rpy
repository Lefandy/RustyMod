init -999 python:



    def gTrEx( aName, **kwargs ):
        dict = {}
        for key,val in kwargs.iteritems():
            dict[ key ] = val
        return CharacterExTransform( aName, dict )


    class CharacterExTransform(store.object):
        
        
        
        
        
        
        
        
        def __init__( self, aTransformName, aNamedParameters, aId = "" ):
            self.mId = aId   
            self.mName = aTransformName
            self.mParams = aNamedParameters 
            self._initVariables()
        
        
        @classmethod
        def create( cls, aDescription ):
            item = cls( aDescription.mName, aDescription.mParams, aDescription.mId )
            return item
        
        def apply( self, aImage ):
            
            result = aImage
            
            if self.mName == 'flip':
                result = im.Flip( aImage, self.mHor, self.mVer )
            
            return result
        
        def discard( self, aImage ):
            
            result = aImage
            
            if self.mName == 'flip':
                result = im.Flip( aImage, self.mHor, self.mVer )
            
            return result
        
        def _initVariables( self ):
            
            if self.mName == 'flip':
                self.mHor = False
                self.mVer = False
                param = 'horizontal'
                if param in self.mParams.keys():
                    self.mHor = wtxml_parseBool( self.mParams[ param ] ) 
                param = 'vertical'
                if param in self.mParams.keys():
                    self.mVer = wtxml_parseBool( self.mParams[ param ] ) 
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
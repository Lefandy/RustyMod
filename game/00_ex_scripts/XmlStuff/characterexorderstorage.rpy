init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExOrderStorage:
        
        def __init__( self ):
            self.mSynonyms = {}
            self.mDataPath = ""   
        
        
        def CLEAR( self ):
            self.mSynonyms.clear()
        
        
        def read( self, aOrderFilePath ):
            self.mDataPath = aOrderFilePath
            f = renpy.file( aOrderFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            
            for child in root:
                key = child.get('name')
                self.mSynonyms[ key ] = int( child.text )
        
        
        def get( self, aValue ):
            if aValue in self.mSynonyms.keys():
                return self.mSynonyms[ aValue ]
            else:
                return int( aValue )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExFolderStorage:
        
        def __init__( self ):
            self.mSynonyms = {}
            self.mDataPath = ""   
        
        
        def CLEAR( self ):
            self.mSynonyms.clear()
        
        
        def read( self, aFolderFilePath ):
            self.mDataPath = aFolderFilePath
            f = renpy.file( aFolderFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            
            for child in root:
                key = child.get('name')
                path = child.text
                if not path.endswith( '/' ):
                    path += '/'
                self.mSynonyms[ key ] = path
        
        
        def get( self, aValue ):
            if aValue in self.mSynonyms.keys():
                return self.mSynonyms[ aValue ]
            else:
                return aValue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
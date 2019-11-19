init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExSetInfo:
        def __init__( self, aItemsList, aItemBase ):
            self.mNames = aItemsList
            self.mKeys = []
            self._createInfo( aItemBase )
        
        def _createInfo( self, aItemBase ):
            for item in self.mNames:
                desc = aItemBase.get( item )
                if desc != None:
                    self.mKeys.append( desc.mKey )
                else:
                    self.mKeys.append( None )

    class CharacterExSetStorage:
        
        def __init__( self ):
            self.mSets = {}  
            self.mSetInfos = {}  
            self.mDataPath = ""   
        
        
        def CLEAR( self ):
            self.mSets.clear()
            self.mSetInfos.clear()
        
        
        def read( self, aStartPath, aItemBase ):
            self.mDataPath = aStartPath
            fileList = renpy.list_files()
            for item in fileList:
                if item.endswith( '.hxml' ):
                    if item.startswith( aStartPath ):
                        
                        self._readFile( item, aItemBase )
        
        def _readFile( self, aFilePath, aItemBase ):
            f = renpy.file( aFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            for item in root:
                if item.tag == 'set':
                    setKey = item.get( 'name' )
                    if not setKey:
                        setKey = wtxml_getFileNameFromPath( aFilePath )  
                    setItems = []
                    for setIt in item:
                        setItems.append( setIt.text )
                    self.mSetInfos[ setKey ] = CharacterExSetInfo( setItems, aItemBase )
                    self.mSets[ setKey ] = setItems
        
        
        
        def get( self, aSetName ):
            if aSetName[0] == '*':
                aSetName = aSetName[1:]
            if aSetName in self.mSets.keys():
                return self.mSets[ aSetName ]
            else:
                
                CharacterExDebuger.LogE( 'CharacterExSetStorage::get: cant find set with aSetName = ' + aSetName )
                return None
        
        
        def getInfo( self, aSetName ):
            if aSetName[0] == '*':
                aSetName = aSetName[1:]
            if aSetName in self.mSetInfos.keys():
                return self.mSetInfos[ aSetName ]
            else:
                
                CharacterExDebuger.LogE( 'CharacterExSetStorage::get: cant find info for aSetName = ' + aSetName )
                return None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
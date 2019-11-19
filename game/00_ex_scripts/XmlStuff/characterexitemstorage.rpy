init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExItemStorage:
        
        def __init__( self ):
            self.mItems = {} 
            self.mDataPath = ""   
        
        
        def CLEAR( self ):
            self.mItems.clear()
        
        
        def read( self, aStartPath, aFolderBase, aZOrderBase ):
            self.mDataPath = aStartPath
            fileList = renpy.list_files()
            for item in fileList:
                if item.endswith( '.hxml' ):
                    if item.startswith( aStartPath ):
                        
                        self._readFile( item, aFolderBase, aZOrderBase )
        
        def _readFile( self, aFilePath, aFolderBase, aZOrderBase ):
            f = renpy.file( aFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            itemDesc = CharacterExDescriptionItem( root, aFolderBase, aZOrderBase )
            if not itemDesc.mName:
                itemDesc.mName = wtxml_getFileNameFromPath( aFilePath )  
            self.mItems[ itemDesc.mName ] = itemDesc
        
        
        
        def get( self, aItemName ):
            if aItemName in self.mItems.keys():
                return self.mItems[ aItemName ]
            else:
                
                CharacterExDebuger.LogE( 'CharacterExItemStorage::get: cant find item with aItemName = ' + aItemName )
                return None
        
        
        
        def getItemStyle( self, aItemName, aStyleName ):
            if aItemName in self.mItems.keys():
                item = self.mItems[ aItemName ]
                if aStyleName in item.mStyles.keys():
                    return item.mStyles[ aStyleName ]
                else:
                    
                    CharacterExDebuger.LogE( 'CharacterExItemStorage::getItemStyle: cant find item with aItemName = ' + aItemName
                        + ', aStyleName = ' + aStyleName )
                    return None
            else:
                
                CharacterExDebuger.LogE( 'CharacterExItemStorage::getItemStyle: cant find item with aItemName = ' + aItemName
                    + ', aStyleName = ' + aStyleName )
                return None
        
        
        def getItemKey( self, aItemName ):
            if aItemName in self.mItems.keys():
                item = self.mItems[ aItemName ]
                return item.mKey
            else:
                
                CharacterExDebuger.LogE( 'CharacterExItemStorage::getItemKey: cant find key for aItemName = ' + aItemName )
                return ""
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
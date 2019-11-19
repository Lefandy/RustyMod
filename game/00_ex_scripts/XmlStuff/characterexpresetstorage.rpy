init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExPresetStorage:
        
        def __init__( self ):
            self.mPresets = {}  
            self.mDataPath = ""   
        
        
        def CLEAR( self ):
            self.mPresets.clear()
        
        
        def read( self, aStartPath ):
            self.mDataPath = aStartPath
            fileList = renpy.list_files()
            for item in fileList:
                if item.endswith( '.hxml' ):
                    if item.startswith( aStartPath ):
                        
                        self._readFile( item )
        
        def _readFile( self, aFilePath ):
            f = renpy.file( aFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            for item in root:
                if item.tag == 'preset':
                    presetName = item.get( 'name' )
                    if not presetName:
                        presetName = wtxml_getFileNameFromPath( aFilePath )  
                    preset = CharacterExPreset()
                    preset.read( item )
                    self.mPresets[ presetName ] = preset
        
        
        def get( self, aPresetName ):
            if aPresetName in self.mPresets.keys():
                return self.mPresets[ aPresetName ]
            else:
                
                CharacterExDebuger.LogE( 'CharacterExPresetStorage::get: cant find preset with aPresetName = ' + aPresetName )
                return None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
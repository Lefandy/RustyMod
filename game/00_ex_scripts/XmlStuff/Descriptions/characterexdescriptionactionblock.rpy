init -999 python:
    import xml.etree.ElementTree as ET
    import re


    class CharacterExDescriptionActionBlock(store.object):
        
        def __init__( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mConditions = []   
            self._read( aElementRoot, aFolderBase, aOrderBase )
        
        
        def _read( self, aElementRoot, aFolderBase, aOrderBase ):
            for child in aElementRoot:
                if child.tag == 'condition':
                    newCond = CharacterExDescriptionActionCondition( child, aFolderBase, aOrderBase )
                    self.mConditions.append( newCond )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
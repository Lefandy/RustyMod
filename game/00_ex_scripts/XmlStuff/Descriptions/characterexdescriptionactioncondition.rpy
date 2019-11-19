init -999 python:
    import xml.etree.ElementTree as ET
    import re


    class CharacterExDescriptionActionCondition(store.object):
        
        def __init__( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mType = ""
            self.mParams = {}   
            
            
            
            
            
            
            
            
            self._read( aElementRoot, aFolderBase, aOrderBase )
        
        
        def _read( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mType = aElementRoot.get('type', 'hasItem')
            compPossible = [ 'e', 'ne', 'ge', 'le', 'g', 'l' ]
            for param in aElementRoot:
                compareMeth = param.get('comp', 'e')
                if compareMeth not in compPossible:
                    compareMeth = 'e'
                
                val = param.text
                if param.tag == 'folder':
                    val = aFolderBase.get( val )
                elif param.tag == 'zorder':
                    val = wtxml_readZOrder( val, aOrderBase )   
                self.mParams[ param.tag ] = ( val, compareMeth )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
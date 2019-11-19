init -999 python:
    import xml.etree.ElementTree as ET
    import re


    class CharacterExDescriptionAction(store.object):
        
        def __init__( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mEvent = ""    
            self.mBlocks = []   
            self.mResults = []  
            self.mBadResults = []   
            self._read( aElementRoot, aFolderBase, aOrderBase )
        
        
        def _read( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mEvent = aElementRoot.get('event')
            for child in aElementRoot:
                if child.tag == 'body':
                    for block in child:
                        self.mBlocks.append( CharacterExDescriptionActionBlock( block, aFolderBase, aOrderBase ) )
                if child.tag == 'result':
                    self.mResults.append( CharacterExDescriptionActionResultFactory.create( child, aFolderBase, aOrderBase ) )
                if child.tag == 'badresult':
                    self.mBadResults.append( CharacterExDescriptionActionResultFactory.create( child, aFolderBase, aOrderBase ) )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
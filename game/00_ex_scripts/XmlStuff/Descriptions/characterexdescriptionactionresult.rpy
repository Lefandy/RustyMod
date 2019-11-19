init -999 python:
    import xml.etree.ElementTree as ET
    import re




    class CharacterExDescriptionActionResultFactory:
        @staticmethod
        def create( aElementRoot, aFolderBase, aOrderBase ):
            resObj = None
            resType = aElementRoot.get( 'type' )
            basicTypes = [ 'addItem', 'removeItem', 'showItem', 'hideItem', 'setStyle' ]
            if resType in basicTypes:
                resObj = CharacterExDescriptionActionResultBasic()
            elif resType == 'setParams':
                resObj = CharacterExDescriptionActionResultSetParams()
            if resObj != None:
                resObj.read( aElementRoot, aFolderBase, aOrderBase )
            return resObj


    class CharacterExDescriptionActionResultBase(store.object):
        def __init__( self ):
            self.mType = ""     
        
        def read( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mType = aElementRoot.get('type')



    class CharacterExDescriptionActionResultBasic( CharacterExDescriptionActionResultBase ):
        
        def __init__( self ):
            super( CharacterExDescriptionActionResultBasic, self ).__init__()
            self.mKeys = []   
            self.mNames = []   
            self.mSets = []    
            self.mItems = []   
        
        
        def read( self, aElementRoot, aFolderBase, aOrderBase ):
            super( CharacterExDescriptionActionResultBasic, self ).read( aElementRoot, aFolderBase, aOrderBase )
            for child in aElementRoot:
                if child.tag == 'key':
                    if child.text:
                        for key in child.text.split(','):
                            self.mKeys.append( key )
                elif child.tag == 'name':
                    if child.text:
                        for name in child.text.split(','):
                            self.mNames.append( name )
                elif child.tag == 'set':
                    if child.text:
                        for name in child.text.split(','):
                            self.mSets.append( name )
                elif child.tag == 'item':
                    if child.text:
                        for name in child.text.split(','):
                            self.mItems.append( name )



    class CharacterExDescriptionActionResultSetParams( CharacterExDescriptionActionResultBase ):
        
        def __init__( self ):
            super( CharacterExDescriptionActionResultSetParams, self ).__init__()
            
            
            
            
            self.mTarget = ""
            
            
            
            
            
            
            
            self.mParams = {}
            
            
            
            self.mConditionBlock = None
        
        
        def read( self, aElementRoot, aFolderBase, aOrderBase ):
            super( CharacterExDescriptionActionResultSetParams, self ).read( aElementRoot, aFolderBase, aOrderBase )
            self.mTarget = aElementRoot.get('target', 'self')
            if self.mTarget not in [ 'self', 'custom' ]:
                self.mTarget = 'self'
            
            operPossible = [ 'set', 'inc', 'dec' ]
            for child in aElementRoot:
                if child.tag == 'filter':
                    
                    self.mConditionBlock = CharacterExDescriptionActionBlock( child, aFolderBase, aOrderBase )
                else:
                    
                    param = child
                    operMeth = param.get('oper', 'set')
                    if operMeth not in operPossible:
                        operMeth = 'set'
                    
                    valueCap = param.get('cap')
                    
                    val = param.text
                    if param.tag == 'folder':
                        val = aFolderBase.get( val )
                    elif param.tag == 'zorder':
                        val = wtxml_readZOrder( val, aOrderBase )   
                        valueCap = wtxml_readZOrder( valueCap, aOrderBase ) 
                    self.mParams[ param.tag ] = ( val, operMeth, valueCap )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
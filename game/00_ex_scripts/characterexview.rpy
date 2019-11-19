screen CharacterExViewScreen(aData, aPos):
    python:
        data = aData.values()
        data.sort( key = lambda item: item.zorder )


    for element in data:
        if element.mIsVisible == True:
            add element.getImage() at gSumPos( aPos, element.position )



    zorder _CharacterExViewScreenZOrder

init -999 python:
    _CharacterExViewScreenZOrder = 0

init -998 python:
    from copy import deepcopy 
    class CharacterExView(store.object):
        
        def __init__( self, zOrder, aCharacter, aUniqName = 'default' ):
            self.mCh = aCharacter
            self.mUniqName = aUniqName
            
            
            
            
            
            
            
            
            
            self.mZOrderScreen = zOrder
            self.mTagScreen = self.__class__.__name__ + '_' + self.mUniqName;
            
            
            self.mTagsStack = []
            
            
            self.mData = None
        
        
        
        def __call__( self, what, interact = True ):
            return self.mCh( what, interact = interact )
        
        
        def predict( self, what ):
            return self.mCh.predict( what )
        
        
        
        
        
        def attach( self, aData ):
            self.mData = aData
            aData.attachedToView( self )
        
        def detach( self ):
            self.mData = None
            aData.detachedFromView( self )
        
        def data( self ):
            return self.mData
        
        
        
        
        
        
        def setZOrder( self, zOrder ):
            self.mZOrderScreen = zOrder
        
        def getZOrder( self ):
            return self.mZOrderScreen
        
        
        
        
        
        def pushScreenTag( self, aNewScreenTag ):
            self.mTagsStack.append( self.mTagScreen )
            self.mTagScreen = aNewScreenTag
        
        def popScreenTag( self ):
            if self.mTagsStack:
                self.mTagScreen = self.mTagsStack.pop()
        
        
        
        
        
        
        
        
        def showQ( self, aFace, aPos, aTransition = None, aPresetActualsList = None ):
            if aFace is not None:
                
                CharacterExDebuger.Log( 'CharacterExView::showQ: aFace = ' + aFace )
                
                if aFace.startswith('#'):
                    
                    aFace = aFace[1:]
                    self.mData.updateItemFrameKey( 'face', aFace )
                else:
                    
                    if '.' not in aFace:
                        
                        self.mData.applyPreset( aFace, aPresetActualsList )
                    else:
                        
                        self.mData.updateItemFrameKey( 'face', aFace )
            
            
            self._showView( self.mData.mItems, aPos )
            if aTransition is not None:
                renpy.with_statement( aTransition, None, True )
        
        
        def hideQ( self, aTransition = None ):
            self._hideView()
            if aTransition is not None:
                renpy.with_statement( aTransition )
        
        
        def showQQ( self, aFace, aPos, aPresetActualsList = None ):
            self.showQ( aFace, aPos, d3, aPresetActualsList )
        
        def hideQQ( self ):
            self.hideQ( d3 )
        
        def hideshowQQ( self, aFace, aPos ):
            self.hideQQ( )
            self.showQ( aFace, aPos )
        
        
        
        
        
        
        
        def addFaceName( self, aFace ):
            self.mData.updateItemFrameKey( 'face', aFace )
        
        
        
        
        
        def _showView( self, aData, aPos ):
            
            
            
            oldOrder = store._CharacterExViewScreenZOrder
            store._CharacterExViewScreenZOrder = self.mZOrderScreen
            renpy.show_screen( "CharacterExViewScreen", aData, aPos, _tag = self.mTagScreen )
        
        def _hideView( self ):
            renpy.hide_screen( self.mTagScreen )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
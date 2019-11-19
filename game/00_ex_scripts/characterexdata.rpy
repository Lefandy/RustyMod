init -998 python:
    _m1_CharacterExData__EData_Add = 0
    _m1_CharacterExData__EData_Remove = 1
    _m1_CharacterExData__EData_Show = 2
    _m1_CharacterExData__EData_Hide = 3
    _m1_CharacterExData__EData_Style = 4

    import re
    from copy import deepcopy

    class CharacterExData(store.object):
        
        def __init__( self, aLinkerKey ):
            self.mLinkerKey = aLinkerKey    
            
            self.mItems = {}
            
            self.mTransforms = {}
            
            self.mSavedItems = {}
            self.mSavedTransforms = {}
            
            self.mViews = []
        
        
        
        
        
        
        
        def getView( self, aIndex = 0 ):
            if aIndex < len( self.mViews ):
                return self.mViews[ aIndex ]
            else:
                return None
        
        def attachedToView( self, aView ):
            self.mViews.append( aView )
        
        def detachedFromView( self, aView ):
            if aView in self.mViews:
                self.mViews.remove( aView )
        
        
        
        
        
        def addTransform( self, aTransform, aKey = 'default' ):
            self.delTransform( aKey )
            
            for val in self.mItems.values():
                val.addTransform( aKey, aTransform )
            self.mTransforms[ aKey ] = aTransform
        
        def delTransform( self, aKey = 'default' ):
            
            if aKey in self.mTransforms.keys():
                del self.mTransforms[ aKey ]
                for val in self.mItems.values():
                    val.delTransform( aKey )
        
        
        def clearTransforms( self ):
            keys = self.mTransforms.keys()
            for key in keys:
                self.delTransform( key )
            self.mTransforms.clear()
        
        
        
        
        
        
        def getItemKey( self, aKey ):
            if aKey in self.mItems.keys():
                return self.mItems[ aKey ]
            else:
                return None
        
        
        def getItem( self, aItemName ):
            key = self._getItemKeyByName( aItemName )
            if key in self.mItems.keys():
                item = self.mItems[ key ]
                if item.mName == aItemName:
                    return item
            return None
        
        
        
        def addItemDirect( self, aKey, aCharacterExItem ):
            
            CharacterExDebuger.Log( 'CharacterExData::addItemDirect: aKey = ' + aKey )
            if not aCharacterExItem:
                CharacterExDebuger.LogE( 'CharacterExData::addItemDirect: aCharacterExItem = None' )
            self._addItem( aKey, aCharacterExItem )
        
        
        def addItemKey( self, aKey, aName, aStyle = 'default' ):
            
            CharacterExDebuger.Log( 'CharacterExData::addItemKey: aKey = ' + aKey + ', aName = ' + aName + ', aStyle = ' + aStyle )
            newItem = WTXmlLinker.c( self.mLinkerKey ).create( aName, aStyle )
            if newItem[0] != None:
                self.addItemDirect( aKey, newItem[0] )
        
        
        def addItem( self, aName, aStyle = 'default' ):
            
            CharacterExDebuger.Log( 'CharacterExData::addItem: aName = ' + aName + ', aStyle = ' + aStyle )            
            newItem = WTXmlLinker.c( self.mLinkerKey ).create( aName, aStyle )
            if newItem[0] != None:
                self.addItemDirect( newItem[0].mKey, newItem[0] )
        
        def addItemSet( self, aSetName, aStyle = 'default' ):
            
            CharacterExDebuger.Log( 'CharacterExData::addItemSet: aSetName = ' + aSetName + ', aStyle = ' + aStyle )
            self._applyToSet( aSetName, _m1_CharacterExData__EData_Add, aStyle )
        
        
        
        def delItemKey( self, aKey ):
            self._delItem( aKey )
        
        
        def delItem( self, aItemName ):
            key = self._getItemKeyByName( aItemName )
            self._delItem( key, aItemName )
        
        def delItemSet( self, aSetName ):
            self._applyToSet( aSetName, _m1_CharacterExData__EData_Remove )
        
        
        
        def showItemKey( self, aKey, aSource = 'game' ):
            self._showItem( aKey, aSource )
        
        
        def showItem( self, aItemName, aSource = 'game' ):
            key = self._getItemKeyByName( aItemName )
            self._showItem( key, aSource, aItemName )
        
        
        def showItemSet( self, aSetName, aSource = 'game' ):
            self._applyToSet( aSetName, _m1_CharacterExData__EData_Show, aSource )
        
        
        
        def hideItemKey( self, aKey, aSource = 'game' ):
            self._hideItem( aKey, aSource )
        
        def hideItem( self, aItemName, aSource = 'game' ):
            key = self._getItemKeyByName( aItemName )
            self._hideItem( key, aSource, aItemName )
        
        
        def hideItemSet( self, aSetName, aSource = 'game' ):
            self._applyToSet( aSetName, _m1_CharacterExData__EData_Hide, aSource )
        
        
        
        def setStyleAll( self, aStyleName ):
            for item in self.mItems.values():
                item.setStyle( aStyleName )
        
        
        def setStyleKey( self, aKey, aStyleName ):
            self._setStyle( aKey, aStyleName )
        
        
        def setStyleItem( self, aItemName, aStyleName ):
            key = self._getItemKeyByName( aItemName )
            self._setStyle( key, aStyleName, aItemName )
        
        
        def setStyleSet( self, aSetName, aStyleName ):
            self._applyToSet( aSetName, _m1_CharacterExData__EData_Style, aStyleName )
        
        
        
        def checkItemKeyName( self, aKey, aName ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                if item.mName == aName:
                    return True
            return False
        
        
        def checkItemKeyStyle( self, aKey, aStyleName ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                if item.getStyle() == aStyleName:
                    return True
            return False
        
        
        def checkItemNameStyle( self, aItemName, aStyleName ):
            key = self._getItemKeyByName( aItemName )
            return self.checkItemKeyStyle( key, aStyleName )
        
        
        
        
        def updateItemFrameKey( self, aKey, aNewFrameName, aNewFrameFolder = None ):
            if aKey in self.mItems.keys(): 
                item = self.mItems[ aKey ]
                frameFolder = aNewFrameFolder
                if frameFolder == None:
                    frameFolder = item.mFileFolder
                item.changeImage( frameFolder, aNewFrameName, True )
        
        
        def updateItemFrameName( self, aItemName, aNewFrameName, aNewFrameFolder = None ):
            key = self._getItemKeyByName( aItemName )
            self.updateItemFrameKey( key, aNewFrameName, aNewFrameFolder )
        
        
        
        def applyPreset( self, aPresetName, aActualTemplateParams = None ):
            preset = WTXmlLinker.p( self.mLinkerKey ).get( aPresetName )
            if preset:
                actualsArray = aActualTemplateParams
                
                if isinstance( aActualTemplateParams, basestring ):
                    actualsArray = re.split( ',|\.| ', aActualTemplateParams )
                presetItems = preset.getItems( actualsArray )
                for item in presetItems:
                    self._applyPresetItem( item )
        
        
        
        def clear( self ):
            self.mItems.clear()
        
        
        def getAllItems( self ):
            return self.mItems
        
        
        
        
        
        
        def saveState( self ):
            self.mSavedItems = {}
            for key in self.mItems.keys():
                self.mSavedItems[ key ] = CharacterExItem.fromItem( self.mItems[ key ] )
            self.mSavedTransforms = {}
            for key in self.mTransforms.keys():
                self.mSavedTransforms[ key ] = deepcopy( self.mTransforms[ key ] )
        
        
        def loadState( self ):
            self.mItems.clear()
            for key in self.mSavedItems.keys():
                self.mItems[ key ] = CharacterExItem.fromItem( self.mSavedItems[ key ] )
            self.mTransforms.clear()
            for key in self.mSavedTransforms.keys():
                self.mTransforms[ key ] = deepcopy( self.mSavedTransforms[ key ] )              
        
        
        def clearState( self ):
            self.mSavedItems = {}
            self.mSavedTransforms = {}
        
        
        def copyState( self, aCharacterEx ):
            self.mItems.clear()
            for key in aCharacterEx.mItems.keys():
                self.mItems[ key ] = deepcopy( aCharacterEx.mItems[ key ] )
            self.mTransforms.clear()
            for key in aCharacterEx.mTransforms.keys():
                self.mTransforms[ key ] = deepcopy( aCharacterEx.mTransforms[ key ] )                
        
        
        
        
        
        def addLegs( self, aData ):
            self._addItem( 'legs', aData )
        def delLegs( self ):
            self._delItem( 'legs' )
        
        def addHands( self, aData ):
            self._addItem( 'hands', aData )
        def delHands( self ):
            self._delItem( 'hands' )
        
        def addPanties( self, aData ):
            self._addItem( 'panties', aData )
        def delPanties( self ):
            self._delItem( 'panties' )
        
        def addSkirt( self, aData ):
            self._addItem( 'skirt', aData )
        def delSkirt( self ):
            self._delItem( 'skirt' )
        
        def addBody( self, aData ):
            self._addItem( 'body', aData )
        def delBody( self ):
            self._delItem( 'body' )
        
        def addDress( self, aData ):
            self._addItem( 'dress', aData )
        def delDress( self ):
            self._delItem( 'dress' )
        
        def addTits( self, aData ):
            self._addItem( 'tits', aData )
        def delTits( self ):
            self._delItem( 'tits' )
        
        def addPose( self, aData ):
            self._addItem( 'pose', aData )
        def delPose( self ):
            self._delItem( 'pose' )
        
        def addFace( self, aData ):
            self._addItem( 'face', aData )
        def delFace( self ):
            self._delItem( 'face' )
        
        
        def updateItemSpecial( self, aItem ):
            self._addItem( aItem.mKey, aItem, False )
        
        
        
        
        
        def _addItem( self, aKey, aData, aIsDeletePrevious = True ):
            if aIsDeletePrevious:
                self._delItem( aKey )
            self.mItems[ aKey ] = aData
            aData.onSelfAdded( aKey, self.mItems, self )
            
            if not aData.getIsSubitem():
                for item in self.mItems.values():
                    if item != aData:
                        item.onItemAdded( aData )
            
            for key,val in self.mTransforms.iteritems():
                aData.addTransform( key, val )
        
        def _delItem( self, aKey, aItemName = None ):
            if aKey in self.mItems.keys():
                data = self.mItems[ aKey ]
                
                if aItemName != None:
                    if data.mName != aItemName:
                        return
                
                if not data.getIsSubitem():
                    for item in self.mItems.values():
                        if item != data:
                            item.onItemRemoved( data )
                
                del self.mItems[ aKey ]
                data.onSelfRemoved( self.mItems, self )
        
        def _showItem( self, aKey, aSource, aItemName = None ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                
                if aItemName != None:
                    if item.mName != aItemName:
                        return
                item.show( aSource )
        
        def _hideItem( self, aKey, aSource, aItemName = None ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                
                if aItemName != None:
                    if item.mName != aItemName:
                        return
                item.hide( aSource )
        
        def _setStyle( self, aKey, aStyleName, aItemName = None ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                
                if aItemName != None:
                    if item.mName != aItemName:
                        return
                item.setStyle( aStyleName )
        
        
        def _onItemHidden( self, aItem ):
            for item in self.mItems.values():
                item.onItemHidden( aItem )
        
        def _onItemShown( self, aItem ):
            for item in self.mItems.values():
                item.onItemShown( aItem )
        
        def _onItemStyleBeforeChange( self, aItem ):
            for item in self.mItems.values():
                item.onItemStyleBeforeChange( aItem )
        
        def _onItemStyleAfterChange( self, aItem ):
            for item in self.mItems.values():
                item.onItemStyleAfterChange( aItem )
        
        
        
        
        
        
        
        def _applyToSet( self, aSetName, aWhatToDo, aStringParam = None ):
            if aSetName[0] != '*':
                aSetName = '*' + aSetName
            setDesc = WTXmlLinker.c( self.mLinkerKey ).mSetBase.getInfo( aSetName )
            if setDesc == None:
                return
            if aWhatToDo == _m1_CharacterExData__EData_Add:
                setItems = WTXmlLinker.c( self.mLinkerKey ).create( aSetName, aStringParam )
                for item in setItems:
                    if item != None:
                        self.addItemDirect( item.mKey, item )
            elif aWhatToDo == _m1_CharacterExData__EData_Remove:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        self.delItem( name )
            elif aWhatToDo == _m1_CharacterExData__EData_Show:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        self.showItem( name, aStringParam )
            elif aWhatToDo == _m1_CharacterExData__EData_Hide:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        self.hideItem( name, aStringParam )
            elif aWhatToDo == _m1_CharacterExData__EData_Style:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        self.setStyleItem( name, aStringParam )
        
        
        
        def _getItemKeyByName( self, aItemName ):
            return WTXmlLinker.i( self.mLinkerKey ).getItemKey( aItemName )
        
        
        
        def _applyPresetItem( self, aPresetItem ):
            key = None
            if aPresetItem.mKey != None:
                key = aPresetItem.mKey
            elif aPresetItem.mName != None:
                key = self._getItemKeyByName( aPresetItem.mName )
            
            if key != None:
                if key in self.mItems.keys():
                    item = self.mItems[ key ]
                    
                    if aPresetItem.mFrame != None:
                        self.updateItemFrameKey( key, aPresetItem.mFrame )
                    elif aPresetItem.mStyle != None:
                        self.setStyleKey( key, aPresetItem.mStyle )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
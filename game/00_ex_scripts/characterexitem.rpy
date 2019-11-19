label main_ex_CharacterExItem_constants:




    define G_Z_UNDERLEGS = 0
    define G_Z_LEGS = 20
    define G_Z_PANTIES = 40
    define G_Z_SKIRT = 60
    define G_Z_HANDS = 80
    define G_Z_BODY = 100
    define G_Z_TITS = 120
    define G_Z_DRESS = 140
    define G_Z_FACE = 300


    define G_Z_HEADWEAR = 160
    define G_Z_POSE = 180


    define G_N_SKIRT = 'skirt'
    define G_N_BADGE = 'badge'
    define G_N_NETS = 'nets'

    return

init -998 python:
    from copy import deepcopy 

    class CharacterExItem(store.object):
        
        _indSelfAdded = CharacterExItemAction._indSelfAdded
        _indSelfRemoved = CharacterExItemAction._indSelfRemoved
        _indItemAdded = CharacterExItemAction._indItemAdded
        _indItemRemoved = CharacterExItemAction._indItemRemoved
        _indItemShown = CharacterExItemAction._indItemShown
        _indItemHidden = CharacterExItemAction._indItemHidden
        _indStyleBeforeChange = CharacterExItemAction._indStyleBeforeChange
        _indStyleAfterChange = CharacterExItemAction._indStyleAfterChange
        _indItemCount = CharacterExItemAction._indItemCount
        
        
        def __init__( self ):
            
            
            
            
            self.mIsSubitem = False
            self.mSubitems = [] 
            self.mSubitemsStyle = [] 
            
            self.mKey = ""
            self.mName = ""
            self.mIsVisible = True
            self.mFileName = ""
            self.mFileFolder = ""
            self.mStyles = []   
            self.mActiveStyle = None  
            self.mOwner = None 
            self.mXmlLinkerKey = "" 
            
            
            self.image = None
            self.zorder = 0
            self.position = Transform( pos = ( 0, 0 ) )            
            
            self.parent = None
            
            self.parentStyles = []
            
            
            self.mHideList = []
            
            
            
            self.mActions = []
            for num in range( CharacterExItem._indItemCount ):
                self.mActions.append( [] )
            
            
            self.mTransforms = {}
            
            
            self.mOwnerTransforms = {}
            
            
            
            self.mDirectors = set()
            
            
            self._x_x_x_screen_pos = None
        
        
        @classmethod
        def createOld( cls, aFolder, aName, aOrder, aParent = None, aPos = None ):
            item = cls()
            
            item.mFileName = aName
            item.mFileFolder = aFolder
            item.image = aFolder + aName
            item.zorder = aOrder
            item.position = Transform( pos = ( 0, 0 ) ) 
            if aPos is not None:
                item.position = aPos
            
            item.parent = aParent
            
            item.mActiveStyle = 'default'
            
            
            item._fillHideList()
            return item
        
        
        @classmethod
        def fromItem( cls, aItem ):
            item = cls()
            item.mKey = aItem.mKey
            item.mName = aItem.mName
            item.mIsVisible = aItem.mIsVisible
            item.mFileName = aItem.mFileName
            item.mFileFolder = aItem.mFileFolder
            item.mStyles = list( aItem.mStyles )
            item.mActiveStyle = aItem.mActiveStyle
            item.mOwner = aItem.mOwner
            item.mXmlLinkerKey = aItem.mXmlLinkerKey
            
            item.mIsSubitem = aItem.mIsSubitem
            item.mSubitems = list( aItem.mSubitems )
            
            item.mSubitemsStyle = list( aItem.mSubitemsStyle )
            
            
            item.zorder = aItem.zorder
            item.position = Transform( pos = ( aItem.position.xpos, aItem.position.ypos ) )
            item.image = aItem.image
            
            item.parent = aItem.parent
            item.parentStyles = list( aItem.parentStyles )
            
            
            item.mHideList = list( aItem.mHideList )
            
            
            
            item.mActions = deepcopy( aItem.mActions )
            
            
            item.mTransforms = deepcopy( item.mTransforms )
            
            
            item.mOwnerTransforms = deepcopy( aItem.mOwnerTransforms )
            
            
            
            item.mDirectors = set( aItem.mDirectors )
            return item
        
        
        @classmethod
        def fromDesc( cls, aDescription, aXmlLinkerKey ):
            item = cls()
            
            item.mXmlLinkerKey = aXmlLinkerKey
            item.mKey = aDescription.mKey
            item.mName = aDescription.mName
            item.mStyles = aDescription.mStyles.keys()   
            
            item.mIsSubitem = aDescription.mIsSubitem
            for subitem in aDescription.mSubitems:
                item.mSubitems.append( subitem )
            
            
            item.setStyle( 'default' )
            item._fillHideList()
            return item
        
        
        @classmethod
        def create( cls, aDescription, aXmlLinkerKey ):
            item = cls.fromDesc( aDescription, aXmlLinkerKey )
            return item
        
        
        
        
        
        
        def setStyle( self, aStyleName ):
            if aStyleName in self.mStyles:
                if self.mActiveStyle != None:
                    self._discardCurrentStyle()
                self.mActiveStyle = aStyleName
                self._applyStyle( aStyleName )
                
                if self.mOwner != None:
                    for item in self.mSubitems:
                        self.mOwner.setStyleItem( item, aStyleName )
        
        def getStyle( self ):
            return self.mActiveStyle
        
        
        
        
        
        def getIsSubitem( self ):
            return self.mIsSubitem
        
        
        
        
        
        
        
        def changeImage( self, aImageFolder, aImageName, aIsActLikeAdding = False ):
            
            CharacterExDebuger.Log( 'CharacterExItem::changeImage: aImageFolder = ' + aImageFolder + ', aImageName = ' + aImageName )
            self.mFileName = aImageName
            self.mFileFolder = aImageFolder
            self.image = aImageFolder + aImageName
            for tr in self.mOwnerTransforms.values():
                self.image = tr.apply( self.image )
            if aIsActLikeAdding:
                if self.mOwner != None:
                    self.mOwner.updateItemSpecial( self )
        
        
        
        
        
        def updateImage( self, aImage ):
            
            self.image = aImage
        
        def getImage( self ):
            return self.image
        
        
        
        
        
        def hide( self, aSource ):
            prevVis = self.mIsVisible
            self._hideInner( aSource )
            if prevVis != self.mIsVisible:
                if not self.mIsSubitem:
                    if self.mOwner != None:
                        self.mOwner._onItemHidden( self )
                self._showFromHideList()
                
                if self.mOwner != None:
                    for item in self.mSubitems:
                        self.mOwner.hideItem( item )
        
        def show( self, aSource ):
            prevVis = self.mIsVisible
            self._showInner( aSource )
            if prevVis != self.mIsVisible:
                if not self.mIsSubitem:
                    if self.mOwner != None:
                        self.mOwner._onItemShown( self )
                self._hideFromHideList()
                
                if self.mOwner != None:
                    for item in self.mSubitems:
                        self.mOwner.showItem( item )
        
        
        def setIsVisible( self, aIsVisible ):
            if self.mIsVisible and not aIsVisible:
                self.hide( None )
            elif not self.mIsVisible and aIsVisible:
                self.show( None )
        
        
        
        
        
        def addTransform( self, aName, aTransform, aIsInner = False ):
            trDict = self._getTransformDict( aIsInner )
            self._addTransform( trDict, aName, aTransform )
        
        def delTransform( self, aName, aIsInner = False ):
            trDict = self._getTransformDict( aIsInner )
            self._delTransform( trDict, aName )
        
        def clearTransforms( self, aIsInner = False ):
            trDict = self._getTransformDict( aIsInner )
            self._clearTransforms( trDict )
        
        def getTransform( self, aName, aIsInner = False ):
            trDict = self._getTransformDict( aIsInner )
            return self._getTransform( trDict, aName )
        
        
        
        
        
        def onSelfAdded( self, aKey, aItems, aCharacterEx ):
            self.mOwner = aCharacterEx
            self.mKey = aKey
            if self.parent and self.parent in aItems:
                itemParent = aItems[ self.parent ]
                self._parentItemRoutines( itemParent )
            self.innerOnSelfAdded( aItems )
        
        def onSelfRemoved( self, aItems, aCharacterEx ):
            self.innerOnSelfRemoved( aItems )
            self.mOwner = None
        
        def onItemAdded( self, aItem ):
            self.innerOnItemAdded( aItem )
        
        def onItemRemoved( self, aItem ):
            self._parentItemRoutines( aItem, True )
            self.innerOnItemRemoved( aItem )
        
        def onItemHidden( self, aItem ):
            self._parentItemRoutines( aItem )
            self.innerOnItemHidden( aItem )
        
        def onItemShown( self, aItem ):
            self._parentItemRoutines( aItem )
            self.innerOnItemShown( aItem )
        
        def onItemStyleBeforeChange( self, aItem ):
            self.innerOnItemStyleBeforeChange( aItem )
        
        def onItemStyleAfterChange( self, aItem ):
            self._parentItemRoutines( aItem )
            self.innerOnItemStyleAfterChange( aItem )
        
        
        
        
        def _hideInner( self, aSource ):
            self.mIsVisible = False
            if aSource != None:
                self.mDirectors.add( aSource )
        
        def _showInner( self, aSource ):
            if aSource != None:
                self.mDirectors.discard( aSource )
            if not self.mDirectors:
                self.mIsVisible = True               
        
        
        def _getTransformDict( self, aIsInner ):
            if aIsInner:
                return self.mTransforms
            else:
                return self.mOwnerTransforms
        
        def _addTransform( self, aTransformDic, aName, aTransform ):
            if aName in aTransformDic.keys():
                tr = aTransformDic[ aName ]
                del aTransformDic[ aName ]
                self.image = tr.discard( self.image )
            self.image = aTransform.apply( self.image )
            aTransformDic[ aName ] = aTransform
        
        def _delTransform( self, aTransformDic, aName ):
            if aName in aTransformDic.keys():
                tr = aTransformDic[ aName ]
                del aTransformDic[ aName ]
                self.image = tr.discard( self.image )
        
        def _clearTransforms( self, aTransformDic ):
            keys = aTransformDic.keys()
            for key in keys:
                self._delTransform( aTransformDic, key )
        
        def _getTransform( self, aTransformDic, aName ):
            if aName in aTransformDic.keys():
                return aTransformDic[ aName ]
            else:
                return None
        
        
        def _applyAction( self, aIndex, aCharacterEx, aEventSenderItem, aItemsAll = None ):
            
            if self.mIsSubitem:
                return
            
            if self.mOwner == None:
                return
            else:
                if aItemsAll == None:
                    aItemsAll = self.mOwner.getAllItems()
            
            for action in self.mActions[ aIndex ]:
                action.act( self, aEventSenderItem, aCharacterEx, aItemsAll )
        
        
        def _applyStyle( self, aStyleName ):
            desc = WTXmlLinker.i( self.mXmlLinkerKey ).getItemStyle( self.mName, aStyleName )
            
            if desc.mFrame != None:
                self.mFileName = desc.mFrame
            if desc.mFileFolder != None:
                self.mFileFolder = desc.mFileFolder
            
            if desc.mFrame != None or desc.mFileFolder != None:
                self.image = self.mFileFolder + self.mFileName
            if desc.mZOrder != None:
                self.zorder = desc.mZOrder
            if desc.mShift != None:
                self.position = Transform( pos = ( desc.mShift.xpos, desc.mShift.ypos ) )
            if desc.mParent != None:
                self.parent = desc.mParent
            if desc.mParentStyles != None:
                del self.parentStyles[:]
                for elem in desc.mParentStyles:
                    self.parentStyles.append( elem )
            if desc.mIsVisible != None:
                self.setIsVisible( bool(desc.mIsVisible) )
            
            
            if desc.mSubItems != None:
                del self.mSubitemsStyle[:]
                for elem in desc.mSubItems:
                    self.mSubitemsStyle.append( elem )
            
            if desc.mHideList != None:
                del self.mHideList[:]
                for elem in desc.mHideList:
                    self.mHideList.append( elem )
            
            
            if desc.mTransforms != None:
                self.mTransforms.clear()
                for key,val in desc.mTransforms.iteritems():
                    self.addTransform( key, CharacterExTransform.create( val ), True )
            
            if desc.mActions != None:
                
                for elem in self.mActions:
                    del elem[:]
                
                for actDesc in desc.mActions:
                    actNew = CharacterExItemAction.create( actDesc )
                    if actNew.mIndex != -1:
                        self.mActions[ actNew.mIndex ].append( actNew )
            
            
            if self.mOwner != None:
                
                if self.mDirectors:
                    self.mIsVisible = False
                
                if self.mIsVisible:
                    self._hideFromHideList()
                
                if not self.mIsSubitem:
                    self.mOwner._onItemStyleAfterChange( self )
                
                for tr in self.mOwnerTransforms.values():
                    self.image = tr.apply( self.image )
                
                if not self.mIsSubitem:
                    for styleSubitem in self.mSubitemsStyle:
                        self.mOwner.addItem( styleSubitem )
        
        def _discardCurrentStyle( self ):
            
            if self.mOwner != None:
                if not self.mIsSubitem:
                    self.mOwner._onItemStyleBeforeChange( self )
            
            self.clearTransforms()
            
            if self.mOwner != None:
                self._showFromHideList()
                
                if not self.mIsSubitem:
                    for styleSubitem in self.mSubitemsStyle:
                        self.mOwner.delItem( styleSubitem )
        
        
        def _showFromHideList( self ):
            if not self.mIsSubitem:
                if self.mOwner != None:
                    for key in self.mHideList:
                        self.mOwner.showItemKey( key, self.mName )
        
        def _hideFromHideList( self ):
            if not self.mIsSubitem:
                if self.mOwner != None:
                    for key in self.mHideList:
                        self.mOwner.hideItemKey( key, self.mName )
        
        
        def _parentItemRoutines( self, aParent, aIsRemoved = False ):
            if aParent.mKey == self.parent:
                isParentVisible = aParent.mIsVisible
                if self.parentStyles:
                    
                    if not aParent.getStyle() in self.parentStyles:
                        isParentVisible = False
                if isParentVisible or aIsRemoved:
                    self._showInner( 'parent' )
                else:
                    self._hideInner( 'parent' )
        
        
        
        
        
        def _fillHideList( self ):
            
            
            None
        
        def innerOnSelfAdded( self, aItems ):
            
            
            self._hideFromHideList()
            self._applyAction( CharacterExItem._indSelfAdded, self.mOwner, self, aItems )
            
            for item in self.mSubitems:
                self.mOwner.addItem( item )
        
        def innerOnSelfRemoved( self, aItems ):
            
            self._showFromHideList()
            self._applyAction( CharacterExItem._indSelfRemoved, self.mOwner, self, aItems )
            
            for item in self.mSubitems:
                self.mOwner.delItem( item )
        
        def innerOnItemAdded( self, aItem ):
            
            
            if not self.mIsSubitem:
                if aItem.mKey in self.mHideList:
                    self.mOwner.hideItemKey( aItem.mKey, self.mName )
            self._applyAction( CharacterExItem._indItemAdded, self.mOwner, aItem )
        
        def innerOnItemRemoved( self, aItem ):
            
            
            
            
            
            self._applyAction( CharacterExItem._indItemRemoved, self.mOwner, aItem )
        
        def innerOnItemHidden( self, aItem ):
            
            self._applyAction( CharacterExItem._indItemHidden, self.mOwner, aItem )
        
        def innerOnItemShown( self, aItem ):
            
            self._applyAction( CharacterExItem._indItemShown, self.mOwner, aItem )
        
        def innerOnItemStyleBeforeChange( self, aItem ):
            
            self._applyAction( CharacterExItem._indStyleBeforeChange, self.mOwner, aItem )
        
        def innerOnItemStyleAfterChange( self, aItem ):
            
            self._applyAction( CharacterExItem._indStyleAfterChange, self.mOwner, aItem )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
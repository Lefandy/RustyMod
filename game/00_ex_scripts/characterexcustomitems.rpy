init -997 python:



    class CharacterExItemDress( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'tits' )




    class CharacterExItemRobe( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'skirt' )




    class CharacterExItemPoseBook( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'hands' )




    class CharacterExItemPantiesShadow( CharacterExItem ):
        def _fillHideList( self ):
            None
        
        def applyChanges( self, aIsPantiesVisible ):
            if aIsPantiesVisible:
                self.mImage = self.mFileFolder + 'shadow_with_panties.png'
            else:
                self.mImage = self.mFileFolder + 'shadow_no_panties.png'
        
        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            if 'panties' in aItems:
                pantiesObj = aItems[ 'panties' ]
                self.applyChanges( pantiesObj.mIsVisible )
            else:
                self.applyChanges( False )
        
        def innerOnItemAdded( self, aItemKey, aItem, ):
            
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem )
            if 'panties' == aItemKey:
                self.applyChanges( aItem.mIsVisible )
        
        def innerOnItemRemoved( self, aItemKey, aItem ):
            
            CharacterExItem.innerOnItemRemoved( self, aItemKey, aItem )
            if 'panties' == aItemKey:
                self.applyChanges( False )




    class CharacterExItemSkirtLifted( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'skirt' )
            self.mHideList.append( 'hands' )
            self.mOldDressTex = None
        
        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            pantiesFound = False
            if 'dress' in aItems.keys():
                dressItem = aItems[ 'dress' ]
                if dressItem.mFileName == 'dress_normal.png':
                    self.mOldDressTex = dressItem.getImage()
                    dressItem.updateImage( self.mOwner.getView().mClothesFolder + "dress_lifted_skirt.png" )
        
        
        
        
        def innerOnSelfRemoved( self, aItems, aCharacterEx ):
            
            CharacterExItem.innerOnSelfRemoved( self, aItems, aCharacterEx )
            
            if self.mOldDressTex != None:
                if 'dress' in aItems.keys():
                    dressItem = aItems[ 'dress' ]
                    if dressItem.mFileName == 'dress_normal.png':
                        dressItem.updateImage( self.mOldDressTex )
                        self.mOldDressTex = None




    class CharacterExItemPoseShowTits( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'dress' )
            self.mHideList.append( 'hands' )




    class CharacterExItemSweat( CharacterExItem ):
        def _fillHideList( self ):
            None
        
        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            if 'face' in aItems:
                faceObj = aItems[ 'face' ]
                if faceObj.mFileName == 'body_97.png' or faceObj.mFileName == 'body_98.png' or faceObj.mFileName == 'body_99.png':
                    self._showInner( 'self' )
                else:
                    self._hideInner( 'self' )
        
        def innerOnItemAdded( self, aItemKey, aItem ):
            
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem )
            if aItemKey == 'face':
                if aItem.mFileName == 'body_97.png' or aItem.mFileName == 'body_98.png' or aItem.mFileName == 'body_99.png':
                    self._showInner( 'self' )
                else:
                    self._hideInner( 'self' )
        
        def innerOnItemRemoved( self, aItemKey, aItem ):
            
            CharacterExItem.innerOnItemRemoved( self, aItemKey, aItem )
            if aItemKey == 'face':
                self._hideInner( 'self' )





    class CharacterExItemPoseParade( CharacterExItem ):
        def _fillHideList( self ):
            None
        
        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            for key,item in aItems.iteritems():
                if item != self and item.mZOrder < G_Z_FACE:
                    self.mOwner.hideItemKey( key, self.__class__.__name__ )
        
        def innerOnSelfRemoved( self, aItems, aCharacterEx ):
            
            CharacterExItem.innerOnSelfRemoved( self, aItems, aCharacterEx )
            for key,item in aItems.iteritems():
                if item != self and item.mZOrder < G_Z_FACE:
                    aCharacterEx.showItemKey( key, self.__class__.__name__ )                 
        
        def innerOnItemAdded( self, aItemKey, aItem ):
            
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem )
            if aItem.mZOrder < G_Z_FACE:
                self.mOwner.hideItem.Key( aItemKey, self.__class__.__name__ ) 




    class CharacterExItemSplatters( CharacterExItem ):
        def _fillHideList( self ):
            None
        
        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            if 'face' in aItems:
                faceObj = aItems[ 'face' ]
                if faceObj.mFileName == 'body_169.png' or faceObj.mFileName == 'body_170.png' or faceObj.mFileName == 'body_171.png':
                    self._showInner( 'self' )
                else:
                    self._hideInner( 'self' )
        
        def innerOnItemAdded( self, aItemKey, aItem ):
            
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem )
            if aItemKey == 'face':
                if aItem.mFileName == 'body_169.png' or aItem.mFileName == 'body_170.png' or aItem.mFileName == 'body_171.png':
                    self._showInner( 'self' )
                else:
                    self._hideInner( 'self' )
        
        def innerOnItemRemoved( self, aItemKey, aItem, aCharacterEx ):
            
            CharacterExItem.innerOnItemRemoved( self, aItemKey, aItem, aCharacterEx )
            if aItemKey == 'face':
                self._hideInner( 'self' )            
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
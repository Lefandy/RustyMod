init -999 python:
    import itertools


    class CharacterExItemAction(store.object):
        _indSelfAdded = 0
        _indSelfRemoved = 1
        _indItemAdded = 2
        _indItemRemoved = 3
        _indItemShown = 4
        _indItemHidden = 5
        _indStyleBeforeChange = 6
        _indStyleAfterChange = 7
        _indItemCount = 8
        
        def __init__( self ):
            self.mIndex = -1
            self.mEvent = ""    
            self.mBlocks = []   
            self.mResults = []  
            self.mBadResults = []   
        
        
        def _checkBlocks( self, aArrayItems, aEventSenderItem ):
            for block in self.mBlocks:
                res = block.check( aArrayItems, aEventSenderItem, False )
                if res.isPassed:
                    return True
            return False
        
        @classmethod
        def create( cls, aActionDescription ):
            desc = aActionDescription
            
            actMap = { 'selfAdded' : CharacterExItemAction._indSelfAdded, 'selfRemoved' : CharacterExItemAction._indSelfRemoved, 
                'itemAdded' : CharacterExItemAction._indItemAdded, 'itemRemoved' : CharacterExItemAction._indItemRemoved,
                'itemShown' : CharacterExItemAction._indItemShown, 'itemHidden' : CharacterExItemAction._indItemHidden,
                'beforeStyleChange' : CharacterExItemAction._indStyleBeforeChange, 'afterStyleChange' : CharacterExItemAction._indStyleAfterChange }
            act = cls()
            
            if desc.mEvent in actMap.keys():
                act.mIndex = actMap[ desc.mEvent ]
            
            act.mEvent = desc.mEvent
            
            for block in desc.mBlocks:
                newBlock = CharacterExItemActionBlock.create( block )
                act.mBlocks.append( newBlock )
            
            for res in desc.mResults:
                newRes = CharacterExItemActionResultFactory.create( res )
                act.mResults.append( newRes )
            
            for badRes in desc.mBadResults:
                newBadRes = CharacterExItemActionResultFactory.create( badRes )
                act.mBadResults.append( newBadRes )
            
            return act
        
        
        def act( self, aParentItem, aEventSenderItem, aCharacterEx, aItemsAllDictionary ):
            
            
            arrayItems = list(aItemsAllDictionary.values())
            
            if self.mEvent == 'selfRemoved':
                arrayItems.append( aParentItem )
            
            
            actionActive = self._checkBlocks( arrayItems, aEventSenderItem )
            
            if actionActive:
                
                
                for res in self.mResults:
                    res.apply( aCharacterEx, aParentItem )
            else:
                for badRes in self.mBadResults:
                    badRes.apply( aCharacterEx, aParentItem )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
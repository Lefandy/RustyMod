init -998 python:
    class CharacterExItemCreator:
        def __init__( self, aItemBase, aSetBase, aXmlLinkerKey ):
            self.mItemBase = aItemBase
            self.mSetBase = aSetBase
            self.mXmlLinkerKey = aXmlLinkerKey    
        
        
        
        def createItem( self, aItemName, aStyle = 'default' ):
            itemDesc = self.mItemBase.get( aItemName )
            if itemDesc != None:
                newItem = CharacterExItem.create( itemDesc, self.mXmlLinkerKey )
                if newItem.mActiveStyle != None and newItem.mActiveStyle != aStyle:
                    newItem.setStyle( aStyle )
                return newItem
            else:
                
                CharacterExDebuger.LogE( 'CharacterExItemCreator::createItem: cant create item with aItemName = ' + aItemName )
                return None
        
        
        
        def createSet( self, aSetName, aStyle = 'default' ):
            setItems = self.mSetBase.get( aSetName )
            if setItems != None:
                resList = []
                for item in setItems:
                    newItem = self.createItem( item )
                    if newItem.mActiveStyle != None and newItem.mActiveStyle != aStyle:
                        newItem.setStyle( aStyle )
                    resList.append( newItem )
                return resList
            else:
                
                CharacterExDebuger.LogE( 'CharacterExItemCreator::createSet: cant create set with aSetName = ' + aSetName )
                return [None]
        
        
        
        def create( self, aItemOrSetName, aStyle = 'default' ):
            if aItemOrSetName[0] == '*':
                setName = aItemOrSetName[1:]
                return self.createSet( setName, aStyle )
            else:
                return [self.createItem( aItemOrSetName, aStyle )]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
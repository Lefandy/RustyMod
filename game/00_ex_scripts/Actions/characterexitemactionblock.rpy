init -999 python:
    import itertools


    class CharacterExItemActionBlock(store.object):
        
        def __init__( self ):
            self.mConditions = []    
        
        @classmethod
        def create( cls, aBlockDescription ):
            desc = aBlockDescription
            block = cls()
            for cond in desc.mConditions:
                condition = CharacterExItemActionConditionFactory.create( cond )
                block.mConditions.append( condition )
            return block
        
        
        
        
        
        
        
        
        
        
        def check( self, aItems, aEventSenderItem, aIsNeedPassedItems = False, aIsNeedPassedUnion = False ):
            if aIsNeedPassedItems:
                passedDic = None
                for cond in self.mConditions:
                    res = cond.check( aItems, aEventSenderItem, aIsNeedPassedItems )
                    if not res.isPassed:
                        return CharacterExItemActionConditionResult( False )
                    else:
                        if not aIsNeedPassedUnion:
                            
                            if passedDic == None:
                                
                                passedDic = res.passedItems
                            else:
                                
                                tmpDic = {}
                                for key in passedDic.keys():
                                    if key in res.passedItems.keys():
                                        tmpDic[ key ] = passedDic[ key ]
                                passedDic = tmpDic
                        else:
                            
                            if key in res.passedItems.keys():
                                passedDic[ key ] = res.passedItems[ key ]
                
                return CharacterExItemActionConditionResult( True, passedDic )
            else:
                for cond in self.mConditions:
                    res = cond.check( aItems, aEventSenderItem, aIsNeedPassedItems )
                    if not res.isPassed:
                        return CharacterExItemActionConditionResult( False )
                return CharacterExItemActionConditionResult( True )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
init -997 python:


    class Item(Entry):
        
        def __init__( self, Name, status, defVals=None):
            if defVals==None:
                defVals={"status": status, "count":0}
            else:
                defVals.update({"status": status, "count":0})
            super(Item, self).__init__(Name=Name, Type="Item", defVals=defVals )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
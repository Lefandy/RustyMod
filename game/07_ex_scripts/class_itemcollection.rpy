init -997 python:


    class ItemCollection(Entry):
        
        def __init__( self, Name, fillingSet=None):
            self.Name=Name
            
            super(ItemCollection, self).__init__(Name=Name, Type="ItemCollection" )
            self.defVals=dict()
            for o in itemList:
                self.defVals.update({o.Name+"_count":0})
                if fillingSet!=None:
                    if o.GetValue("block") in fillingSet:
                        self.defVals.update({o.Name+"_count":fillingSet[o.GetValue("block")]})
        
        
        
        
        def __call__( self, sName=None):
            if sName==None:  
                return self.GetList(0)
            for o in itemList: 
                if o.Name==sName:
                    o.SetValue("count", self.Count(sName))
                    return o
            return None
        
        
        def AddItem(self, Name, count=1): 
            self.IncValue(Name+"_count",count, minim=0)
            return self.__call__(Name)
        
        
        def Count(self, Name):
            
            
            return self.GetValue(Name+"_count")
        
        
        
        def Receive(self, collection, Name, count=1):
            collection.AddItem(Name,-count)
            return self.AddItem(Name,count)
        
        
        def Clear(self, Name=None):
            self.Fill(Name,0)
            return
        
        def Fill(self, Name=None, value=1):
            for o in itemList: 
                if Name==None or o.GetValue("block")==Name:
                    self.SetValue(o.Name+"_count",value)
            return 
        
        
        
        def Any(self,Name=None):
            for o in self.defVals:
                if self.GetValue(o)>0 and (Name==None or Name+"_count"==o):
                    return True
            return False
        
        
        def GetList(self, level=0):
            self._m1_class_ItemCollection__list=[]
            for i in range(len(itemList)):
                if self.Count(itemList[i].Name)>level:
                    self._m1_class_ItemCollection__list.append(itemList[i])
                    itemList[i].SetValue("count",self.Count(itemList[i].Name))
            return self._m1_class_ItemCollection__list
        
        
        def GetBlock(self, sName): 
            for o in itemList: 
                if o.Name==sName:
                    return o.GetValue("block")
            return ""
        
        def SetBlock(self, sName, sBlock): 
            for o in itemList: 
                if o.Name==sName:
                    return o.SetValue("block", sBlock)
            return ""
        
        def GetCaption(self, sName): 
            for o in itemList: 
                if o.Name==sName:
                    return o.GetValue("caption")
            return ""
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
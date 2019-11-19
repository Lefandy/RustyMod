init -997 python:


    class Entry(store.object):
        
        def __init__( self, Name, Type, defVals=None, constVals=None): 
            self.Name=Name
            self.Type=Type
            
            self.defVals = defVals        
            
            if constVals!=None:
                for s in constVals:
                    SetArrayValue(self.Name, s, constVals[s]) 
            return
        
        
        
        
        
        
        
        
        
        def GetValue(self, subkey):
            if subkey in self.defVals:
                return GetStoreValue(self.Name, subkey)
            else:
                return GetArrayValue(self.Name, subkey) 
        
        def SetValue(self, subkey, value, minim=None, maxim=None):
            if minim!=None:
                if value<minim:
                    value=minim
            if maxim!=None:
                if value>maxim:
                    value=maxim
            if subkey in self.defVals:
                if IsStoreSubKey(self.Name, subkey):
                    oldVal=GetStoreValue(self.Name, subkey)
                else:
                    oldVal=None
                SetStoreValue(self.Name, subkey, value)
            else:
                if IsArraySubKey(self.Name, subkey):
                    oldVal=GetArrayValue(self.Name, subkey)
                else:
                    oldVal=None
                SetArrayValue(self.Name, subkey, value)
            
            InitEntryField(self, subkey)
            
            
            
            
            
            return value
        
        def IncValue(self, subkey, incVal, minim=None, maxim=None):
            return self.SetValue(subkey, self.GetValue(subkey)+incVal, minim, maxim)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
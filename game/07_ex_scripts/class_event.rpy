init -997 python:


    class Event(Entry):
        
        def __init__( self, sFullName, scenario, points, ready, done, defVals, constVals):
            alter=None
            caption=None
            self.Name=sFullName
            if ":" in sFullName:
                sp =sFullName.split(":") 
                self.Name=sp[0]
                alter=sp[1]
                if len(sp)>2: caption=sp[2] 
            
            super(Event, self).__init__(Name=self.Name, Type="Event", defVals=defVals, constVals=constVals )
            
            self.defVals = {"startCount": 0, "finishCount": 0, "start1": -1, "start2": -1, "finish1": -1, "finish2": -1, "finish2Time": 0, "start2Time": 0}        
            if defVals!=None:
                self.defVals.update(defVals)
            
            
            
            
            
            SetArrayValue(self.Name, "ready", ready) 
            SetArrayValue(self.Name, "done", done) 
            SetArrayValue(self.Name, "alter", alter) 
            SetArrayValue(self.Name, "caption", caption) 
            SetArrayValue(self.Name, "points", points) 
            SetArrayValue(self.Name, "scenario", scenario) 
            return
        
        
        
        
        
        
        def IsExec( self, iDaysAgo, sStartFinishMode ):
            if self.GetValue(sStartFinishMode)==-1:
                return False
            else:
                return self.GetValue(sStartFinishMode) <= day-iDaysAgo
        
        
        def IsFinished( self ):
            return self.IsExec(0, "finish2")
        
        
        def IncStarted( self ):
            if self.GetValue("start1")==-1:
                self.SetValue("start1", day)
            self.SetValue("start2", day)
            self.SetValue("start2Time", time.stamp)
            self.SetValue("startCount", self.GetValue("startCount")+1)
            return
        
        
        def IncFinished( self ):
            
            
            
            if self.GetValue("finish1")==-1:
                self.SetValue("finish1", day)
            self.SetValue("finish2", day)
            self.SetValue("finish2Time", time.stamp)
            self.IncValue("finishCount", 1)
            return
        
        
        def LabelExecute( self ):
            self.IncStarted()
            
            return
        
        
        
        
        
        def IsAgo( self, interval, intervalType=None ):
            if intervalType==None:
                return self.IsExec(interval, "finish2")
            else:
                time.IsPassed(self.GetValue("finish2Time"), interval, intervalType)
        
        
        
        
        def IsDone(self):
            fn=GetArrayValue(self.Name,"done")
            val=None if fn==None else fn(self)
            bRes=self.IsFinished() if fn==None else val 
            return bRes
        
        def IsReady(self):
            
            bReadyDef=True if self.prev==None else self.prev.IsDone()
            
            fn=GetArrayValue(self.Name,"ready")
            val=None if fn==None else fn(self)
            bReady=True if fn==None else val
            return bReadyDef and bReady
        
        def IsActive(self):
            return self.IsReady() and not self.IsDone()
        
        def NotFinished(self):
            
            
            
            return
        
        
        
        
        
        
        
        
        
        
        
        
        def Finalize(self, label=None):
            self.IncFinished()
            if label != None:
                renpy.jump(label)
            return
        
        
        
        def Run(self):
            renpy.call(self.Name)
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
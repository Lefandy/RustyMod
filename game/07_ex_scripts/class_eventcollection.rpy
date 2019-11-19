init -998 python:


    class EventCollection(store.object):
        def __init__( self): 
            scenario=None
            points={}
            self.List=[] 
        
        
        
        def __call__( self, sName=None):
            return self.GetCall(sName)
        
        def GetCall( self, sName=None):
            if sName==None:
                return self
            
            for e in self.List:
                if e.Name==sName:
                    return e
            
            return None
        
        
        
        
        
        
        
        
        
        
        def Where(self,points, scenario=""):
            self.scenario=scenario
            
            self.points=points.copy()
            return self
        
        
        def AddStep( self, sFullName, ready=None, done=None, defVals=None, constVals=None):
            
            self.AddEvent(sFullName, self.scenario, self.points.copy(), ready, done, defVals, constVals)
        
        
        
        def AddEvent( self, sFullName, scenario=None, points={}, ready=None, done=None, defVals=None, constVals=None):
            prev=None
            prevInList=None
            
            if len(self.List)>0:
                prevInList=self.List[len(self.List)-1]
            
            for e in self.List:
                if e.GetValue("scenario")==scenario:
                    prev=e
            
            self.List.append(RegEntry(Event(sFullName, scenario, points, ready, done, defVals, constVals)))
            
            if prev!=None: prev.next=self.List[len(self.List)-1]
            self.List[len(self.List)-1].prev=prev
            self.List[len(self.List)-1].prevInList=prevInList
            
            return self.List[len(self.List)-1]
        
        
        
        
        def Has( self, sNameOrAlter):
            for e in self.List:
                if e.Name==sNameOrAlter or e._alter==sNameOrAlter:
                    return e.IsDone()
            return False
        
        
        
        
        
        def GetStep(self, point):
            for e in self.List:
                if (point in e._points) and e.IsActive() and e._scenario!=None:
                    return e
            
            return None
        
        def IsStep(self, point):
            return self.GetStep(point) != None
        
        
        def RunStep(self, point):
            e = self.GetStep(point)
            if e!=None:
                e.Run()
        
        
        def GetTime(self, sStartFinishMode, scenario=None, points=None):
            self._m1_class_EventCollection__stamp=0
            for e in self.List:
                debug.SaveString(e.Name+": "+str(e._scenario)+" "+str(e._points))
                if scenario==None or scenario==e._scenario:
                    if points==None or points.intersection(e._points)!={}:
                        if e.GetValue(sStartFinishMode+"Time")>self._m1_class_EventCollection__stamp:
                            
                            self._m1_class_EventCollection__stamp=e.GetValue(sStartFinishMode+"Time")
            return self._m1_class_EventCollection__stamp
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
init -992 python:












    class This(EventCollection): 
        def __init__(self):
            super(This, self).__init__()
            self.Name=None
        
        
        
        
        def __call__( self, sName=None):
            if (sName!=None): 
                this.Name=sName
            
            e=self.GetCall(self.Name)
            if hasattr(renpy.store,"wtevent") and (e!=None): 
                renpy.store.wtevent=e
            return e










    def OnLabelExecute(s):
        try:
            if s[0]!="_":
                labelHistory.append(s)
                if len(labelHistory)>120:
                    del labelHistory[0:len(labelHistory)-121]
                
                
                if this(s)!=None:
                    
                    
                    this().LabelExecute()
        
        except Exception:
            pass







    def IsEventOnlyAfter(actualLabel):
        for s in reversed(labelHistory[0:len(labelHistory)-2]): 
            if s==actualLabel:
                break
            if not this.GetCall(s) in [None, renpy.store.wtevent.Name]: 
                return False
        return True

    def Execute(e, s, condition=True):
        if not condition: return False
        if e!=None:
            s=s.replace("_e.", "this.GetCall('"+e.Name+"').")
        exec s
        return True


    def Rand(iMax): 
        import random 
        return int(random.random()*iMax+1)

    def RandFromSet(availSet, onetimeSet={}):
        o=list(availSet)[Rand(len(availSet))-1]
        if o in onetimeSet:
            availSet-={o}                
        return o

    def Sign(value):
        return (value>0)-(value<0)


    def GetStage(value, minValue, levelCount=3, step=3): 
        value=value-minValue
        if value<0: return 0
        if int(value/step)+1>=levelCount: return levelCount
        return int(value/step)+1









    def SetHearts(heartCount, _event=None): 
        if _event==None:
            _event=wtevent
        return _event.SetValue("heartCount",heartCount)

    def IsFirstRun(): 
        return IsRunNumber(1) 

    def IsNextRun(): 
        return IsRunNumberOrMore(2)

    def IsRunNumber(num): 
        return wtevent._finishCount==num-1

    def IsRunNumberOrMore(num): 
        return wtevent._finishCount>=num-1

    def Say(formatstring):
        if ":>" in formatstring:
            _m1_class_This__temp=formatstring.split(":>")
            _m1_class_This__person=GetEntry(_m1_class_This__temp[0])
            _m1_class_This__person(_m1_class_This__temp[1])
        else:
            screens.Say(formatstring)

    def StringFormat(s):
        _m1_class_This__pars=s.split(" ")
        
        s=""
        for o in _m1_class_This__pars:
            _m1_class_This__count=0
            if len(o)>=2 and not o.isdigit():
                for h in o:
                    if h.isalpha() and h.isupper():
                        _m1_class_This__count+=1
                    if _m1_class_This__count>=2:
                        o="{size=+5}"+o+"{/size}"
                        break
            
            s+=o+" "
        if s!=None:
            s=s.strip(" ")
        
        if "#(" in s: 
            s=s.replace("#(","{size=-3}(") 
            s=s.replace(")","){/size}") 
        else:
            if len(s)>1:
                if s[0]=="#": 
                    s="{size=-3}"+s[1:]+"{/size}"
            if len(s)>3:
                if s[:2] in {"{-", "{+"}: 
                    s="{size="+s[1:3]+s[3:]+"{/size}"
        
        
        return s
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
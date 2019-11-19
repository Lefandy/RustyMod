


init -990 python:




    class Debug(store.object):
        def __init__( self, Level=1):
            self.FileName="debug.txt"
            self.Level=Level  
        
        
        def SaveHeader(self):
            if self.Level>0:
                f1 = open(self.FileName, 'a')
                f1.write("\n-----------------------------------------\n")
                f1.close()
        
        
        def SaveString(self, s, Level=3):
            if Level<=self.Level:
                f1 = open(self.FileName, 'a')
                s=s.encode('utf8')+"\n"
                
                f1.write(s)
                f1.close()
        
        def SaveEvent(self, s, FileName=None):
            if FileName==None:
                FileName=self.FileName
            self.e=this.GetCall(s)
            self.SaveString(str(self.e.__dict__)+", IsReady()="+str(self.e.IsReady())+", IsDone()="+str(self.e.IsDone())+", IsActive()="+str(self.e.IsActive()) )
        
        
        def Dump( self):
            
            
            
            
            
            
            
            
            
            
            
            self.SaveEvent("new_request_01")
            self.SaveEvent("new_request_02")
            return
        
        def LoadExecute(self):
            
            
            f1 = open("code.txt", 'r')
            
            s=f1.read()
            
            f1.close()
            
            Execute(None,s)
            return s

    def le():
        return debug.LoadExecute()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
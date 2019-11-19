init -999 python:


    class Music(store.object):
        
        def __init__( self): 
            self.List=[]
            self.Name=None
            
            return
        
        def __call__( self, name=None):
            if (name!=None):
                if name=="<": 
                    self.List.pop() 
                    name=self.List.pop() 
                self.Start(name) 
            else:
                self.Stop()
            return e
        
        
        def Start(self,name):
            self.Name=name
            self.List.append(self.Name)
            
            self._m1_class_Music__music_start_set={
                "Supergirl":"music/Reamonn-Supergirl.mp3",
                "Daphne Theme":"music/Bittersweet Symphony (Instrumental).mp3",
                 "Daphne Privacy": "music/Cure-Lullaby.mp3"  
            }
            
            self.Name = name if self._m1_class_Music__music_start_set.get(name)==None else self._m1_class_Music__music_start_set.get(name)
            
            renpy.music.play(self.Name, fadein=1, fadeout=1)
            return
        
        def Stop(self):
            renpy.music.stop(fadeout=1.0)
            renpy.pause(1.1)
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
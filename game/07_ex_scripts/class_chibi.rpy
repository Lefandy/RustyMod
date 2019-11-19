init -996 python:


    class Chibi(Entry):
        
        def __init__( self, Name, defVals=None):
            super(Chibi, self).__init__(Name=Name, Type="Chibi", defVals={"x0":0, "y0":0, "speed":0.0, "appearance":None, "image":"blink"} )
            return
        
        
        def TransPos(self, image, x=None, y=None, lag=0.0):
            if y==None:
                y=self.y0
            if x==None:
                x=self.x0
            self.Hide()
            renpy.show_screen(self.Name+"screen", self.Name+" "+("" if self._appearance==None else self._appearance+" ")+image, self.x0, x, y, lag)
            self.SetValue("image",image)
            if self._m1_class_Chibi__transition is not None:
                renpy.with_statement( self._m1_class_Chibi__transition, None, True ) 
            renpy.pause(lag)
            
            self.x0=x
            self.y0=y
            return self
        
        
        def Trans(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            self._m1_class_Chibi__args=[arg1, arg2, arg3, arg4, arg5]
            self._m1_class_Chibi__transition=None
            
            for o in self._m1_class_Chibi__args:
                if o==None:
                    break
                if isinstance( o, basestring ):
                    self._m1_class_Chibi__pars=o.split(" ")
                    if len(self._m1_class_Chibi__pars)>=2:
                        self._m1_class_Chibi__State(self._m1_class_Chibi__pars[1])
                    
                    self.TransPos(self._m1_class_Chibi__pars[0], self._m1_class_Chibi__x, self._m1_class_Chibi__y, 0.0 if self.speed==0.0 else abs(self._m1_class_Chibi__x-self.x0)/self._m1_class_Chibi__speed)
                else:
                    self._m1_class_Chibi__transition=o
            return self
        
        
        def Hide(self, transition=None):
            
            
            
            screens.Hide(transition, self.Name+"screen")
            return self
        
        
        def State(self, x=None, y=None, speed=None, appearance=None):
            if appearance!=None:
                self.appearance=appearance
            if x!=None:
                self._m1_class_Chibi__State(x, y, speed)
                self.x0=self._m1_class_Chibi__x
                self.y0=self._m1_class_Chibi__y
                self.speed=self._m1_class_Chibi__speed
            return self
        
        def Refresh(self):
            self.Trans("blink center")
            return self
        
        
        def _m1_class_Chibi__State(self, x=None, y=None, speed=None):
            self._m1_class_Chibi__speed=self.speed
            self._m1_class_Chibi__x=self.x0
            self._m1_class_Chibi__y=self.y0
            if isinstance( x, basestring ):
                self._m1_class_Chibi__x=self.GetValue(x)[0]
                self._m1_class_Chibi__y=self.GetValue(x)[1]
            else:
                if x!=None:
                    self._m1_class_Chibi__x=x
                if y!=None:
                    self._m1_class_Chibi__y=y
            if isinstance( speed, basestring ):
                self._m1_class_Chibi__speed={"go":80.0}[speed]
            else:
                if speed!=None:
                    self._m1_class_Chibi__speed=speed
            return 
        
        
        
        @property
        def x0(self):
            return self.GetValue("x0")
        @x0.setter
        def x0(self, value):
            self.SetValue("x0", value)
        
        @property
        def y0(self):
            return self.GetValue("y0")
        @y0.setter
        def y0(self, value):
            self.SetValue("y0", value)
        
        @property
        def speed(self):
            return self.GetValue("speed")
        @speed.setter
        def speed(self, value):
            self.SetValue("speed", value)
        
        @property
        def appearance(self):
            return self.GetValue("appearance")
        @speed.setter
        def appearance(self, value):
            self.SetValue("appearance", value)




screen chibidaphnescreen(aImgs, x1=0, x2=0, y=0, lag=1.0 ):
    zorder 2
    add aImgs at chibitrans(x1, x2, y, lag)

transform chibitrans(x1=0, x2=0, y=0, lag=1.0):
    xpos x1
    ypos y
    linear lag xpos x2























































screen chibisnapescreen(aImgs, x1=0, x2=0, y=0, lag=1.0 ):
    zorder 2
    add aImgs at chibitrans(x1, x2, y, lag)

image chibisnape go:
    "03_hp/09_snape_ani/snape_02.png"
    pause .18
    "03_hp/09_snape_ani/snape_03.png"
    pause .18
    "03_hp/09_snape_ani/snape_02.png"
    pause .18
    "03_hp/09_snape_ani/snape_05.png"
    pause .18
    repeat

image chibisnape goout:
    im.Flip("03_hp/09_snape_ani/snape_02.png", horizontal=True)
    pause .18
    im.Flip("03_hp/09_snape_ani/snape_03.png", horizontal=True)
    pause .18
    im.Flip("03_hp/09_snape_ani/snape_02.png", horizontal=True)
    pause .18
    im.Flip("03_hp/09_snape_ani/snape_05.png", horizontal=True)
    pause .18
    repeat

image chibisnape blink:
    "03_hp/09_snape_ani/snape_0130.png"



screen chibihermionescreen(aImgs, x1=0, x2=0, y=0, lag=1.0 ):
    zorder 2
    add aImgs at chibitrans(x1, x2, y, lag)

image chibihermione blink:
    "03_hp/animation/h_walk_01.png"
    pause 2
    "03_hp/animation/h_walk_06.png"
    pause .08
    "03_hp/animation/h_walk_01.png"
    pause 5
    "03_hp/animation/h_walk_06.png"
    pause .08
    "03_hp/animation/h_walk_01.png"
    pause .08
    "03_hp/animation/h_walk_06.png"
    pause .08
    "03_hp/animation/h_walk_01.png"
    pause 3
    repeat

image chibihermione go:
    "03_hp/animation/h_walk_01.png"
    pause .08
    "03_hp/animation/h_walk_02.png"
    pause .08
    "03_hp/animation/h_walk_03.png"
    pause .08
    "03_hp/animation/h_walk_02.png"
    pause .08
    "03_hp/animation/h_walk_01.png"
    pause .08
    "03_hp/animation/h_walk_04.png"
    pause .08
    "03_hp/animation/h_walk_05.png"
    pause .08
    "03_hp/animation/h_walk_04.png"
    pause .08
    repeat

image chibihermione goout:
    im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
    pause .08
    im.Flip("03_hp/animation/h_walk_02.png", horizontal=True)
    pause .08
    im.Flip("03_hp/animation/h_walk_03.png", horizontal=True)
    pause .08
    im.Flip("03_hp/animation/h_walk_02.png", horizontal=True)
    pause .08
    im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
    pause .08
    im.Flip("03_hp/animation/h_walk_04.png", horizontal=True)
    pause .08
    im.Flip("03_hp/animation/h_walk_05.png", horizontal=True)
    pause .08
    im.Flip("03_hp/animation/h_walk_04.png", horizontal=True)
    pause .08
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
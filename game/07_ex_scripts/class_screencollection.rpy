init -998 python:


    class ScreenCollection(store.object):
        def __init__( self): 
            self.Name="screens"
            return 
        
        
        def _m1_class_ScreenCollection__Action(self, name, isshow, position=None, par1=None, par2=None, par3=None):
            self._m1_class_ScreenCollection__transition=None
            for o in name:
                if isinstance( o, basestring ):
                    if isshow:
                        if position!=None:
                            renpy.show_screen( o , position) 
                        else:
                            if par3!=None:
                                renpy.show_screen( o , par1, par2, par3)
                            elif par2!=None:
                                debug.SaveString(o+" "+str(par1)+" "+str(par2))
                                renpy.show_screen( o , par1, par2)
                            elif par1!=None:
                                renpy.show_screen( o , par1)
                            else:
                                renpy.show_screen( o )
                    else:
                        renpy.hide_screen( o ) 
                    if self._m1_class_ScreenCollection__transition is not None:
                        renpy.with_statement( self._m1_class_ScreenCollection__transition, None, True )
                else:
                    self._m1_class_ScreenCollection__transition=o
            return self
        
        
        
        def Show(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None, par1=None, par2=None, par3=None):
            return self._m1_class_ScreenCollection__Action([arg1, arg2, arg3, arg4, arg5], True, None, par1, par2, par3)
        
        
        def ShowHide(self, arg1, arg2, arg3=None):
            if arg3==None:
                self._m1_class_ScreenCollection__transition=None
                self._m1_class_ScreenCollection__name=arg1
                self._m1_class_ScreenCollection__lag=arg2
            else:
                self._m1_class_ScreenCollection__transition=arg1
                self._m1_class_ScreenCollection__name=arg2
                self._m1_class_ScreenCollection__lag=arg3
            
            self.Show(self._m1_class_ScreenCollection__transition, self._m1_class_ScreenCollection__name )
            renpy.pause(self._m1_class_ScreenCollection__lag)
            self.Hide(self._m1_class_ScreenCollection__transition, self._m1_class_ScreenCollection__name )
            return self
        
        
        def Hide(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self._m1_class_ScreenCollection__Action([arg1, arg2, arg3, arg4, arg5], False, None)
        
        
        def ShowD3(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None, par1=None, par2=None, par3=None):
            return self._m1_class_ScreenCollection__Action([Dissolve(.3), arg1, arg2, arg3, arg4, arg5], True, None, par1, par2, par3)
        
        
        def HideD3(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self._m1_class_ScreenCollection__Action([Dissolve(.3), arg1, arg2, arg3, arg4, arg5], False, None)
        
        
        def Pause(self, lag=None):
            renpy.pause(lag)
            return self
        
        
        def ShowPos(self, arg1, arg2, arg3=None):
            if arg3==None:
                self._m1_class_ScreenCollection__transition=None
                self._m1_class_ScreenCollection__name=arg1
                self._m1_class_ScreenCollection__pos=arg2
            else:
                self._m1_class_ScreenCollection__transition=arg1
                self._m1_class_ScreenCollection__name=arg2
                self._m1_class_ScreenCollection__pos=arg3
            return self._m1_class_ScreenCollection__Action([self._m1_class_ScreenCollection__transition, self._m1_class_ScreenCollection__name], True, self._m1_class_ScreenCollection__pos)
        
        
        def Say(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None):
            self._m1_class_ScreenCollection__args=[]
            for o in [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10]:
                if o==None:
                    break
                else:
                    for p in o.split("//"):
                        if p!=None:
                            if p.strip()!=None:
                                self._m1_class_ScreenCollection__args.append(p.strip(" "))
            
            for o in self._m1_class_ScreenCollection__args:
                if o==None:
                    break
                else:
                    renpy.say("", StringFormat(o))
            return self
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
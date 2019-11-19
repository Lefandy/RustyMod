init python:


    class MenuItem(store.object):
        def __init__(self, caption, label, objName, isActive, params):            
            self.caption = caption
            self.label = label
            self.isActive = isActive
            self.objName=objName
            self.params = params

    class RunMenu(store.object):
        current = None
        screen = "display"
        
        def __init__(self,
            text=None,
            who=None,
            items=None):
            
            
            
            self.choice=None
            self.choiceItem = None
            self.menuParams = None
            self.Clear()
            if items!=None:
                for i in items:
                    self.AddItem(i)
            if text:
                self.text = text
                if who:
                    self.who = who 
        
        def SetMenuParams(self, params):
            self.menuParams = params
        
        def AddItem(self, caption=None, label=None,  objName=None, params=None):
            if objName==None:
                objName=label
            self.items.append(MenuItem(caption, label, objName, True, params))
        
        def Clear(self):
            self.items = [ ]
            self.text = None
            self.who = None
        
        def Show(self,
            escLabel=None,
            escText=None,
            escParams=None):
            self.escLabel=escLabel
            RunMenu.current = self                        
            if self.text:
                renpy.say(self.who, self.text, interact=False)
            
            if escLabel!=None:
                if escText==None:
                    escText="- Ничего -"
                self.AddItem(escText, escLabel, "", escParams)
            renpy.call_screen(RunMenu.screen)
        
        
        def SetCurrentMenuItem(self, sName):
            self.choice=sName
        def SetCurrentMenuItemObject(self, sItem):
            self.choiceItem=sItem



screen display:
    add "03_hp/11_misc/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign 0.5

        has vbox:
            style "menu"
            spacing 2

        for i in RunMenu.current.items:

            if i.isActive:

                button:

                    action [Function(this, sName=i.objName), 
                            Function(RunMenu.current.SetCurrentMenuItem, sName=i.objName),
                            Function(RunMenu.current.SetCurrentMenuItemObject, sItem=i),
                            Jump(i.label) if i.label!=None else Return()]
                    style "menu_choice_button"

                    text i.caption style "menu_choice"



            else:
                button:


                    action [Jump(i.label) ]
                    style "menu_choice_button"
                    text "{color=#ffff00}"+i.caption +"{/color}" style "menu_choice"










    zorder 7
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
label Achievement_constants:

    define const_ACH_PERS_HERMIONA = 1
    define const_ACH_PERS_PHOENIX = 2

    define const_ACH_BLOCK_HERMIONA_SHIRT = 11
    define const_ACH_BLOCK_HERMIONA_SKIRT = 12
    define const_ACH_BLOCK_HERMIONA_OTH = 13
    define const_ACH_BLOCK_HERMIONA_SPECIAL = 14

    define const_ACH_BLOCK_PHOENIX_ALL = 21

    define const_ACH_WRD_HERMIONA_STANDART02 = 1101
    define const_ACH_WRD_HERMIONA_STANDART03 = 1102
    define const_ACH_WRD_HERMIONA_STANDART04 = 1103
    define const_ACH_WRD_HERMIONA_STANDART05 = 1104
    define const_ACH_WRD_HERMIONA_SKIMPYSHIRT = 1105
    define const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER = 1106
    define const_ACH_WRD_HERMIONA_SHIRT_BUSINESS = 1107
    define const_ACH_WRD_HERMIONA_SHORTSKIRT = 1201
    define const_ACH_WRD_HERMIONA_XSHORTSKIRT = 1202
    define const_ACH_WRD_HERMIONA_XXSHORTSKIRT = 1203
    define const_ACH_WRD_HERMIONA_XSMALLSKIRT = 1204
    define const_ACH_WRD_HERMIONA_XXSMALLSKIRT = 1205
    define const_ACH_WRD_HERMIONA_XXXSMALLSKIRT = 1206
    define const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER = 1207
    define const_ACH_WRD_HERMIONA_SKIRT_BUSINESS = 1208
    define const_ACH_WRD_HERMIONA_NETS = 1301
    define const_ACH_WRD_HERMIONA_TIGHTS = 1302

    define const_ACH_WRD_HERMIONA_ST_ALL = 1401

    define const_ACH_EASTEREGGS_PHOENIX = 2101
    define const_ACH_EASTEREGGS_PHOENIXSCENE = 2102

    return

init -999 python:


    class Achievement(store.object):
        
        current = None
        screen = "achieves_disp"
        
        
        def __init__( self ):
            
            self.choice = 0
            self.esc = None
            self.ret = None
            self.hero = 0
            self.block = 0
            
            self.Indexes = [ const_ACH_WRD_HERMIONA_SHORTSKIRT, const_ACH_WRD_HERMIONA_XSHORTSKIRT, const_ACH_WRD_HERMIONA_XXSHORTSKIRT,
                             const_ACH_WRD_HERMIONA_XSMALLSKIRT, const_ACH_WRD_HERMIONA_XXSMALLSKIRT, const_ACH_WRD_HERMIONA_XXXSMALLSKIRT,
                             const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER, const_ACH_WRD_HERMIONA_SKIRT_BUSINESS, const_ACH_WRD_HERMIONA_STANDART02,
                             const_ACH_WRD_HERMIONA_STANDART03, const_ACH_WRD_HERMIONA_STANDART04, const_ACH_WRD_HERMIONA_STANDART05,
                             const_ACH_WRD_HERMIONA_SKIMPYSHIRT, const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER, const_ACH_WRD_HERMIONA_SHIRT_BUSINESS,
                             const_ACH_WRD_HERMIONA_NETS, const_ACH_WRD_HERMIONA_TIGHTS,
                             const_ACH_WRD_HERMIONA_ST_ALL,
                            
                            const_ACH_EASTEREGGS_PHOENIX, const_ACH_EASTEREGGS_PHOENIXSCENE,            
                            ]
            self.Values = { const_ACH_WRD_HERMIONA_SHORTSKIRT : False, const_ACH_WRD_HERMIONA_XSHORTSKIRT : False, const_ACH_WRD_HERMIONA_XXSHORTSKIRT : False,
                            const_ACH_WRD_HERMIONA_XSMALLSKIRT : False, const_ACH_WRD_HERMIONA_XXSMALLSKIRT : False, const_ACH_WRD_HERMIONA_XXXSMALLSKIRT : False,
                            const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER : False, const_ACH_WRD_HERMIONA_SKIRT_BUSINESS : False, const_ACH_WRD_HERMIONA_STANDART02 : False,
                            const_ACH_WRD_HERMIONA_STANDART03 : False, const_ACH_WRD_HERMIONA_STANDART04 : False, const_ACH_WRD_HERMIONA_STANDART05 : False,
                            const_ACH_WRD_HERMIONA_SKIMPYSHIRT : False, const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER : False, const_ACH_WRD_HERMIONA_SHIRT_BUSINESS : False,
                            const_ACH_WRD_HERMIONA_NETS : False, const_ACH_WRD_HERMIONA_TIGHTS : False,
                            const_ACH_WRD_HERMIONA_ST_ALL : False,
                            
                            const_ACH_EASTEREGGS_PHOENIX : False, const_ACH_EASTEREGGS_PHOENIXSCENE : False,
                            } 
            
            self.iEndings = { 1,2,3 }                
            self.Endings = { 1 : False , 2 : False , 3 : False }
        
        
        def SetAchievement( self, iIndex=0 ):
            
            tmp = True
            
            if iIndex == 0:
                iIndex = self.choice
            self.Values[iIndex]=True
            
            for i in self.Indexes :
                if ((i >= const_ACH_WRD_HERMIONA_STANDART02 and i <= const_ACH_WRD_HERMIONA_SKIMPYSHIRT) or (i >= const_ACH_WRD_HERMIONA_SHORTSKIRT and i <= const_ACH_WRD_HERMIONA_XXXSMALLSKIRT)) and self.Values [i] == False :
                    tmp = False
            if tmp == True :
                self.Values [const_ACH_WRD_HERMIONA_ST_ALL] = True
        
        
        def IsAchievement( self, iIndex=0 ):
            if iIndex == 0:
                iIndex = self.choice
            if self.Values[iIndex]==True:
                return True
            else:
                return False
        
        
        def GetSumPoints (self, iHero = 1):
            ret = 0
            for i in self.Indexes :
                if self.Values[i] == True:
                    ret += self.GetPoints ( i, iHero )
            
            if iHero == const_ACH_PERS_HERMIONA :
                for i in self.iEndings :
                    if self.Endings[i] == True :
                        ret += 100
            
            return ret
        
        
        def GetPoints (self, iIndex=0, iHero = 1):
            if iHero == const_ACH_PERS_HERMIONA :
                if iIndex == const_ACH_WRD_HERMIONA_SHORTSKIRT :
                    return 10
                elif iIndex == const_ACH_WRD_HERMIONA_XSHORTSKIRT :
                    return 10
                elif iIndex == const_ACH_WRD_HERMIONA_XXSHORTSKIRT :
                    return 15
                elif iIndex == const_ACH_WRD_HERMIONA_XSMALLSKIRT :
                    return 20
                elif iIndex == const_ACH_WRD_HERMIONA_XXSMALLSKIRT :
                    return 25
                elif iIndex == const_ACH_WRD_HERMIONA_XXXSMALLSKIRT :
                    return 30
                elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER :
                    return 10
                elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_BUSINESS :
                    return 15
                elif iIndex == const_ACH_WRD_HERMIONA_STANDART02 :
                    return 5
                elif iIndex == const_ACH_WRD_HERMIONA_STANDART03 :
                    return 5
                elif iIndex == const_ACH_WRD_HERMIONA_STANDART04 :
                    return 10
                elif iIndex == const_ACH_WRD_HERMIONA_STANDART05 :
                    return 15
                elif iIndex == const_ACH_WRD_HERMIONA_SKIMPYSHIRT :
                    return 25
                elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER :
                    return 15
                elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_BUSINESS :
                    return 10
                elif iIndex == const_ACH_WRD_HERMIONA_NETS :
                    return 10
                elif iIndex == const_ACH_WRD_HERMIONA_TIGHTS :
                    return 5
                elif iIndex == const_ACH_WRD_HERMIONA_ST_ALL :
                    return 15
                else :
                    return 0
            
            if iHero == const_ACH_PERS_PHOENIX :
                return 0
        
        
        def Name ( self, iIndex=0 ):
            
            p1 = self.GetPoints (iIndex, const_ACH_PERS_HERMIONA)
            add1 = " {color=00FF00}+" + str (p1) + "G{/color}"
            p2 = self.GetPoints (iIndex, const_ACH_EASTEREGGS_PHOENIX)
            add2 = " {color=888888}+" + str (p2) + "G{/color}"
            
            if iIndex == 0:
                iIndex = self.choice
            if iIndex == const_ACH_WRD_HERMIONA_SHORTSKIRT :
                return "Школьная средняя юбка." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_XSHORTSKIRT :
                return "Школьная короткая юбка." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_XXSHORTSKIRT :
                return "Школьная игривая юбка." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_XSMALLSKIRT :
                return "Школьная мини-юбка." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_XXSMALLSKIRT :
                return "Школьная микро-юбка." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_XXXSMALLSKIRT :
                return "Школьная нано-юбка." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER :
                return "Юбка болельщицы Гриффиндора." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_BUSINESS :
                return "Юбка бизнес-леди." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART02 :
                return "Без жилетки." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART03 :
                return "Без жилетки и галстука." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART04 :
                return "Рубашке с расстегнутым воротом." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART05 :
                return "Полурасстегнутая рубашка." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_SKIMPYSHIRT :
                return "Рубашка мини-топик." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER :
                return "Кофта болельщицы Гриффиндора." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_BUSINESS :
                return "Белая рубашка в деловом стиле." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_NETS :
                return "Ажурные чулки." + add1
            elif iIndex == const_ACH_WRD_HERMIONA_TIGHTS :
                return "Колготки." + add1
            
            elif iIndex == const_ACH_WRD_HERMIONA_ST_ALL :
                return "Комплект школьной одежды."  + add1           
            
            
            
            if iIndex == const_ACH_EASTEREGGS_PHOENIX :
                return "Вам удалось обнаружить пасхалку Феникса." + add2
            elif iIndex == const_ACH_EASTEREGGS_PHOENIXSCENE :
                return "Вам удалось обнаружить второй уровень пасхалки Феникса." + add2
            return "Ошибка: незаданный ачивмент."
        
        
        def DescriptionTxt ( self, iIndex=0 ):
            if iIndex == 0:
                iIndex = self.choice
            if iIndex == const_ACH_WRD_HERMIONA_SHORTSKIRT :
                return "Вы купили Гермионе в подарок укороченную школьную юбку. Затем удалось уговорить ее носить эту юбку в школе на занятиях."
            elif iIndex == const_ACH_WRD_HERMIONA_XSHORTSKIRT :
                return "Вы купили Гермионе в подарок сильно укороченную школьную юбку. Затем удалось уговорить ее носить эту юбку в школе на занятиях."
            elif iIndex == const_ACH_WRD_HERMIONA_XXSHORTSKIRT :
                return "Вы купили Гермионе в подарок короткую школьную юбку. Затем удалось уговорить ее носить эту юбку в школе на занятиях. Куда только смотрят учителя ?"
            elif iIndex == const_ACH_WRD_HERMIONA_XSMALLSKIRT :
                return "Вы купили Гермионе в подарок школьную миниюбку и уговорили носить на занятиях. Спасайся кто может, секс-бомба покинула люк."
            elif iIndex == const_ACH_WRD_HERMIONA_XXSMALLSKIRT :
                return "Вы купили Гермионе в подарок укороченную школьную миниюбку и уговорили носить на занятиях. Месть Снейпу сладка."
            elif iIndex == const_ACH_WRD_HERMIONA_XXXSMALLSKIRT :
                return "Вы купили Гермионе в подарок суперкороткую школьную миниюбку и уговорили носить на занятиях. Нет слов, чтобы это описать."
            elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER :
                return "Вы купили Гермионе в подарок юбку болельщицы Гриффиндора и уговорили носить на занятиях. Раз-два, три-четыре. Юбки выше, колени шире. Или там было по-другому ?"
            elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_BUSINESS :
                return "Вы купили Гермионе в подарок юбку бизнес-леди и уговорили носить на занятиях. Страшно представить, в чем заключается этот бизнес."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART02 :
                return "Вы уговорили Гермиону ходить на занятия без жилетки. Только не думайте, что теперь вас ждет карьера дипломата."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART03 :
                return "Вы уговорили Гермиону ходить на занятия без жилетки и галстука. Пока что ничего выдающегося."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART04 :
                return "Вы уговорили Гермиону ходить на занятия без жилетки и галстука, да еще и расстегнуть верхнюю пуговичку. Совсем неплохо !"
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART05 :
                return "Вы уговорили Гермиону расстегнуть все пуговицы на рубашке, кроме самых важных. Пора подумать о публичных ораторских выступлениях."
            elif iIndex == const_ACH_WRD_HERMIONA_SKIMPYSHIRT :
                return "Вы уговорили Гермиону ходить на занятия в маленьком клочке ткани, называемом рубашка минитопик. Но не нужно гордиться... Ладно ! Вы {size=+2}можете{/size} гордиться !"
            elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER :
                return "Вы подарили Гермионе кофту болельщицы Гриффиндора и уговорили ходить в ней на занятия. Дафна Гринграсс была в ярости."
            elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_BUSINESS :
                return "Вы подарили Гермионе рубашку бизнесс-леди. Осталось придумать соответствующий бизнес."
            elif iIndex == const_ACH_WRD_HERMIONA_NETS :
                return "Вы убедили Гермиону носить сетчатые чулки. И немало рыбки попадется в эти сети..."
            elif iIndex == const_ACH_WRD_HERMIONA_TIGHTS :
                return "Вы убедили Гермиону носить колготки. Зачем ?"
            
            elif iIndex == const_ACH_WRD_HERMIONA_ST_ALL :
                return "Вы убедили Гермиону носить все виды школьной одежды ! Теперь вам не нужен пластмассовый маникен."                
            
            elif iIndex == const_ACH_EASTEREGGS_PHOENIX :
                return "Ваша природная любовь и сострадание к животным дали неожиданный результат. Потому что добро должно размнож... побеждать."
            elif iIndex == const_ACH_EASTEREGGS_PHOENIXSCENE :
                return "Вам удалось увидеть старую сцену времен Акабура под новым углом. С очередной найденной пасхалкой вас!"
            return "Ошибка: незаданное описание"
        
        
        def DispDescription ( self, iIndex=0 ):
            if iIndex == 0:
                iIndex = self.choice
            if iIndex == 0:
                return "Ошибка : нулевой индекс."
            if self.Values[iIndex]==True:
                return self.DescriptionTxt ( iIndex )
            else :
                return "Данное достижение еще не достигнуто. А ведь оно доступно где-то в игре... Терпеливо ждет своего часа..."
        
        
        def DispName ( self, iIndex=0 ):
            if iIndex == 0:
                iIndex = self.choice
            if self.Values[iIndex]==True:
                return self.Name ( iIndex )
            else :
                return "{color=#858585}- Скрыто -{/color}"
        
        
        def UpdatePersistent ( self ):
            if persistent.achieve is None:
                persistent.achieve = set()
            for i in self.Indexes :
                if self.Values[i] == True:
                    persistent.achieve.update({i});
        
        
        def LoadPersistent ( self ):
            for i in self.Indexes :
                self.Values[i] = False
            if persistent.achieve is None:
                persistent.achieve = set()
            for i in persistent.achieve :
                self.Values[i] = True
            
            if persistent.endings == None :
                persistent.endings = set ()
            for i in self.iEndings :
                if i in persistent.endings :
                    self.Endings[i] = True
        
        
        def ShowList ( self , escLabel = None, retLabel = None, iBlock = 1):
            
            Achievement.current = self
            self.esc = escLabel
            self.ret = retLabel
            self.block = iBlock
            
            renpy.call_screen(Achievement.screen)
            
            return
        
        def SetCurrentMenuItem(self, iIndex = 0):
            self.choice=iIndex
            
            return
        
        def IsEnding ( self, ind ):
            if ind < 1 or ind > 3 :
                return False
            return self.Endings[ind]      


screen achieves_disp:
    add "03_hp/11_misc/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign 0.5

        has vbox:
            style "menu"
            spacing 2

        for i in Achievement.current.Indexes:
            if i >= (Achievement.current.block * 100) and i < (Achievement.current.block * 100 + 100):

                button:

                    action [Function(Achievement.current.SetCurrentMenuItem, iIndex=i), Jump(Achievement.current.ret) if Achievement.current.ret !=None else Return()]
                    style "menu_choice_button"

                    text Achievement.current.DispName(i) style "menu_choice"
        if Achievement.current.esc!=None:
            button:
                action [Jump(Achievement.current.esc)]
                style "menu_choice_button"

                text "Назад" style "menu_choice"



    zorder 7
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
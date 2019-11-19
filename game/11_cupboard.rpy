label cupboard:
    $ menu_x = 0.5

    menu:
        "- Осмотреть шкаф -" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_02 
            hide screen genie
            $ tt_xpos=-20
            $ tt_ypos=100
            show screen genie_stands_f
            show screen desk
            with Dissolve(0.5)
            m "Хм....."
            m "Шкаф..."
            m "Я думаю, в нем есть что-то полезное..."
            m "Может порыться в нем чуть позже..."
            show screen genie
            hide screen genie_stands_f
            hide screen chair_02 
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu



        "- Рыться в шкафу -" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}- Рыться в шкафу -{/color}" if searched and not day == 1:
            call already_did
            jump cupboard
        "- Вещи -" if not day == 1:
            label possessions:
                menu:
                    "- Ваши вещи -":
                        $ choose = RunMenu()
                        python:
                            for o in hero.Items():
                                if not o.GetValue("block") in ["gears_shirt", "gears_skirt", "gears_stockings", "gears_other", "gears_dress"] :
                                    choose.AddItem("- "+tr(o._caption)+" ("+str(hero.Items.Count(o.Name))+") -", "menu_cupboard_description" , o.Name)

                        $ choose.Show("cupboard")

                    "- Одежда для подарков -" if day>4:
                        label wrd_clother_cup:
                            menu:
                                "- Юбки -":
                                    $ choose = RunMenu()
                                    python:
                                        for o in hero.Items():
                                            if o.GetValue("block") == "gears_skirt" :
                                                choose.AddItem("- "+tr(o._caption)+" ("+str(hero.Items.Count(o.Name))+") -", "menu_cupboard_description_wrd" , o.Name)

                                    $ choose.Show("wrd_clother_cup")
                                "- Верх -":

                                    $ choose = RunMenu()
                                    python:
                                        for o in hero.Items():
                                            if o.GetValue("block") == "gears_shirt" :
                                                choose.AddItem("- "+tr(o._caption)+" ("+str(hero.Items.Count(o.Name))+") -", "menu_cupboard_description_wrd" , o.Name)

                                    $ choose.Show("wrd_clother_cup")
                                "- Чулки/Колготки -":

                                    $ choose = RunMenu()
                                    python:
                                        for o in hero.Items():
                                            if o.GetValue("block") == "gears_stockings" :
                                                choose.AddItem("- "+tr(o._caption)+" ("+str(hero.Items.Count(o.Name))+") -", "menu_cupboard_description_wrd" , o.Name)

                                    $ choose.Show("wrd_clother_cup")
                                "- Платья-":

                                    $ choose = RunMenu()
                                    python:
                                        for o in hero.Items():
                                            if o.GetValue("block") == "gears_dress" :
                                                choose.AddItem("- "+tr(o._caption)+" ("+str(hero.Items.Count(o.Name))+") -", "menu_cupboard_description_wrd" , o.Name)

                                    $ choose.Show("wrd_clother_cup")
                                "- Прочее -":

                                    $ choose = RunMenu()
                                    python:
                                        for o in hero.Items():
                                            if o.GetValue("block") == "gears_other" :
                                                choose.AddItem("- "+tr(o._caption)+" ("+str(hero.Items.Count(o.Name))+") -", "menu_cupboard_description_wrd" , o.Name)

                                    $ choose.Show("wrd_clother_cup")
                                "- Ничего -":

                                    jump possessions

                    "- Вещи напрокат -" if day>4:
                        label wrd_rent_cup:
                            menu:

                                "- Форма веселой школьницы -" if wrd_rent_happy_schoolgirl == 1:
                                    jump wrd_rent_cup

                                "- Форма игривой школьницы -" if wrd_rent_playful_schoolgirl == 1:
                                    jump wrd_rent_cup

                                "- Форма болельщицы Гриффиндора -" if wrd_rent_cheerleader == 1:
                                    jump wrd_rent_cup

                                "- Одежда бизнес-леди -" if wrd_rent_business == 1:
                                    jump wrd_rent_cup
                                "- Ничего -":

                                    jump possessions

                    "- Помощь -" if day>4:
                        jump cheat_help
                    "- Ничего -":

                        jump cupboard

            label menu_cupboard_description:
                $ item=itsDAHR(choose.choice)
                $ the_gift = item._img
                show screen gift
                with d3
                $ renpy.say(none,">" + tr(item._description))
                if item.Name=="perfume":
                    "> Вы пробовали понюхать эти духи при получении, и нашли их отвратительными."
                    "> Но может быть вы ошиблись? Вы прыскаете из пузырька..."
                    "> Какая гадость! Ваше первое впечатление оказалось верным..."
                    $ hero.SetValue("perfumeused", time.stamp)
                hide screen gift
                with d3
                jump possessions

            label menu_cupboard_description_wrd:
                $ item=itsDAHR(choose.choice)
                $ the_gift = item._img
                show screen gift
                with d3
                $ renpy.say(none,">" + tr(item._description))
                hide screen gift
                with d3
                jump wrd_clother_cup

                label cheat_help:
                menu:
                    "Включить ТУРБО-режим" if turbo==1:
                        $ turbo=2
                        "ТУРБО-режим включен. Теперь ваши действия будут приносить вам вдвое больше денег и очков факультету Слизерина.\n Шанс на прочтение дополнительной главы вдвое больше."
                    "Выключить ТУРБО-режим" if turbo==2:
                        $ turbo=1
                        "ТУРБО-режим выключен. Теперь ваши действия будут приносить вам обычное количество денег и очков факультету Слизерина.\n Шанс на прочтение дополнительной главы стандартный."
                    "ЧИТ: +100 очков Слизерину":
                        hide screen points
                        $ slytherin+=100
                        show screen points
                    "ЧИТ: Гермиона не злится на вас":
                        hide screen points
                        $ hermi.liking=0
                        show screen points
                        "Готово можете проверить"
                    "ЧИТ: Дафна не гневается на вас":
                        hide screen points
                        $ daphne.liking=0
                        show screen points
                        "Запрос выполнен"
                    "ЧИТ: +1000 галеонов":





                        hide screen points
                        $ gold+=1000
                        show screen points
                    "ЧИТ: +100000 галеонов":
                        hide screen points
                        $ gold+=100000
                        show screen points
                    "ЧИТ: Гермиона становится более распутной":
                        if hermi.whoring < 24:
                            "Внимание, вы применяете данный чит на свой страх и риск! Возможен дисбаланс игры."
                            hide screen points
                            $ hermi.whoring+=1
                            show screen points
                            "Готово"
                        else:
                            "Распутнее некуда."
                    "ЧИТ: Прочесть все книги":
                        if days_in_delivery2 > 0:
                            "Для данного чита необходимым компонентом является помет совы, а ваша сова, к сожалению, занята доставкой."
                        else:
                            $ nsp_genie_writer=10
                            $ nsp_genie_typographic=6
                            $ nsp_genie_photocamera=4
                            $ imagination = 5
                            $ concentration = 4
                            $ speedwriting = 4
                            $ s_reading_lvl = 3
                            python:
                                for o in this.List :
                                    if (o.GetValue("block") == "books_newsp" or o.GetValue("block") == "books_newsp2" or o.GetValue("block") == "books_edu" or o.GetValue("block") == "books_fict") and o.Name != "nsp_newsp_book_pre" :
                                        o.SetValue("status", o.GetValue("units"))

                            "Готово"
                    "ЧИТ: Разблокировать публичные задания":
                        $ lock_public_favors = False
                        "Готово"
                    "ЧИТ: Получить ваучер на юбку":
                        $ vouchers += 1
                        $ found_dahrs_ticket_once = True
                        "Готово. Не забудьте проверить каталог"
                    "Прохождение":
                        "Прохождение и ответы на частые вопросы можно найти {a=http://forum.sad-crab.com/forum/main-forum/темы/63-последняя-версия-прохождение-ответы-на-самые-частые-вопросы-история-изменений}ЗДЕСЬ{/a}. "
                    "- Ничего -":

                        jump cupboard
                jump cheat_help



        "- Священные свитки. -" if not day == 1 and cataloug_found:
            label sc_col_men_1:
                $ _scrollSection=0
                jump sc_col_13























                label sc_col:
                    $ choose = RunMenu()
                    python:
                        _itemCount=hero.Items.Count("scroll")
                        for i in range(_scrollSection*15, _scrollSection*15+15):
                            if i<_itemCount:
                                choose.AddItem("- C."+str(i+1)+": Священный свиток #"+str(i+1)+" -", "menu_cupboard_scroll_show" , i)
                    $ choose.Show("cupboard")

                label sc_col_part:
                    $ choose = RunMenu()
                    python:
                        _itemCount=hero.Items.Count("scroll")
                        for i in range(_scrollSection*15, _scrollSection*15+8):
                            if i<_itemCount:
                                choose.AddItem("- C."+str(i+1)+": Священный свиток #"+str(i+1)+" -", "menu_cupboard_scroll_show" , i)
                    $ choose.Show("cupboard")

                label sc_col_13:
                    $ choose = RunMenu()
                    python:
                        _itemCount=hero.Items.Count("scroll")
                        for i in range(_scrollSection*15, _scrollSection*15+13):
                            if i<_itemCount:
                                choose.AddItem("- C."+str(i+1)+": Священный свиток #"+str(i+1)+" -", "menu_cupboard_scroll_show" , i)
                    $ choose.Show("cupboard")

                label menu_cupboard_scroll_show:

                    $ the_gift = "03_hp/19_extras/"+str(choose.choice+1).zfill(2)+".png"

                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump expression "sc_col_men_"+str((choose.choice)//15+1)
        "- Ничего -":

            jump day_main_menu

label rummaging:

    $ searched = True

    $ rum_times += 1

    hide screen cupboard
    hide screen genie
    show screen rum_screen
    with Dissolve(0.3)
    show screen bld1
    with d3
    ">Вы роетесь в шкафу..."

    if day <= 4:
        if rum_times == 2 or rum_times == 3:
            $ renpy.play('sounds/win2.mp3')
            $ potions += 1
            $ the_gift = "03_hp/18_store/32.png"
            show screen gift
            with d3
            ">Вы нашли какое-то зелье..."
            hide screen gift
            with d3
            show screen cupboard
            show screen genie
            hide screen rum_screen

            hide screen bld1
            with d3

            if daytime:
                jump night_start
            else:
                jump day_start

    if rum_times == 15 and not cataloug_found:
        $ renpy.play('sounds/win2.mp3')
        $ cataloug_found = True
        $ the_gift = "03_hp/18_store/dahr2.png"
        show screen gift
        with d3
        ">Вы нашли каталог \"Приблуды Дахра\"... \n>Теперь вы можете использовать каталог для заказа товаров с помощью совы."
        hide screen gift
        with d3
        show screen cupboard
        show screen genie
        hide screen rum_screen

        hide screen bld1
        with d3

        if daytime:
            jump night_start
        else:
            jump day_start


    if i_of_iv == 4:
        $ arrProb={"candy":[2,2,2,0], "wine": [7,5,4,0], "chocolate":[1,1,0,4], "lingere":[1,1,0,1], "sexdoll":[1,1,1,1],
        "krum":[0,1,1,1],"owl":[0,0,4,4], "broom":[0,0,0,1]}

        $ _level=GetStage(hermi.whoring, 0, 4, 6)-1
        $ _randValue=one_of_tw
        $ debug.SaveString(str(_randValue))
        $ _name="gold"
        python:
            for o in arrProb:
                _randValue-=arrProb[o][_level]
                if _randValue<=0:
                    _name=o

        $ debug.SaveString(_name)
        $ renpy.play('sounds/win2.mp3')
        if _name=="gold":
            $ _gold=[gold1,gold2,gold3,gold4][_level]
            hide screen points
            $ gold+=_gold
            show screen points
            $ the_gift="03_hp/18_store/28.png"

            $ _caption=tr("Мешочек с ") +str(_gold)+ tr(" галеонами")
        else:
            $ item=hero.Items.AddItem(_name)
            $ the_gift=item._img
            $ _caption=tr(item._caption)

        $ screens.ShowD3("gift").Say(">Вы нашли предмет: \"[_caption]!\"").HideD3("gift")


    elif i_of_iv == 3:
        $ item=hero.Items.AddItem("wine")
        $ the_gift=item._img

        $ screens.ShowD3("gift").Say(">Вы нашли предмет: \"Вино Дамблдора\"").HideD3("gift")
    else:

        ">...Вы не нашли ничего ценного."



    show screen cupboard
    show screen genie
    hide screen rum_screen

    hide screen bld1
    with d3

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu








label already_did:
    show screen bld1
    with d3
    m "Я сегодня уже рылся в шкафу..."
    hide screen bld1
    with d3
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
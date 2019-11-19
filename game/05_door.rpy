label door:

    if daphne.lastVisitDay == None:
        $ daphne.lastVisitDay = 0

    menu:
        "- Исследовать дверь -" if not door_examined:
            $ door_examined = True
            hide screen genie
            $ tt_xpos=550
            $ tt_ypos=110
            show screen genie_stands
            show screen chair_02 
            show screen desk
            with Dissolve(0.5)
            m "Выглядит надежно..."
            m "Интересно, что за ней."
            label examining_the_door:
            menu:
                "- Постучать в дверь -":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/knocking.mp3')
                    "*Тук-тук-тук*"
                    "..................."
                    hide screen blktone8
                    with d3
                    m "Не отвечают..."
                    jump examining_the_door
                "- Прислонить к ней ухо -":
                    show screen blktone8
                    with d3
                    ">Вы прикладываете ухо и внимательно слушаете..."
                    m "Я ничего не слышу."
                    hide screen blktone8
                    with d3
                    jump examining_the_door
                "- Ударить дверь -":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/kick.ogg')
                    pause.2
                    with hpunch
                    "*Удар!*"
                    ".............................."
                    hide screen blktone8
                    with d3
                    m "Эта дверь выдержит тысячу ударов и не сломается..."
                    m "Xотя и не выглядит запертой..."
                    jump examining_the_door
                "- Оставить в покое -":
                    m "Кто знает, какие опасности могут скрываться за этой дверью?"
                    m "Я думаю мне стоит оставить её в покое..."
                    pass
            show screen genie
            hide screen genie_stands
            hide screen chair_02 
            hide screen desk
            with Dissolve(0.2)
            jump day_main_menu




        "{color=#858585}- Позвать Гермиону -{/color}" if this.Has("her_summon")  and hermione_takes_classes or hermione_sleeping or hermione_out_halfday > 0:
            if hermione_takes_classes:
                show screen bld1
                with d3
                ">Гермиона сейчас на уроке."
                hide screen bld1
                with d3
                jump day_main_menu
            elif hermione_sleeping:
                show screen bld1
                with d3
                ">Гермиона уже спит."
                hide screen bld1
                with d3
                jump night_main_menu
            elif hermione_out_halfday > 0:
                show screen bld1
                with d3
                ">Гермиона сейчас находится вне пределов Хогвартса."
                hide screen bld1
                with d3
                if daytime:
                    jump day_main_menu
                else:
                    jump night_main_menu

        "- Позвать Гермиону -" if this.Has("her_summon") and not hermione_takes_classes and not hermione_sleeping and hermione_out_halfday <= 0:

            if hermione_takes_classes:
                show screen bld1
                with d3
                ">Гермиона сейчас на уроке."
                hide screen bld1
                with d3
                jump day_main_menu
            elif hermione_sleeping:
                show screen bld1
                with d3
                ">Гермиона уже спит."
                hide screen bld1
                with d3
                jump night_main_menu
            else:


                hide screen desk_02

                if hermi.whoring >= 13 and one_out_of_three == 2 and luna_stage <= 2:
                    call accident

                jump hermione_approaching

        "{color=#858585}- Позвать Снейпа -{/color}" if this.Has("snape_summon") and snape_busy:
            ">Профессор Снейп недоступен."
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu

        "- Позвать Снейпа -" if this.Has("snape_summon") and not snape_busy:
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
            jump summon_snape

        "{color=#858585}- Позвать Дафну -{/color}" if this.Has("daphne_pre_finish") and ((day - daphne.lastVisitDay)*24 - daphne._visitInterval < 0):
            $ screens.ShowD3("bld1")
            if day != daphne.lastVisitDay:
                "> У вас соглашение с Гермионой - вы не можете вызывать Дафну чаще, чем раз в [daphne._visitInterval] часов."
            else:
                if daytime:
                    $ renpy.say(none,tr("Дафна сейчас на уроке."))
                else:
                    $ renpy.say(none,tr("Дафна уже спит."))
                pass
            $ screens.HideD3("bld1")
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu


        "- Позвать Дафну -" if this.Has("daphne_pre_finish") and ((day - daphne.lastVisitDay)*24 - daphne._visitInterval >= 0):
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
            hide screen desk_02
            $ daphne.SetValue("lastVisitDay", day);
            jump daphne_approaching
        "- Ничего -":


            jump day_main_menu








label request_01:
    "Гермиона смотрит на вас с интересом и краснеет."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
    $ gryffindor +=5
    "Гриффиндор получает 5 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



label request_02:
    "Сильно краснея и неохотно Гермиона поднимает юбку и показывает вам свои трусики."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
    $ gryffindor +=5
    "Гриффиндор получает 5 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



label request_02_b:
    "Гермиона соглашается попытаться заигрывать с 3 одноклассниками."
    "Вы провожаете Гермиону."
    $ request_02_b = True
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
    $ gryffindor +=5
    "Гриффиндор получает 5 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

label request_02_b_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам о парнях с которыми флиртовала."
    $ request_02_b = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду в кровать."
    return


label request_02_c:
    "Гермиона соглашается попробовать флиртовать с учителем."
    "Вы провожаете Гермиону."
    $ request_02_c = True
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
    $ gryffindor +=5
    "Гриффиндор получает 5 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

label request_02_c_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам о флирте с ее учителем."
    $ request_02_c = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return





label request_03:
    if hermi.whoring <=2:
        jump too_much

    if hermi.whoring >= 3:
        "Гермиона нерешительно стягивает свои трусики и дает их вам."
        "Вы провожаете Гермиону."
        $ request_03 = True
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        $ hermione_takes_classes = True
        "Гриффиндор получает 15 очков."
        jump day_main_menu

label request_03_complete:
    "Гермиона возвращается с занятий. Вы отдаете ей трусики обратно."
    $ request_03 = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return



label request_04:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3:
        "Гермиона позволяет поласкать ее грудь."
        "Вы провожаете Гермиону."
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        "Гриффиндор получает 15 очков."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu


label request_05:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3:
        "Гермиона позволяет поласкать ее попку."
        "Вы провожаете Гермиону."
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        "Гриффиндор получает 15 очков."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu


label request_06:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3:
        "Гермиона соглашается попробовать \"посветить\" своими трусиками перед одноклассником."
        "Вы провожаете Гермиону."
        $ request_05 = True
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        "Гриффиндор получает 15 очков."
        $ hermione_takes_classes = True
        jump day_main_menu

label request_05_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам о своих попытках \"посветить\" своими трусиками перед одноклассником."
    $ request_05 = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return



label request_07:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3:
        "Гермиона соглашается попробовать \"посветить\" своими трусиками перед учителем."
        "Вы провожаете Гермиону."
        $ request_06 = True
        if hermi.whoring <= 5:
            $ hermi.whoring +=1
        $ gryffindor +=15
        "Гриффиндор получает 15 очков."
        $ hermione_takes_classes = True
        jump day_main_menu


label request_06_complete:
    "Гермиона возвращается с занятий и рассказывает о своих попытках \"посветить\" своими трусиками перед учителем."
    $ request_06 = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return




label request_08:
    if hermi.whoring <=5:
        jump too_much
    "Гермиона показывает вам свою грудь."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 8:
        $ hermi.whoring +=1
    $ gryffindor +=25
    "Гриффиндор получает 25 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_09:
    if hermi.whoring <=5:
        jump too_much
    "Гермиона показывает вам свою киску."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 8:
        $ hermi.whoring +=1
    $ gryffindor +=25
    "Гриффиндор получает 25 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_10:
    if hermi.whoring <=5:
        jump too_much
    "Гермиона соглашается попробовать показать свои соски однокласснику."
    "Вы провожаете Гермиону."
    $ request_10 = True
    if hermi.whoring <= 8:
        $ hermi.whoring +=1
    $ gryffindor +=25
    $ hermione_takes_classes = True
    "Гриффиндор получает 25 очков."
    jump day_main_menu

label request_10_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она мелькнула своими сосками перед одноклассником."
    $ request_10 = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return




label request_11:
    if hermi.whoring <=8:
        jump too_much
    "Гермиона раздевается перед вами, а затем откладывает одежду назад."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 11:
        $ hermi.whoring +=1
    $ gryffindor +=35
    "Гриффиндор получает 35 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_12:
    if hermi.whoring <=8:
        jump too_much
    "Гермиона обнажает свою грудь. Вы немного играете с ними."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 11:
        $ hermi.whoring +=1
    $ gryffindor +=35
    "Гриффиндор получает 35 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_13:
    if hermi.whoring <=8:
        jump too_much
    "Гермиона соглашается надеть прозрачную рубашку и пойти в класс."
    "Вы провожаете Гермиону."
    $ request_13 = True
    if hermi.whoring <= 11:
        $ hermi.whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "Гриффиндор получает 35 очков."
    jump day_main_menu

label request_13_complete:
    "Гермиона возвращается с занятий и рассказывает вам, как все пялились на ее грудь."
    $ request_13 = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return


label request_15:
    if hermi.whoring <=8:
        jump too_much
    "Гермиона соглашается попробовать \"посветить\" сосками перед учителем."
    "Вы провожаете Гермиону."
    $ request_15 = True
    if hermi.whoring <= 11:
        $ hermi.whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "Гриффиндор получает 35 очков."
    jump day_main_menu

label request_15_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она \"светила\" сосками перед учителем.."
    $ request_15 = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return




label request_16:
    if hermi.whoring <=11:
        jump too_much
    "Гермиона позволяет пощупать ее киску."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    "Гриффиндор получает 45 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_17:
    if hermi.whoring <=11:
        jump too_much
    "Гермиона позволяет поводить палецем у входа в ее попку."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    "Гриффиндор получает 45 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



label request_18:
    if hermi.whoring <=11:
        jump too_much
    "Гермиона дрочит вам."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    "Гриффиндор получает 45 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_19:
    if hermi.whoring <=11:
        jump too_much
    "Гермиона сидит на месте, пока вы трете свой член о ее личико."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    "Гриффиндор получает 45 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_20:
    if hermi.whoring <=11:
        jump too_much
    "Гермиона соглашается попробовать cхватить одноклассника за член."
    "Вы провожаете Гермиону."
    $ request_20 = True
    if hermi.whoring <= 14:
        $ hermi.whoring +=1
    $ gryffindor +=45
    $ hermione_takes_classes = True
    "Гриффиндор получает 45 очков."
    jump day_main_menu

label request_20_complete:
    "Гермиона возвращается с занятий и рассказывает вам, как она схватила член одного из своих одноклассников."
    $ request_20 = False
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return




label request_21:
    if hermi.whoring <=14:
        jump too_much
    "Гермиона обнажает свою грудь. Вы дрочите и кончая, заливаете спермой ее прелестные сиськи."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 17:
        $ hermi.whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Гриффиндор получает 55 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_22:
    if hermi.whoring <=14:
        jump too_much
    "Гермиона делает вам минет."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 17:
        $ hermi.whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Гриффиндор получает 55 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_23:
    if hermi.whoring <=14:
        jump too_much
    "Гермиона соглашается попробовать подрочить однокласснику."
    "Вы провожаете Гермиону."
    $ request_23 = True
    if hermi.whoring <= 17:
        $ hermi.whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Гриффиндор получает 55 очков."
    jump day_main_menu

label request_23_complete:
    "Гермиона возвращается с занятий и рассказывает вам, как дрочила одному из своих одноклассников во время урока."
    $ request_23 = False
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return


label request_24:
    if hermi.whoring <=14:
        jump too_much
    "Гермиона соглашается попробовать и \"посветить\" грудью перед учителем."
    "Вы провожаете Гермиону."
    $ request_24 = True
    if hermi.whoring <= 17:
        $ hermi.whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Гриффиндор получает 55 очков."
    jump day_main_menu

label request_24_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она \"светила\" сиськами перед учителем."
    $ request_24 = False
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return


label request_25:
    if hermi.whoring <=17:
        jump too_much
    "Гермиона сидит на месте, пока вы дрочите на ее лицо."
    "Вы провожаете Гермиону."
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Гриффиндор получает 65 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_26:
    if hermi.whoring <=17:
        jump too_much

    "Гермиона сидит с открытым ртом, пока вы дрочите и кончаете в него. Вы запретили ей глотать, до того, как она попадет в класс."
    "Вы провожаете Гермиону с полным ртом своей спермы."

    $ request_26 = True
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Гриффиндор получает 65 очков."
    jump day_main_menu

label request_26_complete:
    "Гермиона возвращается с занятий и рассказывает вам, что не могла говорить с одноклассниками, потому что ее рот был заполнен вашей спермой."
    $ request_26 = False
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return


label request_27:
    if hermi.whoring <=17:
        jump too_much
    "Гермиона соглашается попробовать отсосать двум одноклассникам во время занятий."
    "Вы провожаете Гермиону."
    $ request_27 = True
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Гриффиндор получает 65 очков."
    jump day_main_menu

label request_27_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она сосала двум одноклассникам во время занятий."
    $ request_27 = False
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return


label request_28:
    if hermi.whoring <=17:
        jump too_much
    "Гермиона соглашается попробовать и подрочить учителю во время занятий."
    "Вы провожаете Гермиону."
    $ request_28 = True
    if hermi.whoring <= 20:
        $ hermi.whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Гриффиндор получает 65 очков."
    jump day_main_menu

label request_28_complete:
    "Гермиона возвращается с занятий и рассказывает вам, как она мастурбировала учителю во время занятий."
    $ request_28 = False
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return




label request_29:
    if hermi.whoring <=20:
        jump too_much
    if daytime:
        "Вы занимаетесь сексом с Гермионой, после чего отправляете ее на занятия."
    else:
        "Вы занимаетесь сексом с Гермионой."
        "Вы провожаете Гермиону."
    if hermi.whoring <= 23:
        $ hermi.whoring +=1
    $ gryffindor +=75
    "Гриффиндор получает 75 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


label request_30:
    if hermi.whoring <=20:
        jump too_much
    "Гермиона соглашается попробовать и сосет у учителя."
    "Вы провожаете Гермиону."
    $ request_30 = True
    if hermi.whoring <= 23:
        $ hermi.whoring +=1
    $ gryffindor +=75
    $ hermione_takes_classes = True
    "Гриффиндор получает 75 очков."
    jump day_main_menu

label request_30_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она делала минет учителю во время занятий."
    $ request_30 = False
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return




label request_31:
    if hermi.whoring <=23:
        jump too_much
    "Вы занимаетесь анальным сексом с Гермионой"
    "Вы провожаете Гермиону."
    if hermi.whoring <= 26:
        $ hermi.whoring +=1
    $ gryffindor +=85
    "Гриффиндор получает 85 очков."
    $ hermione_sleeping = True
    jump day_start





label request_32:
    if hermi.whoring <=26:
        jump too_much
    "Гермиона надевает очень распутный наряд и идет на занятия."
    $ request_32 = True
    if hermi.whoring <= 29:
        $ hermi.whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "Гриффиндор получает 100 очков."
    jump day_main_menu

label request_32_complete:
    "Гермиона возвращается с занятий и говорит, что люди относились к ней как к шлюхе."
    $ request_32 = False
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return


label request_33:
    if hermi.whoring <=26:
        jump too_much
    "Вы кончаете на лицо Гермионы и отправляете ее на занятия."
    $ request_33 = True
    if hermi.whoring <= 29:
        $ hermi.whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "Гриффиндор получает 100 очков."
    jump day_main_menu

label request_33_complete:
    "Гермиона возвращается с занятий и говорит, что люди относились к ней, как потаскухе и смеялись над ней."
    $ request_33 = False
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return






label too_much:
    if IsEventOnlyAfter("new_personal_request"):
        $ wtevent.NotFinished()
    stop music fadeout 2.0
    $ herView.hideQQ()
    $ pos = POS_120
    $ herView.showQQ( "body_48.png", pos )
    her "Профессор Дамблдор??!"
    her "Как вы можете просить меня о таком!?"
    $ herView.hideQQ()
    $ herView.showQQ( "body_34.png", pos )
    her "По-моему, мне лучше уйти."

    hide screen blktone
    hide screen bld1
    $ herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400
    $ walk_xpos2=610
    $ hermione_speed = 02.0
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ hermione_chibi_xpos = 610
    with Dissolve(.3)

    hide screen hermione_01_f 
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3')
    with Dissolve(.3)
    pause.5

    $ hermi.liking -= 7


    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 


    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
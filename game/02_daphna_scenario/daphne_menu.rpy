

label daphne_approaching(isKnocking=False):




    $ renpy.play('sounds/door.mp3')







    $ this.RunStep("DAPHENTER")

    $ daphne.chibi.State("center").Trans(d4, "blink")

    if dap_ending == 1:
        call dap_preoutro_1
        jump daphne_goout
    elif dap_ending == 2:
        call dap_preoutro_2
        jump daphne_goout

    $ daphne.Visibility("body+", False)

    python:
        for t in [
            (0, ["daphne:> ~55 00 1 def// Да, профессор?"]),
            (-2, [">Похоже, Дафна по-прежнему немного расстроена вами..."]),
            (-9, [">Вы расстроили Дафну."]),
            (-19, [">Дафна очень расстроена вами."]),
            (-39, [">Дафна злится на вас."]),
            (-49, [">Дафна очень злится на вас."]),
            (-59, [">Дафна гневается на вас."]),
            (-100, [">Дафна ненавидит вас."])
            ]:
            (_val, _texts)=t
            if daphne.liking>=_val:
                for s in _texts:
                    Say(tr(s))
                break



    label daphne_main_menu:
    menu:
        "- Поговорить -" if not daphne.IsTalk():
            $ daphne.CommitTalk()
            if daphne.liking >= -7:
                jump daphne_chat
            else:
                $ daphne("Мне нечего сказать вам...")
                jump daphne_main_menu

        "- Тренировка -" if this.daphne_pre_finish.IsFinished():
            if daphne.liking<0:
                python:
                    for t in [
                        (-2, "Мне жаль, профессор, может быть в другой раз..."),
                        (-9, "Мне не хочется сегодня...\nМожет быть через пару дней..."),
                        (-19, "Нет, спасибо...."),
                        (-29, "После того, что вы сделали?\nЯ так не думаю..."),
                        (-39, "Вы серьезно!?"),
                        (-100, "Это какая-то ваша пошлая шутка?!\nПосле того, что вы сделали, я не хочу повторять это!")
                        ]:
                        (_val, _text)=t
                        if daphne.liking>=_val:
                            daphne(tr(_text))
                            break
                jump daphne_main_menu
            else:
                label daphne_main_menu_requests:

                    $ choose = RunMenu()
                    python:
                        for o in this.List:
                            if o._points!=None:
                                if (("daphne_public" in o._points and daytime) or "daphne_private" in  o._points):
                                    choose.AddItem(str(tr(o._caption) + "{image=hearts/heart_" + str (o._fullHeartCount) + str(o._heartCount) +".png}"), None, o.Name)        
                        choose.Show("daphne_main_menu")

                    $ daphne.Visibility("body+")
                    $ hero(m,this(choose.choice)._eventPlan)
                    menu:
                        "\"(Да, сделаем это.)\"":
                            if this(choose.choice)._finishCount>=6:
                                pause 1.0
                                dev "Жаль прерываться на самом интересном месте?"
                                dev "Нам тоже. Но данная сюжетная линия пока дописана только до этой точки..."
                                dev "{size=-3}(впрочем, вам доступны другие сюжетные линии){/size}"
                                dev "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://forum.sad-crab.com}ФОРУМЕ{/a}."
                                dev "Так вы простимулируете нас и продолжение появится быстрее. :)"
                                jump daphne_main_menu_requests

                            call expression this(choose.choice).Name
                        "\"(Не сейчас.)\"":
                            jump daphne_main_menu_requests

                    if not wtevent.Name in {"dap_request_01", "IsRunNumber(4)", "dap_request_03", "dap_request_05_complete"}:
                        call daphne_pre_menu (_return)
                    else:
                        $ screens.HideD3("bld1")
                        $ daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)
                        $ renpy.play('sounds/door.mp3')
                        pause.5
                        call music_block

                    if wtevent._scenario==None:
                        $ wtevent.Finalize("day_main_menu" if daytime else "night_main_menu")
                    else:
                        $ wtevent.Finalize("night_start" if daytime else "day_start")





        "- Дать ей подарок -" if not daphne.IsGift():

            menu:
                "- Подарки -":


                    $ choose = RunMenu()
                    python:
                        for o in hero.Items():
                            if not o.Name in {"scroll", "ball_dress"} and not o.GetValue("block") in ["gears_shirt", "gears_skirt", "gears_stockings", "gears_other", "gears_dress"]:
                                choose.AddItem("- "+tr(o._caption)+" -", 
                                    "daphne_giving" , o.Name)

                    $ choose.Show("daphne_main_menu")
                "- Одежда -":


                    $ choose = RunMenu()
                    python:
                        for o in hero.Items():
                            if not o.Name in {"scroll", "ball_dress"} and o.GetValue("block") in ["gears_shirt", "gears_skirt", "gears_stockings", "gears_other", "gears_dress"]:
                                choose.AddItem("- "+tr(o._caption)+" -", 
                                    "daphne_giving" , o.Name)

                    $ choose.Show("daphne_main_menu")
        "- Попросить уйти -":





































            $ menu_x = 0.5

            if daphne.liking>=-2:
                $ daphne(["О, хорошо! Тогда я пойду на уроки.", "О, хорошо! Тогда я пойду спать."][0 if daytime else 1])
            elif daphne.liking >= -6:
                $ daphne("...............................")
            else:
                $ daphne(["*Гм!*...", "Пф!..."][0 if daytime else 1])


            label daphne_goout:







            $ daphne.Visibility()
            $ daphne.chibi.Hide()
            $ screens.Hide("bld1", "blktone", d3, "ctc")

            if daytime:

                jump day_main_menu
            else:

                jump night_main_menu




label dap_chibi_load:
    if daphne.chibi.State(appearance="a"):

        $ daphne.ItemsCustomize(update={"combi:daphne_combi_handsonhip"})
        $ daphne.ItemsCustomize(update={"skirt:daphne_skirt"})

    elif daphne.chibi.State(appearance="g") and daphne.ItemsCustomize(update={"combi:daphne_combi_handsonhip"}) and daphne.ItemsCustomize(update={"skirt:daphne_skirt"}):

        $ daphne.ItemsCustomize(delete={"combi:daphne_combi_handsonhip"})
        $ daphne.ItemsCustomize(delete={"skirt:daphne_skirt"})

return


label daphne_chat:
    if this.IsStep("DAPHNECHAT"):
        $ this.RunStep("DAPHNECHAT")
    else:
        $ daphne("~55 00 1 def")
        if daphne.whoring in {0,1,2,3,4,5,6,7,8,9,10,11,12}:
            $ daphne([
            "~46 00 1 ope// Мугродью - бой!// Вот что должно быть заповедью каждого настоящего волшебника!",
            "~37 00 1 pri// Сегодня грязнокровка Грейнджер опять получила высший балл. Куда смотрит министерство?!//"
                "~37 01 1 pri// Так скоро среди дипломированных волшебников не останется ни одного чистокровного.",
            "~55 00 1 smi// Сегодня \"Чистокровные вести\" опубликовали список чистокровных волшебников Англии. Гринграссы - в первой дюжине!//"
                "~55 00 1 gri// Вы там тоже есть - на предпоследней строчке.",
            "~55 00 1 ehh// Мама говорит, что я смогу раскрыть свои настоящие таланты, только если займу правильную позицию. Вы тоже так думаете?",
            "~55 00 1 pou// Моя сова Пухля опять обожралась птичьим кормом и теперь не может никуда лететь.//"
                "~55 00 1 smi// Но я ее ни за что не променяю на другую.//"
                "~55 c0 1 smo// Она тоже очень чистокровная!"
            ][Rand(5)-1])
        elif daphne.whoring in {13,14,15,16,17,18,19,20,21,22,23,24}:
            $ daphne([
            "~64 00 1 dis// Конкурс приближается, и я места себе не нахожу. Иногда мне хочется выпить, чтобы немного расслабиться...//"
                "~55 01 2 ehh// Ой, простите, профессор, сорвалось. Я совсем не это имела в виду!",
            "~64 00 1 def// Сегодня какой-то полукровка заговорил со мной.//~64 00 1 dis// Мне даже показалось, что он пытался меня клеить.//"
                "~55 00 1 pri// Ну и самомнение у некоторых!",
            "~55 00 1 def// Этот призрак - Пивз, ну, знаете его, сегодня по секрету рассказал мне что тоже из какого-то древнего рода.//"
                "И представляете, он был очень убедителен.//~55 00 1 neu// Странно - обычно он так себя не ведет.",
            "~37 00 1 pur// Я надеюсь, что с вашей помощью профессор, я утру нос всем этим худородным, полукровкам и конечно же, мугродью.",
            "~55 00 1 def// Сегодня был матч и я исполняла танец чирлидера со всем присущим мне изяществом.//"
                "~37 n2 2 def// Некоторые парни так пялились на меня...// ~37 00 2 pou// Но мне это совсем не нужно, сэр!"
            ][Rand(5)-1])



    jump daphne_main_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
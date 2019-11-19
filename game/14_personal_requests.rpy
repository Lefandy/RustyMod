label new_personal_request:
    $ pos = POS_410
    if slytherin > gryffindor or slytherin == gryffindor:
        $ herView.showQ( None, pos )

        $ menu_x = 0.2

        label not_now:
        menu:
            "- Личные услуги -":
                label not_now2:

                menu:
                    "Услуга: [this.new_request_01._caption] {image=heart_4[this.new_request_01._heartCount].png}":








                        jump new_request_01
                    "Услуга: [this.new_request_02._caption] {image=heart_4[this.new_request_02._heartCount].png}":









                        jump new_request_02


                    "{color=#858585}--Не открытое действие-{/color} -" if imagination == 1:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_03._caption] {image=heart_4[this.new_request_03._heartCount].png}" if daytime and imagination >= 2:
                        jump new_request_03



                    "{color=#858585}--Не открытое действие-{/color} -" if imagination == 1:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_04._caption] {image=heart_4[this.new_request_04._heartCount].png}" if imagination >= 2:
                        jump new_request_04

                    "{color=#858585}--Не открытое действие-{/color} -" if imagination == 1:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_05._caption] {image=heart_0[this.new_request_05._heartCount].png}" if imagination >= 2:
                        jump new_request_05


                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_08._caption] {image=heart_4[this.new_request_08._heartCount].png}" if imagination >= 3:
                        jump new_request_08






                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_11._caption] {image=heart_0[this.new_request_11._heartCount].png}" if imagination >= 3:
                        jump new_request_11


                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_12._caption] {image=heart_0[this.new_request_12._heartCount].png}" if imagination >= 3:
                        jump new_request_12



                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 4:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_16._caption] {image=heart_0[this.new_request_16._heartCount].png}" if imagination >= 4:
                        jump new_request_16



                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 4:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_22._caption] {image=heart_0[this.new_request_22._heartCount].png}" if imagination >= 4:
                        jump new_request_22



                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 5:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_29._caption] {image=heart_0[this.new_request_29._heartCount].png}" if imagination >= 5:
                        jump new_request_29


                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 5:
                        call vague_idea
                        jump not_now2








                    "Услуга: [this.new_request_31._caption] {image=heart_0[this.new_request_31._heartCount].png}" if imagination >= 5:
                        jump new_request_31
                    "- Отмена -":


                        jump new_personal_request

            "{color=#858585}-Публичные услуги-{/color}" if not daytime:
                show screen blktone
                $ herView.hideQQ()
                ">Публичные услуги недоступны в это время суток."
                hide screen blktone
                $ herView.showQ( None, pos )
                with d3
                jump not_now
            "- Публичные услуги -" if daytime:
                if lock_public_favors:
                    her "Эм... Сэр..."
                    her "Я согласна обменивать очки за всякие услуги..."
                    her "Но только до тех пор, пока все это между нами, а не на публику..."
                    jump new_personal_request
                else:
                    label not_now3:
                    menu:

                        "Услуга: \"Флиртуй с учеником\"" if daytime:
                            jump new_request_02_b


                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 2:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Флиртуй с учителем\"" if daytime  and imagination >= 2:
                            jump new_request_02_c


                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Дай однокласснику поприставать к тебе.\"" if imagination >= 3:
                            jump new_request_10


                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Посвети сиськами перед одноклассниками.\"" if imagination >= 3:
                            jump new_request_15



                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Поцелуй девченку.\"" if imagination >= 4:
                            jump new_request_20


                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Вздрочни однокласснику.\"" if imagination >= 4:
                            jump new_request_23


                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Отсоси однокласснику\"" if imagination >= 5:
                            jump new_request_24


                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Трахнись с одноклассником\"" if imagination >= 5:
                            jump new_request_30
                        "- Отмена -":

                            jump new_personal_request
            "- Ничего -":


                jump hermione_main_menu
    else:





































































        her "Гриффиндор лидирует. Мне это не нужно сейчас."
        jump hermione_main_menu








label new_request_06:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3:
        m "Я хочу чтобы ты сегодня кое-что сделала в своем классе: покажи трусики одному из своих однокласников."
        if request_06_points == 0:
            her "Oх..."
            "Гермиона неохотно соглашается."
        elif request_06_points == 1:
            her "Если только..."
            "Гермиона согласна."

        elif request_06_points == 2:
            her "Конечно..."
            "Гермиона согласна. Очень охотно."

        elif request_06_points >= 3:
            her "Конечно, профессор."
            ">Гермиона с радостью согласна."


        "Вы отправляете Гермиону."
        $ request_05 = True
        $ hermione_takes_classes = True

        if hermi.whoring <= 5:
            $ hermi.whoring +=1

        if request_05_points <= 2:
            $ gryffindor +=15
            "Гриффиндору +15 очков."
        else:
            $ gryffindor +=5
            "Гриффиндору +5 очков."

        jump day_main_menu

label new_request_05_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел день, Мисс Грейнджер?"
    if request_06_points == 0:
        her "Хм... Я пытался показать свои трусики, чтобы один из моих одноклассников увидел, но вместо этого я думаю, что пять или шесть из них мельком. Так стыдно..."
    elif request_06_points == 1:
        her "Я показала свои трусики одному из одноклассников."
    elif request_06_points == 2:
        her "Я долго показала свои трусики одному из одноклассников ."
    elif request_06_points >= 3:
        her "Мне удалось показать свои трусики так чтобы один из однокласснников глазел на них."
        her "Это было супер!"

    "Вы отпускаете Гермиону."
    $ request_06_points += 1
    $ request_05 = False
    $ hermione_sleeping = True
    her "Ну, ладно. Я пойду спать тогда."
    return



label new_request_07:
    if hermi.whoring <=2:
        jump too_much
    if hermi.whoring >= 3:
        m "Я хочу чтобы ты сегодня кое-что сделала в своем классе: покажи трусики одному из своих учителей."
        if request_07_points == 0:
            her "Oх..."
            "Гермиона неохотно соглашается."

        elif request_07_points == 1:
            her "Если только..."
            "Гермиона согласна."

        elif request_07_points == 2:
            her "Конечно..."
            "Гермиона согласна. Очень охотно."

        elif request_07_points >= 3:
            her "Конечно, профессор."
            ">Гермиона с радостью согласна."


        "Вы отпускаете Гермиону."
        $ request_06 = True
        if hermi.whoring <= 5:
            $ hermi.whoring +=1

        if request_05_points <= 2:
            $ gryffindor +=15
            "Гриффиндор получает +15 очков."
        else:
            $ gryffindor +=5
            "Гриффиндор получает +5 очков."
        $ hermione_takes_classes = True
        jump day_main_menu


label new_request_06_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел день, Мисс Грейнджер?"
    if request_07_points == 0:
        her "Хм... Я пыталась показать свои трусики учителю, чтобы он увидел их, но вместо этого я думаю, что пять или шесть одноклассников из них увидели мельком. Так стыдно..."
    elif request_07_points == 1:
        her "Я показала свои трусики одному из учителей."
    elif request_07_points == 2:
        her "Я долго показала свои трусики одному из учителей."
    elif request_07_points >= 3:
        her "Я долго показала свои трусики одному из учителей."
        her "Это было супер!"

    $ request_07_points += 1
    $ request_06 = False
    $ hermione_sleeping = True
    her "Ну, ладно. Я пойду спать тогда."
    return


label new_request_09:
    $ herView.hideQQ()
    if request_09_points == 0:
        m "{size=-4}(Попросить девочку, показать мне свою киску?){/size}"
    else:
        m "{size=-4}(Попросить девочку, показать мне свою киску еще раз?){/size}"
    $ menu_x = 0.5
    menu:
        "\"(Да, пусть покажет!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request


    if request_09_points == 0 and hermi.whoring <= 11:
        m "Мисс Грейнджер..."
        m "Сегодняшняя награда для факультета \"Гриффиндора\" 25 очков."
        $ herView.hideQQ()
        $ pos = POS_370
        $ herView.showQQ( "body_03.png", pos )
        her "Правда?"
        her "Спасибо,это так много, сэр!"
        m "Да, но мне потребуется ваша помощь..."
        her "Конечно, сэр! Что угодно!"
        m "Поднимите юбку..."
        her "...?"
        m "Спустите трусики..."
        her "?!!"
        m "И покажи свою киску!"
        if hermi.whoring <=5:
            jump too_much
        her "Профессор Дамблдор!"
        her "Это совершенно новый уровень неуместным, даже для вас, сэр!"
        her "Как можно просить такие вещи вашей ученицы?"
        m "Так вот, как тыы себя чувствущь? Я вижу..."
        m "Тогда я думаю, наградить другие дома..."
        m "\"Слизерин\" ?"
        her "................"
        m "Но ты знаешь,..."
        her "Профессор..."
        her "Судьба моего факультета для меня очень важна..."
        m "Неужели?"
        m "Почему тогда ты не покажешь её мне?"
        m "Да. Покажите мне, как это для вас важно, Мисс Грейнджер."
        her "Но это не просто..."
        m "У нас нет времени обсуждать, что уместно, а что нет, Мисс Грейнджер?"
        her ".................."
        m "Я бы сказал, что корабль уплыл..."
        her ".............."
        m "Все, что я хочу сделать, это быстро посмотреть..."
        her "Но почему? Почему я должена делать это, сэр?"
        m "Минуту вашего времени и \"Гриффиндор\" получает 25 очков..."
        m "Очень хорошее сделка, разве вы не согласны?"
        her "Я подумаю..."
    else:
        m "Мисс Грейнджер?"
        her "Да..."
        m "Мне нужно увидеть вашу киску..."
        if hermi.whoring >= 6 and hermi.whoring <= 8:
            her "Aргх... Только не опять, сэр..."
            her "{size=-5}...так стыдно...{/size}"
            m "25 очков, Мисс Грейнджер..."
            her ".............."
        if hermi.whoring >= 9 and hermi.whoring <= 11:
            her "*Вздох*... Если только..."
        if hermi.whoring >= 12 and hermi.whoring <= 14:
            her "Неужели?"
            her "Ну ладно..."














    if hermi.whoring <=5:
        jump too_much































    m "Покажи мне свою киску..."
    if request_09_points == 0:
        her "Oх... "
        ">Гермиона тянет вверх ее юбку и тянет вниз трусики. Она покраснела и выглядит сердитой."

    elif request_09_points == 1:
        her "...Да, профессор."
        ">Гермиона тянет вверх ее юбку и тянет вниз трусики. Она выглядит нетерпеливой."

    elif request_09_points == 2:
        her "Конечно, сэр..."
        ">Гермиона тянет вверх ее юбку и тянет вниз трусики.Она выглядит игривой."

    elif request_09_points >= 3:
        her "Here you go, Headmaster."
        ">Гермиона тянет вверх ее юбку и тянет вниз трусики. Они вам улыбается."

    "Вы отпускаете Гермиону."

    if hermi.whoring <= 8:
        $ hermi.whoring +=1

    if request_09_points <= 2:
        $ gryffindor +=25
        "Гриффиндор получил +25 очков."
    else:
        $ gryffindor +=7
        "Гриффиндор получил +7 очков."

    $ request_09_points += 1

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu










label new_request_17:
    if hermi.whoring <=11:
        jump too_much

    m "Подойди сюда и дай мне засунуть палец в твою попку."
    if request_17_points == 0:
        her "Ох... "
        ">Гермиона неохотно соглашается."
    elif request_17_points == 1:
        her "...Да, профессор."
        ">Гермиона соглашается."
    elif request_17_points == 2:
        ">Гермиона беззаботно соглашается."
    elif request_17_points >= 3:
        her "Вот, профессор."
        ">Гермиона резво соглашается."

    "Вы отпустили Гермиону."

    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    if request_17_points <= 2:
        $ gryffindor +=45
        "Гриффиндор получает 45 очков."
    else:
        $ gryffindor +=11
        "Гриффиндор получает 11 очков."

    $ request_17_points += 1

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



label new_request_18:
    if hermi.whoring <=11:
        jump too_much

    m "Подойди и потрогай мой член."
    if request_18_points == 0:
        her "Ох... "
        ">Гермиона неохотно соглашается."
    elif request_18_points == 1:
        her "...Да, профессор."
        ">Гермиона соглашается."
    elif request_18_points == 2:
        ">Гермиона беззаботно соглашается."
    elif request_18_points >= 3:
        her "Вот, профессор."
        ">Гермиона резво соглашается."

    "Вы отпускаете Гермиону."

    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    if request_18_points <= 2:
        $ gryffindor +=45
        "Гриффиндор получает 45 очков."
    else:
        $ gryffindor +=11
        "Гриффиндор получает 11 очков."

    $ request_18_points += 1

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu




label new_request_19:
    if hermi.whoring <=11:
        jump too_much

    m "Иди сюда и потри мой член о свои милые щечки."
    if request_19_points == 0:
        her "Ох... "
        ">Гермиона неохотно соглашается."
    elif request_19_points == 1:
        her "...Да, профессор."
        ">Гермиона соглашается."
    elif request_19_points == 2:
        ">Гермиона беззаботно соглашается."
    elif request_19_points >= 3:
        her "Как скажете, профессор."
        ">Гермиона с нетерпением соглашается."

    "Вы прогоняете Гермиону."

    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    if request_19_points <= 2:
        $ gryffindor +=45
        "Гриффиндор получает 45 очков."
    else:
        $ gryffindor +=11
        "Гриффиндор получает 11 очков."

    $ request_19_points += 1

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu











label new_request_21:
    if hermi.whoring <=14:
        jump too_much

    m "Подойди сюда и дай подрочить на твои сиськи."
    if request_21_points == 0:
        her "Ох... "
        ">Гермиона неохотно соглашается."
        ">Вы кончаете на ее голую грудь."
    elif request_21_points == 1:
        her "...Да, профессор."
        ">Гермиона соглашается."
        ">Вы кончаете на ее голую грудь."
    elif request_21_points == 2:
        ">Гермиона беззаботно соглашается."
        ">Вы кончаете на ее голую грудь."

    elif request_21_points >= 3:
        her "Как пожелаете, дире... хозяин."
        ">Гермиона горячо соглашается."
        ">Вы кончаете на ее голую грудь."

    her "Можно дать мне полотенце, чтобы я могла вытереться?"
    menu:
        "\"Конечно.\"":
            ">Вы даете Гермионе полотенце и она вытирает вашу сперму."
        "\"Иди так.\"":
            m "Просто застегни блузку и иди так."

            if request_21_points <= 1:
                her "Что? Я не могу так, пожалуйста дайте полотенце."
                ">Вы даете Гермионе полотенце и она вытирает вашу сперму."
            else:

                her "Что? Но..."
                her "Хорошо, но только если вы дадите мне дополнительные баллы."
                menu:
                    "- Дать дополнительные баллы -":
                        m "Хорошо..."
                        her "Тогда ладно..."
                        ">Гермиона застегивает свою блузку."
                        $ gryffindor +=10
                        "Гриффиндор получает 10 очков."
                        $ request_21 = True
                    "- Забудь -":
                        ">Вы даете Гермионе полотенце и она вытирает вашу сперму."

    "Вы отпускаете Гермиону."

    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    if request_21_points <= 2:
        $ gryffindor +=55
        "Гриффиндор получает 55 очков."
    else:
        $ gryffindor +=12
        "Гриффиндор получает 12 очков."

    $ request_21_points += 1

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



label new_request_21_complete:
    "Гермиона возвращается в свой класс."
    m "Как прошел твой день?"
    if request_21_points == 3:
        her "Эм... В классе я сидела и чувствовала как мои сиськи полностью покрыты спермой. Это было так неприятно..."
    elif request_21_points >= 4:
        her "В классе я сидела и чувствовала как мои сиськи полностью покрыты спермой. Это просто улет."



    $ request_21 = False
    $ hermione_sleeping = True
    her "О, ладно. Я просто вернусь в постель."
    return











label new_request_25:
    if hermi.whoring <=17:
        jump too_much

    m "Подойди сюда и дай мне кончить на твое лицо."
    if request_25_points == 0:
        her "О... "
        ">Гермиона неохотно соглашается."
        ">Вы кончаете ей на лицо."
    elif request_25_points == 1:
        her "...Да, профессор."
        ">Гермиона соглашается."
        ">Вы кончаете ей на лицо."
    elif request_25_points == 2:
        ">Гермиона беззаботно соглашается."
        ">Вы кончаете ей на лицо."

    elif request_25_points >= 3:
        her "Конечно, дире...хозяин."
        ">Гермиона горячо соглашается."
        ">Вы кончаете ей на лицо."

    her "Могу я взять полотенце, чтобы вытереться?"
    menu:
        "\"Конечно.\"":
            ">Вы даете Гермионе полотенце и она стирает с лица вашу сперму."
        "\"Иди так.\"":
            m "Иди на уроки с покрытым спермой лицом."

            if hermi.whoring <=26:
                her "Что? Нет, я не могу, пожалуйста дайте мне полотенце!."
                ">Вы даете Гермионе полотенце и она стирает с лица вашу сперму."
            else:

                her "Что? Но..."
                her "Хорошо, но только если вы дадите мне дополнительные баллы."
                menu:
                    "- Дать дополнительные баллы -":
                        m "Хорошо..."
                        her "Тогда ладно..."
                        ">Гермиона не трогает свое обкончанное лицо."
                        $ gryffindor +=30
                        "Гриффиндор получает 30 очков."
                        $ request_25 = True
                    "- Забудь -":
                        ">Вы даете Гермионе полотенце и она стирает с лица вашу сперму."

    "Вы отпускаете Гермиону."

    if hermi.whoring <= 20:
        $ hermi.whoring +=1

    if request_21_points <= 2:
        $ gryffindor +=65
        "Гриффиндор получает 65 очков."
    else:
        $ gryffindor +=14
        "Гриффиндор получает 14 очков."

    $ request_25_points += 1

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



label new_request_25_complete:
    "Гермиона возвращается с уроков."
    m "Как прошел ваш день, Мисс Грейнджер?"
    her "Эм... Я провела большую часть дня с покрытым спермой лицом. Мне постоянно задавали вопросы."


    $ request_25 = False
    $ hermione_sleeping = True
    her "Хорошо. Тогда я пойду спать."
    return



label new_request_26:
    if hermi.whoring <=17:
        jump too_much
    m "Я хочу кончить тебе в лицо, до того как ты пойдешь в класс."
    if request_26_points == 0:
        her "О..."
        "Гермиона неохотно соглашается."
    elif request_26_points == 1:
        her "Если я должна..."
        "Гермиона соглашается."
    elif request_26_points == 2:
        her "Конечно... профессор."
        "Гермиона соглашается. По ней видно как она этого хочет."
    elif request_26_points >= 3:
        her "Конечно, дире...хозяин"
        ">Гермиона радостно соглашается."

    "Вы отпускаете Гермиону."

    $ request_26 = True
    if hermi.whoring <= 20:
        $ hermi.whoring +=1

    if request_26_points <= 2:
        $ gryffindor +=65
        "Гриффиндор получает 65 очков."
    else:
        $ gryffindor +=14
        "Гриффиндор получает 14 очков."

    $ hermione_takes_classes = True
    jump day_main_menu


label new_request_26_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел ваш день, Мисс Грейнджер?"
    if request_26_points == 0:
        her "Эм... Я провела половину урока со спермой во рту"
    elif request_26_points == 1:
        her "Something else about cum. LVL 2"
    elif request_26_points == 2:
        her "LVL3"
    elif request_26_points >= 3:
        her "LVL4"
        her "Это было чудесно!"

    $ request_26_points += 1
    $ request_26 = False
    $ hermione_sleeping = True
    her "Ох, ладно, тогда я пойду в постель."
    return


label new_request_27:
    if hermi.whoring <=17:
        jump too_much
    m "Я хочу, чтобы вы кое-что сделали для меня сегодня: отсосите у двух одноклассников"
    if request_27_points == 0:
        her "Ох..."
        "Гермиона неохотно соглашается."
    elif request_27_points == 1:
        her "Если я должна..."
        "Гермиона соглашается."
    elif request_27_points == 2:
        her "Конечно, профессор"
        "Гермиона согласна. Она жаждет этого."
    elif request_27_points >= 3:
        her "Конечно директор..."
        ">Гермиона с радостью соглашается."

    "Вы отпускаете Гермиону."

    $ request_27 = True
    if hermi.whoring <= 20:
        $ hermi.whoring +=1

    if request_27_points <= 2:
        $ gryffindor +=65
        "Гриффиндор получает 65 очков."
    else:
        $ gryffindor +=14
        "Гриффиндор получает 14 очков."

    $ hermione_takes_classes = True
    jump day_main_menu


label new_request_27_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел ваш день, Мисс Грейнджер?"
    if request_27_points == 0:
        her "Эм... Lvl.1."
    elif request_27_points == 1:
        her "Something else about LVL 2"
    elif request_27_points == 2:
        her "LVL3"
    elif request_27_points >= 3:
        her "LVL4"
        her "Это было чудесно!"

    $ request_27_points += 1
    $ request_27 = False
    $ hermione_sleeping = True
    her "Ох, ладно. Пожалуй я пойду спать."
    return



label new_request_28:
    if hermi.whoring <=17:
        jump too_much
    m "Я хочу, чтобы ты подрочила своему учителю"
    if request_28_points == 0:
        her "Ох..."
        "Гермиона неохотно соглашается."
    elif request_28_points == 1:
        her "Если так нужно..."
        "Гермиона соглашается."
    elif request_28_points == 2:
        her "Конечно, профессор."
        "Гермиона соглашается. Она жаждет этого."
    elif request_28_points >= 3:
        her "Конечно директор..."
        ">Гермиона с радостью соглашается."

    "Вы отпускаете Гермиону."

    $ request_28 = True
    if hermi.whoring <= 20:
        $ hermi.whoring +=1

    if request_28_points <= 2:
        $ gryffindor +=65
        "Гриффиндор получает 65 очков."
    else:
        $ gryffindor +=14
        "Гриффиндор получает 14 очков."

    $ hermione_takes_classes = True
    jump day_main_menu


label new_request_28_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел ваш день, Мисс Грейнджер?"
    if request_28_points == 0:
        her "Em... Lvl.1."
    elif request_28_points == 1:
        her "Something else about LVL 2"
    elif request_28_points == 2:
        her "LVL3"
    elif request_28_points >= 3:
        her "LVL4"
        her "Это было чудесно!"

    $ request_28_points += 1
    $ request_28 = False
    $ hermione_sleeping = True
    her "Ох, ладно. Я тогда пойду спать."
    return












label new_request_32:
    if hermi.whoring <=26:
        jump too_much
    m "Я хочу, чтобы ты надела это."
    if request_32_points == 0:
        her "Ох..."
        "Гермиона неохотно соглашается."
    elif request_32_points == 1:
        her "Если так нужно..."
        "Гермиона соглашается."
    elif request_32_points == 2:
        her "Конечно, профессор."
        "Гермиона соглашается. Она жаждет этого."
    elif request_32_points >= 3:
        her "Конечно, директор..."
        ">Гермиона с радостью соглашается."

    "Гермиона надевает очень распутный наряд и идет на занятия."

    $ request_32 = True
    if hermi.whoring <= 29:
        $ hermi.whoring +=1

    if request_32_points <= 2:
        $ gryffindor +=100
        "Гриффиндор получает 100 очков."
    else:
        $ gryffindor +=23
        "Гриффиндор получает 23 очков."

    $ hermione_takes_classes = True
    jump day_main_menu


label new_request_32_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел ваш день, Мисс Грейнджер?"
    if request_32_points == 0:
        her "Em... Lvl.1. She tells you how people treated her like a whore today."
    elif request_32_points == 1:
        her "Something else about LVL 2. She tells you how people treated her like a whore today."
    elif request_32_points == 2:
        her "LVL3. She tells you how people treated her like a whore today."
    elif request_32_points >= 3:
        her "LVL4. She tells you how people treated her like a whore today."
        her "Это было чудесно!"

    $ request_32_points += 1
    $ request_32 = False
    $ hermione_sleeping = True
    her "Ох, ладно. Я тогда пойду спать."
    return










label music_block:
    $ music()
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 
    return






label vague_idea:
    show screen blktone8
    ">Вам не хватает воображения для такого."
    hide screen blktone8
    return


label could_not_flirt:
    hide screen blkfade
    hide screen bld1
    $ herView.hideQ()
    hide screen blktone 
    hide screen chair_02
    hide screen hermione_02
    hide screen jerking_off_01 
    hide screen ctc
    show screen genie
    with d3

    $ walk_xpos=400
    $ walk_xpos2=610
    $ hermione_speed = 02.0
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3')
    with Dissolve(.3)

    $ request_02_b_points += 1
    $ request_02_b = False
    $ wtevent.Finalize()







    label finish_daytime_event:
    call music_block

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
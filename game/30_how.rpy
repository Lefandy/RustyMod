label howtoplay:
    $ end_u_1_pic =  "title3.jpg"

    show screen end_u_1                                             
    play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 
    if not persistent.tut:




        $ lola_face = "03_hp/22_lola/01.png"
        $ lola_body = "03_hp/22_lola/body_01.png"

        $ l_things = True

        $ lx = 490
        $ ly = 190
        show screen l_head
        l "Привет интернет-извращугам!"
        hide screen l_head
        a5 "Следи за языком, сучка!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/02.png"
        show screen l_head
        l "Хах...?"
        hide screen l_head
        a6 "Что я тебе говорил о слове на букву \"и\"?"
        $ l_question = True
        $ lola_face = "03_hp/22_lola/03.png"
        show screen l_head
        l "Эм... Использовать его как можно чаще..?"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Нет!{/size}"
        $ l_question = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "Гх!"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Мы не используем его! Никогда!{/size}"
        $ lola_face = "03_hp/22_lola/01.png"
        $ l_drop = False
        show screen l_head
        l "Потому что самый самый большой здесь папочка?"
        hide screen l_head
        a6 "Гх!"
        a6 "Тебе понравилось сниматься в \"Тренер Принцессы\"?"
        $ l_hearts = True
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "Лучшее событие в моей жизни!"
        hide screen l_head
        a1 "Хочешь попасть в \"Золотое издание\"?"
        $ l_hearts = False
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "!!!"
        $ lola_face = "03_hp/22_lola/06.png"
        show screen l_head
        l "Дамы и гопода, добро пожаловать в обучающий режим \"Тренера Гермионы\"."
        hide screen l_head
        a1 "Умница, девочка."
        $ l_drop = True
    else:
        $ lx = 490
        $ ly = 190
        $ lola_body = "03_hp/22_lola/body_01.png"
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Хм...?"
        l "Ты хочешь прослушать обучение снова?"
        $ lola_face = "03_hp/22_lola/09.png"
        l "Хм...."
        $ lola_face = "03_hp/22_lola/11.png"
        l "Ты не смущен?"
        $ lola_face = "03_hp/22_lola/10.png"
        l "Хм..."
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        l "*Хихикает!*"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        l "Ты хочешь, чтобы я учила тебя топлесс?"
        l "Тогда поблагодари партизан,и я тебя буду учить правильно.*Хихикает!*"
        hide screen l_head
        $ d_flag_01 = False
        menu:
            "\"Еще бы!\"":
                $ lola_face = "03_hp/22_lola/01.png"
                show screen l_head

                $ d_flag_01 = True
                l "Океюшки!"
                hide screen l_head
                pause.1
                show screen blkfade
                with d3
                $ lola_body = "03_hp/22_lola/body_02.png"
                $ l_blush = True
                pause.5
                hide screen blkfade
                with d7
            "\"Нет.\"":


                $ lola_face = "03_hp/22_lola/12.png"
                show screen l_head
                l "Ты скучный..."
                $ lola_face = "03_hp/22_lola/09.png"
                l "Ладно, пофиг..."



    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1
    $ lola_face = "03_hp/22_lola/06.png"
    show screen l_head
    l "Вот краткий перечень вещей, которые стоит помнить..."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_02.png"
    $ renpy.play('sounds/boing02.mp3')

    l "Гермиона захочет продавать сексуальные услуги в обмен на очки факультета, когда Гриффиндор отстает."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_01.png"
    $ renpy.play('sounds/boing02.mp3')
    l "Дружба с профессором Снейпом увеличит количество очков, получаемых Слизереном."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_03.png"
    $ renpy.play('sounds/boing02.mp3')
    if d_flag_01:
        $ lola_face = "03_hp/22_lola/07.png"
    l "Чтение образовательных книг позволит тебе зарабатывать, но это по желанию."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_04.png"
    $ renpy.play('sounds/boing02.mp3')
    l "Покупка одной и той же сексуальной услуги может привести к разным последствиям, в зависимости от того, как далеко Гермиона зашла в своих тренировках."
    $ lola_face = "03_hp/22_lola/06.png"

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_07.png"
    l "Все услуги разделены на две группы: \"приватные услуги\" и\"публичные услуги\"."
    l "Приватные услуги оказываются в кабинете и не сильно влияют на репутацию Гермионы."
    l "Публичные услуги оказываются во время уроков за пределами экрана."
    l "Каждая публичная услуга, не считая последней, имеет девять концовок."
    l "Кстати, несмотря на то, что покупка приватных услуг - необходима для тренировки Гермионы, публичные услуги не обязательны."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_05.png"

    $ renpy.play('sounds/boing02.mp3')
    l "Если обращаться с ней плохо, то настроение Гермиона ухудшится, она может обидеться и стать очень неподатливой..."
    l "Она остынет со временем, но ты можешь ускорить процесс, если подаришь ей что-нибудь..."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_06.png"
    $ renpy.play('sounds/boing02.mp3')
    l "Здесь нет временных ограничений. Так что можешь играть в нее столько дней, сколько захочешь."




    $ end_u_1_pic =  "03_hp/22_lola/tut_00.png"
    $ l_drop = False

    if not persistent.tut:
        $ persistent.tut = True
        hide screen l_head
        a1 "Ладно, этого хватит..."
        $ l_question = True
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Как я справилась?"
        hide screen l_head
        a1 "Ты отлично поработала. Хорошая девочка."
        $ l_question = False
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        show screen l_head
        l "Хе-хе-хе. Лола хорошая девочка!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "А что я получу?"
        hide screen l_head
        a1 "А что ты хочешь?"
        $ lola_face = "03_hp/22_lola/10.png"
        show screen l_head
        l "Хм..."
        $ l_exclamation = True
        $ lola_face = "03_hp/22_lola/01.png"
        l "Мы можем сделать сцену изнасилования со мной в \"Золотом издании\"?"
        hide screen l_head
        a6 "Не испытывай мое терпения, девочка."
        $ l_exclamation = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "Извини, папочка."
        $ l_drop = False
        hide screen l_head
        a5 "............"
    else:

        if d_flag_01:
            hide screen l_head
            stop music fadeout 1.0
            a1 "Что здесь происходит?"
            $ lola_face = "03_hp/22_lola/14.png"
            $ l_drop = True
            show screen l_head
            l "Упс!"
            hide screen l_head
            a1 "Что я говорил тебе о раздевании перед незнакомцами?"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Это важная часть взросления?"
            hide screen l_head
            a6 "Нет!"
            $ l_drop = False
            $ l_tears = True
            $ lola_body = "03_hp/22_lola/body_01.png"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Папочка, мне так жаль!"
            l "Этот случайный чувак из интернета заставил меня, я клянусь!"
            hide screen l_head
            a1 "Обучение закончено."
            $ l_blush = False
            $ l_tears = False
            $ lola_face = "03_hp/22_lola/15.png"
            show screen l_head
            l "Хе-хе! Ты попался!"
        else:
            $ lola_face = "03_hp/22_lola/09.png"
            l "И, это..."
            $ lola_face = "03_hp/22_lola/13.png"
            l "Может быть в следующий раз?"

return


label abouttrainer:
    $ end_u_1_pic =  "title3.jpg"

    show screen end_u_1                                             
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1

    dev "Итак, сейчас перед вами \"Невинные Ведьмы\"."
    dev "Наша дружная команда взяла за основу небольшую, но очень приятную игру от Акабура."
    dev "И делает на основе ее идей и контента нечто новое."
    dev "Новые ивенты и персонажи, система гардероба и газетное издательство... Все это только у нас."
    dev "Кроме того, мы не считаем проект законченным и постоянно совершенствуем его."
    dev "А еще, перевели игру на русский язык, чтобы русским людям было приятно играть, и сделали мультиязычную версию."
    dev "Помните, что мы делаем это совершенно бесплатно. Для собственного и вашего удовольствия."
    dev "Все пожертвования в фонд развития игры пойдут не на пиво разработчикам, а на различные нужды проекта."

    return




label devel:

    $ end_u_1_pic =  "title3.jpg"

    show screen end_u_1                                             
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1

    dev "Итак, вы уже обратили внимание, что это не оригинальная игра Акабура..."
    menu:
        "Что ???":
            dev "(facepalm)"
            dev "Я так и знал, что нужно давать больше информации общественности..."
        "Это же шутка ?":

            dev "..........."
        "А разве ты не Акабур ?":

            dev "В рот мне ноги..."

    dev "{size=+3}Т.е. вы все по-прежнему считаете, что игру для вас продолжает улучшать Акабур ?{/size}"
    dev "И это после того, как он сообщил, что считает ее законченной ?"
    dev "После того, как он решил никогда ее не переводить на русский ?"
    dev "После того, как я написал всю эту гору кода, не говоря уж об остальной команде разработчиков, переводчиков и художников, месяцами бесплатно трудящихся для вас ?"
    dev "{size=+4}Аргх...{/size}"
    dev "......."
    dev "Простите, наболело."

    dev "Для вас над игрой трудилась команда \"Sad Crab\""
    dev "Khan (перевод/техническая поддержка) - глава проекта, участвовал в переводе исходной версии, поддерживает английскую версию игры, администратор форума проекта."
    dev "Dron(сценарии/программирование/техническая поддержка) - новые сюжеты и сцены (тексты и программирование), модули работы с ивентами/предметами/персонажами."
    $ renpy.say (dev,tr("Eskelsama (программирование) - модуль работы с артами, модули работы с эвентами, общий кодинг(завершил разработку)."))
    dev "Tobie(геймдизайн/сценарий/арт) - новый сценарий и ивенты, доработка арта."
    dev "Scerg(арт) - основной художник, арт персонажей и другое."
    $ renpy.say(dev, tr("PFMX(перевод и подержка английской версии игры) - основной переводчик игры на английский язык."))
    dev "Appo(техническая поддержка) - сайт и форум команды, помощь в багфиксе и кодинге (завершил разработку)."

    $ hx = 370
    $ hy = 0
    $ h_red_angry = True
    $ h_angry = False
    $ h_smile = False
    $ h_red_smile = False

    dev "И несравненная Гермиона Грейнджер в роли офисной шл..."
    show screen l_hermiona
    her "Что-о-о-о ???"
    hide screen l_hermiona

    dev "Прости, в роли секретут..."
    $ h_red_angry = False
    $ h_angry = True
    $ h_smile = False
    show screen l_hermiona
    her "А на тебя давно в последний раз подавали в суд\n за половую дискриминацию ?"
    hide screen l_hermiona
    dev "Бхм. И наша главная офис-леди - мисс Грейнджер."
    $ h_red_angry = False
    $ h_angry = False
    $ h_smile = True
    show screen l_hermiona
    her "Так то лучше !"
    her "Всем до встречи в игре."
    hide screen l_hermiona
    dev "Недотрога..."
    dev "Ушла наконец."

    dev "Итак, приятной игры, друзья !"

    dev "А если хотите пообщаться с людьми, которые продолжают совершенствование и расширение игры, милости просим."
    dev "{a=http://forum.sad-crab.com}НАШ ФОРУМ ТУТ{/a}"


return

label forum:

    $ end_u_1_pic =  "title3.jpg"

    show screen end_u_1                                             

    dev "Итак, перед вами модификация игры, которая развивается независимой (от Акабура) командой разработчиков. Добро пожаловать на {a=http://forum.sad-crab.com}НАШ ФОРУМ{/a}."

return

label donate:

    $ end_u_1_pic =  "title3.jpg"

    show screen end_u_1                                             

    dev "Вы можете отблагодарить разработчиков, пожертвовав некую сумму денег.Это подстегнет нас увеличить скорость выхода новых версий."
    dev "Все суммы, внесенные вами, пойдут на художников для игры."
    dev "{a=https://www.patreon.com/Sad_Crab}Мы на Патреоне{/a}"
    $ renpy.say (dev,"Webmoney:   {a=http://sad-crab.com/пожертвования}R296092719190{/a}\n                      {a=http://sad-crab.com/пожертвования}Z128903876765{/a}\n                      {a=http://sad-crab.com/пожертвования}E390148659011{/a}")
    dev "Яндекс Деньги:\n{a=http://sad-crab.com/пожертвования}410012123558554{/a}"
    dev "Qiwi:\n{a=http://sad-crab.com/пожертвования}+79637679050{/a}"

    $ hx = 370
    $ hy = 0
    $ h_red_angry = False
    $ h_angry = False
    $ h_smile = True
    $ h_red_smile = False

    show screen l_hermiona2
    her "Приветик !"
    her "Мой дорогой игрок, что бы я без вас делала !"
    her "Ваша радость - то, ради чего я участвую в разработке !"
    her "А еще..."
    hide screen l_hermiona2

    $ dx = 480
    $ dy = 0
    $ d_angry = False
    $ d_smile = True

    show screen l_daphne
    daph "Да помолчи уже !"
    daph "Уж кто-кто, а наш игрок не дурак, и здесь он только из-за меня."
    daph "А ты можешь..."
    hide screen l_daphne

    $ h_smile = False
    $ h_red_angry = True

    show screen l_hermiona2
    her "{size=+2}Что ты сказала ?{/size}"
    her "{size=+4}Да как ты смеешь ?{/size}"
    her "Кому нужна такая дура и зазнайка !"
    her "Разумеется, наш любимый игрок предпочтет общество лучшей ученицы Хог..."
    hide screen l_hermiona2

    $ d_angry = True
    $ d_smile = False

    show screen l_daphne
    daph "Ученицы, говоришь ?"
    daph "{size=+3}Да ведь это из-за тебя мы больше не ученицы !{/size}"
    daph "Зачем было нужно трепаться своим ненаглядным Гарри и Рону о наших секретах ?"
    daph "Слухи дошли до самого верха - и вот результат !"
    daph "Из школы нас выгнали, семья теперь меня презирает..."
    daph "Все, что остается, это шлю... разв... сниматься день за днем в этом унизительном, ужасном..."
    hide screen l_daphne

    $ h_smile = True
    $ h_red_angry = False

    show screen l_hermiona2
    her "Кхм."
    her "Ты случайно не забыла, зачем мы снимаем видео ?"

    hide screen l_hermiona2

    $ d_angry = False
    $ d_smile = True

    show screen l_daphne
    daph "Ой."
    daph "На чем я остановилась ?"
    daph "И этот прекрасный, замечательный проект - именно то, что дает нашей жизни смысл."
    daph "Но, к сожалению, нам тоже нужно на что-то жить..."
    daph "Поэтому количество новых материалов с нашим участием зависит именно от вас."
    hide screen l_daphne

    show screen l_hermiona2
    her "(И все-таки, кто же распустил слухи...)"
    her "(Ведь я даже не думала посвящать в свои дела посторонних.)"
    her "(И теперь нам приходится не учиться, а только и делать, что... Разработчики просто счастливы.)"
    hide screen l_hermiona2

    $ h_red_angry = True
    $ h_smile = False

    show screen l_hermiona2
    her "Так вот оно что. Я кажется поняла, кто проговорился !"
    hide screen l_hermiona2

    dev "Кх-кхм. А вот и я. Вы обе произнесли прекрасную речь. А теперь продолжу."

    $ d_angry = True
    $ d_smile = False

    show screen l_daphne
    daph "Минутку ! Я хочу дослушать Гермиону."
    daph "Уважаемый игрок, мы..."
    hide screen l_daphne

    dev "А ну брысь обе !"
    dev "......."
    dev "Вот, так-то лучше."
    dev "Дались им эти авторы слухов. Главное, что теперь никакие уроки не отвлекает от рабо..."
    dev "Кстати о работе."
    dev "Если вы хотите намного больше картинок в игре, нам нужны для этого дополнительные средства."
    dev "У вас есть возможность помочь проекту."
    dev "Мы обязательно будем развивать его изо всех сил в любом случае, но найм дополнительных девок..."
    dev "Эээээээ. Художников. Найм художников очень поможет делу."
    dev "Спасибо за внимание."

    $ renpy.say (dev,tr("{a=https://www.patreon.com/Sad_Crab}Мы на Патреоне{/a}"))
    $ renpy.say (dev,"Webmoney:   {a=http://sad-crab.com/пожертвования}R296092719190{/a}\n                      {a=http://sad-crab.com/пожертвования}Z128903876765{/a}\n                      {a=http://sad-crab.com/пожертвования}E390148659011{/a}")
    $ renpy.say (dev,tr("Яндекс Деньги:\n{a=http://sad-crab.com/пожертвования}410012123558554{/a}"))
    dev "Qiwi:\n{a=http://sad-crab.com/пожертвования}+79637679050{/a}"

return

label donate2:

    $ end_u_1_pic =  "title3.jpg"

    show screen end_u_1                                             

    dev "Вы можете отблагодарить разработчиков, пожертвовав некую сумму денег.Это подстегнет нас увеличить скорость выхода новых версий."
    dev "Все суммы, внесенные вами, пойдут на развитие проекта."
    $ renpy.say (dev,"Webmoney:   {a=http://sad-crab.com/пожертвования}R296092719190{/a}\n                      {a=http://sad-crab.com/пожертвования}Z128903876765{/a}\n                      {a=http://sad-crab.com/пожертвования}E390148659011{/a}")
    dev "Яндекс Деньги:\n{a=http://sad-crab.com/пожертвования}410012123558554{/a}"
    dev "Qiwi:\n{a=http://sad-crab.com/пожертвования}+79637679050{/a}"

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

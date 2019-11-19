

label new_request_20:



    $ herView.hideQQ()
    m "{size=-4}(Предложить ей развлечься с одноклассницей?){/size}"
    $ menu_x = 0.5
    menu:
        "\"(Да, давай сделаем это!)\"":
            pass
        "\"(Не сейчас.)\"":
            $ wtevent.NotFinished()
            jump new_personal_request


    $ pos = POS_140

    if request_20_points == 0:
        m "Вы когда-нибудь целовали девушку, мисс Грейнджер?"
        $ herView.hideshowQQ( "body_07.png", pos )
        her "?!"

        if hermi.whoring <=11 or request_15_points <= 1:
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        $ herView.hideshowQQ( "body_02.png", pos )
        her "Я не... лесбиянка, сэр."
        m "Глупая девочка... Тебе не надо быть лесбиянкой, чтобы целовать девушек."
        m "Например, я регулярно занимаюсь этим, но я ведь не лесбиянка."
        $ herView.hideshowQQ( "body_05.png", pos )
        her "..............."
        her "Сэр..."
        m "Никаких \"сэров\"! Это твое задание на сегодня!"
        m "Найди какую-нибудь милашку и чмокни ее!"
        $ herView.hideshowQQ( "body_11.png", pos )
        her "Сэр, но я..."
        m "Свободны, мисс Грейнджер."
        $ herView.hideshowQQ( "body_07.png", pos )
        her "Сэр!......"
        m "Свободны, я сказал."
        $ herView.hideshowQQ( "body_09.png", pos )
        her "*Хм!*..."
    else:

        m "45 очков так и ждут, когда их заберут!"
        m "Интересуетесь, мисс Грейнджер?"
        if hermi.whoring >= 12 and hermi.whoring <= 14:
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            $ herView.hideshowQQ( "body_03.png", pos )
            her "Это зависит от того..."
            her "Придется ли мне опять делать что-то развратное?"
            m "\"Развратное\"??! Когда это я?.."
            $ herView.hideshowQQ( "body_04.png", pos )
            her "Серьезно, сэр?"
            m "Ладно, ладно... Все, что я хочу сегодня - чтобы ты немного развлеклась с девушкой."
            $ herView.hideshowQQ( "body_05.png", pos )
            her "Ох, и все?"
            m "Да, ничего необычного для тебя, ведь так?"
            m "А вечером ты, конечно же, получишь свои сорок пять очков."
            $ herView.hideshowQQ( "body_07.png", pos )
            her "............."
            m "...Ты согласна?"
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Я посмотрю, что смогу сделать, сэр..."
            m "Отлично. Тогда увидимся после занятий."
            $ herView.hideshowQQ( "body_79.png", pos )
            her "................"

        elif hermi.whoring >= 15 and hermi.whoring <= 17:
            $ herView.hideshowQQ( "body_70.png", pos )
            her "Наверное..."
            m "Отлично. Все, что мне нужно - чтобы ты немного развлеклась с девушкой."
            $ herView.hideshowQQ( "body_71.png", pos )
            her "Ясно..."
            m "Готовы выполнить задание, мисс Грейнджер?"
            $ herView.hideshowQQ( "body_29.png", pos )
            her "Наверное..."
            m "Отлично. Тогда увидимся после уроков."


        elif hermi.whoring >= 18:
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            $ herView.hideshowQQ( "body_06.png", pos )
            her "Конечно, почему нет?"
            m "Отлично."
            m "Сегодня я хочу, чтобы ты немного поразвлекалась с девушкой."
            $ herView.hideshowQQ( "body_45.png", pos )
            her "Хорошо."
            $ herView.hideshowQQ( "body_64.png", pos )
            her "Я знаю парочку девчонок, которые любят внимание и не будут возвражать против небольшого представления."
            m "Отлично. Тогда, встретимся после занятий."




    $ request_20 = True

    hide screen bld1
    $ herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400
    $ walk_xpos2=610
    $ hermione_speed = 02.0
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3')
    with Dissolve(.3)


    $ hermione_takes_classes = True

    call music_block

    $ wtevent.Finalize()

    jump day_main_menu





label new_request_20_complete:

    $ walk_xpos=520
    $ walk_xpos2=400
    $ hermione_speed = 02.0

    if hermi.whoring >= 18 and one_out_of_three == 3:
        show screen blktone
        with d3
        pause
        m "Хм… странно, ее все еще нет…"
        show screen blktone
        with d3
        pause
        m "Может она забыла?"
        g9 "А может она просто кувыркается с кем-то в постельке?"
        g9 "Вот шлюшка!"
        g9 "Буду ждать завтра подробного доклада!"

    $ renpy.play('sounds/door.mp3')
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400
    show screen hermione_02 
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ pos = POS_370

    $ request_20 = False

    if hermi.whoring >= 12 and hermi.whoring <= 14:
        if one_out_of_three == 1:
            stop music fadeout 1.0
            m "Мисс Грейнджер..."
            m "Вам удалось выполнить задание?"
            show screen blktone
            with d3
            $ herView.hideshowQQ( "body_11.png", pos )
            her "Я..."
            m "Я сказал тебе повеселиться с девушкой..."
            m "Ты сделала это?"
            $ herView.hideshowQQ( "body_10.png", pos )
            her "Я..."
            her "Я пыталась, сэр. Я правда пыталась."
            m "И?"
            $ herView.hideshowQQ( "body_29.png", pos )
            her "Ну..."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            her "Мне было стыдно и неловко..."
            m "Так ты это сделала, или нет?"
            $ herView.hideshowQQ( "body_69.png", pos )
            her "...нет, сэр..."
            her "Все, что я сделала - это выставила себя полной дурой..."
            $ herView.hideshowQQ( "body_47.png", pos )
            her "Перед всем классом..."
            m "Расскажи мне, что произошло, девочка."
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Нет, не расскажу сэр."
            her "Ни за что на свете!"
            $ herView.hideshowQQ( "body_132.png", pos )
            her "Так или иначе, зачем мне надо было выполнять такое дурацкое задание?!"
            her "Какой во всем этом смысл?"
            $ herView.hideshowQQ( "body_30.png", pos )
            her "Я ненавижу его!"
            $ herView.hideshowQQ( "body_69.png", pos )
            her "..............."
            her "................."
            m ".............."
            m "Тебе не заплатят, ты знаешь об этом, так?"
            $ herView.hideshowQQ( "body_30.png", pos )
            her "Мне все равно..."
            $ hermi.liking -=25
            jump could_not_flirt

        elif one_out_of_three == 2:
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $ herView.hideshowQQ( "body_16.png", pos )
            her "Выполнила, сэр..."
            m "Хорошо. Расскажи поподробнее."
            $ herView.hideshowQQ( "body_17.png", pos )
            her "Ну, я поцеловала девочку. Как вы мне и велели."
            m "Ты была смущена?"
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Очень, сэр."
            m "Но тебе понравилось?"
            $ herView.hideshowQQ( "body_79.png", pos )
            her "*Хм!*..."
            m "Итак, вы поцеловали девушку, и вам это понравилось?"
            $ herView.hideshowQQ( "body_66.png", pos )
            her "Да..."
            m "С языком?"
            $ herView.hideshowQQ( "body_66.png", pos )
            her "Да..."
            her "Это был настоящий поцелуй взасос, если вам интересно."
            her "Теперь я могу получить свою плату?"
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Прошу, сэр..."
            m "Ладно, хорошо..."

        elif one_out_of_three == 3:
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $ herView.hideshowQQ( "body_16.png", pos )
            her "Да, сэр, выполнила."
            m "Хорошо. Расскажи мне, как все прошло."
            $ herView.hideshowQQ( "body_16.png", pos )
            her "Все прошло хорошо, сэр."
            m "Превосходно. Расскажи мне детали."
            $ herView.hideshowQQ( "body_04.png", pos )
            her "Что бы вам хотелось узнать, сэр?"
            m "Расскажи мне все! Та девушка была симпатичной?"
            m "Она ответила на поцелуй?"
            $ herView.hideshowQQ( "body_08.png", pos )
            her "Она была относительно симпатичной, сэр."
            her "И она ответила на поцелуй..."
            $ herView.hideshowQQ( "body_184.png", pos )
            her "..........."
            $ herView.hideshowQQ( "body_08.png", pos )
            her "Что-то еще, сэр?"
            m "...."
            m "Почему с тобой так сложно?"
            $ herView.hideshowQQ( "body_04.png", pos )
            her "При всем уважении, сэр..."
            her "Вы сказали мне поцеловать другую девушку, и я поцеловала..."
            $ herView.hideshowQQ( "body_03.png", pos )
            her "Теперь, не могли бы вы быть так любезны заплатить мне?"
            m "......................"
            menu:
                "\"Мне не нравится ваш тон, леди.\"":
                    $ herView.hideshowQQ( "body_04.png", pos )
                    her "Какая жалость, сэр."
                    m "Это точно..."
                    m "Потому что тебе никто ничего не заплатит, нахальная мелкая ведьма."
                    $ herView.hideshowQQ( "body_03.png", pos )
                    stop music fadeout 1.0
                    her "Что?"
                    $ herView.hideshowQQ( "body_11.png", pos )
                    her "Сэр, вы не можете так поступить!"
                    m "Свободны."
                    $ herView.hideshowQQ( "body_10.png", pos )
                    her "Н-но..."
                    $ herView.hideshowQQ( "body_11.png", pos )
                    her "Сэр, пожалуйста!"
                    her "Девушка была из \"Пуффендуя\", и..."
                    m "Поздно для этого, мисс Грейнджер."
                    m "Вы свободны."
                    $ herView.hideshowQQ( "body_21.png", pos )
                    her "......"
                    $ hermi.liking -=25
                    jump could_not_flirt
                "\"Ладно. Вот твоя плата.\"":

                    pass



    elif hermi.whoring >= 15 and hermi.whoring <= 17:
        if one_out_of_three == 1:
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $ herView.hideshowQQ( "body_16.png", pos )
            her "Выполнила, сэр..."
            m "Тогда почему вы просто стоите и молчите? Рассказывайте."
            $ herView.hideshowQQ( "body_14.png", pos )
            her "Эм, ладно..."
            her "Та девочка была из\"Когтеврана\"..."
            $ herView.hideshowQQ( "body_13.png", pos )
            her "Я думаю, что она младшеклассница, но я не спрашивала..."
            her "Мы начали разговаривать о парнях..."
            $ herView.hideshowQQ( "body_16.png", pos )
            her "И она сказала мне, что ни разу не целовалась..."
            her "И что она боится, что у нее, наверное, будет плохо получаться..."
            $ herView.hideshowQQ( "body_06.png", pos )
            her "Ну я и предложила свою помощь..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
            her "Потом мы вместе провели время в одной из кабинок в туалете..."
            $ herView.hideshowQQ( "body_45.png", pos )
            her "Развлекаясь..."
            $ herView.hideshowQQ( "body_31.png", pos )
            her "Она довольно быстро приноровилась... Думаю, что после небольшой практики она будет по настоящему хороша в этом..."
            $ herView.hideshowQQ( "body_45.png", pos )
            her "А еще она была такой милашкой..."
            $ herView.hideshowQQ( "body_46.png", pos )
            her "Она называла меня - \"Мисс Грейнджер\"..."
            m "Хм..."
            m "не помню, чтобы я давал вам задание смущать маленьких детей, мисс Грейнджер."
            $ herView.hideshowQQ( "body_64.png", pos )
            her "\"Маленьких детей\"? Позвольте, сэр..."
            her "Вы бы видели эту девочку..."
            her "Миниатюрная? Может быть... Но определенно не \"ребенок\"."
            $ herView.hideshowQQ( "body_111.png", pos )
            her "И я уверяю вас, что она была какой угодно, но не смущенной."
            her "На самом деле, под конец нашего \"урока\" она стала даже немного несносной..."
            $ herView.hideshowQQ( "body_31.png", pos )
            her "У меня даже появилось чувство, что она просто воспользовалась мной..."
            m "Ох... Ну, в таком случае..."
            $ herView.hideshowQQ( "body_45.png", pos )


        elif one_out_of_three == 2:
            m "Мисс Грейнджер. Вы выполнили задание?"
            show screen blktone
            with d3
            $ herView.hideshowQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            her "Выполнила, сэр."
            m "Расскажи мне, как все прошло."
            $ herView.hideshowQQ( "body_31.png", pos )
            her "Ну... Эм..."
            her "Есть одна девушка, которая любит... девушек..."
            her "Я подумала, что она будет идеальным кандидатом для моего задания..."
            her "И я спросила, могу ли я ее поцеловать..."
            $ herView.hideshowQQ( "body_87.png", pos )
            her "Она сказала, что для этого мы должны пойти в женскую уборную..."
            her "Но я поцеловала ее прямо там, в коридоре..."
            $ herView.hideshowQQ( "body_31.png", pos )
            her "И она поцеловала меня в ответ, но..."
            $ herView.hideshowQQ( "body_118.png", pos )
            her "Это показалось мне странным..."
            her "То, как она целовалась..."
            $ herView.hideshowQQ( "body_117.png", pos )
            her "Она вела себя как парень, сэр..."
            $ herView.hideshowQQ( "body_118.png", pos )
            her "Агрессивно, но уверенно..."
            $ herView.hideshowQQ( "body_120.png", pos )
            her "Естественно, рядом мгновенно образовалась небольшая толпа..."
            $ herView.hideshowQQ( "body_183.png", pos )
            her "В основном парни, конечно..."
            $ herView.hideshowQQ( "body_182.png", pos )
            her "Некоторые из них даже подбадривали нас..."
            $ herView.hideshowQQ( "body_129.png", pos )
            her "....."
            her "Кстати, та девушка, что я поцеловала, сэр..."
            m "Хм...?"
            $ herView.hideshowQQ( "body_127.png", pos )
            her "Она одна из тех непопулярных ребят..."
            her "Я знаю, что остальные ученики могли издеваться над ней..."
            $ herView.hideshowQQ( "body_129.png", pos )
            her "Но сегодня все изменилось..."
            her "Я собственноручно подняла ту девушку с социального дна..."
            $ herView.hideshowQQ( "body_111.png", pos )
            her "В \"лесбиянку, что развлекается с Гермионой Грейнджер\"!"
            m "Вау... Ты прямо герой..."
            $ herView.hideshowQQ( "body_128.png", pos )
            her "Думаю да, сэр..."
            her "Я изменила жизнь той бедной девушки..."
            m "Ты меня растрогала..."



        elif one_out_of_three == 3:
            show screen blktone
            with d3
            $ herView.hideshowQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            her "Профессор Дамблдор?"
            m "Да, мисс Грейнджер?"
            $ herView.hideshowQQ( "body_31.png", pos )
            her "Могу я задать вопрос, сэр?"
            m "Конечно."
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Эм..."
            $ herView.hideshowQQ( "body_66.png", pos )
            her "Почему парни так любят наблюдать за целующимися девушками, сэр?"
            menu:
                m "..."
                "\"Кто знает? Парни странные.\"":
                    $ herView.hideshowQQ( "body_118.png", pos )
                    her "Да, это точно, так ведь...?"
                    m "Да, да..."
                    m "И вот почему такие молоденькие девушки, как ты..."
                    m "Часто интересуются намного более взрослыми джентльменами..."
                    $ herView.hideshowQQ( "body_117.png", pos )
                    her "??!"
                    $ herView.hideshowQQ( "body_79.png", pos )
                    her "Это не то, что я имела в виду, сэр..."
                "\"Ты не поймешь.\"":
                    $ herView.hideshowQQ( "body_120.png", pos )
                    her "Хм..."
                    $ herView.hideshowQQ( "body_117.png", pos )
                    her "Как насчет вас, сэр?"
                    her "Вы были таким же, когда были юны?"
                    m "Нравилось ли мне наблюдать за двумя развлекающимися девушками?"
                    m "Ну конечно."
                    m "Как и сейчас..."
                    $ herView.hideshowQQ( "body_120.png", pos )
                    her "Ох..."
                "\"Целующиеся девушки? Где?!!\"":
                    $ herView.hideshowQQ( "body_76.png", pos )
                    her "Тск!......................"


            $ herView.hideshowQQ( "body_87.png", pos )
            her "Ну, я спрашиваю вас только потому, сэр..."
            $ herView.hideshowQQ( "body_117.png", pos )
            her "...что в нашей школе это что-то вроде новой моды..."
            her "И некоторые девушки таким способом привлекают внимание парней..."
            m "Вы одна из тех девушек, мисс Грейнджер?"
            $ herView.hideshowQQ( "body_118.png", pos )
            her "Наверное..."
            $ herView.hideshowQQ( "body_120.png", pos )
            her "В смысле, это только из-за услуг, что вы у меня покупаете, сэр..."
            m "Хорошо... Расскажи мне больше."
            $ herView.hideshowQQ( "body_80.png", pos )
            her "Ну, как вы знаете, я достаточно популярна..."
            $ herView.hideshowQQ( "body_74.png", pos )
            her "Так что все, что мне надо было сделать, так это просто намекнуть, что я не прочь заняться этим сегодня..."
            her "И тут же выстроилась очередь..."
            $ herView.hideshowQQ( "body_45.png", pos )
            her "Конечно, я выбрала девушку из \"Гриффиндора\"..."
            $ herView.hideshowQQ( "body_31.png", pos )
            her "И мы устроили небольшое шоу прямо посреди класса..."
            m "Хорошо... С языком и всем прочим?"
            $ herView.hideshowQQ( "body_29.png", pos )
            her "С языком и всем прочим, сэр."
            m "Отличная работа."
            $ herView.hideshowQQ( "body_45.png", pos )

    elif hermi.whoring >= 18:
        if one_out_of_three == 1:
            label snowballing:
                pass
            m "Мисс Грейнджер..."
            show screen blktone
            with d3
            $ herView.hideshowQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            her "Добрый вечер, сэр."
            m "Вы выполнили свое задание?"
            $ herView.hideshowQQ( "body_15.png", pos )
            her "Да, сэр."
            m "Я весь внимание..."
            $ herView.hideshowQQ( "body_17.png", pos )
            her "Ну, я поцеловала ту неприятную блондинку из \"Слизерина\"..."
            m "Хм... \"неприятную\", да?"
            m "Потому что она из \"Слизерина\"?"
            $ herView.hideshowQQ( "body_16.png", pos )
            her "Именно, сэр."
            m "Хм..."
            m "Ты не думаешь, что это предрассудок с твоей стороны?"
            m "Или, может, ты становишься \"факультистом\"?"
            $ herView.hideshowQQ( "body_185.png", pos )
            her "...\"факультистом\", сэр?"
            m "Ну, знаешь... Как \"сексист\" или \"расист\"..."
            m "Просто поставь \"ист\" после какого-нибудь слова и это сразу же станет плохой штукой..."
            $ herView.hideshowQQ( "body_13.png", pos )
            her "Слова \"факультист\" не существует, сэр..."
            m "Не существует? Тогда подожди..."
            $ herView.hideshowQQ( "body_185.png", pos )
            her ".............?"
            m "\"Факультофобия\"...?"
            m "Нет, стой, я понял!"
            m "\"Факультофоб\"!"
            $ herView.hideshowQQ( "body_07.png", pos )
            her "Прекратите, сэр. Я не имею отношения к этим странным словам..."
            her "\"Слизеринцы\" злые и надменные. Никто их не любит, и это факт!"
            m "Ладно, пофиг. Тогда вернемся к \"девчачьим поцелуйчикам\"."
            $ herView.hideshowQQ( "body_29.png", pos )
            her "..............."
            her "Как я и говорила..."
            $ herView.hideshowQQ( "body_31.png", pos )
            her "Я поцеловала ту девушку из \"Слизерина\"..."
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Конечно, в обычной ситуации я бы никогда этого не сделала..."
            her "Уж точно не с кем-нибудь с этого жалкого факультета..."
            $ herView.hideshowQQ( "body_79.png", pos )
            her "Но она подошла ко мне сама и практически умоляла меня сделать это с ней..."
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Именно сегодня..."
            her "Если честно..."
            $ herView.hideshowQQ( "body_79.png", pos )
            her "Она была довольно-таки привлекательной..."
            $ herView.hideshowQQ( "body_120.png", pos )
            her "Для кого-то из \"Слизерина\"..."
            $ herView.hideshowQQ( "body_127.png", pos )
            her "Я не спросила, почему ей это было так нужно..."
            her "Возможно, она просто пыталась с моей помощью увеличить свою популярность..."
            her "Или кто-то из школьного персонала купил у нее эту услугу..."
            $ herView.hideshowQQ( "body_186.png", pos )
            her "Так же, как вы покупаете услуги от меня, сэр..."
            m "(Снейп?)"
            $ herView.hideshowQQ( "body_47.png", pos )
            her "Если это так, то я уверена, что это был профессор Снейп..."
            m "Что? Да он бы никогда..."
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Вы в самом деле должны разобраться в делишках профессор Снейпа, сэр..."
            m "Конечно..."
            m "Пока мы говорим, я заношу его в мой \"список плохих мальчиков\"..."
            $ herView.hideshowQQ( "body_66.png", pos )
            her ".........."
            m "Что произошло дальше?"
            $ herView.hideshowQQ( "body_87.png", pos )
            her "Ох, точно..."
            her "Ну, мы немного поразвлекались..."
            her "Она была очень... страстной."
            $ herView.hideshowQQ( "body_122.png", pos )
            her "Мне кажется, что это было то еще зрелище..."
            her "Парни свистели и подбадривали..."
            $ herView.hideshowQQ( "body_124.png", pos )
            her "В общем, мы решили немного \"поиграть в снежки\"..."
            m "Простите, что вы решили?"
            $ herView.hideshowQQ( "body_122.png", pos )
            her "\"Поиграть в снежки\", сэр."
            $ herView.hideshowQQ( "body_128.png", pos )
            her "Это когда одна девушка плюет в рот другой девушке..."
            her "Мы называем это \"снежками\"..."
            her "Почему-то парни сходят с ума от такого..."
            m "Могу себе представить..."
            $ herView.hideshowQQ( "body_127.png", pos )
            her "В общем, она плюнула в мой рот..."
            her "А затем я плюнула в ее..."
            $ herView.hideshowQQ( "body_187.png", pos )
            her "Хотя намного больше мне хотелось плюнуть ей в лицо!"
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Затем она вернула мой плевок..."
            $ herView.hideshowQQ( "body_187.png", pos )
            her "Я с трудом поборола желание врезать ей по наглой роже..."
            $ herView.hideshowQQ( "body_120.png", pos )
            her "Но я думаю, что парни этого бы не оценили..."
            m "Ох, как вы ошибаетесь..."
            $ herView.hideshowQQ( "body_124.png", pos )
            her "В любом случае, после этого мы целовались еще какое-то время..."
            her "И перемена закончилась..."
            $ herView.hideshowQQ( "body_122.png", pos )
            her "И мне пришлось бежать в класс..."
            m "*Вздох...* Беззаботные и невинные школьные деньки..."
            m "Уроки... Домашние задания..."
            m "Школьницы, \"играющие в снежки\" во дворе..."
            m "Отличная работа, мисс Грейнджер."
            $ herView.hideshowQQ( "body_68.png", pos )


        elif one_out_of_three == 2:
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $ herView.hideshowQQ( "body_16.png", pos )
            her "Выполнила, сэр."
            $ herView.hideshowQQ( "body_68.png", pos )
            her "Только... эм..."
            m "Что такое?"
            $ herView.hideshowQQ( "body_45.png", pos )
            her "Ну... У меня есть подруга..."
            her "Ее зовут Джинни Уизли..."
            $ herView.hideshowQQ( "body_188.png", pos )
            her "И... эм..."
            her "Я не знаю, как это сказать..."
            m "Просто скажи это, девочка."
            $ herView.hideshowQQ( "body_31.png", pos )
            her "Ну, мы решили вместе прогулять урок зельеварения..."
            her "И вместо него подготовиться к тесту по травничеству..."
            her "Ну, мы с Джинни учились..."
            her "И болтали о парнях..."
            m "Естественно..."
            $ herView.hideshowQQ( "body_189.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
            her "И тогда я, вроде как, поцеловала ее..."
            $ herView.hideshowQQ( "body_128.png", pos )
            her "И Джинни вернула мой поцелуй с такой страстью..."
            her "Что у нас все кончилось больше, чем просто поцелуями..."
            g9 "После этого у вас была битва подушками в одном лишь нижнем белье?"
            $ herView.hideshowQQ( "body_190.png", pos )
            her "Эмм... Нет..."
            m "Тогда что вы сделали?"
            $ herView.hideshowQQ( "body_188.png", pos )
            her "Я не скажу вам, сэр."
            her "Вы посылали меня поцеловать девушку..."
            her "И я именно это и сделала."
            $ herView.hideshowQQ( "body_122.png", pos )
            her "Остальные происшествия могут быть моими маленькими тайнами."
            m "Это жестоко, маленькая ты ведьма."
            $ herView.hideshowQQ( "body_64.png", pos )
            her "Мои очки, пожалуйста."
            m "Ладно..."


        elif one_out_of_three == 3:
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            $ herView.hideshowQQ( "body_56.png", pos )
            her "Простите, сэр, я немного задержалась."
            $ herView.hideshowQQ( "body_84.png", pos )
            m "Эх, жаль…"
            m "Я имел в виду, хорошо, что вы все-таки пришли."
            m "Вы прямо сияете от счастья. Думаю, вам есть, что мне рассказать."
            $ herView.hideshowQQ( "body_64.png", pos )
            her "Еще как!"
            $ herView.hideshowQQ( "body_127.png", pos )
            her "Я решила немного поменять способ. Эти искусственные лесбиянки и би-шлюшки, которым плевать вообще на то, кто с ними…"
            $ herView.hideshowQQ( "body_58.png", pos )
            her "Они мне надоели…"
            m "Так вы выполнили задание?"
            $ herView.hideshowQQ( "body_129.png", pos )
            her "Конечно же!"
            $ herView.hideshowQQ( "body_59.png", pos )
            her "Просто я решила сделать это для себя, а не для других."
            m "Хм. То есть вы очков не хотите?"
            $ herView.hideshowQQ( "body_51.png", pos )
            her "Профессор, вас это решение не касается."
            $ herView.hideshowQQ( "body_50.png", pos )
            her "Я имела в виду, я поцеловалась... не с лесбиянкой… и не как лесбиянка…"
            g9 "Вот отсюда поподробнее..."
            $ herView.hideshowQQ( "body_56.png", pos )
            her "У нас на факультете есть одна девушка."
            $ herView.hideshowQQ( "body_78.png", pos )
            her "Она просто секси…"
            $ herView.hideshowQQ( "body_55.png", pos )
            her "Но она мало того, что к девушкам холодна, так у нее есть парень."
            g9 "Мне уже интересно, что будет дальше."
            $ herView.hideshowQQ( "body_16.png", pos )
            her "Каждый вечер ее парень пробирается к нам в спальню и… немного с ней шалит…"
            $ herView.hideshowQQ( "body_15.png", pos )
            m "А вы это просто так позволяете?"
            $ herView.hideshowQQ( "body_189.png", pos )
            her "Профессор, этот парень - просто мачо…"
            $ herView.hideshowQQ( "body_101.png", pos )
            m "И вы просто так позволяете им веселиться без вас?"
            $ herView.hideshowQQ( "body_87.png", pos )
            her "Профессор!"
            $ herView.hideshowQQ( "body_66.png", pos )
            m "Облепили бы парня своими голыми телами, облизывали бы ему по очереди…"
            $ herView.hideshowQQ( "body_86.png", pos )
            her "ПРОФЕССОР!"
            $ herView.hideshowQQ( "body_61.png", pos )
            m "Молчу…"
            $ herView.hideshowQQ( "body_62.png", pos )
            her "ВЫНЬТЕ РУКИ ИЗ-ПОД СТОЛА!"
            $ herView.hideshowQQ( "body_73.png", pos )
            g4 "Да что ж ты за человек…"
            $ herView.hideshowQQ( "body_69.png", pos )
            her "Так вот…"
            $ herView.hideshowQQ( "body_93.png", pos )
            her "Я предлагала, но девчонки не хотят…"
            $ herView.hideshowQQ( "body_51.png", pos )
            her "Руки, сэр!"
            $ herView.hideshowQQ( "body_66.png", pos )
            g4 "..."
            $ herView.hideshowQQ( "body_59.png", pos )
            g9 "Ну так что было дальше?"
            $ herView.hideshowQQ( "body_102.png", pos )
            her "Она не может спать при свете. Любом. Поэтому она спит в ночной маске-очках. И вот сегодня опять приходил ее парень. Потом он услышал шум и пошел прятаться. А она легла и надела эти очки."
            $ herView.hideshowQQ( "body_58.png", pos )
            g9 "Я в предвкушении..."
            $ herView.hideshowQQ( "body_17.png", pos )
            her "Кто бы сомневался…"
            $ herView.hideshowQQ( "body_16.png", pos )
            her "Моя кровать была недалеко, а практически все девочки уже спали. Я тихонько встала и подошла к ее кровати."
            $ herView.hideshowQQ( "body_15.png", pos )
            g9 "Продолжай…"
            $ herView.hideshowQQ( "body_189.png", pos )
            her "Я присела рядом и склонилась над ее лицом."
            $ herView.hideshowQQ( "body_121.png", pos )
            her "Она была такая классная…"
            $ herView.hideshowQQ( "body_102.png", pos )
            her "Она едва слышно спросила “Это ты?”. Я попыталась гукнуть в ответ низким голосом. Её руки потянулись к моему лицу…"
            $ herView.hideshowQQ( "body_78.png", pos )
            g9 "(Чувствую, мои руки уже тоже тянутся кое-куда...)"
            $ herView.hideshowQQ( "body_106.png", pos )
            her "Я не стала испытывать удачу и впилась ей в губы первой…"
            $ herView.hideshowQQ( "body_196.png", pos )
            her "Это было так нежно и искренне…"
            $ herView.hideshowQQ( "body_57.png", pos )
            her "Она потянулась к моей промежности, но, дабы ее не напугать, я взяла её руку и проводила ей же в трусы…"
            $ herView.hideshowQQ( "body_106.png", pos )
            her "Она так мягко прикусывала мои губы… "
            $ herView.hideshowQQ( "body_56.png", pos )
            m "И она все еще не понимала, что ты не то, что не ее парень - ты вообще не парень?"
            $ herView.hideshowQQ( "body_200.png", pos )
            her "Она была сонной..."
            $ herView.hideshowQQ( "body_198.png", pos )
            her "К тому же она меня не лапала… Просто копалась в волосах…"
            $ herView.hideshowQQ( "body_189.png", pos )
            her "А ее парень был с шикарной шевелюрой. Почти как у меня, но только блондин. Это скорее ее парня можно перепутать с девушкой…"
            $ herView.hideshowQQ( "body_196.png", pos )
            her "Затем я начала по привычке к ней приставать… залезла в трусы… под пижаму… Это было просто потрясающе…"
            $ herView.hideshowQQ( "body_188.png", pos )
            m "Я вижу по глазам. Что было дальше?"
            $ herView.hideshowQQ( "body_190.png", pos )
            her "Ну… Затем я услышала шум и быстро отступилась. Ее парень возвращался. Я не теряя времени бесшумно нырнула в постель, аккуратно глядя в ее сторону."
            $ herView.hideshowQQ( "body_122.png", pos )
            her "Парень вернулся и тут же едва слышно спросил “Ты еще пока не уснула?”. Она аж с кровати подскочила. Стянула маску и спросила “Где ты был?”."
            $ herView.hideshowQQ( "body_75.png", pos )
            her "Он ответил: “Прятался в гостиной”. Она начала подозрительно оглядывать все вокруг. Кажется, в этот момент до нее дошло, что это был не он."
            $ herView.hideshowQQ( "body_189.png", pos )
            m "Ну ты и стервочка…"
            $ herView.hideshowQQ( "body_60.png", pos )
            her "Потом она сказала, что очень устала и выпроводила его из спальни. Но сама не уснула. Еще некоторое время я смотрела, как она играла с собой, скинув одеяло… "
            $ herView.hideshowQQ( "body_121.png", pos )
            her "Она повторяла наши движения и трогала себя так, как ее трогала я. Готова поспорить, она ждала меня. И, может даже, звала… "
            $ herView.hideshowQQ( "body_128.png", pos )
            g9 "И ты вновь подошла к ней…"
            $ herView.hideshowQQ( "body_189.png", pos )
            her "Нет, сэр. Я, вот, пришла к вам доложить…"
            $ herView.hideshowQQ( "body_119.png", pos )
            g4 "ЧЕГО?!"
            $ herView.hideshowQQ( "body_117.png", pos )
            her "Профессор, вы говорили…"
            $ herView.hideshowQQ( "body_118.png", pos )
            g4 "Да плевать, что я говорил! Мигом лети к ней, пока она не уснула!"
            $ herView.hideshowQQ( "body_55.png", pos )
            her "Но как же…"
            $ herView.hideshowQQ( "body_56.png", pos )
            g4 "Да будут тебе очки, сколько захочешь!"
            $ herView.hideshowQQ( "body_53.png", pos )
            m "Вернее, сколько заслужишь."
            $ herView.hideshowQQ( "body_08.png", pos )
            her "Вы хотите..."
            $ herView.hideshowQQ( "body_203.png", pos )
            g4 "Мне не нужны никакие подробности! Просто не смей ее оставлять в таком виде!"
            $ herView.hideshowQQ( "body_206.png", pos )
            her "Хорошо, сэр."
            $ herView.hideshowQQ( "body_57.png", pos )
            g9 "Давай, натри ей там всё за меня! И если она спит, засунь ей язык так глубоко между ног, чтобы она мигом проснулась!"
            $ herView.hideshowQQ( "body_108.png", pos )
            her "Эм... я постараюсь... а..."
            $ herView.hideshowQQ( "body_55.png", pos )
            g4 "Вон из кабинета…"
            $ herView.hideQ()


    $ gryffindor +=45

    if not (hermi.whoring >= 18 and one_out_of_three == 3):
        m "45 очков \"Гриффиндору\"!"
        her "Спасибо, сэр."

    hide screen bld1
    $ herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400
    $ walk_xpos2=610
    $ hermione_speed = 02.0
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3')
    with Dissolve(.3)

    $ request_20_points += 1
    $ request_20 = False
    $ hermione_sleeping = True

    call music_block

    if hermi.whoring >= 18 and one_out_of_three == 3:
        m "Вот теперь она точно кувыркается с кем-то в постельке."
        m "А меня ждет незабываемая ночь с моими руками."
        m "Эх… ну почему я не сексуальная студентка-лесбиянка?.."

    $ wtevent.Finalize()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
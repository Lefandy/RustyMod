



label new_request_02_c:

    $ herView.hideQQ()
    m "{size=-4}(Заставить ее флиртовать с учителем?){/size}"
    $ menu_x = 0.5
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас)\"":
            $ wtevent.NotFinished()
            jump new_personal_request

    m "Мисс Грейнджер, я хочу, чтобы вы флиртовали с учителем."
    if hermi.whoring <=2 or request_02_b_points <= 1:
        jump too_much

    $ pos = POS_140

    if request_02_c_points == 0 and hermi.whoring <= 8:

        $ herView.showQQ( "body_01.png", pos )
        her "Я постараюсь, сэр!"
        $ herView.hideshowQQ( "body_02.png", pos )
        her "Я рада, что вы наконец предложили это мне!"
        m "Да?"
        $ herView.hideshowQQ( "body_07.png", pos )
        her "Вы наконец-то решили устроить проверку учителям, которые обменивают очки на услуги, не так ли?"
        $ herView.hideshowQQ( "body_16.png", pos )
        her "Для меня большая честь выступить в качестве приманки."
        m "Эм... Да, именно этим мы и займемся."
        $ herView.hideshowQQ( "body_07.png", pos )
        her "Отлично! Можете рассчитывать на меня!"
    else:
        $ herView.hideshowQQ( "body_07.png", pos )
        her "Я зайду к вам с подробностями вечером."
        m "Буду ждать..."


    her "Ну, мне следует идти. Занятия вот-вот начнутся..."


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

    $ wtevent.Finalize()

    jump day_main_menu



label new_request_02_c_complete:
    $ walk_xpos=520
    $ walk_xpos2=400
    $ hermione_speed = 02.0
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

    if hermi.whoring >= 6 and hermi.whoring <= 8 and one_out_of_three == 2:
        $ herView.data().saveState()
        $ herView.data().addItem( 'item_autograph' )

    $ herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    her "Добрый вечер, сэр."
    m "Мисс Грейнджер..."
    m "Вы справились с заданием?"
    her "Я сделала, что вы просили, сэр..."
    menu:
        "\"Отлично, вот твои очки\"":
            pass
        "\"Теперь поподробнее\"":
            $ herView.hideQQ()
            m "Скажите, со сколькими учителями вы заигрывали, Мисс Грейнджер?"
            m "Мне нужны подробности."
            show screen blktone
            with d3

            if hermi.whoring >= 3 and hermi.whoring <= 5:
                if one_out_of_three == 1:
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    $ herView.hideshowQQ( "body_10.png", pos )
                    her "Ну, я попыталась заигрывать с профессором Флитвиком..."
                    $ herView.hideshowQQ( "body_09.png", pos )
                    her "Но это не сработало..."
                    $ herView.hideshowQQ( "body_12.png", pos )
                    her ".............................."
                    m "Как замечательно..."
                    m "Это все, что вы сделали сегодня, Мисс Грейнджер?"
                    $ herView.hideshowQQ( "body_11.png", pos )
                    her "Д-да..."
                    her "Но сэр, я знаю \"грязные\" факты о профессоре Флитвике!"
                    her "Всем известно, что из-за его роста..."
                    $ herView.hideshowQQ( "body_13.png", pos )
                    her "Он иногда... Эм..."
                    $ herView.hideshowQQ( "body_29.png", pos )
                    her "Он любит заглядывать под юбки учениц, сэр!"
                    m "Это еще не все?"
                    $ herView.hideshowQQ( "body_31.png", pos )
                    her "Что?"
                    m "Я имею в виду, он нам всем нравится, и мы возмущены таким поведением профессора Флик-флика."
                    $ herView.hideshowQQ( "body_07.png", pos )
                    her "Э-э... \"Профессор Флитвик\", сэр."
                    m "Верно. Внесем его в мой \"список непослушных мальчиков\", как я и говорил."
                    $ herView.hideshowQQ( "body_17.png", pos )
                    her "......................"
                    m "Ну, не хочу это говорить, но вы очень плохо выполнили свою работу, Мисс Грейнджер."
                    $ herView.hideshowQQ( "body_12.png", pos )
                    her "................................"

                    $ pos = POS_140

                    menu:
                        "\"Остаетесь без очков!\"":

                            $ herView.hideshowQQ( "body_28.png", pos )
                            her "но профессор, я сделала все, что смогла!"
                            $ herView.hideshowQQ( "body_67.png", pos )
                            her "Вы не можете отказаться от своего обещания!"
                            m "......................."
                            $ herView.hideshowQQ( "body_32.png", pos )
                            stop music fadeout 1.0
                            her "Это не подобает директору школы!"
                            m "Вы провалились, Мисс Грейнджер."
                            $ herView.hideshowQQ( "body_76.png", pos )
                            her "Арх!"
                            $ hermi.liking -= 18
                            call music_block
                            jump could_not_flirt_02
                        "\"Хотя, вы заслужили эти очки.\"":
                            $ herView.hideQQ()
                            $ pos = POS_140
                            $ herView.showQQ( "body_28.png", pos )
                            her "Правда?"
                            $ herView.hideshowQQ( "body_75.png", pos )
                            her "Огромное спасибо, профессор!"

                elif one_out_of_three == 2:
                    $ herView.hideQQ()
                    $ pos = POS_140
                    $ herView.showQQ( "body_13.png", pos )
                    her ".................."
                    her "............................"
                    m "Мисс Грейнджер?"
                    $ herView.hideshowQQ( "body_11.png", pos )
                    her "Да, профессор... Мне жаль... Просто я..."
                    $ herView.hideshowQQ( "body_13.png", pos )
                    her "............"
                    m "Ты сделала, что я просил?"
                    $ herView.hideshowQQ( "body_14.png", pos )
                    her "Я пыталась, сэр. Правда..."
                    m "С кем ты пыталась заигрывать?"
                    $ herView.hideshowQQ( "body_13.png", pos )
                    her "........."
                    $ herView.hideshowQQ( "body_12.png", pos )
                    her "Профессор Снейп, сэр."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    m "Северус? Интересно..."
                    m "И как все прошло?"
                    $ herView.hideshowQQ( "body_07.png", pos )
                    her "Ужасно, сэр..."
                    her "Простите, но я правда ненавижу Профессора Снейпа, сэр!"
                    m "И почему-то я уверен, что это взаимно..."
                    m "Расскажи, что произошло."
                    $ herView.hideshowQQ( "body_09.png", pos )
                    her "Ничего не произошло, сэр. Он просто рассмеялся мне в лицо..."
                    $ herView.hideshowQQ( "body_29.png", pos )
                    her "У меня не так уж много женского очарования, но я пыталась быть милой..."

                    $ pic_for_event = "03_hp/25_pic_events/snapegrope.png"
                    show screen blkfade
                    show screen pic_event
                    pause
                    hide screen pic_event
                    hide screen blkfade

                    $ herView.hideshowQQ( "body_30.png", pos )
                    her "И он просто начал смеяться прямо мне в лицо!"
                    $ herView.hideshowQQ( "body_34.png", pos )
                    her "...действительно страшно видеть, как Профессор Снейп смеется..."
                    her "........"
                    her "Я ужасно заигрываю, простите, сэр..."
                    $ herView.hideshowQQ( "body_47.png", pos )
                    her "Но я знаю, что Профессор Снейп тоже проворачивает \"грязные\" делишки!"
                    her "Если бы вы отправили кого-то другого к нему, то все было бы иначе!"
                    m "Кого-то другого?"
                    $ herView.hideshowQQ( "body_44.png", pos )
                    her "Да! Кого-то опытного..."
                    her "Кого-то..."
                    her "Кого-то, хм..."
                    m "Распущенного?"
                    $ herView.hideshowQQ( "body_66.png", pos )
                    her "Да, я полагаю..."
                    m "Не сдавайтесь, Мисс Грейнджер. Мы сделаем из вас шлюху э-э..."
                    m "То есть женщину!"
                    $ herView.hideshowQQ( "body_79.png", pos )
                    her "..................."
                    menu:
                        "\"...Но ты не получишь очки в этот раз\"":
                            $ herView.hideshowQQ( "body_12.png", pos )
                            her "Но я старалась..."
                            $ herView.hideshowQQ( "body_34.png", pos )
                            her "И я чувствую себя очень униженной..."
                            $ herView.hideshowQQ( "body_33.png", pos )
                            her "Но я понимаю и не буду с вами спорить..."
                            call music_block
                            jump could_not_flirt_02
                        "\"Ты заслужила очки, девочка.\"":
                            pass
                elif one_out_of_three == 3:
                    stop music fadeout 1.0
                    $ herView.hideshowQQ( "body_10.png", pos )
                    her "Я пыталась флиртовать с профессором Филчем, сэр..."
                    m "Понятно. {size=-5}(Понятия не имею, кто это.){/size}"
                    $ herView.hideQQ()
                    $ pos = POS_140
                    $ herView.showQQ( "body_11.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    her "Да, знаю, технически он не учитель..."
                    m "А?"
                    $ herView.hideshowQQ( "body_01.png", pos )
                    her "Но он является частью персонала школы..."
                    her "И мы нашли общий язык с ним!"
                    her "Он на удивление милый."
                    her "Но я не знаю ничего о его \"грязных\" делах, сэр."
                    translators "Filtch - мистер Филч. Filth - грязь."
                    m "Ага... Мистер Гряз{size=+7}ик{/size} исключен из списка."
                    $ herView.hideshowQQ( "body_07.png", pos )
                    her "\"Мистер Филч\", сэр..."
                    m "А я что сказал?"


            elif hermi.whoring >= 6 and hermi.whoring <= 8:
                if one_out_of_three == 1:
                    stop music fadeout 1.0
                    $ herView.hideQQ()
                    $ pos = POS_140
                    $ herView.showQQ( "body_10.png", pos )
                    her "Ну, профессор Слагхорн пригласил меня к себе..."
                    her "Профессор просто пригласил меня на чашечку чая..."
                    $ herView.hideshowQQ( "body_16.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    her "Там было несколько девочек..."
                    her "Но все из них были намного младше меня..."
                    $ herView.hideshowQQ( "body_17.png", pos )
                    her "Почти каждая из них была первокурсницей..."
                    $ herView.hideshowQQ( "body_16.png", pos )
                    her "Пы пили чай и ели печеньки..."
                    her "Все было довольно безобидно..."
                    m "Ты флиртовала с кем-то или нет?"
                    her "Флиртовала..."
                    $ herView.hideshowQQ( "body_17.png", pos )
                    her "Ну, то есть, я пыталась..."
                    her "Профессор Слагхорн, кажется, более заинтересован в молодых девочках..."
                    m "Вы будто ревнуете его, Мисс Грейнджер."
                    $ herView.hideshowQQ( "body_18.png", pos )
                    her "Что?!"
                    $ herView.hideshowQQ( "body_69.png", pos )
                    her "Это нелепо!"
                    m "Вот ваши очки..."
                    her "...................."

                elif one_out_of_three == 2:
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    $ herView.hideQQ()
                    $ pos = POS_140
                    $ herView.showQQ( "body_80.png", pos )
                    her "Это был удивительный день, сэр!"
                    m "Ну же, расскажите, Мисс Грейнджер..."
                    $ herView.hideshowQQ( "body_68.png", pos )
                    her "У меня были занятия у профессора Локонса..."
                    her "сэр Локонс, он такой милый и умный..."
                    $ herView.hideshowQQ( "body_78.png", pos )
                    her "И идеальный..."
                    m "Избавьте меня от вашей школьной влюбленности, Мисс Грейнджер."
                    $ herView.hideshowQQ( "body_80.png", pos )
                    her "сэр Локонс был так любезен, что дал мне свой автограф..."
                    m "Как мило с его стороны."
                    $ herView.hideshowQQ( "body_68.png", pos )
                    her "Да, не могу дождаться, когда покажу его девочкам!"
                    m "Хм.. Могу я увидеть его?"
                    $ herView.hideshowQQ( "body_45.png", pos )
                    her "Сэр?"
                    m "Автограф, девочка. Могу я его увидеть?"
                    $ herView.hideshowQQ( "body_44.png", pos )
                    her "Ну... Эм... Он в весьма тайной зоне, сэр."
                    m "Что? Ну, следовательно, у профессора Локонса есть какие-то \"грязные\" делишки!"
                    $ herView.hideshowQQ( "body_69.png", pos )
                    her "Это профессор Локонс, сэр..."
                    her "И... Эм..."
                    her "Ну, это не {size=+5}настолько{/size} укромное место..."
                    m "Покажи его мне!"
                    $ herView.hideshowQQ( "body_66.png", pos )
                    her "Нет, сэр! Это было бы неуместно!"
                    menu:
                        "{size=-3}\"Профессор Локонс вылетит из школы в ближайшее время!\"{/size}":
                            $ herView.hideshowQQ( "body_72.png", pos )
                            her "Из-за меня?"
                            $ herView.hideshowQQ( "body_67.png", pos )
                            her "Сэр, пожалуйста!"
                            m "Покажи мне!"
                            $ herView.hideshowQQ( "body_32.png", pos )
                            her "Нет, мне стыдно!"
                            menu:
                                "\"Ладно. Вот твои очки.\"":
                                    $ herView.hideshowQQ( "body_74.png", pos )
                                    her "Спасибо за понимание, сэр."
                                "\"Покажи мне, или ты не получишь ничего!\"":
                                    $ herView.hideshowQQ( "body_72.png", pos )
                                    her "Что?!"
                                    $ herView.hideshowQQ( "body_73.png", pos )
                                    her "..............."
                                    $ herView.hideshowQQ( "body_29.png", pos )
                                    her ".................."
                                    $ herView.hideshowQQ( "body_47.png", pos )
                                    her "Ну, ладно, но только, чтобы очистить имя моего кумира..."
                                    $ herView.hideQQ()
                                    show screen blktone8
                                    with d5
                                    $ her_head_state = 12
                                    her_head_main "Вот...."
                                    m "Хм..."
                                    hide screen blktone8 
                                    with d5


                                    $ hermi.WrdUpSkirt()
                                    $ herView.data().addItem( 'item_autograph' )


                                    $ herView.showQ( "body_51.png", pos )
                                    hide screen ctc
                                    show screen ctc
                                    with d3
                                    pause
                                    $ herView.hideshowQQ( "body_50.png", pos )
                                    her "Как вы понимаете, профессор Локонс очень смелый и воплощает в себе все чистое."
                                    pause
                                    m "Что мне теперь делать?"
                                    her "Можете не беспокоиться об этом, сэр."
                                    her "Он не один из \"пошлых\" учителей."
                                    m "Ах, да какое мне дело..."
                                    $ herView.hideshowQQ( "body_51.png", pos )
                                    her "............?"
                                    $ herView.hideQQ()

                                    $ herView.showQ( "body_47.png", pos, fade )
                                    pause
                                    hide screen ctc
                                    $ hermi.liking -= 18
                        "\"Ладно... Вот твои очки.\"":
                            $ herView.hideshowQQ( "body_74.png", pos )
                            her "Спасибо за понимание, профессор."

                elif one_out_of_three == 3:
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    $ herView.hideQQ()
                    $ pos = POS_370
                    $ herView.showQQ( "body_15.png", pos )
                    her "Ну, сегодня я некоторое время заигрывала с мистером Филчем."
                    $ herView.hideshowQQ( "body_16.png", pos )
                    her "Ну, мистел Филч очень начитанный и обладает манерами."
                    m "........"
                    $ herView.hideshowQQ( "body_13.png", pos )
                    her "Не думаю, что кто-то знает его таким..."
                    her "Не думаю, что кто-то знает мистера Филча так, как я."
                    $ herView.hideshowQQ( "body_06.png", pos )
                    her "Я чувствую, что со мной он очень открыт, сэр."
                    m "Ладно..."
                    m "Этот, мистер Фли{size=+7}нт{/size}..."
                    $ herView.hideQQ()
                    $ h_xpos=370
                    $ herView.showQQ( "body_04.png", pos )
                    her "Мистер Филч, сэр."
                    m "Да, не важно... Он учитель?"
                    her "Мистер Филч? Учитель? Нет, сэр..."
                    $ herView.hideshowQQ( "body_06.png", pos )
                    her "Он смотритель..."
                    m "Смотритель...?"
                    m "Ты имеешь в виду - дворник?"
                    $ herView.hideshowQQ( "body_10.png", pos )
                    her "Ну..."
                    m "Мисс Грейнджер, я не посылал вас очаровывать дворников!"
                    $ herView.hideshowQQ( "body_14.png", pos )
                    her "Но мистер Филч является частью школьного персонала, сэр!"
                    menu:
                        "\"Просто бери свои очки и уходи!\"":
                            $ herView.hideshowQQ( "body_03.png", pos )
                            her "........................."
                        "\"Задание провалено! Ты не получишь очки!\"":
                            $ hermi.liking -=15
                            $ herView.hideshowQQ( "body_07.png", pos )
                            her "Но профессор?"
                            m "Вы провалились, Мисс Грейнджер."
                            $ herView.hideshowQQ( "body_05.png", pos )
                            her "........................................."
                            jump could_not_flirt_02


            elif hermi.whoring >= 9:
                if one_out_of_three == 1:
                    stop music fadeout 1.0
                    $ herView.hideshowQQ( "body_33.png", pos )
                    her "............................."
                    her "....................................."
                    m "Мисс Грейнджер?"
                    $ herView.hideshowQQ( "body_34.png", pos )
                    her "Профессор, Я....."
                    m "Что такое? Что произошло?"
                    $ herView.hideshowQQ( "body_29.png", pos )
                    her "Ну..."
                    her "Мистер Филч, сэр..."
                    m "Дворник?"
                    $ herView.hideshowQQ( "body_31.png", pos )
                    her "Я с ним немного флиртовала..."
                    her "И вначале все было отлично..."
                    $ herView.hideshowQQ( "body_29.png", pos )
                    her "......................."
                    m "................?"
                    $ herView.hideshowQQ( "body_31.png", pos )
                    her "А потом..."
                    $ herView.hideshowQQ( "body_29.png", pos )
                    her "Не уверена, должна ли я..."
                    m "Мисс Грейнджер, если вы не хотите говорить, можете уйти."
                    $ herView.hideshowQQ( "body_32.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    her "Он показал мне свою \"штучку\", сэр!"
                    m "Его - что?"
                    $ herView.hideshowQQ( "body_34.png", pos )
                    her "Его... мужское начало, сэр."
                    g9 "Так держать, парень-дворник!"
                    $ herView.hideshowQQ( "body_72.png", pos )
                    her "Что?!"
                    m "*Кхм* То есть - это возмутимо!"
                    $ herView.hideshowQQ( "body_21.png", pos )
                    her "Да... Мерзкий, кривой, весь в венах..."
                    m "Избавьте меня от ужасных подробностей, девушка."
                    $ herView.hideshowQQ( "body_20.png", pos )
                    her "Зачем он вообще сделал это?"
                    her "Только что мы говорили, как вдруг..."
                    m "Ну, ваша благородная жертва не должна остаться незамеченной, Мисс Грейнджер!"
                    m "Пятнадцать очков \"Грифф..."
                    $ herView.hideshowQQ( "body_19.png", pos )
                    her "Профессор Дамблдор, пожалуйста подождите."
                    m "А?"
                    $ herView.hideshowQQ( "body_31.png", pos )
                    her "Ну, вы не собираетесь что-то с этим сделать?"
                    m "Ну..."
                    $ herView.hideshowQQ( "body_47.png", pos )
                    her "Что, если я не первая жертва..?"
                    her "Какой-нибудь первокур может получить травму на всю жизнь!"
                    m "Действительно может?"
                    $ herView.hideshowQQ( "body_31.png", pos )
                    her "Это значит, что вы примете меры, сэр?"
                    m "Эм... Да, конечно..."
                    m "Занесу его в свой \"список\"..."
                    m "\"Позаботиться о дворнике и его жутко кривом члене.\"..."
                    m "Да, завтра же, в первую очередь."
                    $ herView.hideshowQQ( "body_16.png", pos )
                    her "Спасибо сэр."
                    $ herView.hideshowQQ( "body_75.png", pos )
                    her "Могу я получить свои очки?"

                elif one_out_of_three == 2:
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    $ herView.hideshowQQ( "body_76.png", pos )
                    her "Профессор Снейп!"
                    m "Эм... Ага, Я, вообще-то, Дамблдор, вроде как..."
                    $ herView.hideQQ()

                    g4 "{size=-5}(Стоп, может {size=+7}он{/size} сменил мою маскировку?){/size}"
                    g4 "{size=-5}(Значит, теперь я выгляжу как Профессор Снейп?){/size}"
                    g4 "{size=-5}(Во имя великих песков пустыни! Что они со мной сделали!){/size}"
                    $ herView.hideshowQQ( "body_02.png", pos )
                    her "Профессор? С кем вы говорили?"
                    m "Эм... Я связался с духами из другого измерения..."
                    $ herView.hideshowQQ( "body_17.png", pos )
                    her ".....??!"
                    $ herView.hideQQ()
                    $ herView.hideshowQQ( "body_02.png", pos )
                    her "Профессор Дамблдор, пожалуйста, выслушайте меня!"
                    m "Да, да, девочка. Я слушаю."
                    $ herView.hideshowQQ( "body_04.png", pos )
                    her "Я нашла подтверждение тому, что профессор Снейп коррумпирован и занимается \"грязными\" делами, сэр!"
                    m "Расскажи, что произошло."
                    $ herView.hideshowQQ( "body_02.png", pos )
                    her "ну, сегодня во время занятий..."
                    her "Я делала все возможное, чтобы привлечь внимание профессора Снейпа..."
                    her "Я \"мечтательно\" пялилась на него..."
                    her "И следила за его членом..."
                    m "Ты..."
                    m "Смотрела в сторону его члена?"
                    $ herView.hideshowQQ( "body_04.png", pos )
                    her "Да... Я имею в виду, когда вы смотрите туда и хотите кое-что от него..."
                    m "Откуда ты знаешь о таком?"
                    $ herView.hideshowQQ( "body_10.png", pos )
                    her "Женские журналы..."
                    $ herView.hideshowQQ( "body_07.png", pos )
                    her "Ну, не важно, это сработало, сэр."
                    $ herView.hideshowQQ( "body_47.png", pos )
                    her "Когда занятия закончились, Профессор Снейп схватил меня за попку, сэр!"
                    m "Дьявол!"
                    m "Тебе понравилось, не так ли?"
                    $ herView.hideshowQQ( "body_30.png", pos )
                    her "Сэр, я делаю это только для..."
                    m "Только \"во имя чести \"Гриффиндора\" и все такое. Да, помню."
                    m "Вот твои очки."
                    $ herView.hideshowQQ( "body_66.png", pos )

                elif one_out_of_three == 3:
                    stop music fadeout 1.0
                    $ herView.hideshowQQ( "body_09.png", pos )
                    her "Профессор Локонс!"
                    m "Ага! Добавим его в \"список непослушных\"!"
                    $ herView.hideshowQQ( "body_11.png", pos )
                    her "Нет, сэр, это не то..."
                    $ herView.hideshowQQ( "body_12.png", pos )
                    her "Или..."
                    her "Я не уверена..."
                    $ herView.hideshowQQ( "body_11.png", pos )
                    her "Раньше я его обожала..."
                    $ herView.hideshowQQ( "body_13.png", pos )
                    her "Но он..."
                    her "Он просто..."
                    $ herView.hideshowQQ( "body_20.png", pos )
                    her "Как это возможно?"
                    her "Я не могу поверить в это..."
                    $ herView.hideQQ()
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
                    m "{size=-4}(Арх! Ожидание убивает меня!){/size}"
                    m "{size=-4}(Может, он заставил ее сосать?){/size}"
                    m "{size=-4}(Или, может, изнасиловал?){/size}"
                    g4 "Что такое, девочка? Говори!"
                    $ herView.hideshowQQ( "body_14.png", pos )
                    her "А?"
                    m "Что профессор Локонс сделал с тобой?"
                    $ herView.hideshowQQ( "body_13.png", pos )
                    her "Эм... Ничего, сэр..."
                    m "Ничего?!"
                    $ herView.hideshowQQ( "body_11.png", pos )
                    her "Да. Я, конечно, загнала его в угол сегодня..."
                    $ herView.hideshowQQ( "body_31.png", pos )
                    her "И еще старалась выглядеть доступной для него..."
                    m "Серьезно?"
                    $ herView.hideshowQQ( "body_34.png", pos )
                    her "Да... Не уверена, что он хотел что-то от меня, сэр..."
                    m "Ну же, Мисс Грейнджер!"
                    $ herView.hideshowQQ( "body_32.png", pos )
                    her "Выслушайте меня сначала, пожалуйста!"
                    m "Мои извинения. Продолжай."
                    $ herView.hideshowQQ( "body_14.png", pos )
                    her "Ну, обычно профессор Локонс ведет себя как джентльмен..."
                    her "И... и я просто хотела очистить его имя от всех этих подозрений раз и навсегда..."
                    $ herView.hideshowQQ( "body_29.png", pos )
                    her "..............."
                    her "Ну, профессор Локонс не отверг меня..."
                    m "Ты меня убиваешь, девочка!"
                    m "Он не отверг тебя, он не изнасиловал тебя..."
                    m "Тогда что произошло?"
                    $ herView.hideshowQQ( "body_33.png", pos )
                    her "............."
                    $ herView.hideshowQQ( "body_34.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                    her "Я заставила его плакать, сэр..."
                    m "..............стоп.......что?"
                    $ herView.hideshowQQ( "body_28.png", pos )
                    her "Он озадаченно посмотрел и затем начал рыдать..."
                    her "Он смотрел на меня так, как будто боится, сэр."
                    $ herView.hideshowQQ( "body_29.png", pos )
                    her "Я думаю..."
                    her "Я думаю, мистер Локонс боится женщин..."
                    m "Боится женщин?"
                    m "Что это может значить?"
                    $ herView.hideshowQQ( "body_34.png", pos )
                    her "То, что ему нравятся мальчики, сэр?"
                    m "Ох..."
                    $ herView.hideshowQQ( "body_44.png", pos )
                    her "............"
                    m "..........."
                    m "Ну, почти уверен, что этот опыт нанес вам травму, Мисс Грейнджер."
                    $ herView.hideshowQQ( "body_31.png", pos )
                    her "Вроде, сэр..."
                    m "Ну, надеюсь эти очки поднимут тебе настроение.."



    $ gryffindor +=15
    m "\"Гриффиндор\" получает 15 очков!"
    her "Спасибо, сэр."

    hide screen bld1
    $ herView.hideQ()


    $ herView.data().loadState()
    $ hermi.WrdSetMain ()

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

    call music_block

    $ p_level_03_active = True


    if hermi.whoring <= 5:
        $ hermi.whoring +=1

    $ request_02_c_points += 1

    $ hermione_sleeping = True
    $ wtevent.Finalize()
    return

label could_not_flirt_02:
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

    $ request_02_b_points += 1
    $ wtevent.Finalize()
    jump finish_daytime_event
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii




label new_request_08:
    $ herView.hideQQ()
    if IsFirstRun():

        m "{size=-4}(Я хочу посмотреть на эти сиськи?){/size}"
    else:
        m "{size=-4}(Я хочу посмотреть на эти сиськи снова?){/size}"
    $ menu_x = 0.5
    menu:
        "\"(Да, давай попробуем!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            $ wtevent.NotFinished()
            jump new_personal_request

    if hermi.whoring <=5:
        jump too_much



    $ current_payout = 25

    $ pos = POS_140


    $ herView.data().saveState()

    if IsFirstRun() and hermi.whoring <= 11:
        m "Мисс Грейнджер?"
        $ herView.hideQQ()
        $ pos = POS_370

        $ herView.showQQ( "body_03.png", pos )
        her "Да, сэр..."
        m "Сколько стоит посмотреть на твои сиськи?"
        $ herView.hideshowQQ( "body_14.png", pos )
        stop music fadeout 1.0
        her "Сколько стоит посмотреть на...?"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        $ herView.hideshowQQ( "body_30.png", pos )
        her "Профессор Дамблдор!"
        m "Хм... Я думал, вашему факультету пригодятся дополнительные очки..."
        m "Но, видимо, я ошибался..."
        $ herView.hideshowQQ( "body_31.png", pos )
        her ".........?"
        m "Ладно, не бери в голову..."
        m "Я всего лишь хотел помочь тебе..."
        $ herView.hideshowQQ( "body_29.png", pos )
        her "............."
        $ herView.hideshowQQ( "body_33.png", pos )
        her "200 очков, сэр."
        m "Если я дам вам 200 очков, Мисс Грейнджер..."
        m "Вы оголите грудь и покажете свои дыньки?"
        $ herView.hideshowQQ( "body_47.png", pos )
        her "Профессор Дамблдор! Не надо так выражаться!"
        her "Думаю, я лучше пойду..."
        menu:
            "\"Стой. 200 очков твои. Показывай!\"":
                $ current_payout = 200
                $ herView.hideshowQQ( "body_14.png", pos )
                her "Серьезно?"
                m "Да"
                $ herView.hideshowQQ( "body_29.png", pos )
                her "......................................"
                her "Вы обещаете, что не будете трогать их, сэр?"
                m "Конечно, конечно..."
                $ herView.hideshowQQ( "body_32.png", pos )
                her "Я делаю это только ради моего факультета, сэр!"
            "\"Я дам тебе 5 очков, если ты покажешь сиськи.\"":

                $ herView.hideshowQQ( "body_72.png", pos )
                her "Пять?!"
                $ herView.hideshowQQ( "body_76.png", pos )
                her "Профессор, я не собираюсь показывать их за скромные пять очков!"
                m "Ну, твои сиськи, конечно, не стоят 200, девочка!"
                $ herView.hideshowQQ( "body_73.png", pos )
                her "(Неужели они так плохи?)"
                $ herView.hideshowQQ( "body_69.png", pos )
                her "Может быть, за сто очков?"
                menu:
                    "\"Хорошо. 100 очков твои! Показывай!":
                        $ current_payout = 100
                        her "................."
                        her "Так и быть... за сто баллов..."
                    "\"25 очков - окончательная цена!\"":
                        her "..............."
                        her "Ну, так и быть..."
            "\"Отлично, вали. Мне пофиг...\"":
                $ hermi.liking -= 12
                her "Арх!"
                call music_block

                jump loadState_and_could_not_flirt


        hide screen blktone
        with d3
        hide screen bld1
        with d3
        $ herView.hideQ( d5 )
        $ menu_x = 0.5
        show screen ctc
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
        pause
        show screen hermione_04
        with fade
        pause
        show screen bld1
        with d3
        m "Хм..."
        $ her_head_state = 12
        her_head_main "{size=-5}(Ох, я ведь еще никому не позволяла смотреть на мои...){/size}"
        m "Подойди ближе, девочка, дай как следует рассмотреть..."
        $ her_head_state = 4
        her_head_main "............"

        hide screen bld1
        with d3

        show screen blkfade 
        with Dissolve(1)
        pause.5
        ">Гермиона медленно подходит к вам."
        ">её сиськи покачиваются в такт шагам..."

        hide screen hermione_04 
        hide screen genie
        show screen ctc
        show screen genie_and_tits_01
        with d1
        hide screen blkfade
        with d5
        pause
        show screen bld1
        with d3
        $ her_head_state = 1
        her_head_main "............"
        m "Очень хорошо..."
        $ her_head_state = 4
        her_head_main "....."


        show screen blktone
        with d3
        $ herView.hideQQ()

        $ pos = POS_140






        $ hermi.WrdUpShirt ()

        $ herView.showQQ( "body_81.png", pos )
        pause
        her "...................................."
    else:


        if hermi.whoring >= 6 and hermi.whoring <= 8:
            m "Мисс Грейнджер?"
            $ her_head_state = 2
            her_head_main "Да, профессор?"
            m "Я хочу посмотреть на твои сиськи."
            $ her_head_state = 4
            her_head_main "............"
            her_head_main "Вы обещаете не трогать их, сэр?"
            m "Конечно."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            $ herView.hideQ( d5 )
            $ menu_x = 0.5
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Хм..."
            m "Подойди ближе, девочка, дай получше рассмотреть их..."
            hide screen bld1
            with d3
            show screen blkfade 
            with Dissolve(1)
            pause.5
            ">Гермиона медленно подходит к вам."
            hide screen hermione_04 
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Очень хорошо..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
            show screen blktone
            with d3
            $ herView.hideQQ()





            $ hermi.WrdUpShirt()

            $ herView.showQQ( "body_81.png", pos )


            pause
            her "...................................."




        elif hermi.whoring >= 9:
            m "Я хочу увидеть ваши сиськи, Мисс Грейнджер."
            $ her_head_state = 15
            her_head_main "Вы будете только смотреть, сэр?"
            m "Конечно..."
            if hermi.whoring >= 15:
                $ herView.hideshowQQ( "body_09.png", pos )
                her "Сэр, мы оба знаем, что вам интереснее не просто смотреть, а делать кое-что еще..."
                m "Может быть это {size=+4}ВАМ{/size} интересно, мисс Грейнджер, чтобы я делал кое-что еще?"
                $ herView.hideshowQQ( "body_17.png", pos )
                her "Сэр, не будем играть в игры. Мне нужны очки для факультета, вам нужны сексуальные услуги."
                her "Я не получаю от этого никакого удовольствия, но если это нужно вам, то готова пойти на большее, чтобы заработать."
                m "Вы теперь подрабатываете этим, мисс Грейнджер?"
                $ herView.hideshowQQ( "body_47.png", pos )
                her "Что?.. {size=+4}СЭР!{/size} Я говорю о том, чтобы заработать очки!"
                m "Ох, простите, а я было подумал..."
                $ herView.hideshowQQ( "body_51.png", pos )
                her "Вы подумали неправильно! Я никогда не опущусь до такого!"
                m "Ну хорошо, мисс, если речь идет о том, чтобы заработать побольше очков..."
                $ herView.hideshowQQ( "body_47.png", pos )
                her "Только об этом и идет, сэр!"
                m "Тогда давайте займемся вашей попкой."
                if hermi.whoring<21:
                    $ herView.hideshowQQ( "body_95.png", pos )
                    her "Попкой, сэр? В смысле, вы потрогаете..."
                    m "В смысле, я потрогаю ее своим членом..."
                    $ herView.hideshowQQ( "body_48.png", pos )
                    her "Но, сэр! Что вы такое... Я не имела в виду..."
                    m "Не имели в виду? А за что, по-вашему, я должен давать вам больше очков? За рождественскую песенку?"
                    $ herView.hideshowQQ( "body_32.png", pos )
                    her "Но я не готова, это слишком!"
                    m "Зачем же тогда вы мне морочите голову, мисс, рассказывая, что хотите заработать побольше очков?"
                    $ herView.hideshowQQ( "body_120.png", pos )
                    her "Я хочу, сэр, но не такой ценой!"
                    m "То есть, вы теперь указываете мне, девушка, за что вам платить?"
                    m "Вы знаете, мисс, я неравнодушен к Гриффиндору..."
                    m "Но из-за ваших капризов начинаю серьезно подумывать, не ошибся ли я в вас?"
                    m "Может, мне позвать кого-нибудь из слизеринок? Наверняка, они более преданы факультету."
                    m "Да! Отличная идея. Мисс Грейнджер, будьте любезны, пригласите профессоры Снейпа."
                    m "Наверняка он порекомендует мне {size=+4}ДОСТОЙНУЮ{/size} кандидатку."
                    $ herView.hideshowQQ( "body_117.png", pos )
                    her "Профессор, пожалуйста..."
                    m "Что такое, мисс Грейнджер? Вы и этого не в состоянии сделать?"
                    $ herView.hideshowQQ( "body_67.png", pos )
                    her "Профессор, я ошиблась... я была неправа... пожалуйста, простите меня."
                    m "И что будет завтра?"
                    m "Вам опять будет мало очков?"
                    her "Нет, сэр, я поняла."
                    $ herView.hideshowQQ( "body_55.png", pos )
                    her "Если вы хотите посмотреть на мои сиськи, значит я должна показать вам сиськи и не торговаться из-за очков."
                    m "..............................."
                    her "............................."
                    menu:
                        "Простить":
                            m "Похоже, вы не понимаете, мисс Грейнждер, что я подбираю вам посильные задания."
                            m "Вы должны быть благодарны."
                            $ herView.hideshowQQ( "body_29.png", pos )
                            her "Я благодарна, сэр, правда."
                            m "И в благодарность вы сегодня показываете свои сиськи бесплатно. Не так ли?"
                            $ herView.hideshowQQ( "body_103.png", pos )
                            her "Эмм... Д-да, сэр."
                            $ current_payout=0
                        "Наказать":
                            $ herView.hideshowQQ( "body_61.png", pos )
                            m "Вы понимаете, мисс, что провинились и должны быть наказаны?"
                            her "На-наверное..."
                            m "То есть, вы не уверены?"
                            $ herView.hideshowQQ( "body_103.png", pos )
                            her "Нет, я уверена... видимо."
                            m "Я не стану мучать вас сложными наказаниями, вы просто отсосете у меня. Это вы любите..."
                            $ herView.hideshowQQ( "body_47.png", pos )
                            her "Ничего подобного..."
                            m "Мне послышалось?.. Или стоит выбрать наказание серьезнее?"
                            $ herView.hideshowQQ( "body_34.png", pos )
                            her "Эмм... Хорошо, сэр. Да, я люблю."
                            m "Скажите полностью, будьте добры!"
                            $ herView.hideshowQQ( "body_47.png", pos )
                            her "Я люблю... отсасывать, сэр."
                            m "Замечательно. Но чтобы наказание не превратилось для вас в сплошное удовольствие, в этот раз я не стану платить вам."
                            her "Да, сэр."
                            m "А наоборот, вы заплатите мне за доставленное удовольствие - я вычту стоимость услуги из очков Гриффиндора."
                            $ herView.hideshowQQ( "body_130.png", pos )
                            her "Но, сэр!"
                            m "Вы считаете это несправедливым, юная леди?"
                            $ herView.hideshowQQ( "body_47.png", pos )
                            her "....................................."
                            m "Я не слышу!"
                            $ herView.hideshowQQ( "body_120.png", pos )
                            her "Ну, если вы так говорите..."
                            m "Отлично! Тогда доставьте себе удовольствие."
                            her "Вы имеете в виду, я должна?..."
                            g9 "Должны-должны, мисс. Получите удовольствие, отсасывая у меня."
                            $ current_payout=-55
                            jump blowjob_jumping
                else:
                    her "Спасибо, сэр."
                    menu:
                        "Передумать":
                            m "Впрочем, я передумал, мисс Грейнджер."
                            m "Сегодня мы ограничимся просмотром ваших сисек!"
                            $ herView.hideshowQQ( "body_50.png", pos )

                            her "................"
                            m "Приступим."
                        "\"Тогда приступим!\"":
                            m "Ну что ж..."
                            $ current_payout=95
                            jump new_request_31_start
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            $ herView.hideQ( d5 )
            $ menu_x = 0.5
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Хм..."
            m "Подойди ближе, девочка, дай получше рассмотреть их..."
            hide screen bld1
            with d3
            show screen blkfade 
            with Dissolve(1)
            pause.5
            ">Гермиона медленно подходит к вам."
            hide screen hermione_04 
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Очень хорошо..."
            show screen blktone
            with d3
            $ herView.hideQQ()







            $ hermi.WrdUpShirt()

            $ herView.showQQ( "body_84.png", pos )

            pause
            her "...................................."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 



    menu:
        "\"Солгать. Схватить за сиськи!\"":
            if hermi.whoring >= 6 and hermi.whoring <= 8:
                $ herView.hideQQ()
                show screen blkfade
                with d3
                ">Вы протягиваете руки и хватаете грудь Гермионы..."
                $ her_head_state = 7
                her_head_main "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3

                m "Расслабься, девочка. Просто стой!"
                m "Oх... Какие же у тебя классные сиськи..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                $ her_head_state = 13
                her_head_main "Нет, сэр, пожалуйста! Вы не должны..."
                m "Это не займет много времени, просто стой."
                $ her_head_state = 24
                her_head_main "Сэр, Я не соглашалась на это!"
                with hpunch
                $ her_head_state = 23
                her_head_main "Вы должны отпустить меня сейчас же!!!"
                show screen blkfade
                with d5
                ">Гермиона отстраняется от вас и спешно прикрывается."
                $ her_head_state = 19
                her_head_main "Думаю, я лучше пойду..."
                hide screen blkfade
                hide screen chair_02 
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400
                show screen hermione_02 
                with d5
                pause
                show screen bld1
                m "Вали, девочка. Ты не получишь свою оплату..."
                her_head_main "Но я показала свои..."
                $ her_head_state = 24
                her_head_main "И вы трогали меня..."
                $ her_head_state = 23
                her_head_main "И я ничего не получу?"
                m "Вы провалились, Мисс Грейнджер..."
                $ her_head_state = 19
                her_head_main "Гр.................."
                her_head_main "{size=-5}(Гори в аду, ты, ущербный старый...{/size}"
                $ hermi.liking -= 22
                call music_block
                jump loadState_and_could_not_flirt
            elif hermi.whoring >= 9 and hermi.whoring <= 11:
                $ herView.hideQQ()
                $ only_upper = False
                show screen blkfade
                with d3
                ">Вы протягиваете свои руки и хватаете сиськи Гермионы..."
                $ her_head_state = 7
                her_head_main "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Расслабься, девочка. Просто стой!"
                $ her_head_state = 4
                her_head_main "Я не соглашалась на это, сэр..."
                her_head_main "Я не думаю, что вы должны..."
                m "Тебе не нравится?.."
                $ her_head_state = 12
                her_head_main "Что?"
                m "Тебе не нравится, как я играю и сжимаю твои сиськи?"
                her_head_main "..............."
                m "Признайся, тебе это приятно..."
                her_head_main "{size=-5}(Так странно видеть мои сиськи у кого-то в руках...){/size}"
                $ her_head_state = 13
                her_head_main "сэр, Я позволяю вам делать это со мной, чтобы помочь моему факультету, ничего более!"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                $ her_head_state = 4
                her_head_main "Пожалуйста, отпустите меня!"
                show screen blkfade
                with d5
                ">Гермиона отстраняется от вас и спешно прикрывается."
                her_head_main "Вы обещали не трогать, профессор..."
                m "Так сложно удержаться..."
                hide screen blkfade
                hide screen chair_02 
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400
                show screen hermione_02 
                with d5
                pause
                show screen bld1
                $ her_head_state = 1
                her_head_main "............."
                $ her_head_state = 9
                her_head_main "Могу я получить свою оплату?"
                m "Конечно..."
                $ hermi.liking -= 9
            elif hermi.whoring >= 12:
                $ herView.hideQQ()
                show screen blkfade
                with d3
                ">Вы протягиваете свои руки и хватаете грудь Гермионы..."
                $ her_head_state = 7
                her_head_main "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Расслабься, девочка. Просто стой!"
                $ her_head_state = 12
                her_head_main "Но..."
                $ her_head_state = 13
                her_head_main "ах...{image=textheart.png}"
                $ her_head_state = 12
                her_head_main " Я не соглашалась на это..."
                m "Но тебе это нравится, не так ли?"
                $ her_head_state = 13
                her_head_main "Не совсем, сэр!{image=textheart.png}"
                show screen blktone
                with d3
                ">Вы несколько раз сжимаете её сиськи..."
                hide screen blktone
                with d3
                $ her_head_state = 15
                her_head_main "Сэр, вы обещали не трогать..."
                m "Я знаю, знаю... Но так трудно удержаться..."
                $ her_head_state = 20
                her_head_main "................."
                $ her_head_state = 6
                her_head_main "....................aх...{image=textheart.png}"
                her_head_main "Cэр, вы должны остановиться..."
                m "Еще чуть-чуть..."
                show screen blktone8
                with d3
                ">Вы продолжаете мять её сиськи..."
                hide screen blktone8
                with d3
                $ her_head_state = 37
                her_head_main "сэр... остановитесь..."
                m "Почему? Потому что тебе это очень нравится?"
                $ her_head_state = 18
                her_head_main "Нет, это не так..."
                $ her_head_state = 17
                her_head_main "Я считаю..."
                show screen blktone8
                with d3
                ">Вы тянете сиськи в разные стороны, а затем стягиваете их вместе..."
                hide screen blktone8
                with d3
                $ her_head_state = 38
                her_head_main "Aх...{image=textheart.png} сэр... я, действительно, должна идти..."
                if daytime:
                    $ her_head_state = 17
                    her_head_main "Хорошо... скоро начнутся уроки..."
                else:
                    her_head_main "Уже поздно..."
                m "Ну, хорошо..."
                show screen blkfade
                with d5
                ">Вы отпускаете ее грудь..."
                ">Гермиона прикрывается..."
                $ herView.data().loadState()
                $ hermi.WrdSetMain()
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                $ her_head_state = 25
                her_head_main "Пожалуйста, не думайте, что я забыла ваше обещание, сэр."
                m "Точно..."
                hide screen blkfade
                hide screen chair_02 
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400
                show screen hermione_02 
                with d5
                pause
                show screen bld1
                $ her_head_state = 35
                her_head_main "Могу я получить свои очки?"
                $ hermi.liking -=7
        "\"Сдержать обещание. Просто смотреть.\"":

            ">Вы долго разглядываете грудь Гермионы..."
            if hermi.whoring >= 6 and hermi.whoring <= 8:
                pause
                menu:
                    "- Одобрительно кивнуть -":
                        ">Вы смотрите на ее сиськи и одобрительно киваете..."
                        her "......................"
                    "- Показать разочарование -":
                        $ hermi.liking -= 3
                        ">Вы смотрите на сиськи девушки, а затем разочарованно качаете головой..."
                        her ".....................?"
            elif hermi.whoring >= 9 and hermi.whoring <= 11:
                pause
                menu:
                    "\"У тебя отличные сиськи.\"":
                        $ herView.hideshowQQ( "body_83.png", pos )
                        pause
                        her "Спасибо..."
                        $ herView.hideshowQQ( "body_82.png", pos )
                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                        her "..........."
                        $ herView.hideshowQQ( "body_81.png", pos )
                        her "В последнее время вы частенько говорите разные неуместные вещи, профессор."
                    "\"Хм... Видел и лучше.\"":

                        $ hermi.liking -= 7
                        $ herView.hideshowQQ( "body_83.png", pos );
                        her "Арх..."
                        her "Теперь мы закончили?"

            elif hermi.whoring >= 12:
                pause
                menu:
                    "\"У тебя отличные сиськи, девочка.\"":
                        $ herView.hideshowQQ( "body_82.png", pos )
                        her "Вы правда так думаете, профессор?"
                        $ herView.hideshowQQ( "body_84.png", pos )
                        her "Мне приятно, что вам они нравятся, сэр..."
                    "\"Ну, так себе сиськи...\"":
                        $ herView.hideshowQQ( "body_82.png", pos )
                        her "А?"
                        her "Это значит, что они вам не нравятся, сэр?"
                        $ herView.hideshowQQ( "body_85.png", pos )
                        her "Мне жаль..."
            ">Вы пялитесь на ее грудь еще какое-то время..."
            pause
            m "Ладно, ты можешь прикрыться, девочка..."
            her "............."
            $ herView.hideQQ()

            show screen blkfade
            with d3
            ">Гермиона прикрывается..."
            $ herView.data().loadState()
            $ hermi.WrdSetMain()
            hide screen chair_02 
            hide screen genie_and_tits_01
            hide screen bld1
            hide screen blktone
            show screen genie
            show screen bld1
            $ hermione_chibi_xpos = 400
            show screen hermione_02 
            with d5
        "\"Начать дрочить.\"":

            if hermi.whoring >= 6 and hermi.whoring <= 8:
                $ hermi.liking -= 2
                $ herView.hideQQ()
                ">Вы взяли свой член и начали дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                $ her_head_state = 30
                her_head_main "Профессор?!!"
                m "Просто стой, девочка..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause

                show screen bld1
                with d3
                ">Вы пялитесь на сиськи Гермионы голодными глазами..."
                $ her_head_state = 13
                her_head_main "Профессор, что вы...?"
                ">Вы продолжаете дрочить свой член..."
                $ her_head_state = 12
                her_head_main "Профессор, нет..."
                her_head_main "Вы должны... Убрать это..."
                m "Успокойся, девочка. Я же не трогаю тебя?"
                $ her_head_state = 19
                her_head_main "Но..."
                $ her_head_state = 20
                her_head_main "Но я не соглашалась на это!"
                $ her_head_state = 19
                her_head_main "Я..."
                her_head_main "думаю, мне лучше уйти!"
                menu:
                    "\"Уйдешь сейчас - не получишь очков!\"":
                        $ her_head_state = 21
                        her_head_main "После {size=+5}этого{/size}? Вы издеваетесь, сэр?"
                        her_head_main "Я показала свои..."
                        $ her_head_state = 25
                        her_head_main ".........."
                        $ her_head_state = 24
                        her_head_main "Я не желаю продолжать, профессор!"
                        show screen blkfade
                        with d3
                        ">Гермиона оттолкнула вас и прикрылась..."
                        $ herView.data().loadState()
                        $ hermi.WrdSetMain()
                        g4 "Не смей покидать меня в таком состоянии, девочка!"
                        $ her_head_state = 10
                        her_head_main "Ноги моей больше не будет в вашем кабинете, сэр!"
                        g4 "Да ладно уже, скажи что нибудь грязное! Я почти кончил!"
                        $ her_head_state = 27
                        her_head_main "Вы ужасный человек, сэр..."
                        $ hermi.liking -= 30
                        call music_block
                        jump loadState_and_could_not_flirt
                    "\"Ладно, ладно. На сегодня достаточно.\"":
                        $ hermi.liking -=9
                        pass
                    "- Дрочить быстрее -":
                        $ hermi.liking -= 35
                        ">Вы начали дрочить очень быстро!"
                        $ her_head_state = 23
                        her_head_main "Нет, профессор, стойте!"
                        ">Вы дрочите еще быстрее!"
                        $ her_head_state = 25
                        her_head_main "Профессор, думаю, я пойду..."
                        g4 "Нет, подожди, я почти кончил!"
                        show screen blkfade
                        with d3
                        $ her_head_state = 10
                        her_head_main "Иу! Профессор!"
                        her_head_main "Я ухожу!"
                        call music_block
                        jump loadState_and_could_not_flirt
            elif hermi.whoring >= 9 and hermi.whoring <= 11:
                $ herView.hideQQ()
                ">Вы взяли свой член и начали дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                $ her_head_state = 30
                her_head_main "Профессор?"
                ">Вы смотрите на сиськи Гермионы голодными глазами..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause

                show screen bld1
                with d3
                $ her_head_state = 13
                her_head_main "Профессор, я не соглашалась на это..."
                m "Чего ты жалуешься, девочка?"
                m "Я не трогаю тебя..."
                her_head_main "Да, но вы трогаете себя, сэр."
                ">Вы увеличиваете темп..."
                m "Просто стой, девочка."
                m "Скоро я закончу."
                her_head_main ".................."
                $ her_head_state = 12
                her_head_main "(Он такой большой...)"
                m "Да, вот так..."
                m "Да, с твоими голыми сиськами..."
                her_head_main ".............."
                $ her_head_state = 17
                her_head_main "ну, так и быть..."
                her_head_main "Вы можете трогать себя, сэр..."
                $ her_head_state = 1
                her_head_main "Но вы должны обещать мне не..."
                $ her_head_state = 5
                her_head_main "Не... eм..."
                $ her_head_state = 4
                her_head_main "Не закончить на меня..."
                $ her_head_state = 8
                her_head_main "Не передо мной, сэр..."
                m "Хорошо..."
                m "Ах, ты, маленькая шлюшка. Ты - дикая шлюшка!"
                $ her_head_state = 19
                her_head_main "......................."
                "Вы начали дрочить еще быстрее..."
                g4 "Да, ты знаешь что это! Да!"
                her_head_main "................"
                show screen blkfade
                with d3
                ">Вы собираетесь кончить..."
                menu:
                    "- Сдержаться, как обещали -":
                        g4 "Ох, отлично..."
                        g4 "думаю, стоит остановиться..."
                        $ her_head_state = 15
                        her_head_main "..............."
                        ">Гермиона прикрыла груди..."
                    "- Кончить -":

                        g4 "Aргх! Ты шлюшка!"
                        $ her_head_state = 21
                        her_head_main "Профе??.."
                        show screen white
                        pause.1
                        hide screen white
                        pause.2
                        show screen white
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! ДА!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $ her_head_state = 23
                        her_head_main "Профессор, нет! Вы обещали!"
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False
                        hide screen jerking_off_cum
                        with d3
                        $ her_head_state = 10
                        her_head_main "Профессор, как вы могли...?"
                        m "Ох, это было классно..."
                        show screen blktone8
                        with d3


                        call addSperm

                        $ herView.showQQ( "body_85.png", pos )
                        pause
                        her "Моя форма..."
                        her "Испорчена...."
                        m "Не беспокойся, я дам тебе очки факультета, девочка."
                        m "Ты сделала мне хорошо."
                        her "................"
                        her "Мне нужно привести себя в порядок..."
                        $ herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        with d3

                        hide screen blkfade
                        with d5

                        call delSperm





                        $ hermi.WrdSpermDried()

                        $ herView.showQQ( "body_47.png", pos )
                        pause

                        her "Как вы могли, сэр?!"
                        her "Вы дали слово!"
                        $ herView.hideQQ()
                        $ hermi.liking -= 45
            elif hermi.whoring >= 12:
                $ herView.hideQQ()
                ">Вы берете свой член и начинаете дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                $ her_head_state = 6
                her_head_main "Профессор?"
                ">Вы смотрите на сиськи Гермионы голодными глазами..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause

                show screen bld1
                with d3
                $ her_head_state = 13
                her_head_main "Профессор, я не соглашалась на это..."
                m "Чего ты жалуешься, девочка?"
                m "Я тебя не трогаю..."
                her_head_main "Да, но вы... трогаете себя, сэр."

                m "Просто стой, сука."
                m "Я скоро кончу."
                her_head_main ".................."
                m "Да... да, вот так..."
                m "Да, твои сисечки..."
                $ her_head_state = 12
                her_head_main ".............."
                $ her_head_state = 17
                her_head_main "Ну, так и быть..."
                $ her_head_state = 1
                her_head_main "Но вы должны мне пообещать..."
                $ her_head_state = 5
                her_head_main "Не... Эм..."
                $ her_head_state = 4
                her_head_main "Не кончать..."
                her_head_main "Не передо мной, сэр..."
                m "Хорошо..."
                m "Ах, ты, маленькая шлюшка. Ты - грязная шлюшка!"
                $ her_head_state = 12
                her_head_main "......................."
                ">Вы начинаете дрочить еще быстрее..."
                g4 "Да, я знаю, ты хочешь этого! Да!"
                her_head_main "................"
                show screen blkfade
                with d3

                g4 "Aргх! (Я кончаю!)"
                menu:
                    "- Сдержать обещание -":
                        g4 "Ох, ладно..."
                        g4 "Думаю, лучше остановиться..."
                        her_head_main "..............."
                        her_head_main "Эм... Я читала, что это вредно для мужчин, сэр..."
                        m "А?"
                        $ her_head_state = 13
                        her_head_main "Это вредит вашему здоровью - сдерживать себя..."
                        $ her_head_state = 12
                        her_head_main "Eм..."
                        $ her_head_state = 14
                        her_head_main "Если хотите, вы можете..."
                        g4 "Aргх! Ты шлюшка!"
                        $ her_head_state = 7
                        her_head_main "???"
                        show screen white
                        pause.1
                        hide screen white
                        pause.2
                        show screen white
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! ДА!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $ her_head_state = 9
                        her_head_main "Профессор, я не имела в виду, что вы можете ... кончить на меня, сэр..."
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False
                        hide screen jerking_off_cum
                        with d3
                        $ her_head_state = 18
                        her_head_main "Ну, что сделано, то сделано, я полагаю..."
                        m "Ох, это было классно..."
                        show screen blktone8
                        with d3

                        call addSperm

                        $ herView.showQQ( "body_85.png", pos )
                        pause
                        her "Моя форма испачкана..."
                        m "Не беспокойся, я дам тебе очки для факультета, девочка."
                        m "Ты сделала мне хорошо."
                        $ herView.hideshowQQ( "body_84.png", pos )
                        her "Спасибо, сэр."
                        $ herView.hideshowQQ( "body_83.png", pos )
                        her "мне нужно привести себя в порядок..."
                        pause
                        $ herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        hide screen blkfade
                        with d5

                        call delSperm



                        $ hermi.WrdSpermDried ()

                        $ herView.showQ( "body_45.png", pos )
                        pause
                        her "Ну, это следует сделать сейчас..."
                        $ herView.hideQQ()
                    "- Кончить -":
                        g4 "Aргх! Ты шлюшка!"
                        $ her_head_state = 7
                        her_head_main "???"
                        show screen white
                        pause.1
                        hide screen white
                        pause.2
                        show screen white
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! Да!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $ her_head_state = 13
                        her_head_main "Ах...{image=textheart.png} Так горячо...{image=textheart.png}"
                        $ her_head_state = 9
                        her_head_main "Профессор, вы обещали..."
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False
                        hide screen jerking_off_cum
                        with d3
                        $ her_head_state = 15
                        her_head_main "Ну, что сделано, то сделано, я полагаю..."
                        m "Ох, это было довольно классно.."
                        show screen blktone8
                        with d3

                        call addSperm

                        $ herView.showQQ( "body_85.png", pos )
                        pause
                        her "Моя форма испачкана..."
                        m "Не беспокойся, я дам тебе очки факультета, девочка."
                        m "Ты сделала мне хорошо."
                        $ herView.hideshowQQ( "body_84.png", pos )
                        her "Спасибо, сэр."
                        $ herView.hideshowQQ( "body_83.png", pos )
                        her "Мне надо привести себя в порядок..."
                        pause
                        $ herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        hide screen blkfade
                        with d5

                        call delSperm




                        $ hermi.WrdSpermDried()

                        $ herView.showQ( "body_45.png", pos )
                        pause
                        her "Ну, это следует сделать сейчас..."
                        $ herView.hideQQ()



    hide screen jerking_off_01
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    hide screen chair_02
    show screen hermione_02
    show screen genie
    $ hermi.WrdSetMain()
    with fade

    hide screen blkfade
    with d3

    label new_request_08_finish:
    $ gryffindor +=current_payout
    m " \"Гриффиндор\" получает [current_payout] очков!"
    stop music fadeout 10.0



    $ hermione_chibi_xpos = 400
    show screen hermione_02 
    show screen bld1
    hide screen blkfade
    with Dissolve(1)




    $ pos = POS_370
    $ herView.showQQ( "body_29.png", pos )
    her ".................."
    her "Спасибо, сэр..."
    if daytime:
        her "Теперь, если Вы не возражаете, я пойду. Мои занятия сейчас начнутся."
    else:
        her " Я лучше пойду. Пока не слишком поздно..."











    $ SetHearts(GetStage(hermi.whoring, 6, 4, 3))


    hide screen bld1
    $ herView.hideQ( Dissolve(.3) )
    $ herView.data().loadState()
    $ hermi.WrdSetMain()

    $ walk_xpos=400
    $ walk_xpos2=610
    $ hermione_speed = 02.0
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ hermione_chibi_xpos = 610
    show screen hermione_01_f 
    with Dissolve(.3)

    if hermi.whoring >= 6 and hermi.whoring <= 8:
        $ her_head_state = 12
        her_head_main "(Как унизительно... кем я стала?..)"
        $ renpy.play('sounds/door.mp3')
        hide screen hermione_01_f 
        with Dissolve(.3)
    elif hermi.whoring >= 9 and hermi.whoring <= 11:
        her_head_main "........................"
        $ renpy.play('sounds/door.mp3')
        hide screen hermione_01_f 
        with Dissolve(.3)
    elif hermi.whoring >= 12:
        $ her_head_state = 6
        her_head_main "{size=-5}(Как унизительно...){/size}"
        $ her_head_state = 24
        her_head_main "{size=-5}(Нет, Гермиона, глупая девочка!){/size}"
        her_head_main "{size=-5}(Мы делаем это, чтобы защитить честь нашего факультета!){/size}"
        $ her_head_state = 19
        her_head_main "................................."
        $ renpy.play('sounds/door.mp3')
        hide screen hermione_01_f 
        with Dissolve(.3)
    else:
        $ renpy.play('sounds/door.mp3')
        hide screen hermione_01_f 
        with Dissolve(.3)



    if hermi.whoring <= 8:
        $ hermi.whoring +=1






    $ herView.data().loadState()
    $ hermi.WrdSetMain()

    $ wtevent.Finalize()
    jump finish_daytime_event



label addTitsPose:


    $ herView.data().addItem( 'item_pose_show_tits' )
    return

label addSperm:


    $ hermi.WrdSpermDried ()

    return

label delSperm:


    $ hermi.WrdNoSpermDried ()
    return





label loadState_and_could_not_flirt:
    $ herView.data().loadState()
    $ hermi.WrdSetMain()
    jump could_not_flirt
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
label summon_snape:
    if snape_busy:
        ">Профессор Снейп недоступен."
        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu


    $ renpy.play('sounds/door.mp3')






    $ menu_x = 0.2
    $ tt_xpos=350
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_02 
    show screen bld1
    show screen snape_main
    with Dissolve(.3)


    sna "Да, что такое?"
    label snape_ready:
        pass
    menu:
        "- Поговорить -" if sfmax and not chitchated_with_snape and not daytime:
            $ chitchated_with_snape = True
            $ menu_x = 0.5

            jump snape_chitchat
        "- Поговорить -" if daytime and not chitchated_with_snape:
            $ chitchated_with_snape = True
            $ menu_x = 0.5

            jump snape_chitchat






        "- Поговорить о газете -" if nsp_pre_letter == 2 and nsp_pre_snape < 5:
            $ menu_x = 0.5
            jump newsp_pre_snape_dialog

        "- Поговорить о газете -" if nsp_newspaper_menu == 3:
            $ menu_x = 0.5
            jump newsp_pre_snape_dialog2

        "- Впечатления о газете -" if nsp_newspaper_menu >= 5:
            $ menu_x = 0.5
            jump nsp_snape_dialog_stat



        "\"Отвиснуть.\"" if not daytime and not sfmax:





            if one_of_ten == 10:
                call not_today


            elif snape_friendship >= 99 and snape_events >= 15:
                call not_today
            else:
                pass
                $ menu_x = 0.5
                jump snape_dates
        "Ничего.":
            label snape_nothing:
            stop music fadeout 1.0
            $ menu_x = 0.5
            $ screens.Hide("snape_main")
            $ snape.State("door").Visibility("body")
            if daytime:
                $ snape("~06//.....//Ну что ж, пора вернуться к работе...")
                play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
            else:
                $ snape("~06//Эмм... если это все, тогда доброй ночи.")
                play music "music/Music for Manatees.mp3" fadein 1 fadeout 1

            label snape_nothing_exit:
            $ snape_busy = True





            $ screens.Hide("snape_02", "bld1", d3 )
            $ snape.Visibility(transition=d3)
            $ renpy.play('sounds/door.mp3')
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu


label snape_dates:
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 
    show screen fireplace_fire
    hide screen genie
    hide screen chair
    hide screen desk
    show screen desk

    hide screen snape_02 
    hide screen bld1
    hide screen snape_main
    with d3


    with fade
    $ fire_in_fireplace = True

    if this.IsStep("SNAPE"):
        show screen with_snape 
        show screen fireplace_fire
        $ this.RunStep("SNAPE")


    if hero.Items.Any("wine"):
        $ hero.Items.AddItem("wine",-1)
        if not wine_not:
            $ wine_not=True
            call wine_first
        else:
            call wine_not_first





    if snape_friendship >= 5 and snape_events == 0:
        call date_with_snape_01

    elif snape_friendship >= 12 and snape_events == 1:
        call date_with_snape_02

    elif snape_friendship >= 19 and snape_events == 2:
        call date_with_snape_03

    elif snape_friendship >= 26 and snape_events == 3:
        call date_with_snape_04

    elif snape_friendship >= 33 and snape_events == 4:
        call date_with_snape_05

    elif snape_friendship >= 40 and snape_events == 5:
        call date_with_snape_06

    elif snape_friendship >= 47 and snape_events == 6:
        call date_with_snape_07

    elif snape_friendship >= 54 and snape_events == 7:
        call date_with_snape_08

    elif snape_friendship >= 61 and snape_events == 8:
        call date_with_snape_09

    elif snape_friendship >= 68 and snape_events == 9:
        call date_with_snape_10

    elif snape_friendship >= 75 and snape_events == 10:
        call date_with_snape_11

    elif snape_friendship >= 82 and snape_events == 11:
        call date_with_snape_12

    elif snape_friendship >= 89 and snape_events == 12:
        call date_with_snape_13

    elif snape_friendship >= 96 and snape_events == 13:
        call date_with_snape_14

    elif snape_friendship >= 99 and snape_events == 14:
        call date_with_snape_15
    else:


        show screen bld1
        with d3
        $ renpy.play('sounds/win_04.mp3')
        hide screen notes
        show screen notes
        ">Вы проводите вечер, болтая с профессором Снейпом.\n>Ваши отношения с ним улучшились."
        hide screen bld1
        with d3




    $ snape_friendship +=1
    hide screen desk
    if avogadro_law == True:
        $ snape_friendship +=4
    hide screen desk
    jump day_start



label special_date_with_snape:

    $ sna_head_state = 2
    sna_head_main "..........................."
    m "...............................?"
    $ sna_head_state = 3
    sna_head_main "Я ненавижу ее..."
    menu:
        "\"Да! Та еще сука!\"":
            $ sna_head_state = 1
            sna_head_main "Приятно знать, что мы одного мнения..."
            $ sna_head_state = 2
            sna_head_main "Эта девка..."
        "\"Кого ты ненавидишь?\"":
            $ sna_head_state = 1
            sna_head_main "И ты еще спрашивешь?"
            sna_head_main "Эту девку Гермиону, конечно!"
        "\"Она настолько плоха?\"":
            sna_head_main "Хуже!"

    $ sna_head_state = 2
    sna_head_main "Лучший студент..."
    $ sna_head_state = 3
    sna_head_main "Ведет все виды внеклассных мероприятий и клубов..."
    sna_head_main "Президент школьного Студенческого совета..."
    sna_head_main "Скорее всего станет старостой в ближайшее время..."
    $ sna_head_state = 2
    sna_head_main "................"
    $ sna_head_state = 3
    sna_head_main "............"
    with hpunch
    $ sna_head_state = 5
    sna_head_main "{size=+7}Я ненавижу эту гребаную ведьму!!!{/size}"
    g4 "{size=-4}(Что за...?){/size}"
    $ sna_head_state = 2
    sna_head_main ".............."
    sna_head_main "Раньше она просто раздражала, но в эти дни..."
    $ sna_head_state = 1
    sna_head_main "Она стала реальной угрозой..."
    sna_head_main "Теперь эта ведьма - официально мой самый нелюбимый ученик из всей школы..."
    m "Как насчет этого мальчишки Поттера?"
    $ sna_head_state = 6
    sna_head_main "Поттер? Ха! Да кто он такой!?"
    $ sna_head_state = 1
    sna_head_main "Нет, я серьезно..."
    sna_head_main "Более того, я скажу, что Поттер младший, взятый вместе со своим жалким отцом..."
    sna_head_main "Не вызывает у меня столько злости, сколько эта маленькая ведьма, особенно в последнее время..."
    m "Да, конечно, мы оба знаем, что это не так..."
    $ sna_head_state = 2
    sna_head_main "Да... Ты прав..."
    $ sna_head_state = 7
    sna_head_main "Этот ублюдок Джеймс Поттер действительно бесил меня-"
    $ sna_head_state = 6
    sna_head_main "Подожди, как ты узнал это?"
    m "Ну... Я читал книги..."
    sna_head_main "Что? Какие книги?"
    m "А, не важно. Я Джинн, помнишь? Я знаю всякое..."
    $ sna_head_state = 9
    sna_head_main "Хм... И все же ты хочешь, чтобы я обучил тебя..."
    m "Ну, я говорил тебе, моя магия не полностью действует в вашем мире..."
    sna_head_main "Конечно, конечно..."
    m "......"
    m "Она приходила ко мне..."
    $ sna_head_state = 10
    sna_head_main "Кто?"
    m "Девочка, Гермиона..."
    $ sna_head_state = 1
    sna_head_main "Что?!"
    $ sna_head_state = 2
    sna_head_main "Я думал, мы договорились о правиле \"никаких контактов с людьми\"."
    $ sna_head_state = 7
    sna_head_main "(Хотя в последнее время я задавался вопросом, является ли она вообще человеком...)"
    m "Я знаю ... Она была вынуждена так поступить..."
    $ sna_head_state = 1
    sna_head_main "Я полагаю она была здесь..."
    sna_head_main "Что она хотела?"

    if jerk_off_session:
        m "Я не имею понятия..."
        $ sna_head_state = 11
        sna_head_main "??"
        m "Я дрочил в течение всего времени, пока она говорила..."
        $ sna_head_state = 2
        sna_head_main "Ты..."
        sna_head_main "... делал что?"
        m "Эй, не суди меня!"
        m "Ты не знаешь, какого это - быть запертым в этой башне, как заключенный!"
        sna_head_main "Ты... т-ты..."
        $ sna_head_state = 12
        sna_head_main "......"
        $ sna_head_state = 15
        sna_head_main "Ха.... ха-ха... ХА-ХА-ХА!!!"
        m "Чт...? Что я сказал?"
        $ sna_head_state = 14
        sna_head_main "Ха-ха-ха! Ты бесподобен!"
        $ sna_head_state = 9
        sna_head_main "Все Джинны - такие... удивительные нигилисты?"
        m "Да уж... Мы - бессмертные, и, как правило, нам плевать."
        sna_head_main "Понятно..."
        $ sna_head_state = 10
        sna_head_main "К сожалению, мы, простые смертные, не можем позволить себе такую роскошь..."
    else:

        m "Не уверен, что запомнил... Она много говорила ..."
        m "Что-то насчет \"гриффиндорских\" очков... и..."
        m "Э-э ... я не обращал внимания, если честно ..."
        $ sna_head_state = 1
        sna_head_main "Пф... Наверное был загружен другим оправданным дерьмом..."
        $ sna_head_state = 7
        sna_head_main "Она знаменита этим..."


    sna_head_main "У меня занятия завтра рано, так что давай закругляться."
    m "Что насчет обучения магии и прочему?"
    $ sna_head_state = 10
    sna_head_main "Да, конечно..."
    sna_head_main "В следующий раз..."
    m "Хорошо..."





    $ this.special_date_with_snape.Finalize()
    jump day_start


label special_date_with_snape_02:
    show screen bld1
    with d5

    m "......................."
    m "Гермиона Грейнджер приходила снова..."
    $ sna_head_state = 1
    sna_head_main "Не произноси имя этой ведьмы, когда я здесь."
    $ sna_head_state = 2
    sna_head_main "..............."
    $ sna_head_state = 3
    sna_head_main "Черт возьми! Я взрослый человек, Альбус!"
    m "Меня зовут не-"
    sna_head_main "Глубокоуважаемый чародей..."
    m "Ну, ладно, проехали..."
    $ sna_head_state = 2
    sna_head_main "Почему одно крошечное.... влагалище, может вызвать во мне столько злости?!"
    $ sna_head_state = 4
    sna_head_main "Я думал, что с тобой как с моим союзником у меня будет шанс-"
    m "Бесит?"
    $ sna_head_state = 2
    sna_head_main "Да, не то слово..."
    $ sna_head_state = 16
    sna_head_main "Но все, что я делал, давало ей больше возможностей, чтобы бесить меня..."
    sna_head_main "Она даже настроила учителей против меня..."
    $ sna_head_state = 3
    sna_head_main "................."
    $ sna_head_state = 7
    sna_head_main "Ее следует убрать..."
    m "Что ты имеешь в виду?"
    with hpunch
    $ sna_head_state = 5
    sna_head_main "{size=+6}Я хочу убить ее!{/size}"
    g4 "Убить в буквальном смысле?"
    $ sna_head_state = 6
    sna_head_main "У тебя есть другое предложение?"
    m "Ты шутишь, верно?"
    sna_head_main "Я?!"
    $ sna_head_state = 11
    sna_head_main "Можешь сделать это для меня?"
    m "Эм..."
    m "Как бы я ни наслаждался убийством девочки..."
    m "Джинны не могут убивать..."
    $ sna_head_state = 7
    sna_head_main "Вздор!"
    m "И мы осуждаем убийц..."
    if jerk_off_session:
        $ sna_head_state = 17
        sna_head_main "В самом деле? Я думал, тебе плевать..."
        m "До определенной степени..."
        $ sna_head_state = 7
        sna_head_main "............."
    $ sna_head_state = 2
    sna_head_main "Ну...значит, не обращай на меня внимания..."
    sna_head_main "Это все - разговоры..."
    sna_head_main "Я бы никогда на самом деле не навредил студенту..."
    $ sna_head_state = 3
    sna_head_main "(...до поры, до времени.)"
    m "Слушай, если она настолько вредна, почему бы просто не найти менее радикальный способ борьбы с ней?"
    $ sna_head_state = 7
    sna_head_main "Ха... Порка была объявлена вне закона год назад..."
    m "Это не то, что я имею в виду..."
    $ sna_head_state = 1
    sna_head_main "А?"
    m "Она лучший студент, так?"
    $ sna_head_state = 2
    sna_head_main "Да, черт ее возьми. Эта девчонка трудоголик. Я признаю это за ней."
    m "Также она имеет превосходную репутацию."
    $ sna_head_state = 6
    sna_head_main "О, да!"
    m "И она думает, что она лучше, чем все остальные ..."
    $ sna_head_state = 17
    sna_head_main "Что ты будешь делать с этим?"
    m "Ну, кажется ее влияние исходит из репутации..."
    $ sna_head_state = 11
    sna_head_main "......................?"
    m "Что если мы отнимем это у нее?"
    $ sna_head_state = 10
    sna_head_main "Это заткнет ее, я полагаю..."
    $ sna_head_state = 2
    sna_head_main "Но как? Она практически святая."
    $ sna_head_state = 7
    sna_head_main "Даже студенты, которые ненавидят ее, тайно восхищаются ею."
    $ sna_head_state = 2
    sna_head_main "Она не провалила ни одного теста за все время здесь..."
    sna_head_main "Она всегда опережает расписание..."
    $ sna_head_state = 3
    sna_head_main "Черт, как же я ненавижу, когда она исправляет меня во время моих занятий..."
    $ sna_head_state = 6
    sna_head_main "И благодаря ей \"Гриффиндор\" далеко впереди всех остальных сейчас..."
    $ sna_head_state = 7
    sna_head_main "Даже \"Слизерин\" не так догоняет в этом году..."
    $ sna_head_state = 16
    sna_head_main "........................"
    $ sna_head_state = 6
    sna_head_main "Черт... Мне нужно больше вина..."
    m "Вино может подождать. Выслушай меня для начала!"
    $ sna_head_state = 1
    sna_head_main "Ну...?"
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label fuck_off:
    m "Хм... Итак..."
    menu:
        m "..."
        "{size=-3}\"Убедим ее в том, что она больше не лучший ученик!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            sna_head_main "Что? Ты предлагаешь оценивать ее несправедливо?"
            $ sna_head_state = 2
            sna_head_main "Ха... Дамблдор никогда не позволит-"
            $ sna_head_state = 9
            sna_head_main "Погоди-ка!"
            m "Вот именно!"
            $ sna_head_state = 18
            sna_head_main "Ты прав! Я стану оценивать ее несправедливо! Я мог бы даже подговорить других учителей!"
            sna_head_main "Я мог бы сказать, что это ваш приказ..."
            $ sna_head_state = 19
            sna_head_main "И когда настоящий Дамблдор вернется, я сделаю вид, что не знал, кто ты на самом деле. И я..."
            m "...работал на директора."
            $ sna_head_state = 10
            sna_head_main "Э-э..."
            sna_head_main "Это все еще ты, Джинн?"
            m "Да, да, все еще я..."
            $ sna_head_state = 18
            sna_head_main "Отлично."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off
        "{size=-3}\"Конечно же \"Гриффиндор\" потеряет кубок в этом году!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            $ sna_head_state = 1
            sna_head_main "Просто начать вычитать очки у них без всякой причины?"
            $ sna_head_state = 18
            sna_head_main "О, мне нравится это!"
            $ sna_head_state = 20
            sna_head_main "Есть несколько \"Слизеринских\" девиц, готовых получить дополнительные очки для своего факультета."
            $ sna_head_state = 19
            sna_head_main "Да, это великолепно сработает!"
            $ sna_head_state = 18
            sna_head_main "Ты - Гений!"
            m "Да, я и джинн, и гений. Это вообще-то одно и то же ..."
            translators "Игра слов. По-английски 'джинн' (genie), звучит сходно с 'гений' (genius)."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Испортим ее репутацию!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            $ sna_head_state = 1
            sna_head_main "Запятнаем ее репутацию?"
            sna_head_main "Эта девушка неподкупна..."
            m "Нонсенс!"
            m "Все, что нужно - это убедить ее сделать какие-то жертвы для \"блага\""
            $ sna_head_state = 9
            sna_head_main "О, ну конечно..."
            $ sna_head_state = 21
            sna_head_main "Она с удовольствием \"замарает руки\", только чтобы сохранить честь своего драгоценного \"Гриффиндора\"!"
            $ sna_head_state = 9
            sna_head_main "И когда она это сделает, у нас появятся рычаги для воздействия..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

    sna_head_main "Это может сработать!"
    m "Я тоже так думаю."
    $ sna_head_state = 19
    sna_head_main "О, я чувствую себя таким... живым сегодня!"
    $ sna_head_state = 15
    sna_head_main "Налей мне еще кубок!"
    $ sna_head_state = 19
    sna_head_main "Занятие по \"Защите от Темных Искусств \" начнется завтра позднее, чем обычно!"
    m "....."
    m "Не кажется ли тебе это немного жестоким?"
    m "Я думаю, она просто девочка..."
    $ sna_head_state = 8
    sna_head_main "Просто девочка?"
    sna_head_main "Ох, нет, нет, нет..."
    $ sna_head_state = 4
    sna_head_main "Она - воплощение чистого зла!"
    $ sna_head_state = 2
    sna_head_main "Если мы не сделаем этого сейчас..."
    $ sna_head_state = 3
    sna_head_main "Однажды я могу просто не выдержать и \"Авада Кедаврануть\" ее!"
    m "Ты можешь что?"
    $ sna_head_state = 4
    sna_head_main "Убью ее по-настоящему!"
    m "Хорошо, хорошо... Понял...."
    m "Давай выберем наименьшее из двух зол."
    $ sna_head_state = 7
    sna_head_main "Да..."
    $ sna_head_state = 6
    sna_head_main "Теперь налей мне еще вина."

    ">Вы проводите остаток вечера в компании Снейпа, запивая ваши заботы."






    hide screen bld1
    with d3
    $ days_without_an_event = 0
    $ this.special_date_with_snape_02.Finalize()
    jump day_start






















































































































label wine_first:
    m "Смотри, что у меня есть!"
    $ s_head_xpos = 330
    $ s_head_ypos = 380
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    show screen s_head2                                                                                                 
    sna "Хм..?"
    sna "Дай-ка взглянуть..."
    hide screen s_head2
    pause.1
    $ the_gift = "03_hp/18_store/27.png"
    show screen gift
    with d3
    ">Вы передаете Снейпу бутылку, которую нашли в шкафу..."
    hide screen gift
    with d3


    $ s_sprite = "03_hp/10_snape_main/24.png"
    show screen s_head2                                                                                                 
    sna2 "Эта бутылка из тайника Дамблдора!"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    show screen s_head2                                                                                                 
    sna2 "Очень дорогая и очень раритетная вещица."
    hide screen s_head2
    m "В таком случае, можем ли мы позволить себе?"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen s_head2                                                                                                 
    sna "Мы, безусловно, можем!"
    hide screen s_head2
    show screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')
    hide screen notes
    show screen notes
    ">Ваши отношения с профессором Снейпом улучшились."
    $ snape_friendship +=1
    hide screen bld1
    with d3
    return


label wine_not_first:

    $ hero("Смотри, что у меня есть!")

    pause.1








    $ screens.ShowD3("gift", par1=itsDAHR("wine")._img).Say(">Вы передаете Снейпу бутылку, которую нашли в шкафу...").HideD3("gift")

    $ s_head_xpos = 330
    $ s_head_ypos = 380



    $ snape("~05").Visibility("head")("Еще одна?")
    $ snape(RandFromSet({
        "~02// Великолепно!",
        "~02// Превосходно!",
        "~02// Бесподобно!",
        "~02// Отлично, мой друг!",
        "~05// Ты нашел тайник Альбуса или это его личный винный погреб?",
        "~02// В последнее время мне с трудом дается выпивка, но не эта!",
        "~02// Отлично! Я уже чувствую себя менее напряженным!",
        "~02// Становится все лучше и лучше!",
        "~05// Серьезно, насколько велик этот тайник?",
        "~02// Уверен, нами быть хорошо! Давай откупорим этого ублюдка!",
        }))















































    $ snape.Visibility()
    $ screens.ShowD3("bld1")

    $ renpy.play('sounds/win_04.mp3')







    $ screens.Hide("notes").Show("notes").Say(">Ваши отношения с профессором Снейпом улучшились.").HideD3("bld1")
    $ snape_friendship +=1
    return



label not_today:
    if one_out_of_three == 1:
        sna "К сожалению, я не могу сегодня..."
    elif one_out_of_three == 2:
        sna "К сожалению, у меня есть другие дела сегодня ночью..."
    elif one_out_of_three == 3:
        sna "К сожалению, у меня другие планы. Может быть, в другой раз?"

    jump snape_nothing
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
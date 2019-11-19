label nsp_theme_forest:

    $ herView.hideshowQQ( "body_01.png", pos )
    m "Скажи, что тебе известно о Запретном лесе ?"
    $ herView.hideshowQQ( "body_13.png", pos )
    her "Дайте подумать, сэр."
    her "Это лес вокруг Хогвартса, считающийся частью его территории."
    her "И там живут разные волшебные существа. И мистер Хагрид следит за порядком в нем."
    m "А еще ?"
    her "В нем опасно, сэр. Некоторые из существ агрессивны."
    m "И ?"
    $ herView.hideshowQQ( "body_15.png", pos )
    her "И ученикам запрещено ходить туда в одиночку, сэр !"
    m "Вот как ? А если у тебя... ну то есть у ученика будет разрешение директора ?"
    $ herView.hideshowQQ( "body_14.png", pos )
    her "Вы решили проверить меня, сэр ? Да, директор имеет право дать доступ в Запретный лес."
    her "Но вы же не..."
    $ herView.hideshowQQ( "body_11.png", pos )
    her "О, нет. Вы хотите отправить туда {size=+4}меня{/size} ?"
    g9 "Не волнуйся, я не предложу тебе ничего опасного."
    $ herView.hideshowQQ( "body_12.png", pos )
    her "Да, сэр."
    $ herView.hideshowQQ( "body_01.png", pos )

    return

label nsp_event_forest_1:

    if cur_level == 1:

        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_event_forest_1 == 0:

            g6 "(Если честно, я не знаю, как ее убедить. Я иссяк.)"
            $ herView.hideshowQQ( "body_11.png", pos )
            her "Почему вы молчите, сэр ?"
            her "У вас есть для меня какое-то поручение для газеты ?"
            g10 "Даже не знаю, как тебе сказать. "
            $ herView.hideshowQQ( "body_63.png", pos )
            her "Неужели что-то {size=+4}настолько{/size} обескураживающее ?"
            m "Видишь ли, у нашей редакции возникло небольшое дело в Запретном лесу."
            $ herView.hideshowQQ( "body_18.png", pos )
            her "{size=+3}В За-запретном л-лесу ?{/size}"
            her "При всем моем уважении, сэр ! Это совершенно невозможно, отправлять меня туда."
            her "Я хочу сказать, мне уже приходилось делать много вещей, которые я даже не могла представить раньше."
            her "Но рисковать жизнью, это уже слишком !"
            m "(На самом деле поход безопасен, ведь жертв ни разу не было. Но как ее убедить ?)"
            m "Но в Дурмстранге..."
            $ herView.hideshowQQ( "body_28.png", pos )
            her "В Дурмстранге {size=+4}нет{/size} Запретного леса."
            her "И в Шармбатоне тоже !"
            g6 "(Похоже, придется сделать еще один подход в другой день, сегодня это не в моих силах.)"
            m "Хорошо, девочка, ты права. Я поторопился."
            $ herView.hideshowQQ( "body_04.png", pos )
            her "Да, сэр. Спасибо за понимание, но от одной мысли о том, чтобы пойти одной в Запретный лес у меня сжимается в па… не важно."
            m "Придется написать мистеру Хагриду, что... "
            g5 "Одной ?"
            $ herView.hideshowQQ( "body_18.png", pos )
            her "Хагриду ?"
            g1 "Разве я не сказал ? Хагрид просил тебя участвовать в его группе для похода по лесу."
            m "А я планировал написать статью, чтобы помочь ему рекламой."
            $ herView.hideshowQQ( "body_24.png", pos )
            her "О, профессор, я так глупо себя чувствую. Конечно я помогу Хагриду."
            her "Да и в лесу с ним и целой группой будет безопасно."
            her "Я побегу собираться !"
            g10 "(Если кто и чувствует себя глупо, так это я.)"
        else:


            m "Готова к новому походу с группой Хагрида ?"
            her "Да, сэр."
            her "Пойду собираться."

        $ herView.hideshowQQ( "body_01.png", pos )


    elif cur_level == 2:
        ">текст преивента леса 1-2"
    elif cur_level == 3:
        ">текст преивента леса 1-3"
    elif cur_level == 4:
        ">текст преивента леса 1-4"
    elif cur_level == 5:
        ">текст преивента леса 1-5"

    $ hermione_out_halfday += 2
    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_forest_1_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о Запретном лесе ")
    $ nsp_genie_sphere_req = nsp_germiona_forest_1_photo

    if nsp_germiona_forest_1_statimg == "New":
        $ cur_level = nsp_event_forest_1 + 1
    else:
        $ cur_level = nsp_event_forest_1

    if cur_level == 1:
        show screen hermione_02
        $ herView.hideshowQQ( "body_01.png", pos )
        her "А вот и я, сэр."
        g9 "Ну как тебе ночевка в лесу ?"

        if nsp_germiona_forest_1_statimg == "New":
            $ herView.hideshowQQ( "body_06.png", pos )
            her "Сэр, это был мой первый поход."
        else:
            her "Так же, как и в прошлый раз, сэр."

        her "Скажите, как вы думаете, зачем вообще устраивают походы ?"
        g1 "Ну вообще-то я..."
        $ herView.hideshowQQ( "body_12.png", pos )
        her "Для того, чтобы веcело провести время на природе !"
        her "А эти озабоченные парни все время ко мне приставали !"
        her "Я не могу понять, почему. Остальные девушки спокойно отдыхали и развлекались."
        her "И только мне четыре раза пытались назначить свидание, пять раз лезли обниматься и два раза - целоваться."
        $ herView.hideshowQQ( "body_28.png", pos )
        her "Да что они все обо мне думают ?"
        g6 "Ну... Дай подумать..."
        g7 "Ты флиртуешь с учениками..."
        g7 "Зарабатываешь много очков, и никто не знает, за что..."
        g7 "Пытаешься флиртовать с учителями..."
        g9 "Хм. Даже и не знаю, почему они считают тебя доступной."
        $ herView.hideshowQQ( "body_77.png", pos )
        her "Как вы можете, сэр !"
        her "Вы считаете меня просто шлюхой ?"
        her "По-вашему, именно такой меня видит вся школа ?"
        her "Гррррр."
        g5 "(Похоже я неудачно пошутил. Нужно исправлять положение.)"
        $ herView.hideshowQQ( "body_71.png", pos )
        her "Почему вы молчите, сэр ? Я была права ?"
        m "Тут вот какое дело..."
        $ herView.hideshowQQ( "body_70.png", pos )
        her "Сэр, пожалуйста, скажите прямо, по-вашему вся школа считает меня девицей легкого поведения ?"
        m "Вообще-то я пошутил, на самом деле я вижу более простую причину, почему тебе уделили столько внимания."
        $ herView.hideshowQQ( "body_73.png", pos )
        her "И какую же ?"
        m "Ну я бы сказал, что ты просто показалась им гораздо привлекательнее других девочек."
        $ herView.hideshowQQ( "body_33.png", pos )
        her ".............."
        m "Что ?"
        m "Опять что-то не так ?"
        $ herView.hideshowQQ( "body_142.png", pos )
        her "Простите, сэр. Что-то в глаз попало."
        her "Пожалуй, я пойду. Пора собираться на уроки."
        m "Да, разумеется."
        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_germiona_mediawhoring < 10:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_forest_1 = cur_level

        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента леса 1-2"

        if nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_1 = cur_level

        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента леса 1-3"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_1 = cur_level

        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента леса 1-4"

        if nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_1 = cur_level

        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента леса 1-5"

        if nsp_germiona_mediawhoring < 150:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 60:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_1 = cur_level

        $ nsp_newspaper_bonus_base = 200

        call nsp_bonus_calc


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_forest_2:

    if cur_level == 1:
        ">текст преивента леса 2-1"

    elif cur_level == 2:
        ">текст преивента леса 2-2"

    elif cur_level == 3:
        ">текст преивента леса 2-3"

    elif cur_level == 4:
        ">текст преивента леса 2-4"

    elif cur_level == 5:
        ">текст преивента леса 2-5"


    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_forest_2_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о Запретном лесе ")
    $ nsp_genie_sphere_req = nsp_germiona_forest_2_photo

    if nsp_germiona_forest_2_statimg == "New":
        $ cur_level = nsp_event_forest_2 + 1
    else:
        $ cur_level = nsp_event_forest_2

    if cur_level == 1:
        ">текст ивента леса 2-1"

        if nsp_germiona_mediawhoring < 10:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_2 = cur_level

        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента леса 2-2"

        if nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_2 = cur_level

        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента леса 2-3"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_2 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента леса 2-4"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_2 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

        $ hermi.liking -= 10

    elif cur_level == 5:
        ">текст ивента леса 2-5"

        if nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 60:
            $ nsp_germiona_impudence += 1

        $ nsp_event_forest_2 = cur_level

        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
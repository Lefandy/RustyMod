label nsp_theme_nude:

    $ herView.hideshowQQ( "body_01.png", pos )
    g9 "Итак, Гермиона, сегодня у меня..."
    $ herView.hideshowQQ( "body_12.png", pos )
    her "Сэр ! Вы снова хотите заставить меня делать что-то неприличное ?"
    her "Как вы можете ?"
    g4 "Заставить ? По-моему, ты вызвалась добровольцем. И выполняя задания, помнишь о том, что приносишь пользу."
    g4 "Похоже я ошибся, считая, что тебе важно помочь школе поддержать свою честь на соревновании."
    m "Наверное, другая ученица могла бы справиться лучше."
    $ herView.hideshowQQ( "body_18.png", pos )
    her "Другая, сэр ?"
    m "Ну я мог бы пригласить мисс Гринграсс, например."
    $ herView.hideshowQQ( "body_05.png", pos )
    her "Что ? Эта тупая гордячка ? Это исключено. Именно я спасу Хогвартс от проигрыша !"
    $ herView.hideshowQQ( "body_14.png", pos )
    her "Профессор, пожалуйста, не думайте, что я безответственная."
    her "Разумеется я готова вести нас к победе под вашим руководством."
    $ herView.hideshowQQ( "body_24.png", pos )
    her "Просто ваши задания, сэр..."
    $ herView.hideshowQQ( "body_33.png", pos )
    her "Они сильно меня смущают."
    m "Хорошо, на этот раз в центре внимания в статье будешь не ты, а другие."
    $ herView.hideshowQQ( "body_13.png", pos )
    her "И мне не придется выставляться напоказ, или делать что-то подобное ?"
    m "На этот раз твоей задачей будет действовать незаметно."
    $ herView.hideshowQQ( "body_07.png", pos )
    her "Ох, сэр, даже не знаю. Я постараюсь."
    her "(Чувствую, я об этом еще пожалею.)"
    $ herView.hideshowQQ( "body_01.png", pos )

    return

label nsp_event_nude_1:

    if cur_level == 1:
        ">текст преивента голой 1-1"
    elif cur_level == 2:
        ">текст преивента голой 1-2"
    elif cur_level == 3:
        ">текст преивента голой 1-3"
    elif cur_level == 4:
        ">текст преивента голой 1-4"
    elif cur_level == 5:
        ">текст преивента голой 1-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_nude_1_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" об эксгибиционизме ")
    $ nsp_genie_sphere_req = nsp_germiona_nude_1_photo

    if nsp_germiona_nude_1_statimg == "New":
        $ cur_level = nsp_event_nude_1 + 1
    else:
        $ cur_level = nsp_event_nude_1

    if cur_level == 1:
        ">текст ивента голой 1-1"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_1 = cur_level

        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента голой 1-2"

        if nsp_germiona_mediawhoring < 55:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 65:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_1 = cur_level

        $ nsp_newspaper_bonus_base = 65

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента голой 1-3"

        if nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_1 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента голой 1-4"

        if nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_1 = cur_level

        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента голой 1-5"

        if nsp_germiona_mediawhoring < 135:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 145:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_1 = cur_level

        $ nsp_newspaper_bonus_base = 165

        call nsp_bonus_calc


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_nude_2:

    if cur_level == 1:
        ">текст преивента голой 2-1"

    elif cur_level == 2:
        ">текст преивента голой 2-2"

    elif cur_level == 3:
        ">текст преивента голой 2-3"

    elif cur_level == 4:
        ">текст преивента голой 2-4"

    elif cur_level == 5:
        ">текст преивента голой 2-5"


    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_nude_2_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" об эксгибиционизме ")
    $ nsp_genie_sphere_req = nsp_germiona_nude_2_photo

    if nsp_germiona_nude_2_statimg == "New":
        $ cur_level = nsp_event_nude_2 + 1
    else:
        $ cur_level = nsp_event_nude_2

    if cur_level == 1:
        ">текст ивента голой 2-1"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_2 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента голой 2-2"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_2 = cur_level

        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента голой 2-3"

        if nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_2 = cur_level

        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента голой 2-4"

        if nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_2 = cur_level

        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента голой 2-5"

        if nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 60:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_2 = cur_level

        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_nude_3:

    if cur_level == 1:
        ">текст преивента голой 3-1"
    elif cur_level == 2:
        ">текст преивента голой 3-2"
    elif cur_level == 3:
        ">текст преивента голой 3-3"
    elif cur_level == 4:
        ">текст преивента голой 3-4"
    elif cur_level == 5:
        ">текст преивента голой 3-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_nude_3_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" об эксгибиционизме ")
    $ nsp_genie_sphere_req = nsp_germiona_nude_3_photo

    if nsp_germiona_nude_3_statimg == "New":
        $ cur_level = nsp_event_nude_3 + 1
    else:
        $ cur_level = nsp_event_nude_3

    if cur_level == 1:
        ">текст ивента голой 3-1"

        if nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_3 = cur_level

        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc

        $ hermi.liking -= 2

    elif cur_level == 2:
        ">текст ивента голой 3-2"

        if nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_3 = cur_level

        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

        $ hermi.liking -= 2

    elif cur_level == 3:
        ">текст ивента голой 3-3"

        if nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_3 = cur_level

        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента голой 3-4"

        if nsp_germiona_mediawhoring < 150:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 60:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_3 = cur_level

        $ nsp_newspaper_bonus_base = 200

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента голой 3-5"

        if nsp_germiona_mediawhoring < 170:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 180:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 70:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_3 = cur_level

        $ nsp_newspaper_bonus_base = 230

        call nsp_bonus_calc

        $ hermi.liking -= 2

    elif cur_level == 6:
        ">текст ивента голой 3-6"

        if nsp_germiona_mediawhoring < 180:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 190:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 70:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_3 = cur_level

        $ nsp_newspaper_bonus_base = 240

        call nsp_bonus_calc

        $ hermi.liking -= 5

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_nude_4:

    if cur_level == 1:
        ">текст преивента голой 4-1"
    elif cur_level == 2:
        ">текст преивента голой 4-2"
    elif cur_level == 3:
        ">текст преивента голой 4-3"
    elif cur_level == 4:
        ">текст преивента голой 4-4"
    elif cur_level == 5:
        ">текст преивента голой 4-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_nude_4_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" об эксгибиционизме ")
    $ nsp_genie_sphere_req = nsp_germiona_nude_4_photo

    if nsp_germiona_nude_4_statimg == "New":
        $ cur_level = nsp_event_nude_4 + 1
    else:
        $ cur_level = nsp_event_nude_4

    if cur_level == 1:
        ">текст ивента голой 4-1"

        if nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_4 = cur_level

        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента голой 4-2"

        if nsp_germiona_mediawhoring < 150:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_4 = cur_level

        $ nsp_newspaper_bonus_base = 180

        call nsp_bonus_calc

        $ hermi.liking -= 2

    elif cur_level == 3:
        ">текст ивента голой 4-3"

        if nsp_germiona_mediawhoring < 160:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_4 = cur_level

        $ nsp_newspaper_bonus_base = 200

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента голой 4-4"

        if nsp_germiona_mediawhoring < 170:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 180:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 60:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_4 = cur_level

        $ nsp_newspaper_bonus_base = 220

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента голой 4-5"

        if nsp_germiona_mediawhoring < 180:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 190:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 60:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_4 = cur_level

        $ nsp_newspaper_bonus_base = 230

        call nsp_bonus_calc

        $ hermi.liking -= 4


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_nude_5:

    if cur_level == 1:
        ">текст преивента голой 5-1"
    elif cur_level == 2:
        ">текст преивента голой 5-2"
    elif cur_level == 3:
        ">текст преивента голой 5-3"
    elif cur_level == 4:
        ">текст преивента голой 5-4"
    elif cur_level == 5:
        ">текст преивента голой 5-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_nude_5_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" об эксгибиционизме ")
    $ nsp_genie_sphere_req = nsp_germiona_nude_5_photo

    if nsp_germiona_nude_5_statimg == "New":
        $ cur_level = nsp_event_nude_5 + 1
    else:
        $ cur_level = nsp_event_nude_5

    if cur_level == 1:
        ">текст ивента голой 5-1"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_5 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента голой 5-2"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_5 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента голой 5-3"

        if nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_5 = cur_level

        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента голой 5-4"

        if nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 60:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_5 = cur_level

        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента голой 5-5"

        if nsp_germiona_mediawhoring < 140:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 150:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 70:
            $ nsp_germiona_impudence += 1

        $ nsp_event_nude_5 = cur_level

        $ nsp_newspaper_bonus_base = 200

        call nsp_bonus_calc

        $ hermi.liking -= 20


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
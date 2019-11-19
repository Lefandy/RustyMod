label nsp_theme_sex:

    $ herView.hideshowQQ( "body_01.png", pos )
    g6 "Боюсь, у меня плохие новости."
    $ herView.hideshowQQ( "body_03.png", pos )
    her "Рейтинг нашей газеты недостаточно высок ?"
    g6 "Боюсь, что Шармбатон вырвался вперед благодаря своим статьям о вейлах, и нам не удается сократить разрыв."
    m "(Хорошо, что в ящике стола есть книга о других школах и об используемых ими существах.)"
    $ herView.hideshowQQ( "body_06.png", pos )
    her "Вы расстроены, сэр ?"
    m "Кто, я ?"
    g6 "Ах да, конечно расстроен. Даже не знаю, как быть. Боюсь, что без новых оригинальных статей мы обречены."
    $ herView.hideshowQQ( "body_07.png", pos )
    her "Может быть я могу чем-то помочь, профессор ?"
    her "Надеюсь под словом \"оригинальные\" вы не подразумевали ничего странного ?"
    g9 "Ну, вейл у нас нет, зато есть кое-кто получше."
    $ herView.hideshowQQ( "body_10.png", pos )
    her "Сэр ? Вы же не ..."
    g9 "У нас есть умная {size=+4}и{/size} красивая ученица, которая способна спасти Хогвартс от позора."
    $ herView.hideshowQQ( "body_13.png", pos )
    her "Неужели вы про меня ?"
    her "Я постараюсь, сэр. Вы можете на меня рассчитывать."
    $ herView.hideshowQQ( "body_24.png", pos )
    her "(Надеюсь это не кончится тем же, чем и обычно.)"
    $ herView.hideshowQQ( "body_01.png", pos )

    return

label nsp_event_sex_1:

    if cur_level == 1:
        ">текст преивента секса 1-1"
    elif cur_level == 2:
        ">текст преивента секса 1-2"
    elif cur_level == 3:
        ">текст преивента секса 1-3"
    elif cur_level == 4:
        ">текст преивента секса 1-4"
    elif cur_level == 5:
        ">текст преивента секса 1-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_sex_1_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о сексе ")
    $ nsp_genie_sphere_req = nsp_germiona_sex_1_photo

    if nsp_germiona_sex_1_statimg == "New":
        $ cur_level = nsp_event_sex_1 + 1
    else:
        $ cur_level = nsp_event_sex_1

    if cur_level == 1:
        ">текст ивента секса 1-1"

        if nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_sex_1 = cur_level

        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента секса 1-2"

        if nsp_germiona_mediawhoring < 35:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 45:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_1 = cur_level

        $ nsp_newspaper_bonus_base = 35

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента секса 1-3"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_1 = cur_level

        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента секса 1-4"

        if nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_1 = cur_level

        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента секса 1-5"

        if nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_1 = cur_level

        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_sex_2:

    if cur_level == 1:
        ">текст преивента секса 2-1"

    elif cur_level == 2:
        ">текст преивента секса 2-2"

    elif cur_level == 3:
        ">текст преивента секса 2-3"

    elif cur_level == 4:
        ">текст преивента секса 2-4"

    elif cur_level == 5:
        ">текст преивента секса 2-5"


    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_sex_2_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о сексе ")
    $ nsp_genie_sphere_req = nsp_germiona_sex_2_photo

    if nsp_germiona_sex_2_statimg == "New":
        $ cur_level = nsp_event_sex_2 + 1
    else:
        $ cur_level = nsp_event_sex_2

    if cur_level == 1:
        ">текст ивента секса 2-1"

        if nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_2 = cur_level

        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента секса 2-2"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_2 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента секса 2-3"

        if nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_2 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента секса 2-4"

        if nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_2 = cur_level

        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента секса 2-5"

        if nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_2 = cur_level

        $ nsp_newspaper_bonus_base = 150

        call nsp_bonus_calc

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_sex_3:

    if cur_level == 1:
        ">текст преивента секса 3-1"
    elif cur_level == 2:
        ">текст преивента секса 3-2"
    elif cur_level == 3:
        ">текст преивента секса 3-3"
    elif cur_level == 4:
        ">текст преивента секса 3-4"
    elif cur_level == 5:
        ">текст преивента секса 3-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_sex_3_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о сексе ")
    $ nsp_genie_sphere_req = nsp_germiona_sex_3_photo

    if nsp_germiona_sex_3_statimg == "New":
        $ cur_level = nsp_event_sex_3 + 1
    else:
        $ cur_level = nsp_event_sex_3

    if cur_level == 1:
        ">текст ивента секса 3-1"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_sex_3 = cur_level

        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента секса 3-2"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_3 = cur_level

        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента секса 3-3"

        if nsp_germiona_mediawhoring < 75:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 85:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_3 = cur_level

        $ nsp_newspaper_bonus_base = 85

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента секса 3-4"

        if nsp_germiona_mediawhoring < 95:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 105:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_3 = cur_level

        $ nsp_newspaper_bonus_base = 115

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента секса 3-5"

        if nsp_germiona_mediawhoring < 115:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 125:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_3 = cur_level

        $ nsp_newspaper_bonus_base = 145

        call nsp_bonus_calc


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_sex_4:

    if cur_level == 1:
        ">текст преивента секса 4-1"
    elif cur_level == 2:
        ">текст преивента секса 4-2"
    elif cur_level == 3:
        ">текст преивента секса 4-3"
    elif cur_level == 4:
        ">текст преивента секса 4-4"
    elif cur_level == 5:
        ">текст преивента секса 4-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_sex_4_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о сексе ")
    $ nsp_genie_sphere_req = nsp_germiona_sex_4_photo

    if nsp_germiona_sex_4_statimg == "New":
        $ cur_level = nsp_event_sex_4 + 1
    else:
        $ cur_level = nsp_event_sex_4

    if cur_level == 1:
        ">текст ивента секса 4-1"

        if nsp_germiona_mediawhoring < 45:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 55:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_4 = cur_level

        $ nsp_newspaper_bonus_base = 55

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента секса 4-2"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_4 = cur_level

        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента секса 4-3"

        if nsp_germiona_mediawhoring < 85:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 95:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_4 = cur_level

        $ nsp_newspaper_bonus_base = 115

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента секса 4-4"

        if nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_4 = cur_level

        $ nsp_newspaper_bonus_base = 160

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента секса 4-5"

        if nsp_germiona_mediawhoring < 140:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 150:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_4 = cur_level

        $ nsp_newspaper_bonus_base = 180

        call nsp_bonus_calc


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_sex_5:

    if cur_level == 1:
        ">текст преивента секса 5-1"
    elif cur_level == 2:
        ">текст преивента секса 5-2"
    elif cur_level == 3:
        ">текст преивента секса 5-3"
    elif cur_level == 4:
        ">текст преивента секса 5-4"
    elif cur_level == 5:
        ">текст преивента секса 5-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_sex_5_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о сексе ")
    $ nsp_genie_sphere_req = nsp_germiona_sex_5_photo

    if nsp_germiona_sex_5_statimg == "New":
        $ cur_level = nsp_event_sex_5 + 1
    else:
        $ cur_level = nsp_event_sex_5

    if cur_level == 1:
        ">текст ивента секса 5-1"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_5 = cur_level

        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента секса 5-2"

        if nsp_germiona_mediawhoring < 65:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 75:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_5 = cur_level

        $ nsp_newspaper_bonus_base = 85

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента секса 5-3"

        if nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_5 = cur_level

        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента секса 5-4"

        if nsp_germiona_mediawhoring < 115:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 125:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_5 = cur_level

        $ nsp_newspaper_bonus_base = 155

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента секса 5-5"

        if nsp_germiona_mediawhoring < 160:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 60:
            $ nsp_germiona_impudence += 1

        $ nsp_event_sex_5 = cur_level

        $ nsp_newspaper_bonus_base = 210

        call nsp_bonus_calc


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
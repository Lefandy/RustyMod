label nsp_theme_studio:

    $ herView.hideshowQQ( "body_01.png", pos )
    g9 "Девочка, кто-нибудь говорил тебе, что ты могла бы стать фотомоделью ?"
    $ herView.hideshowQQ( "body_18.png", pos )
    her "Фотомоделью ? Я ?"
    her "Спасибо, сэр, но я предпочитаю вместо этого быть лучшей ученицей."
    m "Ясно, ну что же..."
    $ herView.hideshowQQ( "body_24.png", pos )
    her "Но сэр ! Почему вы все-таки спросили ? Это был комплимент ?"
    m "Э... Да."
    $ herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор, мне очень приятно. Так неожиданно."
    m "Хм-да. Пожалуйста."
    m "Однако, я также хотел бы предложить тебе кое-что."
    m "Видишь ли, наша газета нуждается в хорошем графическом оформлении, и у меня появилась идея."
    $ herView.hideshowQQ( "body_14.png", pos )
    her "Неужели, вы хотите фотографировать {size=+3}меня{/size} ?"
    her "Я так польщена. Но ведь у меня совсем нет опыта."
    m "Ничего страшного, научишься по ходу дела."
    $ herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо !"
    her "Не знаю как спросить, но вы же сделаете просто красивые фото ? Ничего странного или неприличного ?"
    her "Просто фото ученицы Хогвартса ?"
    g9 "(Му-ха-ха)"
    g9 "Да да, фото ученицы."
    ">Вы незаметно скрестили пальцы"
    $ herView.hideshowQQ( "body_01.png", pos )

    return

label nsp_event_studio_1:

    if cur_level == 1:

        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_event_studio_1 == 0:

            m "(Гермиона не любит фотографироваться. Нужно будет использовать небольшую хитрость.)"
            g9 "Сегодня тебе нужно будет подгототовиться к фотосессии !"
            g9 "Это единственный шанс догнать конкурирующие редакции, так как они уже давно украшают обложки фотографиями красоток в купальниках."
            $ herView.hideshowQQ( "body_57.png", pos )
            her "{size=+3}В купальниках{/size}, профессор ?"
            $ herView.hideshowQQ( "body_94.png", pos )
            her "{size=+4}В купальниках ???{/size}"
            g9 "Да, и нам {size=+2}обязательно{/size} нужно их обойти."
            g9 "Я предлагаю для начала съемки топлесс, а уже потом, после разогрева аудитории..."
            $ herView.hideshowQQ( "body_96.png", pos )
            her "{size=+6}Фото топлесс ???{/size}"
            her "Разогрева... {size=+8}фото топлесс ???{/size}"
            ">Гермиона покачнулась, ее лицо попеременно краснело и бледнело."
            m "Я понимаю, это не совсем то, чего ты ожидала..."
            $ herView.hideshowQQ( "body_62.png", pos )
            her "Вы знаете, сэр, существует понятие преуменьшение. Но сказать, что это {size=+3}не совсем{/size} то..."
            her "У меня просто нет слов !"
            m "Да, прекрасно тебя понимаю."
            g9 "К сожалению, снимать тебя сразу голой не стоит, другие могут не так понять..."
            $ herView.hideshowQQ( "body_96.png", pos )
            her "{size=+8}Снимать го... ?{/size}"
            $ herView.hideshowQQ( "body_74.png", pos )
            her "Ах..."
            her "Так вы меня разыграли, сэр."
            her "Ну и шутки."
            g9 "{size=+4}Му-ха-ха.{/size}"
            $ herView.hideshowQQ( "body_16.png", pos )
            her "В чем на самом деле будет заключаться задание ?"
            m "Я сделаю несколько фотографий, тебе придется позировать."
            $ herView.hideshowQQ( "body_03.png", pos )
            her "В одежде ?"
            m "Да."
            $ herView.hideshowQQ( "body_15.png", pos )
            her "В нормальной одежде ?"
            m "Да, разумеется."
            her "Хорошо, я прийду."
        else:


            m "Готова сегодня изображать школьницу ?"
            $ herView.hideshowQQ( "body_13.png", pos )
            her "Но я и есть школьница !"
            her "А, так вы хотите устроить новую фотосессию ?"
            $ herView.hideshowQQ( "body_07.png", pos )
            her "Хорошо, я прийду."

        $ herView.hideshowQQ( "body_01.png", pos )

    elif cur_level == 2:
        ">текст преивента студии 1-2"
    elif cur_level == 3:
        ">текст преивента студии 1-3"
    elif cur_level == 4:
        ">текст преивента студии 1-4"
    elif cur_level == 5:
        ">текст преивента студии 1-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_studio_1_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о фотостудии ")

    if nsp_germiona_studio_1_statimg == "New":
        $ cur_level = nsp_event_studio_1 + 1
    else:
        $ cur_level = nsp_event_studio_1

    if cur_level == 1:

        $ herView.hideshowQQ( "body_01.png", pos )

        her "Здравствуйте, профессор."
        m "Здравствуй, Гермиона."
        m "Сегодня мы сделаем несколько фотографий, тебе нужно будет изображать школьницу."
        $ herView.hideshowQQ( "body_17.png", pos )
        her "Изображать ? Сэр, я и есть школьница !"
        g9 "Хорошо, тогда так. Тебе нужно будет изображать фотомодель, которая изображает школьницу. Так понятнее ?"
        $ herView.hideshowQQ( "body_15.png", pos )
        her "Я не уверена, что поняла. Но попробую."
        m "Хорошо, тогда покажи мне ответ у доски."
        her "У какой доски ?"
        m "У воображаемой !"
        $ herView.hideshowQQ( "body_208.png", pos )
        her "E=MC{size=-4}{/size}"
        m "Теперь невыученный урок !"
        $ herView.hideshowQQ( "body_02.png", pos )
        her "Как это, сэр ? Такое мне трудно представить !"
        m "Ну же, соберись ! Представь, что ты - это одна из глупых слизеринок."
        $ herView.hideshowQQ( "body_70.png", pos )
        her "Профессор, я правда занималась, но понимаете... Мой маникюр... Я сломала ноготь на странице 8, поэтому не дочитала параграф."
        g9 "(Какая жалость, что обе руки заняты фотоаппаратом.)"
        m "Теперь представь, что увидела на полу змею - как ты будешь реагировать ?"

        hide screen hermione_02
        show screen nsp_hermione_panic
        $ herView.hideshowQQ( "body_18.png", pos )
        her "О нет, что же делать !"
        her "Спасите, она меня укусит !"
        her "Профессор Снейп, помогите !"
        m "Профессор Снейп ???"
        hide screen nsp_hermione_panic
        show screen hermione_02

        $ herView.hideshowQQ( "body_95.png", pos )
        her "Нет, сэр... В смысле, это само вырвалось. Я не знаю, почему."
        g9 "Ай-яй-яй мисс Грейнджер."
        $ herView.hideshowQQ( "body_33.png", pos )
        her "Пожалуйста, сэр. Теперь вы меня совсем смутили..."
        m "Хорошо, тогда последнее. Посмотри в объектив и сделай такое лицо, как будто тебе залез под юбку слизеринец."
        her "Хорошо, сэр. Надеюсь, вы знаете, что делаете."
        $ herView.hideshowQQ( "body_34.png", pos )
        pause
        g9 "Отлично, на сегодня все. Мне еще предстоит как следует подро... подработать это материал."
        $ herView.hideshowQQ( "body_31.png", pos )
        her "До свидания, профессор."
        g9 "(Пока она бегала по комнате, мне удалось снять пару неожиданных ракурсов.)"

        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_germiona_mediawhoring < 10:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_1 = cur_level

        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc_photo

    elif cur_level == 2:
        ">текст ивента студии 1-2"

        if nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_1 = cur_level

        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc_photo

    elif cur_level == 3:
        ">текст ивента студии 1-3"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_1 = cur_level

        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc_photo

    elif cur_level == 4:
        ">текст ивента студии 1-4"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_1 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc_photo

    elif cur_level == 5:
        ">текст ивента студии 1-5"

        if nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_1 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc_photo

    if nsp_germiona_artistry < 25:
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_studio_2:

    if cur_level == 1:
        ">текст преивента студии 2-1"

    elif cur_level == 2:
        ">текст преивента студии 2-2"

    elif cur_level == 3:
        ">текст преивента студии 2-3"

    elif cur_level == 4:
        ">текст преивента студии 2-4"

    elif cur_level == 5:
        ">текст преивента студии 2-5"


    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_studio_2_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о фотостудии ")

    if nsp_germiona_studio_2_statimg == "New":
        $ cur_level = nsp_event_studio_2 + 1
    else:
        $ cur_level = nsp_event_studio_2

    if cur_level == 1:
        ">текст ивента студии 2-1"

        if nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_2 = cur_level

        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc_video

    elif cur_level == 2:
        ">текст ивента студии 2-2"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_2 = cur_level

        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc_video

    elif cur_level == 3:
        ">текст ивента студии 2-3"

        if nsp_germiona_mediawhoring < 65:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 75:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_2 = cur_level

        $ nsp_newspaper_bonus_base = 65

        call nsp_bonus_calc_video

    elif cur_level == 4:
        ">текст ивента студии 2-4"

        if nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_2 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc_video

    elif cur_level == 5:
        ">текст ивента студии 2-5"

        if nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_2 = cur_level

        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc_video

    if nsp_germiona_artistry < 25:
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_studio_3:

    if cur_level == 1:
        ">текст преивента студии 3-1"
    elif cur_level == 2:
        ">текст преивента студии 3-2"
    elif cur_level == 3:
        ">текст преивента студии 3-3"
    elif cur_level == 4:
        ">текст преивента студии 3-4"
    elif cur_level == 5:
        ">текст преивента студии 3-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_studio_3_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о фотостудии ")

    if nsp_germiona_studio_3_statimg == "New":
        $ cur_level = nsp_event_studio_3 + 1
    else:
        $ cur_level = nsp_event_studio_3

    if cur_level == 1:
        ">текст ивента студии 3-1"

        if nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_3 = cur_level

        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc_photo

    elif cur_level == 2:
        ">текст ивента студии 3-2"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_3 = cur_level

        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc_photo

    elif cur_level == 3:
        ">текст ивента студии 3-3"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_3 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc_photo

    elif cur_level == 4:
        ">текст ивента студии 3-4"

        if nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_3 = cur_level

        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc_photo

    elif cur_level == 5:
        ">текст ивента студии 3-5"

        if nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_3 = cur_level

        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc_photo

    if nsp_germiona_artistry < 25:
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_studio_4:

    if cur_level == 1:
        ">текст преивента студии 4-1"
    elif cur_level == 2:
        ">текст преивента студии 4-2"
    elif cur_level == 3:
        ">текст преивента студии 4-3"
    elif cur_level == 4:
        ">текст преивента студии 4-4"
    elif cur_level == 5:
        ">текст преивента студии 4-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_studio_4_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о фотостудии ")

    if nsp_germiona_studio_4_statimg == "New":
        $ cur_level = nsp_event_studio_4 + 1
    else:
        $ cur_level = nsp_event_studio_4

    if cur_level == 1:
        ">текст ивента студии 4-1"

        if nsp_germiona_mediawhoring < 25:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 35:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_4 = cur_level

        $ nsp_newspaper_bonus_base = 25

        call nsp_bonus_calc_video

    elif cur_level == 2:
        ">текст ивента студии 4-2"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_4 = cur_level

        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc_video

    elif cur_level == 3:
        ">текст ивента студии 4-3"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_4 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc_video

    elif cur_level == 4:
        ">текст ивента студии 4-4"

        if nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_4 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc_video

    elif cur_level == 5:
        ">текст ивента студии 4-5"

        if nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_4 = cur_level

        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc_video

    if nsp_germiona_artistry < 25:
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_studio_5:

    if cur_level == 1:
        ">текст преивента студии 5-1"
    elif cur_level == 2:
        ">текст преивента студии 5-2"
    elif cur_level == 3:
        ">текст преивента студии 5-3"
    elif cur_level == 4:
        ">текст преивента студии 5-4"
    elif cur_level == 5:
        ">текст преивента студии 5-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_studio_5_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о фотостудии ")

    if nsp_germiona_studio_5_statimg == "New":
        $ cur_level = nsp_event_studio_5 + 1
    else:
        $ cur_level = nsp_event_studio_5

    if cur_level == 1:
        ">текст ивента студии 5-1"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_5 = cur_level

        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc_photo

    elif cur_level == 2:
        ">текст ивента студии 5-2"

        if nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_5 = cur_level

        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc_photo

    elif cur_level == 3:
        ">текст ивента студии 5-3"

        if nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_5 = cur_level

        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc_photo

    elif cur_level == 4:
        ">текст ивента студии 5-4"

        if nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_5 = cur_level

        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc_photo

    elif cur_level == 5:
        ">текст ивента студии 5-5"

        if nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_5 = cur_level

        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc_photo

    if nsp_germiona_artistry < 25:
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_studio_6:

    if cur_level == 1:
        ">текст преивента студии 5-1"
    elif cur_level == 2:
        ">текст преивента студии 5-2"
    elif cur_level == 3:
        ">текст преивента студии 5-3"
    elif cur_level == 4:
        ">текст преивента студии 5-4"
    elif cur_level == 5:
        ">текст преивента студии 5-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_studio_6_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о фотостудии ")

    if nsp_germiona_studio_6_statimg == "New":
        $ cur_level = nsp_event_studio_6 + 1
    else:
        $ cur_level = nsp_event_studio_6

    if cur_level == 1:
        ">текст ивента студии 6-1"

        if nsp_germiona_mediawhoring < 45:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 55:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_6 = cur_level

        $ nsp_newspaper_bonus_base = 45

        call nsp_bonus_calc_video

    elif cur_level == 2:
        ">текст ивента студии 6-2"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_6 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc_video

    elif cur_level == 3:
        ">текст ивента студии 6-3"

        if nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_6 = cur_level

        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc_video

    elif cur_level == 4:
        ">текст ивента студии 6-4"

        if nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_6 = cur_level

        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc_video

    elif cur_level == 5:
        ">текст ивента студии 6-5"

        if nsp_germiona_mediawhoring < 140:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 150:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_studio_6 = cur_level

        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc_video

    if nsp_germiona_artistry < 25:
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
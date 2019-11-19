label nsp_theme_rights:

    $ herView.hideshowQQ( "body_01.png", pos )
    m "Итак, пришло направить твою стропт... настойчивость на новую цель."
    her "Сэр ?"
    m "Ты помнишь, зачем приходила в этот кабинет в первый раз ?"
    $ herView.hideshowQQ( "body_15.png", pos )
    her "Э... Это когда вы попросили меня..."
    m "Нет, в самый первый раз."
    her "А, вы имеете ввиду, на первом курсе, когда мы с Гарри и Роном..."
    g4 "(Кактус мне в ухо.)"
    m "В первый раз с тех пор, как я здесь появ... Нет опять не то."
    m "Я говорю про твои обвинения в адрес преподавателей, проявляющих дискриминацию."
    $ herView.hideshowQQ( "body_75.png", pos )
    her "Да, понимаю. Пришло время раскрыть правду общественности ?"
    her "Отлично, я готова !"
    $ herView.hideshowQQ( "body_01.png", pos )
    g1 "Кхм-кха."
    m "На самом деле, я предлагаю сначала подготовить почву для этого."
    g9 "Есть пара идей, как это сделать."
    her "Хорошо, сэр."

    return

label nsp_event_rights_1:

    if cur_level == 1:
        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_event_rights_1 == 0:
            m "Сегодня тебе предстоит составить репортаж о том, как некоторые ученики пристают к девочкам. Возможно, это слизеринцы."
            m "Нам действительно нужен этот материал."
            $ herView.hideshowQQ( "body_02.png", pos )
            her "Вы хотите, чтобы я провела расследование ?"
            m "Не ты ли жаловалась, что такое происходит ? Теперь есть возможность привлечь внимание читателей к проблеме."
            $ herView.hideshowQQ( "body_24.png", pos )
            her "Да, но я..."
            her "Возможно, я немного преувеличила."
            her "То есть некоторые ученики действительно ведут себя неподобающе, но это происходит не так часто."
            m "Это не важно, от тебя требуется только придумать сюжет и убедительно пересказать его мне."
            $ herView.hideshowQQ( "body_13.png", pos )
            her "Ну, если вы так считаете... Хорошо."
            $ herView.hideshowQQ( "body_01.png", pos )
        else:
            m "Сегодня тебе снова предстоит придумать рассказ о домогательствах."
            m "Есть вдохновение ?"
            $ herView.hideshowQQ( "body_06.png", pos )
            her "Наверное да, сэр."

        $ herView.hideshowQQ( "body_01.png", pos )

    elif cur_level == 2:
        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_event_rights_1 == 1:
            m "Сегодня тебе предстоит придумать новый текст репортажа."
            $ herView.hideshowQQ( "body_02.png", pos )
            her "Опять про приставание на улице ?"
            m "Эм... Прояви фантазию ! На этот раз можно написать про..."
            g1 "Про..."
            $ herView.hideshowQQ( "body_04.png", pos )
            her "Похоже, не только у меня плохо с фантазией."
            her "Сэр."
            g4 "Ах так ? Вечером принеси мне рассказ про пенную вечиринку !"
            $ herView.hideshowQQ( "body_31.png", pos )
            her "Ох."
            her "Профессор, но я ни разу не была на пенных... Да я и на обычных вечиринках бываю редко."
            g9 "Что поделать, жизнь журналиста состоит не только из славы и доступных девчо... то есть почестей."
            m "Жду тебя вечером."
            $ herView.hideshowQQ( "body_33.png", pos )
            her "Да, сэр."
        else:

            g9 "Сегодня вечером мы должны снова проработать тему вечеринок для читателей."
            $ herView.hideshowQQ( "body_06.png", pos )
            her "Так точно, сэр."

        $ herView.hideshowQQ( "body_01.png", pos )

    elif cur_level == 3:
        ">текст преивента прав 1-3"
    elif cur_level == 4:
        ">текст преивента прав 1-4"
    elif cur_level == 5:
        ">текст преивента прав 1-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_rights_1_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о правах ")
    $ nsp_genie_sphere_req = nsp_germiona_rights_1_photo

    if nsp_germiona_rights_1_statimg == "New":
        $ cur_level = nsp_event_rights_1 + 1
    else:
        $ cur_level = nsp_event_rights_1

    if cur_level == 1:

        show screen hermione_02
        $ herView.hideshowQQ( "body_01.png", pos )
        g9 "Ты пришла ? Отлично, я готов записывать."
        $ herView.hideshowQQ( "body_06.png", pos )
        her "Хорошо, сэр"
        her "Сегодня я шла по улице в сторону оранжереи."
        her "Вот."
        g9 "Отлично, продолжай."
        $ herView.hideshowQQ( "body_09.png", pos )
        her "И у двери стояла группа слизеринцев. Один из них позвал меня и я..."
        m "И ты пошла с ним в укромное место ?"
        $ herView.hideshowQQ( "body_13.png", pos )
        her "Э... Нет, сэр. Я попыталась пройти мимо. Но один из них загородил мне дорогу."
        her "Пока я пыталась его обойти, подошли остальные."
        $ herView.hideshowQQ( "body_24.png", pos )
        her "И они... Они трогали меня..."
        m "Трогали ? Как именно трогали ?"
        $ herView.hideshowQQ( "body_31.png", pos )
        her "Я ..."
        $ herView.hideshowQQ( "body_33.png", pos )
        ">Гермиона покраснела и замолчала."
        $ herView.hideshowQQ( "body_30.png", pos )
        her "Сэр, напоминаю вам, что это выдуманная история !"
        m "Да, но у любой истории должно быть окончание."
        $ herView.hideshowQQ( "body_45.png", pos )
        her "Ммм. Хорошо."
        her "Один из них схватил меня за локоть и начал поглаживать плечо."
        her "Другой погладил по щеке."
        $ herView.hideshowQQ( "body_54.png", pos )
        her "Третий... Третий..."
        m "И что же третий ?"
        her "Третий подошел сзади и положил руку мне на живот."
        $ herView.hideshowQQ( "body_85.png", pos )
        her "Сэр, я больше не могу."
        m "Ну же, еще пару фраз для завершения."
        her "Мне очень стыдно такое представлять."
        g4 "Сосредоточься !"
        $ herView.hideshowQQ( "body_81.png", pos )
        her "Ладно. Четвертый парень усмехнулся и посмотрел мне в глаза. Маленькая шлюха, сказал он."
        her "И..."
        m "И ?"
        $ herView.hideshowQQ( "body_59.png", pos )
        her "И приподняв край моей юбки провел рукой по обнаженному бедру."
        her "А потом я вырвалась и убежала."
        her "Вот и вся история, сэр."
        g9 "Ну что же, совсем неплохо."
        $ herView.hideshowQQ( "body_02.png", pos )
        her "Правда, сэр ?"
        m "Да. До следующего раза."
        $ herView.hideshowQQ( "body_14.png", pos )
        her "Следующего ра... Да, профессор, как скажете."
        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_germiona_mediawhoring < 10:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_rights_1 = cur_level

        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc

    elif cur_level == 2:
        show screen hermione_02
        $ herView.hideshowQQ( "body_01.png", pos )

        her "Здравствуйте, сэр."
        m "Здравствуй, Гермиона. Давай сразу к делу. Что ты можешь рассказать мне о недавней вечеринке на факультете Слизерин ?"
        $ herView.hideshowQQ( "body_08.png", pos )
        her "(Я так и знала, что этот старый извращенец упомянет Слизерин.)"
        m "Ты что-то сказала ?"
        $ herView.hideshowQQ( "body_208.png", pos )
        her "Я говорю, прекрасный выбор, сэр. Вы как всегда в ударе."
        m "Итак ?"
        $ herView.hideshowQQ( "body_04.png", pos )
        her "Нуууу. На прошлой неделе в гостиной подземелья Слизерина устроили просто нечто."
        g5 "Слизеринцы живут в подземелье ??? Впрочем не важно, продолжай."
        $ herView.hideshowQQ( "body_75.png", pos )
        her "Сок лился рекой, друзья шутили друг над другом, всем было весело, а какие там были викторины ..."
        m "И розовые пони какали радугой на брудершафт..."
        g4 "Ты издеваешься ? Может быть, мне лучше было доверить спасение школы кому-то вроде этой Гринграсс ?"
        $ herView.hideshowQQ( "body_198.png", pos )
        her "Простите, сэр, я исправлюсь !"
        her "Пиво лилось рекой, небольшие компании распивали напитки покрепче, раскрасневшиеся девчонки постепенно позволяли себе все больше..."
        g9 "О да, я в тебе не сомневался. Продолжай !"
        $ herView.hideshowQQ( "body_199.png", pos )
        her "Чем больше меня накачивали, тем приятнее становилось..."
        g5 ".............."
        $ herView.hideshowQQ( "body_191.png", pos )
        her "Пивом, сэр ! Я говорю про пиво !"
        $ herView.hideshowQQ( "body_09.png", pos )
        her "И вот кульминация вечеринки. Все девчонки собрались в круг. Парни приготовились. И началась..."
        g9 "Оргия ! О да, я знал это. Давай же, главное не упускай подробности !"
        $ herView.hideshowQQ( "body_12.png", pos )
        her "..............."
        her "Сэр."
        her "Я..."
        her "Прошу вас, не говорите таких вещей."
        g6 "Но ты же не оставишь меня... в смысле рассказ в таком состоянии ?"
        m "Нам нужно что-то действительно интересное. Неужели у тебя нет никаких идей ?"
        $ herView.hideshowQQ( "body_04.png", pos )
        her "Эм, да. Если подумать..."
        her "Итак, все собрались и начался конкурс. Все девушки пытались пройти под шестом изогнувшись, не задев его грудью."
        her "Побеждает та, которой громче будет кричать толпа."
        her "В какой-то момент выпивка начала ударять в голову..."
        g1 "И тебе тоже !"
        $ herView.hideshowQQ( "body_206.png", pos )
        her "Да, мне тоже... И мы начали проходить под шестом задрав рубашку, с голой грудью..."
        g9 "Превосходно ! Продолжай !"
        $ herView.hideshowQQ( "body_24.png", pos )
        her "И вот настала моя очередь. Все уставились только на меня."
        m "О да, детка"
        $ herView.hideshowQQ( "body_33.png", pos )
        her "Мои освобожденные буфера весело подпрыгнули, разгоряченное тело изогнулось..."
        g1 "аааааргх"
        her "И я начала проходить, стараясь удержать равновесие."
        her "Но алкоголь сделал свое дело."
        her "Меня начало вести в бок. Какой-то хитрый парень воспользовался ситуацией и подошел меня поддержать."
        her "И он схватил..."
        her "Нет, я не могу это сказать."
        m "Давай, сделай это !"
        $ herView.hideshowQQ( "body_17.png", pos )
        her "Вы помните, что это всего лишь придуманный рассказ ?"
        m "Ты сейчас все испортишь ! Нужно немедленно кончить ! То есть закончить !"
        $ herView.hideshowQQ( "body_34.png", pos )
        her "Хорошо, хорошо. И он схватил мои буфера, как бы поддерживая, и начал их мять."
        her "В этот момент я опомнилась, и начала вырываться. От неожиданности он отступил, и я, покраснев, убежала."
        $ herView.hideshowQQ( "body_45.png", pos )
        her "Вот такие вечиринки и проходят на факультете Слизерин."
        $ herView.hideshowQQ( "body_52.png", pos )
        her "Это непримелимо и с ними нужно бороться."
        her "Хороший финал, сэр ?"
        $ renpy.play('sounds/gulp.mp3')
        pause.8
        $ renpy.play('sounds/gulp.mp3')
        pause.8
        $ renpy.play('sounds/gulp.mp3')
        g7 "Да да, все отлично. Ты можешь идти. У меня тут небольшая авария."
        $ herView.hideshowQQ( "body_50.png", pos )
        her "Эх, профессор."

        if nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_rights_1 = cur_level

        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента прав 1-3"

        if nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_rights_1 = cur_level

        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента прав 1-4"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_1 = cur_level

        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента прав 1-5"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_1 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_rights_2:

    if cur_level == 1:
        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_event_rights_1 == 0:
            m "Сегодня у меня будет новое интересное задание."
            g9 "Помнишь, почему тебе приходится регулярно приходить сюда и бороться против несправедливости ?"
            $ herView.hideshowQQ( "body_185.png", pos )
            her "Бороться ? Я бы назвала это по-другому."
            m "Не важно. Итак, ты можешь теперь помочь в написании статьи, обличающей учителей."
            m "Мы покажем, что заставлять учеников торговать \"особыми\" услугами недостойно настоящего педагога!"
            g4 "Только учеба. Только труд. Только знания."
            $ herView.hideshowQQ( "body_184.png", pos )
            her "(Что-то он увлекся.)"
            m "Что-то я увлекся."
            m "В общем, приходи вечером с рассказом."
            $ herView.hideshowQQ( "body_01.png", pos )
            her "Да, сэр."
        else:
            m "Готова написать новую обличающую статью об учителях ?"
            her "Да, сэр."
            $ herView.hideshowQQ( "body_24.png", pos )
            her "Что, если на этот раз написать о вас ?"
            g9 "Спасибо, я тоже ценю наше сотрудничество."


        $ herView.hideshowQQ( "body_01.png", pos )

    elif cur_level == 2:
        ">текст преивента прав 2-2"

    elif cur_level == 3:
        ">текст преивента прав 2-3"

    elif cur_level == 4:
        ">текст преивента прав 2-4"

    elif cur_level == 5:
        ">текст преивента прав 2-5"


    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_rights_2_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о правах ")
    $ nsp_genie_sphere_req = nsp_germiona_rights_2_photo

    if nsp_germiona_rights_2_statimg == "New":
        $ cur_level = nsp_event_rights_2 + 1
    else:
        $ cur_level = nsp_event_rights_2

    if cur_level == 1:
        show screen hermione_02
        $ herView.hideshowQQ( "body_01.png", pos )

        m ".................."
        her ".................."
        m ".................."
        $ herView.hideshowQQ( "body_73.png", pos )
        her "Сэр ?"
        m "Я рассматривал тебя для того, чтобы стимулировать свое воображение."
        $ herView.hideshowQQ( "body_71.png", pos )
        her "Профессор, вы всегда придумываете что-то неприличное !"
        her "Лучше я начну, чтобы поскорее кончить."
        g9 "................................."
        $ herView.hideshowQQ( "body_50.png", pos )
        her "Закончить, сэр ! Завершить !"
        $ herView.hideshowQQ( "body_04.png", pos )
        her "Итак, сегодня я снова помогла своему факультету."
        m "Так так."
        her "Нам были очень нужны очки, все только об этом и говорили."
        $ herView.hideshowQQ( "body_05.png", pos )
        her "Ведь слизеринки вовсю жульничали, они только и делают, что продают се..."
        m "Гермиона, ближе к теме !"
        m "(Про снейповских шлюх я уже достаточно слышал от него самого.)"
        $ herView.hideshowQQ( "body_10.png", pos )
        her "Мммм да. Хорошо, сэр."
        her "Был вечер и уроки уже закончились. Но было одно место, где еще можно было обнаружить задержавшегося учителя и немного заработать."
        m "Продолжай, мне начинает нравиться."
        $ herView.hideshowQQ( "body_11.png", pos )
        her "И вот, я прошла по темному коридору к заветной двери. Внутри сидел наш профессор зельеварения..."
        her "Я знала, что он именно тот, кто действительно ценит услужливость..."
        g9 "Да, да !"
        m "То есть нет ! Нельзя вот так прямо порочить настоящего учителя !"
        $ herView.hideshowQQ( "body_12.png", pos )
        her "Но сэр ! Почему нет ? Ведь он действительно любитель..."
        g1 "Стоп ! Подумай сама, ведь если мы хотим обличить всех непорядочных учителей, нельзя спугнуть их раньше времени !"
        m "(Уф. Выкрутился.)"
        $ herView.hideshowQQ( "body_24.png", pos )
        her "О да, сэр, я поняла ! Но можно распустить хотя бы маленький слух, что именно о нем речь в рассказе..."
        m "На твоем месте я бы больше беспокоился о слухах, кто его автор."
        $ herView.hideshowQQ( "body_12.png", pos )
        her "Ох. Я поняла, профессор. Лучше я продолжу."
        her "Итак, высокая худая фигура примерно 180 см роста в черной мантии с длинными темными волосами и крючковатым носом ждала меня."
        her "\"Не желаете ли чего, профессор\", - спросила я."
        her "Но преподаватель ответил презрительным молчанием и продолжил проверять работы по зельев... по своему предмету."
        m "(Как точно описано. Хм.)"
        $ herView.hideshowQQ( "body_16.png", pos )
        her "Тогда я снова стала намекать на то, как сильно наш факультет и лично я нуждаемся в очках."
        her "Вволю насладившись своей властью, он зло усмехнулся и кивнул."
        m "(Она просто не могла это придумать. Неужели ? Да нет, не может быть...)"
        $ herView.hideshowQQ( "body_31.png", pos )
        her "\"Ваша грудь не соответствует уставу\" - мрачно заметил он. Форма ученицы не должна быть так сильно натянута. Это просто неприлично !"
        her "\"Но сэр\", - ответила я, - \"Я же не виновата в этом !\""
        $ herView.hideshowQQ( "body_15.png", pos )
        her "Сэр, что с вами ?"
        her "Профессор ?"
        g7 "А ? Да, продолжай же, не останавливайся."
        $ herView.hideshowQQ( "body_14.png", pos )
        her "И вот он заявляет, что должен проверить, действительно ли грудь настоящая, или я намеренно хочу ввести всех в заблуждение..."
        her "\"Я дам тебе пять очков за это\", - обещает он, и его глаза загораются."
        g9 "(Готов поклясться, что она сосредоточилась на совсем иных книгах, чем до нашей встречи.)"
        $ herView.hideshowQQ( "body_33.png", pos )
        her "И вот я смущенно соглашаюсь и замираю."
        m "О да, продолжай !"
        $ herView.hideshowQQ( "body_34.png", pos )
        her "Сне... Учитель дотрагивается до моей груди и начинает мять ее. В этот момент я замечаю, что дверь приоткрыта, и кто-нибудь может увидеть нас."
        her "Собрав все силы, я остаюсь неподвижной до конца."
        m "Эх, а я уже надеялся..."
        $ herView.hideshowQQ( "body_47.png", pos )
        her "Сэр, мне и так было трудно все это расска... то есть придумать !"
        m "Хорошо, но признайся, ведь это было на самом деле ?"
        $ herView.hideshowQQ( "body_50.png", pos )
        her "Сэр ! Как вы можете такое говорить ? И потом мы не договаривались, что я буду выдавать свои секреты."
        her "Вы хотели получить рассказ ! Вот вам рассказ."
        m "Ладно, ты можешь идти."
        $ herView.hideshowQQ( "body_56.png", pos )
        her "(Неужели он действительно догадался ?)"
        m "(А ведь Снейп ничего мне не рассказал об этом. Вот же...)"

        $ herView.hideshowQQ( "body_01.png", pos )

        if nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_rights_2 = cur_level

        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента прав 2-2"

        if nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_rights_2 = cur_level

        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента прав 2-3"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_2 = cur_level

        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента прав 2-4"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_2 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента прав 2-5"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_2 = cur_level

        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_rights_3:

    if cur_level == 1:

        $ herView.hideshowQQ( "body_01.png", pos )
        ">текст преивента прав 3-1"
        $ herView.hideshowQQ( "body_01.png", pos )

    elif cur_level == 2:
        ">текст преивента прав 3-2"
    elif cur_level == 3:
        ">текст преивента прав 3-3"
    elif cur_level == 4:
        ">текст преивента прав 3-4"
    elif cur_level == 5:
        ">текст преивента прав 3-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_rights_3_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о правах ")
    $ nsp_genie_sphere_req = nsp_germiona_rights_3_photo

    if nsp_germiona_rights_3_statimg == "New":
        $ cur_level = nsp_event_rights_3 + 1
    else:
        $ cur_level = nsp_event_rights_3

    if cur_level == 1:
        ">текст ивента прав 3-1"

        if nsp_germiona_mediawhoring < 10:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_rights_3 = cur_level

        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc

        $ nsp_event_rights_3_unpub = True

    elif cur_level == 2:
        ">текст ивента прав 3-2"

        if nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_3 = cur_level

        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc

        $ nsp_event_rights_3_unpub = True

    elif cur_level == 3:
        ">текст ивента прав 3-3"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_3 = cur_level

        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc

        $ hermi.liking -= 10

        $ nsp_event_rights_3_unpub = True

    elif cur_level == 4:
        ">текст ивента прав 3-4"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_3 = cur_level

        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc

        $ nsp_event_rights_3_unpub = True

    elif cur_level == 5:
        ">текст ивента прав 3-5"

        if nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_3 = cur_level

        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc

    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_rights_4:

    if cur_level == 1:
        ">текст преивента прав 4-1"
    elif cur_level == 2:
        ">текст преивента прав 4-2"
    elif cur_level == 3:
        ">текст преивента прав 4-3"
    elif cur_level == 4:
        ">текст преивента прав 4-4"
    elif cur_level == 5:
        ">текст преивента прав 4-5"

    $ wtevent.Finalize()

    jump hermione_goout

label nsp_event_rights_4_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о правах ")
    $ nsp_genie_sphere_req = nsp_germiona_rights_4_photo

    if nsp_germiona_rights_4_statimg == "New":
        $ cur_level = nsp_event_rights_4 + 1
    else:
        $ cur_level = nsp_event_rights_4

    if cur_level == 1:
        ">текст ивента прав 4-1"

        if nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_rights_4 = cur_level

        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента прав 4-2"

        if nsp_germiona_mediawhoring < 50:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 1

        $ nsp_event_rights_4 = cur_level

        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента прав 4-3"

        if nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_4 = cur_level

        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента прав 4-4"

        if nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_4 = cur_level

        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента прав 4-5"

        if nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_4 = cur_level

        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

        $ hermi.liking -= 2


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return

label nsp_event_rights_5:

    if cur_level == 1:
        ">текст преивента прав 5-1"
    elif cur_level == 2:
        ">текст преивента прав 5-2"
    elif cur_level == 3:
        ">текст преивента прав 5-3"
    elif cur_level == 4:
        ">текст преивента прав 5-4"
    elif cur_level == 5:
        ">текст преивента прав 5-5"
    elif cur_level == 6:
        ">текст преивента прав 5-6"
    elif cur_level == 7:
        ">текст преивента прав 5-7"

    $ event.Finalize()

    jump hermione_goout

label nsp_event_rights_5_complete:

    $ cur_level = 0

    $ nsp_newspaper_bonus_text_base = tr(" о правах ")
    $ nsp_genie_sphere_req = nsp_germiona_rights_5_photo

    if nsp_germiona_rights_5_statimg == "New":
        $ cur_level = nsp_event_rights_5 + 1
    else:
        $ cur_level = nsp_event_rights_5

    if cur_level == 1:
        ">текст ивента прав 5-1"

        if nsp_germiona_mediawhoring < 30:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 10:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_5 = cur_level

        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc

    elif cur_level == 2:
        ">текст ивента прав 5-2"

        if nsp_germiona_mediawhoring < 60:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_5 = cur_level

        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc

    elif cur_level == 3:
        ">текст ивента прав 5-3"

        if nsp_germiona_mediawhoring < 70:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 20:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_5 = cur_level

        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc

    elif cur_level == 4:
        ">текст ивента прав 5-4"

        if nsp_germiona_mediawhoring < 90:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 30:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_5 = cur_level

        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc

    elif cur_level == 5:
        ">текст ивента прав 5-5"

        if nsp_germiona_mediawhoring < 110:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 40:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_5 = cur_level

        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc

    elif cur_level == 6:
        ">текст ивента прав 5-6"

        if nsp_germiona_mediawhoring < 130:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_5 = cur_level

        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc

    elif cur_level == 7:
        ">текст ивента прав 5-7"

        if nsp_germiona_mediawhoring < 150:
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160:
            $ nsp_germiona_mediawhoring += 1

        if nsp_germiona_impudence < 50:
            $ nsp_germiona_impudence += 1

        $ nsp_event_rights_5 = cur_level

        $ nsp_newspaper_bonus_base = 190

        call nsp_bonus_calc


    call nsp_hermione_goout

    $ wtevent.Finalize()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
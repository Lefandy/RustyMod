label phoenix:
    if bird_interact == 15:
        stop music fadeout 3.0
        $ bird_interact += 1
        if pnx_stage == 0:
            $ pnx_stage = 1
            hide screen genie
            show screen feeding 
            with Dissolve(0.3)
            pause 1
            show screen phoenix_food
            show screen bld1

            ">Когда вы подходите к фениксу, он смотрит на вас ожидающим взглядом и немного оживает."
            m "Ну чего ты, птичка, грустишь? Хоть директора и нет, я о тебе позабочусь. "
            m "Видали и более противных попугаев, и ни чего - в обиду их не давал…"

            ">Феникс указывает вам на книги на камине. Он что-то хочет вам сказать, но не может."
            ">Вы осматриваете полку возле книг и находите записку."

            $ letter_text = "{size=-2}Уважаемый профессор Дамблдор. \n\nНе знаю, что вы за вид оборотня такой, но судя по всему - слизняк, т.к. уже множество месяцев подряд после каждого полнолуния весь пол у вас в чем-то липком и противном. Прошу вас относиться к чистоте в кабинете ответственнее, иначе на вашу башню я более подниматься не буду. {/size}"

            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc

            g4 "На башню? Это метафора такая? Он еще и уборщицу трахал?"
            m "Почему нельзя выражаться проще: \"никогда не сяду на ваш член\"?"
            m "Почему все вокруг так любят маскировать пенис под фаллические предметы? Всё равно всем и так ясно, о чём они говорят."
            g9 "Особенно мне."
            pause.5
            m "Хм, я, конечно, понимаю, чем занимался тут профессор, но…"
            m "Так необычно подобранное время…"
            m "Феникс, ты что-то знаешь об этом?"

            ">Феникс смотрит на вас ожидающим взглядом."

            g4 "Господи, надеюсь, он не феникса трахал…"
            g4 "Это же глупость…"
            m "Хотя…"
            g9 "Эй, феникс!"
            g4 "Стоп, джин, это перебор даже для тебя."

            ">Феникс продолжает смотреть на вас ожидающим взглядом."

            m "Он точно что-то знает. Нужно разгадать этот ребус. Мой член в этом заинтересован."

            hide screen bld1
            show screen genie
            hide screen feeding 
            with Dissolve(0.3)
        jump day_main_menu

    menu:
        "- Исследовать -" if not bird_examined:
            $ bird_examined = True
            hide screen genie
            $ tt_xpos=270
            $ tt_ypos=90
            show screen genie_stands
            show screen chair_02 
            show screen desk
            with Dissolve(0.5)
            m "Хм....."
            m "Даже эта странная птица излучает магию.."
            show screen genie
            hide screen genie_stands
            hide screen chair_02 
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu

        "- Перечитать бумажку -" if pnx_stage == 1:

            $ letter_text = "{size=-2}Уважаемый профессор Дамблдор. \n\nНе знаю, что вы за вид оборотня такой, но судя по всему - слизняк, т.к. уже множество месяцев подряд после каждого полнолуния весь пол у вас в чем-то липком и противном. Прошу вас относиться к чистоте в кабинете ответственнее, иначе на вашу башню я более подниматься не буду. {/size}"

            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc

            jump phoenix

        "- Покормить птицу -" if not phoenix_is_feed and bird_examined:
            $ phoenix_is_feed = True
            jump feeding

        "- Погладить птицу -" if bird_examined:
            jump petting
        "- Ничего -":
            call screen main_menu_01    



label feeding:
    $ bird_interact += 1
    hide screen genie
    show screen feeding 
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    $ genie_speaks = renpy.random.randint(1, 3)
    if genie_speaks == 1:
        m "Держи..."
    else:
        pause.5
    show screen genie
    hide screen feeding 
    with Dissolve(0.3)
    call screen main_menu_01    



label petting:
    $ bird_interact += 1
    hide screen genie
    show screen petting
    with Dissolve(0.3)
    pause 3
    show screen sad_phoenix 
    pause 1.5
    m "Птица плохо выглядит. Может быть она больна?"
    pause.5



    show screen genie
    hide screen sad_phoenix 
    hide screen petting
    with Dissolve(0.3)
    call screen main_menu_01




label pnx_call:


    $ phoenix.LoadDefItemSets()
    $ phoenix.Visibility("body+", False)

    hide screen phoenix
    show screen phoenix_no
    hide screen animation_feather
    show screen bld1

    $ phoenix("~n c def c")
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3

    if pnx_stage == 0:
        $ pnx_stage = 1

    if pnx_stage <= 1:

        g4 "Что… кто… откуда…"
        $ phoenix("~n n def c")
        g4 "ЧТО ТЫ СДЕЛАЛА С ФЕНИКСОМ?!"
        $ phoenix("~n n def o// Думаю, вы говорите именно о том фениксе, в которого я была обращена.")
        $ phoenix("~n n def c")
        m "Да? Вот это опция…"
        m "А почему ты раньше не вылазила?"
        $ phoenix("~n a def o// Я зачарована, сэр. Директор выкупил меня очень давно у арабских купцов. С тех пор я была у него. Правда он уже много лет не менял мое обличие...")
        $ phoenix("~w c def o// Но, судя по тому, что его здесь нет, а вы на его месте, он ушел и продал меня вам. Так что теперь вы мой мастер.")
        $ phoenix("~n n def c")
        m "...Эм?"
        g9 "Да, я твой мастер! Ты исполняешь желания?"
        $ phoenix("~w h def o// А про какие желания вы говорите?")
        $ phoenix("~a n def c")
        g9 "Что значит, “про какие?”"
        g9 "Я - твой мастер, и какие желания я от тебя потребую - такие тебе выполнить и придется."
        $ phoenix("~a a def o// Хм…")
        $ phoenix("~a a def o// Глупость какая-то. Я же не джин…")
        $ phoenix("~w n def c")
        g9 "О, нет. Желания будут вполне смертными."
        $ phoenix("~n c def c")
        m "И, боюсь, мне придется превратить тебя обратно в птицу, если…"
        $ phoenix("~n n def o// В птицу?")
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("...Как вам будет угодно.")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        ">Девушка элегантно преобразуется в феникса, сидящего на прежнем месте."
        $ phoenix.body.data().delPose()
        $ phoenix.Visibility()

        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        hide screen phoenix_no
        show screen phoenix

        pause 3

        hide screen heal3

        g4 "Что? Стой! Как ты это?.."
        g4 "Так ты можешь сама?! Так, превратись обратно немедленно! Мастер приказывает!"
        g4 "Феникс!"
        m "Пожалуйста…"
        g4 "Как я вообще это сделал? Ты слышишь меня? Тупая курица!"
        m "Прости, прости, это…"
        m "Это у меня комплименты такие…"
        g4 "...Вернись!"
        m "Так, надо понять свою последовательность действий"

    elif pnx_stage == 2:

        $ phoenix("~n n def o// Это снова вы, мастер?")
        $ phoenix("~n a def c")
        m "А ты видишь кого-то еще?"
        $ phoenix("~s n def o// А должна?")
        $ phoenix("~n c def c")
        m "Даже не знаю… проехали."
        m "А как я тебя высвободил?"
        $ phoenix("~w c def o// Ваше семя попало на мое перо под светом полной луны.")
        $ phoenix("~w h def o// Это означает, что вы хотите меня видеть.")
        $ phoenix("~a h def c")
        m "Странная логика. Ты мне, по сути и не нужна, если я…"
        $ phoenix("~a a def c")
        g9 "“Излил всё семя”..."
        $ phoenix("~w n def o// А, так я вам не нужна?")
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Хорошо, тогда не буду вас доставать…")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        g4 "Эй, подожди…"
        $ phoenix.body.data().delPose()
        $ phoenix.Visibility()

        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        hide screen phoenix_no
        show screen phoenix

        pause 3

        hide screen heal3

        m "Нашел, блин, время умничать…"
        m "Мы с ней так далеко не продвинемся."

    elif pnx_stage == 3:

        $ phoenix("~n a def o// Добрый вечер, сэр.")
        $ phoenix("~w a def c")
        m "Ты вообще слышишь меня, когда ты в форме феникса?"
        $ phoenix("~s a def o// Ну конечно. Просто не понимаю.")
        $ phoenix("~n c def c")
        m "...Так, давай вернемся обратно к желаниям."
        $ phoenix("~n n def o// Хорошо. Какие у вас будут желания?")
        $ phoenix("~w c def c")
        g9 "(Ну наконец-то)"
        $ phoenix("~n h def c")
        g9 "Хочу, чтобы ты была моей, птичка!"
        $ phoenix("~w n def o// Вашей птичкой? Какое-то странное желание…")
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Ну как скажете.")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        $ phoenix("Зовите, если передумаете")
        $ phoenix.body.data().delPose()
        $ phoenix.Visibility()

        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        hide screen phoenix_no
        show screen phoenix

        pause 3

        hide screen heal3

        m "..."
        m "Так, нужно быть аккуратнее с желаниями. У нее, судя по всему, и мозг остается от птицы."

    elif pnx_stage ==4:

        $ phoenix("~n n def c// Приветствую, мастер.")
        $ phoenix("~w n def c")
        m "Я теперь научен. Буду говорить короткими и недвусмысленными фразами."
        $ phoenix("~n h def c")
        g9 "...Так ты выполняешь интимные желания?"
        $ phoenix("~w h def o// Интимные - в смысле...")
        $ phoenix("~w n def c")
        m "Чем вы занимались с Директором?"
        $ phoenix("~s a def o// Ну... он заботился обо мне... купал меня...")
        $ phoenix("~s c def o// Называл меня дочкой и просил называть его папочкой...")
        $ phoenix("~n n def o")
        g9 "(Ох, старый извращенец)"
        $ phoenix("~n a def o// Когда я себя хорошо вела, он позволял мне сидеть на его палочке...")
        $ phoenix("~w n def o")
        m "Так, на этом и остановимся. Давай вообще забудем про Директора. Начнем разговор с начала…"
        $ phoenix("~s n def o// Эм... приветствую, мастер...")
        $ phoenix("~n c def c")
        m "(Ух, я был близок. Перемотай она еще чуть-чуть назад...)"
        $ phoenix("~n n def c")
        m "Ты говорила, что при попадании на твое перо семени, ты становишься девушкой..."
        $ phoenix("~n h def o// Один раз за ночь...")
        $ phoenix("~n h def c")
        m "(Нужно сразу уточнить все подробности. Главное аккуратно ей...)"
        $ phoenix("~a a def c")
        g9 "...А если я оболью тебя спермой, ты превратишься в феникса обратно?"
        $ phoenix("~a c def o// Хм. Я сама, вроде, могу принимать его форму.")
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Сейчас покажу...")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        g4 "Стой!"
        $ phoenix.body.data().delPose()
        $ phoenix.Visibility()

        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        hide screen phoenix_no
        show screen phoenix

        pause 3

        hide screen heal3

        g4 "Я уже насмотрелся на это, тупая ты птица."
        g4 "Она опять удрала! Да она это специально делает!"

    elif pnx_stage == 5:

        $ phoenix("~n c def o// Я вам понадобилась, сэр?")
        $ phoenix("~n h def c")
        m "Я бы сказал, что надобность в тебе не пропадала с самой первой встречи."
        $ phoenix("~n a def c")
        m "Давай договоримся так: пока я сам не повелю тебе превратиться обратно, ты не будешь этого делать."
        $ phoenix("~s c def o// Хорошо, сэр")
        $ phoenix("~s n def c")
        m "Больше ни каких демонстраций, додумываний и предположений. Либо я тебе прикажу, либо разрешу."
        $ phoenix("~s h def o// Я поняла. Простите, сэр.")
        $ phoenix("~w a def c")
        g9 "Ничего. Ты сейчас как раз загладишь свою вину."
        g9 "Ты готова выполнять мои сексуальные желания?"
        $ phoenix("~n h def o// Готова, сэр.")
        $ phoenix("~n n def c")
        g9 "Ох… с чего начнем? Ну… для начала..."
        $ phoenix("~w a def c")
        g9 "Начни с мастурбации. Ты знаешь, что это? Умеешь?"
        $ phoenix("~w n def o// Конечно, сэр.")
        $ phoenix("~w h def o// А кому? Себе или вам?")
        $ phoenix("~w c def c")
        g9 "(Наконец-то мы дошли до этого…)"
        $ phoenix("~n a def c")
        g9 "Ну я даже не знаю. А чего хочешь ты?"
        $ phoenix("~w a def o// Я?")
        $ phoenix("~n c def o// Я бы хотела...")
        $ phoenix("~w h def o// ...Сесть на вашу палочку, сэр.")
        $ phoenix("~n h def c")
        g9 "Да, детка, вот это взрослый разговор."
        $ phoenix("~n a def c")
        g9 "Так чего же ты ждешь?"
        $ phoenix("~w n def o// Вы разрешаете, сэр?")
        $ phoenix("~n h def c")
        g9 "Я приказываю!"
        $ phoenix("~w c def c")
        g4 "Стой, подожди, о какой…"
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Спасибо, сэр.")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        $ phoenix("~a a def o// ...")
        $ phoenix.body.data().delPose()
        $ phoenix.Visibility()

        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        hide screen phoenix_no
        show screen phoenix

        pause 3

        hide screen heal3

        g4 "..."
        g4 "Ты на этой палочке сидишь целыми днями..."
        m "Я просто в ярости. Ты либо настолько тупая, либо настолько хитрая. Но настолько меня достала..."

    elif pnx_stage == 6:

        $ phoenix("~n n def o// Вы снова вызвали меня, мастер?")
        $ phoenix("~n c def c")
        m "Нет, это ты снова убежала. Я вообще не горю желанием превращать тебя в птицу."
        $ phoenix("~s h def o// Но мастер, а если кто-то...")
        $ phoenix("~s a def c")
        m "Знаю, тебя не стоит показывать всем подряд. Давай договоримся: будет специальное слово."
        m "И пока ты это слово не услышишь - ни каких подвижек в сторону феникса. Даже если я тебе скажу это напрямую."
        $ phoenix("~s n def c")
        m "Волшебное слово. Понятно?"
        $ phoenix("~s a def o// Эм... понятно, мастер.")
        $ phoenix("~s c def c")
        m "И этим волшебным словом будет..."
        $ phoenix("~w n def c")
        g9 "“Проваливай!”"
        $ phoenix("~s h def o// ...“Проваливай”?")
        $ phoenix("~w a def c")
        m "Хм… да, проваливай…"
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        g4 "Нет, в смысле не сейчас. Когда ты его услышишь в следующий раз."
        $ phoenix.body.data().delPose()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix("~s c def c")
        m "Запомнила слово?"
        m "Повтори."
        $ phoenix("~s c def o// Проваливай...")
        $ phoenix("~s n def c")
        g9 "Умная птичка!"
        m "Превращайся!"
        $ phoenix("~s a def c// ...")
        $ phoenix("~s n def o")
        m "Стань фениксом!"
        $ phoenix("~s c def c// ...")
        $ phoenix("~s h def c")
        g9 "Сядь на палочку!"
        $ phoenix("~s a def o// ...")
        $ phoenix("~n n def o")
        g9 "Хе-хе-хе… Кстати, нужно будет договориться о новом значении последней фразы."
        $ phoenix("~n c def o// Хорошо, мастер...")
        $ phoenix("~w n def c")
        m "Тогда сейчас же подойди сюда и повернись ко мне попкой. Буду объяснять тебе значение…"
        $ phoenix("~w h def o// Как пожелаете...")
        $ phoenix("~a a def c")
        g9 "Ох, как же тебя сейчас оттрахают..."
        pause.2

        $ renpy.play('sounds/knocking.mp3')
        "> тук-тук"
        $ phoenix("~n h def c")
        sna "Джин, у меня к тебе есть дело..."
        $ phoenix("~w n def o")
        g4 "Проваливай!"
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Я поняла...")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        g4 "Да не ты!.."
        $ phoenix.body.data().delPose()
        $ phoenix.Visibility()

        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        hide screen phoenix_no
        show screen phoenix

        pause 3

        hide screen heal3

        g4 "Стой! Тупая ты курица! У тебя вообще есть мозги или они вслед за перьями отваливаются?!"
        g4 "Есть вообще в этом мире существо тупее, чем ты?!"
        g4 "Какой же нужно быть идиоткой, чтобы ты выглядела на ее фоне умнее?! "
        g4 "Я бы превратил тебя в стул, но он был бы и то разумнее!"
        pause.2

        sna "Джин, с кем ты там?"
        m "Оставь меня, пожалуйста..."
        sna "Эм… ну ладно… Завтра зайду."

    elif pnx_stage == 7:

        $ phoenix("~a a def c// ...")
        $ phoenix("~a n def c")
        m "Ты сегодня какая-то не разговорчивая."
        $ phoenix("~a a def o// Сэр, может я и не понимаю, что вы говорите, но это не значит, что я не запоминаю.")
        $ phoenix("~w n def c")
        m "Ой, я как-то не подумал..."
        $ phoenix("~a h def c")
        m "Хотя чего это я? У тебя всё равно мозги птицы, ты, наверное, и половины слов не поняла."
        m " А кричал я… не на тебя. У меня посетитель был..."
        $ phoenix("~a h def o// Между прочим я - анимаг. Это я превращаюсь в феникса, а не он в меня.")
        $ phoenix("~a c def c")
        m "Тогда я не понимаю, чем вы, анимаги, умнее тех зверей, в которых превращаетесь..."
        $ phoenix("~n a def o// Сэр, вы сказали - и я испонила. Вы говорили, что меня не стоит показывать всем...")
        $ phoenix("~w n def o")
        m "Позволь мне самому решать, кому тебя показывать, а под кого и вовсе тебя класть."
        m "Напряги ты хоть одну свою извилинку, ты бы поняла какие слова адресованы тебе, а какие - нет. "
        $ phoenix("~a c def o")
        g4 "Будь ты человеком разумным, ты бы не убегала после каждой глупой фразы!"
        g4 "Но ты ведешь себя, как тупая птица! А я хочу трахать девушку, а не тупую птицу!"
        $ phoenix("~a n def o// Ах так? Ладно, я поняла: я - тупая птица и я вам не нужна.")
        $ phoenix("~a c def c")
        m "Ну не принимай это настолько близко..."
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Советую разглядеть мой зад хорошенько. Вы видите его последний раз.")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        m "Ну не надо настолько радикально-то…"
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Не переживайте. Секс с птицей вам вряд-ли будет интересен...")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        g9 "Да брось, я просто погорячился!"
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Прощайте!")
        $ phoenix.body.data().delPose()
        $ phoenix.Visibility()

        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        hide screen phoenix_no
        show screen phoenix

        pause 3

        hide screen heal3

        m "Такая капризная. Нет, она точно девушка."

    elif pnx_stage >= 8:

        $ phoenix("~n c def o// Вы что-то хотели?")
        $ phoenix("~n c def c")
        g9 "Да. Кого-то. Тебя."
        $ phoenix("~w c def o// Зачем? Вы что, зоофил?")
        $ phoenix("~a n def c")
        g9 "Да прекрати это. Подойди и обхвати мой член уже."
        $ phoenix("~a a def o// Простите, боюсь поцарапать его когтями...")
        $ phoenix("~a n def c// ...И клювом.")
        $ phoenix("~n n def c")
        g9 "Ладно, черт с тобой. Тебе нужно успокоиться. А пока дай хотя бы тебя разглядеть."
        $ phoenix("~w a def o// Какой в этом смысл? Я что так птица, что так...")
        $ phoenix("~w h def c")
        m "Ну не придуривайся. В такой птице ты очень даже сексуальная."
        $ phoenix("~a n def c")
        g9 "Хоть и такая же плоская."
        $ phoenix.Visibility()
        pause.2
        $ phoenix.Visibility("body+", False)
        $ phoenix.body.data().addItem( 'item_pose_back_open' )
        $ phoenix("Все с вами ясно.")
        $ phoenix.body.data().delPose()
        $ phoenix.body.data().addItem( 'item_pose_back_closed' )
        $ phoenix("~a a def o// Спокойной ночи.")
        $ phoenix.body.data().delPose()
        $ phoenix.Visibility()

        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        hide screen phoenix_no
        show screen phoenix

        pause 3

        hide screen heal3

        m "Эх... думаю, мы с ней не помиримся..."
        $ pho_ending = 1

    $ pnx_stage += 1

    hide screen bld1

    show screen animation_feather

    if daytime:
        jump night_start
    else:
        jump day_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
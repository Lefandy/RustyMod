label accident:

    pause.8

    $ renpy.play('sounds/knocking.mp3')
    ">Тук-тук-тук."

    m "Хм, кто же это? Снейп с гермионой давно уже без стука входят. Или в них внезапно совесть проснулась?"

    $ renpy.play('sounds/knocking.mp3')
    ">Тук-тук-тук."

    if luna_stage == 0:

        fem "Профессор, вы там ?"
        g9 "(Ха ! Юный женский голос.)"
        g9 "(Ох, что же за лапочка там меня зовет. Ну как я могу отказать ей в желании подержать меня за член.)"
        fem "Профессор, я хотела вас попросить кое о чем."
        m "(Давай, не разочаруй меня, крошка.)"
        fem "Профессор, мне нужно несколько ваших уроков пользования палочкой."
        m "(Да меня даже просить об этом не придется, маленькая шлюшка.)"

    $ luna.Visibility()
    $ luna ("Профессор, это я, Полумна, вы слышите меня?")

    menu:
        "Подойти к двери":

            pass
        "Сидеть молча":

            call accident_none
            return

    hide screen genie
    $ tt_xpos=650
    $ tt_ypos=110
    show screen genie_stands
    show screen chair_02 
    show screen desk
    with Dissolve(0.5)

    $ luna ("Сэр, у вас не будет минутки?")

    menu:
        "Посмотреть в щель":
            pass
        "Сидеть молча":

            call accident_none2
            return

    show screen blkfade

    $ luna.Visibility("body")

    $ luna ("~00 def def def// Профессор, мне буквально уточнить движения рук…")

    menu:
        "Смотреть дальше":
            $ luna ("~00 def def ope// Я просто не уверена, что обращаюсь с палочкой правильно…")

            menu:
                "Смотреть дальше":
                    $ luna ("~def clo def def// Заодно бы показали, как пользуетесь своей палочкой…")
                    menu:
                        "Смотреть дальше":
                            $ luna ("~def def def def// И может даже дали бы мне ее подержать…")
                            menu:
                                "Смотреть дальше":
                                    call accident_none2
                                    return
                                "Просунуть член":

                                    pass
                        "Просунуть член":

                            pass
                "Просунуть член":

                    pass
        "Просунуть член":

            pass

    g9 "(Надеюсь, она догадается, что делать с моей \"палочкой\" ?)"
    m "(Давай, обхвати ее ладошками...)"

    if luna_stage == 0:
        stop music
        $ renpy.play('sounds/glass_break.mp3')
        $ luna ("~def low def ope// {size=+5} А-А-А-А! ЗМЕЯ! {/size}")
        $ luna.Visibility()
        hide screen blkfade
        ">Крик быстро отдаляется."
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 

        ">Вы прячете член обратно"
        g5 "Что? Змея? Где? А если бы она меня за член укусила?"
        g4 "Это не школа, а питомник какой-то!"

    elif luna_stage == 1:

        $ luna.Visibility()
        hide screen blkfade
        sna "Джин, мать твою, ты совсем ополоумел?"
        sna "Когда я сказал тебе не покидать этого кабинета, я имел ввиду тебя целиком."
        g5 "Снейп?! Тебя же только что не было…"
        m "Ты мне прервал такой интимный момент…"
        sna "Ох, прости, если я помешал чему-то романтическому между тобой и дверью. Надеюсь, ты спросил согласия ее отца?"
        m "Ты все неправильно понял…"
        sna "Эта груда досок мне не жена, так что можешь не оправдываться. Как я понял, занозы любви не помеха, только это тот случай, когда лучше вынуть."
        sna "Не потому, что я боюсь появления маленьких похотливых буратино, а потому, что не хочу ходить по твоим детям."

        ">Вы прячете член"

        m "Блин, Снейп, ты же понимаешь, что всё было не так."
        sna "Я не знаю, как теперь спать буду, а ты всё продолжаешь оправдываться."
        m "А ты продолжаешь надо мной издеваться…"
        m "Ты хочешь чего-то?"
        sna "Ну разве только развидеть это. Пойду для сна приму чая с бергамотом… рюмочку."

    elif luna_stage == 2:

        $ luna.Visibility ()
        hide screen blkfade
        ">За дверью наступила тишина."
        g9 "(Хм, она засмущалась, наверное. Надо бы ее подбодрить.)"
        ">Вы начали шевелить членом."
        ">Внезапно вы чувствуете аккуратные касания вашей плоти."
        m "(Смелее, крошка, эта штука тебя не обидит...)"
        ">Ваш член медленно гладят ладонью."
        g9 "(... а может даже и похвалит.)"
        ">Вы чувствуете обе руки, которые плавно двигаются вдоль вашего члена взад и вперед."
        m "(А у тебя и не настолько плохо это получается, юная потаскушка...)"
        ">Движения становятся все быстрее, а обхват - все сильнее."
        m "(Твои движения руками просто бесподобны, даже и не знаю, что добавить...)"
        ">Темп начинает замедляться, а руки - размыкаться."
        m "(Уже наигралась? А я только начал...)"
        ">Вы внезапно чувствуете нежное прикосновение мягких влажных губ."
        m "(Ох… это не входило в нашу обучающую программу...)"
        ">Губы скользят по вашему члену от двери и до головки."
        m "(Ты явно выпрашиваешь высший бал...)"
        ">Девушка за дверью начинает облизывать ваш член, мягко покусывая."
        g9 "(А ты любительница “палочек”, я посмотрю...)"
        ">Она заглатывает головку и начинает ее страстно обсасывать."
        m "(Вот, уже лучше, идешь на медаль...)"
        ">Постепенно она принимает в рот ваш член всё глубже и глубже, пока ее губы не доходят до самой двери."
        m "(Вау… да ей не учиться, ей преподавать надо...)"
        ">Она начинает ускоряться, страстно всасывая ваш член."
        m "(Какой же у нее классный рот… Я сейчас вот-вот его заполню...)"
        ">Почувствовав нарастающее напряжение в вас, девушка останавливается и отпускает член."
        m "(Ну перестань… вернее, продолжай… не бросай меня так...)"
        ">После короткой паузы вы чувствуете, как ваш член начинает погружаться во что-то влажное и узкое."
        m "(Да, детка… этот экзамен ты сдала на отлично...)"
        ">Девушка начинает двигаться телом, скользя по вашему члену."
        m "(А эта шлюшка привыкла исполнять полную программу...)"
        ">Она двигается все быстрее и быстрее, хлопая своей попой по деревянной двери."
        m "(Она так увлеклась… могла бы уже зайти и получить свое по полной...)"
        ">Вы чувствуете, как напряжение в вас подходит к пику."
        m "(Ох, я даже не знаю, стоит ли ее предупреждать, что я вот-вот залью всю ее крохотную пещерку спермой...)"
        ">Девушка двигается с несбавляемым темпом, тихо постанывая."
        m "(В конце концов она сама виновата. Да и ее, похоже это не волнует...)"
        ">Ваше семя вот-вот вырвется наружу."
        g9 "(Плевать, кончаю в нее. Если будут претензии - скажу настолько перевозбудился, что распух и застрял в двери.)"
        ">Вы отпускаете семя в девушку."
        ">Девушка, похоже, это замечает и начинает замедляться, но даже не думает слазить."
        m "(Да, я так и знал, что этой юной шалаве это будет в кайф...)"
        ">Ваш член всё еще пульсирует в ней."
        ">Через некоторое время девушка освобождает его из своего плена."
        ">Вы решаете напоследок взглянуть через щель на оттраханную нимфоманку."

        show screen blkfade
        show screen minerva_door
        stop music
        $ renpy.play('sounds/scratch.wav')
        pause

        macgon "Я рада, что вы все-таки созрели профессор."
        g5 "(Нет… это невозможно… она… она подошла только что… да, именно… только что...)"
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 
        macgon "Думаю, нам стоит оставить это в тайне. Я не знаю, как вы догадались, что я направляюсь к вам, но мне понравился ваш настрой."
        g5 "(Этого не могло случиться… это была точно не она...)"
        macgon "В следующий раз мне все же лучше зайти, а то тут всякие студентки шастают."
        macgon "Что было бы, если Полумна развернулась и пошла обратно к вам со мной?"
        g6 "(Лучше бы она пошла обратно ко мне, а ты развернулась…)"
        macgon "В лучшем случае - испугалась бы и убежала. А в худшем - представляете, если бы мне пришлось делить вас с ней?"
        macgon "Думаю. вы и сами от этой мысли не в восторге."
        g6 "(Естественно, я не в восторге от любой мысли, где ты даже просто голая...)"
        macgon "Хотя… мы так долго к этому шли…"
        macgon "К тому же у меня никогда за всю мою долгую жизнь не было такого оригинального секса, а уж сексом меня удивить крайне сложно."
        m "(Пффф… нашлась тут Клеопатра… небось с одними котами и трахалась...)"
        macgon "Так что, если вы настаиваете, можем оставить наши маленькие свидания в таком формате…"
        m "(Да ни в жизнь!)"
        m "(Хотя… действительно, это было шикарно. Я так давно не ощущал свой член в руках профессионала… да и дверь заметно улучшает дело...)"
        macgon "Так что скажете? Вам понравилось? Вы согласны?"
        g9 "Да, во имя песчаных девов и всех их наложниц, это было поистине потрясающе!"
        macgon "Я знала, что вам понравится! Тогда я жду вашего члена, когда очередной раз постучу в дверь..."
        m "Замётано!"

        hide screen minerva_door

    hide screen blkfade

    show screen genie
    hide screen genie_stands
    hide screen chair_02 
    hide screen desk
    with Dissolve(0.2)

    $ luna_stage += 1

    return

label accident_none:
    m ".............."
    $ luna ("Странно, мне казалось, там кто-то есть…")
    m ".............."
    m "Кажется, она ушла."
    $ luna.Visibility()

    return

label accident_none2:

    m ".............."
    $ luna ("Вы, похоже, очень заняты… где-то…")
    $ luna ("Я зайду к вам, когда вы будете в кабинете.")
    $ luna ("Хм… а кому я это сказала-то?...")
    $ luna.Visibility()
    m ".............."
    m "Кажется, она ушла."

    hide screen blkfade

    show screen genie
    hide screen genie_stands
    hide screen chair_02 
    hide screen desk
    with Dissolve(0.2)

    return

init -2 python:
    def bm_check () :
        
        import os.path
        if renpy.config.savedir is not None:
            savedir_spl=renpy.config.savedir.split ("\\")
            sdir=""
            for i in savedir_spl :
                sdir=sdir + i + "/"
            
            sdir2=sdir[:-1]     
            savedir_spl2=sdir2.split("/")
            
            sdir=""
            for i in savedir_spl2[:-1] :
                sdir=sdir + i + "/"
            
            return os.path.isfile (sdir[:-1] + "/BadManners-1431362765/persistent")
        
        return False

label night_acc:

    if night_acc_stage == 0 and hermi.whoring >= 16:

        show screen blkfade

        m "Хрррррррр. Хрррррррр."
        m "Нет.... Нет.... Ох."
        m "Хрррррр-пффм. Ханс... Ханс.... Помоги..."
        m "У меня... Хррр.... Ханс, где же мой ?..."

        $ pos = POS_410
        $ renpy.play('sounds/door.mp3')

        g5 "А-А-А-А. Где мой член ?! Верните мой член ! Нееет."
        m "(Уф. Это был всего лишь сон. Какой ужас. Мне снился какой-то принц...)"
        m "(Еще там был лес... {size=+6}И у меня не было члена !{/size})"
        g6 "(Какая темная ночь. И, кажется, кто-то открыл дверь, пока я спал.)"
        m "Кто здесь ?"

        $ hermi.WrdDelAllClother()
        $ hermi.WrdMain()
        $ herView.data().addItem( 'item_pose_black_latex' )

        $ herView.hideshowQQ( "s02.png", pos )

        pause

        her "Привет, Джинни !"
        g6 "Привет, Гермиона."
        g6 "Чем обязан ночному виз..."
        g5 "{size=+4}Как ты меня назвала ?{/size}"
        $ herView.hideshowQQ( "s04.png", pos )
        her "Джинни, кончай валять дурака !"
        m "(Что происходит ? Мой секрет в опасности !)"
        m "Мисс Грейнджер, я не понимаю, о чем вы."
        m "Здесь только вы и я, поэтому..."
        $ herView.hideshowQQ( "s02.png", pos )
        her "Заткнись и слушай. Ты нужен Хансу прямо сейчас, так что хватит предаваться разврату во сне и просыпайся уже."
        g1 "Что ? Нет, постой, откуда ты знаешь про Ханса ? Это был мой сон !"
        $ herView.hideshowQQ( "s05.png", pos )
        her "Сон ?"
        her "Именно сейчас ты спишь, лентяй !"
        her "Мне пришлось проникнуть в твои грезы, чтобы вызвать в реальный мир."
        m "Реальный мир ? Нет, не может быть..."
        $ herView.hideshowQQ( "s02.png", pos )
        her "Да, и дело очень важное..."
        g5 "Ты намекаешь, что у меня {size=+6}на самом деле нет члена ?{/size}"
        g8 "Что-то в глазах потемнело..."

        $ herView.hideQ()

        $ hermi.WrdSetMain()

        hide screen blkfade

        $ night_acc_stage = 1

    elif night_acc_stage == 2 and hermi.whoring >= 18:

        show screen blkfade

        m "Хрррпфффффф. Хрпфффффф. Умпф."
        m "Ханс, Ханс, а знаешь, кого я трахал во сне ?"
        m "А вот и не угадал. Хррпфффф."
        m "Хррррр. Хрррр. Да... да да, сразу две студентки..."

        $ pos = POS_410
        $ renpy.play('sounds/door.mp3')

        g1 "Аа-а. Кто здесь ?"

        $ hermi.WrdDelAllClother()
        $ hermi.WrdMain()
        $ herView.data().addItem( 'item_pose_black_latex' )

        $ herView.hideshowQQ( "s02.png", pos )

        pause

        her "Опять спит, лентяй."
        m "Гермиона ?"
        $ herView.hideshowQQ( "s05.png", pos )
        her "Кто ? А, ты про эту девочку. Я использовала ее тело, чтобы разговаривать в твоем сне."
        g6 "Вот как ? Тогда кто же ты ?"
        $ herView.hideshowQQ( "s06.png", pos )
        her "Большой член ты себе вообразил, а на ум поскупился. Разумеется я Меридиана. Надеюсь, это был последний глупый вопрос."
        g1 "Меридиана ? Тут ? Погоди, ты же часть моего сна ? Но как ?"
        $ herView.hideshowQQ( "s05.png", pos )
        meri "(facepalm)"
        meri "Ну да, конечно, тебе приятно считать реальностью именно этот странный мир."
        $ herView.hideshowQQ( "s02.png", pos )
        meri "Но я здесь не для дурацких споров."
        meri "Нам с Хансом нужно, чтобы ты кое-что узнал с помощью своей особой силы. Так что прощайся со своим маленьким воображаемым другом и бегом за мной."
        g5 "Моим мале... {size=+6}Что ? Ты хочешь сказать, что у меня нет...{/size}"
        g8 "Апф. Воздуха... Мне не хватает воздуха... В глазах темнеет."
        $ herView.hideshowQQ( "s05.png", pos )
        meri "Стой ! Куда ты опять пропадаешь ? Стоять я ска..."

        $ herView.hideQ()

        $ hermi.WrdSetMain()

        hide screen blkfade

        $ night_acc_stage = 3

    elif night_acc_stage == 4 and hermi.whoring >= 20:

        g10 "У меня дурное предчувствие."
        g10 "Лучше крепко держаться за самые ценные предметы."

        hide screen genie
        show screen genie_jerking_off

        m "Как хочется спать..."

        show screen blkfade

        $ pos = POS_410
        $ renpy.play('sounds/door.mp3')

        $ hermi.WrdDelAllClother()
        $ hermi.WrdMain()
        $ herView.data().addItem( 'item_pose_black_latex' )

        $ herView.hideshowQQ( "s02.png", pos )

        pause

        meri "Эй, Джин ! Джи-и-и-н."
        meri "Вот же бесполезное создание."
        m "(Тсссс. Я уверен, что если молчать, то она уйдет и не будет больше меня пугать.)"

        $ herView.hideshowQQ( "s06.png", pos )
        meri "Хорошо, оставлю новости о твоем члене до следующего раза."

        $ herView.hideQ()

        pause 1

        g5 "Нет ! Я тут ! Меридиана ! Мери..."

        $ herView.hideshowQQ( "s03.png", pos )
        meri "Я смотрю, ты тут неплохо устроился. Директор школы, значит ? Юные ведьмы и всякое такое ?"
        meri "Небось падают прямо на твою палку безо всяких усилий ?"
        meri "Возможно, я промахнулась игр... клиентом."

        m "Да, но теперь, когда я знаю правду..."
        g1 "Когда я уже не верю в существование своей трости, своего скипетра, своего магического жезла, своего..."

        $ herView.hideshowQQ( "s01.png", pos )
        meri "Вот разошелся..."

        g1 "Мой талисман... моя ветка древа жизни... моя... моя..."
        g4 "Моя прелессссть. Я не отдам вам мою прелессссть..."

        $ herView.hideshowQQ( "s04.png", pos )
        meri "Да уймись уже."

        $ herView.hideshowQQ( "s07.png", pos )
        meri "Дело в том, что возникло недопонимание."
        g7 "То есть именно ты и Ханс с Дороти живете во сне ?"

        meri "Все немного сложнее. В реальности существуют оба мира, а контактируют они во сне."

        g1 "То есть все это время я зря засыпал со своим жезлом в руке ? Зря каждый раз прощался с ним перед сном ?"
        g1 "Зря дро... Кхм. Зря трахался каждый раз как в последний ?"
        g4 "{size=+6}Аргх.{/size}"

        $ herView.hideshowQQ( "s03.png", pos )
        meri "Ну извини, так вышло."

        g4 "Да ты знаешь, что я сейчас с тобой сделаю ?"
        g4 "Я и сам пока этого не знаю !"
        g9 "Но тело Гермионы всегда меня заводит, да еще в такой одежде. Так что..."
        g9 "А ну ка, посмотрим поближе, а то в темноте почти ничего не видно..."

        $ herView.hideshowQQ( "s05.png", pos )
        meri "(Э, минутку. Если я займусь этим в чужом теле под заклинанием временного вселения, то...)"
        $ herView.hideshowQQ( "s02.png", pos )
        meri "{size=+6}Стоять !{/size}"
        meri "Нечего подкрадываться в темноте !"
        meri "Я... я ухожу !"

        $ herView.hideQ()
        $ renpy.play('sounds/door.mp3')

        pause.5

        m "Эх, упустил. А могла быть чудная ночь."

        $ hermi.WrdSetMain()

        hide screen blkfade

        $ night_acc_stage = 5

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii





label dap_request_04:

    $ music("Daphne Theme")

label dap_request_04_complete:
    if daphne.whoring < 11:
        $ hero("Думаю, мне не стоит торопиться...// Может позже....")
        call daphne_main_menu_requests
    elif hero.Items.Count("wine") == 0:
        $ hero("Для подобных разговоров необходимо «Вино Дамбулдора»")
        call daphne_main_menu_requests
    pass
    if IsRunNumber(1):
        $ hero("Хм....// Мисс, как вы относитесь к алкоголю?")
        $ daphne("~46 00 2 ope// На что вы намекаете, профессор?")
        $ hero("Я просто хотел угостить вас вином, из собственного запаса...// Ну раз вы против...")
        $ daphne("~55 02 1 smi// Чего ради, сэр?")
        $ hero("Хотябы ради того, что вы поднялись на 2 пункта в общих списках.")
        $ daphne("~26 w0 1 ope// Что!?// За меня в правду начали голосовать?")
        $ hero("Голосовать!?// Да за вас отдают свои голоса, даже дружки ваших конкуренток...")
        $ daphne("Правда?!//~46 c1 2 smi// Это так приятно...// Хм....// Ну хорошо, профессор.... раз такое дело...//~26 s0 3 smi// Пожалуй я выпью с вами.")

        $ screens.Show(Dissolve(1), "blkfade")
        $ hero.Items.AddItem("wine", -1)
        pause.5
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Ну как мисс, вам понравилось?")
        $ daphne("~72 00 2 smi// Безусловно...// Очень богатый букет...")
        $ hero("Я рад, что вы можете оценить это по достоинству...// Еще желаете?")
        $ daphne("~46 01 1 neu// Эм... нет, профессор... думаю мне достаточно...")
        $ hero("Ну что ж, Дафна...// Я даже не поинтересовался вашими делами с...")
        $ daphne("~46 00 2 ehh// С мальчиками, сэр?")
        $ hero("Именно.")
        $ daphne("~55 02 2 pri// Ну... Все идет довольно не плохо...// Эм... Ну кажется мое поведение и в правду начало нравится парням.")
        $ hero("Были ли какие-то намеки на это?")
        $ daphne("~46 00 2 dis// Ну если это можно назвать намеком...//~26 01 1 pri// Мне понравился один парень из команды Слизерина по квидичу...// И я сказала что если они победят в игре, я подарю ему поцелуй...")
        $ hero("И что же?")
        $ daphne("~64 01 2 smi// Я сдержала свое обещание, ведь он и в правду не плохо играл...")
        $ hero("Вы не сожалеете об этом, мисс?")
        $ daphne("~46 01 2 neu// Конечно нет.// Что в этом такого...//~48 c1 2 ehh// Это же просто поцелуй...")
        $ hero("Это похвально.")
        $ daphne("~55 s2 2 smi// Спасибо...")
        $ hero("Ну хорошо мисс Гринграсс, можете взять мой не большой подарок, и быть свободны.")
        $ daphne.whoring += 1
        $ SetHearts(1)

    elif IsRunNumber(2):
        if hero.Items.Count("wine") == 0:
            $ hero("Для подобных разговоров необходимо «Вино Дамбулдора»")
            call daphne_main_menu_requests
        else:
            $ hero("Мисс, как вы смотрите на то, что бы выпить со мной?")
            $ daphne("~46 00 1 neu// Если только это...// Останется между нами.")
            $ hero("Конечно.")

        $ screens.Show(Dissolve(1), "blkfade")
        pause.5
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Хм....// Эм....")
        $ daphne("~55 01 2 pou// Что-то не так, профессор?")
        $ hero("Эм... да не то чтобы...// ..........// Давайте повторим, и я вам все расскажу.")
        $ daphne("~46 00 1 smi// Ну хорошо, давайте...")

        $ screens.Show(Dissolve(1), "blkfade")
        $ hero.Items.AddItem("wine", -1)
        pause.5
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Эм... в общем, ваше положение в списке...// Ухудшается, мисс...")
        $ daphne("~86 w0 2 dis// Как?!//~46 01 1 dis// Я ведь делаю все, чтобы....")
        $ hero("Видимо этого не достаточно, мисс...// Понимаете?")
        $ daphne("~26 00 2 pou// Не совсем, сэр...")
        $ hero("Я хочу сказать, что ваши конкурентки, по какой-то причине опережают вас...// И тут нужно действовать быстро и решительно...// Ведь до начала уже совсем не долго...")
        $ daphne("Эм....//~46 01 1 neu// Я полагаю что вы правы, профессор.// Но... что я еще могу сделать?")
        $ hero("Мисс Гринграсс, я думаю что вам не хватает уверенности...// Что не скажешь о других...")
        $ daphne("~55 00 1 ope// Но... Я же выполняю все ваши поручения, сэр...// Прислушиваюсь к каждому вашиму совету...")
        $ hero("И я не могу не похвалить вас за это...// Но если поручение будет вам не посильным...// Вы справитесь?")
        $ daphne("~26 01 2 pou// Э-э... Смотря о чем будет идти речь...")
        $ hero("Скажем....// Я попрошу показать мне, вашу грудь...// Это вам под силу?")
        $ daphne("~46 02 3 dis// ..........//~26 01 2 neu// Я... я не знаю, профессор...")
        $ hero("А что мешает вам попробовать?")
        $ daphne("~46 00 2 neu// Эм... Сейчас?")
        $ hero("Именно.")
        $ daphne("Хорошо...//~46 02 1 pri// Дайте мне минутку.")

        $ screens.Show(Dissolve(1), "blkfade")
        pause.5
        "> Сложно не заметить волнение Дафны..."
        "> Но, после долгой возни с бюстгальтером..."
        $ daphne.ItemsCustomize(update={"combi:default_up"}).chibi.State(appearance="a").Trans("tits center")
        $ daphne.ItemsCustomize(delete={"bra"}).chibi.State(appearance="a").Trans("tits center")
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Великолепно Дафна.// Признаться я не думал...")
        $ daphne("~46 01 1 pri// Эм... что-то еще, сэр?")
        $ hero("Гхм... да, мисс...// Вы не могли бы подойти по ближе?")
        $ daphne("~62 s2 2 neu// Э-э... Это обязательно, профессор?")
        $ hero("Да, девушка...")
        $ daphne("~46 01 1 neu// Ну... хорошо...// Только пообещайте что не будете прикасаться...//~55 00 2 dis// Эм... трогать...")
        $ hero("Я вас понял, мисс...// Я буду просто смотреть.")
        $ daphne("~78 s2 1 def//Хорошо...")

        $ screens.Show(Dissolve(1), "blkfade")
        "> Слегка волнуясь, Дафна подходит к вашему столу..."
        hide screen genie
        hide screen desk
        show screen look_02
        $ daphne.chibi.Hide()
        pause.5
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Потрясающе...// У вас довольно привлекательные сись... эм... грудь, мисс.")
        $ daphne("~46 01 2 dis// Профессор, пожалуйста...")
        $ hero("Преодолевайте свое стеснение, мисс...// Если вас не будет смущать это, то более легкие задания...// Вы будете щелкать как орешки.")
        $ daphne("~55 01 2 neu// Хорошо, сэр...//~22 00 1 smi// Я постараюсь...")
        $ hero(g9, "#(Вот и славно)")
        label fel1:
            menu:
                "- Просто смотреть -":
                    $ hero(m, "Это восхитительно...// Ваша грудь, мисс, такая молодая...// Смотреть на неё одно удовольствие...")
                    $ daphne("~55 01 1 pou// ...........//~46 01 1 ope// Возможно вы правы, сэр...")
                    $ hero("Молодец Дафна...// Не останавливайся...")
                    $ daphne("~66 00 2 pou// Но она меньше чем у других, профессор...// И я кажется комплексую по этому поводу...")
                    $ hero("Глупости...// Ваша грудь вполне средних размеров...// Да и к тому же на много красивее, чем у этих эм... полукровок...")
                    $ daphne("~46 01 1 smi// Верно... я и сама догадывалась...// Что так и есть на самом деле.")
                    $ hero(g9, "#(Хотя до Гермионы здесь еще далеко)")
                    $ daphne("~46 00 1 pou// Эм...  Сэр, что, простите...")
                    $ hero(m, "Ох... Это просто восхищение Дафна, не обращай внимания...")
                    $ daphne("~46 01 0 smi// Слушаюсь...")
                    $ hero(g9, "#(Скоро это слово будет звучать чаще)")
                    "Вы еще какое-то время смотрите на грудь Дафны..."
                    pause.5
                    $ hero(m, "Что ж, мисс... можете одеваться.")
                    $ daphne("Хорошо.")

                    $ screens.Show(Dissolve(1), "blkfade")
                    $ daphne.ItemsCustomize(update={"combi:daphne_combi_handsonhip"}).chibi.State(appearance="a")
                    show screen genie
                    hide screen look_02
                    pause.5
                    $ screens.Hide(Dissolve(1), "blkfade")

                    $ daphne.whoring += 1
                    $ SetHearts(2)
                "- Начать дрочить -":

                    $ screens.Show(Dissolve(1), "blkfade")
                    "> Вы достаете свой член, и начинаете дрочить глядя на Дафну..."
                    pause.5
                    hide screen look_02
                    $ genie_chibi_xpos = -185
                    $ genie_chibi_ypos = 10
                    $ g_c_u_pic = "jerking_off_02_ani"
                    show screen chair_02
                    show screen g_c_u
                    show screen look_fap_01
                    $ daphne.chibi.Hide()
                    $ screens.Hide(Dissolve(1), "blkfade")

                    $ hero(m, "О, да...")
                    $ daphne("~55 00 2 dis// {size=+5}Профессор что вы делаете?!{/size}// Уберите эту штуку!")
                    $ hero("На что вы жалуете, мисс?// Разве я вас трогаю?")
                    $ daphne("Да но вы трогаете его...//~74 w2 3 dis// Это...")

                    $ screens.Show(Dissolve(1), "blkfade")
                    pause.5
                    $ screens.Hide(Dissolve(1), "blkfade")

                    $ daphne.liking-=5
                    $ hero("Хорошо... Я кажется немного перегнул...// Давайте забудем это...")
                    $ daphne(".........")
                    hide screen g_c_u
                    hide screen chair_02
                    hide screen look_fap_01
                    show screen look_02
                    jump fel1
                "- Схватить Дафну за грудь -":
                    "Вы протягиваете руки, чтобы схватить Дафну за грудь..."
                    $ daphne("~55 02 2 wo// ПРОФЕССОР!!!// Что вы себе поз...")
                    $ hero(m, "Расслабься Дафна, я просто хочу потрогать её...")
                    $ daphne("~46 01 2 dis// Профессор это слишком...// Я могу вам позволять такое...")
                    $ daphne.liking-=10
                    $ hero("Хорошо... Я кажется немного перегнул...// Давайте забудем это...")
                    $ daphne(".........")
                    jump fel1

        show screen genie
        hide screen look_02
        $ daphne.chibi.Refresh()
        $ hero("Вы сегодня на славу постарались, и у меня есть отличный подарок для вас.")

    elif IsRunNumber(3):
        if hero.Items.Count("wine") == 0:
            $ hero("Для подобных разговоров необходимо «Вино Дамбулдора»")
            call daphne_main_menu_requests
        else:
            $ hero("Мисс, как вы смотрите на то, что бы выпить со мной?")
            $ daphne("~46 00 1 neu// Если только это...// Останется между нами.")
            $ hero("Конечно.")

        $ screens.Show(Dissolve(1), "blkfade")
        pause.5
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Хм....// Эм....")
        $ daphne("~55 01 2 pou// Что-то не так, профессор?")
        $ hero("Эм... да не то чтобы...// ..........// Давайте повторим, и я вам все расскажу.")
        $ daphne("~46 00 1 smi// Ну хорошо, давайте...")

        $ screens.Show(Dissolve(1), "blkfade")
        $ hero.Items.AddItem("wine", -1)
        pause.5
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Мисс, я хочу попросить вас, показать мне вашу грудь.")
        $ daphne("~46 01 3 smi// Снова, сэр?")
        $ hero("Да, мисс...")
        $ daphne("~55 00 2 def// Хорошо...//~46 w2 2 neu// Дайте мне минутку.")

        $ screens.Show(Dissolve(1), "blkfade")
        "Сложно не заметить как Дафна скрывает свое волнение ..."
        "И после долгой возни с бюстгальтером..."
        $ daphne.ItemsCustomize(update={"combi:default_up"}).chibi.State(appearance="a").Trans("tits center")
        $ daphne.ItemsCustomize(delete={"bra"}).chibi.State(appearance="a").Trans("tits center")
        pause.5
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Великолепно Дафна.// Признаться я не думал...")
        $ daphne("~46 01 1 neu// Эм... что-то еще, сэр?")
        $ hero("Гхм... да, мисс...// Вы не могли бы подойти по ближе?")
        $ daphne("~62 00 2 dis// Э-э... Это обязательно, профессор?")
        $ hero("Да, девушка...")
        $ daphne("~46 01 1 neu// Ну... хорошо...// Только пообещайте что не будете прикасаться...//~55 00 2 dis// Эм... трогать...")
        $ hero("Я вас понял, мисс...// Я буду просто смотреть.")
        $ daphne("~78 s2 1 pri//Хорошо...")

        $ screens.Show(Dissolve(1), "blkfade")
        "> Немного волнуясь, Дафна подходит к вашему столу..."
        hide screen genie
        show screen look_02
        $ daphne.chibi.Hide()
        pause.5
        $ screens.Hide(Dissolve(1), "blkfade")

        $ hero("Потрясающе...// У вас довольно привлекательные сись... эм... грудь, мисс.")
        $ daphne("~46 01 2 dis// Профессор, пожалуйста...")
        $ hero("Преодолевайте свое стеснение, мисс...// Если вас не будет смущать это, то более легкие задания...// Вы будете щелкать как орешки.")
        $ daphne("~55 01 2 neu// Хорошо, сэр...//~22 w00 1 smi// Я постараюсь...")
        $ hero(g9, "#(Вот и славно)")
        label fel2:
            menu:
                "- Просто смотреть -":
                    $ hero(m, "Кажется это мы уже проходили...// Полагаю стоит попробовать что-то по веселее...")
                    jump fel2
                "- Начать дрочить -":

                    $ screens.Show(Dissolve(1), "blkfade")
                    "> Вы достаете свой член, и начинаете дрочить глядя на Дафну..."
                    pause.5
                    hide screen look_02
                    $ genie_chibi_xpos = -185
                    $ genie_chibi_ypos = 10
                    $ g_c_u_pic = "jerking_off_02_ani"
                    show screen chair_02
                    show screen g_c_u
                    show screen look_fap_01
                    $ daphne.chibi.Hide()
                    $ screens.Hide(Dissolve(1), "blkfade")

                    $ hero(m, "О, да...")
                    $ daphne("~55 00 2 wo// {size=+5}Профессор что вы делаете?!{/size}// Уберите эту штуку!")
                    $ hero("На что вы жалуете, мисс?// Разве я вас трогаю?")
                    $ daphne("Да но вы трогаете его...//~64 01 3 dis// Это...")
                    $ hero("Что «Это», мисс?// Хотите сказать «это» вас смущает?// Хотите сказать, что чувствуете себя не ловко?")
                    $ daphne("~26 01 2 neu// Эм... Нет, сэр...// Все в порядке, простите...")
                    $ hero(g9, "#(Вот это хватка)")
                    "Вы продолжаете дрочить на Дафну..."
                    "*Фап - фап - фап*"
                    $ daphne("~55 01 2 neu//..........// Профессор, я хотела сказать...// Что бы вы предупредили, о том...//~55 w1 2 ope// Когда вы будете... эм... заканчивать...")
                    $ hero(m, "О, разумеется, мисс...// Не переживайте.")
                    $ daphne("~36 01 1 neu// Спасибо....// Сэр....")
                    "Вы набираете более быстрый темп..."
                    "*Фап - фап - фап*"
                    $ hero("Дафна, не отводи от меня взгляд...// Смотрите мне прямо в глаза...")
                    $ daphne("~55 00 2 ang// Это обязательно, профессор?")
                    $ hero("Ты сомневаешься?")
                    $ daphne("~55 01 2 neu// Нет, сэр... Ни в коем случае...// #(Черт... что я делаю?)//~26 00 2 dis// #(Нужно уходить от сюда)")
                    $ hero("Гхм... Скажите, мисс...// Что вы думаете о моем члене?")
                    $ daphne("О члене, сэр?!//~78 01 2 dis// Я не знаю....//~55 00 2 neu// Эм... он большой, сэр...")
                    $ hero("Думаете?")
                    $ daphne("~55 00 2 neu// Да, несомненно это самый огромный член, который я видела...")
                    $ hero("Вам он нравится, Дафна?")
                    $ daphne("~55 00 1 pri// Безусловно, сэр...//~26 00 2 neu// Ваш член на столь огромен, что думаю девочки пугаются одного его вида...")
                    $ hero("Черт! Да....// Кажется я приближаюсь к финалу...// Думаю стоит сбавить темп.")

                    $ screens.Show(Dissolve(1), "blkfade")
                    pause.5
                    hide screen g_c_u
                    hide screen look_fap_01
                    hide screen chair_02
                    show screen look_02
                    $ screens.Hide(Dissolve(1), "blkfade")

                    $ hero("Что ж, вот это высочайшая сила воли...// Ах, да... Можете уже прикрыться, мисс...")

                    $ screens.Show(Dissolve(1), "blkfade")
                    $ daphne.ItemsCustomize(update={"combi:daphne_combi_handsonhip"}).chibi.State(appearance="a")
                    pause.5
                    $ screens.Hide(Dissolve(1), "blkfade")

                    $ daphne.liking-=2
                    $ daphne.whoring += 1
                    $ SetHearts(3)
                "- Схватить Дафну за грудь -":
                    "Вы протягиваете руки, чтобы схватить Дафну за грудь..."
                    $ daphne("~55 02 2 wo// ПРОФЕССОР!!!// Что вы себе поз...")
                    $ hero(m, "Расслабься Дафна, я просто хочу потрогать её...")
                    $ daphne("~46 01 2 dis// Профессор это слишком...// Я могу вам позволять такое...")
                    $ daphne.liking-=10
                    $ hero("Хорошо... Я кажется немного перегнул...// Давайте забудем это...")
                    $ daphne(".........")
                    jump fel2

        show screen genie
        hide screen look_02
        $ daphne.chibi.Refresh()
        $ hero("Вы сегодня на славу постарались, и у меня есть подходящий подарок для вас.")
















































































































    elif IsRunNumber(4):
        $ hero("#(На мой взгляд, в этой сфере Дафна уже вполне преуспела)")
        call daphne_main_menu_requests

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
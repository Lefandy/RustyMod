




label daphne_giving:
    $ item=itsDAHR(choose.choice)
    $ daphne_giving_return=choose.escLabel

    if item.Name=="wine":
        if daphne.whoring<6:
            $ daphne("~55 w0 1 ang// Вино, сэр?// Я,.. я даже не знаю.//~55 01 1 ehh// Я, конечно, совершеннолетняя, но мама считает, что мне все равно рано."),
            $ hero("Но вы ведь хотите попробовать, мисс Гринграсс.")
            $ daphne("~64 00 1 smo// Да, пожалуй.//~55 01 1 pou// Но на прошлом \"Осеннем балу\" я что-то такое попробовала, а потом... //~55 01 2 dis// мне рассказывали, что я... даже лезла целоваться с полукровкой.// Но я ничего такого не помню.")
            $ hero("О, думаю, это была просто случайность. Я уверен, что вы готовы пить вино, уже как вполне взрослая женщина."),
            $ daphne("~55 00 1 def// Да, сэр, конечно. Спасибо, что верите в меня.")
            call daphne_changeliking (+3)
        elif daphne.whoring>=6:
            if daphne.Items(item.Name)._count==0:
                $ daphne("~55 w0 1 ang// Вино, сэр?// Я,.. я даже не знаю.")
                $ hero("Это особый подарок для особой студентки, мисс.")
            $ daphne("~55 00 1 smo// Спасибо, сэр. Я припрячу, чтобы никто из ЭТИХ не увидел.")
            $ hero("Жду, вашего рассказа, как вам понравилось. Впрочем, если захотите посидеть в компании, я к вашим услугам.")
            $ daphne("~55 00 1 def// Спасибо, сэр.")
            call daphne_changeliking (+6)

    if item.Name=="beer":
        if daphne.whoring<6:
            $ daphne("~37 c0 1 pri// Не думаю, что это хорошая идея, сэр.// Вы даете пиво своему студенту? Пиво запрещено в Хогвартсе!")
            $ hero("Мисс, Гринграсс, ОБЫЧНОМУ студенту, разумеется, я не дал бы пива. Но ВАМ... Вы - совсем другое дело.")
            $ daphne("~64 00 1 smo// О!...//.....//~55 00 1 smi// Вы, конечно, правы, сэр.")
            call daphne_changeliking (+4)
        elif daphne.whoring>=6:
            $ daphne("~55 00 1 smi// Пиво запрещено в Хогвартсе, сэр.// Но из уважения к вам я возьму.")
            call daphne_changeliking (+8)

    if item.Name=="candy":

        $ daphne("~55 00 1 pri// Конфета? Сэр, это даже оскорбительно!// Вы считаете меня маленькой?")
        call daphne_changeliking (-5)

    if item.Name=="chocolate":

        $ daphne("~55 00 1 neu// Хм... Говорят, от него толстеют.//~55 00 1 smi// Я, пожалуй, возьму, сэр. Просто чтобы показать, что ценю вашу заботу.")
        call daphne_changeliking (0)

    if item.Name=="owl":

        $ daphne("~37 00 1 pou// Похоже на китайскую игрушку из дешевого ларька для недоволшебников.//"
                "Наверное, какое-нибудь мугродье порадуется такому подарку, сэр.//"
                "~37 00 1 smo// Но один мой подарок на день рождения стоит больше, чем все совы из этого ларька.//"
                "И сам ларек с продавцом впридачу."),
        call daphne_changeliking (-6)

    if item.Name=="mag1":

        $ daphne("~55 00 1 pur// Что за скука!// Зачем вы мне предлагаете такое, сэр?")
        call daphne_changeliking (-5)

    if item.Name=="mag2":

        $ daphne("~55 00 1 neu// Это чтиво для девчонок-полукровок, сэр... Но я, пожалуй, возьму.//~55 00 1 ope// Просто, лишний раз убедиться, что они в подметки мне не годятся...")
        call daphne_changeliking (+2)

    if item.Name=="mag3":

        $ daphne("~55 01 1 neu// Гхм... Это такой намек, что у меня нет парня, сэр?//~37 00 1 neu// А у меня - есть, вот так!//~46 00 1 def// Ладно уж, я возьму.// Хотя все это я и так знаю. И про парней... и про все остальное.")
        call daphne_changeliking (+1)

    if item.Name=="mag4":

        $ daphne("~46 00 1 dis// Что это вообще за подарок, сэр?! Это отвратительно, чистокровные девочки ничем подобным не занимаются!")

        call daphne_changeliking (-5)

    if item.Name=="condoms":

        $ daphne("~37 c0 1 pri// Презервативы? Зачем они мне, я ни с кем...//"
                "~37 00 1 pur// Эмм... Я хотела сказать...//~37 01 1 pur// Нет, конечно же, я уже долго встречаюсь с достойным, высоким и красивым парнем... И мы часто с ним...//~37 01 1 ope// В общем, давайте их сюда, профессор!...// Хотя они мне и не нужны, у нас и так все хорошо!"),
        call daphne_changeliking (0)

    if item.Name=="perfume":
        $ Say("> Вы собираетесь подарить Дафне духи, но они чудесным образом не даются вам в руки.//"
            "> После нескольких безуспешных попыток схватить уворачивающийся флакончик, вы решаете отказаться от этой идеи, чтобы не выглядеть полным идиотом.")
        $ item=None
        jump expression daphne_giving_return

    if item.Name=="vibrator":

        $ daphne("~55 w0 1 def// Хм, странная вещица. Ой, она жужжит и трясется.// Это миксер для кухни или что-то вроде того?//~37 s0 1 pou// Пф! Я вам не кухарка, сэр!")
        call daphne_changeliking (-8)

    if item.Name=="lubricant":

        $ daphne("~64 s0 1 dis// Какая-то жирная дрянь.//~64 00 1 pou// Хотя... Это похоже на крем для загара.//~64 00 1 smi// Спасибо, сэр. Я попробую намазаться им завтра после уроков!")
        call daphne_changeliking (+4)

    if item.Name=="ballgag":

        $ daphne("~26 00 1 smi// О, сэр!// С каким удовольствием я надела бы это на какую-нибудь грязнокровку, а потом излупила ее плеткой!//~26 00 1 gri// Надеюсь, этот день когда-нибудь наступит.")
        call daphne_changeliking (+10)

    if item.Name=="plug":

        $ daphne("~64 00 1 ehh// Даже не пойму, что это такое. Затычка от ванной?// Возьму ее с собой, когда буду мыться. Спасибо, сэр.")
        call daphne_changeliking (+1)

    if item.Name=="strapon":

        $ daphne("~64 00 1 dis// Это напоминает мне...//~64 00 1 pou// Нет, не может быть. Не думаю...")
        call daphne_changeliking (-1)

    if item.Name=="krum":

        $ daphne("~55 00 1 smo// О, этот парень. Он, конечно, худородный, но, в принципе, ничего...//"
                "~46 00 1 pou// Только не подумайте, что я интересуюсь худородными, профессор, и повешу плакат у себя над кроватью!")
        call daphne_changeliking (+2)

    if item.Name=="lingerie":

        $ daphne("~64 00 1 pur// О, эмм... Это слишком смело.// И потом...//~46 01 2 pur// Ну, мой парень, помните рассказывала, он высокий красивый и все такое. Вот он недавно подарил мне это.//~46 00 1 pur// Так что я, воздержусь, сэр.")
        call daphne_changeliking (-2)

    if item.Name=="broom":

        $ daphne("~55 00 1 neu// Хм, метла... Я не слишком люблю летать, сэр.//~55 00 1 ehh// И потом вот этот выступ.// Не пойму, зачем его сделали, он же только мешает.//~55 01 2 ehh// Того и гляди, воткнется в... куда не надо.")
        call daphne_changeliking (-3)

    if item.Name=="sexdoll":

        $ daphne("~55 w0 2 ehh// Это... это кукла для секса?!//~55 01 2 ehh// Сэр, иногда мне кажется, что вы - извращенец... эмм, совсем немного, конечно.//"
                "~55 00 2 pur// Но предлагать такое - девушке?!")
        call daphne_changeliking (-10)

    if item.Name=="badge":

        $ daphne("~37 00 1 dis// Профессор, это ведь значок общества сук этой мугродки Грейнджер! Или какого-то другого ее общества!//~26 00 1 dis// Как вы можете предлагать мне ТАКОЕ?!")
        call daphne_changeliking (-20)

    if item.Name=="nets":

        $ daphne("~55 00 1 smi// Довольная приятная вещица, сэр (хотя я видала и получше).... Спасибо!")
        call daphne_changeliking (+5)

    if item.Name in {"shortskirt", "xshortskirt", "xxshortskirt", "xsmallskirt", "xxsmallskirt", "xxxsmallskirt", "skirt_cheerleader", "skirt_business", }:

        $ daphne("~55 00 1 pou// Хм... Она слишком короткая. Не думаю, что захочу ее одевать.")
        $ hero("Хорошо, тогда я предложу эту юбку мисс Грейнджер.")
        $ daphne("~55 w0 1 ope// Что?! Вы хотите сделать подарок грязнокровке?!")
        $ hero("Мисс, в Хогвартсе планируется изменение формы, и я думал, вам приятно будет первой получить вещь, которой еще ни у кого нет.//"
                "Но раз вы против, мне придется обратиться к мисс Грейнджер. Юбку должна получить первая девушка факультета, раз не вы, видимо это будет Грейнджер, все-таки по учебе она...")
        $ daphne("~37 s0 1 ope// ГРРХ!! Дайте сюда, я еще раз просмотрю!")
        $ daphne("~37 s0 1 pri// ........................")
        $ daphne("~37 s0 1 pou// Я беру эту юбку!//# И ничего она не короткая, мне просто показалось.")
        call daphne_changeliking (0)

    if item.Name in {"skimpyshirt", "shirt_cheerleader", "shirt_business", "tights", }:
        ">Подумав, вы поняли, что это не лучшая идея."
        $ item=None
        jump expression daphne_giving_return

    if daphne_giving_return=="daphne_main_menu":
        $ daphne.CommitGift()
    jump expression daphne_giving_return

label daphne_item_on(item):
    if item.Name=="skirt":
        pass

label daphne_item_off(item):
    if item.Name=="skirt":
        pass



label daphne_changeliking(_m1_daphne_gifts__liking):
    $ daphne.liking+=_m1_daphne_gifts__liking
    if _m1_daphne_gifts__liking>=0:
        $ daphne.Items.Receive(hero.Items, item.Name)


    if _m1_daphne_gifts__liking<0:
        ">Настроение Дафны ухудшилось...\n>Дафна {size=+5}злится{/size} на вас..."
    elif _m1_daphne_gifts__liking==0:
        ">Настроение Дафны не изменилось..."
    else:
        if daphne.liking < 0:
            ">Настроение Дафны улучшено...\n>Дафна {size=+5}огорчена вами{/size}..."
        elif daphne.liking == 0:
            ">Настроение Дафны улучшено...\n>Дафна {size=+5}не злится{/size} на вас..."
        else:
            ">Настроение Дафны улучшено...\n>Дафне {size=+5}приятно ваше общество{/size}..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
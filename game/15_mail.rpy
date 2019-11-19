label mail:

    $ this.RunStep("MAIL")
    if got_paycheck == True and finished_report >= 1 and letter_from_ficbook_fun == False:
        $ letters -= 1
        $ got_paycheck = False
        if letters <= 0:
            hide screen owl
            show screen owl_02
        ">Вы читаете свои сообщения."
        play sound "sounds/money.mp3"  

        $ dgold=([40, 70, 90, 110, 150, 200][finished_report-1])*turbo
        $ letter_text = "{size=-7}ОТ:Министерства Магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим Вас за отчеты, присланные на этой неделе.\n Ваша оплата:{/size} \n{size=+4}[dgold] галеонов.{/size}\n\n\n{size=-3}-С уважением-{/size}"
        hide screen points
        $ gold += dgold
        show screen points


        show screen bld1
        show screen letter
        show screen ctc
        pause
        hide screen letter
        hide screen bld1
        hide screen ctc


        $ finished_report = 0

        if (hermi._incomePercent>0):
            $ dgold=dgold*hermi._incomePercent//100
            hide screen points
            $ gold-=dgold
            show screen points
            "> Согласно вашему соглашению с Гермионой [dgold] галеонов ([hermi._incomePercent]%%) перечисляются на ее счет"
        call screen main_menu_01


    if got_paycheck == True and finished_report >= 1 and letter_from_ficbook_fun == True:
        $ one_of_ten = renpy.random.randint(1, 6)
        $ letters -= 1
        $ got_paycheck = False
        if letters <= 0:
            hide screen owl
            show screen owl_02
        ">Вы читаете свои сообщения."



        $ dgold=([80, 140, 180, 220, 300, 400][finished_report-1])*turbo

        if one_of_ten == 1:
            play sound "sounds/money.mp3"  
            $ letter_text = "{size=-7}ОТ:Министерства Магии\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-2}Благодарим Вас за отчеты, присланные на этой неделе.\n Ваша оплата:{/size} \n{size=+4}[dgold] галеонов.{/size}\n\n\n{size=-3}-С уважением-{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc

        if one_of_ten == 2:
            play sound "sounds/money.mp3"  
            $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-2}Дорогой Альбус,\nмы всем офисом благодарим Вас за новую главу! Позвольте передать вам {size=+4}[dgold] галеонов.{/size} и наше искреннее восхищение.{/size}\n\n\n{size=-3}-С уважением-{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc

        if one_of_ten == 3:
            play sound "sounds/money.mp3"  
            $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-2}Дорогой Альбус,\nна правах человека, ведущего связь с Вами, могу ли я узнать, будут ли Педреро и Хуанито вместе? Отправляю вам {size=+4}[dgold] галеонов{/size} и скромную надежду на ответ.{/size}\n\n\n{size=-3}-С уважением-{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            g9 "Хороший писатель никогда не раскрывает сюжетных поворотов!"
            m "..."
            m "Я и вправду сказал это?"
            hide screen letter
            hide screen bld1
            hide screen ctc

        if one_of_ten == 4:
            $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-2}Дорогой Альбус,\nновые главы вышли великолепными, особенно когда...{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc
            g1 "..."
            g1 "..."
            $ renpy.say(g1,tr("Черт, нет."))
            m "Я ничего не хочу об этом знать."
            play sound "sounds/money.mp3"  
            g9 "Ну, по крайней мере, в конверте лежали мои [dgold] галеонов."

        if one_of_ten == 5:
            $ letter_text = "{size=-7}ОТ:Джоданны Кроулинг\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-2}Дорогой Альбус,\nна правах главы Вашего фан-клуба, позвольте пригласить Вас на пенную вечеренку, адрес и время написаны на приглашении. Мы ждем вас с нетерпением!{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc
            g9 "Вечеринка, полная фанаток-извращенок? Впишите меня!"
            m "Ах, ну да... \"Будь хорошим джином, Джинни и сиди взаперти весь день, как осел.\""
            m "Черт."
            play sound "sounds/money.mp3"  
            g4 "Зачем мне [dgold] галеонов, если я не могу их как следует потратить?!"

        if one_of_ten == 6:
            $ letter_text = "{size=-7}ОТ:XXX\nКому: Альбусу Дамблдору\n\n\n{/size}{size=-2}У МЕНЯ БРАТ УМЕР ИЗ-ЗА ТАКИХ ИСТОРИЙ, ГОРИ В АДУ, ГРЯЗНЫЙ ИЗВРАЩЕНЕЦ!!!{/size}"
            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc
            m "..."
            g9 "О, монетки!"
            play sound "sounds/money.mp3"  
            "> Получено [dgold] галеонов"
            m "..."
            m "Смертные."














        hide screen points
        $ gold += dgold
        show screen points

        $ finished_report = 0

        if (hermi._incomePercent>0):
            $ dgold=dgold*hermi._incomePercent//100
            hide screen points
            $ gold-=dgold
            show screen points
            "> Согласно вашему соглашению с Гермионой [dgold] галеонов ([hermi._incomePercent]%%) перечисляются на ее счет"
        call screen main_menu_01



if day == 1:

    $ letter_text = "{size=-7}От: Гермионы Грейнджер\nКому: Профессору Дамблдору\n\n{/size}{size=-4}Я уверена, вы помните причину, по которой я написала вам последнее письмо, сэр.\n\nЯ прошу вас, пожалуйста, услышьте меня на этот раз. Эта несправедливость не может продолжаться...\nТолько не в наши дни и не в нашей школе.\n\nПожалуйста, примите меры.\n\n{size=-3}С уважением,\nГермиона Грейнджер{/size}"
    $ letters -= 1
    if letters <= 0:
        hide screen owl
        show screen owl_02

    label letter01_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Закончить чтение -":
            pass
        "- Продолжить чтение -":
            jump letter01_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    show screen bld1
    with d3
    m "Эмм..............................."
    m "Что?"
    m "................................."
    hide screen bld1
    with d3
    jump event_00




if letter_from_hermione_02:
    $ letter_from_hermione_02 = False

    $ letter_text = "{size=-7}От: Гермионы Грейнджер\nКому: Профессору Дамблдору\n\n{/size}{size=-4}Прошу прощения, что беспокою Вас снова профессор. Я просто хочу убедиться, что Вы отнесётесь к этой проблеме серьезно.\n\nПрошлой ночью еще одна однокурсница призналась мне... Я пообещала держать это в секрете, поэтому не могу вдаваться в подробности.\n\nВсе, что я могу сказать, это то, что вовлечен один из профессоров.\n\nПожалуйста примите меры в ближайшее время.\n\n{size=-3}С уважением,\nГермиона Грейнджер.{/size}"
    $ letters -= 1
    if letters <= 0:
        hide screen owl
        show screen owl_02

    label letter02_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Закончить чтение -":
            pass
        "- Продолжить чтение -":
            jump letter02_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_menu_01






if work_unlock:
    $ work_unlock = False
    $ letters -= 1
    $ work_unlock2 = True
    if letters <= 0:
        hide screen owl
        show screen owl_02
    $ letter_text = "{size=-7}От: Министерства Магии\nКому: Профессору Альбусу Дамблдору\n\n{/size}{size=-4}Дорогой профессор Дамблдор.\nМы напоминаем Вам, что только при предоставлении нам выполненого отчета, мы можем перечислить оплату на Ваше имя.\n\n{size=-3}С уважением,\nМинистерство Магии.{/size}"
    label letter_work:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Закончить чтение -":
            pass
        "- Продолжить чтение -":
            jump letter_work
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "Оплата? Хм..."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Теперь вы можете писать отчеты в Министерство магии, чтобы заработать золото..."
    hide screen blktone8
    with d3
    call screen main_menu_01


if total_report >= 10 and letter_from_ficbook_fun == False:
    $ letters -= 1
    $ letter_from_ficbook_fun = True
    if letters <= 0:
        hide screen owl
        show screen owl_02
    $ letter_text = "{size=-7}От: Жодана Кроулинг\nКому: Профессору Альбусу Дамблдору\n\n{/size}{size=-4}Дорогой Альбус Дамблдор.\nВ связи с открывшимся в Вас новым даром, Комитет Образования решил удвоить финансирование вашей отчетности.\nЖдем от вас больше захватывающих отчетов, в особенности про потомственного волшебника Педреро.\n\n{size=-3}С уважением,\nваша преданная фанатка и секретарь Комитета Образования,\nЖодана Кроулинг.{/size}"
    label letter_funletter:
    show screen bld1
    show screen letter
    show screen ctc
    with Dissolve(.3)
    pause
    menu:
        "- Закончить чтение -":
            pass
        "- Продолжить чтение -":
            jump letter_work
    hide screen letter
    hide screen bld1
    hide screen ctc
    with Dissolve(.3)
    m "..."
    m "Это определенно самый странный мир из увиденных мною."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Теперь вы получаете в два раза больше денег за... \nОтчеты."
    ">Оно того стоит?"
    m "Деньги не пахнут."
    hide screen blktone8
    with d3
    call screen main_menu_01



if day > 20 and nsp_pre_jobs_max >= 4 and nsp_pre_letter == 1:
    jump newsp_pre_letter

if nsp_newspaper_published_mail == True:
    jump newsp_letter

if nsp_letter_1 == 1:
    jump nsp_text_letter_1

if nsp_letter_2 == 1:
    jump nsp_text_letter_2

if nsp_letter_3 == 1:
    jump nsp_text_letter_3

if nsp_letter_4 == 1:
    jump nsp_text_letter_4

if nsp_letter_5 == 1:
    jump nsp_text_letter_5

if nsp_letter_6 == 1:
    jump nsp_text_letter_6

if nsp_letter_7 == 1:
    jump nsp_text_letter_7

if nsp_letter_8 == 1:
    jump nsp_text_letter_8

if nsp_letter_9 == 1:
    jump nsp_text_letter_9

if nsp_letter_10 == 1:
    jump nsp_text_letter_10

if nsp_letter_11 == 1:
    jump nsp_text_letter_11

if nsp_letter_12 == 1:
    jump nsp_text_letter_12

if nsp_letter_13 == 1:
    jump nsp_text_letter_13



label mail_02:

    $ evn=None
    python:
        for e in this.List:
            if "book_" in e.Name and e._status==-1:
                e.SetValue("status", 0)
                evn=e

    if evn!=None:
        $ package_is_here = False

        $ screens.ShowD3("gift", par1=evn._img).Say(tr(">Книга ") + tr(evn._caption) + tr(" была добавлена в Вашу коллекцию.")).HideD3("gift")







        call screen main_menu_01








    if itsOWL.Any():
        $ item=itsOWL()[0]
        $ _count=itsOWL.Count(item.Name)
        $ hero.Items.AddItem(item.Name, _count)
        $ itsOWL.Clear()
        $ package_is_here = False

        $ screens.ShowD3("gift", par1=item._img).Say(tr(">Добавлено к вашим вещам: ") + tr(item._caption) + ", " + str (_count) + tr("шт. ")).HideD3("gift")







        call screen main_menu_01


$ letters=0
call screen main_menu_01

label bigletter(_m1_15_mail__pages):
    $ letters -= 1
    if letters <= 0:
        $ screens.Hide("owl").Show("owl_02")

    $ _m1_15_mail__pageIndex=0
    label letterbig_newpage:
    $ screens.Show("letterbig", par1=_m1_15_mail__pages[_m1_15_mail__pageIndex])
    $ screens.Show("ctc", d3, "bld1").Pause()

    menu:
        "<<< Вернуться " if _m1_15_mail__pageIndex>0:
            $ _m1_15_mail__pageIndex-=1
            jump letterbig_newpage
        " Продолжить >>>" if _m1_15_mail__pageIndex<len(_m1_15_mail__pages)-1:
            $ _m1_15_mail__pageIndex+=1
            jump letterbig_newpage
        "- Завершить -":
            pass
    $ screens.Hide("letterbig", "ctc", d3, "bld1")
    return

label bigtext(_m1_15_mail__pages):

    $ _m1_15_mail__pageIndex=0
    label letterbig_newpage:
    $ screens.Show("letterbig", par1=_m1_15_mail__pages[_m1_15_mail__pageIndex])
    $ screens.Show("ctc", d3, "bld1").Pause()

    menu:
        "<<< Вернуться " if _m1_15_mail__pageIndex>0:
            $ _m1_15_mail__pageIndex-=1
            jump letterbig_newpage
        " Продолжить >>>" if _m1_15_mail__pageIndex<len(_m1_15_mail__pages)-1:
            $ _m1_15_mail__pageIndex+=1
            jump letterbig_newpage
        "- Завершить -":
            pass
    $ screens.Hide("letterbig", "ctc", d3, "bld1")
    return



label daphne_pre_04:
    call bigletter (["{size=-7}От: Оливии Гринграсс\nКому: Профессору Дамблдору\n\n{/size}"
    "{size=-4}Профессор Дамблдор!\n\nМы с мужем серьезно обеспокоены тем, что наша дочь не получает достаточно внимания в Хогвартсе и до сих пор не заняла в нем подобающего положения.\n\n "
    "Профессор Северус Снейп проинформировал нас, что вы, наконец-то, спохватились и вызвались давать ей частные уроки.\n\n Вы непозволительно долго шли к этому, профессор!\n\n "
    "Надеемся, что ваши запоздалые действия возымеют хоть какой-то эффект...{/size}\n\n ",
    "{size=-4}...Как вы знаете, в министерстве намечено очередное заседание по вопросам выделения фондов магическим учебным заведениям.\n\n "
    "Информируем вас, что если вами не будет достигнут достаточный прогресс, Дафна будет переведена в Дурмштанг - в академию, где умеют ценить настоящих чистокровных магов.\n\n "
    "Мы же в этом случае приложим все усилия, чтобы Хогвартс получил самое минимальное финансирование.{/size}\n\n "
    "{size=-3}Без особой надежды на ваш успех,\nОливия Гринграсс.{/size}"])

    $ hero(g4, "Великие пески!..",
        m,"Чувствуется почерк дружищи Снейпа, и я не уверен, что мне это нравится.//"
        "Подобающее положение?! Если она у меня займет подобающее ЕЙ положение, оно не слишком понравится ее мамочке!//"
        "Что теперь? Все время трястись, чтобы не сболтнуть лишнего, и она не настучала родителям...//"
        "Чему ее учить, если я вообще ничего о ней не знаю?! И главное: как ее заставить держать язык за зубами?")

    $ wtevent.Finalize()

    call screen main_menu_01


label daphne_pre_06:
    $ music("Daphne Privacy")

    call bigletter (["{size=-7}От: Северуса Снейпа\nКому: Профессору Дамблдору\n\n{/size}"
    "{size=+2}Выписка из досье на Дафну Гринграсс\n\n{/size}"
    "{size=-4}Рост: 5' 8\", Вес: 53 kg, Размер груди: 34В\n\n"
    "Ориентация: Предположительно гетеро.\n\n"
    "Девственница: Нет доказательств обратного.\n\n"
    "Мастурбация: Да? (доказательства косвенные: однокурсница, случайно оказавшаяся рядом, слышала ее стоны из кабинки в душе)\n\n"
    "Просмотр порно: Да? (доказательства косвенные: оставленный порно-журнал исчез из гостиной Слизерина, в гостиную кроме Гринграсс никто не входил)\n\n"
    "Подглядывание: Да? (доказательства косвенные: была застигнута около отверстия, которое однокурсницы проделали в мужскую душевую, но поймана за подглядыванием не была){/size}",
    "{size=-4}Убеждения и опасения:\n\n"
    "* комплексует, что ее грудь слишком мала\n"
    "* считает, что спать можно только с чистокровным высоким, мужественным и т.п.\n"
    "* боится, что не сможет удовлетворить чистокровного высокого, мужественного и т.п.\n"
    "* комплексует по поводу своего маленького (отсутствующего?) сексуального опыта\n\n"
    "Девиации: Не обнаружены{/size}\n\n "
    "{size=-3}Успехов, мой друг!\nСеверус Снейп.{/size}\n\n"
    "{size=-4}P.S. Мисс Гринграсс получила напутственное письмо от родителей. Думаю, будет правильно, мой друг, если не ты станешь вызывать ее, а она сама придет к тебе на первое занятие.{/size}"])

    $ hero(m,"Ну и досье. Он что диссертацию по ней собирался писать? И через слово \"нет доказательств\", \"не обнаружено\", \"доказательства косвенные\"...//"
        "Неудивительно, что у него ничего с ней не вышло...// Хм, как бы мне подготовиться к ее приходу?")

    call music_block
    $ wtevent.Finalize()

    call screen main_menu_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
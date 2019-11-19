label jerk_off:
    $ cum_on_floor = False
    $ cum_under_desk = False
    $ jerk_zorder = 5
    $ cum_on_panties = False
    $ jerking_off_to_jasmine = False
    $ jerking_off_to_lara = False
    m "Хм...кем же мы займемся сегодня?"
    menu:
        "- Принцесса Жасмин -":
            m "Да, принцесса... Эта грязная шлюха!"
            $ jerking_off_to_jasmine = True
            pass
        "- Лара Крофт -":
            $ jerking_off_to_lara = True
            pass
        "- Передумал -":
            jump desk

    m "Куда бы кончить?"
    label how_to_finish:
        menu:
            "- Под стол -":
                $ cum_under_desk = True
                pass
            "- На пол -":
                $ cum_on_floor = True
                pass
            "{color=#858585}- (ЗАБЛОКИРОВАННО) -{/color}" if not request_03:
                ">Вам не доступен этот выбор."
                jump how_to_finish
            "- Трусики Гермионы -" if request_03:
                $ cum_on_panties = True
                pass
            "- Отмена -":
                jump jerk_off



    with d5
    ">Вы решили вздрочнуть, вспоминая былые времена..."
    show screen genie_jerking_off
    with d8
    if jerking_off_to_jasmine:
        ">Вы фантазируете о принцессе Жасмин..."
        $ checked = 'jas'
        g9 "Ух...да, та еще шлюшка..."
        jump random_pics
    if jerking_off_to_lara:
        ">Вы фантазируете о Ларе Крофт..."
        $ checked = 'lara'
        g9 "О да... эта соска была великолепна..."

        with d8
        jump random_pics

    label finish_cum:
        ">Вы вот-вот кончите..."
        if one_out_of_three == 1:
            g4 "Архг! Шлюха!"
        elif one_out_of_three == 2:
            g4 "ДА! ПОЛУЧАЙ ПОТАСКУХА! АРРХ!"
        elif one_out_of_three == 2:
            g4 "О да! Вау... Давненько такого не было."

        show screen genie_jerking_sperm
        if cum_on_floor:
            ">Вы обильно кончаете на пол."
            g4 "Придется здесь прибраться..."

            if ((wather_generator >= 31 and wather_generator <= 40) or (wather_generator >= 51 and wather_generator <= 60)) and not daytime:
                hide screen genie_jerking_sperm
                $ jerking_off_to_jasmine = False
                $ jerking_off_to_lara = False
                $ cum_under_desk = False
                $ cum_on_panties = False

                jump pnx_call


        if cum_under_desk:
            ">Вы кончили под стол."
        if cum_on_panties:
            $ have_cum_soaced_panties = True
            ">Вы кончили на трусики Гермионы, а затем протерли ими пол..."
            ">Вы получили предмет: \"Трусики пропитанные спермой\"."
        hide screen genie_jerking_sperm
        g7 "Да уж, было время. Интересно, получится ли вернуть старые добрые времена?"
        g7 "С удовольствие снова натянул бы эту потаскуху... как ее там... Лара..."
        g4 "Да и принцесса еще та соска. Как вспомню ее влажный ротик. Ух..."
        g4 "Ладно, стоит вернуться к текущим делам."

    $ jerking_off_to_jasmine = False
    $ jerking_off_to_lara = False
    $ cum_under_desk = False
    $ cum_on_panties = False

    if daytime:
        jump night_start
    else:
        jump day_start

    label random_pics:
        $ list_of_files_jas = 10
        $ list_of_files_lara = 100

        if checked == 'jas':
            $ directory_of_images = '03_hp/22_dreams/jas'
            $ list_of_files = list_of_files_jas
        elif checked == 'lara':
            $ list_of_files = list_of_files_lara
            $ directory_of_images = '03_hp/22_dreams/lara'
        else:
            $ list_of_files = list_of_files_jas
            $ directory_of_images = '03_hp/22_dreams/jas'


        python:
            x = 0
            list_of_numbers = []
            while x < 10:
                random_int = renpy.random.randint(1, list_of_files)
                list_of_numbers.append(random_int)
                x = x+1
            list_of_numbers = set(list_of_numbers)

            for i in list_of_numbers:
                jerk_image = directory_of_images + '/%s.png' % i
                renpy.show_screen("jerkingimage")
                renpy.pause()
                renpy.hide_screen("jerkingimage")


        $ directory_of_images = False;
        $ list_of_files = False;
        jump finish_cum
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
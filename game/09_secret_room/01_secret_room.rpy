label sroom_main:

    scene title2
    with flashbb

    call Achievement_constants

    python:

        global achieve

        achieve = Achievement()
        achieve.LoadPersistent()

    dev "Добро пожаловать Тайную Комнату. Здесь вы можете изучить список своих игровых достижений и насладиться некоторыми бонусами."


    label sroom_main2:
    menu:
        "- Посмотреть список достижений -":



            label sroom_achlist:

                $ ach_hermi_points = 0
                python:
                    ach_hermi_points = achieve.GetSumPoints (const_ACH_PERS_HERMIONA)

                menu:
                    ach "Очки Гермионы : {color=00FF00}[ach_hermi_points]G{/color}"
                    "- Концовки -":
                        label sroom_achlist2:
                            menu:
                                ach "Очки Гермионы : {color=00FF00}[ach_hermi_points]G{/color}"

                                "{color=#858585}- Скрыто -{/color}" if not achieve.IsEnding(1):
                                    ach "Данное достижение еще не достигнуто. А ведь оно доступно где-то в игре... Терпеливо ждет своего часа..."
                                    jump sroom_achlist2

                                "Концовка Гермионы 01: Ваша Шлюха. {color=00FF00}+100G{/color}" if achieve.IsEnding(1):
                                    ach "В результате обучения Гермиона стала Вашей персональной шлюхой. Приятно осознавать это."
                                    jump sroom_achlist2

                                "{color=#858585}- Скрыто -{/color}" if not achieve.IsEnding(2):
                                    ach "Данное достижение еще не достигнуто. А ведь оно доступно где-то в игре... Терпеливо ждет своего часа..."
                                    jump sroom_achlist2

                                "Концовка Гермионы 02: Публичная Шлюха. {color=00FF00}+100G{/color}" if achieve.IsEnding(2):
                                    ach "В результате обучения Гермиона стала школьной шлюхой Хогвартса. Под вашим чутким руководством, конечно."
                                    jump sroom_achlist2

                                "{color=#858585}- Скрыто -{/color}" if not achieve.IsEnding(3):
                                    ach "Данное достижение еще не достигнуто. А ведь оно доступно где-то в игре... Терпеливо ждет своего часа..."
                                    jump sroom_achlist2

                                "Концовка Гермионы 03: Сильная девушка. {color=00FF00}+100G{/color}" if achieve.IsEnding(3):
                                    ach "В результате обучения Гермиона стала независимой и волевой... правильно, шлюхой !"
                                    jump sroom_achlist2
                                "Назад":

                                    call sroom_achlist
                    "- Одежда Гермионы -":

                        label sroom_achlist3:

                            menu:
                                ach "Очки Гермионы : {color=00FF00}[ach_hermi_points]G{/color}"
                                "- Кофты -":

                                    label sroom_achlist11:
                                        python:
                                            achieve.ShowList("sroom_achlist3",None,const_ACH_BLOCK_HERMIONA_SHIRT)

                                            renpy.say( ach, achieve.DispDescription())

                                        call sroom_achlist11
                                "- Юбки -":

                                    label sroom_achlist12:
                                        python:
                                            achieve.ShowList("sroom_achlist3",None,const_ACH_BLOCK_HERMIONA_SKIRT)

                                            renpy.say( ach, achieve.DispDescription())

                                        call sroom_achlist12
                                "- Прочее -":

                                    label sroom_achlist13:
                                        python:
                                            achieve.ShowList("sroom_achlist3",None,const_ACH_BLOCK_HERMIONA_OTH)

                                            renpy.say( ach, achieve.DispDescription())

                                        call sroom_achlist13
                                "- Особое -":

                                    label sroom_achlist14:
                                        python:
                                            achieve.ShowList("sroom_achlist3",None,const_ACH_BLOCK_HERMIONA_SPECIAL)

                                            renpy.say( ach, achieve.DispDescription())

                                        call sroom_achlist14
                                "- Назад -":

                                    jump sroom_achlist
                    "- Назад -":

                        jump sroom_main2
        "- Отмена -":


            return

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
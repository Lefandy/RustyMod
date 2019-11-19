



label menu_dahre_newsp:
    $ choose = RunMenu()
    python:
        for e in this.List:
            if e.GetValue("block")==_block: 
                choose.AddItem("- Для газет: "+e._caption+" - "+("{image=check_08.png}" if e._status>-2 else "{image=check_07.png}"), 
                    "menu_dahre_newsp_2", e.Name)

    $ choose.Show("the_oddities")

    label menu_dahre_newsp_2:
        $ the_gift = wtevent._img
        show screen gift
        with d3
        $ renpy.say(dahr,tr(wtevent._caption) + ". " + tr(wtevent._description) + "\n")
        if wtevent._status>-2:
            call do_have_book
            jump the_oddities
        if nsp_newspaper_menu < 4 and wtevent.Name <> "nsp_newsp_book_pre":
            "> Эта книга вас не интересует."
            hide screen gift
            jump expression _label
        menu:
            "- Купить книгу за [wtevent._price] галлеонов -":
                if gold >= wtevent._price:
                    $ gold -= wtevent._price
                    $ order_placed = True
                    $ wtevent.IncValue("status",1)

                    call thx_4_shoping
                    jump desk
                else:
                    call no_gold
                    jump expression _label
            "- Ничего -":
                hide screen gift
                jump expression _label

label menu_dahre_upd:
    $ choose = RunMenu()
    python:
        for e in this.List:
            if e.GetValue("block")==_block: 
                choose.AddItem("- Для газет: "+e._caption+" - "+("{image=check_08.png}" if e._status>-2 else "{image=check_07.png}"), 
                    "menu_dahre_upd_2", e.Name)

    $ choose.Show("the_oddities")

    label menu_dahre_upd_2:
        $ the_gift = wtevent._img
        show screen gift
        with d3
        $ renpy.say(dahr,tr(wtevent._caption) + ". " + tr(wtevent._description) + "\n")
        if wtevent._status>-2:
            call do_have_book
            jump the_oddities
        menu:
            "- Купить за [wtevent._price] галлеонов -":
                if gold >= wtevent._price:
                    $ gold -= wtevent._price
                    $ order_placed = True
                    $ wtevent.IncValue("status",1)

                    call thx_4_shoping
                    jump desk
                else:
                    call no_gold
                    jump expression _label
            "- Ничего -":
                hide screen gift
                jump expression _label

label nsp_sphere_dahre:
    $ price = 0
    $ caption = ""
    menu:
        "Уровень сапфира [nsp_genie_sphere_sapphire_level]\nУровень рубина [nsp_genie_sphere_ruby_level]\nУровень алмаза [nsp_genie_sphere_diamond_level]"

        "- Купить Сапфир (моментальная доставка совой-молнией) -" if nsp_genie_sphere_sapphire_level < 5:
            menu:
                "Уровень сапфира [nsp_genie_sphere_sapphire_level]\nУровень рубина [nsp_genie_sphere_ruby_level]\nУровень алмаза [nsp_genie_sphere_diamond_level]"

                "Купить осколок сапфира (1 уровень)" if nsp_genie_sphere_sapphire_level < 1:
                    $ the_gift = "08_newspaper_scenario/sphere/Saphire1.png"
                    show screen gift

                    menu:
                        "Осколок сапфира."
                        "- Купить за 100 галлеонов -":
                            if gold >= 100:
                                $ gold -= 100
                                $ nsp_genie_sphere_sapphire_level = 1
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился осколок сапфира."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre

                "Купить маленький сапфир (2 уровень)" if nsp_genie_sphere_sapphire_level < 2:
                    $ the_gift = "08_newspaper_scenario/sphere/Saphire2.png"
                    show screen gift

                    menu:
                        "Маленький сапфир."
                        "- Купить за 200 галлеонов -":
                            if gold >= 200:
                                $ gold -= 200
                                $ nsp_genie_sphere_sapphire_level = 2
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился маленький сапфир."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить нормальный сапфир (3 уровень)" if nsp_genie_sphere_sapphire_level < 3:
                    $ the_gift = "08_newspaper_scenario/sphere/Saphire3.png"
                    show screen gift

                    menu:
                        "Нормальный сапфир."
                        "- Купить за 400 галлеонов -":
                            if gold >= 400:
                                $ gold -= 400
                                $ nsp_genie_sphere_sapphire_level = 3
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился сапфир."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить крупный сапфир (4 уровень)" if nsp_genie_sphere_sapphire_level < 4:
                    $ the_gift = "08_newspaper_scenario/sphere/Saphire4.png"
                    show screen gift

                    menu:
                        "Крупный сапфир."
                        "- Купить за 700 галлеонов -":
                            if gold >= 700:
                                $ gold -= 700
                                $ nsp_genie_sphere_sapphire_level = 4
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился крупный сапфир."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить совершенный сапфир (5 уровень)" if nsp_genie_sphere_sapphire_level < 5:
                    $ the_gift = "08_newspaper_scenario/sphere/Saphire5.png"
                    show screen gift

                    menu:
                        "Совершенный сапфир."
                        "- Купить за 1000 галлеонов -":
                            if gold >= 1000:
                                $ gold -= 1000
                                $ nsp_genie_sphere_sapphire_level = 5
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился совершенный сапфир."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre
                "- Ничего -":


                    jump nsp_sphere_dahre



        "- Купить Рубин (моментальная доставка совой-молнией) -" if nsp_genie_sphere_ruby_level < 5:
            menu:
                "Уровень сапфира [nsp_genie_sphere_sapphire_level]\nУровень рубина [nsp_genie_sphere_ruby_level]\nУровень алмаза [nsp_genie_sphere_diamond_level]"

                "Купить осколок рубина (1 уровень)" if nsp_genie_sphere_ruby_level < 1:
                    $ the_gift = "08_newspaper_scenario/sphere/Ruby1.png"
                    show screen gift

                    menu:
                        "Осколок рубина."
                        "- Купить за 200 галлеонов -":
                            if gold >= 200:
                                $ gold -= 200
                                $ nsp_genie_sphere_ruby_level = 1
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился осколок рубина."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre

                "Купить маленький рубин (2 уровень)" if nsp_genie_sphere_ruby_level < 2:
                    $ the_gift = "08_newspaper_scenario/sphere/Ruby2.png"
                    show screen gift

                    menu:
                        "Маленький рубин."
                        "- Купить за 600 галлеонов -":
                            if gold >= 600:
                                $ gold -= 600
                                $ nsp_genie_sphere_ruby_level = 2
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился маленький рубин."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить нормальный рубин (3 уровень)" if nsp_genie_sphere_ruby_level < 3:
                    $ the_gift = "08_newspaper_scenario/sphere/Ruby3.png"
                    show screen gift

                    menu:
                        "Нормальный рубин."
                        "- Купить за 1500 галлеонов -":
                            if gold >= 1500:
                                $ gold -= 1500
                                $ nsp_genie_sphere_ruby_level = 3
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился рубин."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить крупный рубин (4 уровень)" if nsp_genie_sphere_ruby_level < 4:
                    $ the_gift = "08_newspaper_scenario/sphere/Ruby4.png"
                    show screen gift

                    menu:
                        "Крупный рубин."
                        "- Купить за 5000 галлеонов -":
                            if gold >= 5000:
                                $ gold -= 5000
                                $ nsp_genie_sphere_ruby_level = 4
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился крупный рубин."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить совершенный рубин (5 уровень)" if nsp_genie_sphere_ruby_level < 5:
                    $ the_gift = "08_newspaper_scenario/sphere/Ruby5.png"
                    show screen gift

                    menu:
                        "Совершенный рубин."
                        "- Купить за 20000 галлеонов -":
                            if gold >= 20000:
                                $ gold -= 20000
                                $ nsp_genie_sphere_ruby_level = 5
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился совершенный рубин."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre
                "- Ничего -":


                    jump nsp_sphere_dahre



        "- Купить Алмаз (моментальная доставка совой-молнией) -" if nsp_genie_sphere_diamond_level < 5:
            menu:
                "Уровень сапфира [nsp_genie_sphere_sapphire_level]\nУровень рубина [nsp_genie_sphere_ruby_level]\nУровень алмаза [nsp_genie_sphere_diamond_level]"

                "Купить осколок алмаза (1 уровень)" if nsp_genie_sphere_diamond_level < 1:
                    $ the_gift = "08_newspaper_scenario/sphere/Diamond1.png"
                    show screen gift

                    menu:
                        "Осколок алмаза."
                        "- Купить за 500 галлеонов -":
                            if gold >= 500:
                                $ gold -= 500
                                $ nsp_genie_sphere_diamond_level = 1
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился осколок алмаза."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre

                "Купить маленький алмаз (2 уровень)" if nsp_genie_sphere_diamond_level < 2:
                    $ the_gift = "08_newspaper_scenario/sphere/Diamond2.png"
                    show screen gift

                    menu:
                        "Маленький алмаз."
                        "- Купить за 1500 галлеонов -":
                            if gold >= 1500:
                                $ gold -= 1500
                                $ nsp_genie_sphere_diamond_level = 2
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился маленький алмаз."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить нормальный алмаз (3 уровень)" if nsp_genie_sphere_diamond_level < 3:
                    $ the_gift = "08_newspaper_scenario/sphere/Diamond3.png"
                    show screen gift

                    menu:
                        "Нормальный алмаз."
                        "- Купить за 5000 галлеонов -":
                            if gold >= 5000:
                                $ gold -= 5000
                                $ nsp_genie_sphere_diamond_level = 3
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился алмаз."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить крупный алмаз (4 уровень)" if nsp_genie_sphere_diamond_level < 4:
                    $ the_gift = "08_newspaper_scenario/sphere/Diamond4.png"
                    show screen gift

                    menu:
                        "Крупный алмаз."
                        "- Купить за 15000 галлеонов -":
                            if gold >= 15000:
                                $ gold -= 15000
                                $ nsp_genie_sphere_diamond_level = 4
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился крупный алмаз."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre


                "Купить совершенный алмаз (5 уровень)" if nsp_genie_sphere_diamond_level < 5:
                    $ the_gift = "08_newspaper_scenario/sphere/Diamond5.png"
                    show screen gift

                    menu:
                        "Совершенный алмаз."
                        "- Купить за 40000 галлеонов -":
                            if gold >= 40000:
                                $ gold -= 40000
                                $ nsp_genie_sphere_diamond_level = 5
                                call nsp_genie_sphere_level_check
                                ">За окном мелькнула стремительная тень и по столу покатился совершенный алмаз."
                                hide screen gift
                                jump desk
                            else:
                                call no_gold
                                jump nsp_sphere_dahre
                        "- Ничего -":
                            hide screen gift
                            jump nsp_sphere_dahre
                "- Ничего -":


                    jump nsp_sphere_dahre
        "- Ничего -":


            jump the_oddities
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
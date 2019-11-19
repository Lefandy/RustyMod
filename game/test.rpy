label own_test:
    $ cum_on_floor = False
    $ cum_under_desk = False
    $ jerk_zorder = 5
    $ cum_on_panties = False
    $ jerking_off_to_jasmine = False
    $ jerking_off_to_lara = False
    m "Это тестовый текст!"

    $ menu_x = 0.2
    $ tt_xpos=350
    $ tt_ypos=0
    # $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    # Снейп на сцене (ниже)
    show screen snape_02
    show screen bld1
    # Снейп во время диалога
    show screen snape_main

    with Dissolve(.3)

    m "Это ущу тестовый текст!"
    gw "Да, что такое?"
    # hide screen snape_02

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

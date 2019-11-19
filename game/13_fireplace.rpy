label fireplace:


    if not fireplace_examined:
        $ fireplace_examined = True
        hide screen genie
        $ tt_xpos=350
        $ tt_ypos=90
        show screen genie_stands
        show screen chair_02 
        show screen desk
        with Dissolve(0.5)
        m "Хм... Выглядит как обычный камин..."
        show screen genie
        hide screen genie_stands
        hide screen chair_02 
        hide screen desk
        with Dissolve(0.5)
        jump day_main_menu









    if not fire_in_fireplace and not day == 1:


        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 
        $ fire_in_fireplace = True
        show screen fireplace_fire
        jump day_main_menu

    if fire_in_fireplace:
        $ fire_in_fireplace = False
        stop bg_sounds 
        hide screen fireplace_fire
        jump day_main_menu



    jump day_main_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
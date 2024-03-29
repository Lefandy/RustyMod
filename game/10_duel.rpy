label duel:


    $ d_flag_01 = False
    $ d_flag_02 = False

    $ genie_hp = 1000
    $ snape_hp = 2000



    $ blocking = False
    $ snape_blocking = False
    $ pentogram = False




    $ phoenix_is_feed = False

    stop bg_sounds 
    stop weather 

    hide screen notes 
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_02
    hide screen candlefire_01 
    hide screen candlefire_02 
    hide screen lightening 
    hide screen cloud_night_01 
    hide screen cloud_night_02 
    hide screen cloud_night_03 

    hide screen room_night 


    hide screen door
    hide screen cupboard
    hide screen chair
    hide screen fireplace
    hide screen phoenix
    hide screen candle_01
    hide screen candle_02
    hide screen genie
    hide screen owl
    hide screen owl_02
    hide screen points
    hide screen ctc


    show expression "03_hp/01_bg/01_main_room_02.png"
    show expression "03_hp/05_props/01_door.png" at Position(xpos=758, ypos=315, xanchor="center", yanchor="center")
    show expression "03_hp/05_props/02_cupboard_00.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
    show expression "03_hp/05_props/04_chair.png" at Position(xpos=653, ypos=300, xanchor="center", yanchor="center")
    show expression "03_hp/05_props/03_fireplace.png" at Position(xpos=553, ypos=277, xanchor="center", yanchor="center")

    show expression "03_hp/05_props/06_phoenix.png" at Position(xpos=400, ypos=225, xanchor="center", yanchor="center")
    show expression "03_hp/05_props/07_candle.png" at Position(xpos=693, ypos=225, xanchor="center", yanchor="center")
    show expression "03_hp/05_props/08_candle.png" at Position(xpos=210, ypos=160, xanchor="center", yanchor="center")

    show expression "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    show screen candlefire_01 
    show screen candlefire_02 

    hide screen snape_defends
    hide screen blkfade

    if skip_duel == True:
        jump snape_lost





    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")

    hide screen end_u_1
    with fade


    m "Это глупо...ты мне не ровня..."
    $ sna_head_state = 1
    sna_head_main "Забавно..."
    m "{size=-4}(Вообще-то, мой человеческий сосуд довольно слаб...){/size}"
    m "{size=-4}(Но, все равно, я должен быть сильнее любого \"человеческого\" мага...){/size}"
    sna_head_main "Да начнется битва!"
    hide screen bld1
    show screen hp_bar
    with d5








label duel_main:
    if genie_hp <= 300 and not d_flag_01:
        $ d_flag_01 = True
        sna_head_main "Уже готов сдаться?"
        g4 "Пф..."

    if snape_hp <= 400 and not d_flag_02:
        $ d_flag_02 = True
        g4 "{size=-4}(Он слабеет, я это чувствую!){/size}"
        sna_head_main "*Задыхается*"

    call screen duel_buttons




    menu:
        "- Атака -":
            $ blocking = False
            if snape_blocking:
                $ snape_blocking = False
                pause 1
                jump snape_defends
            else:
                jump genie_attack
        "- Защита -":
            $ blocking = True
            show ch_gen guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1
            jump snapes_turn
        "- Зелье (x[potions])-":
            if potions >= 1:
                jump potion
            else:
                m "Черт! У меня нет целебных зелий!"
                jump duel_main



label snapes_turn:
    if pentogram:
        $ pentogram = False
        hide ch_sna
        hide pentogram
        show hand at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
        $ renpy.play('sounds/attack_snape3.ogg')
        pause 1.5
        hide hand
        hide ch_gen
        $ renpy.play('sounds/attack_snape4.ogg')
        if blocking:
            $ blocking = False
            show hand_guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1.8
            hide hand_guard
            show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            hide screen minus_50_genie
            show screen minus_50_genie
            $ genie_hp -= 50
            if genie_hp < 50:
                jump genie_lost

            show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            show ch_gen duel_01 behind smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            jump duel_main
        else:


            show hand_genie at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1.3
            hide hand_genie
            show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            hide screen minus_400_genie
            show screen minus_400_genie
            $ genie_hp -= 400
            if genie_hp < 50:
                jump genie_lost
            show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            jump duel_main
    else:


        $ snape_blocking = False

        $ snape_decides = renpy.random.randint(1, 3)

        if snape_decides == 1:
            if blocking:
                $ blocking = False
                jump snape_attack_guard
            else:
                jump snape_attack
        elif snape_decides == 2:
            $ snape_blocking = True
            show ch_sna defend at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1
            jump duel_main

        elif snape_decides == 3:
            $ pentogram = True
            hide ch_sna
            show expression "03_hp/04_duel/snape_casting_01.png" at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            $ renpy.play('sounds/attack_snape2.ogg')
            pause.8
            show pentogram at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1
            hide expression "03_hp/04_duel/snape_casting_01.png"
            show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")

            jump duel_main




label snape_attack:
    hide ch_sna
    hide ch_gen
    show snape_attack at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    with Dissolve(.1)
    $ renpy.play('sounds/attack_snape.ogg')
    pause 0.45
    hide snape_attack at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    $ genie_hp -= 100
    if genie_hp < 50:
        jump genie_lost
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    with Dissolve(.1)
    jump duel_main



label snape_attack_guard:
    hide ch_sna
    hide ch_gen
    show snape_attack_guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    with Dissolve(.1)
    $ renpy.play('sounds/attack_snape.ogg')
    pause 0.5
    hide screen minus_0_genie
    show screen minus_0_genie
    hide snape_attack_guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_gen guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    pause 1


    with Dissolve(.1)

    jump duel_main




label snape_defends:
    hide ch_sna
    hide ch_gen
    $ renpy.play('sounds/magic4.ogg')
    show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show snape_defend behind smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    with Dissolve(.1)
    pause 2.3
    hide screen minus_0
    show screen minus_0
    hide snape_defend at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_gen barb at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    pause 1

    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    pause 1
    jump snapes_turn



label genie_attack:
    hide ch_sna
    hide ch_gen

    $ renpy.play('sounds/magic4.ogg')
    show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show genie_attack behind smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    with Dissolve(.1)

    pause 1
    $ renpy.play('sounds/attack_axe.mp3')

    pause 1.8



    if pentogram:
        hide screen minus_300
        show screen minus_300
        $ snape_hp -= 300
    else:
        hide screen minus_100
        show screen minus_100
        $ snape_hp -= 100
    pause 1
    if snape_hp < 50:
        jump snape_lost
    show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    hide genie_attack at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_gen barb at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    pause 1
    jump snapes_turn




label potion:
    pause.5
    hide heal_02
    show heal_02 at Position(xpos=360, ypos=330, xanchor="center", yanchor="center")
    $ renpy.play('sounds/attack_heal.ogg')
    pause 1



    hide screen plus_300
    show screen plus_300
    pause 1
    $ potions -=1
    $ genie_hp += 300
    if genie_hp >= 1000:
        $ genie_hp = 1000
    pause.5
    hide screen plus_300
    jump snapes_turn






label main_attack:
    $ blocking = False
    if snape_blocking:
        $ snape_blocking = False
        pause 1
        jump snape_defends
    else:
        jump genie_attack

label main_block:
    $ blocking = True
    $ renpy.play('sounds/magic4.ogg')
    show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_gen guard behind smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    pause 1
    jump snapes_turn

label main_potion:
    if potions >= 1:
        jump potion
    else:
        m "Черт! У меня нет целебных зелий!"
        jump duel_main








init -1:



    screen hp_bar:
        if genie_hp == 1000:
            add "03_hp/04_duel/hp_bar_02.png"
        if genie_hp == 950:
            add "03_hp/04_duel/hp_bar_02.png" xpos -15 ypos 0
        if genie_hp == 900:
            add "03_hp/04_duel/hp_bar_02.png" xpos -30 ypos 0
        if genie_hp == 850:
            add "03_hp/04_duel/hp_bar_02.png" xpos -45 ypos 0
        if genie_hp == 800:
            add "03_hp/04_duel/hp_bar_02.png" xpos -60 ypos 0
        if genie_hp == 750:
            add "03_hp/04_duel/hp_bar_02.png" xpos -75 ypos 0
        if genie_hp == 700:
            add "03_hp/04_duel/hp_bar_02.png" xpos -90 ypos 0
        if genie_hp == 650:
            add "03_hp/04_duel/hp_bar_02.png" xpos -105 ypos 0
        if genie_hp == 600:
            add "03_hp/04_duel/hp_bar_02.png" xpos -120 ypos 0
        if genie_hp == 550:
            add "03_hp/04_duel/hp_bar_02.png" xpos -135 ypos 0
        if genie_hp == 500:
            add "03_hp/04_duel/hp_bar_02.png" xpos -150 ypos 0
        if genie_hp == 450:
            add "03_hp/04_duel/hp_bar_02.png" xpos -165 ypos 0
        if genie_hp == 400:
            add "03_hp/04_duel/hp_bar_02.png" xpos -180 ypos 0
        if genie_hp == 350:
            add "03_hp/04_duel/hp_bar_02.png" xpos -195 ypos 0
        if genie_hp == 300:
            add "03_hp/04_duel/hp_bar_02.png" xpos -210 ypos 0
        if genie_hp == 250:
            add "03_hp/04_duel/hp_bar_02.png" xpos -225 ypos 0
        if genie_hp == 200:
            add "03_hp/04_duel/hp_bar_02.png" xpos -240 ypos 0
        if genie_hp == 150:
            add "03_hp/04_duel/hp_bar_02.png" xpos -255 ypos 0
        if genie_hp == 100:
            add "03_hp/04_duel/hp_bar_02.png" xpos -270 ypos 0
        if genie_hp == 50:
            add "03_hp/04_duel/hp_bar_02.png" xpos -285 ypos 0
        if genie_hp < 50:
            add "03_hp/04_duel/hp_bar_02.png" xpos -300 ypos 0
        add "03_hp/04_duel/hp_bar.png"
        if _preferences.language == "english":
            add "03_hp/04_duel/hp_bar_05_en.png"
        else:
            add "03_hp/04_duel/hp_bar_05.png"

        add "03_hp/04_duel/hp_bar_11.png"
        if snape_hp == 2000:
            add "03_hp/04_duel/hp_bar_12.png"
        if snape_hp == 1900:
            add "03_hp/04_duel/hp_bar_12.png" xpos 35 ypos 0
        if snape_hp == 1800:
            add "03_hp/04_duel/hp_bar_12.png" xpos 70 ypos 0
        if snape_hp == 1700:
            add "03_hp/04_duel/hp_bar_12.png" xpos 105 ypos 0
        if snape_hp == 1600:
            add "03_hp/04_duel/hp_bar_12.png" xpos 140 ypos 0
        if snape_hp == 1500:
            add "03_hp/04_duel/hp_bar_12.png" xpos 175 ypos 0
        if snape_hp == 1400:
            add "03_hp/04_duel/hp_bar_12.png" xpos 205 ypos 0
        if snape_hp == 1300:
            add "03_hp/04_duel/hp_bar_12.png" xpos 240 ypos 0
        if snape_hp == 1200:
            add "03_hp/04_duel/hp_bar_12.png" xpos 275 ypos 0
        if snape_hp == 1100:
            add "03_hp/04_duel/hp_bar_12.png" xpos 305 ypos 0
        if snape_hp == 1000:
            add "03_hp/04_duel/hp_bar_12.png" xpos 340 ypos 0
        if snape_hp == 900:
            add "03_hp/04_duel/hp_bar_12.png" xpos 375 ypos 0
        if snape_hp == 800:
            add "03_hp/04_duel/hp_bar_12.png" xpos 405 ypos 0
        if snape_hp == 700:
            add "03_hp/04_duel/hp_bar_12.png" xpos 440 ypos 0
        if snape_hp == 600:
            add "03_hp/04_duel/hp_bar_12.png" xpos 475 ypos 0
        if snape_hp == 500:
            add "03_hp/04_duel/hp_bar_12.png" xpos 505 ypos 0
        if snape_hp == 400:
            add "03_hp/04_duel/hp_bar_12.png" xpos 545 ypos 0
        if snape_hp == 300:
            add "03_hp/04_duel/hp_bar_12.png" xpos 585 ypos 0
        if snape_hp == 200:
            add "03_hp/04_duel/hp_bar_12.png" xpos 630 ypos 0
        if snape_hp == 100:
            add "03_hp/04_duel/hp_bar_12.png" xpos 670 ypos 0
        if snape_hp < 100:
            add "03_hp/04_duel/hp_bar_12.png" xpos 700 ypos 0



        add "03_hp/04_duel/hp_bar_10.png"





    screen duel_buttons:
        imagebutton:
            focus_mask True
            if _preferences.language == "english":
                idle "03_hp/04_duel/hp_bar_03_en.png"
                hover "03_hp/04_duel/hp_bar_04_en.png"
            else:
                idle "03_hp/04_duel/hp_bar_03.png"
                hover "03_hp/04_duel/hp_bar_04.png"
            action [Jump("main_attack")]
        imagebutton:
            focus_mask True
            if _preferences.language == "english":
                idle "03_hp/04_duel/hp_bar_07_en.png"
                hover "03_hp/04_duel/hp_bar_06_en.png"
            else:
                idle "03_hp/04_duel/hp_bar_07.png"
                hover "03_hp/04_duel/hp_bar_06.png"
            action [Jump("main_block")]
        imagebutton:
            focus_mask True
            if _preferences.language == "english":
                idle "03_hp/04_duel/hp_bar_09_en.png"
                hover "03_hp/04_duel/hp_bar_08_en.png"
            else:
                idle "03_hp/04_duel/hp_bar_09.png"
                hover "03_hp/04_duel/hp_bar_08.png"
            action [Jump("main_potion")]




label snape_lost:
    play music "music/Final Fantasy VII - Victory Fanfare.mp3" fadein 1 fadeout 4
    hide genie_attack at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    hide pentogram
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")

    show expression "03_hp/04_duel/snape.png" at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    with flashbulb


    pause 1
    jump event_06



label genie_lost:
    play music "music/Final Fantasy 7 Game Over Theme.mp3" fadein 1 fadeout 1

    show screen end_u_1
    $ end_u_1_pic =  "03_hp/20_intro/game_over.jpg"
    with flashbulb
    with hpunch
    show screen ctc
    pause
    hide screen ctc
    menu:
        "- Попробовать снова -":
            stop music
            $ renpy.play('sounds/glass_break.mp3')
            play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1
            hide screen end_u_1
            if rum_times == 2:
                $ potions = 1
            elif rum_times == 3:
                $ potions = 2
            else:
                pass
            jump duel
        "- Сдаться -":

            pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
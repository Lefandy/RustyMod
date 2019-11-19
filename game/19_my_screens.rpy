init -1 python:
    hermione_chibi_xpos = 400
    hermione_chibi_ypos = 250
    hermione_speed = 02.5



screen main_menu_01:
    imagebutton:
        xpos 758
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/05_props/01_door.png"
        hover "03_hp/05_props/01_door_02.png"
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("door")]



    imagebutton:
        xpos 120
        ypos 280
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/05_props/02_cupboard.png"
        hover "03_hp/05_props/02_cupboard_02.png"
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("cupboard")]

    imagebutton:
        xpos 111
        ypos 131
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/05_props/00_lrm_hat.png"
        hover "03_hp/05_props/00_lrm_hat_1.png"


        action [Hide("main_menu_01"), Jump("lrm_stats_00")]


    imagebutton:
        xpos 217
        ypos 342
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "newanimation"
        hover "03_hp/05_props/11_genie_02.png"
        hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195, my_tt_ypos=210) ]

        unhovered [Hide("gui_tooltip")]
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("desk")]



    if package_is_here:
        imagebutton:
            xpos 260
            ypos 235
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "03_hp/05_props/owl_06.png"
            hover "03_hp/05_props/owl_06_2.png"


            action [Hide("main_menu_01"), Hide("package"), Jump("mail_02")]

    imagebutton:
        xpos 400
        ypos 225
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "pho_01"
        hover "03_hp/05_props/06_phoenix_02.png"



        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("phoenix")]

    imagebutton:
        xpos 553
        ypos 277
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/05_props/03_fireplace_02.png"
        hover "03_hp/05_props/03_fireplace_03.png"
        action [Hide("main_menu_01"), Jump("fireplace")]

    if letters >= 1:
        imagebutton:
            xpos 315
            ypos 270
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "owl_01"
            hover "03_hp/05_props/owl_04.png"


            action [Hide("main_menu_01"), Jump("mail")]

    imagebutton:
        xpos 640
        ypos 560
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/05_props/menu_bat.png"
        hover "03_hp/05_props/menu_bat.png"
        action [ShowMenu("save")]



    if False and desk_examined == True:
        imagebutton:
            xpos 636
            ypos 16
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "03_hp/11_misc/cal_button.png"
            hover "03_hp/11_misc/cal_button_active.png"
            action [Hide("main_menu_01"), Jump("calendar")]


        if cal_day in circled_days[cal_month] or cal_day in starred_days[cal_month]:
            add "03_hp/11_misc/cal_notify.png" at Position(xpos=590, ypos=1)


        hbox:
            spacing 10 xpos 619 ypos 10
            python:


                status_date = "{size=-4}" + month_info[cal_month][4] + " [cal_day]{/size}"
                if cal_day in holidays[cal_month] or cal_day in weekends[cal_month]:
                    status_date = "{color=942121}" + status_date + "{/color}"
            text status_date


screen calendar:
    zorder 4

    imagebutton:
        xpos 636
        ypos 16
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/11_misc/cal_button.png"
        hover "03_hp/11_misc/cal_button_active.png"
        action [Hide("calendar"), Jump("calendar_cleanup")]


    if cal_day in circled_days[cal_month] or cal_day in starred_days[cal_month]:
        add "03_hp/11_misc/cal_notify.png" at Position(xpos=590, ypos=1)


    hbox:
        spacing 10 xpos 619 ypos 10
        python:


            status_date = "{size=-4}" + month_info[cal_month][4] + " [cal_day]{/size}"
            if cal_day in holidays[cal_month] or cal_day in weekends[cal_month]:
                status_date = "{color=942121}" + status_date + "{/color}"
        text status_date

    add "03_hp/11_misc/calendar.png" at Position(align=(0.5, 0.5))
    add "03_hp/11_misc/cal_w.png" at Position(align=(0.5, 0.29))


    if cal_browsing_month > 9 or cal_browsing_new_year:
        imagebutton:
            xpos 243
            ypos 125
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "03_hp/11_misc/cal_arrow_left.png"
            hover "03_hp/11_misc/cal_arrow_left_active.png"
            action [Jump("calendar_decrement")]
    else:
        add "03_hp/11_misc/cal_arrow_left_disabled.png" at Position(xpos=243, ypos=125, xanchor="center", yanchor="center")

    if cal_browsing_month < 8 or not cal_browsing_new_year:
        imagebutton:
            xpos 557
            ypos 125
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "03_hp/11_misc/cal_arrow_right.png"
            hover "03_hp/11_misc/cal_arrow_right_active.png"
            action [Jump("calendar_increment")]
    else:
        add "03_hp/11_misc/cal_arrow_right_disabled.png" at Position(xpos=557, ypos=125, xanchor="center", yanchor="center")

    python:
        if cal_browsing_month < 10:
            cal_month_str = "0" + str(cal_browsing_month)
        else:
            cal_month_str = str(cal_browsing_month)

    add "03_hp/11_misc/cal_m" + cal_month_str + ".png" at Position(align=(0.5, 0.17))

    $ curr_col = month_info[cal_browsing_month][1]
    $ curr_row = 1
    $ curr_day = 1



    for x in range(month_info[cal_browsing_month][0]):
        $ curr_x, curr_y = cal_pos(curr_col, curr_row)


        if curr_day == month_info[cal_browsing_month][2]:
            add "03_hp/11_misc/cal_moon_new.png" at Position(xpos=curr_x+26, ypos=curr_y-7)
        elif curr_day == month_info[cal_browsing_month][3]:
            add "03_hp/11_misc/cal_moon_full.png" at Position(xpos=curr_x+26, ypos=curr_y-7)

        python:
            if curr_day < 10:
                curr_day_str = "0" + str(curr_day)
            else:
                curr_day_str = str(curr_day)
            if curr_col == 1 or curr_col == 7 or curr_day in holidays[cal_browsing_month]:
                curr_day_str += "r"


        add "03_hp/11_misc/cal_d" + curr_day_str + ".png" at Position(xpos=curr_x, ypos=curr_y)


        if curr_day in circled_days[cal_browsing_month]:
            $ variant = str(renpy.random.randint(1, 7))
            add "03_hp/11_misc/cal_circle" + variant + ".png" at Position(xpos=curr_x-36, ypos=curr_y-28)


        if curr_day in starred_days[cal_browsing_month]:
            $ variant = str(renpy.random.randint(1, 7))
            add "03_hp/11_misc/cal_star" + variant + ".png" at Position(xpos=curr_x-36, ypos=curr_y-28)


        for x in (range(len(cal_notes[cal_browsing_month]))):
            if cal_notes[cal_browsing_month][x][0] == curr_day:
                add "03_hp/11_misc/" + cal_notes[cal_browsing_month][x][1] + ".png" at Position(xpos=curr_x-36, ypos=curr_y-28)


        if (cal_browsing_month == cal_month and curr_day < cal_day) or (cal_browsing_month < cal_month and cal_browsing_month >= 9 and not cal_new_year) or (cal_browsing_month < cal_month and cal_browsing_month >= 1 and cal_new_year) or (cal_browsing_month > cal_month and cal_browsing_month <= 8 and not cal_new_year) or (cal_browsing_month > cal_month and cal_browsing_month >= 9 and cal_new_year):
            $ variant = str(renpy.random.randint(1, 7))
            add "03_hp/11_misc/cal_cross" + variant + ".png" at Position(xpos=curr_x-36, ypos=curr_y-28)

        python:
            if curr_col + 1 > 7:
                curr_col = 0
                curr_row += 1

            curr_col += 1
            curr_day += 1

screen cal_button_flash:
    zorder 4

    add "03_hp/11_misc/cal_button_active.png" at Position(xpos=636, ypos=16, xanchor="center", yanchor="center")


    hbox:
        spacing 10 xpos 619 ypos 10
        python:


            status_date = "{size=-4}" + month_info[cal_month][4] + " [cal_day]{/size}"
            if cal_day in holidays[cal_month] or cal_day in weekends[cal_month]:
                status_date = "{color=942121}" + status_date + "{/color}"
        text status_date



screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

screen animation_feather:
    add "feather" xpos 360 ypos 140
    zorder 4

screen rum_screen:
    add "03_hp/05_props/02_cupboard_03.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=192, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    add "03_hp/05_props/krk1.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    add "rum" xpos 20 ypos 110
    zorder 1

screen feeding:
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    add "feeding" xpos 270 ypos 75
    zorder 1

screen petting:
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    add "petting" xpos 250 ypos 65
    zorder 1

screen sad_phoenix:
    add "sad_01" xpos 423 ypos 130
    zorder 1

screen notes:
    add "notes" xpos 320 ypos 330
    zorder 1

screen paperwork:
    add "paperwork_02" xpos 84 ypos 205

screen reading_near_fire:
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    add "reading_near_fire" xpos 290 ypos 205
    zorder 4

screen reading:
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    add "reading" xpos 290 ypos 205
    zorder 4

screen done_reading:
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    add im.Flip("03_hp/animation/reading_07.png", horizontal=True) xpos 290 ypos 205
    zorder 4

screen done_reading_02:
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    add "03_hp/animation/reading_07.png" xpos 290 ypos 205

    zorder 4

screen genie_jerking_off tag chibi_genie:
    add "genie_jerking_off" xpos 78 ypos 205
    zorder 2


screen genie_jerking_sperm tag after_jerk:
    add "genie_jerking_sperm_ani" xpos 78 ypos 205

    zorder 2

screen genie_jerking_sperm_02 tag after_jerk:
    add "03_hp/animation/jerking_sperm_11.png" xpos 78 ypos 205

    zorder 2



screen candlefire_01:
    add "candle_fire" xpos 100 ypos 43
    zorder 2

screen candlefire_02:
    add "candle_fire_02" xpos 583 ypos 108
    zorder 2















screen phoenix_food:
    add "03_hp/05_props/06_phoenix_food.png" xpos 350 ypos 49
    zorder 3

screen fireplace_fire:
    add "fireplace_fire" xpos 436 ypos 141
    zorder 1



screen room:

    add "03_hp/01_bg/01_main_room.png"
screen room_night:
    add "03_hp/01_bg/01_main_room_02.png"

screen look_01:
    add "03_hp/24_daphne/dap_look_a1.png"
screen look_02:
    add "03_hp/24_daphne/dap_look_a2.png"
screen look_fap_01:
    add "03_hp/24_daphne/dap_look_b2.png"

screen dap_fap_genie:
    add "dap_fap" at Position(xpos=70)
    zorder 2

screen door:
    add "03_hp/05_props/01_door.png" at Position(xpos=758, ypos=315, xanchor="center", yanchor="center")
screen cupboard:
    add "03_hp/05_props/02_cupboard_00.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
screen chair:
    add "03_hp/05_props/04_chair.png" at Position(xpos=653, ypos=300, xanchor="center", yanchor="center")
screen chair_02:
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=192, ypos=300, xanchor="center", yanchor="center")
screen fireplace:
    add "03_hp/05_props/03_fireplace.png" at Position(xpos=553, ypos=277, xanchor="center", yanchor="center")
screen phoenix:
    add "03_hp/05_props/06_phoenix.png" at Position(xpos=400, ypos=225, xanchor="center", yanchor="center")
screen phoenix_no:
    add "03_hp/05_props/06_phoenix_no.png" at Position(xpos=400, ypos=225, xanchor="center", yanchor="center")
screen candle_01:
    add "03_hp/05_props/07_candle.png" at Position(xpos=693, ypos=225, xanchor="center", yanchor="center")
screen candle_02:
    add "03_hp/05_props/08_candle.png" at Position(xpos=210, ypos=160, xanchor="center", yanchor="center")
screen genie tag chibi_genie:

    add "03_hp/05_props/11_genie_00.png" at Position(xpos=217, ypos=342, xanchor="center", yanchor="center")

screen krk:
    add "03_hp/05_props/krk1.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")

screen owl:
    add "03_hp/05_props/owl_01.png" at Position(xpos=315, ypos=270, xanchor="center", yanchor="center")
screen owl_02:
    add "03_hp/05_props/owl_05.png" at Position(xpos=315, ypos=270, xanchor="center", yanchor="center")
screen package:
    add "03_hp/05_props/owl_06.png" at Position(xpos=260, ypos=235, xanchor="center", yanchor="center")
screen owl_03:
    add "03_hp/05_props/owl_05.png" at Position(xpos=310, ypos=235, xanchor="center", yanchor="center")

screen dumbledore tag chibi_genie:

    add "03_hp/05_props/dum.png" at Position(xpos=230, ypos=336, xanchor="center", yanchor="center")


screen thought(position=None) tag emo:

    add "thought" at (position if position!=None else Position(xpos=tt_xpos, ypos=tt_ypos))
    zorder 2


screen snape_01 tag snape:

    add "03_hp/09_snape_ani/snape_0130.png" at Position(xpos=610, ypos=210)

screen snape_01_f tag snape:

    add im.Flip("03_hp/09_snape_ani/snape_0130.png", horizontal=True) at Position(xpos=610, ypos=210)

screen snape_02 tag snape:

    add "00_ex_characters/05_ginny/graphics/chibis/chibi_base.png" at Position(xpos=360, ypos=210)
    # add "00_ex_characters/05_ginny/chibi.png" at Position(xpos=360, ypos=210)

    zorder 3

screen ginny_02 tag ginny:

    # add "00_ex_characters/05_ginny/graphics/dialog/ginny_dialog_base.png" at Position(xpos=360, ypos=210)
    add "03_hp/animation/01.png" at Position(xpos=ginny_chibi_xpos, ypos=ginny_chibi_ypos)
    zorder 3

screen snape_03(aXpos) tag snape:

    add "03_hp/09_snape_ani/snape_0130.png" at Position(xpos=aXpos, ypos=210)
    zorder 3

screen snape_03_f(aXpos) tag snape:

    add im.Flip("03_hp/09_snape_ani/snape_0130.png", horizontal=True) at Position(xpos=aXpos, ypos=210)
    zorder 3




screen snape_walk_01 tag snape:

    add "snape_walk_01" at custom_walk(walk_xpos, walk_xpos2)
    zorder 2



screen snape_walk_01_f tag snape:

    add "snape_walk_01_f" at custom_walk(walk_xpos, walk_xpos2)
    zorder 2


screen hermione_01 tag hermione:

    add "03_hp/animation/h_walk_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2

screen hermione_01_f tag hermione:

    add im.Flip("03_hp/animation/h_walk_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2




screen hermione_02 tag hermione:

    add "ch_hem blink" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2

screen hermione_02_b tag hermione:

    add "03_hp/animation/01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2




screen hermione_lift_skirt_angry tag hermione:

    add "03_hp/16_hermione_chibi/panties_00.png" at Position(xpos=350, ypos=190)

screen hermione_lift_skirt_normal tag hermione:

    add "03_hp/16_hermione_chibi/panties_01.png" at Position(xpos=350, ypos=190)

screen hermione_lift_skirt_no_panties tag hermione:

    add "03_hp/16_hermione_chibi/panties_02.png" at Position(xpos=350, ypos=190)

screen hermione_lift_skirt_shift_panties tag hermione:

    add "03_hp/16_hermione_chibi/panties_02_s.png" at Position(xpos=350, ypos=190)



screen hermione_04 tag hermione:

    add "03_hp/16_hermione_chibi/tits_00.png" at Position(xpos=350, ypos=190)

screen hermione_04_b tag hermione:

    add "03_hp/16_hermione_chibi/tits_00.png" at Position(xpos=250, ypos=190)



screen hermione_walk_01 tag hermione:
    zorder 2

    add "ch_hem walk_01" at custom_walk_02(walk_xpos, walk_xpos2)


screen hermione_chibi_robe tag hermione:
    zorder 2

    add "ch_hem robe" at custom_walk_02(walk_xpos, walk_xpos2)

screen hermione_chibi_robe_f tag hermione:
    zorder 2

    add "ch_hem robe_f" at custom_walk_02(walk_xpos, walk_xpos2)


screen hermione_walk_01_f tag hermione:
    zorder 2

    add "ch_hem walk_01_f" at custom_walk_02(walk_xpos, walk_xpos2)

screen hermione_walk_02_f(timeClose) tag hermione:
    zorder 2

    add "ch_hem walk_01_f" at custom_walk_02(walk_xpos, walk_xpos2)
    timer timeClose action [Hide("hermione_walk_02_f")]


screen hermione_run tag hermione:
    zorder 2

    add "ch_hem run_f" at custom_walk_02(walk_xpos, walk_xpos2)



screen nsp_hermione_business tag hermione:

    add "03_hp/animation/nsp_business.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2

screen nsp_hermione_cheerleader_gryffindor tag hermione:

    add "03_hp/08_animation_02/nsp01_cheerleader_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2

screen nsp_hermione_cheerleader_gryffindor_dance1 tag hermione:

    add "nsp_cheerleader_dance1_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2

screen nsp_hermione_cheerleader_gryffindor_dance2 tag hermione:

    add "nsp_cheerleader_dance2_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2

screen nsp_hermione_panic tag hermione:

    add "nsp_hermiona_panic_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 2



screen genie_walk tag chibi_genie:

    add "genie_walk_ani" at genie_walk(walk_xpos, walk_xpos2)



screen snape_main tag big_snape:

    # add "03_hp/10_snape_main/snape_main.png" xpos tt_xpos ypos tt_ypos
    add "03_hp/09_snape_ani/ginny_dialog_base.png" xpos tt_xpos ypos tt_ypos

    # add s_sprite xpos tt_xpos + 299 ypos tt_ypos

    zorder 3




screen s_emo_01 tag semo:

    add "03_hp/10_snape_main/s_emo_01.png" xpos tt_xpos ypos tt_ypos
    zorder 2

















screen bld1:
    add "03_hp/11_misc/bld.png"
    zorder 3
screen ctc:
    zorder 7
    add "ctc4"
screen points:
    add "03_hp/11_misc/points_02.png" at Position(xpos=0, ypos=1)
    hbox:
        spacing 10 xpos 146 ypos 11
        text "{size=-5}[slytherin]{/size}"
    hbox:
        spacing 10 xpos 252 ypos 11
        text "{size=-5}[gryffindor]{/size}"
    hbox:
        spacing 10 xpos 365 ypos 11
        text "{size=-5}[hufflepuff]{/size}"
    hbox:
        spacing 10 xpos 37 ypos 11
        text "{size=-5}[ravenclaw]{/size}"









    hbox:
        spacing 10 xpos 619 ypos 10
        python:


            status_date = "{size=-4}" + month_info[cal_month][4] + " [cal_day]{/size}"
            if cal_day in holidays[cal_month] or cal_day in weekends[cal_month]:
                status_date = "{color=942121}" + status_date + "{/color}"
        text status_date



    hbox:
        spacing 10 xpos 734 ypos 10
        text "{size=-4}[gold]{/size}"


screen gift(_m1_19_my_screens__par=the_gift):
    zorder 5
    add "03_hp/18_store/00.png"
    add _m1_19_my_screens__par

screen pic_event(_m1_19_my_screens__par=pic_for_event):
    zorder 5
    add _m1_19_my_screens__par















screen letter(par1=letter_text):
    zorder 4
    add "03_hp/11_misc/letter.png" at Position(xpos=200, ypos=30)
    hbox:
        spacing 40 xpos 270 ypos 80 xmaximum 250
        text par1
screen blkfade:
    zorder 5
    add "blackfade.png"

screen letterbig(par1=letter_text):
    zorder 4
    add "03_hp/11_misc/letterbig.png" at Position(xpos=40, ypos=30)
    hbox:
        spacing 40 xpos 150 ypos 80 xmaximum 480
        text par1


screen jerkingimage:
    zorder jerk_zorder
    add jerk_image



screen blktone:
    zorder 5
    add im.Alpha("blackfade.png", 0.5)

screen blktone7:
    zorder 7
    add im.Alpha("blackfade.png", 0.5)

screen blktone8:
    zorder 5
    add im.Alpha("blackfade.png", 0.8)

screen whitetone8:
    zorder 5
    add im.Alpha("white.jpg", 0.8)

screen white:
    zorder 3
    add "white.jpg"

screen emo:

    add "emo8" at Position(xpos=700, ypos=100, xanchor=0, yanchor=0)




screen adding_03_points:
    add "what_03_points" at Position(xpos=131, ypos=0)


screen gryffindor_03_points:
    add "what_03_points" at Position(xpos=238, ypos=0)
screen gryffindor_01_points:
    add "what_01_points" at Position(xpos=238, ypos=0)
screen gryffindor_02_points:
    add "what_02_points" at Position(xpos=238, ypos=0)
screen gryffindor_05_points:
    add "what_05_points" at Position(xpos=238, ypos=0)
screen gryffindor_15_points:
    add "what_15_points" at Position(xpos=238, ypos=0)



screen hufflepuff_03_points:
    add "what_03_points" at Position(xpos=348, ypos=0)
screen hufflepuff_01_points:
    add "what_01_points" at Position(xpos=348, ypos=0)
screen hufflepuff_02_points:
    add "what_02_points" at Position(xpos=348, ypos=0)
screen hufflepuff_05_points:
    add "what_05_points" at Position(xpos=348, ypos=0)
screen hufflepuff_15_points:
    add "what_15_points" at Position(xpos=348, ypos=0)


screen ravenclaw_03_points:
    add "what_03_points" at Position(xpos=22, ypos=0)
screen ravenclaw_01_points:
    add "what_01_points" at Position(xpos=22, ypos=0)
screen ravenclaw_02_points:
    add "what_02_points" at Position(xpos=22, ypos=0)
screen ravenclaw_05_points:
    add "what_05_points" at Position(xpos=22, ypos=0)
screen ravenclaw_15_points:
    add "what_15_points" at Position(xpos=22, ypos=0)




screen s_p_u:
    add s_p_u_pic at Position(xpos=131, ypos=0)

screen s_p_u2:
    add s_p_u_pic at Position(xpos=131, ypos=0)
    add s_p_u_pic at Position(xpos=131, ypos=22)


screen g_p_u:
    add g_p_u_pic at Position(xpos=238, ypos=0)

screen h_p_u:
    add h_p_u_pic at Position(xpos=348, ypos=0)

screen r_p_u:
    add r_p_u_pic at Position(xpos=22, ypos=0)







screen genie_stands:
    add "03_hp/animation/feeding_01.png" xpos tt_xpos ypos tt_ypos

screen genie_stands_f:
    add im.Flip("03_hp/animation/feeding_01.png", horizontal=True) xpos tt_xpos ypos tt_ypos

screen desk:
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    zorder 2

screen desk_02:
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    zorder 2




screen snape_defends:
    add "ch_sna defend" at Position(xpos=-90, ypos=-5)
    zorder 7


screen minus_100:
    add "minus_100" at Position(xpos=640, ypos=120)

screen minus_300:
    add "minus_300" at Position(xpos=640, ypos=120)


screen minus_500:
    add "minus_500" at Position(xpos=640, ypos=120)

screen minus_0:
    add "minus_0" at Position(xpos=640, ypos=120)

screen minus_0_genie:
    add "minus_0" at Position(xpos=310, ypos=120)
screen minus_400_genie:
    add "minus_400" at Position(xpos=310, ypos=120)
screen minus_50_genie:
    add "minus_50" at Position(xpos=310, ypos=120)

screen plus_300:
    add "plus_300" at Position(xpos=310, ypos=120)





screen with_snape tag hanging_with_snape:
    add "03_hp/05_props/with_snape.png"

    zorder 3
screen with_snape_animated tag hanging_with_snape:
    add "genie_jerking_sperm"

    zorder 3
screen with_snape_animated_advanced tag hanging_with_snape:
    add "hanging_with_snape_animated"

    zorder 3

screen s_head tag head:

    add "03_hp/10_snape_main/snape_main.png" xpos tt_xpos ypos tt_ypos
    add s_sprite xpos tt_xpos + 299 ypos tt_ypos
    zorder 8

screen s_head2 tag head:

    add "03_hp/10_snape_main/snape_main.png" xpos s_head_xpos ypos s_head_ypos
    add s_sprite xpos s_head_xpos + 299 ypos s_head_ypos
    zorder 8














screen groping_01 tag favor:

    add "groping_01" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)

screen groping_02 tag favor:

    add "groping_02" at Position(xpos=-200, ypos=10)
    add "groping_02_blinking" at Position(xpos=-200, ypos=10)

screen no_groping_01 tag favor:

    add "03_hp/animation/grope_05.png" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)

screen no_groping_02 tag favor:

    add "03_hp/animation/grope_b_05.png" at Position(xpos=-200, ypos=10)
    add "groping_02_blinking" at Position(xpos=-200, ypos=10)



screen groping_03 tag favor:

    add "groping_03_ani" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)



screen groping_naked_tits tag favor:

    add "groping_naked_tits_ani" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 1



screen jerking_off_01 tag favor:

    add "jerking_off_ani" at Position(xpos=-200, ypos=10)
    if not no_blinking:
        add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 1


screen jerking_off_cum:
    add "jerking_off_cum_ani" at Position(xpos=-200, ypos=10)

    zorder 2


screen genie_and_tits_01 tag favor:

    add "03_hp/05_props/admire_tits_00.png" at Position(xpos=-200, ypos=10)


screen clothed_dance tag hermione:


    add "clothed_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)


screen no_vest_dance tag hermione:


    add "no_vest_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)


screen no_skirt_dance tag hermione:


    add "no_skirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)


screen no_shirt_dance tag hermione:


    add "no_shirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)


screen no_shirt_no_skirt_dance:

    zorder 3
    add "no_shirt_no_skirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)


screen h_c_u tag hermione:

    add h_c_u_pic at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)

screen h_c_u2 tag hermione:

    zorder 3
    add h_c_u_pic at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)


screen g_c_u tag genie:

    add g_c_u_pic at Position(xpos=genie_chibi_xpos, ypos=genie_chibi_ypos)
    zorder 3


screen s_c_u tag snape:

    add s_c_u_pic at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos)
    zorder 3








screen g_c_c_u:
    add g_c_c_u_pic at Position(xpos=genie_cum_chibi_xpos, ypos=genie_cum_chibi_ypos)

screen g_c_c_u2:
    zorder 4
    add g_c_c_u_pic at Position(xpos=genie_cum_chibi_xpos, ypos=genie_cum_chibi_ypos)


screen s_c_c_u:
    add s_c_c_u_pic at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)




screen end_u_1 tag ending:
    add end_u_1_pic

    zorder 2


screen end_u_2 tag ending:
    add end_u_2_pic

    zorder 2


screen end_u_3:
    add end_u_3_pic
    zorder 2


screen end_u_4:
    add end_u_4_pic
    zorder 2


screen new_window:
    zorder -2
    add "03_hp/01_bg/03_weather.png"

screen cloud:
    zorder -1
    add "03_hp/07_weather/cloud_small.png" at cloud_move

screen cloud_night_01:

    add "03_hp/07_weather/night_cloud_02.png" at cloud_night_move_01

screen cloud_night_02:

    add "03_hp/07_weather/night_cloud_01.png" at cloud_night_move_02

screen cloud_night_03:

    add "03_hp/07_weather/night_cloud_03.png" at cloud_night_move_03



screen credits_chibi:
    zorder 5
    add dermo at Position(xpos=280, ypos=140)


screen credits_chibi2:
    zorder 5
    add dermo at Position(xpos=150, ypos=140)

screen uni_cr:
    zorder 5
    add dermo at Position(xpos=xder, ypos=yder)

screen patreon_cr:
    zorder 5
    add dermo at Position(xpos=xder, ypos=yder)






screen l_head tag head:

    zorder 8
    add lola_body xpos lx ypos ly
    add lola_face xpos lx ypos ly
    if l_blush:
        add "03_hp/22_lola/blush.png" xpos lx ypos ly
    if l_things:
        add "03_hp/22_lola/things.png" xpos lx ypos ly
    if l_question:
        add "03_hp/22_lola/question.png" xpos lx ypos ly
    if l_drop:
        add "03_hp/22_lola/drop.png" xpos lx ypos ly
    if l_hearts:
        add "03_hp/22_lola/hearts.png" xpos lx ypos ly
    if l_exclamation:
        add "03_hp/22_lola/exclamation.png" xpos lx ypos ly
    if l_tears:
        add "03_hp/22_lola/tears.png" xpos lx ypos ly



screen l_hermiona tag body:

    zorder 8

    add "00_ex_characters/00_hermione/graphics/hair/hair_normal_1.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/head.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/hair/hair_normal_2.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/body.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/legs_universal.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/hands_universal.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/tits_no.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/clothes/stockings/tights.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/clothes/skirts/skirt_business.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/clothes/shirts/shirt_business_B.png" xpos hx ypos hy

    if h_red_angry:
        add "00_ex_characters/00_hermione/graphics/face/body_47.png" xpos hx ypos hy
    if h_angry:
        add "00_ex_characters/00_hermione/graphics/face/body_05.png" xpos hx ypos hy
    if h_smile:
        add "00_ex_characters/00_hermione/graphics/face/body_24.png" xpos hx ypos hy

screen l_hermiona2 tag body:

    zorder 2

    add "00_ex_characters/00_hermione/graphics/hair/hair_normal_1.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/head.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/hair/hair_normal_2.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/body.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/legs_universal.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/hands_universal.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/body/tits_no.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/clothes/skirts/skirt_cheerleader.png" xpos hx ypos hy
    add "00_ex_characters/00_hermione/graphics/clothes/shirts/shirt_cheerleader.png" xpos hx ypos hy

    if h_red_angry:
        add "00_ex_characters/00_hermione/graphics/face/body_47.png" xpos hx ypos hy
    if h_angry:
        add "00_ex_characters/00_hermione/graphics/face/body_05.png" xpos hx ypos hy
    if h_smile:
        add "00_ex_characters/00_hermione/graphics/face/body_24.png" xpos hx ypos hy
    if h_red_smile:
        add "00_ex_characters/00_hermione/graphics/face/body_46.png" xpos hx ypos hy

screen l_daphne tag body:

    zorder 2

    add "00_ex_characters/01_daphne/graphics/body/daphne_head_base.png" xpos dx ypos dy
    add "00_ex_characters/01_daphne/graphics/body/daphne_body.png" xpos dx ypos dy
    add "00_ex_characters/01_daphne/graphics/hair/daphne_hair_base.png" xpos dx ypos dy
    add "00_ex_characters/01_daphne/graphics/clothes/daphne_cheer_stockings.png" xpos dx ypos dy
    add "00_ex_characters/01_daphne/graphics/clothes/daphne_cheer_skirt_long.png" xpos dx ypos dy
    add "00_ex_characters/01_daphne/graphics/pose/daphne_arms_onhips.png" xpos dx ypos dy
    add "00_ex_characters/01_daphne/graphics/clothes/daphne_cheer_sleeves_handsonhips.png" xpos dx ypos dy
    add "00_ex_characters/01_daphne/graphics/clothes/daphne_cheer_topbase.png" xpos dx ypos dy

    if d_angry:
        add "00_ex_characters/01_daphne/graphics/face/daphne_eyes_strongnarrowforward_Z.png" xpos dx ypos dy
        add "00_ex_characters/01_daphne/graphics/face/daphne_brows_narrowed_ZS.png" xpos dx ypos dy
        add "00_ex_characters/01_daphne/graphics/face/daphne_mouth_angry.png" xpos dx ypos dy
    if d_smile:
        add "00_ex_characters/01_daphne/graphics/face/daphne_eyes_normal_Z.png" xpos dx ypos dy
        add "00_ex_characters/01_daphne/graphics/face/daphne_brows_narrowed.png" xpos dx ypos dy
        add "00_ex_characters/01_daphne/graphics/face/daphne_mouth_open.png" xpos dx ypos dy


screen heal3:
    add "heal" xpos 430 ypos 20
    zorder 4

screen minerva_door:
    add "03_hp/25_pic_events/minerva_door.png" xpos 580 ypos 100
    zorder 6
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii



screen ginny_1 tag ginny:

    add "00_ex_characters/05_ginny/graphics/dialog/ginny_dialog_base.png" xpos tt_xpos ypos tt_ypos
    # add s_sprite xpos tt_xpos + 299 ypos tt_ypos

    zorder 3

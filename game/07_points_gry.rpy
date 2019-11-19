label points_changes_gryffindor:

    if generating_points_gryffindor == 1 or generating_points_gryffindor == 2:
        pass
    elif generating_points_gryffindor == 3 or generating_points_gryffindor == 4:
        $ gryffindor +=1
        hide screen g_p_u
        $ g_p_u_pic = "what_01_points"
        show screen g_p_u

    elif generating_points_gryffindor == 5 or generating_points_gryffindor == 6:
        $ gryffindor +=2
        hide screen g_p_u
        $ g_p_u_pic = "what_02_points"
        show screen g_p_u

    elif generating_points_gryffindor == 7 or generating_points_gryffindor == 8:
        $ gryffindor +=3
        hide screen g_p_u
        $ g_p_u_pic = "what_03_points"
        show screen g_p_u

    elif generating_points_gryffindor == 9:
        $ gryffindor +=5
        hide screen g_p_u
        $ g_p_u_pic = "what_05_points"
        show screen g_p_u


    elif generating_points_gryffindor == 7:
        $ gryffindor +=7
        hide screen g_p_u
        $ g_p_u_pic = "what_07_points"
        show screen g_p_u







    if generating_points_hufflepuff == 1 or generating_points_hufflepuff == 2:
        pass

    elif generating_points_hufflepuff == 3 or generating_points_hufflepuff == 4:
        $ hufflepuff +=1
        hide screen h_p_u
        $ h_p_u_pic = "what_01_points"
        show screen h_p_u

    elif generating_points_hufflepuff == 5 or generating_points_hufflepuff == 6:
        $ hufflepuff +=2
        hide screen h_p_u
        $ h_p_u_pic = "what_02_points"
        show screen h_p_u

    elif generating_points_hufflepuff == 7 or generating_points_hufflepuff == 8:
        $ hufflepuff +=4
        hide screen h_p_u
        $ h_p_u_pic = "what_04_points"
        show screen h_p_u

    elif generating_points_hufflepuff == 9:
        $ hufflepuff +=7
        hide screen h_p_u
        $ h_p_u_pic = "what_07_points"
        show screen h_p_u

    elif generating_points_hufflepuff == 10:
        $ hufflepuff +=14
        hide screen h_p_u
        $ h_p_u_pic = "what_14_points"
        show screen h_p_u





    if generating_points_ravenclaw == 1 or generating_points_ravenclaw == 2:
        pass
    elif generating_points_ravenclaw == 3 or generating_points_ravenclaw == 4:
        $ ravenclaw +=1
        hide screen r_p_u
        $ r_p_u_pic = "what_01_points"
        show screen r_p_u

    elif generating_points_ravenclaw == 5 or generating_points_ravenclaw == 6:
        $ ravenclaw +=2
        hide screen r_p_u
        $ r_p_u_pic = "what_02_points"
        show screen r_p_u

    elif generating_points_ravenclaw == 7 or generating_points_ravenclaw == 8:
        $ ravenclaw +=6
        hide screen r_p_u
        $ r_p_u_pic = "what_06_points"
        show screen r_p_u

    elif generating_points_ravenclaw == 9:
        $ ravenclaw +=8
        hide screen r_p_u
        $ r_p_u_pic = "what_08_points"
        show screen r_p_u

    elif generating_points_ravenclaw == 10:
        $ ravenclaw +=13
        hide screen r_p_u
        $ r_p_u_pic = "what_13_points"
        show screen r_p_u

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
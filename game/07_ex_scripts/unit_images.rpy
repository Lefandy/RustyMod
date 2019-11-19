label daphne_images_init:
    python:
        _m1_unit_Images__path="03_hp/24_daphne/dap_walk_"


        for s in {"a", "b", "c", "d", "e", "f", "g"}:  
            _m1_unit_Images__s=s
            
            
            
            renpy.image("chibidaphne "+_m1_unit_Images__s+" go", Animation(_m1_unit_Images__path+s+"1.png", .08,
                                        _m1_unit_Images__path+s+"2.png", .08,
                                        _m1_unit_Images__path+s+"3.png", .08,
                                        _m1_unit_Images__path+s+"2.png", .08,
                                        _m1_unit_Images__path+s+"1.png", .08,
                                        _m1_unit_Images__path+s+"4.png", .08,
                                        _m1_unit_Images__path+s+"5.png", .08,
                                        _m1_unit_Images__path+s+"4.png", .08
                                        ))
            renpy.image("chibidaphne "+_m1_unit_Images__s+" goout", Animation(im.Flip(_m1_unit_Images__path+s+"1.png", horizontal=True), .08,
                                        im.Flip(_m1_unit_Images__path+s+"2.png", horizontal=True), .08,
                                        im.Flip(_m1_unit_Images__path+s+"3.png", horizontal=True), .08,
                                        im.Flip(_m1_unit_Images__path+s+"2.png", horizontal=True), .08,
                                        im.Flip(_m1_unit_Images__path+s+"1.png", horizontal=True), .08,
                                        im.Flip(_m1_unit_Images__path+s+"4.png", horizontal=True), .08,
                                        im.Flip(_m1_unit_Images__path+s+"5.png", horizontal=True), .08,
                                        im.Flip(_m1_unit_Images__path+s+"4.png", horizontal=True), .08
                                        ))




    image chibidaphne a blink:
        choice 12.0:
            "03_hp/24_daphne/dap_blink_a1.png"
            pause .4
        choice:
            "03_hp/24_daphne/dap_blink_a2.png"
            pause .08
        repeat

    image chibidaphne a tits:
        "03_hp/24_daphne/dap_tits_a1.png"

    image chibidaphne b blink:
        choice 12.0:
            "03_hp/24_daphne/dap_blink_b1.png"
            pause .4
        choice:
            "03_hp/24_daphne/dap_blink_b2.png"
            pause .08
        repeat

    image chibidaphne c blink:
        choice 12.0:
            "03_hp/24_daphne/dap_blink_c1.png"
            pause .4
        choice:
            "03_hp/24_daphne/dap_blink_c2.png"
            pause .08
        repeat

    image chibidaphne d blink:
        choice 12.0:
            "03_hp/24_daphne/dap_blink_d1.png"
            pause .4
        choice:
            "03_hp/24_daphne/dap_blink_d2.png"
            pause .08
        repeat

    image chibidaphne e blink:
        choice 12.0:
            "03_hp/24_daphne/dap_blink_e1.png"
            pause .4
        choice:
            "03_hp/24_daphne/dap_blink_e2.png"
            pause .08
        repeat

    image chibidaphne f blink:
        choice 12.0:
            "03_hp/24_daphne/dap_blink_f1.png"
            pause .4
        choice:
            "03_hp/24_daphne/dap_blink_f2.png"
            pause .08
        repeat

    image chibidaphne g blink:
        choice 12.0:
            "03_hp/24_daphne/dap_blink_g1.png"
            pause .4
        choice:
            "03_hp/24_daphne/dap_blink_g2.png"
            pause .08
        repeat

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
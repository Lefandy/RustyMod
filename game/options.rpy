








init -1 python hide:

    config.autoreload = False 





    config.developer = True



    config.screen_width = 800
    config.screen_height = 600




    if _preferences.language == "english" :
        config.window_title = u"Witch Trainer 1.6f"
    else :
        config.window_title = u"Witch Trainer 1.6f"



    config.name = "Witch Trainer"
    config.version = "1.6f"










    theme.threeD(
        
        

        
        widget = "#777777",

        
        widget_hover = "#73735C",

        
        widget_text = "#404033",

        
        
        widget_selected = "#000000",

        
        disabled = "#73735C",

        
        disabled_text = "#8C8C70",

        
        label = "#1A0001",

        
        frame = "#555544",

        
        
        
        
        mm_root = "titleMain",

        
        
        
        gm_root = "title2.jpg",
        


        
        
        rounded_window = False,

        
        
        
        )










    style.window.background = Frame("frame2.png", 12, 12)












    style.window.left_padding = 65
    style.window.right_padding = 70
    style.window.top_padding = 40





    style.window.yminimum = 143



























    style.default.font = "CREABBB.TTF"


    style.default.size = 18
    style.default.color = "#402313"











    config.has_sound = True



    config.has_music = True



    config.has_voice = False



    style.button.activate_sound = "click3.mp3"
    style.imagemap.activate_sound = "click3.mp3"












    config.main_menu_music = "music/01 Prologue.mp3"












    config.help = "README.html"






    config.enter_transition = None


    config.exit_transition = None


    config.intra_transition = None


    config.main_game_transition = None


    config.game_main_transition = None


    config.end_splash_transition = Dissolve(.3)


    config.end_game_transition = Dissolve(.7)


    config.after_load_transition = Dissolve(.3)


    config.window_show_transition = Dissolve(.3)


    config.window_hide_transition = Dissolve(.3)


    config.adv_nvl_transition = dissolve


    config.nvl_adv_transition = dissolve


    config.enter_yesno_transition = None


    config.exit_yesno_transition = None


    config.enter_replay_transition = None


    config.exit_replay_transition = None


    config.say_attribute_transition = None





python early:
    config.save_directory = "WitchTrainer-1.6f"

init -1 python hide:









    config.default_fullscreen = False



    config.default_text_cps = 40



    config.default_afm_time = 40





















    style.menu_choice.hover_color = "#e9d570"
    style.menu_choice.hover_outlines = [(2, "#402313", 0, 0)]







    style.say_who_window.background = Frame("PinkBox.png", 15, 15) 
    style.say_who_window.xalign = 0.0
    style.say_who_window.yalign = 1.0


    style.say_who_window.left_padding = 20
    style.say_who_window.top_padding = 15
    style.say_who_window.right_padding = 15
    style.say_who_window.bottom_padding = 15
    style.say_who_window.xminimum = 150
    style.say_who_window.yminimum = 10
    style.say_who_window.xfill = False






init python:




    build.directory_name = "WitchTrainer_1.6f"




    build.executable_name = "Witch Trainer"



    build.include_update = True





























    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/_backup_and_src/**', None)
    build.classify('**/FAQ_private/**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)


    build.archive("scripts", "all")
    build.archive("hxml", "all")

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/music/**.ogg', 'archive')
    build.classify('game/music/**.mp3', 'archive')
    build.classify('game/music/**.wav', 'archive')
    build.classify('game/sounds/**.ogg', 'archive')
    build.classify('game/sounds/**.mp3', 'archive')
    build.classify('game/sounds/**.wav', 'archive')
    build.classify('game/**.TTF', 'archive')
    build.classify('game/**.aif', 'archive')

    build.classify('game/**.hxml', 'hxml')

    build.classify('game/**.rpy', None)
    build.classify('game/**.rpyc', 'scripts')









    config.window_icon = "icon.png"

    config.hard_rollback_limit = 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
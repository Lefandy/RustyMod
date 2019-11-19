







screen say:
    zorder 6


    default side_image = None
    default two_window = False




    if not two_window:


        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:


        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"


    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


    use quick_menu








screen choice:
    add "03_hp/11_misc/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign 0.5

        has vbox:
            style "menu"
            spacing 2

        for caption, action, chosen in items:

            if action:

                button:
                    action action
                    style "menu_choice_button"

                    text caption style "menu_choice"

            else:
                text caption style "menu_caption"
    zorder 7

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)








screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu







screen nvl:
    zorder 7
    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu







screen main_menu tag menu:





    window:
        style "mm_root"
        add title_anim_fire
        add title_anim_eyes








    frame:
        style_group "mm"
        xalign .96
        yalign .96

        has vbox


        if not persistent.game_complete:
            textbutton _("Новая игра") action Start()
        if persistent.game_complete:
            textbutton _("Новая игра {size=+3}+{/size}") action Start()
        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Экстра") action ShowMenu("extras")
        textbutton _("Форум") action Start("forum")
        textbutton _("Пожертвовать") action Start("donate")


        textbutton _("Выход") action Quit(confirm=True)

    imagebutton:
        xpos 110
        ypos 406


        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/23_title/ru_dis.png"
        hover "03_hp/23_title/ru_en.png"









        action [ Language(None)]

    imagebutton:
        xpos 110
        ypos 453


        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/23_title/en_dis.png"
        hover "03_hp/23_title/en_en.png"







        action [ Language("english")]

init -2:


    style mm_button:
        size_group "mm"





screen lang_menu:
    window:
        style "gm_root"
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98


        has vbox

        label _("Выбор языка")
        textbutton "Русский" action Language(None)
        textbutton "English" action Language("english")
        textbutton _("Отмена") action Start("assmenu")




screen extras:
    window:
        style "gm_root"
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox









        textbutton _("От разработчиков") action Start("devel")
        textbutton _("Прочее") action ShowMenu("old_extras")


        textbutton _("Отмена") action Start("assmenu")

screen old_extras:
    window:
        style "gm_root"
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Как играть") action Start("howtoplay")
        if not persistent.game_complete:
            textbutton _("{color=#858585}Галерея{/color}") action Start("gallery_locked")
        if persistent.game_complete:
            textbutton _("Галерея") action Start("gallery")

        textbutton _("Отмена") action Start("assmenu")

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"











screen navigation:


    window:
        style "gm_root"


    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Назад") action Return()
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Сохранить") action ShowMenu("save")
        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Главное меню") action MainMenu()
        textbutton _("Помощь") action OpenURL("http://forum.sad-crab.com/forum/main-forum/темы/63-последняя-версия-прохождение-ответы-на-самые-частые-вопросы-история-изменений")
        textbutton _("Выход") action Quit()

init -2:


    style gm_nav_button:
        size_group "gm_nav"













screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox



        hbox:
            style_group "file_picker_nav"

            textbutton _("Пред."):
                action FilePagePrevious()

            textbutton _("Авто"):
                action FilePage("auto")

            textbutton _("Быстрые"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("След."):
                action FilePageNext()

        $ columns = 2
        $ rows = 5


        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"


            for i in range(1, columns * rows + 1):


                button:
                    action FileAction(i)
                    xfill True

                    has hbox


                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Пустой слот."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save tag menu:




    use navigation
    use file_picker

screen load tag menu:




    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text








screen preferences tag menu:




    use navigation


    grid 3 1:
        style_group "prefs"
        xfill True


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Дисплей")
                textbutton _("Окно") action Preference("display", "window")
                textbutton _("Полный экран") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Переходы")
                textbutton _("Все") action Preference("transitions", "all")
                textbutton _("Нет") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Скорость текста")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Джойстик") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Пропустить")
                textbutton _("Просмотренные сообщения") action Preference("skip", "seen")
                textbutton _("Все сообщения") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Начать пропуск") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("После выбора")
                textbutton _("Остановить пропуск") action Preference("after choices", "stop")
                textbutton _("Продолжить пропуск") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Авто-перемотка времени")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Ждать голос") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Громкость музыки")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Громкость звуков")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Тест"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Громкость голоса")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Тест"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0








screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Да") action yes_action
            textbutton _("Нет") action no_action


    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"







screen quick_menu:


    hbox:
        style_group "quick"

        xalign 1.0
        yalign 0.0





        textbutton _("Пропустить") action Skip()

        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Настр.") action ShowMenu('preferences')

init -2:
    style quick_button is default:

        background None
        xpadding 4

    style quick_button_text is default:

        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
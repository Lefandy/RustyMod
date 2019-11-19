label lrm_stats_00:


    if not hat_examined:
        $ hat_examined = True
        show screen chair_02 
        hide screen genie
        $ tt_xpos=-20
        $ tt_ypos=100
        show screen genie_stands_f
        show screen desk
        with Dissolve(0.5)
        m "Хм....."
        m "Эта шляпа выглядит как живая..."
        show screen genie
        hide screen genie_stands_f
        hide screen chair_02 
        hide screen desk
        with Dissolve(0.5)
        jump day_main_menu




    if not day == 1:
        jump lrm_stats



label lrm_stats:
    $ hat_examined = True


    $ par1_add1 = ""
    $ par1_add2 = ""
    $ par1_add3 = ""
    if nsp_germiona_mediawhoring > 0:
        $ par1_add1 = "{size=-6}Медиа-развр.:{/size}{size=-4} [nsp_germiona_mediawhoring]{/size}\n                    {size=-6}{/size}"
    if nsp_germiona_impudence > 0:
        $ par1_add2 = "{size=-6}Наглость:{/size}{size=-4} [nsp_germiona_impudence]{/size}\n                    {size=-6}{/size}"
    if nsp_germiona_artistry > 0:
        $ par1_add3 = "{size=-6}Артистичность:{/size}{size=-4} [nsp_germiona_artistry]{/size}\n                    {size=-6}{/size}"
    if snape_friendship >= 99:
        $ screens.ShowD3("lrm_stats_00", 
        par1="{size=-3}Гермиона{/size}      {size=-6}Развращенность:{/size}"
        "{size=-4} [hermi.whoring]{/size}\n                     {size=-6}Отношение:{/size}"
        "{size=-4} [hermi.liking]{/size}\n                    {size=-6}{/size}"+par1_add1+par1_add2+par1_add3,
        par2="{size=-3}Дафна   {/size}      {size=-6}Развращенность:{/size}"
        "{size=-4} [daphne.whoring]{/size}\n                    {size=-6}Отношение:{/size}"
        "{size=-4} [daphne.liking]{/size}\n                    {size=-6}{/size}",
        par3="{size=-3}Снейп{/size}           {size=-6}Откровенность: {/size}"
        "{size=12}99({color=#FF0000}max{/color}){/size}\n                     {size=-6}Дружба:{/size} {size=-6}[snape_events]{/size}", 
        )
        $ config.allow_skipping = False
        pause
        $ config.allow_skipping = True
        $ screens.HideD3("lrm_stats_00")

        call screen main_menu_01
    else:
        $ screens.ShowD3("lrm_stats_00", 
        par1="{size=-3}Гермиона{/size}      {size=-6}Развращенность:{/size}"
        "{size=-4} [hermi.whoring]{/size}\n                     {size=-6}Отношение:{/size}"
        "{size=-4} [hermi.liking]{/size}\n                    {size=-6}{/size}"+par1_add1+par1_add2+par1_add3,
        par2="{size=-3}Дафна   {/size}      {size=-6}Развращенность:{/size}"
        "{size=-4} [daphne.whoring]{/size}\n                    {size=-6}Отношение:{/size}"
        "{size=-4} [daphne.liking]{/size}\n                    {size=-6}{/size}",
        par3="{size=-3}Снейп{/size}          {size=-6}Откровенность: {/size}"
        "{size=-4}[snape_friendship]{/size}\n                     {size=-6}Дружба:{/size} {size=-6}[snape_events]{/size}",
        )





        $ config.allow_skipping = False
        pause
        $ config.allow_skipping = True
        $ screens.HideD3("lrm_stats_00")


        call screen main_menu_01

screen lrm_stats_00(par1, par2, par3):
    zorder 4

    add "03_hp/11_misc/lrm_stats.png" at Position(xpos=200, ypos=30)

    hbox:
        spacing 40 xpos 260 ypos 100 xmaximum 350
        text par1

    hbox:
        spacing 40 xpos 260 ypos 200 xmaximum 350
        text par2

    hbox:
        spacing 40 xpos 260 ypos 300 xmaximum 350
        text par3

screen lrm_hat:
    add "03_hp/05_props/00_lrm_hat.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
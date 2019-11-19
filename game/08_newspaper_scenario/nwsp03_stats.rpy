
label newsp_stats_00:

    $ nsp_newspaper_qual_text=""
    $ nsp_genie_typographic_text=""
    $ nsp_genie_writer_text=""
    $ nsp_genie_photocamera_text=""

    $ nsp_newspaper_qual = (10 * (1 + nsp_genie_writer) * (1 + nsp_genie_typographic)) + (5 * nsp_genie_photocamera)

    if nsp_newspaper_qual >= 0:
        $ nsp_newspaper_qual_text = tr("никакое")
    if nsp_newspaper_qual >= 20:
        $ nsp_newspaper_qual_text = tr("плохое")
    if nsp_newspaper_qual >= 60:
        $ nsp_newspaper_qual_text = tr("ниже среднего")
    if nsp_newspaper_qual >= 150:
        $ nsp_newspaper_qual_text = tr("среднее")
    if nsp_newspaper_qual >= 240:
        $ nsp_newspaper_qual_text = tr("выше среднего")
    if nsp_newspaper_qual >= 400:
        $ nsp_newspaper_qual_text = tr("хорошее")
    if nsp_newspaper_qual >= 540:
        $ nsp_newspaper_qual_text = tr("отличное")
    if nsp_newspaper_qual >= 770:
        $ nsp_newspaper_qual_text = tr("шедевр")

    if nsp_genie_typographic == 0:
        $ nsp_genie_typographic_text = tr("рукописный листок")
    if nsp_genie_typographic == 1:
        $ nsp_genie_typographic_text = tr("плохо напечатано")
    if nsp_genie_typographic == 2:
        $ nsp_genie_typographic_text = tr("напечатано")
    if nsp_genie_typographic == 3:
        $ nsp_genie_typographic_text = tr("хорошо напечатано")
    if nsp_genie_typographic == 4:
        $ nsp_genie_typographic_text = tr("глянец")
    if nsp_genie_typographic == 5:
        $ nsp_genie_typographic_text = tr("яркий глянец")
    if nsp_genie_typographic == 6:
        $ nsp_genie_typographic_text = tr("сияющий глянец")

    if nsp_genie_writer == 0:
        $ nsp_genie_writer_text = tr("никакое")
    if nsp_genie_writer == 1:
        $ nsp_genie_writer_text = tr("начинающий")
    if nsp_genie_writer == 2:
        $ nsp_genie_writer_text = tr("слабый любитель")
    if nsp_genie_writer == 3:
        $ nsp_genie_writer_text = tr("любитель")
    if nsp_genie_writer == 4:
        $ nsp_genie_writer_text = tr("хороший любитель")
    if nsp_genie_writer == 5:
        $ nsp_genie_writer_text = tr("продвинутый любитель")
    if nsp_genie_writer == 6:
        $ nsp_genie_writer_text = tr("начинающий профессионал")
    if nsp_genie_writer == 7:
        $ nsp_genie_writer_text = tr("слабый профессионал")
    if nsp_genie_writer == 8:
        $ nsp_genie_writer_text = tr("профессионал")
    if nsp_genie_writer == 9:
        $ nsp_genie_writer_text = tr("сильный профессионал")
    if nsp_genie_writer == 10:
        $ nsp_genie_writer_text = tr("шедевр пера")

    if nsp_genie_photocamera == 0:
        $ nsp_genie_photocamera_text = tr("нет")
    if nsp_genie_photocamera == 1:
        $ nsp_genie_photocamera_text = tr("ч/б орнаменты")
    if nsp_genie_photocamera == 2:
        $ nsp_genie_photocamera_text = tr("цветные орнаменты")
    if nsp_genie_photocamera == 3:
        $ nsp_genie_photocamera_text = tr("псевдо-3д орнаменты")
    if nsp_genie_photocamera == 4:
        $ nsp_genie_photocamera_text = tr("движущиеся орнаменты")


    $ screens.ShowD3("newsp_stats_00", 
    par1=tr("{size=-3}ИНФОРМАЦИЯ о ГАЗЕТЕ{/size}") + "\n\n" +
    tr("{size=-4} Итоговое качество газеты :\n") +str(nsp_newspaper_qual)+ " " +str(nsp_newspaper_qual_text)+ "{/size}\n" +
    tr("{size=-4} Качество печати газеты:\n") +str(nsp_genie_typographic)+ " " +str(nsp_genie_typographic_text)+ "{/size}\n" +
    tr("{size=-4} Качество статей газеты:\n") +str(nsp_genie_writer)+ " " +str(nsp_genie_writer_text)+ "{/size}\n" +
    tr("{size=-4} Качество украшений газеты:\n") +str(nsp_genie_photocamera)+ " " +str(nsp_genie_photocamera_text)+ "{/size}\n" +
    tr("{size=-4} Бонусный контент:\n") +str(nsp_newspaper_bonus_text)+ "{/size}\n" +
    tr("{size=-4} Качество бонусного контента:\n") +str(nsp_newspaper_bonus_point)+ "{/size}\n" +
    tr("{size=-4} Прошлая награда:\n") +str(nsp_newspaper_last_money)+ "{/size}\n",
        )



    $ config.allow_skipping = False
    pause
    $ config.allow_skipping = True
    $ screens.HideD3("newsp_stats_00")


    call screen main_menu_01



screen newsp_stats_00(par1):
    zorder 4

    add "03_hp/11_misc/lrm_stats.png" at Position(xpos=200, ypos=30)

    hbox:
        spacing 40 xpos 260 ypos 100 xmaximum 350
        text par1

label nsp_snape_dialog_stat:

    $ nsp_txt_add = ""

    $ screens.Hide("snape_main")
    $ snape.State("door").Visibility("body")

    if nsp_newspaper_qual_last >= 770:
        $ nsp_txt_add = tr("великолепное глянцевое издание")
    elif nsp_newspaper_qual_last >= 240:
        $ nsp_txt_add = tr("хорошо оформленное издание")
    elif nsp_newspaper_qual_last >= 60:
        $ nsp_txt_add = tr("скромное издание")
    else:
        $ nsp_txt_add = tr("жалко выглядящее издание")


    if nsp_newspaper_bonus_point_last >= 15000:
        if one_out_of_three == 1:
            $ snape ("~28//" + tr("Сегодня я видел в главном зале огромную толпу учеников, которая разглядывала наше ") +str(nsp_txt_add)+ ".")
            $ snape ("~21//Профессор Мак-Гонагалл с трудом навела порядок, а разглядев газету поближе густо покраснела.")
            $ snape ("~02//Анонимность - это круто !")
        elif one_out_of_three == 2:
            $ snape ("~23//" + tr("Ученики украдкой бегают с уроков посмотреть на наше ") +str(nsp_txt_add)+ ".")
            $ snape ("~02//Я уже не говорю о переменах.")
            $ snape ("~20//На сегодняшнем сдвоенном зельеварении было восемь случаев сексуальных домогательств между учениками прямо в классе.")
        else:
            $ snape ("~03//" + tr("Сегодня Филч и профессор Флитвик дежурили возле стенда, на котором висит наше ") +str(nsp_txt_add)+ ".")
            $ snape ("~28//Но ученики освоили новую тактику, пока один отвлекает, остальные пользуются моментом.")
            $ snape ("~20//А еще, по Хогвартсу тайно распространяются уменьшенные копии гезатных материалов.")
            $ snape ("~22//Я и сам раздоб... то есть конфисковал парочку.")

    elif nsp_newspaper_bonus_point_last >= 5000:
        if one_out_of_three == 1:
            $ snape ("~10//Многие ученики постоянно крутятся у стенда.")
            $ snape ("~02//" + tr("Думаю, они уже готовы на все, лишь бы перечитать наше ") +str(nsp_txt_add)+ ".")
            $ snape ("~28//Похоже, профессора понемногу тоже привыкают.")
        elif one_out_of_three == 2:
            $ snape ("~23//Ученики, и особенно ученицы, стали заметно распутнее.")
            $ snape ("~24//" + tr("На них явно действует наше ") +str(nsp_txt_add)+ ".")
            $ snape ("~28//Хорошо, что эту газету не видят их родители.")
        else:
            $ snape ("~01//" + tr("Сегодня Минерва пыталась удалить наше ") +str(nsp_txt_add)+ ".")
            $ snape ("~28//Но листы надежно защищены заклинанием Альбуса.")
            $ snape ("~23//Мне уже трудно вспомнить, почему издание газеты могло казаться скучным.")

    elif nsp_newspaper_bonus_point_last >= 1000:
        if one_out_of_three == 1:
            $ snape ("~24//" + tr("Некоторое количество учеников каждый день читает наше ") +str(nsp_txt_add)+ ".")
            $ snape ("~09//Похоже моя идея про секс-материалы работает.")
            $ snape ("~23//И это не удивляет.")
        elif one_out_of_three == 2:
            $ snape ("~02//Ученики на уроках выглядят более возбужденными.")
            $ snape ("~13//Да и на моих \"личных\" ученицах это сказывается в лучшую сторону.")
        else:
            $ snape ("~03//" + tr("Наше ") +str(nsp_txt_add)+ tr(" пока что не очень интересно для мужской аудитории, но у него большой потенциал."))
    else:


        $ snape ("~04//" + tr("У нас ") +str(nsp_txt_add)+ tr(", да, именно ") +str(nsp_txt_add)+ tr(". Формально."))
        $ snape ("~06//А когда будут выполнятся мои советы относительно дополнительных материалов, его даже могут начать читать другие люди.")

    $ screens.Hide("snape_02", "bld1", d3 )
    $ snape.Visibility(transition=d3)

    show screen snape_main

    jump snape_ready

label nsp_hermione_dialog_status:

    if nsp_newspaper_qual_last >= 770:
        $ nsp_txt_add = tr("Сэр, газета прекрасно оформлена и может служить образцом для других !")
    elif nsp_newspaper_qual_last >= 240:
        $ nsp_txt_add = tr("Сэр, газета хорошо оформлена и смотрится просто здорово.")
    elif nsp_newspaper_qual_last >= 60:
        $ nsp_txt_add = tr("Сэр, газета оформлена более-менее нормально, но могла бы быть и лучше.")
    else:
        $ nsp_txt_add = tr("Сэр, газета выглядит просто ужасно, если вы хотите мое мнение. Я утешаю себя тем, что это просто разминка.")


    if nsp_newspaper_bonus_point_last >= 15000:
        if one_out_of_three == 1:
            $ herView.hideshowQQ( "body_33.png", pos )
            her "Сэр, по всей школе обсуждают нашу газету. Может это и хорошо для соревнования, но нормально ли ?"
            $ herView.hideshowQQ( "body_34.png", pos )
            her "Я хочу сказать, неужели и во всех остальных школах происходит то же самое ? Трудно поверить."
        elif one_out_of_three == 2:
            $ herView.hideshowQQ( "body_50.png", pos )
            her "Если хотите знать мое мнение, логичнее было открыть борд... в смысле класс сексуального образования, чем выставлять меня напоказ перед всей школой."
            $ herView.hideshowQQ( "body_57.png", pos )
            her "А как же моя гордость ?"
            her "Так, крепись, Гермиона, все ради победы школы."
        else:
            $ herView.hideshowQQ( "body_02.png", pos )
            her "Сэр, в школе появился фан-клуб {size=+4}газеты{/size}!"
            $ herView.hideshowQQ( "body_33.png", pos )
            her "Многие считают авторов героями за то, что вы их не можете найти."
            her "Если бы они только знали... Нет, хорошо, что они не знают, а то я бы сошла с ума."

    elif nsp_newspaper_bonus_point_last >= 5000:
        if one_out_of_three == 1:
            $ herView.hideshowQQ( "body_34.png", pos )
            her "Профессор, скажите, неужели газета с самого начала задумывалась именно в таком виде ?"
            $ herView.hideshowQQ( "body_50.png", pos )
            her "Теперь я целый день чувствую смущение после каждой публикации."
        elif one_out_of_three == 2:
            $ herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $ herView.hideshowQQ( "body_04.png", pos )
            her "Многие ученики пытаются вычислить, кто работает в редакции. Надеюсь, этого не произойдет."
            $ herView.hideshowQQ( "body_08.png", pos )
            her "Иначе моя жизнь уже никогда не станет прежней."
        else:
            $ herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $ herView.hideshowQQ( "body_12.png", pos )
            her "Я не понимаю, кем нужно быть, чтобы постоянно изучать наши материалы. А ведь многие это делают."
            $ herView.hideshowQQ( "body_34.png", pos )
            her "А самое ужасное, что после публикации и я не могу удержаться. Уф."

    elif nsp_newspaper_bonus_point_last >= 1000:
        if one_out_of_three == 1:
            $ herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $ herView.hideshowQQ( "body_12.png", pos )
            her "И еще, меня смущают особые материалы, которые вы разместили в центре."
            $ herView.hideshowQQ( "body_24.png", pos )
            her "Я не думала, что это будет так... так... так откровенно !"
        elif one_out_of_three == 2:
            $ herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $ herView.hideshowQQ( "body_28.png", pos )
            her "Но я хотела бы спросить, вы уверены, что публикация таких материалов допустимо ?"
            m "Неужели ты стыдишься своей же журналистской деятельности ?"
            $ herView.hideshowQQ( "body_33.png", pos )
            her "Вовсе нет !"
            her "Я просто... просто переживаю за результат межшкольного соревнования !"
            m "Какого еще межшко... А, ну да ! Ты об {size=+3}этом{/size} соревновании."
        else:
            $ herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $ herView.hideshowQQ( "body_50.png", pos )
            her "Но, среди учеников теперь ходят разные сплетни по поводу редакции. Наверное, я не буду их пересказывать."
            $ herView.hideshowQQ( "body_13.png", pos )
            her "Хорошо, никто не знает, что я работаю на вас."
    else:


        $ herView.hideshowQQ( "body_01.png", pos )
        $ renpy.say(her, tr(nsp_txt_add) + "\n" + tr("А еще не хватает чего-нибудь интересного, что могло бы издалека заинтересовать читателя."))

    $ herView.hideshowQQ( "body_01.png", pos )
    jump hermione_main_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
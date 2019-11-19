label snape_tutor_1:
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 
    show screen fireplace_fire
    hide screen genie
    hide screen chair
    hide screen desk
    show screen desk

    hide screen snape_02 
    hide screen bld1
    hide screen snape_main
    with d3


    with fade
    $ fire_in_fireplace = True

    show screen bld1
    with d3
    m "... кстати говоря, о девчонке Грейнджер..."
    $ s_head_xpos = 330
    $ s_head_ypos = 380
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    show screen s_head2      
    sna2 "..."
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    show screen s_head2 
    sna2 "А ведь вечер обещал быть приятным..."
    sna2 "Что она устроила в этот раз?"
    hide screen s_head2
    m "Боюсь, я не смогу обучать ее."
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    show screen s_head2
    sna2 "Ха! Теперь-то ты меня понимаешь!"
    sna2 "Держу пари, ты не продержался и десяти минут."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    show screen s_head2
    sna2 "Хотя я могу тебя понять. И даже немного сочувствую..."
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
    show screen s_head2
    sna2 "Черт, у нее завтра опять \"защита от темных искусств\"."
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"
    show screen s_head2
    sna2 "Налей мне еще."
    hide screen s_head2
    m "Я не говорил, что сдаюсь."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    show screen s_head2
    sna2 "Хм?"
    hide screen s_head2
    m "Проблема в том, что я ничему не могу ее научить."
    m "Знаю, я и так не должен учить ее ничему путному."
    m "Но я по крайней мере должен делать вид, что занимаюсь с ней чем-то полезным."
    m "Боюсь, что трюк с зябликом дважды не сработает."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    show screen s_head2
    sna2 "\"Трюк с зябликом\"?"
    hide screen s_head2
    m "... ты не хочешь об этом знать, поверь мне."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    show screen s_head2
    sna2 "Хм."
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    show screen s_head2
    sna2 "В общем, ты ведешь к тому, чтобы я стал твоим репетитором?"
    hide screen s_head2
    m "Послушай, я сам от этого не в восторге."
    m "Но если я буду обучать ее, то это намного упростит нашу с тобой задачу."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    show screen s_head2
    sna2 "Да понял я, понял."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    show screen s_head2
    sna2 "Хммм..."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen s_head2
    sna2 "Однако мы можем пойти другим путем."
    hide screen s_head2
    m "Каким, интересно?"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen s_head2
    sna2 "Ботанойдное зелье."
    hide screen s_head2
    m "..."
    g4 "Ты назвал меня ботаником?"
    g4 "ТЫ, МАТЬ ТВОЮ, НАЗВАЛ МЕНЯ БОТАНИКОМ??!"
    g4 "ДА, Я НОСИЛ ОЧКИ, И ПОСТОЯННО СИДЕЛ ЗА КНИГАМИ, НО ЭТО НЕ ПОВОД ЗВАТЬ МЕНЯ \"БОТАНОМ\"!!!"
    g4 "И ГДЕ ТЕПЕРЬ ТЕ КАЧКИ, ЧТО ТАСКАЛИ МЕНЯ ЗА ПОДВЯЗКИ?! ДЕРЖУ ПАРИ, ВЫЛИЗЫВАЮТ АНУС КАКОЙ-НИБУДЬ ЖИРНОЙ ЖЕНУШКЕ СУЛТАНА!"
    g4 "А ТО И САМОМУ СУЛТАНУ!"
    g4 "А Я В ЭТО ВРЕМЯ ПЕРДОЛЮ ВО ВСЕ ДЫРЫ ЧЕРТОВУ ПРИНЦЕССУ АГРАБЫ!!!"
    g4 "И КТО ТЕПЕРЬ ИЗ НАС НЕУДАЧНИК, А??!"
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    show screen s_head2
    sna2 "..."
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    show screen s_head2
    sna2 "..."
    hide screen s_head2
    m ".. ты сказал {i}запретное слово{/i}?"
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    show screen s_head2
    sna2 "\"Запретное слово\"?"
    hide screen s_head2
    m "Да, на букву \"б\"."
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    show screen s_head2
    sna2 "А, ты про..."
    hide screen s_head2
    g4 "ЗАТКНИСЬ!!!"
    m "Есть шрамы, которые не заживают даже спустя девять тысяч лет."
    m "Просто не упоминай {i}это{/i} слово вслух, и мы поладим, договорились?"
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    show screen s_head2
    sna2 "Знаешь, а звучит забавно."
    hide screen s_head2
    g4 "Убью."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen s_head2
    sna2 "Ладно-ладно, не серчай. Не говорить слово на букву \"б\", ясно."
    hide screen s_head2
    m "Вот и славно. Так о чем мы там говорили?"
    $ s_sprite = "03_hp/10_snape_main/snape_23.png"
    show screen s_head2
    sna2 "В общем, есть... зелье, которое может тебе помочь."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen s_head2
    sna2 "Просто выпей его - и сможешь выучить всю школьную программу за ночь"
    hide screen s_head2
    g9 "Звучит читерски."
    m "Какой вообще смысл во всей этой школе, если все можно выучить буквально за ночь?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    show screen s_head2
    sna2 "Ну, во-первых, большинство ингредиентов очень редки и на них нужна чертова куча денег."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    show screen s_head2
    sna2 "Во-вторых, процесс варки чертовски сложен."
    sna2 "Ну, и в третьих, сам рецепт известен далеко не каждому."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna2 "Посуди сам - если все узнают об этом рецепте, то никому не будут нужны школы, а это море потерянных денег."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna2 "В сущности, почти вся экономика магов держится на волшебных школах."
    hide screen s_head2
    m "Ладно-ладно, я понял. Большие шишки не хотят, чтобы это зелье стало популярным."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen s_head2
    sna2 "Именно."
    hide screen s_head2
    m "Так все что мне нужно, так это купить ингредиенты, так?"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    show screen s_head2
    sna2 "Точно."
    hide screen s_head2
    m "Прелесть. Как будто в этой игре было мало гринда."
    m "И во сколько мне обойдется эта радость?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    show screen s_head2
    sna2 "Ну... Некоторые из ингредиентов запрещены, так что мне прийдется привлечь свои каналы..."
    $ s_sprite = "03_hp/10_snape_main/snape_23.png"
    sna2 "Так что, думаю, тысяч десять."
    show screen s_head2
    m "..."
    m "Ты накинул себе пару тысяч, да?"
    $ s_sprite = "03_hp/10_snape_main/snape_30.png"
    show screen s_head2
    sna "Да как ты мог такое подумать?!"
    $ s_sprite = "03_hp/10_snape_main/snape_27.png"
    show screen s_head2
    sna2 "Мы же друзья..."
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_27.png"
    show screen s_head2
    sna2 "..."
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    show screen s_head2
    sna2 "Ладно, восемь тысяч."
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    show screen s_head2
    sna2 "Послушай, больше я скинуть никак не могу."
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"
    show screen s_head2
    sna "..."
    hide screen s_head2
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    show screen s_head2
    sna2 "Семь тысяч. Мое последнее слово."
    hide screen s_head2
    g9 "Шикарно! Договорились."
    "Задание обновлено! Нагриндить семь тысяч галеонов для Снейпа."
    m "Только это все равно чертовски здоровая куча золота."
    g9 "Думаю, мне стоит поискать работенку на стороне."
    g9 "Поговаривают, что жиголо неплохо зарабатывают..."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    show screen s_head2
    sna2 "Тебе нельзя покидать эту комнату и тебя никто не должен видеть, помнишь?"
    m "..."
    m "Зануда."
    hide screen s_head2
    $ teacher_jinn_quest = 2
    stop music fadeout 1.0
    $ menu_x = 0.5
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    $ snape_busy = True
    hide screen snape_02 
    hide screen bld1
    hide screen snape_main
    with d3
    $ renpy.play('sounds/door.mp3')
    hide screen desk
    jump day_start

label snape_tutor_2:

    g9 "Вот золотишко за учебники."
    $ renpy.play('sounds/money.mp3')
    hide screen points
    $ gold -=7000
    show screen points
    "Вы отдали Снейпу 7000 галеонов."
    hide screen snape_main                                                                                                                   
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen snape_main  
    with d3
    sna "Отлично! Я немедленно займусь всеми приготовлениями."
    hide screen snape_main                                                                                                                   
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    show screen snape_main
    with d3
    sna "Варка зелья такого уровня занимает чертовски много сил и времени..."
    hide screen snape_main                                                                                                                   
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    show screen snape_main  
    with d3
    sna "И оно очень быстро портится. Так что держи книги наготове."
    m "... книги?"
    hide screen snape_main                                                                                                                   
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    show screen snape_main  
    with d3
    sna "Ну да. Учебники."
    m "А разве ты не собирался их мне одолжить по старой дружбе?"
    sna "С чего ты решил, что они у меня есть?"
    m "Эм, ну..."
    g4 "Черт."
    hide screen snape_main                                                                                                                   
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    show screen snape_main  
    with d3
    sna "Даже если у меня и завалялась пара-тройка старых учебников по зельеварению, этого все равно будет недостаточно."
    m "Тогда есть идеи, где их достать?"
    sna "Ну, обычно в таких случаях идут в Косой переулок, но..."
    m "Но?"
    hide screen snape_main                                                                                                                   
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with d3
    sna "Но я слишком занят, а тебе нельзя покидать башню."
    m "А как насчет отправить мисс Грейнджер таскать мешки с книгами, пока мы будем попивать вино у камина?"
    hide screen snape_main                                                                                                                   
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    show screen snape_main
    with d3
    sna "Не выйдет. Косой переулок достаточно далеко, а трансгрессировать на территории Хогвартса невозможно."
    g9 "Не так уж это и плохо. Трансвестирование никогда не было хорошей идеей, поверь мне на слово."
    hide screen snape_main                                                                                                                   
    with d3
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    show screen snape_main  
    with d3
    sna "..?"
    m "В общем, я постараюсь что-нибудь придумать."
    "Квест обновлен: нужно достать учебники"
    sna "Ну что же, тогда удачи."
    $ screens.Hide("snape_main")
    $ teacher_jinn_quest = 3
    $ snape_busy = True
    hide screen snape_02 
    hide screen bld1
    hide screen snape_main
    with d3
    $ renpy.play('sounds/door.mp3')
    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
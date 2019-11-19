label snape_chitchat:
    $ this.RunStep("CHITCHAT")


    $ one_of_ten = renpy.random.randint(1, 10)


    if hermi.whoring >= 0 and hermi.whoring <= 2:
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты действительно думаешь что сделаешь это?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты действительно думаешь, что сломаешь девчонку?"

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты тоже ненавидишь эту мерзкую солнечную погоду?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Хотел бы я, чтобы дождь шел круглые сутки..."

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Знаешь, меня одолевают сомнения относительно нашего плана..."

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты уверен, что ты не Альбус Дамблдор?"
            sna "Иногда мне всё еще трудно в это поверить..."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Однажды я убил ученика."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Да... Я задушил недомерка своими руками."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "........*Негромко рычит*."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Это звучало правдоподобно?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Когда эти животные перестанут меня боятся, мне конец."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Вселять страх в сердца студентов это важная задача учителей."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Эти ничтожества Уизли..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_07.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Однажды я просто не выдержу, Богом клянусь!"

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Эта совиная почта нелепа, разве не так?"
            sna "Я бы предпочёл использовать воронов."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "У меня был худший день в моей жизни..."
            sna "Так что у меня нет настроения разговаривать..."

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Быть волшебником это значит работать 24 часа в сутки..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "7 дней в неделю..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "365 дней в году."
            sna "И без отпуска..."

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Квиддич..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Что за бессмысленная трата ресурсов!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3





    if hermi.whoring >= 3 and hermi.whoring <= 5:
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я не замечаю никаких изменений в поведение мисс Грейнджер..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты уверен, что знаешь, что ты делаешь?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я чувствую власть, награждая факультеты очками или отнимая их когда захочу."
            sna "Мой авторитет среди студентов растёт с каждым днём..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "И когда я говорю \"авторитет\" я имею в виду \"страх\"."

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты знал что полная луна влияет на мужскую силу?"
            sna "Она также помогает сосредоточится на деле, делает тебя более собраным."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Но кого это волнует, верно?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Мои драгоценные Слизеринки делают эту пытку стоящей..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Их юбки становятся короче с каждой неделей, честно."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Было время когда я был молод и полон надежды..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ха-ха... я просто шучу, приятель"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я никогда не был полон надежды..."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Дуэли - это одна из моих сильных сторон, ну ты понимаешь..."

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Хех, \"Движение за права мужчин\"...?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Что дальше? Ассоциация по освобождению эльфов?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Как может лучший студент быть таким глупым?"

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "У меня нет любимчиков среди моих студентов."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я просто терплю некоторых и ненавижу остальных."

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В Хогвартсе есть четыре факультета..."
            sna "Слизерин, Когтевран, Гриффиндор и..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "...и Хафф-что-то..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Всем без разницы."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Мётлы для детей и ведьм."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты никогда не увидишь, чтобы уважающий себя колдун летал на метле."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3










    if hermi.whoring >= 6 and hermi.whoring <= 8:
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Есть ли прогресс в обработке нашей Мисс Всезнайки?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Однажды девченка продала мне свои трусы за пять очков факультета."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Самое главное, что она была очень рада этому..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Думаю, она отдала бы их и бесплатно, лишь бы задобрить меня."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я думаю, это очень хорошее начало дня..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Спорим, ты не думал, что я это скажу?"

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Квиддич с годами становится все популярнее..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Как это печально..."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Моя жизнь была скучна до твоего появления..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "А теперь она..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "...менее печальна."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Сожалеть? Я не знаю значения этого слова!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я живу очень интересной жизнью."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ха-ха-ха! Прости, я просто не могу спокойно произнести это."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "На занятиях ты не можешь ошибиться."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Один промах и эти чертовы ублюдки разорвут тебя на части."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты - единственный человек перед кем я отвечаю..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Так что теперь я могу делать практически всё что угодно..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "..............."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Так вот что такое свобода, да?"

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Осень... самое грустное время года..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Обожаю его!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В моей комнате висит магический портрет стриптизерши."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Одна из моих драгоценных вещей."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3












    if hermi.whoring >= 9 and hermi.whoring <= 11:
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В последнее время мисс Грейнджер стала очень агрессивной..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Надеюсь, ты знаешь, что делаешь..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Меня не должна мучать совесть после секса с моими студентами, верно?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Если бы ты видел какую форму носят некоторые из этих девченок..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Они просто напрашиваются на ЭТО."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_12.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В последнее время дождь льет чаще..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Думаю мне нравится такая погода, потому что она делает других печальнее..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Мои последние наблюдения показывают, что 9 из 10 девочек мечтают, что бы их соблазнил учитель."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я так же уверен, что десятая - это Гермиона Грейнджер ."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В такие дни мне нужно стараться, чтобы быть в плохом настроение."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "У тебя есть пара лишних презервативов?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "У меня была полная пачка..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "...они кончились год назад..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Мне нравится, как ты изменил мою жизнь, приятель."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Думаешь, мы сможем превратить Хогвартс в школу \"только для девочек\" ?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Академия девочек Хогвартс!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Это было бы идеально... не считая Локхарта."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Почему учитель перешел дорогу?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Чтобы сбежать от студентов!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ха-ха-ха! Шутка на все времена!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Хочешь услышать забавную историю?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ну, я не знаю таких..."

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты знаешь что такое \"Королевский Кубок\" ?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты знаешь, верно?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3










    if hermi.whoring >= 12 and hermi.whoring <= 14:
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "15 очков за работу ртом справедливо, верно?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты был когда нибудь влюблен, приятель?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты был когда нибудь влюблен в школьницу?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "А как на счет сразу нескольких?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_20.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_20.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Прошлой ночью между мной и одной из Слизеринских шлюх произошло что-то невероятное."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Вкратце, все мои мышцы болят и я чуствую себя опустошенным..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В последнее время становится холоднее..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Зима близко..."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты когда нибудь видел как магловские женщины одеваются в ведьм?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Так восхитительно."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты знаешь что такое \"Интернет\" ?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Он позволяет тебе \" быть внутри сети \" и смотреть магические фотографии голых женщин маглов."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Жаль, что у нас нет этого в Хогвартсе."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В моей жизни есть два влечения..."
            sna "Темные искуства..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_12.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "......"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "...и шлюхи."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты думаешь, я не смогу отказаться от выпивки?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ведь моя жизнь наполнена стрессом..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Хм..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я могу попробовать отказаться от нее..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_21.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Взамен на дикий секс с моими студентками!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Мисс Грейнджер в последнее время притихла..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я уверен, она замышляет что-то..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Написать книгу и убить почти всех персонажей ради драматической сцены очень легко..."
            sna "Но поставить своих персонажей в невыгодное положение и помочь им выжить звучит убедительнее..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Сейчас {size=+7}это{/size} настоящее мастерство."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3










    if hermi.whoring >= 15 and hermi.whoring <= 17:
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_11.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "А что если не мы играем с девченкой, а она с нами?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Слышал ли ты о \"Слизневом клубе\"?"
            sna "Что если я сам сделаю клуб?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я назову его \"Клуб Снейпа\"!"
            sna "Я бы пригласил туда девченок, предложил бы им чай и кексики..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Полапал бы их немного..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Гениально!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Скажи мне, Джинни... тебе когда нибудь вылизывала зад молодая ведьмочка?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_21.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Незабываемые ощущения, скажу я тебе..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Итак, как продвигается обучение?"
            sna "Все по плану, надеюсь?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты знаешь... Я вижу Фестралов."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты знаешь, что я люблю в Квиддиче?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_15.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ничего! Абсолютно ничего!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Хогвартс сильно вознесся с твоим приходом."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "И когда я говорю \"Хогвартс\", я имею в виду \"Себя\"."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Настоящие волшебники носят черное."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ведь так?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Некоторые девочки Слизерина восхищаются мной..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я бы предпочел, чтобы меня боялись..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Но, я думаю, с этим тоже всё в порядке..."

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В последнее время ты слишком щедр с очками Гриффиндора, приятель."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я почти не успеваю за тобой..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"
            show screen snape_main                                                                                                                  
            with d3






    if hermi.whoring >= 18 and hermi.whoring <= 20:
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Мисс Грейнджер меняется. И это становится заметно..."
            sna "Ее оценки идут вниз и даже поведение стало далеко от идеала..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Но несмотря на это, она все еще заноза в моей заднице!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Мой самый не любимый цвет?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_07.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Их два. Красный и золотой."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я слышал что тема вампиров популярна среди девочек."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Из меня получился бы отличный вампир?"
            sna "Может, я куплю пару фальшивых клыков..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_21.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Просто, что бы завести этих сумасшедших шлюх."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я ...ненавижу свою жизнь."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Нет, постой, перефразирую..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_17.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я ...ненавижу свою жизнь."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Блин! Я пытаюсь сказать \"люблю\" но у меня не получается..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я не думаю, что я когда либо использовал слова \"Люблю\" и \"Жизнь\" в одном предложение."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Попробую снова..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я не... лю... люблю свою жизнь!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Отлично, я люблю свою жизнь..."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Солнце, шоколад, квиддич, кошки и апельсиновый сок..."
            sna "Это список вещей, которые я не люблю..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "А теперь короткий список того что люблю..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Темные искуства, вино и девочки."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты видел колдунов в кулачной драке?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Просто отвратительно!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "То чувство, когда ты кончил студентке в рот, а она произносит: \"Спасибо, профессор\"."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Оно великолепно, правда?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Как думаешь, призраки Хогвартса подглядывают за девочками в душе?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Если бы я был призраком, я бы так и делал."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Однажды девчонка поведала мне, что хочет быть изнасилованной этим сквибом Мистером Филтчем."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Думаю, мне стоит это устроить. Что думаешь?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я привык ненавидеть свою работу..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ненависть чиста, проста и уверенна..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03png"
            show screen snape_main                                                                                                                  
            with d3
            sna "А теперь, не пойми меня неправильно - я все еще ненавижу ее."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Но также я теперь люблю ее..."
            sna "Как не делать этого? Особенно с тем что происходит в последнее время?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ненавидеть и любить в равных пропорциях..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Это как влюбится снова..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3


    if hermi.whoring >= 21:
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты знаешь что такое \"буккакэ\", а?"
            sna "А как насчет \"глубокого заглота\"?"
            sna "Так же есть \"изнасилование\"."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Что за дети пошли, приятель..."
            sna "У них есть клички для всего."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Так или иначе \"изнасилование\" было всегда..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "В мои дни мы называли его просто \"секс\"."

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Приятель, мой член готов к \"Воспитание принцессы золотое издание\"!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "*Кашель!* Я имел в виду, Слизерин рулит, я ненавижу Гриффиндор и так далее..."

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Недавно я устроил вечеринку..."
            sna "Одна девочка и три парня..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Они насиловали ее, а я смотрел..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "........................."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ты думаешь я слишком поддался своей темной стороне?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "У меня кончились все презервативы, приятель."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Подкинешь пару?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я тайно варю зелье, которое заставляет течь женскую грудь..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Великолепно, да?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Итак, эта ведьма взяла мой член в свой рот, верно?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Ее горячие подружки занимались моим задом..."
            sna "В это время третья девченка ждала меня на коленях с открытым ртом, ожидая что я сейчас кончу..."
            sna "Каждый раз когда я извергался, она говорила: \"Благодарю вас, профессор Снейп\"."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Это был очень выматывающий вечер..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Одна из девченок меня приследует и умоляет, что бы я мочился ей в рот..."
            sna "Настойчивая маленькая шлюха..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Может, мне помочь ей?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я одинаково доминирую над всеми студентами..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Но у меня к каждому свой подход."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Я люблю свою жизнь!"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Но все еще ненавижу свою работу..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Если бы я только мог забросить преподавание, но продолжать веселится..."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/24.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Мне почти стыдно за мои похождения."
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"
            show screen snape_main                                                                                                                  
            with d3
            sna "Хочешь, пришлю тебе пару шлюх?"
            hide screen snape_main                                                                                                                   
            with d3
            $ s_sprite = "03_hp/10_snape_main/23.png"
            show screen snape_main                                                                                                                  
            with d3










    jump snape_nothing































label chitchat_event_01:
    hide screen snape_main
    with d3
    $ sna_head_state = 1
    sna_head_main "Итак..."
    sna_head_main "Я слышал что мисс Грейнджер начала заниматься с тобой наедине?"
    m "Да, так и есть..."
    m "Хотя не уверен, что это входит в наш план."
    $ sna_head_state = 9
    sna_head_main "О чем ты? Все идет отлично."
    sna_head_main "Я лично и пара учителей делаем ее занятия невыносимыми!"
    sna_head_main "И в результате она стала заниматься больше..."
    sna_head_main "Теперь вот берет частные уроки..."
    $ sna_head_state = 18
    sna_head_main "И значит у нее все меньше и меньше времени докучать мне!"
    m "Понятно..."
    $ sna_head_state = 10
    sna_head_main "И еще... Ты, конечно и сам знаешь,... но просто на всякий случай..."
    sna_head_main "Не учи ее ничему полезному, ладно?"
    m "Я постараюсь."
    $ sna_head_state = 1
    sna_head_main "Ладно, на сегодня всё..."





    hide screen bld1
    with d3
    $ walk_xpos=360
    $ walk_xpos2=610
    $ snapes_speed = 03.0
    show screen snape_walk_01_f 
    pause 3
    $ renpy.play('sounds/door.mp3')
    hide screen snape_walk_01_f 
    with d3

    $ chitchat_event_01_happened = True
    $ snape_busy = True
    $ days_without_an_event = 0

    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1


    $ this.chitchat_event_01.Finalize()

    jump day_main_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
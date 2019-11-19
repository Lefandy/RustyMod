label hp:
    stop music fadeout 1









    show screen blkfade

    show expression "03_hp/01_bg/00.png"
    pause.1
    scene blkfade
    show expression "03_hp/01_bg/00.png"
    hide blkfade with Dissolve(.3)
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    hide screen blkfade
    show magic5
    pause.05
    scene white
    pause.05
    pause.05
    scene white
    pause.05
    show expression "03_hp/01_bg/00.png"
    show whitefade at basicfade, center


    show magic3 at basicfade3, center

    hide magic
    hide magic2
    hide magic3
    hide magic4

    show heal
    stop music fadeout 1
    pause 1
    hide whitefade
    with d3
    pause 1








$ day = 0





$ cal_new_year = False
$ cal_month = 9
$ cal_day = 13









$ circled_days = [[0],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []]









$ starred_days = [[0],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []]

















$ cal_notes = [[(0,"")],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []]


















$ important_dates = {
    'four_seasons':[(9,22,"Autumn"),(12,21,"Winter"),(3,20,"Spring"),(6,21,"Summer")],
    'term_dates':[(9,1,"Autumn term"),(12,19),(1,15,"Winter term"),(4,2),(4,15,"Spring term"),(6,26)],
    'holiday_dates':[(12,20,"Christmas holidays"),(1,14),(4,3,"Easter holidays"),(4,14),(6,27,"Summer holidays"),(8,31)],
    'OWL_dates':[(6,10),(6,21)],
    'hogsmeade_weekends':[(9,23),(10,15),(11,4),(11,26),(12,16),(2,4),(2,24),(3,17),(5,4),(5,26),(6,15)],
    'dumblegenies_arrival':[(9,14)],
    'hermiones_periods':[(9,18),(10,16),(11,13),(12,11),(1,8),(2,5),(3,4),(4,1),(4,29),(5,27),(6,24),(7,22),(8,19)],
    'ball_dates':[(9,30,"Autumn Ball"),(12,16,"Yule Ball"),(3,30,"Spring Fling"),(6,22,"Prom")] }



$ known_dates = {
    'OWL_dates':False,
    'hogsmeade_weekends':False,
    'hermiones_periods':False,
    'ball_dates':False }



$ travel_fire = False


$ floo_travel_known = True
$ hogsmeade_known = True
$ inv_floo_powder = 1
$ Hermione_here = False




$ day_of_week = 0
$ report_chapters = 0
$ finished_report = 0
$ total_report = 0

$ got_mail = False
$ got_package = False
$ got_paycheck = False
$ mail_from_her = False
$ letter_text = []
$ letters = 0



$ nsp_genie_typographic = 0
$ nsp_genie_typographic_exp = 0
$ nsp_genie_writer = 0
$ nsp_genie_photocamera = 0
$ nsp_genie_photocamera_exp = 3
$ nsp_genie_sphere = False
$ nsp_genie_sphere_level = 0
$ nsp_genie_sphere_level_exp = 0
$ nsp_genie_sphere_ruby_level = 0
$ nsp_genie_sphere_diamond_level = 0
$ nsp_genie_sphere_sapphire_level = 0
$ nsp_genie_sphere_video = False

$ nsp_genie_sphere_diamond_req = 0

$ nsp_genie_sphere_ruby_level_eff = 0
$ nsp_genie_sphere_diamond_level_eff = 0
$ nsp_genie_sphere_sapphire_level_eff = 0

$ nsp_germiona_mediawhoring = 0
$ nsp_germiona_impudence = 0
$ nsp_germiona_artistry = 0

$ nsp_newspaper_bonus_text = tr("нет")
$ nsp_newspaper_bonus_point = 0
$ nsp_newspaper_bonus_base = 0
$ nsp_newspaper_bonus_text_base = 0
$ nsp_newspaper_bonus_point_last = 0
$ nsp_newspaper_qual_last = 0
$ nsp_newspaper_last_money = 0

$ nsp_newspaper_qual = 10
$ nsp_newspaper_cur_money = 10
$ nsp_newspaper_published = False
$ nsp_newspaper_published_mail = False

$ nsp_newspaper_articles = 0
$ nsp_newspaper_ready = False

$ nsp_pre_jobs_max = 0

$ nsp_germiona_menu_rights = 1
$ nsp_germiona_menu_magls = 1
$ nsp_germiona_menu_kviddich = 1
$ nsp_germiona_menu_sex = 1
$ nsp_germiona_menu_maniac = 1
$ nsp_germiona_menu_nude = 1
$ nsp_germiona_menu_forest = 1
$ nsp_germiona_menu_studio = 1


$ nsp_event_rights_1 = 0
$ nsp_event_rights_2 = 0
$ nsp_event_rights_3 = 0
$ nsp_event_rights_4 = 0
$ nsp_event_rights_5 = 0

$ nsp_event_magls_1 = 0
$ nsp_event_magls_2 = 0
$ nsp_event_magls_3 = 0
$ nsp_event_magls_4 = 0
$ nsp_event_magls_5 = 0

$ nsp_event_kviddich_1 = 0
$ nsp_event_kviddich_2 = 0
$ nsp_event_kviddich_3 = 0
$ nsp_event_kviddich_4 = 0
$ nsp_event_kviddich_5 = 0
$ nsp_event_kviddich_6 = 0

$ nsp_event_sex_1 = 0
$ nsp_event_sex_2 = 0
$ nsp_event_sex_3 = 0
$ nsp_event_sex_4 = 0
$ nsp_event_sex_5 = 0

$ nsp_event_maniac_1 = 0
$ nsp_event_maniac_2 = 0
$ nsp_event_maniac_3 = 0

$ nsp_event_nude_1 = 0
$ nsp_event_nude_2 = 0
$ nsp_event_nude_3 = 0
$ nsp_event_nude_4 = 0
$ nsp_event_nude_5 = 0

$ nsp_event_forest_1 = 0
$ nsp_event_forest_2 = 0

$ nsp_event_studio_1 = 0
$ nsp_event_studio_2 = 0
$ nsp_event_studio_3 = 0
$ nsp_event_studio_4 = 0
$ nsp_event_studio_5 = 0
$ nsp_event_studio_6 = 0



$ nsp_day = 0
$ nsp_day_letter7 = 0

$ nsp_letter_1 = 0
$ nsp_letter_2 = 0
$ nsp_letter_3 = 0
$ nsp_letter_4 = 0
$ nsp_letter_5 = 0
$ nsp_letter_6 = 0
$ nsp_letter_7 = 0
$ nsp_letter_8 = 0
$ nsp_letter_9 = 0
$ nsp_letter_10 = 0
$ nsp_letter_11 = 0
$ nsp_letter_12 = 0
$ nsp_letter_13 = 0

$ nsp_pre_letter = 0
$ nsp_pre_snape = 0
$ nsp_pre_dahre = 0
$ nsp_newspaper_menu = 0

$ hermione_out_halfday = 0





$ wrd_new_items = 0

$ wrd_tits = 0
$ wrd_tits_no = 1


$ wrd_skirt = 1
$ wrd_shortskirt = 0
$ wrd_xshortskirt = 0
$ wrd_xxshortskirt = 0
$ wrd_xsmallskirt = 0
$ wrd_xxsmallskirt = 0
$ wrd_xxxsmallskirt = 0
$ wrd_skirt_cheerleader = 0
$ wrd_skirt_business = 0


$ wrd_standart01 = 1
$ wrd_standart02 = 0
$ wrd_standart03 = 0
$ wrd_standart04 = 0
$ wrd_standart05 = 0
$ wrd_skimpyshirt = 0
$ wrd_shirt_cheerleader = 0
$ wrd_shirt_business = 0


$ wrd_badge_01 = 0


$ wrd_nets = 0
$ wrd_tights = 0



$ wrd_rent_happy_schoolgirl = 0
$ wrd_rent_playful_schoolgirl = 0
$ wrd_rent_cheerleader = 0
$ wrd_rent_business = 0

$ wrd_nopanties_dialog = False



$ pnx_stage = 0



$ luna_stage = 0



$ night_acc_stage = 0


$ letter_from_hermione_02 = False
$ letter_from_ficbook_fun = False


$ snape_busy = False
$ snape_friendship = 0
$ snape_events = 0




$ hermione_takes_classes = False
$ hermione_sleeping = False



$ tutoring_events = 0
$ knowledge = 0

$ teachers_pet = 0
$ classmates_pet = 0
$ being_mean = 0

$ currentBook=None
$ item=None


$ dates = 0




$ chitchat_event_01_happened = False
$ chitchat_event_02_happened = False
$ chitchat_event_03_happened = False
$ chitchat_event_04_happened = False
$ chitchat_event_05_happened = False
$ chitchat_event_06_happened = False
$ chitchat_event_07_happened = False








$ hold_all_the_events_please = False
$ jerk_off_session = False

$ tutoring_offer_made = False










$ phoenix_is_feed = False
$ fire_in_fireplace = False
$ hat_act = False







$ have_catalogue = False



$ gifts12 = []




$ imagination = 1
$ concentration = 0
$ speedwriting = 0
$ job_lvl = 1




$ book_07_units = 0
$ book_07_complete = False
$ book07 = "\"Моя дорогая вайфу\""
$ shea = 0
$ shea_waifu = False
$ complited_shea_already = False

$ victoria = 0
$ victoria_waifu = False
$ complited_stevens_already = False

$ leena = 0
$ leena_waifu = False
$ complited_leena_already = False
$ waifu_book_completed = False








$ s_reading_lvl = 0




$ order_placed = False

$ days_in_delivery2 = 0
$ package_is_here = False




$ request_01 = 0

$ request_02_b_points = 0
$ request_02_c_points = 0



$ request_06_points = 0
$ request_07_points = 0

$ request_09_points = 0
$ request_10_points = 0
$ request_11_points = 0

$ request_15_points = 0
$ request_16_points = 0
$ request_17_points = 0

$ request_19_points = 0
$ request_20_points = 0
$ request_21_points = 0

$ request_23_points = 0
$ request_24_points = 0
$ request_25_points = 0
$ request_26_points = 0
$ request_27_points = 0
$ request_28_points = 0

$ request_30_points = 0

$ request_32_points = 0



$ request_02_b = False
$ request_02_c = False
$ request_03 = False
$ request_05 = False
$ request_06 = False
$ request_10 = False
$ request_13 = False
$ request_15 = False
$ request_20 = False
$ request_21 = False
$ request_23 = False
$ request_24 = False
$ request_25 = False
$ request_26 = False
$ request_27 = False
$ request_28 = False
$ request_30 = False
$ request_32 = False
$ request_33 = False



$ desk_examined = False
$ cupboard_examined = False
$ bird_examined = False
$ door_examined = False
$ fireplace_examined = False
$ hat_examined = False

$ dap_ending = 0
$ pho_ending = 0

if this.event_05._finish2==4:
    $ day = 4
    $ desk_examined = True
    $ cupboard_examined = True
    $ bird_examined = True
    $ door_examined = True
    $ fireplace_examined = True
    $ hat_examined = True
    $ rum_times = 4
$ report_talk = False


$ zyablik_switch = 0




screen statistics:
    hbox:
        spacing 10 xpos 630 ypos 20
        text "{size=-3}День: [day]\nРаспутство: [whoring]\nУровень: [level]\nЗнания: [knowledge]\nСлизерин: [slytherin]\nГриффиндор: [gryffindor]\nДружба со Снейпом: [snape_friendship]\nДень недели: [day_of_week]\nКонцентрация: [concentration]\nСкорописание: [speedwriting]{/size}"





label day_start:






    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 


$ chitchated_with_her = False
$ chitchated_with_snape = False

$ hermione_main_zorder = 5
$ gifted = False
$ searched = False



$ menu_x = 0.5


$ only_upper = False
$ autograph = False
$ no_blinking = False
$ sperm_on_tits = False
$ aftersperm = False

$ phoenix_is_feed = False
$ only_upper = False
$ hat_act = False

stop bg_sounds 
stop weather 

hide screen blkfade
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
hide screen bld1 
hide screen desk



























if hermi.whoring >= 12 and not touched_by_boy:
    $ lock_public_favors = True



$ generating_snape_bonus = renpy.random.randint(1, 2)
$ generating_points = renpy.random.randint(1, 2)
$ generating_points_gryffindor = renpy.random.randint(1, 10)
$ generating_points_hufflepuff = renpy.random.randint(1, 10)
$ generating_points_ravenclaw = renpy.random.randint(1, 10)

$ one_out_of_three = renpy.random.randint(1, 3)
$ i_of_iv = renpy.random.randint(1, 4)
$ one_of_five = renpy.random.randint(1, 5)
$ i_of_vii = renpy.random.randint(1, 7)
$ one_of_ten = renpy.random.randint(1, 10)
$ one_of_tw = renpy.random.randint(1, 20)



$ gold1 = renpy.random.randint(1, 10)
$ gold2 = renpy.random.randint(10, 40)
$ gold3 = renpy.random.randint(20, 50)
$ gold4 = renpy.random.randint(30, 90)



$ daytime = True
$ hermione_sleeping = False
$ hermione_takes_classes = False
$ snape_busy = False
$ fire_in_fireplace = False
$ hat_act = False
hide screen fireplace_fire


$ days_without_an_event +=1

if letters < 0:
    $ letters = 0


if day_of_week >= 7:
    $ day_of_week = 0
    if finished_report >= 1:
        $ got_paycheck = True
        $ letters += 1

$ day_of_week += 1



$ hermi.liking += 1
$ daphne.liking += 1




if nsp_pre_jobs_max < finished_report:
    $ nsp_pre_jobs_max = finished_report

if nsp_newspaper_menu >= 6:
    $ nsp_day += 1
    $ nsp_day_letter7 += 1

if nsp_letter_7 == 3:
    $ nsp_letter_7 = 0


if nsp_letter_7 == 2:
    $ nsp_letter_7 = 0

if nsp_letter_7 == 1:
    $ nsp_letter_7 = 2


if order_placed:
    $ days_in_delivery2 -=1
    if days_in_delivery2 <= 0:
        $ package_is_here = True
        $ order_placed = False



scene black

$ raining = False
hide screen new_window 
hide screen cloud 


$ wather_generator = renpy.random.randint(1, 100)

if wather_generator >= 81 and wather_generator <= 90:

    $ raining = True
    show expression "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
elif wather_generator >= 1 and wather_generator <= 40:
    show screen new_window 

elif wather_generator >= 41 and wather_generator <= 60:
    show screen new_window 
    show screen cloud 


elif wather_generator >= 61 and wather_generator <= 80:
    show expression "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
elif wather_generator >= 91 and wather_generator <= 100:

    $ raining = True
    show expression "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")







hide screen room_night 
show screen room 

hide screen krk
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
hide screen with_snape 
hide screen with_snape_animated 
if package_is_here:
    hide screen package

show screen krk
show screen door
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01
show screen candle_02



if day == 2:
    $ letter_from_hermione_02 = True
    $ letters += 1

if day == 12:
    $ work_unlock = True
    $ letters += 1



if day > 20 and ((nsp_pre_jobs_max >= 4 and nsp_pre_letter < 1) or (nsp_pre_letter == 1 and letters == 0)):
    $ nsp_pre_letter = 1
    $ letters += 1

if nsp_newspaper_published_mail == False and nsp_newspaper_published == True:
    $ nsp_newspaper_published_mail = True
    $ letters += 1

if nsp_day == 10:
    $ nsp_letter_1 = 1
    $ letters += 1
















if letters <= 0:
    $ nsp_newspaper_published = False
    $ nsp_newspaper_published_mail = False
    $ got_paycheck = False




if package_is_here:
    play sound "sounds/owl.mp3"  
    show screen package
show screen genie

if total_report >= 10 and letter_from_ficbook_fun == False:
    $ letters+=1

if this.IsStep("MAIL"):
    $ letters+=1
if got_mail or mail_from_her or letters >= 1:
    play sound "sounds/owl.mp3"  
    show screen owl







hide screen points
show screen points

with fade

$ day +=1



$ increment_cal_date()





if wrd_rent_happy_schoolgirl == 1:
    ">С мягким шелестом форма веселой школьницы рассыпалась в пыль."

if wrd_rent_playful_schoolgirl == 1:
    ">С мягким шелестом форма игривой школьницы рассыпалась в пыль."

if wrd_rent_cheerleader == 1:
    ">С мягким шелестом форма болельщицы Гриффиндора рассыпалась в пыль."

if wrd_rent_business == 1:
    ">С мягким шелестом одежда бизнес-леди рассыпалась в пыль."

$ wrd_rent_happy_schoolgirl = 0
$ wrd_rent_playful_schoolgirl = 0
$ wrd_rent_cheerleader = 0
$ wrd_rent_business = 0





if night_acc_stage == 1:
    m "Уф, какой ужасный сон."
    m "Даже вспоминать не хочется."
    g9 "А Гермионе действительно пошел бы черный..."
    m "Нет, стоп, лучше вообще не думать об этом."

    $ night_acc_stage = 2
elif night_acc_stage == 3:
    g1 "А-а-а-а-а-а-а."
    g1 "Мой вообра... Не-е-е-е-т. Стоп."
    m "Это был сон. Да, именно сон. Но я проверю. Так-с."

    hide screen genie
    show screen genie_jerking_off

    g6 "Кажется все в порядке, хотя настроения нет."

    hide screen genie_jerking_off
    show screen genie

    $ night_acc_stage = 4
elif night_acc_stage == 5:

    m "Прекрасное утро. Не помню, что снилось, кажется снова что-то странное."
    g9 "Но почему-то сегодня у меня превосходное настроение. Пора браться за дело."

    $ night_acc_stage = 6


if nsp_newspaper_menu == 8:
    jump nsp_snape_dialog3

$ hermione_out_halfday -= 1

if hermione_out_halfday <= 0:
    $ hermione_out_halfday = 0
    $ this.RunStep("DAY")






label day_main_menu:


if phoenix_is_feed:
    show screen phoenix_food



if day == 1 and daytime and bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined and hat_examined:
    show screen bld1
    with d3
    m "Уже темнеет..."
    m "Я просто проведу остаток дня в этой комнате?"
    hide screen bld1
    with d3
    jump night_start



show screen animation_feather
call screen main_menu_01






label night_start:
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 





$ daytime = False
$ snape_busy = False
$ hermione_takes_classes = False
$ chitchated_with_snape = False
$ chitchated_with_her = False
$ gifted = False
$ hat_act = False

stop bg_sounds 
stop weather 

scene black

hide screen blkfade
hide screen notes 
hide screen done_reading 
hide screen done_reading_02 
hide screen new_window 
hide screen cloud 

hide screen lightening 

if wather_generator >= 81 and wather_generator <= 90:
    show expression "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
elif wather_generator >= 1 and wather_generator <= 30:
    show expression "03_hp/07_weather/night_sky.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")

elif wather_generator >= 41 and wather_generator <= 50:
    show expression "03_hp/07_weather/night_sky.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")

elif wather_generator >= 31 and wather_generator <= 40:
    show expression "03_hp/07_weather/night_sky_02.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")

elif wather_generator >= 51 and wather_generator <= 60:
    show screen cloud_night_01
    show screen cloud_night_02
    show screen cloud_night_03
    show expression "03_hp/07_weather/night_sky_02.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")

elif wather_generator >= 61 and wather_generator <= 80:
    show expression "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")

elif wather_generator >= 91 and wather_generator <= 100:
    show expression "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")





if package_is_here:
    hide screen package
hide screen room 
show screen room_night 
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
hide screen krk

show screen krk
show screen door
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01
show screen candlefire_01 
show screen candle_02
show screen candlefire_02 
if package_is_here:
    show screen package
show screen genie




hide screen points
show screen points

if got_mail or mail_from_her or letters >= 1:
    show screen owl
with fade





call points_changes
call points_changes_gryffindor



















$ hermione_out_halfday -= 1

if hermione_out_halfday <= 0:
    $ hermione_out_halfday = 0
    $ this.RunStep("NIGHT")






label night_main_menu:


if phoenix_is_feed:
    show screen phoenix_food

show screen animation_feather
call screen main_menu_01


pause
show ch_hem 01 at Position(xpos=732, ypos=350, xanchor="center", yanchor="center")
pause


show ch_hem walk_01 at Move((732, 350), (300, 350), 5.0,
                  xanchor="center", yanchor="center") with Dissolve(.1)
pause 5.0

show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
pause

show ch_hem run_f at Move((300, 350), (732, 350), 2.0,
                  xanchor="center", yanchor="center") with Dissolve(.1)

pause 2.0

show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
pause












init -2:

    $ l_blush = False
    $ l_things = False
    $ l_question = False
    $ l_drop = False
    $ l_hearts = False
    $ l_exclamation = False
    $ l_tears = False

    $ config.autoreload = False











    transform cloud_move:
        xpos 408
        choice:
            ypos 150
        choice:
            ypos 160
        choice:
            ypos 170
        choice:
            ypos 190
        choice:
            ypos 200

        linear 15.0 xpos 50
        pause 7
        repeat


    transform cloud_night_move_01:
        xpos 408
        choice:
            ypos 130
        choice:
            ypos 150
        choice:
            ypos 150
        linear 30.0 xpos 50
        pause 2
        repeat

    transform cloud_night_move_02:
        xpos 408
        choice:
            ypos 150
        choice:
            ypos 170
        linear 70.0 xpos 50
        pause 2
        repeat

    transform cloud_night_move_03:
        xpos 408
        ypos 160
        linear 50.0 xpos 50
        pause 2
        repeat

    label assmenu:
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
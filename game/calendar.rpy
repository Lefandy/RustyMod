


init -2 python:





















    month_info = [(0,0,0,0,"",""),
        (31,2,20,5,"Jan","January"),
        (29,5,18,4,"Feb","February"),
        (31,6,19,5,"Mar","March"),
        (30,2,17,4,"Apr","April"),
        (31,4,17,3,"May","May"),
        (30,7,16,1,"Jun","June"),
        (31,2,15,1,"Jul","July"),
        (31,5,14,28,"Aug","August"),
        (30,6,24,9,"Sep","September"),
        (31,1,24,8,"Oct","October"),
        (30,4,22,7,"Nov","November"),
        (31,6,22,7,"Dec","December")]










    week_info = [("",""),
        ("Sun","Sunday"),
        ("Mon","Monday"),
        ("Tue","Tuesday"),
        ("Wed","Wednesday"),
        ("Thu","Thursday"),
        ("Fri","Friday"),
        ("Sat","Saturday")]



    weekends = [[0],
        [6,7,13,14,20,21,27,28],
        [3,4,10,11,17,18,24,25],
        [2,3,9,10,16,17,23,24,30,31],
        [6,7,13,14,20,21,27,28],
        [4,5,11,12,18,19,25,26],
        [1,2,8,9,15,16,22,23,29,30],
        [6,7,13,14,20,21,27,28],
        [3,4,10,11,17,18,24,25],
        [2,3,9,10,16,17,23,24,30],
        [1,7,8,14,15,21,22,28,29],
        [4,5,11,12,18,19,25,26],
        [2,3,9,10,16,17,23,24,30,31]]























    holidays = [[0],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
        [],
        [],
        [3,4,5,6,7,8,9,10,11,12,13,14],
        [],
        [27,28,29,30],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [],
        [],
        [],
        [20,21,22,23,24,25,26,27,28,29,30,31]]





    def increment_cal_date():
        global cal_new_year
        global cal_month
        global cal_day
        
        cal_day += 1
        
        if cal_day > month_info[cal_month][0]:
            cal_month += 1
            cal_day = 1
        
        if cal_month > 12:
            cal_new_year = True
            cal_month = 1
        
        
        if cal_month == 9 and cal_new_year:
            cal_new_year = False













    def add_cal_notes(dates, note):
        note = "cal_note_" + note
        
        for x in range(len(dates)):
            month = dates[x][0]
            day = dates[x][1]
            cal_notes[month].append((day, note))





    def add_circled_days(dates):
        for x in range(len(dates)):
            month = dates[x][0]
            day = dates[x][1]
            circled_days[month].append(day)





    def add_starred_days(dates):
        for x in range(len(dates)):
            month = dates[x][0]
            day = dates[x][1]
            starred_days[month].append(day)







    def dates_of_day(month, day):
        list = []
        
        query_month = build_month(month)
        
        for x in range(len(query_month)):
            if (query_month[x][day-1] != 0):
                list.append((month, query_month[x][day-1]))
        
        return list









    def day_of_date(date):
        curr_month = date[0]
        curr_day = date[1]
        
        list = []
        
        query_month = build_month(curr_month)
        
        for x in range(len(query_month)):
            if curr_day in query_month[x]:
                for y in range(len(query_month[x])):
                    if query_month[x][y] == curr_day:
                        return (y + 1)








    def date_finder(date, days):
        curr_month = date[0]
        curr_day = date[1]
        
        if days == 0:
            return date
        elif days < 0:
            for x in range(days*-1):
                curr_day -= 1
                if curr_day < 1:
                    curr_month -= 1
                    if curr_month < 1:
                        curr_month = 12
                    curr_day = month_info[curr_month][0]
            return (curr_month, curr_day)
        else:
            for x in range(days):
                curr_day += 1
                if curr_day > month_info[curr_month][0]:
                    curr_month += 1
                    if curr_month > 12:
                        curr_month = 1
                    curr_day = 1
            return (curr_month, curr_day)
















    def day_count_forwards(start_date, end_date):
        start_month = start_date[0]
        start_day = start_date[1]
        end_month = end_date[0]
        end_day = end_date[1]
        
        count = 0
        
        if (start_month == end_month) and (start_day == end_day):
            return 0
        
        while (start_month != end_month) or (start_day != end_day):
            start_day += 1
            count += 1
            if start_day > month_info[start_month][0]:
                start_month +=1
                if start_month > 12:
                    start_month = 1
                start_day = 1
        
        return count
















    def day_count_backwards(start_date, end_date):
        start_month = start_date[0]
        start_day = start_date[1]
        end_month = end_date[0]
        end_day = end_date[1]
        
        count = 0
        
        if (start_month == end_month) and (start_day == end_day):
            return 0
        
        while (start_month != end_month) or (start_day != end_day):
            start_day -= 1
            count += 1
            if start_day < 1:
                start_month -=1
                if start_month < 1:
                    start_month = 12
                start_day = month_info[start_month][0]
        
        return count









    def day_to_date():
        for x in range(day):
            increment_cal_date()



    def cal_pos(col, row):
        origin_xpos, origin_ypos = 192, 208
        spacing_x, spacing_y = 60, 50
        return origin_xpos + spacing_x*(col-1), origin_ypos + spacing_y*(row-1)






    def build_month(month):
        matrix = [[],
                  [],
                  [],
                  [],
                  [],
                  []]
        
        curr_row = 0
        curr_col = 0
        curr_day = 1
        spaces_filled = 0
        
        
        for x in range(month_info[month][1] - 1):
            matrix[curr_row].append(0)
            curr_col += 1
            spaces_filled += 1
        
        
        for y in range(month_info[month][0]):
            if curr_col == 7:
                curr_row += 1
                curr_col = 0
            
            matrix[curr_row].append(curr_day)
            curr_col += 1
            curr_day += 1
            spaces_filled += 1
        
        
        
        
        for z in range(42-spaces_filled):
            if curr_col == 7:
                curr_row += 1
                curr_col = 0
            
            matrix[curr_row].append(0)
            curr_col += 1
        
        return matrix

label calendar:
    $ cal_browsing_month = cal_month
    $ cal_browsing_new_year = cal_new_year

    show screen bld1
    with Dissolve(.3)
    call screen calendar

label calendar_cleanup:
    hide screen bld1
    with Dissolve(.3)
    jump day_main_menu

label calendar_decrement:
    if cal_browsing_month == 1:
        $ cal_browsing_month = 12
        $ cal_browsing_new_year = False
    else:
        $ cal_browsing_month -= 1
    call screen calendar

label calendar_increment:
    if cal_browsing_month == 12:
        $ cal_browsing_month = 1
        $ cal_browsing_new_year = True
    else:
        $ cal_browsing_month += 1
    call screen calendar
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
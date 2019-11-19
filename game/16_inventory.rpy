label inventory:
    menu:
        "- Книги -":
            if "book_01" in books:
                menu:
                    "- Читать книгу # 1 -" if book_01_units <= 19:
                        pass
                    "- Читать книгу # 1 (Завершить) -" if book_01_units == 20:
                        ">Вы уже прочитали ее."

            "У вас нет ни одной книги."
            jump inventory
        "- Подарки -":
            pass
        "- Ничего -":
            jump cupboard
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
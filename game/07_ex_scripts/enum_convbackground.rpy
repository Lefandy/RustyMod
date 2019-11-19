init -1 python:
    CONVERSATION_BG_DIRECTOR = '10_new_game/graph/bg_conversation/director_room.png'
    CONVERSATION_BG_DIRECTOR_NIGHT = '10_new_game/graph/bg_conversation/director_room_night.png'

screen ConversationBGScreen(BgImageArray, BgPos):
    add BgImageArray[_ConversationBGScreenIndex] at BgPos
    zorder _ConversationBGScreenZOrder

init -999 python:
    _ConversationBGScreenIndex = 0
    _ConversationBGScreenZOrder = 0    
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
label _custom_hide_windows_label:
    python:

        config.context_clear_layers = _custom_hide_windows_get()

        _custom_hide_windows_set([])

        sl = renpy.game.context().scene_lists







        somethingRemoved = True
        while(somethingRemoved):
            somethingRemoved = False
            foundTag = None
            for el in sl.layers['screens']:
                if _custom_hide_windows_remove_condition(el):
                    del sl.at_list['screens'][el.tag]
                    sl.layers['screens'].remove(el)
                    somethingRemoved = True
                    break






    $ result = renpy.call_screen("_custom_hide_windows_block_screen")

    return


init -1 python:

    def _custom_hide_dialogue_prepare():
        
        config.underlay[0].keymap['hide_windows'] = _custom_hide_windows_func
        
        
        
        
        
        
        
        
        
        
        return


    def _custom_hide_windows_func():
        
        if renpy.context()._menu:
            return
        
        
        _custom_hide_windows_set(config.context_clear_layers)
        
        config.context_clear_layers = []
        
        renpy.call_in_new_context("_custom_hide_windows_label")
        return


    def _custom_hide_windows_set(aList):
        setattr(renpy.store, '_custom_hide_windows_clear_layers', aList)
        return

    def _custom_hide_windows_get():
        return getattr(renpy.store, '_custom_hide_windows_clear_layers', [])



    def _custom_hide_windows_remove_condition(el):
        return (el.tag == 'say') or (el.tag == 'head') or (el.tag == 'choice')\
        or (el.tag == '_ctc') or (el.tag == 'display') or ('CharacterExView_head' in el.tag)\
        or ('CustomHideWindows_' in el.tag)








screen _custom_hide_windows_block_screen tag _custom_hide_windows_block_screen:
    zorder 1500
    modal True



    for i in config.keymap.values():
        for ll in i:
            if (not 'mousedown' in ll):
                key ll action Return(0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
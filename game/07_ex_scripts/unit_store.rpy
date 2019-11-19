label after_load:



    if not hasattr(renpy.store,'day'):
        $ day = 0
    if not hasattr(renpy.store,'desk_examined'):
        $ desk_examined = False
    if not hasattr(renpy.store,'cal_new_year'):
        $ cal_new_year = False
    if not hasattr(renpy.store,'cal_month'):
        $ cal_month = 9
    if not hasattr(renpy.store,'cal_day'):
        $ cal_day = 13
        if day > 0:
            $ day_to_date()
    if not hasattr(renpy.store,'important_dates'):
        $ important_dates = {
            'four_seasons':[(9,22,"Autumn"),(12,21,"Winter"),(3,20,"Spring"),(6,21,"Summer")],
            'term_dates':[(9,1,"Autumn term"),(12,19),(1,15,"Winter term"),(4,2),(4,15,"Spring term"),(6,26)],
            'holiday_dates':[(12,20,"Christmas holidays"),(1,14),(4,3,"Easter holidays"),(4,14),(6,27,"Summer holidays"),(8,31)],
            'OWL_dates':[(6,10),(6,21)],
            'hogsmeade_weekends':[(9,23),(10,15),(11,4),(11,26),(12,16),(2,4),(2,24),(3,17),(5,4),(5,26),(6,15)],
            'dumblegenies_arrival':[(9,14)],
            'hermiones_periods':[(9,18),(10,16),(11,13),(12,11),(1,8),(2,5),(3,4),(4,1),(4,29),(5,27),(6,24),(7,22),(8,19)],
            'ball_dates':[(9,30,"Autumn Ball"),(12,16,"Yule Ball"),(3,30,"Spring Fling"),(6,22,"Prom")] }
    if not hasattr(renpy.store,'known_dates'):
        $ known_dates = {
            'OWL_dates':False,
            'hogsmeade_weekends':False,
            'hermiones_periods':False,
            'ball_dates':False }
        if desk_examined:
            $ known_dates['hogsmeade_weekends'] = True
    if not hasattr(renpy.store,'circled_days'):
        $ circled_days = [[0],[],[],[],[],[],[],[],[],[],[],[],[]]
    if not hasattr(renpy.store,'starred_days'):
        $ starred_days = [[0],[],[],[],[],[],[],[],[],[],[],[],[]]
    if not hasattr(renpy.store,'cal_notes'):
        $ cal_notes = [[(0,"")],[],[],[],[],[],[],[],[],[],[],[],[]]
        if desk_examined:
            $ dates_list = important_dates['hogsmeade_weekends']
            $ add_cal_notes(dates_list, 'hogsmeade_weekends')






    python:
        InitEntriesFields()


    return

label start_elog:


    python:
        global elog
        global labelHistory
        global jumpHistory

    $ elog=dict()
    $ labelHistory=[]
    $ jumpHistory=[]

    return

init -999 python:

    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')



    def IsStoreKey(key):
        return key in elog

    def IsStoreSubKey(key, subkey):
        if IsStoreKey(key):
            return subkey in elog[key]
        return False

    def SetStoreValue(key, subkey, value):
        
        if not IsStoreKey(key):
            elog.update({key: dict()})
        
        _m1_unit_Store__SetStoreValue_oldvalue=GetStoreValue(key, subkey)
        
        if not IsStoreSubKey(key, subkey):
            elog[key].update({subkey: value})
        else:
            elog[key][subkey]=value
        OnChangeStoreValue(key, subkey, _m1_unit_Store__SetStoreValue_oldvalue, value) 


    def GetStoreValue(key, subkey):
        if IsStoreKey(key):
            
            pass
        else:
            debug.SaveString("GetStoreValue("+str(key)+", "+str(subkey)+")=НЕТ КЛЮЧА!", 3)
        
        return elog[key].get(subkey)

    def GetStoreAllSubKeys(key):
        res=[]
        for s in elog:
            if s==key:
                for subkey in elog[s]:
                    res.append(subkey)
                return res
        return res





    def IsArrayKey(key):
        return key in arr

    def IsArraySubKey(key, subkey):
        if IsArrayKey(key):
            return subkey in arr[key]
        return False

    def SetArrayValue(key, subkey, value):
        
        if not IsArrayKey(key):
            arr.update({key: dict()})
        if not IsArraySubKey(key, subkey):
            arr[key].update({subkey: value})
        else:
            arr[key][subkey]=value


    def GetArrayValue(key, subkey):
        
        return arr[key].get(subkey)

    def GetArrayAllSubKeys(key):
        res=[]
        for s in arr:
            if s==key:
                for subkey in arr[s]:
                    
                    res.append(subkey)
                return res
        return res









    def RegEntry(entry):
        entry.handle=len(entries)
        entries.append(entry)
        return entry

    def GetEntry(Name):
        for o in entries:
            if o.Name==Name:
                return o
        return None


    def GetEntriesByType(typeName):
        _m1_unit_Store__set=set()
        for o in entries:
            if o.Type==typeName:
                _m1_unit_Store__set.update({o})
        return _m1_unit_Store__set

    def InitEntryField(entry, subkey):
        exec "entries["+str(entry.handle)+"]._"+subkey+"=entries["+str(entry.handle)+"].GetValue('"+subkey+"')"
        return            

    def InitEntriesFields():
        if hasattr(renpy.store,"elog"): 
            
            if hasattr(renpy.store,"wtevent"):
                if renpy.store.wtevent!=None: 
                    for e in this.List: 
                        if e.Name==renpy.store.wtevent.Name:
                            renpy.store.wtevent=this.GetCall(renpy.store.wtevent.Name)
                            break
            
            for o in entries:   
                for subkey in o.defVals:
                    if not IsStoreSubKey(o.Name, subkey):
                        SetStoreValue(o.Name, subkey,  o.defVals[subkey])
        
        for o in entries: 
            _m1_unit_Store__list=GetStoreAllSubKeys(o.Name)
            for subkey in _m1_unit_Store__list:
                InitEntryField(o, subkey)
            _m1_unit_Store__list=GetArrayAllSubKeys(o.Name)
            for subkey in _m1_unit_Store__list:
                
                if not subkey in ["ready", "done"]:
                    InitEntryField(o, subkey)
        storeInitialized=True


    def OnChangeStoreValue(key, subkey, oldvalue, newvalue):
        _m1_unit_Store__entry=GetEntry(key)        
        if _m1_unit_Store__entry.Type=="Event":
            
            if (_m1_unit_Store__entry.GetValue("members")!=None):
                if ("daphne" in _m1_unit_Store__entry.GetValue("members")) and (subkey=="finishCount") and (newvalue>(0 if oldvalue==None else oldvalue)):
                    if hermi._pointsPerDaphneVisit>0:
                        Say("По вашему соглашению с Гермионой Гриффиндор получает 10 очков")
                        renpy.store.gryffindor+=10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
init -800 python:
    import ntpath


    def wtxml_parseBool( aString ):
        
        return aString in [ '1', 'true', 'True', True ]

    def wtxml_getFileNameFromPath( aPath ):
        filename = ntpath.basename( aPath ).encode( "utf-8" )
        splitted = filename.rsplit( '.', 1 )
        return splitted[0]

    def wtxml_readZOrder( aOrderString, aOrderBase ):
        txt = aOrderString.replace( ' ', '' )   
        tokens = []
        operators = []
        prevPos = 0
        for ind in range( len( txt ) ):
            if txt[ind] == '+' or txt[ind] == '-' or txt[ind] == '*' or txt[ind] == '/':
                param = txt[prevPos:ind]
                prevPos = ind + 1
                tokens.append( param )
                operators.append( txt[ind] )
        if prevPos != 0 and prevPos < len( txt ):
            param = txt[prevPos:len(txt)]
            tokens.append( param )
        if not tokens:
            return aOrderBase.get( txt )
        else:
            
            for ind in range( len( tokens ) ):
                tokens[ind] = aOrderBase.get( tokens[ind] )
            res = tokens[0]
            tokInd = 1
            
            
            for op in operators:
                nextVal = tokens[tokInd]
                if op == '+':
                    res += nextVal
                elif op == '-':
                    res -= nextVal
                elif op == '*':
                    res *= nextVal
                elif op == '/':
                    res //= nextVal
                tokInd += 1
            return res

    def wtxml_readList( aChild, aListToRead ):
        itemList = list( aChild )
        if not itemList:
            aListToRead.append( aChild.text )
        else:    
            for hideItem in itemList:
                aListToRead.append( hideItem.text )


    def wtxml_updateLinker( aCharacterEx ):
        linkerKey = aCharacterEx.mLinkerKey
        
        f = WTXmlLinker.f( linkerKey )
        fPath = f.mDataPath
        f.CLEAR()
        f.read( fPath )
        
        o = WTXmlLinker.o( linkerKey )
        oPath = o.mDataPath
        o.CLEAR()
        o.read( oPath )
        
        i = WTXmlLinker.i( linkerKey )
        iPath = i.mDataPath
        i.CLEAR()
        i.read( iPath, f, o )
        
        s = WTXmlLinker.s( linkerKey )
        sPath = s.mDataPath
        s.CLEAR()
        s.read( sPath, i )
        
        
        p = WTXmlLinker.p( linkerKey )
        sPath = p.mDataPath
        p.CLEAR()
        p.read( sPath )

    def wtxml_updateItems( aCharacterEx ):
        linkerKey = aCharacterEx.mLinkerKey
        keys = aCharacterEx.mItems.keys()
        for key in keys:
            item = aCharacterEx.getItemKey( key )
            if item != None:
                if item.mName:
                    if not item.mIsSubitem:
                        actStyle = item.getStyle()
                        if actStyle == None:
                            actStyle = 'default'
                        
                        newItem = WTXmlLinker.c( linkerKey ).create( item.mName, actStyle )
                        if newItem[0] != None:
                            aCharacterEx.delItemKey( key )
                            aCharacterEx.addItemDirect( key, newItem[0] )

    def wtxml_updateAll( aCharacterEx ):
        wtxml_updateLinker( aCharacterEx )
        wtxml_updateItems( aCharacterEx )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
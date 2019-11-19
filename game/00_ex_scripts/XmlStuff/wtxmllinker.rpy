init -999 python:

    class WTXmlLinker:
        _indF = 0
        _indO = 1
        _indI = 2
        _indS = 3
        _indC = 4
        _indP = 5
        
        _mLinkerDictionary = {}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        @staticmethod
        def prepareCharacterResources( aKey, aZOrderPath, aFolderPath, aItemsRootPath ):
            
            var_OS = CharacterExOrderStorage()
            var_FS = CharacterExFolderStorage()
            var_IS = CharacterExItemStorage()
            var_SS = CharacterExSetStorage()
            var_PS = CharacterExPresetStorage()
            var_creator = CharacterExItemCreator( var_IS, var_SS, aKey )
            
            
            var_OS.read( aZOrderPath + '/zorders.hxml' )
            var_FS.read( aItemsRootPath + '/folders.hxml' )
            var_IS.read( aItemsRootPath + '/items/', var_FS, var_OS )
            var_SS.read( aItemsRootPath + '/sets/', var_IS )
            var_PS.read( aItemsRootPath + '/presets/' )
            
            
            WTXmlLinker._mLinkerDictionary[ aKey ] = [ var_FS, var_OS, var_IS, var_SS, var_creator, var_PS ]
            
            
            execString = (
                    "@staticmethod\n"
                    "def _return_key_{0}():\n"
                    "   return '{0}'\n"
                    "# and add it to the linker class\n"
                    "WTXmlLinker.getLinkerKey_{0} = _return_key_{0}"
                    ).format( aKey )
            exec( execString )
        
        @staticmethod
        def f( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indF ]
            return None
        
        @staticmethod
        def o( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indO ]
            return None
        
        @staticmethod
        def i( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indI ]
            return None
        
        @staticmethod
        def s( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indS ]            
            return None
        
        @staticmethod
        def c( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indC ]            
            return None
        
        @staticmethod
        def p( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indP ]            
            return None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

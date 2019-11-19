init python:


    onLabelExecute = None
    onJumpExecute = None

    def executeUpdatedLabel( self ):
        renpy.ast.next_node(self.next)
        renpy.ast.statement_name("label")
        
        renpy.game.context().mark_seen()
        if onLabelExecute != None:
            onLabelExecute(self.name)
        
        values = renpy.ast.apply_arguments(self.parameters, renpy.store._args, renpy.store._kwargs)
        
        for k, v in values.iteritems():
            renpy.exports.dynamic(k)
            setattr(renpy.store, k, v)
        
        renpy.store._args = None
        renpy.store._kwargs = None
        
        if renpy.config.label_callback:
            renpy.config.label_callback(self.name, renpy.game.context().last_abnormal)    


    def executeUpdatedJump( self ):
        renpy.ast.statement_name("jump")
        
        if onJumpExecute != None:
            onJumpExecute(self.name,self.target,self.expression)
        
        target = self.target
        if self.expression:
            target = renpy.python.py_eval(target)
        
        rv = renpy.game.script.lookup(target)
        renpy.game.context().abnormal = True
        
        renpy.ast.next_node(rv)


    renpy.ast.Label.execute = executeUpdatedLabel
    renpy.ast.Jump.execute = executeUpdatedJump
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
# Moded by Sad Crab
# Unpacked by partizein
# https://pikabu.ru/@HAWKii
from spells.spelltypes import SPELLTYPES

# TODO: Spells should account for talents and other modifiers

class Spell:
    def __init__(self, spell_type):
        self.spell_type = spell_type

class CastSpell(Spell):
    def __init__(self, cast_time):
        super().__init__(SPELLTYPES.CAST)
        self.cast_time = cast_time
        
    def sim(self, haste_percent):
        return self.cast_time / (1 + haste_percent / 100)

class InstantSpell(Spell):
    def __init__(self):
        super().__init__(SPELLTYPES.INSTANT)
        self.BASE_GLOBAL_COOLDOWN = 1.5
    
    def sim(self, haste_percent):
        return self.BASE_GLOBAL_COOLDOWN / (1 + haste_percent / 100)

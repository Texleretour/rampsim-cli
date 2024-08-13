class Sequence(): 
    def __init__(self, sequence): 
        self.sequence = sequence
        
    def sim(self, haste_percent):
        # TODO: Should consider spells cooldowns
        
        time = 0
        
        for spell in self.sequence:
            time += spell.sim(haste_percent)
    
        return round(time, 1)
                
        
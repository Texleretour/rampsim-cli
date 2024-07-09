from sequence import Sequence
from haste import calculate_haste_percent
from spells.classes.druid.restoration import *
from spells.classes.priest.discipline import *

def main():
    # TODO: Add support for mana costs
    
    # ******************************
    
    HASTE_RATING = 1000
    
    SEQUENCE = [
        power_word_radiance,
        power_word_radiance,
        mindbender,
        mindblast,
        penance,
        smite,
        smite,
    ]
    
    # ******************************
    
    sequence = Sequence(SEQUENCE)
    haste_percent = calculate_haste_percent(HASTE_RATING) 
    
    print("############################")
    print("Ramp simulator\n")
    print(f"Haste : {HASTE_RATING} / {haste_percent} %")
    print("Result :", sequence.sim(haste_percent), "seconds")
    
main()
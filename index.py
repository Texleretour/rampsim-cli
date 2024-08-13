from sequence import Sequence
from haste import calculate_haste_percent
from spells.classes.druid.restoration import *
from spells.classes.priest.discipline import *
import toml 

def main():
    # TODO Add support for mana costs
    # Load config file

    with open('config.toml', 'r') as config_file:
        config = toml.load(config_file)
    
    # ******************************
    # TODO Determine Haste from a config file
    HASTE_RATING = config['statistics']['haste']
    
    # TODO Determine the sequence from a txt file
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
    print(f"Haste : {HASTE_RATING} = {haste_percent} %")
    print("Result :", sequence.sim(haste_percent), "seconds")
    
main()
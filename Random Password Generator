from random import choices
from string import ascii_letters, punctuation
from copy import copy

class Password:

    def __init__(self, strength = "mid", length = None):
        self.length = length
        self.strength = strength

    INPUT_UNIVERSE = {
    "letters": list(ascii_letters),
    "symbols": list(punctuation),
    "numbers": list(range(10))
    }

    LENGTHS = {
        "low": 8,
        "mid": 10,
        "high": 16
    }
    
    def generate(self):
        pw = copy(self.INPUT_UNIVERSE["letters"])
        lngth = self.length or self.LENGTHS[self.strength]
        
        if self.strength == "mid":
            pw += self.INPUT_UNIVERSE["numbers"]
        elif self.strength == "high":
            pw += self.INPUT_UNIVERSE["symbols"] + self.INPUT_UNIVERSE["numbers"]

        return "".join(map(lambda x: str(x), choices(pw, k=lngth)))
    
    @classmethod
    def show_input_universe(cls):
        return cls.INPUT_UNIVERSE

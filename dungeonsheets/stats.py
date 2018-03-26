import math


def mod_str(modifier):
    """Converts a modifier to a string, eg 2 -> '+2'."""
    if modifier > 0:
        mod_str = '+' + str(modifier)
    else:
        mod_str = str(modifier)
    return mod_str



class Stat():
    value = 10
    
    def __init__(self, value=10):
        self.value = value
    
    @property
    def modifier(self):
        return math.floor((self.value - 10) / 2)
    
    def __set__(self, obj, val):
        self.value = val

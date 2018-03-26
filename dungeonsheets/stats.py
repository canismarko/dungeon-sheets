import math

class Stat():
    value = 10
    
    def __init__(self, value=10):
        self.value = value
    
    @property
    def modifier(self):
        return math.floor((self.value - 10) / 2)

    @property
    def modifier_string(self):
        """Similar to ``modifier`` but as a string.
        
        This also adds a '+' if necessary.
        
        """
        mod = self.modifier
        if mod > 0:
            mod_str = '+' + str(mod)
        else:
            mod_str = str(mod)
        return mod_str
            
    def __set__(self, obj, val):
        self.value = val

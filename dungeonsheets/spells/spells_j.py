from .spells import Spell


class Jump(Spell):
    """You touch a creature. The creature’s jump distance is tripled until the spell 
    ends.
    """
    name = "Jump"
    level = 1
    casting_time = "1 action"
    casting_range = "Touch"
    components = ('V', 'S', 'M')
    materials = """A grasshopper’s hind leg"""
    duration = "1 minute"
    ritual = False
    magic_school = "Transmutation"
    classes = ('Druid', 'Ranger', 'Sorcerer', 'Wizard')



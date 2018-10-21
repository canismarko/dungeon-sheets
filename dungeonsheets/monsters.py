"""A collection of monsters. Also useful for building a list of wild
shape forms."""


from .stats import Ability


class Monster():
    """A monster that may be encountered when adventuring."""
    name = "Generic Monster"
    description = ""
    challenge_rating = 0
    armor_class = 0
    skills = "Perception +3, Stealth +4"
    strength = Ability()
    dexterity = Ability()
    constitution = Ability()
    intelligence = Ability()
    wisdom = Ability()
    charisma = Ability()
    speed = 30
    swim_speed = 0
    fly_speed = 0
    hp_max = 10
    hit_dice = '1d6'
    
    @property
    def is_beast(self):
        is_beast = 'beast' in self.description.lower()
        return is_beast


class Crocodile(Monster):
    name = "Crocodile"


class GiantEagle(Monster):
    name = "Giant eagle"


class Wolf(Monster):
    """**Keen Hearing and Smell.** The wolf has advantage on Wisdom
    (Perception) checks that rely on hearing or smell.
    
    **Pack Tactics.** The wolf has advantage on an attack roll against a
    creature if at least one of the wolf's allies is within 5 ft. of
    the creature and the ally isn't incapacitated.  Actions
    
    **Bite.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one
    target. *Hit:* (2d4 + 2) piercing damage. If the target is a
    creature, it must succeed on a DC 11 Strength saving throw or be
    knocked prone
    
    """
    name = "Wolf"
    description = "Medium beast, unaligned"
    challenge_rating = 1/4
    armor_class = 13
    skills = "Perception +3, Stealth +4"
    senses = "Passive Perception 13"
    strength = Ability(12)
    dexterity = Ability(15)
    constitution = Ability(12)
    intelligence = Ability(6)
    wisdom = Ability(12)
    charisma = Ability(6)
    speed = 40
    hp_max = 11
    hit_dice = '2d8+2'

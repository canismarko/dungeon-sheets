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


class Spider(Monster):
    """**Spider Climb:** The spider can climb difficult surfaces,
    including upside down on ceilings, without needing to make an
    ability check.
    
    **Web Sense:** While in contact with a web, the spider knows the
    exact location of any other creature in contact with the same web.
    
    **Web Walker:** The spider ignores Movement restrictions caused by
    webbing.
    
    **Bite:** Melee Weapon Attack: +4 to hit, reach 5 ft., one
    creature. Hit: 1 piercing damage, and the target must succeed on a
    DC 9 Constitution saving throw or take 2 (1d4) poison damage.
    
    """
    name = "Spider"
    description = "Tiny beast, unaligned"
    challenge_rating = 0
    armor_class = 12
    skills = "Stealth +4"
    senses = "Darkvision 30 Ft., passive Perception 12"
    strength = Ability(2)
    dexterity = Ability(14)
    constitution = Ability(8)
    intelligence = Ability(1)
    wisdom = Ability(10)
    charisma = Ability(2)
    speed = 20
    hp_max = 1
    hit_dice = '1d4-1'


class Rat(Monster):
    """**Keen Smell:** The rat has advantage on Wisdom (Perception) checks
    that rely on smell.
    
    **Bite:** Melee Weapon Attack: +0 to hit, reach 5 ft., one
    target. Hit: 1 piercing damage.
    
    """
    name = "Rat"
    description = "Tiny beast, unaligned"
    challenge_rating = 0
    armor_class = 10
    skills = ""
    senses = "Darkvision 30 Ft., passive Perception 10"
    strength = Ability(2)
    dexterity = Ability(11)
    constitution = Ability(9)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(4)
    speed = 20
    hp_max = 1
    hit_dice = '1d4-2'


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

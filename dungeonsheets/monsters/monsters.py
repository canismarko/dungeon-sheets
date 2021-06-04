"""A collection of monsters. Also useful for building a list of wild
shape forms.

"""


from dungeonsheets.stats import Ability
from dungeonsheets.entity import Entity


class Monster(Entity):
    """A monster that may be encountered when adventuring."""

    name = "Generic Monster"
    description = ""
    challenge_rating = 0
    skills = "Perception +3, Stealth +4"
    swim_speed = 0  # TODO: Consider refactoring stats.Speed to consider all of these just like we do stats.Ability
    fly_speed = 0
    climb_speed = 0
    hp_max = 10
    hit_dice = "1d6"

    def __init__(self):
        super(Monster, self).__init__()

    @property
    def is_beast(self):
        is_beast = "beast" in self.description.lower()
        return is_beast


class Ankylosaurus(Monster):
    """Thick armor plating covers the body of the plant-eating dinosaur
    ankylosaurus, which defends itself against predators with a
    knobbed tail that delivers a devastating strike.

    **Tail:** *Melee Weapon Attack:* +7 to hit, reach 10 ft., one
    target. *Hit:* 18 (4d6+4) bludgeoning damage. If the target is a
    creature, it must succeed on a DC 14 Strength saving throw or be
    knocked prone.

    """

    # TODO: This doesn't appear to be SRD

    name = "Ankylosaurus"
    description = "Huge beast, unaligned"
    challenge_rating = 3
    armor_class = 15
    skills = ""
    senses = "passive Perception 11"
    strength = Ability(19)
    dexterity = Ability(11)
    constitution = Ability(15)
    intelligence = Ability(2)
    wisdom = Ability(12)
    charisma = Ability(5)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 68
    hit_dice = "8d12+16"

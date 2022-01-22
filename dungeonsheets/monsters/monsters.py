"""A collection of monsters. Also useful for building a list of wild
shape forms.

"""

from abc import ABCMeta


from dungeonsheets.content import Creature
from dungeonsheets.spells import Spell


xp_by_challenge_rating = {
    0: 10,
    (1 / 8): 25,
    (1 / 4): 50,
    (1 / 2): 100,
    1: 200,
    2: 450,
    3: 700,
    4: 1100,
    5: 1800,
    6: 2300,
    7: 2900,
    8: 3900,
    9: 5000,
    10: 5900,
    11: 7200,
    12: 8400,
    13: 10000,
    14: 11500,
    15: 13000,
    16: 15000,
    17: 18000,
    18: 20000,
    19: 22000,
    20: 25000,
    21: 33000,
    22: 41000,
    23: 50000,
    24: 62000,
    25: 75000,
    26: 90000,
    27: 105000,
    28: 120000,
    29: 130000,
    30: 155000,
}


def challenge_rating_to_xp(cr):
    """Determine the XP awarded for slaying a monster with the given
    challenge rating *cr*.

    """
    xp = xp_by_challenge_rating[cr]
    return "{:,}".format(xp)


class SpellFactory(ABCMeta):
    """Meta class to resolve spell strings into the ``spells.Spell``.
    
    For classes using this metaclass, the *spell* attribute, if
    present, should be a list of spells that the entity knows. For
    each entry on that list, anything that is not already a spell
    class (so probably a string) will be resolved into the
    corresponding ``spells.Spell`` class.
    
    """
    def __init__(self, name, bases, attrs):
        for idx, spell in enumerate(self.spells):
            TheSpell = self._resolve_mechanic(spell, SuperClass=Spell)
            self.spells[idx] = TheSpell


class Monster(Creature, metaclass=SpellFactory):

    """A monster that may be encountered when adventuring."""

    name = "Generic Monster"
    description = ""
    challenge_rating = 0
    skills = "Perception +3, Stealth +4"
    damage_resistances = ""
    damage_immunities = ""
    damage_vulnerabilities = ""
    condition_immunities = ""
    saving_throws = ""
    # TODO: Consider refactoring stats.Speed to consider all of these
    # just like we do stats.Ability
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 10
    hit_dice = "1d6"
    spells = []

    def __init__(self):
        super(Monster, self).__init__()

    @property
    def is_beast(self):
        is_beast = "beast" in self.description.lower()
        return is_beast

    def has_feature(self, *args, **kwargs):
        return False
    
    @property
    def is_spellcaster(self):
        return len(self.spells) > 0

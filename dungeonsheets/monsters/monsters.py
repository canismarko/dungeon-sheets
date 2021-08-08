"""A collection of monsters. Also useful for building a list of wild
shape forms.

"""

from abc import ABCMeta


from dungeonsheets.content import Creature
from dungeonsheets.spells import Spell


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

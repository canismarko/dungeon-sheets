"""A collection of monsters. Also useful for building a list of wild
shape forms.

"""


from dungeonsheets.entity import Entity


class Monster(Entity):
    """A monster that may be encountered when adventuring."""

    name = "Generic Monster"
    description = ""
    challenge_rating = 0
    skills = "Perception +3, Stealth +4"
    damage_resistances = ""
    damage_immunities = ""
    damane_vulnerabilities = ""
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

    def __init__(self):
        super(Monster, self).__init__()

    @property
    def is_beast(self):
        is_beast = "beast" in self.description.lower()
        return is_beast

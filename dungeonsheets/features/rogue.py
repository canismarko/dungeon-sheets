from .features import Feature
from math import ceil


# PHB
class RogueExpertise(Feature):
    """At 1st level, choose two of your skill proficiencies, or one of your skill
    proficiencies and your proficiency with thieves’ tools. Your proficiency
    bonus is doubled for any ability check you make that uses either of the
    chosen proficiencies. 

    At 6th level, you can choose two more of your
    proficiencies (in skills or with thieves’ tools) to gain this benefit.

    Add these skills to "skill_expertise" in your character.py file

    """
    name = "Expertise"
    source = "Rogue"


class SneakAttack(Feature):
    """Beginning at 1st level, you know how to strike subtly and exploit a foe’s
    distraction. Once per turn, you can deal an extra 1d6 damage to one
    creature you hit with an attack if you have advantage on the attack
    roll. The attack must use a finesse or a ranged weapon.

    You don’t need advantage on the attack roll if another enemy of the target
    is within 5 feet of it, that enemy isn’t incapacitated, and you don’t have
    disadvantage on the attack roll.

    The amount of the extra damage increases as you gain levels in this class,
    as shown in the Sneak Attack column of the Rogue table.
    """
    _name = "Sneak Attack"
    source = "Rogue"

    @property
    def name(self):
        level = self.owner.Rogue.level
        dice = ceil(level / 2.)
        name = self._name + " ({:d}d6)".format(dice)
        return name


class CunningAction(Feature):
    """Starting at 2nd level, your quick thinking and agility allow you to move
    and act quickly. You can take a bonus action on each of your turns in
    combat. This action can be used only to take the Dash, Disengage, or Hide
    action.

    """
    name = "Cunning Action"
    source = "Rogue"


class UncannyDodge(Feature):
    """Starting at 5th level, when an attacker that you can see hits you with an
    attack, you can use your reaction to halve the attack’s damage against you.

    """
    name = "Uncanny Dodge"
    source = "Rogue"


class Evasion(Feature):
    """Beginning at 7th level, you can nimbly dodge out o f the way of certain
    area effects, such as a red dragon’s fiery breath or an ice storm
    spell. When you are subjected to an effect that allows you to make a
    Dexterity saving throw to take only half damage, you instead take no damage
    if you succeed on the saving throw, and only half damage if you fail.

    """
    name = "Evasion"
    source = "Class (many)"


class ReliableTalent(Feature):
    """By 11th level, you have refined your chosen skills until they approach
    perfection. Whenever you make an ability check that lets you add your
    proficiency bonus, you can treat a d20 roll of 9 or lower as a 10.

    """
    name = "Reliable Talent"
    source = "Rogue"


class BlindSense(Feature):
    """Starting at 14th level, if you are able to hear, you are aware of the
    location of any hidden or invisible creature within 10 feet of you.
    """
    name = "Blind Sense"
    source = "Rogue"


class SlipperyMind(Feature):
    """By 15th level, you have acquired greater mental strength. You gain
    proficiency in W isdom saving throws.

    """
    name = 'Slippery Mind'
    source = "Rogue"


class Elusive(Feature):
    """Beginning at 18th level, you are so evasive that attackers rarely gain the
    upper hand against you. No attack roll has advantage against you while you
    aren’t incapacitated.

    """
    name = "Elusive"
    source = "Rogue"


class StrokeOfLuck(Feature):
    """At 20th level, you have an uncanny knack for succeeding when you need
    to. If your attack m isses a target within range, you can turn the miss
    into a hit. Alternatively, if you fail an ability check, you can treat the
    d20 roll as a 20.

    Once you use this feature, you can’t use it again until you finish a short
    or long rest.

    """
    name = "Stroke of Luck"
    source = "Rogue"

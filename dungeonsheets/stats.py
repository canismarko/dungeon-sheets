import math
from collections import namedtuple
from math import ceil
import logging

from dungeonsheets.armor import HeavyArmor, NoArmor, NoShield
from dungeonsheets.features import (
    AmbushMaster,
    Defense,
    DraconicResilience,
    DreadAmbusher,
    FastMovement,
    FeralInstinct,
    GiftOfTheDepths,
    JackOfAllTrades,
    NaturalArmor,
    NaturalExplorerRevised,
    QuickDraw,
    RakishAudacity,
    RemarkableAthlete,
    SeaSoul,
    SoulOfTheForge,
    SuperiorMobility,
    UnarmoredDefenseBarbarian,
    UnarmoredDefenseMonk,
    UnarmoredMovement,
)


log = logging.getLogger(__name__)


def mod_str(modifier):
    """Converts a modifier to a string, eg 2 -> '+2'."""
    return "{:+d}".format(modifier)


def ability_mod_str(character, ability):
    return mod_str(getattr(character, ability).modifier)


def stat_abbreviation(stat_name):
    """Abbreviate the name of an ability."""
    return stat_name.upper()[:3]


AbilityScore = namedtuple("AbilityScore", ("value", "modifier", "saving_throw", "name"))


class Ability:
    ability_name = None

    def __init__(self, default_value=10):
        self.default_value = default_value

    def __set_name__(self, character, name):
        self.ability_name = name

    def _check_dict(self, obj):
        if not hasattr(obj, "_ability_scores"):
            # No ability score dictionary exists
            obj._ability_scores = {self.ability_name: self.default_value}
        elif self.ability_name not in obj._ability_scores.keys():
            # ability score dictionary exists but doesn't have this ability
            obj._ability_scores[self.ability_name] = self.default_value

    def __get__(self, entity, Entity):
        self._check_dict(entity)
        score = entity._ability_scores[self.ability_name]
        modifier = math.floor((score - 10) / 2)
        # Check for proficiency
        saving_throw = modifier
        if self.ability_name is not None and hasattr(
            entity, "saving_throw_proficiencies"
        ):
            is_proficient = self.ability_name in entity.saving_throw_proficiencies
            if is_proficient:
                saving_throw += entity.proficiency_bonus
        # Create the named tuple
        value = AbilityScore(modifier=modifier, value=score, saving_throw=saving_throw, name=self.ability_name)
        return value

    def __set__(self, entity, val):
        self._check_dict(entity)
        entity._ability_scores[self.ability_name] = val
        self.value = val


class Skill:
    """An ability-based skill, such as athletics.

    Attributes
    ----------
    ability_name:
      The name of the ability, as a python-compatible string.
    skill_name:
      The name of the base ability that determines the skill
      modifier.
    is_proficient
      Bool that describes if the owner is proficient in this skill.
    is_expertise
      Bool that describes if the owner has expertise in this skill.
    is_jack_of_all_trades
      Bool that describes if this skill benefits from Jack of All
      Trades feature (False if already proficient).
    is_remarkable_athlete
      Bool that describes if this skill benefits from Remarkable
      Athlete feature (False if already proficient).
    modifier
      The base ability modifier, after relevant proficiency bonuses
      have been applied.
    proficiency_modifier
      The bonus that is applied to the base ability. Usually the same
      as the owner's proficiency bonus if ``is_proficient`` is True,
      but can be different based on class features.,

    """
    
    ability_name = ""
    skill_name = ""
    entity = None
    
    def __init__(self, ability):
        self.ability_name = ability

    def __set_name__(self, owner, name):
        self.skill_name = name.lower().replace("_", " ")

    def __get__(self, entity, owner):
        self.entity = entity
        return self

    def __str__(self):
        return self.skill_name.title()

    @property
    def is_remarkable_athlete(self):
        already_proficient = (self.is_proficient or self.is_expertise)
        if self.entity.has_feature(RemarkableAthlete) and not already_proficient:
            return True
        else:
            return False

    @property
    def is_jack_of_all_trades(self):
        already_proficient = (self.is_proficient or self.is_expertise or self.is_remarkable_athlete)
        if self.entity.has_feature(JackOfAllTrades) and not already_proficient:
            return True
        else:
            return False

    @property
    def is_proficient(self):
        # Check for proficiency
        proficiencies = [p.replace("_", " ") for p in self.entity.skill_proficiencies]
        is_proficient = self.skill_name in proficiencies
        return is_proficient

    @property
    def is_expertise(self):
        return self.skill_name in self.entity.skill_expertise

    @property
    def proficiency_modifier(self):
        modifier = 0
        if self.is_proficient:
            modifier += self.entity.proficiency_bonus
        if self.is_remarkable_athlete:
            modifier += ceil(self.entity.proficiency_bonus / 2.0)
        if self.is_jack_of_all_trades:
            modifier += self.entity.proficiency_bonus // 2
        # Check for expertise
        if self.is_expertise:
            modifier += self.entity.proficiency_bonus
        return modifier

    @property
    def modifier(self):
        ability = getattr(self.entity, self.ability_name)
        modifier = ability.modifier + self.proficiency_modifier
        log.info("%s modifier for '%s': %d", self, self.entity.name, modifier)
        return modifier


class ArmorClass:
    """
    The Armor Class of a character
    """

    def __get__(self, entity, Entity):
        armor = entity.armor or NoArmor()
        ac = armor.base_armor_class
        # calculate and apply modifiers
        if armor.dexterity_mod_max is None:
            ac += entity.dexterity.modifier
        else:
            ac += min(entity.dexterity.modifier, armor.dexterity_mod_max)
        if entity.has_feature(NaturalArmor):
            ac = max(ac, 13 + entity.dexterity.modifier)
        shield = entity.shield or NoShield()
        ac += shield.base_armor_class
        # Compute feature-specific additions
        if entity.has_feature(UnarmoredDefenseMonk):
            if isinstance(armor, NoArmor) and isinstance(shield, NoShield):
                ac += entity.wisdom.modifier
        if entity.has_feature(UnarmoredDefenseBarbarian):
            if isinstance(armor, NoArmor):
                ac += entity.constitution.modifier
        if entity.has_feature(DraconicResilience):
            if isinstance(armor, NoArmor):
                ac += 3
        if entity.has_feature(Defense):
            if not isinstance(armor, NoArmor):
                ac += 1
        if entity.has_feature(SoulOfTheForge):
            if isinstance(armor, HeavyArmor):
                ac += 1
        # Check if any magic items add to AC
        for mitem in entity.magic_items:
            if hasattr(mitem, "ac_bonus"):
                ac += mitem.ac_bonus
        return ac


class Speed:
    """
    The speed of a character
    """

    def __get__(self, entity, Entity):
        speed = entity.race.speed
        other_speed = ""
        if isinstance(speed, str):
            other_speed = speed[2:]
            speed = int(speed[:2])  # ignore other speeds, like fly
        if entity.has_feature(FastMovement):
            if not isinstance(entity.armor, HeavyArmor):
                speed += 10
        if entity.has_feature(SuperiorMobility):
            speed += 10
        if isinstance(entity.armor, NoArmor) or (entity.armor is None):
            for f in entity.features:
                if isinstance(f, UnarmoredMovement):
                    speed += f.speed_bonus
        if entity.has_feature(GiftOfTheDepths):
            if "swim" not in other_speed:
                other_speed += " ({:d} swim)".format(speed)
        if entity.has_feature(SeaSoul):
            if "swim" not in other_speed:
                other_speed += " (30 swim)"
        return "{:d}{:s}".format(speed, other_speed)


class NumericalInitiative:
    """A numerical representation of initiative"""

    def __get__(self, entity, Entity):
        ini = entity.dexterity.modifier
        if entity.has_feature(QuickDraw):
            ini += entity.proficiency_bonus
        if entity.has_feature(DreadAmbusher):
            ini += entity.wisdom.modifier
        if entity.has_feature(RakishAudacity):
            ini += entity.charisma.modifier

        has_advantage = (
            entity.has_feature(NaturalExplorerRevised)
            or entity.has_feature(FeralInstinct)
            or entity.has_feature(AmbushMaster)
        )
        return ini, has_advantage


class Initiative(NumericalInitiative):
    """A character's initiative"""

    def __get__(self, entity, Entity):
        ini, has_advantage = super(Initiative, self).__get__(entity, Entity)
        ini = "{:+d}".format(ini)
        if has_advantage:
            ini += "(A)"
        return ini

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
    RemarkableAthelete,
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


AbilityScore = namedtuple("AbilityScore", ("value", "modifier", "saving_throw"))


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
        value = AbilityScore(modifier=modifier, value=score, saving_throw=saving_throw)
        return value

    def __set__(self, entity, val):
        self._check_dict(entity)
        entity._ability_scores[self.ability_name] = val
        self.value = val


class Skill:
    """An ability-based skill, such as athletics."""

    def __init__(self, ability):
        self.ability_name = ability

    def __set_name__(self, entity, name):
        self.skill_name = name.lower().replace("_", " ")
        self.character = entity

    def __get__(self, entity, owner):
        log.debug("Getting skill '%s' for '%s'", self.skill_name, entity.name)
        ability = getattr(entity, self.ability_name)
        modifier = ability.modifier
        # Check for proficiency
        proficiencies = [p.replace("_", " ") for p in entity.skill_proficiencies]
        is_proficient = self.skill_name in proficiencies
        log.debug(
            "%s is proficient in %s: %s", entity.name, self.skill_name, is_proficient
        )
        if is_proficient:
            modifier += entity.proficiency_bonus
        elif entity.has_feature(JackOfAllTrades):
            modifier += entity.proficiency_bonus // 2
        elif entity.has_feature(RemarkableAthelete):
            if self.ability_name.lower() in ("strength", "dexterity", "constitution"):
                modifier += ceil(entity.proficiency_bonus / 2.0)

        # Check for expertise
        is_expert = self.skill_name in entity.skill_expertise
        if is_expert:
            modifier += entity.proficiency_bonus
        log.info("'%s' modifier for '%s': %d", self.skill_name, entity.name, modifier)
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

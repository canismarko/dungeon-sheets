#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets.character import Character
from dungeonsheets.encounter import Encounter
from dungeonsheets.monsters import Monster
from dungeonsheets.stats import Ability


class TestEncounter(TestCase):
    """Tests for features and feature-related activities."""

    def test_simulation(self):
        """Can I run an encounter against Schlangdedrosa Magentawrath?"""
        char = Character()
        char.set_attrs(name="Stravajiaxen")
        char.set_attrs(weapons=["greataxe"])
        char.set_attrs(armor="split mail")

        # Check that race gets set to an object
        char.set_attrs(race="half orc")
        char.set_attrs(inspiration=False)

        class SchlangdedrosaMagentawrath(Monster):
            """
            **Action Surge (Recharges on a Short or Long Rest).** On his turn, Langdedrosa
            can take one additional action.

            **Improved Critical.** Langdedrosa's weapon attacks score a critical hit on a
            roll of 19 or 20.
            
            **Multiattack:** Schlangdedrosa attacks twice, either with his greatsword or spear.

            **Greatsword.** Melee Weapon Attack: +6 to hit, reach 5 ft., one target.
            Hit: 11 (2d6 + 4) slashing damage.

            **Spear.** Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or
            ranged 20/60 ft., one target. Hit: 7 (1d6 + 4) piercing damage.

            **Lightning Breath (Recharge 5-6)**. Schlangdedrosa breathes lightning in a
            30-foot line that is 5 feet wide. Each creature in the line must make a DC 13
            Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or
            half as much damage on a successful one.

            **Climbing speed:** 30 ft.
            """

            name = "Schlangdedrosa Magentawrath"
            description = "Medium humanoid (half-dragon), lawful evil"
            challenge_rating = 4
            armor_class = 17
            skills = "Athletics +6, Intimidation +3, Perception +4"
            senses = "blindsight 10 ft., darkvision 60ft., passive Perception 14"
            strength = Ability(19)
            dexterity = Ability(13)
            constitution = Ability(16)
            intelligence = Ability(10)
            wisdom = Ability(14)
            charisma = Ability(12)
            speed = 30
            swim_speed = 0
            fly_speed = 0
            hp_max = 57
            hit_dice = "6d12+18"

        schlang = SchlangdedrosaMagentawrath()

        battle = Encounter([char], [schlang])
        results = battle.simulate()
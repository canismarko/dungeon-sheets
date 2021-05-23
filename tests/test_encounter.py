#!/usr/bin/env python

from unittest import TestCase, skip

from dungeonsheets.armor import ChainShirt
from dungeonsheets.character import Character
from dungeonsheets.encounter import Encounter
from dungeonsheets.encounter.actions import Attack
from dungeonsheets.encounter.events import AttackEvent
from dungeonsheets.monsters import Monster, GiantRat
from dungeonsheets.stats import Ability
from dungeonsheets.dice import roll


class TestEncounter(TestCase):
    """Tests for features and feature-related activities."""

    def setUp(self):

        char = SimpleRanger()

        class StravajiaxenAttack(Attack):
            # TODO: Get default player attacks as a result of
            #  creating a player character and classes

            def __init__(self, subj, obj):
                super(StravajiaxenAttack, self).__init__(subj, obj)

            def execute(self):
                result = roll(20) + self.subj.dexterity.modifier + self.subj.proficiency_bonus
                damage = roll(1, 8) + self.subj.dexterity.modifier
                is_hit = result >= self.obj.armor_class

                if is_hit:
                    self.obj.current_hp -= damage

                return AttackEvent(self, result, damage, is_hit)

        char.default_actions.append(StravajiaxenAttack)

        class GiantRatAttack(Attack):

            def __init__(self, subj, obj):
                super(GiantRatAttack, self).__init__(subj, obj)

            def execute(self):
                result = roll(20) + 4
                damage = roll(1, 4) + 2
                is_hit = result >= self.obj.armor_class

                if is_hit:
                    self.obj.current_hp -= damage

                return AttackEvent(self, result, damage, is_hit)

        enemy = GiantRat()
        enemy.name = "Nameless Rat"  # I don't want things to be personal...
        enemy.default_actions.append(GiantRatAttack)
        self.default_player = char
        self.default_enemy = enemy

    def test_encounter_rating(self):
        battle = Encounter([self.default_player], [self.default_enemy])
        self.assertRaises(NotImplementedError, battle.rating)

    def test_opponents(self):
        battle = Encounter([self.default_player], [self.default_enemy])
        self.assertEqual([self.default_enemy], battle.opponents(self.default_player))
        self.assertEqual([self.default_player], battle.opponents(self.default_enemy))

    def test_allies(self):
        battle = Encounter([self.default_player], [self.default_enemy])
        self.assertEqual(0, len(battle.allies(self.default_player)))
        self.assertEqual(0, len(battle.allies(self.default_enemy)))

    def test_simple_rat_fight(self):
        """A fight against a giant rat"""
        battle = Encounter([self.default_player], [self.default_enemy])
        battle.reset()
        results = battle.simulate()
        for event in results:
            print(str(event))
        print(results)

    @skip('NotImplementedError')
    def test_langdedrosa_fight(self):
        """Can I run an encounter against Langdedrosa Cyanwrath?"""
        char = Character()
        char.set_attrs(name="Stravajiaxen")
        char.set_attrs(weapons=["greataxe"])
        char.set_attrs(armor="split mail")

        # Check that race gets set to an object
        char.set_attrs(race="half orc")
        char.set_attrs(inspiration=False)

        class LangdedrosaCyanwrath(Monster):
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

            name = "Langdedrosa Cyanwrath"
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

        lang = LangdedrosaCyanwrath()

        battle = Encounter([char], [lang])
        results = battle.simulate()


class SimpleRanger(Character):  # Taken from ranger2.py
    """This file describes the heroic adventurer Ranger2.

    It's used primarily for saving characters from create-character,
    where there will be many missing sections.

    Modify this file as you level up and then re-generate the character
    sheet by running ``makesheets`` from the command line.

    """

    dungeonsheets_version = "0.9.4"

    name = "Stravajiaxen"
    player_name = "Ben"

    # Be sure to list Primary class first
    classes = ['Ranger']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
    levels = [3]  # ex: [10] or [3, 2]
    subclasses = ["Horizon Walker"]  # ex: ['Necromacy'] or ['Thief', None]
    background = "Uthgardt Tribe Member"
    race = "Lizardfolk"
    alignment = "Neutral good"

    xp = 0
    hp_max = 24
    inspiration = 0  # integer inspiration value

    # Ability Scores
    strength = Ability(13)
    dexterity = Ability(15)
    constitution = Ability(12)
    intelligence = Ability(8)
    wisdom = Ability(15)
    charisma = Ability(12)

    # Select what skills you're proficient with
    # ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
    skill_proficiencies = ('athletics', 'insight', 'investigation')

    # Any skills you have "expertise" (Bard/Rogue) in
    skill_expertise = ()

    # Named features / feats that aren't part of your classes, race, or background.
    # Also include Eldritch Invocations and features you make multiple selection of
    # (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
    # Gunslinger, etc.)
    # Example:
    # features = ('Tavern Brawler',) # take the optional Feat from PHB
    features = ()

    # If selecting among multiple feature options: ex Fighting Style
    # Example (Fighting Style):
    # feature_choices = ('Archery',)
    feature_choices = ('dueling',)

    # Weapons/other proficiencies not given by class/race/background
    weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
    _proficiencies_text = ()  # ex: ("thieves' tools",)

    # Proficiencies and languages
    languages = """Dwarvish, Common, Draconic"""

    # Inventory
    # TODO: Get yourself some money
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0

    # TODO: Put your equipped weapons and armor here
    weapons = ('rapier', 'hand crossbow')  # Example: ('shortsword', 'longsword')
    magic_items = ()  # Example: ('ring of protection',)
    armor = ChainShirt  # Eg "leather armor"
    shield = ""  # Eg "shield"

    equipment = """TODO: list the equipment and magic items your character carries"""

    attacks_and_spellcasting = """TODO: Describe how your character usually attacks
    or uses spells."""

    # List of known spells
    # Example: spells_prepared = ('magic missile', 'mage armor')
    spells_prepared = ()  # Todo: Learn some spells

    # Which spells have not been prepared
    __spells_unprepared = ()

    # all spells known
    spells = spells_prepared + __spells_unprepared

    # Wild shapes for Druid
    wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

    # Backstory
    # Describe your backstory here
    personality_traits = """TODO: How does your character behave? See the PHB for
    examples of all the sections below"""

    ideals = """TODO: What does your character believe in?"""

    bonds = """TODO: Describe what debts your character has to pay,
    and other commitments or ongoing quests they have."""

    flaws = """TODO: Describe your characters interesting flaws.
    """

    features_and_traits = """TODO: Describe other features and abilities your
    character has."""

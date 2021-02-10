"""This file describes the heroic adventurer Homebrewelda.

This example demonstrates how to add homebrew spells into the game.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""
from dungeonsheets import mechanics

dungeonsheets_version = "0.9.4"

name = "Homebrewelda"
player_name = "Clara"

# Be sure to list Primary class first
classes = ['Wizard']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [20]  # ex: [10] or [3, 2]
subclasses = ["School of Transmutation"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Hermit"
race = "Air Genasi"
alignment = "Chaotic neutral"

xp = 0
hp_max = 105
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 8
dexterity = 11
constitution = 14
intelligence = 15
wisdom = 13
charisma = 14

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('arcana', 'history', 'medicine', 'religion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
class Juggler(mechanics.Feature):
    """You can juggle like a pro!"""
    name = "Juggler"
features = (Juggler, "master_of_ceremonies")

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()


class DullSword(mechanics.Weapon):
    """Bonk things with it."""
    name = "Dullsword"

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = (DullSword,)  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """[choose one], Common, Primoridal"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# Put your equipped weapons and armor here

class RobeOfBreadSummoning(mechanics.MagicItem):
    """Shamefully stolen from the "D&D minus" podcast."""
    name = "Robe of Bread Summoning"


class PlasticArmor(mechanics.Armor):
    name = "Plastic armor"
    base_armor_class = 23


class LegoShield(mechanics.Shield):
    name = "Lego shield"
    base_armor_class = 114


weapons = (DullSword, "rusty_shiv")  # Example: ('shortsword', 'longsword')
magic_items = (RobeOfBreadSummoning, "staff_of_the_arbor_abode")
armor = PlasticArmor # Eg "leather armor"
shield = LegoShield  # Eg "shield"

equipment = """TODO: list the equipment and magic items your character carries"""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

class MagicFlask(mechanics.Spell):
    """A spectral, floating hand appears at a point you choose within
    range holding a flask of finely distilled spirits.
    
    The flask lasts for the duration or until you dismiss it as an
    action. The flask vanishes if it is ever more than 30 feet away
    from you or if you cast this spell again.
    
    You can use your action to take a sip of the flask or provide a
    sip to a willing target. You can move the hand up to 30 feet each
    time you use it.
    
    """
    name = "Magic Flask"
    level = 0
    casting_time = "1 action"
    casting_range = "30 feet"
    components = ('V', 'S')
    materials = """"""
    duration = "1 minute"
    ritual = False
    magic_school = "Conjuration"
    classes = ('Bard', 'Warlock', 'Wizard')
    

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ('acid splash', 'animate_objects', 'ray of frost', 'light', 'friends',
                   'disguise self', 'identify', 'jump',
                   'blur', 'knock', 'shatter',
                   'blink', 'fly', 'slow',
                   'blight', 'ice storm',
                   'cone of cold', 'magic jar',
                   'teleport', 'maze', 'wish',
                   # Home brew stuff:
                   MagicFlask, 'summon_corgis')

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

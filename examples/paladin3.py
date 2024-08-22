
"""This file describes the heroic adventurer Paladin3.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

This example demonstrates selecting enough spells to generate
the half-caster sheet.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""
dungeonsheets_version = "0.9.4"


name = "Paladin3"
player_name = "Alice"

# Be sure to list Primary class first
classes = ['Paladin']
levels = [4]
subclasses = ["Oath of Conquest"]
background = "Acolyte"
race = "Protector Aasimar"
alignment = "Lawful Good"

xp = 2700
hp_max = 28
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 16
dexterity = 8
constitution = 12
intelligence = 10
wisdom = 12 + 1
charisma = 15 + 2


# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('intimidation', 'medicine', 'insight', 'religion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerers, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('Defense', )

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish, Celestial, Draconic"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
# Example: ('shortsword', 'longsword')
weapons = ('longsword', 'javelin', 'longbow')
magic_items = ()  # Example: ('ring of protection',)
armor = "chain mail"  # Eg "leather armor"
shield = "shield"  # Eg "shield"


equipment = """TODO: list the equipment and magic items your character carries"""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ('light',)

# Which spells have not been prepared
__spells_unprepared = (
    'bless',
    'ceremony',
    'command',
    'compelled duel',
    'cure wounds',
    'detect evil and good',
    'detect magic',
    'detect poison and disease',
    'divine favor',
    'heroism',
    'protection from evil and good',
    'purify food and drink',
    'searing smite',
    'shield of faith',
    'thunderous smite',
    'wrathful smite')

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

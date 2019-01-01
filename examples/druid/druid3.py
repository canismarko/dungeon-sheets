"""This file describes the heroic adventurer Druid3.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Druid3"
player_name = "Ben"

# Be sure to list Primary class first
classes = ['Druid']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [11]  # ex: [10] or [3, 2]
subclasses = ["Circle of the Land"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Urchin"
race = "Wood Elf"
alignment = "Chaotic good"

xp = 0
hp_max = 60
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 8
dexterity = 12
constitution = 12
intelligence = 13
wisdom = 15
charisma = 15

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('insight', 'medicine', 'sleight of hand', 'stealth', 'perception')

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
feature_choices = ('underdark',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ('club', 'sickle')  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = ""  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """TODO: list the equipment and magic items your character carries"""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ('shillelagh', 'poison spray', 'druidcraft',
                   'speak with animals', 'entangle', 'cure wounds',
                   'create or destroy water')

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ["wolf", "crocodile", "giant eagle", 'ape', 'ankylosaurus']

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

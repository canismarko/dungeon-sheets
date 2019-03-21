"""This file describes the heroic adventurer Ben.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Ben"
player_name = "Ben"

# Be sure to list Primary class first
classes = ['Cleric', 'Barbarian']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [5, 10]  # ex: [10] or [3, 2]
subclasses = ["Light Domain", "Path of the Battlerager"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Criminal"
race = "High Elf"
alignment = "Chaotic good"

xp = 0
hp_max = 100
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 10
dexterity = 12
constitution = 18
intelligence = 11
wisdom = 10
charisma = 10

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('insight', 'medicine', 'deception', 'stealth', 'perception')

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
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish, [choose one]"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Greatclub"]  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "Padded Armor"  # Eg "leather armor"
shield = "None"  # Eg "shield"

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
personality_traits = """TODO: Describe how your character behaves, interacts with others"""

ideals = """TODO: Describe what values your character believes in."""

bonds = """TODO: Describe your character's commitments or ongoing quests."""

flaws = """TODO: Describe your character's interesting flaws."""

features_and_traits = """TODO: Describe other features and abilities your
character has."""

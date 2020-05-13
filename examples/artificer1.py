"""This file describes the heroic adventurer Cemzack.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.10.1"

name = "Cemzack"
player_name = ""

# Be sure to list Primary class first
classes = ['Artificer']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [20]  # ex: [10] or [3, 2]
subclasses = ["Artillerist"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Sailor"
race = "Rock Gnome"
alignment = "Neutral good"

xp = 0
hp_max = 149
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 13
dexterity = 16
constitution = 18
intelligence = 20
wisdom = 12
charisma = 10

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('investigation', 'sleight of hand', 'athletics', 'perception')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('sharpshooter')

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Gnomish"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = []  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "Breastplate"  # Eg "leather armor"
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

# Infusions for Artificer
infusions = ('boots of the winding path', 'enhanced arcane focus',
             'enhanced defense', 'enhanced weapon', 'repeating shot',
             'homunculus servant', 'radiant weapon', 'replicate magic item',
             'repulsion shield', 'resistant armor', 'returning weapon')
# Ex: ('repeating shot', 'replicate magic item')

# Backstory
# Describe your backstory here
personality_traits = """TODO: Describe how your character behaves, interacts with others"""

ideals = """TODO: Describe what values your character believes in."""

bonds = """TODO: Describe your character's commitments or ongoing quests."""

flaws = """TODO: Describe your character's interesting flaws."""

features_and_traits = """TODO: Describe other features and abilities your
character has."""

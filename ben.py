"""This file describes the heroic adventurer Ben.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.8.0"

name = "Ben"
classes_levels = ['barbarian 1', 'bard 1', 'cleric 1', 'druid 1', 'fighter 1', 'monk 1', 'ranger 1', 'rogue 1', 'sorceror 1', 'warlock 1', 'wizard 1', 'revised ranger 1']
subclasses = ["Path of the Berserker", "College of Lore", "Arcana Domain", "Circle of the Land", "Arcane Archer", "Way of the Open Hand", <dungeonsheets.classes.ranger.Hunter object at 0x108e7ba20>, "Thief", "Draconic Bloodline", "The Archfey Patron", "School of Abjuration", '']
player_name = "Ben"
background = "Mercenary Veteran"
race = "Hill Dwarf"
alignment = "Neutral good"
xp = 0
hp_max = 10

# Ability Scores
strength = 14
dexterity = 15
constitution = 15
intelligence = 12
wisdom = 11
charisma = 8

# Select what skills you're proficient with
skill_proficiencies = ('nature', 'animal handling', 'athletics', 'persuasion')

# Named features / feats that aren't part of your classes,
# race, or background.
# Example:
# features = ('Tavern Brawler',)  # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Proficiencies and languages
languages = """Common, Dwarvish"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = () # Example: ('shortsword', 'longsword')
armor = "" # Eg "light leather armor"
shield = "" # Eg "shield"

equipment = """TODO: list the equipment and magic items your character carries"""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = () # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

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

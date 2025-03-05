"""This file describes the heroic adventurer Bloodhunter1.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.17.1"

name = "Bloodhunter1"
player_name = "plsaddbloodhunter"

# Be sure to list Primary class first
classes = ['Blood hunter']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [15]  # ex: [10] or [3, 2]
subclasses = ["Order of the Profane Soul"]  # ex: ['Necromancy'] or ['Thief', None]
background = "Pirate"
race = "Human"
alignment = "Neutral good"

xp = "Milestone"
hp_max = 96
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 17
dexterity = 14
constitution = 13
intelligence = 12
wisdom = 10
charisma = 9

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('athletics', 'intimidation', 'history', 'persuasion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerers, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ('rite of the frozen', 'rite of the storm', 'rite of the oracle',
            'alluring', 'celerity', 'embers', 'impermeable', 'reconstruction',
            'cruelty', 'precision', 'blood curse of the anxious', 'blood curse of binding',
            'blood curse of the fallen puppet', 'blood curse of the muddled mind',)

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('great-weapon fighting', 'undying',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Elvish, Common, Draconic"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ('greatsword', 'longbow', 'battleaxe')  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "chain mail"  # Eg "leather armor"
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


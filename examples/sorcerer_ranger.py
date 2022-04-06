"""This file describes the heroic adventurer DooDee.
It's used primarily for saving characters from create-character,
where there will be many missing sections.
Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.
"""

# To add your own content, write a .py file with your definitions.
# Then, import here using the 'import_homebrew' function.
from dungeonsheets import import_homebrew
# from dungeonsheets.equipment_reader import explorers_pack
HB_races = import_homebrew("HB_races.py")
kits = import_homebrew("kits.py")

dungeonsheets_version = '0.17.1'
name = "DooDee"
player_name = "George Martin"

# Be sure to list Primary class first
classes = ['Druid', 'Ranger', 'Sorceror']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [5, 3, 1]  # ex: [10] or [3, 2]
subclasses = ["Circle of the Moon", "Beast Master", None ]  # ex: ['Necromacy'] or ['Thief', None]
background = "Hermit"
race = HB_races.WildhuntShifter
alignment = "Lawful Neutral"

xp = 14587
hp_max = 77
# hp_temp = 5
# hp_current = 31
inspiration = 1  # integer inspiration value

# Ability Scores
strength = 10
dexterity = 17
constitution = 14
intelligence = 16
wisdom = 14
charisma = 12

# Select what skills you're proficient with
skill_proficiencies = ('insight', 'perception', 
                       'medicine', 'survival', 'religion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = (HB_races.WildCompanion, "Sharpshooter")

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ("Archery",)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ("Cartographer's tools", )  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Druidic, Elven, Draconic"""

# Inventory
# Get yourself some money
cp = 0
sp = 95
ep = 12
gp = 140
pp = 0

# Put your equipped weapons and armor here
weapons = ("Longbow", 'Quarterstaff','dagger')  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "Hide Armor"  # Eg "leather armor"
shield = ""  # Eg "shield"

# The equipment goes here. A total weight will be automatically 
# calculated and added. 
equipment = kits.explorers_pack.format(rations=9, torches=3, 
                                       pitons=10, rope=50) + \
    ", human skin mask, sacrificial knife, 10 arrows."

# If the weight of an item is undetermined, you can include it
# in the equipment_weight_dict
equipment_weight_dict = {"human skin mask":0.5}

attacks_and_spellcasting = \
"""
Quarterstaff with Shillelagh: +5 to hit, 1d8+3/b
"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ("Shillelagh", "Druidcraft", "Cure Wounds", "Faerie Fire",
                   "Entangle", "Thunderwave", "Fog Cloud", "Barkskin") 


# Which spells have not been prepared
__spells_unprepared = ("Speak with animals", "Charm Person", 
                       "Animal Friendship", "Create or Destroy Water",
                       "Goodberry", "Purify Food and Drink", "Find Familiar")

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ("Ape", "Wolf", "Mastiff", "Giant Spider", "Tiger",
               "Dire Wolf", "Brown Bear","Cat")  # Ex: ('ape', 'wolf', 'ankylosaurus')
# List any monsters whose reference can come at hand 
# for spells like Find Familiar
companions = ["owl", "poisonous snake", "panther"]

# Rangers Beast for Beast Master
ranger_beast = "Panther"

# Backstory
# Describe your backstory here
personality_traits = """
I am introspective.
"""

ideals = """I search for nature balance."""

bonds = """My friends from my village."""

flaws = """
    I lose my temper when I see animal corpses as trophies."""

features_and_traits = """"""

portrait = 'shifter_2.png'
age = 15
height = "1,77m"
weight = "72kg"
eyes = "Black"
skin = "Brown"
hair = "Brown"


# optionally, if you set portrait to false, you can include a text
# in the appearance box using the 'appearece_text' variable:
# appearance_text =  
additional_description = \
    '''
Find it better to avoid conflict. 
'''

backstory = \
    '''

Born at Makudan Village, helped many other 
shifters to overcome the vampire known as Strahd.

'''

treasure = \
    '''
    A Dire Wolf tooth
    
    '''

allies = \
    '''
    His childhood friend Krenak
    
    His elder master Caiubi;
    
    Druids of Rakshak
    
    Druids of Makudan
    '''
    
org_name = \
    '''
    Druids of Makudan
    
    '''

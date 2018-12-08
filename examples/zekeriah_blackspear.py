dungeonsheets_version = "0.4.2"

# Basic information
name = 'Zekeriah Blackspear'
character_class = 'cleric'
player_name = 'Ben'
background = "Acolyte"
race = 'Human'
level = 1
alignment = 'Neutral-Good'
xp = 0
hp_max = 10

# Ability Scores
strength = 12
dexterity = 12
constitution = 14
intelligence = 6 
wisdom = 17 
charisma = 8

# Proficiencies and languages
skill_proficiencies = [
    'insight',
    'medicine',
    'perception',
    'persuasion',
    'religion',
]
languages = "Common, Elvish, Dwarvish, Halfling."

# Inventory
cp = 0
sp = 0
ep = 0
gp = 155
pp = 0
weapons = ('mace', 'handaxe')
armor = 'Leather Armor'
shield = 'Shield'
equipment = (
          """Priest's Pack, Backpack, Blanket, 10 Candles, 
          Tinderbox, Alms Box, (2/2) Blocks of Insense, 
          A Censer, Vestments, (2/2) Days of Rations, 
          A Waterskin""")

# List of known spells
#spells = ('spare the dying', 'guidance' )
spells = ('false life', 'blindness deafness' )

# Which spells have been prepared (not including cantrips)
spells_prepared = ('blindness deafness', 'false life', 'mage armor',
                   'ray of sickness', 'shield', 'sleep',)

# Backstory
personality_traits = """I am tolerant of other faiths and respect the worship
                        of other gods. I see omens in every event and action.
                        The gods try to speak to us. We just need to listen."""

ideals = """Charity: I always try to help those in need, no matter what the personal cost."""

bonds = """Someone saved my life on the battlefield. To this day I will
           never leave a friend behind."""

flaws = """Once I pick a goal, I become obsessed with it to the
           detriment of everything else in my life."""

features_and_traits = (
        """*Observant (feat)*  +5 to passive perception and passive investigation. If you can see a creature's mouth while it is speaking a language you understand, you can read its lips.
        *Domain* Grave
        *Circle of Mortality* when restoring HP of a creature at 0 HP, instead of rolling, use highest value of each die (spare dying with 30 ft bonus
        *Eyes of the Grave* as action, until end of next turn, know location of undead within 60 ft. (doesn't reveal capabilities or identity) (3 per rest)""")

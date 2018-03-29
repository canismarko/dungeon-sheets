from . import weapons

class Race():
    name = "Unknown"
    size = "medium"
    speed = 30
    proficiencies_text = tuple()
    weapon_proficiences = tuple()
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<self.name>"


# Dwarves
class Dwarf(Race):
    name = "Dwarf"
    size = "medium"
    speed = 25
    proficiencies_text = ('battleaxes', 'handaxes', 'throwing hammers', 'warhammers')
    weapon_proficiences = (weapons.Battleaxe, weapons.Handaxe,
                           weapons.ThrowingHammer, weapons.Warhammer)


class HillDwarf(Dwarf):
    name = "Hill Dwarf"


class MountainDwarf(Dwarf):
    name = "Mountain Dwarf"


# Elves
class Elf(Race):
    name = "Elf"
    size = "medium"
    speed = 30


class HighElf(Elf):
    name = "High Elf"
    weapon_proficiencies = (weapons.Longsword, weapons.Shortsword,
                           weapons.Shortbow, weapons.Longbow)
    proficiencies_text = ('longswords', 'shortswords', 'shortbows', 'longbows')


class WoodElf(Elf):
    name = "Wood Elf"
    weapon_proficiencies = (weapons.Longsword, weapons.Shortsword,
                           weapons.Shortbow, weapons.Longbow)
    proficiencies_text = ('longswords', 'shortswords', 'shortbows', 'longbows')


class DarkElf(Elf):
    name = "Dark Elf"
    weapon_proficiencies = (weapons.Rapier, weapons.Shortsword, weapons.HandCrossbow)
    proficiencies_text = ('repiers', 'shortswords', 'hand crossbows')


# Halflings
class Halfling(Race):
    name = "Halfling"
    size = "small"
    speed = 25


class LightfootHalfling(Halfling):
    name = "Lightfoot Halfling"


class StoutHalfling(Halfling):
    name = "Stout Halfling"


# Humans
class Human(Race):
    name = "Human"
    size = "medium"
    speed = 30


# Dragonborn
class Dragonborn(Race):
    name = "Dragonborn"
    size = "medium"
    speed = 30


# Gnomes
class Gnome(Race):
    name = "Gnome"
    size = "small"
    speed = 25


class ForestGnome(Gnome):
    name = "Forest Gnome"


class RockGnome(Gnome):
    name = "Rock Gnome"


# Half-elves
class HalfElf(Race):
    name = "Half-Elf"
    size = "medium"
    speed = 30


# Half-Orcs
class HalfOrc(Race):
    name = "Half-Orc"
    size = "medium"
    speed = 30


# Tielflings
class Tiefling(Race):
    name = "Tiefling"
    size = "medium"
    speed = 30

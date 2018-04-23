from . import weapons


__all__ = ('Dwarf', 'HillDwarf', 'MountainDwarf', 'Elf', 'HighElf',
           'WoodElf', 'DarkElf', 'Halfling', 'LightfootHalfling',
           'StoutHalfling', 'Human', 'Dragonborn', 'Gnome', 'ForestGnome',
           'RockGnome', 'HalfElf', 'HalfOrc', 'Tiefling')


class Race():
    name = "Unknown"
    size = "medium"
    speed = 30
    languages = ('Common', )
    proficiencies_text = tuple()
    weapon_proficiences = tuple()
    skill_proficiencies = ()
    strength_bonus = 0
    dexterity_bonus = 0
    constitution_bonus = 0
    intelligence_bonus = 0
    wisdom_bonus = 0
    charisma_bonus = 0
    hit_point_bonus = 0
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"<self.name>"


# Dwarves
class Dwarf(Race):
    name = "Dwarf"
    size = "medium"
    speed = 25
    languages = ("Common", "Dwarvish")
    constitution_bonus = 2
    proficiencies_text = ('battleaxes', 'handaxes', 'throwing hammers', 'warhammers')
    weapon_proficiences = (weapons.Battleaxe, weapons.Handaxe,
                           weapons.ThrowingHammer, weapons.Warhammer)


class HillDwarf(Dwarf):
    name = "Hill Dwarf"
    wisdom_bonus = 1
    hit_point_bonus = 1


class MountainDwarf(Dwarf):
    name = "Mountain Dwarf"
    strength_bonus = 2


# Elves
class Elf(Race):
    name = "Elf"
    size = "medium"
    speed = 30
    dexterity_bonus = 2
    skill_proficiencies = ('perception',)
    languages = ('Common', 'Elvish')


class HighElf(Elf):
    name = "High Elf"
    weapon_proficiencies = (weapons.Longsword, weapons.Shortsword,
                           weapons.Shortbow, weapons.Longbow)
    proficiencies_text = ('longswords', 'shortswords', 'shortbows', 'longbows')
    intelligence_bonus = 1
    languages = ('Common', 'Elvish', '[choose one]')


class WoodElf(Elf):
    name = "Wood Elf"
    weapon_proficiencies = (weapons.Longsword, weapons.Shortsword,
                           weapons.Shortbow, weapons.Longbow)
    proficiencies_text = ('longswords', 'shortswords', 'shortbows', 'longbows')
    wisdom_bonus = 1


class DarkElf(Elf):
    name = "Dark Elf"
    weapon_proficiencies = (weapons.Rapier, weapons.Shortsword, weapons.HandCrossbow)
    proficiencies_text = ('rapiers', 'shortswords', 'hand crossbows')
    charisma_bonus = 1


# Halflings
class Halfling(Race):
    name = "Halfling"
    size = "small"
    speed = 25
    dexterity_bonus = 2
    languages = ('Common', 'Halfling')


class LightfootHalfling(Halfling):
    name = "Lightfoot Halfling"
    charisma_bonus = 1


class StoutHalfling(Halfling):
    name = "Stout Halfling"
    constitution_bonus = 1


# Humans
class Human(Race):
    name = "Human"
    size = "medium"
    speed = 30
    strength_bonus = 1
    dexterity_bonus = 1
    constitution_bonus = 1
    intelligence_bonus = 1
    wisdom_bonus = 1
    charisma_bonus = 1
    languages = ("Common", '[choose one]')


# Dragonborn
class Dragonborn(Race):
    name = "Dragonborn"
    size = "medium"
    speed = 30
    strength_bonus = 2
    charisma_bonus = 1
    languages = ("Common", "Draconic")


# Gnomes
class Gnome(Race):
    name = "Gnome"
    size = "small"
    speed = 25
    intelligence_bonus = 2
    languages = ("Common", "Gnomish")


class ForestGnome(Gnome):
    name = "Forest Gnome"
    dexterity_bonus = 1


class RockGnome(Gnome):
    name = "Rock Gnome"
    constitution_bonus = 1


# Half-elves
class HalfElf(Race):
    name = "Half-Elf"
    size = "medium"
    speed = 30
    charisma_bonus = 2
    languages = ("Common", "Elvish", "[choose one]")


# Half-Orcs
class HalfOrc(Race):
    name = "Half-Orc"
    size = "medium"
    speed = 30
    strength_bonus = 2
    constitution_bonus = 1
    languages = ("Common", "Orc")


# Tielflings
class Tiefling(Race):
    name = "Tiefling"
    size = "medium"
    speed = 30
    intelligence_bonus = 1
    charisma_bonus = 2
    languages = ("Common", "Infernal")

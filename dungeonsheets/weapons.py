from .stats import mod_str

class Weapon():
    name = ""
    cost = "0 gp"
    base_damage = "1d4"
    bonus_damage = 0
    damage_type = "piercing"
    attack_bonus = 0
    weight = 1 # In lbs
    properties = "Light"
    ability = 'strength'
    is_finesse = False
    
    @property
    def damage(self):
        dam_str = str(self.base_damage)
        if self.bonus_damage != 0:
            dam_str += ' ' + mod_str(self.bonus_damage)
        return dam_str


class Club(Weapon):
    name = "Club"
    cost = "1 sp"
    base_damage = "1d4"
    damage_type = "bludgeoning"
    weight = 2
    properties = "Light"
    ability = 'strength'


class Dagger(Weapon):
    name = "Dagger"
    cost = "2 gp"
    base_damage = "1d4"
    damage_type = "piercing"
    weight = 1
    properties = "Finesse, light, thrown (range 20/60)"
    is_finesse = True
    ability = 'strength'


class Greatclub(Weapon):
    name = "Greatclub"
    cost = "2 sp"
    base_damage = "1d8"
    damage_type = "bludgeoning"
    weight = 10
    properties = "Two-handed"
    ability = 'strength'


class Handaxe(Weapon):
    name = "Handaxe"
    cost = "5 gp"
    base_damage = "1d6"
    damage_type = "slashing"
    weight = 2
    properties = "Light, thrown (range 20/60)"
    ability = 'strength'


class Javelin(Weapon):
    name = "Javelin"
    cost = "5 sp"
    base_damage = "1d6"
    damage_type = "piercing"
    weight = 2
    properties = "Thrown (range 30/120)"
    ability = 'strength'


class LightHammer(Weapon):
    name = "Light hammer"
    cost = "2 gp"
    base_damage = "1d4"
    damage_type = "bludgeoning"
    weight = 2
    properties = "Light, thrown (range 20/60)"
    ability = 'strength'


class Mace(Weapon):
    name = "Mace"
    cost = "5 gp"
    base_damage = "1d6"
    damage_type = "bludgeoning"
    weight = 4
    properties = ""
    ability = 'strength'


class Quarterstaff(Weapon):
    name = "Quarterstaff"
    cost = "2 sp"
    base_damage = "1d6"
    damage_type = "bludgeoning"
    weight = 4
    properties = "Versatile (1d8)"
    ability = 'strength'


class Sickle(Weapon):
    name = "Sickle"
    cost = "1 gp"
    base_damage = "1d4"
    damage_type = "slashing"
    weight = 2
    properties = "Light"
    ability = 'strength'


class Spear(Weapon):
    name = "Spear"
    cost = "1 gp"
    base_damage = "1d6"
    damage_type = "piercing"
    weight = 3
    properties = "Thrown (range 20/60), versatile (1d8)"
    ability = 'strength'


class LightCrossbow(Weapon):
    name = "Light crossbow"
    cost = "25 gp"
    base_damage = "1d8"
    damage_type = "piercing"
    weight = 5
    properties = "Ammunition (range 80/320, loading, two-handed"
    ability = 'dexterity'


class Dart(Weapon):
    name = "Dart"
    cost = "5 cp"
    base_damage = "1d4"
    damage_type = "piercing"
    weight = 0.25
    properties = "Finesse, thrown (range 20/60)"
    is_finesse = True
    ability = 'dexterity'


class Shortbow(Weapon):
    name = "Shortbow"
    cost = "25 gp"
    base_damage = "1d6"
    damage_type = "piercing"
    weight = 2
    properties = "Ammunition (range 80/320), two-handed"
    ability = 'dexterity'


class Sling(Weapon):
    name = "Sling"
    cost = "1 sp"
    base_damage = "1d4"
    damage_type = "bludgeoning"
    weight = 0
    properties = "Ammunition (range 30/120)"
    ability = 'dexterity'


class Battleaxe(Weapon):
    name = "Battleaxe"
    cost = "10 gp"
    base_damage = "1d8"
    damage_type = "slashing"
    weight = 4
    properties = "Versatile (1d10)"
    ability = 'strength'


class Flail(Weapon):
    name = "Flail"
    cost = "10gp"
    base_damage = "1d8"
    damage_type = "bludgeoning"
    weight = 2
    properties = ""
    ability = 'strength'


class Glaive(Weapon):
    name = "Glaive"
    cost = "20 gp"
    base_damage = "1d10"
    damage_type = "slashing"
    weight = 6
    properties = "Heavy, reach, two-handed"
    ability = 'strength'


class Greataxe(Weapon):
    name = "Greataxe"
    cost = "30 gp"
    base_damage = "1d12"
    damage_type = "slashing"
    weight = 7
    properties = "Heavy, two-handed"
    ability = 'strength'


class Greatsword(Weapon):
    name = "Greatsword"
    cost = "50 gp"
    base_damage = "2d6"
    damage_type = "slashing"
    weight = 6
    properties = "Heavy, two-handed"
    ability = 'strength'


class Halberd(Weapon):
    name = "Halberd"
    cost = "20 gp"
    base_damage = "1d10"
    damage_type = "slashing"
    weight = 6
    properties = "Heavy, reach, two-handed"
    ability = 'strength'


class Lance(Weapon):
    name = "Lance"
    cost = "10gp"
    base_damage = "1d12"
    damage_type = "piercing"
    weight = 6
    properties = "Reach, special"
    ability = 'strength'


class Longsword(Weapon):
    name = "Longsword"
    cost = "15 gp"
    base_damage = "1d8"
    damage_type = "slashing"
    weight = 3
    properties = "Versatile (1d10)"
    ability = 'strength'


class Maul(Weapon):
    name = "Maul"
    cost = "10 gp"
    base_damage = "2d6"
    damage_type = "bludgeoning"
    weight = 10
    properties = "Heavy, two-handed"
    ability = 'strength'


class Morningstar(Weapon):
    name = "Morningstar"
    cost = "15 gp"
    base_damage = "1d8"
    damage_type = "piercing"
    weight = 4
    properties = ""
    ability = 'strength'


class Pike(Weapon):
    name = "Pike"
    cost = "5 gp"
    base_damage = "1d10"
    damage_type = "piercing"
    weight = 18
    properties = "Heavy, reach, two-handed"
    ability = 'strength'


class Rapier(Weapon):
    name = "Rapier"
    cost = "25 gp"
    base_damage = "1d8"
    damage_type = "piercing"
    weight = 2
    properties = "Finesse"
    is_finesse = True
    ability = 'strength'


class Scimitar(Weapon):
    name = "Scimitar"
    cost = "25 gp"
    base_damage = "1d6"
    damage_type = "slashing"
    weight = 3
    properties = "Finesse, light"
    is_finesse = True
    ability = 'strength'


class Shortsword(Weapon):
    name = "Shortsword"
    cost = "10 gp"
    base_damage = "1d6"
    damage_type = "piercing"
    weight = 0
    properties = "Finesse, light"
    is_finesse = True
    ability = 'strength'


class ThrowingHammer(Weapon):
    name = "Throwing Hammer"
    cost = "15 gp"
    base_damage = '1d6'
    damage_type = "bludgeoning"
    weight = 4
    properties = "Thrown (range 60/120)"
    ability = "strength"


class Trident(Weapon):
    name = "Trident"
    cost = "5 gp"
    base_damage = "1d6"
    damage_type = "piercing"
    weight = 4
    properties = "Thrown (range 20/60), versatile (1d8)"
    ability = 'strength'


class WarPick(Weapon):
    name = "War pick"
    cost = "5 gp"
    base_damage = "1d8"
    damage_type = "piercing"
    weight = 2
    properties = ""
    ability = 'strength'


class Warhammer(Weapon):
    name = "Warhammer"
    cost = "15 gp"
    base_damage = "1d8"
    damage_type = "bludgeoning"
    weight = 2
    properties = "Versatile (1d10)"
    ability = 'strength'


class Whip(Weapon):
    name = "Whip"
    cost = "2 gp"
    base_damage = "1d4"
    damage_type = "slashing"
    weight = 3
    properties = "Finesse, reach"
    is_finesse = True
    ability = 'strength'


class Blowgun(Weapon):
    name = "Blowgun"
    cost = "10 gp"
    base_damage = "1"
    damage_type = "piercing"
    weight = 1
    properties = "Ammunition (range 25/100), loading"
    ability = 'dexterity'


class HandCrossbow(Weapon):
    name = "Crossbow, hand"
    cost = "75 gp"
    base_damage = "1d6"
    damage_type = "piercing"
    weight = 3
    properties = "Ammunition (range 30/120), light, loading"
    ability = 'dexterity'


class HeavyCrossbow(Weapon):
    name = "Crossbow, heavy"
    cost = "50 gp"
    base_damage = "1d10"
    damage_type = "piercing"
    weight = 18
    properties = "Ammunition (range 100/400), heaving, loading, two-handed"
    ability = 'strength'


class Longbow(Weapon):
    name = "Longbow"
    cost = "50 gp"
    base_damage = "1d8"
    damage_type = "piercing"
    weight = 2
    properties = "Ammunition (range 150/600), heavy, two-handed"
    ability = 'strength'


class Net(Weapon):
    name = "Net"
    cost = "1 gp"
    base_damage = "-"
    damage_type = ""
    weight = 3
    properties = "Special, thrown (range 5/15)"
    ability = 'strength'


# Some lists of weapons for easy proficiency resolution
simple_melee_weapons = (Club, Dagger, Greatclub, Handaxe, Javelin,
                        LightHammer, Mace, Quarterstaff, Sickle, Spear)
simple_ranged_weapons = (LightCrossbow, Dart, Shortbow, Sling)
simple_weapons = simple_melee_weapons + simple_ranged_weapons

martial_melee_weapons = (Battleaxe, Flail, Glaive, Greataxe,
                         Greatsword, Halberd, Lance, Longsword, Maul,
                         Morningstar, Pike, Rapier, Scimitar,
                         Shortsword, ThrowingHammer, Trident, WarPick,
                         Warhammer, Whip)
martial_ranged_weapons = (Blowgun, HandCrossbow, HeavyCrossbow,
                          Longbow, Net)
martial_weapons = martial_melee_weapons + martial_ranged_weapons

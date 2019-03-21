class Weapon():
    name = ""
    cost = "0 gp"
    base_damage = "1d4"
    damage_bonus = 0
    attack_bonus = 0
    damage_type = "p"
    weight = 1  # In lbs
    properties = ""
    ability = 'strength'
    is_finesse = False
    features_applied = False

    def __init__(self, wielder=None):
        self.wielder = wielder

    @classmethod
    def improved_version(cls, bonus):
        bonus = int(bonus)
        
        class NewWeapon(cls):
            name = f'+{bonus} ' + cls.name
            damage_bonus = bonus
            attack_bonus = bonus
            
        return NewWeapon

    def apply_features(self):
        if (not self.features_applied) and (self.wielder is not None):
            self.features_applied = True
            for f in self.wielder.features:
                f.weapon_func(self)

    @property
    def ability_mod(self):
        if self.wielder is None:
            return 0
        else:
            if self.is_finesse:
                return max(self.wielder.strength.modifier,
                           self.wielder.dexterity.modifier)
            else:
                return getattr(self.wielder, self.ability).modifier
        
    @property
    def attack_modifier(self):
        self.apply_features()
        mod = self.attack_bonus
        if self.wielder is not None:
            mod += self.ability_mod
            if self.wielder.is_proficient(self):
                mod += self.wielder.proficiency_bonus
        return mod
    
    @property
    def damage(self):
        self.apply_features()
        dam_str = str(self.base_damage)
        bonus = self.damage_bonus
        if self.wielder is not None:
            bonus += self.ability_mod
        if bonus != 0:
            dam_str += '{:+d}'.format(bonus)
        return dam_str

    def __str__(self):
        return self.name

    def __repr__(self):
        return "\"{:s}\"".format(self.name)


class MeleeWeapon(Weapon):
    name = "Melee Weapons"
    ability = 'strength'


class RangedWeapon(Weapon):
    name = "Ranged Weapons"
    ability = 'dexterity'


class SimpleWeapon(Weapon):
    name = "Simple Weapons"


class MartialWeapon(Weapon):
    name = "Martial Weapons"
    

class Club(SimpleWeapon, MeleeWeapon):
    name = "Club"
    cost = "1 sp"
    base_damage = "1d4"
    damage_type = "b"
    weight = 2
    properties = "Light"
    ability = 'strength'


class Dagger(SimpleWeapon, MeleeWeapon):
    name = "Dagger"
    cost = "2 gp"
    base_damage = "1d4"
    damage_type = "p"
    weight = 1
    properties = "Finesse, light, thrown (range 20/60)"
    is_finesse = True
    ability = 'strength'


class Greatclub(SimpleWeapon, MeleeWeapon):
    name = "Greatclub"
    cost = "2 sp"
    base_damage = "1d8"
    damage_type = "b"
    weight = 10
    properties = "Two-handed"
    ability = 'strength'


class Handaxe(SimpleWeapon, MeleeWeapon):
    name = "Handaxe"
    cost = "5 gp"
    base_damage = "1d6"
    damage_type = "s"
    weight = 2
    properties = "Light, thrown (range 20/60)"
    ability = 'strength'


class Javelin(SimpleWeapon, MeleeWeapon):
    name = "Javelin"
    cost = "5 sp"
    base_damage = "1d6"
    damage_type = "p"
    weight = 2
    properties = "Thrown (range 30/120)"
    ability = 'strength'


class LightHammer(SimpleWeapon, MeleeWeapon):
    name = "Light hammer"
    cost = "2 gp"
    base_damage = "1d4"
    damage_type = "b"
    weight = 2
    properties = "Light, thrown (range 20/60)"
    ability = 'strength'


class Mace(SimpleWeapon, MeleeWeapon):
    name = "Mace"
    cost = "5 gp"
    base_damage = "1d6"
    damage_type = "b"
    weight = 4
    properties = ""
    ability = 'strength'


class Quarterstaff(SimpleWeapon, MeleeWeapon):
    name = "Quarterstaff"
    cost = "2 sp"
    base_damage = "1d6"
    damage_type = "b"
    weight = 4
    properties = "Versatile (1d8)"
    ability = 'strength'


class Sickle(SimpleWeapon, MeleeWeapon):
    name = "Sickle"
    cost = "1 gp"
    base_damage = "1d4"
    damage_type = "s"
    weight = 2
    properties = "Light"
    ability = 'strength'


class Spear(SimpleWeapon, MeleeWeapon):
    name = "Spear"
    cost = "1 gp"
    base_damage = "1d6"
    damage_type = "p"
    weight = 3
    properties = "Thrown (range 20/60), versatile (1d8)"
    ability = 'strength'


class LightCrossbow(SimpleWeapon, RangedWeapon):
    name = "Light crossbow"
    cost = "25 gp"
    base_damage = "1d8"
    damage_type = "p"
    weight = 5
    properties = "Ammunition (range 80/320), loading, two-handed"
    ability = 'dexterity'


class Dart(SimpleWeapon, RangedWeapon):
    name = "Dart"
    cost = "5 cp"
    base_damage = "1d4"
    damage_type = "p"
    weight = 0.25
    properties = "Finesse, thrown (range 20/60)"
    is_finesse = True
    ability = 'dexterity'


class Shortbow(SimpleWeapon, RangedWeapon):
    name = "Shortbow"
    cost = "25 gp"
    base_damage = "1d6"
    damage_type = "p"
    weight = 2
    properties = "Ammunition (range 80/320), two-handed"
    ability = 'dexterity'


class Sling(SimpleWeapon, RangedWeapon):
    name = "Sling"
    cost = "1 sp"
    base_damage = "1d4"
    damage_type = "b"
    weight = 0
    properties = "Ammunition (range 30/120)"
    ability = 'dexterity'


class Battleaxe(MartialWeapon, MeleeWeapon):
    name = "Battleaxe"
    cost = "10 gp"
    base_damage = "1d8"
    damage_type = "s"
    weight = 4
    properties = "Versatile (1d10)"
    ability = 'strength'


class Flail(MartialWeapon, MeleeWeapon):
    name = "Flail"
    cost = "10gp"
    base_damage = "1d8"
    damage_type = "b"
    weight = 2
    properties = ""
    ability = 'strength'


class Glaive(MartialWeapon, MeleeWeapon):
    name = "Glaive"
    cost = "20 gp"
    base_damage = "1d10"
    damage_type = "s"
    weight = 6
    properties = "Heavy, reach, two-handed"
    ability = 'strength'


class Greataxe(MartialWeapon, MeleeWeapon):
    name = "Greataxe"
    cost = "30 gp"
    base_damage = "1d12"
    damage_type = "s"
    weight = 7
    properties = "Heavy, two-handed"
    ability = 'strength'


class Greatsword(MartialWeapon, MeleeWeapon):
    name = "Greatsword"
    cost = "50 gp"
    base_damage = "2d6"
    damage_type = "s"
    weight = 6
    properties = "Heavy, two-handed"
    ability = 'strength'


class Halberd(MartialWeapon, MeleeWeapon):
    name = "Halberd"
    cost = "20 gp"
    base_damage = "1d10"
    damage_type = "s"
    weight = 6
    properties = "Heavy, reach, two-handed"
    ability = 'strength'


class Lance(MartialWeapon, MeleeWeapon):
    name = "Lance"
    cost = "10gp"
    base_damage = "1d12"
    damage_type = "p"
    weight = 6
    properties = "Reach, special"
    ability = 'strength'


class Longsword(MartialWeapon, MeleeWeapon):
    name = "Longsword"
    cost = "15 gp"
    base_damage = "1d8"
    damage_type = "s"
    weight = 3
    properties = "Versatile (1d10)"
    ability = 'strength'


class Maul(MartialWeapon, MeleeWeapon):
    name = "Maul"
    cost = "10 gp"
    base_damage = "2d6"
    damage_type = "b"
    weight = 10
    properties = "Heavy, two-handed"
    ability = 'strength'


class Morningstar(MartialWeapon, MeleeWeapon):
    name = "Morningstar"
    cost = "15 gp"
    base_damage = "1d8"
    damage_type = "p"
    weight = 4
    properties = ""
    ability = 'strength'


class Pike(MartialWeapon, MeleeWeapon):
    name = "Pike"
    cost = "5 gp"
    base_damage = "1d10"
    damage_type = "p"
    weight = 18
    properties = "Heavy, reach, two-handed"
    ability = 'strength'


class Rapier(MartialWeapon, MeleeWeapon):
    name = "Rapier"
    cost = "25 gp"
    base_damage = "1d8"
    damage_type = "p"
    weight = 2
    properties = "Finesse"
    is_finesse = True
    ability = 'strength'


class Scimitar(MartialWeapon, MeleeWeapon):
    name = "Scimitar"
    cost = "25 gp"
    base_damage = "1d6"
    damage_type = "s"
    weight = 3
    properties = "Finesse, light"
    is_finesse = True
    ability = 'strength'


class Shortsword(MartialWeapon, MeleeWeapon):
    name = "Shortsword"
    cost = "10 gp"
    base_damage = "1d6"
    damage_type = "p"
    weight = 0
    properties = "Finesse, light"
    is_finesse = True
    ability = 'strength'


class ThrowingHammer(MartialWeapon, MeleeWeapon):
    name = "Throwing Hammer"
    cost = "15 gp"
    base_damage = '1d6'
    damage_type = "b"
    weight = 4
    properties = "Thrown (range 60/120)"
    ability = "strength"


class Trident(MartialWeapon, MeleeWeapon):
    name = "Trident"
    cost = "5 gp"
    base_damage = "1d6"
    damage_type = "p"
    weight = 4
    properties = "Thrown (range 20/60), versatile (1d8)"
    ability = 'strength'


class WarPick(MartialWeapon, MeleeWeapon):
    name = "War pick"
    cost = "5 gp"
    base_damage = "1d8"
    damage_type = "p"
    weight = 2
    properties = ""
    ability = 'strength'


class Warhammer(MartialWeapon, MeleeWeapon):
    name = "Warhammer"
    cost = "15 gp"
    base_damage = "1d8"
    damage_type = "b"
    weight = 2
    properties = "Versatile (1d10)"
    ability = 'strength'


class Whip(MartialWeapon, MeleeWeapon):
    name = "Whip"
    cost = "2 gp"
    base_damage = "1d4"
    damage_type = "s"
    weight = 3
    properties = "Finesse, reach"
    is_finesse = True
    ability = 'strength'


class Blowgun(MartialWeapon, RangedWeapon):
    name = "Blowgun"
    cost = "10 gp"
    base_damage = "1"
    damage_type = "p"
    weight = 1
    properties = "Ammunition (range 25/100), loading"
    ability = 'dexterity'


class HandCrossbow(MartialWeapon, RangedWeapon):
    name = "Crossbow, hand"
    cost = "75 gp"
    base_damage = "1d6"
    damage_type = "p"
    weight = 3
    properties = "Ammunition (range 30/120), light, loading"
    ability = 'dexterity'


class HeavyCrossbow(MartialWeapon, RangedWeapon):
    name = "Crossbow, heavy"
    cost = "50 gp"
    base_damage = "1d10"
    damage_type = "p"
    weight = 18
    properties = "Ammunition (range 100/400), heaving, loading, two-handed"
    ability = 'dexterity'


class Longbow(MartialWeapon, RangedWeapon):
    name = "Longbow"
    cost = "50 gp"
    base_damage = "1d8"
    damage_type = "p"
    weight = 2
    properties = "Ammunition (range 150/600), heavy, two-handed"
    ability = 'dexterity'


class Net(MartialWeapon, RangedWeapon):
    name = "Net"
    cost = "1 gp"
    base_damage = "-"
    damage_type = ""
    weight = 3
    properties = "Special, thrown (range 5/15)"
    ability = 'strength'

    
class Unarmed(MeleeWeapon):
    name = "Unarmed"
    cost = "0 gp"
    base_damage = "1"
    damage_type = "b"
    weight = 0
    properties = ""
    ability = "strength"


class SunBolt(RangedWeapon):
    name = "Sun Bolt"
    cost = "0 gp"
    base_damage = "1d4"
    damage_type = "r"
    weight = 0
    properties = "(range 20/60)"
    ability = 'dexterity'

    
# Custom weapons
class HeavyPunch(MeleeWeapon):
    base_damage = "1d4"
    name = "Heavy Punch"
    damage_type = 'b'
    damage_bonus = 10  # Heavy weapon master
    attack_bonus = -5  # Heavy weapon master


class Bite(MeleeWeapon):
    name = "Bite"
    base_damage = "1d4"
    damage_type = 'p'
    cost = "0 gp"
    weight = 0
    properties = ""
    ability = "strength"


class Talons(MeleeWeapon):
    name = 'Talons'
    base_damage = '1d4'
    damage_type = 's'
    cost = '0 gp'
    weight = 0
    properties = ''
    ability = 'strength'


class Claws(MeleeWeapon):
    name = 'Claws'
    base_damage = '1d4'
    damage_type = 's'
    cost = '0 gp'
    weight = 0
    properties = ''
    ability = 'strength'


class Firearm(RangedWeapon):
    name = 'Firearm'
    ability = 'dexterity'
    damage_type = 'p'
    
    
class Blunderbuss(Firearm):
    name = 'Blunderbuss'
    base_damage = '2d8'
    cost = '300 gp'
    weight = 10
    properties = "Ammunition (range 15/60), Reload 1, Misfire 2"


class Pistol(Firearm):
    name = 'Pistol'
    base_damage = '1d10'
    cost = '150 gp'
    weight = 3
    properties = "Ammunition (range 60/240), Reload 4, Misfire 1"

    
class Musket(Firearm):
    name = 'Musket'
    base_damage = '1d12'
    cost = '300'
    weight = 10
    properties = "Ammunition (range 120/480), Two-Handed, Reload 1, Misfire 2"


# Magic Items
class FlameTongue(Greatsword):
    name = "Flame Tongue +1"
    damage_bonus = 1
    attack_bonus = 1
    base_damage = "4d6"
    damage_type = 'f'


class SpearOfLightning(Spear):
    name = "Spear +1"
    damage_bonus = 1
    attack_bonus = 1


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

monk_weapons = (Shortsword, Unarmed, Club, Dagger, Handaxe, Javelin,
                LightHammer, Mace, Quarterstaff, Sickle, Spear, SunBolt)

firearms = (Firearm, Blunderbuss, Pistol, Musket)

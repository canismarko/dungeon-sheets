from .ranger import Archery, Defense, Dueling, TwoWeaponFighting
from .features import Feature, FeatureSelector
from .. import (weapons, armor)

# Features added for all PHB classes
# SCAG and XGTE needed


# PHB
class GreatWeaponFighting(Feature):
    """When you roll a 1 or 2 on a damage die for an attack you make with a melee
    weapon that you are wielding with two hands, you can reroll the die and
    must use the new roll, even if the new roll is a 1 or a 2. The weapon must
    have the two-handed or versatile property for you to gain this benefit.

    """
    name = "Fighting Style (Great Weapon Fighting)"
    source = "Fighter"


class Protection(Feature):
    """When a creature you can see attacks a target other than you that is within
    5 feet of you, you can use your reaction to impose disadvantage on the
    attack roll. You must be wielding a shield.

    """
    name = "Fighting Style (Protection)"
    source = "Fighter"
    

class FighterFightingStyle(FeatureSelector):
    """
    Select a Fighting Style by choosing in feature_choices:

    archery
 
    defense

    dueling

    great-weapon fighting

    protection

    two-weapon fighting
    """
    options = {'archery': Archery,
               'defense': Defense,
               'dueling': Dueling,
               'great': GreatWeaponFighting,
               'great-weapon fighting': GreatWeaponFighting,
               'projection': Protection,
               'two-weapon fighting': TwoWeaponFighting,
               'two-weapon': TwoWeaponFighting,
               'dual wield': TwoWeaponFighting}
    name = "Fighting Style (Select One)"
    source = "Fighter"
    

class SecondWind(Feature):
    """You have a limited well of stamina that you can draw on to protect yourself
    from harm. On your turn, you can use a bonus action to regain hit points
    equal to 1d10 + your fighter level. Once you use this feature, you must
    finish a short or long rest before you can use it again

    """
    name = "Second Wind"
    source = "Fighter"


class ActionSurge(Feature):
    """Starting at 2nd level, you can push yourself beyond your normal limits for a
    moment. On your turn, you can take one additional action on top of your
    regular action and a possible bonus action.

    Once you use this feature, you must finish a short or long rest before you
    can use it again. Starting at 17th level, you can use it twice before a
    rest, but only once on the same turn.

    """
    name = "Action Surge"
    source = "Fighter"


class ExtraAttackFighter(Feature):
    """Beginning at 5th level, you can attack twice, instead of once, whenever you
    take the Attack action on your turn. The number of attacks increases to
    three when you reach 11th level in this class and to four when you reach
    20th level in this class.

    """
    _name = "Extra Attack"
    source = "Fighter"

    @property
    def name(self):
        level = self.owner.Fighter.level
        if level < 11:
            return self._name + ' (2x)'
        elif level < 20:
            return self._name + ' (3x)'
        else:
            return self._name + ' (4x)'


class Indomitable(Feature):
    """Beginning at 9th level, you can reroll a saving throw that you fail. If you
    do so, you must use the new roll, and you can’t use this feature again
    until you finish a long rest.

    You can use this feature twice between long rests starting at 13th level
    and three times between long rests starting at 17th level.

    """
    _name = "Indomitable"
    source = "Fighter"

    @property
    def name(self):
        level = self.owner.Fighter.level
        if level < 13:
            return self._name + ' (1x/LR)'
        elif level < 17:
            return self._name + ' (2x/LR)'
        else:
            return self._name + ' (3x/LR)'


# Champion
class ImprovedCritical(Feature):
    """Beginning when you choose this archetype at 3rd level, your weapon attacks
    score a critical hit on a roll of 19 or 20.

    """
    name = "Improved Critical"
    source = "Fighter (Champion)"


class RemarkableAthelete(Feature):
    """Starting at 7th level, you can add half your proficiency bonus (round up)
    to any Strength, Dexterity, or Constitution check you make that doesn’t
    already use your proficiency bonus.

    In addition, when you make a running long jump, the distance you can cover
    increases by a number of feet equal to your Strength modifier.

    """
    name = "Remarkable Athelete"
    source = "Fighter (Champion)"


class AdditionalFightingStyle(FeatureSelector):
    """
    Select a Fighting Style by choosing in feature_choices:

    archery 2
 
    defense 2

    dueling 2

    great-weapon fighting 2

    protection 2

    two-weapon fighting 2
    """
    options = {'archery 2': Archery,
               'defense 2': Defense,
               'dueling 2': Dueling,
               'great 2': GreatWeaponFighting,
               'great-weapon fighting 2': GreatWeaponFighting,
               'projection 2': Protection,
               'two-weapon fighting 2': TwoWeaponFighting,
               'two-weapon 2': TwoWeaponFighting,
               'dual wield 2': TwoWeaponFighting}
    name = "Fighting Style (Select One)"
    source = "Fighter (Champion)"


class SuperiorCritical(Feature):
    """Starting at 15th level, your weapon attacks score a critical hit on a roll
    of 18-20 .
    """
    name = "Superior Critical"
    source = "Fighter (Champion)"

    
class Survivor(Feature):
    """At 18th level, you attain the pinnacle of resilience in battle. At the
    start of each of your turns, you regain hit points equal to 5 + your
    Constitution modifier if you have no more than half of your hit points
    left. You don’t gain this benefit if you have 0 hit points.

    """
    name = "Survivor"
    source = "Fighter (Champion)"


# Battle Master
class CombatSuperiority(Feature):
    """When you choose this archetype at 3rd level, you learn maneuvers that are
    fueled by special dice called superiority dice.

    **Maneuvers**: You learn three maneuvers of your choice, which are detailed
    under “Maneuvers” below. Many maneuvers enhance an attack in some way. You
    can use only one maneuver per attack. You learn two additional maneuvers
    of your choice at 7th, 10th, and 15th level. Each time you learn new
    maneuvers, you can also replace one maneuver you know with a different one.

    **Superiority Dice**: You have four superiority dice, which are d8s. A
    superiority die is expended when you use it. You regain all of your
    expended superiority dice when you finish a short or long rest. You gain
    another superiority die at 7th level and one more at 15th level.

    **Saving Throws**: Some of your maneuvers require your target to make a
    saving throw to resist the maneuver’s effects. The saving throw DC is
    calculated as follows:

    Maneuver save DC = 8 + your proficiency bonus + your Strength or Dexterity
    modifier (your choice)

    """
    _name = "Combat Superiority"

    @property
    def name(self):
        level = self.owner.Fighter.level
        if level < 10:
            return self._name + ' (d8)'
        elif level < 18:
            return self._name + ' (d10)'
        else:
            return self._name + ' (d12)'


class StudentOfWar(Feature):
    """At 3rd level, you gain proficiency with one type of artisan’s tools of your
    choice.

    """
    name = "Student of War"
    source = "Fighter (Battle Master)"


class KnowYourEnemy(Feature):
    """Starting at 7th level, if you spend at least 1 minute observing or
    interacting with another creature outside combat, you can learn certain
    information about its capabilities compared to your own. The DM tells you
    if the creature is your equal, superior, or inferior in regard to two of
    the following characteristics of your choice:

    --Strength score

    --Dexterity score

    --Constitution score

    --Armor Class

    --Current hit points

    --Total class levels (if any)

    --Fighter class levels (if any)
    """
    name = "Know Your Enemy"
    source = "Fighter (Battle Master)"
    
        
class Relentless(Feature):
    """Starting at 15th level, when you roll initiative and have no superiority
    dice remaining, you regain 1 superiority die.

    """
    name = "Relentless"
    source = "Fighter (Battle Master)"


# Maneuvers
class Maneuver(Feature):
    """
    A generic Maneuver
    """
    name = "Maneuver"
    source = "Fighter Maneuver (Battle Master)"


class CommandersStrike(Maneuver):
    """When you take the Attack action on your turn, you can forgo one of your
    attacks and use a bonus action to direct one of your companions to
    strike. When you do so, choose a friendly creature who can see or hear you
    and expend one superiority die. That creature can immediately use its
    reaction to make one weapon attack, adding the superiority die to the
    attack’s damage roll.

    """
    name = "Commander's Strike"


class DisarmingStrike(Maneuver):
    """When you hit a creature with a weapon attack, you can expend one
    superiority die to attempt to disarm the target, forcing it to drop one
    item o f your choice that it’s holding. You add the superiority die to the
    attack’s damage roll, and the target must make a Strength saving throw. On
    a failed save, it drops the object you choose. The object lands at its
    feet.

    """
    name = "Disarming Strike"


class DistractingStrike(Maneuver):
    """When you hit a creature with a weapon attack, you can expend one
    superiority die to distract the creature, giving your allies an
    opening. You add the superiority die to the attack’s damage roll. The next
    attack roll against the target by an attacker other than you has advantage
    if the attack is made before the start of your next turn.

    """
    name = "Distracting Strike"


class EvasiveFootwork(Maneuver):
    """When you move, you can expend one superiority die, rolling the die and
    adding the number rolled to your AC until you stop moving.

    """
    name = "Evasive Footwork"


class FeintingAttack(Maneuver):
    """You can expend one superiority die and use a bonus action on your turn to
    feint, choosing one creature within 5 feet of you as your target. You have
    advantage on your next attack roll against that creature. If that attack
    hits, add the superiority die to the attack’s damage roll.

    """
    name = "Feinting Attack"


class GoadingAttack(Maneuver):
    """When you hit a creature with a weapon attack, you can expend one
    superiority die to attempt to goad the target into attacking you. You add
    the superiority die to the attack’s damage roll, and the target must make a
    W isdom saving throw. On a failed save, the target has disadvantage on all
    attack rolls against targets other than you until the end of your next
    turn.

    """
    name = "Goading Attack"


class LungingAttack(Maneuver):
    """When you make a melee weapon attack on your turn, you can expend one
    superiority die to increase your reach for that attack by 5 feet. If you
    hit, you add the superiority die to the attack’s damage roll.

    """
    name = "Lunging Attack"


class ManeuveringAttack(Maneuver):
    """When you hit a creature with a weapon attack, you can expend one
    superiority die to maneuver one o f your comrades into a more advantageous
    position. You add the superiority die to the attack’s damage roll, and you
    choose a friendly creature who can see or hear you. That creature can use
    its reaction to move up to half its speed without provoking opportunity
    attacks from the target of your attack.

    """
    name = "Maneuvering Attack"


class MenacingAttack(Maneuver):
    """When you hit a creature with a weapon attack, you can expend one
    superiority die to attempt to frighten the target. You add the superiority
    die to the attack’s damage roll, and the target must make a Wisdom saving
    throw. On a failed save, it is frightened of you until the end o f your
    next turn.

    """
    name = "Menacing Attack"


class Parry(Maneuver):
    """When another creature damages you with a melee attack, you can use your
    reaction and expend one superiority die to reduce the damage by the number
    you roll on your superiority die + your Dexterity modifier.

    """
    name = "Parry"


class PrecisionAttack(Maneuver):
    """When you make a weapon attack roll against a creature, you can expend one
    superiority die to add it to the roll. You can use this maneuver before or
    after making the attack roll, but before any effects of the attack are
    applied

    """
    name = "Precision Attack"


class PushingAttack(Maneuver):
    """When you hit a creature with a weapon attack, you can expend one
    superiority die to attempt to drive the target back. You add the
    superiority die to the attack's damage roll, and if the target is Large or
    smaller, it must make a Strength saving throw. On a failed save, you push
    the target up to 15 feet away from you.

    """
    name = "Pushing Attack"


class Rally(Maneuver):
    """On your turn, you can use a bonus action and expend one superiority die to
    bolster the resolve of one of your companions. When you do so, choose a
    friendly creature who can see or hear you. That creature gains temporary
    hit points equal to the superiority die roll + your Charisma modifier.

    """
    name = "Rally"


class Riposte(Maneuver):
    """When a creature misses you with a melee attack, you can use your reaction
    and expend one superiority die to make a melee weapon attack against the
    creature. If you hit, you add the superiority die to the attack's damage
    roll

    """
    name = "Riposte"


class SweepingAttack(Maneuver):
    """When you hit a creature with a melee weapon attack, you can expend one
    superiority die to attempt to damage another creature with the same
    attack. Choose another creature within 5 feet of the original target and
    within your reach. If the original attack roll would hit the second
    creature, it takes damage equal to the number you roll on your superiority
    die. The damage is of the same type dealt by the original attack. Trip

    """
    name = "Sweeping Attack"


class TripingAttack(Maneuver):
    """When you hit a creature with a weapon attack, you can expend one
    superiority die to attempt to knock the target down. You add the
    superiority die to the attack’s damage roll, and if the target is Large or
    smaller, it must make a Strength saving throw. On a failed save, you knock
    the target prone

    """
    name = "Triping Attack"


# Eldritch Knight
class EldritchKnightSpellcasting(Feature):
    """You know three 1st-level wizard spells of your choice, two of which you
    must choose from the abjuration and evocation spells on the wizard spell
    list.

    The Spells Known column of the Eldritch Knight Spellcasting table shows
    when you learn more wizard spells of 1st level or higher. Each of these
    spells must be an abjuration or evocation spell of your choice, and must be
    of a level for which you have spell slots. For instance, when you reach 7th
    level in this class, you can learn one new spell of 1st or 2nd level.

    The spells you learn at 8th, 14th, and 20th level can come from any school
    of magic.

    Whenever you gain a level in this class, you can replace one of the wizard
    spells you know with another spell o f your choice from the wizard spell
    list. The new spell must be of a level for which you have spell slots, and
    it must be an abjuration or evocation spell, unless you’re replacing the
    spell you gained at 8th, 14th, or 20th level.

    """
    name = "Spellcasting"
    source = "Fighter (Eldritch Knight)"


class WeaponBond(Feature):
    """At 3rd level, you learn a ritual that creates a magical bond between
    yourself and one weapon. You perform the ritual over the course of 1 hour,
    which can be done during a short rest. The weapon must be within your reach
    throughout the ritual, at the conclusion of which you touch the weapon and
    forge the bond.

    Once you have bonded a weapon to yourself, you can’t be disarmed of that
    weapon unless you are incapacitated. If it is on the same plane of
    existence, you can summon that weapon as a bonus action on your turn,
    causing it to teleport instantly to your hand.

    You can have up to two bonded weapons, but can summon only one at a time
    with your bonus action. If you attempt to bond with a third weapon, you
    must break the bond with one of the other two.

    """
    name = "Weapon Bond"
    source = "Fighter (Eldritch Knight)"


class WarMagic(Feature):
    """Beginning at 7th level, when you use your action to cast a cantrip, you can
    make one weapon attack as a bonus action.

    """
    name = "War Magic"
    source = "Fighter (Eldritch Knight)"


class EldritchStrike(Feature):
    """At 10th level, you learn how to make your weapon strikes undercut a
    creature’s resistance to your spells. When you hit a creature with a weapon
    attack, that creature has disadvantage on the next saving throw it makes
    against a spell you cast before the end of your next turn.

    """
    name = "Eldritch Strike"
    source = "Fighter (Eldritch Knight)"


class ArcaneCharge(Feature):
    """At 15th level, you gain the ability to teleport up to 30 feet to an
    unoccupied space you can see when you use your Action Surge. You can
    teleport before or after the additional action.

    """
    name = "Arcane Charge"
    source = "Fighter (Eldritch Knight)"


class ImprovedWarMagic(Feature):
    """Starting at 18th level, when you use your action to cast a spell, you can
    make one weapon attack as a bonus action.

    """
    name = "Improved War Magic"
    source = "Fighter (Eldritch Knight)"


# Gunslinger
class Gunsmith(Feature):
    """Upon choosing this archetype at 3rd level, you gain proficiency with
    Tinker's Tools. You may use them to craft ammunition at half the cost,
    repair damaged firearms, or even draft and create new ones (DM's
    discretion). Some extremely experimental and intricate firearms are only
    available through crafting.

    """
    name = "Gunsmith"
    source = "Fighter (Gunslinger)"


class AdeptMarksman(Feature):
    """When you choose this archetype at 3rd level, you learn to perform powerful
    trick shots to disable or damage your opponents using your firearms.

    **Trick Shots**: You learn two trick shots of your choice, which are detailed under "Trick Shots" below. 
    If you have not already, add them by name to "features" in your character's .py file.

    Many maneuvers enhance an attack in some way. Each use of a trick shot must be declared before the attack roll is made. You can use only one trick shot per attack.

    You learn an additional trick shot of your choice at 7th, 10th, 15th, and
    18th level. Each time you learn a new trick shot, you can also replace one
    trick shot you know with a different one.
    
    Grit. You gain a number of grit points equal to your Wisdom modifier
    (minimum of 1). You regain 1 expended grit point each time you roll a 20 on
    the d20 roll for an attack with a firearm, or deal a killing blow with a
    firearm to a creature of significant threat (DM’s discretion). You regain
    all expended grit points after a short or long rest.

    Saving Throws. Some of your trick shots require your targets to make a
    saving throw to resist the trick shot’s effects. The saving throw DC is
    calculated as follows:

   Trick Shot save DC = 8 + your proficiency bonus + your Dexterity modifier

    Firearm Properties Firearms are a new and volatile technology, and as such
    bring their own unique set of weapon properties. Some properties are
    followed by a number, and this number signifies an element of that property
    (outlined below). These properties replace the optional ones presented in
    the Dungeon Master’s Guide. Firearms are ranged weapons.

    Reload. The weapon can be fired a number of times equal to its Reload score
    before you must spend 1 attack or 1 action to reload. You must have one
    free hand to reload a firearm.

    Misfire. Whenever you make an attack roll with a firearm, and the dice roll
    is equal to or lower than the weapon’s Misfire score, the weapon
    misfires. The attack misses, and the weapon cannot be used again until you
    spend an action to try and repair it. To repair your firearm, you must make
    a successful Tinker’s Tools check (DC equal to 8 + misfire score). If your
    check fails, the weapon is broken and must be mended out of combat at a
    quarter of the cost of the firearm. Creatures who use a firearm without
    being proficient increase the weapon’s misfire score by 1.

    Explosive. Upon a hit, everything within 5 ft of the target must make a
    Dexterity saving throw (DC equal to 8 + your proficiency bonus + your
    Dexterity modifier) or suffer 1d8 fire damage. If the weapon misses, the
    ammunition fails to detonate, or bounces away harmlessly before doing so.

    Ammunition All firearms require ammunition to make an attack, and due to
    their rare nature, ammunition may be near impossible to find or
    purchase. However, if materials are gathered, you can craft ammunition
    yourself using your Tinker’s Tools at half the cost. Each firearm uses its
    own unique ammunition and is generally sold or crafted in batches listed
    below next to the price.

    """
    name = "Adept Marksman"
    source = "Fighter (Gunslinger"


class QuickDraw(Feature):
    """When you reach 7th level, you add your proficiency bonus to your
    initiative. You can also stow a firearm, then draw another firearm as a
    single object interaction on your turn.

    """
    name = "Quick Draw"
    source = "Fighter (Gunslinger)"


class RapidRepair(Feature):
    """Upon reaching 10th level, you learn how to quickly attempt to fix a jammed
    gun. You can spend a grit point to attempt to repair a misfired (but not
    broken) firearm as a bonus action.

    """
    name = "Rapid Repair"
    source = "Fighter (Gunslinger)"


class LightningReload(Feature):
    """Starting at 15th level, you can reload any firearm as a bonus action.

    """
    name = "Lightning Repaid"
    source = "Fighter (Gunslinger)"


class ViciousIntent(Feature):
    """At 18th level, your firearm attacks score a critical hit on a roll of 19-20,
    and you regain a grit point on a roll of 19 or 20 on a d20 attack roll.

    """
    name = "Vicious Intent"
    source = "Fighter (Gunslinger)"


class HemorrhagingCritical(Feature):
    """Upon reaching 18th level, whenever you score a critical hit on an attack
    with a firearm, the target additionally suffers half of the damage from the
    attack at the end of its next turn.

    """
    name = "Hemorrhaging Critical"
    source = "Fighter (Gunslinger)"


class BullyingShot(Feature):
    """You can use the powerful blast and thundering sound of your firearm to shake
    the resolve of a creature. You can expend one grit point while making a
    Charisma (Intimidation) check to gain advantage on the roll.

    """
    name = "Bullying Shot"
    source = "Gunslinger (Trick Shot)"


class DazingShot(Feature):
    """When you make a firearm attack against a creature, you can expend one grit
    point to attempt to dizzy your opponent. On a hit, the creature suffers
    normal damage and must make a Constitution saving throw or suffer
    disadvantage on attacks until the end of their next turn.

    """
    name = "Dazing Shot"
    source = "Gunslinger (Trick Shot)"


class DeadeyeShot(Feature):
    """When you make a firearm attack against a creature, you can expend one grit
    point to gain advantage on the attack roll.

    """
    name = "Deadeye Shot"
    source = "Gunslinger (Trick Shot)"


class DisarmingShot(Feature):
    """When you make a firearm attack against a creature, you can expend one grit
    point to attempt to shoot an object from their hands. On a hit, the
    creature suffers normal damage and must succeed on a Strength saving throw
    or drop 1 held object of your choice and have that object be pushed 10 feet
    away from you.

    """
    name = "Disarming Shot"
    source = "Gunslinger (Trick Shot)"


class ForcefulShot(Feature):
    """When you make a firearm attack against a creature, you can expend one grit
    point to attempt to trip them up and force them back. On a hit, the
    creature suffers normal damage and must succeed on a Strength saving throw
    or be pushed 15 feet away from you.

    """
    name = "Forceful Shot"
    source = "Gunslinger (Trick Shot)"


class PiercingShot(Feature):
    """When you make a firearm attack against a creature, you can expend one grit
    point to attempt to fire through multiple opponents. The initial attack
    gains a +1 to the firearm’s misfire score. On a hit, the creature suffers
    normal damage and you make an attack roll with disadvantage against every
    creature in a line directly behind the target within your first range
    increment. Only the initial attack can misfire.

    """
    name = "Piercing Shot"
    source = "Gunslinger (Trick Shot)"


class WingingShot(Feature):
    """When you make a firearm attack against a creature, you can expend one grit
    point to attempt to topple a moving target. On a hit, the creature suffers
    normal damage and must make a Strength saving throw or be knocked prone.

    """
    name = "Winging Shot"
    source = "Gunslinger (Trick Shot)"

    
class ViolentShot(Feature):
    """When you make a firearm attack against a creature, you can expend one or
    more grit points to enhance the volatility of the attack. For each grit
    point expended, the attack gains a +2 to the firearm’s misfire score. If
    the attack hits, you can roll one additional weapon damage die per grit
    point spent when determining the damage.

    """
    name = "Violent Shot"
    source = "Gunslinger (Trick Shot)"

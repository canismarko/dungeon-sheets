from dungeonsheets import spells, weapons
from dungeonsheets.features.features import Feature


class UnarmoredDefenseMonk(Feature):
    """Beginning at 1st level, while you are wearing no armor and not
    wearing a shield, your AC equals 10 + your Dexterity modifier +
    your Wisdom modifier.

    This bonus is computed in the AC given on the Character Sheet
    above.

    """

    name = "Unarmored Defense"
    source = "Monk"


class MartialArts(Feature):
    """At 1st level, your practice of martial arts gives you mastery of
    combat styles that use unarmed strikes and monk weapons, which are
    shortswords and any simple melee weapons that don't have the
    two-handed or heavy property. You gain the following benefits
    while you are unarmed or wielding only monk weapons and you aren't
    wearing armor or wielding a shield:

    - You can use Dexterity instead of Strength for the attack and
      damage rolls of your unarmed strikes and monk weapons.
    - You can roll a d4 in place of the normal damage of your unarmed
      strike or monk weapon. This die changes as you gain monk levels,
      as shown in the Martial Arts column of the Monk table.
    - When you use the Attack action with an unarmed strike or a monk
      weapon on your turn, you can make one unarmed strike as a bonus
      action. For example, if you take the Attack action and attack
      with a quarterstaff, you can also make an unarmed strike as a
      bonus action, assuming you haven't already taken a bonus action
      this turn.

    Certain monasteries use specializepd forms of the monk
    weapons. For example, you might use a club that is two lengths of
    w ood connected by a short chain (called a nunchaku) or a sickle
    with a shorter, straighter blade (called a kama). Whatever name
    you use for a monk weapon, you can use the game statistics
    provided for

    """

    name = "Martial Arts"
    source = "Monk"
    die = "d4"

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """Update increasing damage dice and DEX mod of Monk weapons"""
        is_monk_weapon = any([isinstance(weapon, w) for w in weapons.monk_weapons])
        level = self.owner.Monk.level
        if not is_monk_weapon:
            return weapon
        self.die = "d4"
        if level >= 5:
            self.die = "d6"
        if level >= 11:
            self.die = "d8"
        if level >= 17:
            self.die = "d10"
        # check if new damage is better than default
        if int(self.die[1:]) > int(weapon.base_damage.split("d")[-1]):
            weapon.base_damage = "1" + str(self.die)
        weapon.is_finesse = True


class Ki(Feature):
    """Starting at 2nd level, your training allows you to harness the
    mystic energy of ki. Your access to this energy is represented by
    a number of ki points. Your monk level determines the number of
    points you have, as shown in the Ki Points column of the Monk
    table. You can spend these points to fuel various ki features.

    You start knowing three such features: Flurry of Blows, Patient
    Defense, and Step of the Wind. You learn more ki features as you
    gain levels in this class. When you spend a ki point, it is
    unavailable until you finish a short or long rest, at the end of
    which you draw all of your expended ki back into yourself. You
    must spend at least 30 minutes of the rest meditating to regain
    your ki points.

    Some of your ki features require your target to make a saving
    throw to resist the feature's effects. The saving throw DC is
    calculated as follows: Ki save DC = 8 + your proficiency bonus +
    your Wisdom modifier

    """

    _name = "Ki"
    source = "Monk"

    @property
    def name(self):
        num = self.owner.Monk.level
        DC = 8 + self.owner.proficiency_bonus + self.owner.wisdom.modifier
        return self._name + " ({:d} pts, DC={:d})".format(num, DC)


class FlurryOfBlows(Feature):
    """Immediately after you take the Attack action on your turn, you can spend 1
    ki point to make two unarmed strikes as a bonus action

    """

    name = "Flurry of Blows"
    source = "Monk"


class PatientDefense(Feature):
    """You can spend 1 ki point to take the Dodge action as a bonus action on your
    turn

    """

    name = "Patient Defense"
    source = "Monk"


class StepOfTheWind(Feature):
    """You can spend 1 ki point to take the Disengage or Dash action as a bonus
    action on your turn, and your jump distance is doubled for the turn

    """

    name = "Step of the Wind"
    source = "Monk"


class UnarmoredMovement(Feature):
    """Starting at 2nd level, your speed increases by 10 feet while you are not
    wearing armor or wielding a shield. This bonus increases when you reach
    certain monk levels, as shown in the Monk table.

    At 9th level, you gain the ability to move along vertical surfaces and
    across liquids on your turn without falling during the move.

    """

    name = "Unarmored Movement"
    source = "Monk"

    @property
    def speed_bonus(self):
        level = self.owner.Monk.level
        _speed_bonus = 10
        if level >= 6:
            _speed_bonus = 15
        if level >= 10:
            _speed_bonus = 20
        if level >= 14:
            _speed_bonus = 25
        if level >= 18:
            _speed_bonus = 30
        return _speed_bonus


class DeflectMissiles(Feature):
    """Starting at 3rd level, you can use your reaction to deflect or
    catch the missile when you are hit by a ranged weapon attack. When
    you do so, the damage you take from the attack is reduced by 1d10
    + your Dexterity modifier + your monk level. If you reduce the
    damage to 0, you can catch the missile if it is small enough for
    you to hold in one hand and you have at least one hand free.

    If you catch a missile in this way, you can spend 1 ki point to
    make a ranged attack with the weapon or piece of ammunition you
    just caught, as part of the same reaction. You make this attack
    with proficiency, regardless of your weapon proficiencies, and the
    missile counts as a monk weapon for the attack

    """

    _name = "Deflect Missiles"
    source = "Monk"

    @property
    def name(self):
        mod = self.owner.dexterity.modifier + self.owner.Monk.level
        return self._name + " (1d10+{:d})".format(mod)


class SlowFall(Feature):
    """Beginning at 4th level, you can use your reaction when you fall to
    reduce any falling damage you take by an amount equal to five
    times your monk level.

    """

    name = "Slow Fall"
    source = "Monk"


class ExtraAttackMonk(Feature):
    """Beginning at 5th level, you can attack twice, instead of once,
    whenever you take the Attack action on your turn

    """

    name = "Extra Attack (2x)"
    source = "Monk"


class StunningStrike(Feature):
    """Starting at 5th level, you can interfere with the flow of ki in an
    opponent's body. When you hit another creature with a melee weapon
    attack, you can spend 1 ki point to attempt a stunning strike. The
    target must succeed on a Constitution saving throw or be stunned
    until the end of your next turn

    """

    name = "Stunning Strike"
    source = "Monk"


class KiEmpoweredStrikes(Feature):
    """Starting at 6th level, your unarmed strikes count as magical for
    the purpose of overcoming resistance and immunity to nonmagical
    attacks and damage

    """

    name = "Ki-Empowered Strikes"
    source = "Monk"


class StillnessOfMind(Feature):
    """Starting at 7th level, you can use your action to end one effect on
    yourself that is causing you to be charmed or frightened

    """

    name = "Stillness of Mind"
    source = "Monk"


class PurityOfBody(Feature):
    """At 10th level, your mastery of the ki flowing through you makes you
    immune to disease and poison.

    """

    name = "Purity of Body"
    source = "Monk"


class TongueOfTheSunAndMoon(Feature):
    """Starting at 13th level, you learn to touch the ki of other minds so
    that you understand all spoken languages. Moreover, any creature
    that can understand a language can understand what you say.

    """

    name = "Tongue of the Sun and Moon"
    source = "Monk"


class DiamondSoul(Feature):
    """Beginning at 14th level, your mastery of ki grants you proficiency
    in all saving throws. Additionally, whenever you make a saving
    throw and fail, you can spend 1 ki point to reroll it and take the
    second result.

    """

    name = "Diamond Soul"
    source = "Monk"


class TimelessBody(Feature):
    """At 15th level, your ki sustains you so that you suffer none of the
    frailty of old age, and you can't be aged magically. You can still
    die of old age, however. In addition, you no longer need food or
    water.

    """

    name = "Timeless Body"
    source = "Monk"


class EmptyBody(Feature):
    """Beginning at 18th level, you can use your action to spend 4 ki
    points to become invisible for 1 minute. During that time, you
    also have resistance to all damage but force damage. Additionally,
    you can spend 8 ki points to cast the astral projection spell,
    without needing material components. When you do so, you can't
    take any other creatures with you.

    """

    name = "Empty Body"
    source = "Monk"


class PerfectSelf(Feature):
    """At 20th level, when you roll for initiative and have no ki points
    remaining, you regain 4 ki points.

    """

    name = "Perfect Self"
    source = "Monk"


# Way of the Open Hand
class OpenHandTechnique(Feature):
    """Starting when you choose this tradition at 3rd level, you can
    manipulate your enemy's ki when you harness your own. Whenever you
    hit a creature with one of the attacks granted by your *Flurry of
    Blows*, you can impose one of the following effects on that
    target:

    - It must succeed on a Dexterity saving throw or be knocked prone.
    - It must make a Strength saving throw. If it fails, you can push
      it up to 15 feet away from you.
    - It can't take reactions until the end of your next turn

    """

    name = "Open Hand Technique"
    source = "Monk (Way of the Open Hand)"


class WholenessOfBody(Feature):
    """At 6th level, you gain the ability to heal yourself. As an action,
    you can regain hit points equal to three times your monk
    level. You must finish a long rest before you can use this feature
    again

    """

    name = "Wholeness of Body"
    source = "Monk (Way of the Open Hand)"


class Tranquility(Feature):
    """Beginning at 11th level, you can enter a special meditation that
    surrounds you with an aura of peace. At the end of a long rest,
    you gain the effect of a sanctuary spell that lasts until the
    start of your next long rest (the spell can end early as
    normal). The saving throw DC for the spell equals 8 + your Wisdom
    modifier + your proficiency bonus

    """

    name = "Tranquility"
    source = "Monk (Way of the Open Hand)"


class QuiveringPalm(Feature):
    """At 17th level, you gain the ability to set up lethal vibrations in
    someone's body. When you hit a creature with an unarmed strike,
    you can spend 3 ki points to start these imperceptible vibrations,
    which last for a number of days equal to your monk level. The
    vibrations are harmless unless you use your action to end them. To
    do so, you and the target must be on the same plane of
    existence. When you use this action, the creature must make a
    Constitution saving throw. If it fails, it is reduced to 0 hit
    points. If it succeeds, it takes 10d10 necrotic damage. You can
    have only one creature under the effect of this feature at a
    time. You can choose to end the vibrations harmlessly without
    using an action.

    """

    name = "Quivering Palm"
    source = "Monk (Way of the Open Hand)"


# Way of Shadow
class ShadowArts(Feature):
    """Starting when you choose this tradition at 3rd level, you can use
    your ki to duplicate the effects of certain spells. As an action,
    you can spend 2 ki points to cast darkness, darkvision, pass
    without trace, or silence, without providing material
    components. Additionally, you gain the minor illusion cantrip if
    you don't already know it.

    """

    name = "Shadow Arts"
    source = "Monk (Way of Shadow)"


class ShadowStep(Feature):
    """At 6th level, you gain the ability to step from one shadow into
    another. When you are in dim light or darkness, as a bonus action
    you can teleport up to 60 feet to an unoccupied space you can see
    that is also in dim light or darkness. You then have advantage on
    the first melee attack you make before the end of the turn.

    """

    name = "Shadow Step"
    source = "Monk (Way of Shadow)"


class CloakOfShadows(Feature):
    """By 11th level, you have learned to become one with the
    shadows. When you are in an area of dim light or darkness, you can
    use your action to become invisible. You remain invisible until
    you make an attack, cast a spell, or are in an area of bright
    light.

    """

    name = "Cloak of Shadows"
    source = "Monk (Way of Shadow)"


class Opportunist(Feature):
    """At 17th level, you can exploit a creature's momentary distraction
    when it is hit by an attack. Whenever a creature within 5 feet of
    you is hit by an attack made by a creature other than you, you can
    use your reaction to make a melee attack against that creature.

    """

    name = "Opportunist"
    source = "Monk (Way of Shadow)"


# Way of the Four Elements
class DiscipleOfTheElements(Feature):
    """When you choose this tradition at 3rd level, you learn magical
    disciplines that harness the power of the four elements. A
    discipline requires you to spend ki points each time you use
    it. You know the Elemental Attunement discipline and one other
    elemental discipline of your choice, which are detailed in the
    "Elemental Disciplines" section below.

    You learn one additional elemental discipline of your choice at
    6th, 11th, and 17th level. Whenever you learn a new elemental
    discipline, you can also replace one elemental discipline that you
    already know with a different discipline.

    Add your chosen disciplines under "features" in your .py file

    **Casting Elemental Spells:** Some elemental disciplines allow you
    to cast spells. See chapter 10 for the general rules of
    spellcasting. To cast one o f these spells, you use its casting
    time and other rules, but you don't need to provide material
    components for it. Once you reach 5th level in this class, you can
    spend additional ki points to increase the level of an elemental
    discipline spell that you cast, provided that the spell has an
    enhanced effect at a higher level, as burning hands does. The
    spell's level increases by 1 for each additional ki point you
    spend. For example, if you are a 5th-level monk and use Sweeping
    Cinder Strike to cast burning hands, you can spend 3 ki points to
    cast it as a 2nd-level spell (the discipline's base cost of 2 ki
    points plus 1).

    The maximum number of ki points you can spend to cast a spell in
    this way (including its base ki point cost and any additional ki
    points you spend to increase its level) is determined by your monk
    level, as shown in the Spells and Ki Points table.

    Monk Levels 5-8 : 3 Ki points Max

    Monk Levels 9-12 : 4 Ki points Max

    Monk Levels 13-16 : 5 Ki points Max

    Monk Levels 17-20 : 6 Ki points Max

    """

    name = "Disciple of the Elements"
    source = "Monk (Way of the Four Elements)"


class ElementalAttunement(Feature):
    """You can use your action to briefly control elemental forces nearby,
    causing one of the following effects of your choice:

    - Create a harmless, instantaneous sensory effect related to air,
      earth, fire, or water, such as a shower of sparks, a puff of
      wind, a spray o f light mist, or a gentle rumbling of stone.
    - Instantaneously light or snuff out a candle, a torch, or a small
      campfire.
    - Chill or warm up to 1 pound of nonliving material for up to 1
      hour.
    - Cause earth, fire, water, or mist that can fit within a 1-foot
      cube to shape itself into a crude form you desig nate for 1
      minute.

    """

    name = "Elemental Attunement"
    source = "Monk (Way of the Four Elements)"


class BreathOfWinter(Feature):
    """You can spend 6 ki points to cast cone of cold.

    **Prerequisite:** 17th Level

    """

    name = "Breath of Winter"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.ConeOfCold,)


class ClenchOfTheNorthWind(Feature):
    """You can spend 3 ki points to cast hold person.

    **Prerequisite:** 6th Level

    """

    name = "Clench of the North Wind"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.HoldPerson,)


class EternalMountainDefense(Feature):
    """You can spend 5 ki points to cast stoneskin, targeting yourself.

    **Prerequisite:** 11th Level

    """

    name = "Eternal Mountain Defense"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.Stoneskin,)


class FangsOfTheFireSnake(Feature):
    """When you use the Attack action on your turn, you can spend 1 ki
    point to cause tendrils of flame to stretch out from your fists
    and feet. Your reach with your unarmed strikes increases by 10
    feet for that action, as well as the rest o f the turn. A hit with
    such an attack deals fire damage instead of bludgeoning damage,
    and if you spend 1 ki point when the attack hits, it also deals an
    extra 1d10 fire damage

    """

    name = "Fangs of the Fire Snake"
    source = "Monk (Way of the Four Elements)"


class FistOfFourThunders(Feature):
    """You can spend 2 ki points to cast thunderwave."""

    name = "Fist of Four Thunders"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.Thunderwave,)


class FistOfUnbrokenAir(Feature):
    """You can create a blast of compressed air that strikes like a mighty
    fist. As an action, you can spend 2 ki points and choose a
    creature within 30 feet of you. That creature must make a Strength
    saving throw. On a failed save, the creature takes 3d10
    bludgeoning damage, plus an extra 1d10 bludgeoning damage for each
    additional ki point you spend, and you can push the creature up to
    20 feet away from you and knock it prone. On a successful save,
    the creature takes half as much damage, and you don't push it or
    knock it prone.

    """

    name = "Fist of Unbroken Air"
    source = "Monk (Way of the Four Elements)"


class FlamesOfThePhoenix(Feature):
    """You can spend 4 ki points to cast fireball.

    **Prerequisite:** 11th Level

    """

    name = "Flames of the Phoenix"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.Fireball,)


class GongOfTheSummit(Feature):
    """You can spend 3 ki points to cast shatter.

    **Prerequisite:** 6th Level

    """

    name = "Gong of the Summit"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.Shatter,)


class MistStance(Feature):
    """You can spend 4 ki points to cast gaseous form, targeting yourself.

    **Prerequisite:** 11th Level

    """

    name = "Mist Stance"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.GaseousForm,)


class RideTheWind(Feature):
    """You can spend 4 ki points to cast fly, targeting yourself

    **Prerequisite:** 11th Level

    """

    name = "Ride the Wind"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.Fly,)


class RiverOfHungryFlame(Feature):
    """You can spend 5 ki points to cast wall of fire.

    **Prerequisite:** 17th Level

    """

    name = "River of Hungry Flame"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.WallOfFire,)


class RushOfTheGaleSpirits(Feature):
    """You can spend 2 ki points to cast gust of wind."""

    name = "Rush of the Gale Spirits"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.GustOfWind,)


class ShapeTheFlowingRiver(Feature):
    """As an action, you can spend 1 ki point to choose an area of ice or
    water no larger than 30 feet on a side within 120 feet o f
    you. You can change water to ice within the area and vice versa,
    and you can reshape ice in the area in any manner you choose. You
    can raise or lower the ice's elevation, create or fill in a
    trench, erect or flatten a wall, or form a pillar. The extent of
    any such changes can't exceed half the area's largest
    dimension. For example, if you affect a 30-foot square, you can
    create a pillar up to 15 feet high, raise or lower the square's
    elevation by up to 15 feet, dig a trench up to 15 feet deep, and
    so on. You can't shape the ice to trap or injure a creature in the
    area.

    """

    name = "Shape the Flowing River"
    source = "Monk (Way of the Four Elements)"


class SweepingCinderStrike(Feature):
    """You can spend 2 ki points to cast burning hands."""

    name = "Sweeping Cinder Strike"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.BurningHands,)


class WaterWhip(Feature):
    """You can spend 2 ki points as a bonus action to create a whip of
    water that shoves and pulls a creature to unbalance it. A creature
    that you can see that is within 30 feet of you must make a
    Dexterity saving throw. On a failed save, the creature takes 3d10
    bludgeoning damage, plus an extra 1d10 bludgeoning damage for each
    additional ki point you spend, and you can either knock it prone
    or pull it up to 25 feet closer to you. On a successful save, the
    creature takes half as much damage, and you don't pull it or knock
    it prone

    """

    name = "Water Whip"
    source = "Monk (Way of the Four Elements)"


class WaveOfRollingEarth(Feature):
    """You can spend 6 ki points to cast wall of stone

    **Prerequisite:** 17th Level

    """

    name = "Wave of Rolling Earth"
    source = "Monk (Way of the Four Elements)"
    spells_known = (spells.WallOfStone,)


# Way of the Long Death
class TouchOfDeath(Feature):
    """Starting when you choose this tradition at 3rd level, your study of death
    allows you to extract vitality from an- other creature as it nears its
    demise. When you reduce a creature within 5 feet of you to 0 hit points,
    you gain temporary hit points equal to your Wisdom modifier + your monk
    level (minimum of 1 temporary hit point)

    """

    name = "Touch of Death"
    source = "Monk (Way of the Sun Soul)"


class HourOfReaping(Feature):
    """At 6th level, you gain the ability to unsettle or terrify those around you
    as an action, for your soul has been touched by the shadow of death. When
    you take this ac- tion , each creature within 30 feet of you that can see
    you must succeed on a Wisdom saving throw or be fright- ened of you until
    the end of your next turn

    """

    name = "Hour of Reaping"
    source = "Monk (Way of the Sun Soul)"


class MasteryOfDeath(Feature):
    """Beginning at 11th level, you use your familiarity with death to escape its
    grasp. When you are reduced to 0 hit points, you can expend 1 ki point (no
    action required) to have 1 hit point instead

    """

    name = "Mastery of Death"
    source = "Monk (Way of the Sun Soul)"


class TouchOfTheLongDeath(Feature):
    """Starting at 17th level, your touch can channel the energy of death into a
    creature. As an action, you touch one creature within 5 feet of you, and
    you expend 1 to 10 ki points. The target must make a Constitution saving
    throw, and it takes 2d10 necrotic damage per ki point spent on a failed
    save, or half as much damage on a suc- cessful one

    """

    name = "Touch of the Long Death"
    source = "Monk (Way of the Sun Soul)"


# Way of the Sun Soul
class RadiantSunBolt(Feature):
    """Starting when you choose this tradition at 3rd level, you can hurl searing
    bolts of magical radiance. You gain a ranged spell attack that you can use
    with the Attack action. The attack has a range of 30 feet. You are
    proficient with it, and you add your Dexterity modi- fier to its attack and
    damage rolls. Its damage is radiant, and its damage die is a d4.

    This die changes as you gain monk levels, as shown in the Martial Arts
    column of the Monk table. When you use the Attack action on your turn to
    use this special attack, you can spend 1 ki point to make two additional
    attacks with it as a bonus action.

    """

    name = "Radiant Sun Bolt"
    source = "Monk (Way of the Sun Soul)"

    def __init__(self, owner=None):
        super().__init__(owner=owner)
        self.owner.wield_weapon("sun bolt")


class SearingArcStrike(Feature):
    """At 6th level, you gain the ability to channel your ki into searing waves of
    energy. Immediately after you take the Attack action on your turn, you can
    spend 2 ki points to cast the 1st-level spell burning hands as a bonus
    action. You can spend additional ki points to cast burning hands as a
    higher level spell. Each additional ki point you spend increases the
    spell's level by 1. The maximum number of ki points (2 plus any additional
    points) that you can spend on the spell equals half your monk level (round
    down)

    """

    name = "Searing Arc Strike"
    source = "Monk (Way of the Sun Soul)"
    spells_known = (spells.BurningHands,)


class SearingSunburst(Feature):
    """At 11th level, you gain the ability to create an orb of light that erupts
    into a devastating explosion. As an action, you create an orb and hurl it
    at a point you choose within 150 feet, where it erupts into a sphere of
    radiant light for a brief but deadly instant. Each creature in that
    20-foot-radius sphere must succeed on a Constitution saving throw or take
    2d6 radiant damage. A creature doesn't need to make the save if the
    creature is behind total cover that is opaque. You can increase the
    sphere's damage by spending ki points. Each point you spend, up to a
    maximum of 3, increases the damage by 2d6.

    """

    name = "Searing Sunburst"
    source = "Monk (Way of the Sun Soul)"


class SunShield(Feature):
    """At 17th level, you become wreathed in a luminous aura. You shed bright
    light in a 30-foot radius and dim light for an additional 30 feet. You can
    extinguish or restore the light as a bonus action. If a creature hits you
    with a melee attack while this light shines, you can use you r reaction to
    deal radiant damage to the creature. The radiant damage equals 5 + your
    Wisdom modifier

    """

    name = "Sun Shield"
    source = "Monk (Way of the Sun Soul)"


# Way of the Drunken Master
class DrunkenTechnique(Feature):
    """At 3rd level, you learn how to twist and turn quickly as part of your
    Flurry of Blows. Whenever you use Flurry of Blows, you gain the benefit of
    the Disengage action, and your walking speed increases by 10 feet until the
    end of the current turn

    """

    name = "Drunken Technique"
    source = "Monk (Way of the Drunken Master)"


class TipsySway(Feature):
    """Starting at 6th level, you can move in sudden, swaying ways. You gain the
    following benefits.

    **Leap to Your Feet:** When you're prone, you can stand up
    by spending 5 feet of movement, rather than half your speed.

    **Redirect Attack:** When a creature misses you with a melee attack roll,
    you can spend 1 ki point as a re- action to cause that attack to hit one
    creature of your choice, other than the attacker, that you can see within 5
    feet of you.

    """

    name = "Tipsy Sway"
    source = "Monk (Way of the Drunken Master)"


class DrunkardsLuck(Feature):
    """Starting at llth level, you always seem to get a lucky bounce at the right
    moment. When you make an ability check, an attack roll, or a saving throw
    and have disad- vantage on the roll, you can spend 2 ki points to cancel
    the disadvantage for that roll

    """

    name = "Drunkard's Luck"
    source = "Monk (Way of the Drunken Master)"


class IntoxicatedFrenzy(Feature):
    """At 17th level, you gain the ability to make an overwhelm- ing number of
    attacks against a group of enemies. When you use your Flurry of Blows, you
    can make up to three additional attacks with it (up to a total of five
    Flurry of Blows attacks), provided that each Flurry of Blows at- tack
    targets a different creature this turn

    """

    name = "Intoxicated Frenzy"
    source = "Monk (Way of the Drunken Master)"


# Way of the Kensei
class PathOfTheKensei(Feature):
    """When you choose this tradition at 3rd level, your spe- cial martial arts
    training leads you to master the use of certain weapons. This path also
    includes instruction in the deft strokes of calligraphy or painting. You
    gain the following benefits.

    **Kensei Weapons:** Choose two types of weapons to be your kensei weapons:
    one melee weapon and one ranged weapon. Each of these weapons can be any
    sim- ple or martial weapon that lacks the heavy and special properties. The
    longbow is also a valid choice. You gain proficiency with these weapons if
    you don't already have it. Weapons of the chosen types are monk weapons for
    you. Many of this tradition's features work only with your kensei
    weapons. When you reach 6th, 11th, and 17th level in this class. you can
    choose another type of weapon-either melee or ranged-to be a kensei weapon
    for you. following the criteria above.

    **Agile Parry:** If you make an unarmed strike as part of the Attack action
    on your turn and are holding a kensei weapon, you can use it to defend
    yourself if it is a melee weapon. You gain a +2 bonus to AC until the start
    of your next turn, while the weapon is in your hand and you aren't
    incapacitated.

    **Kensei's Shot:** You can use a bonus action on your turn to make your
    ranged attacks with a kensei weapon more deadly. When you do so, any target
    you hit with a ranged attack using a kensei weapon takes an extra 1d4
    damage of the weapons type. You retain this benefit un- til the end of the
    current turn.

    **Way ofthe Brush:** You gain proficiency with your choice of
    calligrapher's supplies or painter's supplies

    """

    name = "Path of the Kensei"
    source = "Monk (Way of the Kensei)"


class OneWithTheBlade(Feature):
    """At 6th level, you extend your ki into your kensei weap- ons, granting you
    the following benefits.

    **Magic Kensei Weapons:** Your attacks with your kensei weapons count as
    magical for the purpose of over- coming resistance and immunity to
    nonmagical attacks and damage

    **Deft Strike:** When you hit a target with a kensei weapon, you can spend
    1 ki point to cause the weapon to deal extra damage to the target equal to
    your Martial Arts die. You can use this feature only once on each of
    your turns.

    """

    name = "One with the Blade"
    source = "Monk (Way of the Kensei)"


class SharpenTheBlade(Feature):
    """At 11th level, you gain the ability to augment your weap- ons further with
    your ki. As a bonus action, you can expend up to 3 ki points to grant one
    kensei weapon you touch a bonus to attack and damage rolls when you attack
    with it. The bonus equals the number of ki points you spent. This bonus
    lasts for 1 minute or until you use this feature again. This feature has no
    effect on a magic weapon that already has a bonus to attack and damage
    rolls

    """

    name = "Sharpen the Blade"
    source = "Monk (Way of the Kensei)"


class UnerringAccuracy(Feature):
    """At 17th level, your mastery of weapons grants you ex- traordinary
    accuracy. Ifyou miss with an attack roll using a monk weapon on your turn,
    you can reroll it. You can use this feature only once on each of your
    turns.

    """

    name = "Unerring Accuracy"
    source = "Monk (Way of the Kensei)"

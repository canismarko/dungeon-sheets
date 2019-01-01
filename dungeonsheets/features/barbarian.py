from .features import Feature, FeatureSelector
from .. import (weapons, armor)


# PHB
class Rage(Feature):
    """In battle, you fight with primal ferocity. On your turn, you can enter a
    rage as a bonus action. While raging, you gain the following benefits if
    you aren’t wearing heavy armor:

    --You have advantage on Strength checks and
    Strength saving throws.

    --When you make a melee weapon attack using
    Strength, you gain a bonus to the damage roll that increases as you gain
    levels as a barbarian, as shown in the Rage Damage column of the Barbarian
    table.

    --You have resistance to bludgeoning, piercing, and slashing
    damage.

    If you are able to cast spells, you can’t cast them or concentrate on them
    while raging. Your rage lasts for 1 minute. It ends early if you are
    knocked unconscious or if your turn ends and you haven’t attacked a hostile
    creature since your last turn or taken damage since then. You can also end
    your rage on your turn as a bonus action. Once you have raged the number of
    times shown for your barbarian level in the Rages column of the Barbarian
    table, you must finish a long rest before you can rage again

    """
    _name = "Rage"
    source = "Barbarian"

    @property
    def name(self):
        level = self.owner.Barbarian.level
        num = 2
        if level >= 3:
            num = 3
        if level >= 6:
            num = 4
        if level >= 12:
            num = 5
        if level >= 17:
            num = 6
        if level >= 20:
            num = 100
        damage = '+2'
        if level >= 9:
            damage = "+3"
        if level >= 16:
            damage = "+4"
        return self._name + " ({:s}, {:d}x/LR)".format(damage, num)


class UnarmoredDefenseBarbarian(Feature):
    """While you are not wearing any armor, your Armor Class equals 10 + your
    Dexterity modifier + your Constitution modifier. You can use a shield and
    still gain this benefit.

    This bonus is computed in the AC given on the Character Sheet above.

    """
    name = "Unarmored Defense"
    source = 'Barbarian'


class RecklessAttack(Feature):
    """Starting at 2nd level, you can throw aside all concern for defense to
    attack with fierce desperation. When you make your first attack on your
    turn, you can decide to attack recklessly. Doing so gives you advantage on
    melee weapon attack rolls using Strength during this turn, but attack rolls
    against you have advantage until your next turn

    """
    name = "Reckless Attack"
    source = "Barbarian"


class DangerSense(Feature):
    """At 2nd level, you gain an uncanny sense of when things nearby aren’t as
    they should be, giving you an edge when you dodge away from danger. You
    have advantage on Dexterity saving throws against effects that you can see,
    such as traps and spells. To gain this benefit, you can’t be blinded,
    deafened, or incapacitated.

    """
    name = "Danger Sense"
    source = "Barbarian"


class ExtraAttackBarbarian(Feature):
    """Beginning at 5th level, you can attack twice, instead of once, whenever you
    take the Attack action on your turn.

    """
    name = "Extra Attack (2x)"
    source = "Barbarian"


class FastMovement(Feature):
    """Starting at 5th level, your speed increases by 10 feet while you aren’t
    wearing heavy armor.

    """
    name = "Fast Movement"
    source = "Barbarian"


class FeralInstinct(Feature):
    """By 7th level, your instincts are so honed that you have advantage on
    initiative rolls. Additionally, if you are surprised at the beginning of
    combat and aren’t incapacitated, you can act normally on your first turn,
    but only if you enter your rage before doing anything else on that turn.

    """
    name = "Feral Instinct"
    source = "Barbarian"


class BrutalCritical(Feature):
    """Beginning at 9th level, you can roll one additional weapon damage die when
    determining the extra damage for a critical hit with a melee attack. This
    increases to two additional dice at 13th level and three additional dice at
    17th level.

    """
    name = "Brutal Critical"
    source = "Barbarian"


class RelentlessRage(Feature):
    """Starting at 11th level, your rage can keep you fighting despite grievous
    wounds. If you drop to 0 hit points while you’re raging and don’t die
    outright, you can make a DC 10 Constitution saving throw. If you succeed,
    you drop to 1 hit point instead. Each time you use this feature after the
    first, the DC increases by 5. When you finish a short or long rest, the DC
    resets to 10.

    """
    name = "Relentless Rage"
    source = "Barbarian"


class PersistentRage(Feature):
    """Beginning at 15th level, your rage is so fierce that it ends early only if
    you fall unconscious or if you choose to end it.

    """
    name = "Persistent Rage"
    source = "Barbarian"

    
class IndomitableMight(Feature):
    """Beginning at 18th level, if your total for a Strength check is less than
    your Strength score, you can use that score in place of the total.

    """
    name = "Indomitable Might"
    source = "Barbarian"

    
class PrimalChampion(Feature):
    """At 20th level, you embody the power of the wilds. Your Strength and
    Constitution scores increase by 4. Your maximum for those scores is now 24.

    """
    name = "Primal Champion"
    source = "Barbarian"


# Berserker
class Frenzy(Feature):
    """Starting when you choose this path at 3rd level, you can go into a frenzy
    when you rage. If you do so, for the duration of your rage you can make a
    single melee weapon attack as a bonus action on each of your turns after
    this one. When your rage ends, you suffer one level o f exhaustion (as
    described in appendix A)

    """
    name = "Frenzy"
    source = "Barbarian (Berserker)"


class MindlessRage(Feature):
    """Beginning at 6th level, you can’t be charmed or frightened while raging. If
    you are charmed or frightened when you enter your rage, the effect is
    suspended for the duration of the rage.

    """
    name = "Mindless Rage"
    source = "Barbarian (Berserker)"


class IntimidatingPresence(Feature):
    """Beginning at 10th level, you can use your action to frighten someone with
    your menacing presence. When you do so, choose one creature that you can
    see within 30 feet of you. If the creature can see or hear you, it must
    succeed on a Wisdom saving throw (DC equal to 8 + your proficiency bonus +
    your Charisma modifier) or be frightened of you until the end of your next
    turn. On subsequent turns, you can use your action to extend the duration
    of this effect on the frightened creature until the end of your next
    turn. This effect ends if the creature ends its turn out of line of sight
    or more than 60 feet away from you. If the creature succeeds on its saving
    throw, you can't use this feature on that creature again for 24 hours.

    """
    name = "Intimidating Presence"
    source = "Barbarian (Berserker)"


class Retaliation(Feature):
    """Starting at 14th level, when you take damage from a creature that is within
    5 feet of you. you can use your reaction to make a melee weapon attack
    against that creature.

    """
    name = "Retaliation"
    source = "Barbarian (Berserker)"


# Totem Warrior
class SpiritSeeker(Feature):
    """Yours is a path that seeks attunement with the natural world, giving you a
    kinship with beasts. At 3rd level when you adopt this path, you gain the
    ability to cast the beast sense and speak with animals spells, but only as
    rituals, as described in chapter 10 of PHB.

    """
    name = "Spirit Seeker"
    source = "Barbarian (Totem Warrior)"

    
class BearSpirit(Feature):
    """While raging, you have resistance to all damage except psychic damage. The
    spirit of the bear makes you tough enough to stand up to any punishment.

    """
    name = "Totem Spirit (Bear)"
    source = "Barbarian (Totem Warrior)"


class EagleSpirit(Feature):
    """While you're raging and aren’t wearing heavy armor, other creatures have
    disadvantage on opportunity attack rolls against you, and you can use the
    Dash action as a bonus action on your turn. The spirit of the eagle makes
    you into a predator who can weave through the fray with ease.

    """
    name = "Totem Spirit (Eagle)"
    source = "Barbarian (Totem Warrior)"


class WolfSpirit(Feature):
    """While you're raging, your friends have advantage on melee attack rolls
    against any creature within 5 feet of you that is hostile to you. The
    spirit of the wolf makes you a leader of hunters

    """
    name = "Totem Spirit (Wolf)"
    source = "Barbarian (Totem Warrior)"


class ElkSpirit(Feature):
    """While you're raging and aren't wearing heavy armor, your walking speed
    increases by 15 feet. The spirit of the elk makes you extraordinarily swift

    """
    name = "Totem Spirit (Elk)"
    source = "Barbarian (Totem Warrior)"


class TigerSpirit(Feature):
    """While raging, you can add 10 feet to your long jump distance and 3 feet to
    your high jump distance. The spirit of the tiger empowers your leaps

    """
    name = "Totem Spirit (Tiger)"
    source = "Barbarian (Totem Warrior)"


class TotemSpirit(FeatureSelector):
    """
    Select a Totem Spirit from one of the following under feature_choices in
    your .py file:

    bear spirit

    eagle spirit

    wolf spirit

    elk spirit

    tiger spirit

    """
    options = {'bear spirit': BearSpirit,
               'eagle spirit': EagleSpirit,
               'wolf spirit': WolfSpirit,
               'elk spirit': ElkSpirit,
               'tiger spirit': TigerSpirit}
    name = "Totem Spirit (Select One)"
    source = "Barbarian (Totem Warrior)"


class BearAspect(FeatureSelector):
    """You gain the might of a bear. Your carrying capacity (including maximum
    load and maximum lift) is doubled, and you have advantage on Strength
    checks made to push, pull, lift, or break objects.

    """
    name = "Aspect of the Beast (Bear)"
    source = "Barbarian (Totem Warrior)"


class EagleAspect(FeatureSelector):
    """You gain the eyesight of an eagle. You can see up to 1 mile away with no
    difficulty, able to discern even fine details as though looking at
    something no more than 100 feet away from you. Additionally, dim light
    doesn't impose disadvantage on your Wisdom (Perception) checks.

    """
    name = "Aspect of the Beast (Eagle)"
    source = "Barbarian (Totem Warrior)"


class WolfAspect(FeatureSelector):
    """You gain the hunting sensibilities of a wolf. You can track other creatures
    while traveling at a fast pace, and you can move stealthily while traveling
    at a normal pace (see chapter 8 for rules on travel pace).

    """
    name = "Aspect of the Beast (Wolf)"
    source = "Barbarian (Totem Warrior)"


class ElkAspect(FeatureSelector):
    """Whether mounted or on foot , your travel pace is doubled, as is the travel
    pace of up to ten companions while they're within 60 feet of you and you're
    not incapacitated (see chapter 8 in the Player's Handbook for more
    information about travel pace). The elk spirit helps you roam far and fast

    """
    name = "Aspect of the Beast (Elk)"
    source = "Barbarian (Totem Warrior)"


class TigerAspect(FeatureSelector):
    """You gain proficiency in two skills from the following list: Athletics,
    Acrobatics, Stealth, and Survival. The cat spirit hones your survival
    instincts

    """
    name = "Aspect of the Beast (Tiger)"
    source = "Barbarian (Totem Warrior)"


class BeastAspect(FeatureSelector):
    """Select an Aspect of the Beast from one of the following under
    feature_choices in your .py file:

    bear aspect

    eagle aspect

    wolf aspect

    elk aspect

    tiger aspect

    """
    options = {'bear aspect': BearAspect,
               'eagle aspect': EagleAspect,
               'wolf aspect': WolfAspect,
               'elk aspect': ElkAspect,
               'tiger aspect': TigerAspect}
    name = "Aspect of the Beast (Select One)"
    source = "Barbarian (Totem Warrior)"


class SpiritWalker(Feature):
    """At 10th level, you can cast the commune with nature spell, but only as a
    ritual. When you do so, a spiritual version of one of the animals you chose
    for Totem Spirit or Aspect of the Beast appears to you to convey the
    information you seek.

    """
    name = "Spirit Walker"
    source = "Barbarian (Totem Warrior)"


class BearAttunement(Feature):
    """While you’re raging, any creature within 5 feet o f you that’s hostile to
    you has disadvantage on attack rolls against targets other than you or
    another character with this feature. An enemy is immune to this effect if
    it can’t see or hear you or if it can’t be frightened.
    
    """
    name = "Totemic Attunement (Bear)"
    source = "Barbarian (Totem Warrior)"


class EagleAttunement(Feature):
    """While raging, you have a flying speed equal to your current walking
    speed. This benefit works only in short bursts; you fall if you end your
    turn in the air and nothing else is holding you aloft.

    """
    name = "Totemic Attunement (Eagle)"
    source = "Barbarian (Totem Warrior)"


class WolfAttunement(Feature):
    """Wolf. While you’re raging, you can use a bonus action on your turn to knock
    a Large or smaller creature prone when you hit it with melee weapon attack.

    """
    name = "Totemic Attunement (Wolf)"
    source = "Barbarian (Totem Warrior)"


class ElkAttunement(Feature):
    """While raging, you can use a bonus action during your move to pass through
    the space of a Large or smaller creature. That creature must succeed on a
    Strength saving throw (DC 8 + your Strength bonus + your proficiency
    bonus) or be knocked prone and take bludgeoning damage equal to 1d12 + your
    Strength modifier
    
    """
    name = "Totemic Attunement (Elk)"
    source = "Barbarian (Totem Warrior)"


class TigerAttunement(Feature):
    """While you're raging, if you move at least 20 feet in a straight line toward
    a Large or smaller target right before making a melee weapon attack against
    it, you can use a bonus action to make an additional melee weapon attack
    against it

    """
    name = "Totemic Attunement (Tiger)"
    source = "Barbarian (Totem Warrior)"


class TotemicAttunement(FeatureSelector):
    """Select a Totemic Attunement from one of the following under feature_choices
    in your .py file:

    bear attunement

    eagle attunement

    wolf attunement

    elk attunement

    tiger attunement

    """
    options = {'bear attunement': BearAttunement,
               'eagle attunement': EagleAttunement,
               'wolf attunement': WolfAttunement,
               'elk attunement': ElkAttunement,
               'tiger attunement': TigerAttunement}
    name = "Totemic Attunement (Select One)"
    source = "Barbarian (Totem Warrior)"
    

# Battlerager
class BattleragerArmor(Feature):
    """When you choose this path at 3rd level, you gain the ability to use spiked
    armor (see the "Spiked Armor" sidebar in SCAG) as a weapon. While you are
    wearing spiked armor and are raging, you can use a bonus action to make one
    melee weapon attack with your armor spikes against a target within 5 feet
    of you. If the attack hits , the spikes deal ld4 piercing damage. You use
    your Strength modifier for the attack and damage rolls. Additionally, when
    you use the Attack action to grapple a creature, the target takes 3
    piercing damage if your grapple check succeeds.

    """
    name = 'Battlerager Armor'
    source = "Barbarian (Battlerager)"


class RecklessAbandon(Feature):
    """Beginning at 6th level, when you use Reckless Attack while raging, you also
    gain temporary hit points equal to your Constitution modifier (minimum of
    1). They vanish if any of them are left when your rage ends .

    """
    name = "Reckless Abandon"
    source = "Barbarian (Battlerager)"


class BattleragerCharge(Feature):
    """Beginning at 10th level, you can take the Dash action as a bonus action
    while you are raging.

    """
    name = "Battlerager Charge"
    source = "Barbarian (Battlerager)"

    
class SpikedRetribution(Feature):
    """Starting at 14th level, when a creature within 5 feet of you hits you with
    a melee attack, the attacker takes 3 piercing damage if you are raging,
    aren't incapacitated, and are wearing spiked armor.

    """
    name = "Spiked Retribution"
    source = "Barbarian (Battlerager)"


# Ancestral Guardian
class AncestralProtectors(Feature):
    """Starting when you choose this path at 3rd level, spectral warriors appear
    when you enter your rage. While you’re raging, the first creature you hit
    with an attack on your turn becomes the target of the warriors, which
    hinder its attacks. Until the start ofyour next turn, that target has
    disadvantage on any attack roll that isn’t against you, and when the target
    hits a creature other than you with an attack, that creature has resistance
    to the damage dealt by the attack. The effect on the target ends early
    ifyour rage ends

    """
    name = "Ancestral Protectors"
    source = "Barbarian (Ancestral Guardian)"


class SpiritShield(Feature):
    """Beginning at 6th level, the guardian spirits that aid you can provide
    supernatural protection to those you defend. If you are raging and another
    creature you can see within 30 feet of you takes damage, you can use your
    reaction to reduce that damage by 2d6.

    When you reach certain levels in this class. you can reduce the damage by
    more: by 3d6 at 10th level and by 4d6 at 14th level.

    """
    _name = "Spirit Shield"
    source = "Barbarian (Ancestral Guardian)"

    @property
    def name(self):
        level = self.owner.Barbarian.level
        damage = " (2d6)"
        if level >= 10:
            damage = " (3d6)"
        if level >= 14:
            damage = " (4d6)"
        return self._name + damage


class ConsultTheSpirits(Feature):
    """At 10th level, you gain the ability to consult with your ancestral
    spirits. When you do so, you cast the augury or clairvoyance spell, without
    using a spell slot or material components. Rather than creating a spherical
    sensor, this use of clairvoyance invisibly summons one Of your ancestral
    spirits to the chosen location. Wisdom is your spellcasting ability for
    these spells. After you cast either spell in this way, you can’t use this
    feature again until you finish a short or long rest

    """
    name = "Consult the Spirits"
    source = "Barbarian (Ancestral Guardian)"


class VengefulAncestors(Feature):
    """At 14th level, your ancestral spirits grow powerful enough to
    retaliate. When you use your Spirit Shield to reduce the damage of an
    attack, the attacker takes an amount of force damage equal to the damage
    that your Spirit Shield prevents.

    """
    name = "Vengeful Ancestors"
    source = "Barbarian (Ancestral Guardian)"


# Storm Herald
class DesertAura(Feature):
    """Starting at 3rd level, you emanate a stormy, magical aura while you
    rage. The aura extends 10 feet from you in every direction, but not through
    total cover. Your aura has an effect that activates when you enter your
    rage, and you can activate the effect again on each of your turns as a
    bonus action.

    Choose desert, sea, or tundra. Your aura’s effect depends on that chosen
    environment, as detailed below. You can change your environment choice
    whenever you gain a level in this class. If your aura's effects require a
    saving throw, the DC equals 8 + your proficiency bonus + your Constitu-
    tion modifier.

    **Desert**: When this effect is activated, all other creatures in your
    aura take 2 fire damage each. The damage increases when you reach certain
    levels in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at
    15th level, and 6 at 20th level.

    """
    name = "Storm Aura (Desert)"
    source = "Barbarian (Storm Herald)"


class SeaAura(Feature):
    """Starting at 3rd level, you emanate a stormy, magical aura while you
    rage. The aura extends 10 feet from you in every direction, but not through
    total cover. Your aura has an effect that activates when you enter your
    rage, and you can activate the effect again on each of your turns as a
    bonus action.

    Choose desert, sea, or tundra. Your aura’s effect depends on that chosen
    environment, as detailed below. You can change your environment choice
    whenever you gain a level in this class. If your aura's effects require a
    saving throw, the DC equals 8 + your proficiency bonus + your Constitu-
    tion modifier.

    **Sea**: When this effect is activated, you can choose one other creature
    you can see in your aura. The target must make a Dexterity saving
    throw. The target takes 1d6 lightning damage on a failed save, or half as
    much damage on a successful one. The damage increases when you reach
    certain levels in this class, increasing to 2d6 at 10th level, 3d6 at 15th
    level, and 4d6 at 20th level.

    """
    name = "Storm Aura (Sea)"
    source = "Barbarian (Storm Herald)"


class TundraAura(Feature):
    """Starting at 3rd level, you emanate a stormy, magical aura while you
    rage. The aura extends 10 feet from you in every direction, but not through
    total cover. Your aura has an effect that activates when you enter your
    rage, and you can activate the effect again on each of your turns as a
    bonus action.

    Choose desert, sea, or tundra. Your aura’s effect depends on that chosen
    environment, as detailed below. You can change your environment choice
    whenever you gain a level in this class. If your aura's effects require a
    saving throw, the DC equals 8 + your proficiency bonus + your Constitu-
    tion modifier.

    **Tundra**: When this effect is activated, each creature of your choice in
    your aura gains 2 temporary hit points, as icy spirits inure it to
    suffering. The temporary hit points increase when you reach certain levels
    in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at 15th
    level, and 6 at 20th level.

    """
    name = "Storm Aura (Tundra)"
    source = "Barbarian (Storm Herald)"


class StormAura(FeatureSelector):
    """
    Select a Storm Aura from one of the following under feature_choices in
    your .py file:

    desert

    sea

    tundra
    """
    options = {'desert': DesertAura,
               'sea': SeaAura,
               'tundra': TundraAura}
    name = "Storm Aura (Select One)"
    source = "Barbarian (Storm Herald)"


class DesertSoul(Feature):
    """At 6th level, the storm grants you benefits even when your aura isn’t
    active. The benefits are based on the environment you chose for your
    Storm Aura.

    **Desert**: You gain resistance to fire damage, and you don’t suffer the
    effects of extreme heat, as described in the Dungeon Master’s
    Guide. Moreover, as an action, you can touch a flammable object that isn’t
    being worn or carried by anyone else and set it on fire

    """
    name = "Storm Soul (Desert)"
    source = "Barbarian (Storm Herald)"


class SeaSoul(Feature):
    """At 6th level, the storm grants you benefits even when your aura isn’t
    active. The benefits are based on the environment you chose for your
    Storm Aura.

    **Sea**: You gain resistance to lightning damage, and
    you can breathe underwater. You also gain a swimming speed of 30 feet.
    """
    name = "Storm Soul (Sea)"
    source = "Barbarian (Storm Herald)"


class TundraSoul(Feature):
    """At 6th level, the storm grants you benefits even when your aura isn’t
    active. The benefits are based on the environment you chose for your
    Storm Aura.

    **Tundra**: You gain resistance to cold damage, and you don’t suffer the
    effects of extreme cold, as described in the Dungeon Master’s
    Guide. Moreover, as an action, you can touch water and turn a 5-foot cube
    Of it into ice, which melts after 1 minute. This action fails if a creature
    is in the cube
    """
    name = "Storm Soul (Tundra)"
    source = "Barbarian (Storm Herald)"


class StormSoul(FeatureSelector):
    """Select a Storm Soul (same as Soul Aura) from one of the following under
    feature_choices in your .py file:

    desert

    sea

    tundra

    """
    options = {'desert': DesertSoul,
               'sea': SeaSoul,
               'tundra': TundraSoul}
    name = "Storm Soul (Select One)"
    source = "Barbarian (Storm Herald)"


class ShieldingStorm(Feature):
    """At 10th level, you learn to use your mastery of the storm to protect
    others. Each creature of your choice has the damage resistance you gained
    from the Storm Soul fea ture while the creature is in your Storm Aura.

    """
    name = "Shielding Storm"
    source = "Barbarian (Storm Herald)"


class RagingDesert(Feature):
    """At 14th level, the power of the storm you channel grows mightier, lashing
    out at your foes. The effect is based on the environment you chose for your
    Storm Aura

    **Desert**: Immediately after a creature in your aura hits you with an
    attack, you can use your reaction to force that creature to make a
    Dexterity saving throw. On a failed save, the creature takes fire damage
    equal to half your barbarian level.

    """
    name = "Raging Storm (Desert)"
    source = "Barbarian (Storm Herald)"


class RagingSea(Feature):
    """At 14th level, the power of the storm you channel grows mightier, lashing
    out at your foes. The effect is based on the environment you chose for your
    Storm Aura

    **Sea**: When you hit a creature in your aura with an attack, you can use
    your reaction to force that creature to make a Strength saving throw. On a
    failed save, the creature is knocked prone, as if struck by a wave.

    """
    name = "Raging Storm (Sea)"
    source = "Barbarian (Storm Herald)"


class RagingTundra(Feature):
    """At 14th level, the power of the storm you channel grows mightier, lashing
    out at your foes. The effect is based on the environment you chose for your
    Storm Aura

    **Tundra**: Whenever the effect of your Storm Aura is activated, you can
    choose one creature you can see in the aura. That creature must succeed on
    a Strength saving throw, or its speed is reduced to 0 until the start of
    your next turn, as magical frost covers it

    """
    name = "Raging Storm (Tundra)"
    source = "Barbarian (Storm Herald)"


class RagingStorm(FeatureSelector):
    """Select a Raging Storm (same as Soul Aura) from one of the following under
    feature_choices in your .py file:

    desert

    sea

    tundra

    """
    options = {'desert': RagingDesert,
               'sea': RagingSea,
               'tundra': RagingTundra}
    name = "Raging Storm (Select One)"
    source = "Barbarian (Storm Herald)"


# Zealot
class DivineFury(Feature):
    """Starting when you choose this path at 3rd level, you can channel divine
    fury into your weapon strikes. While you’re raging, the first creature you
    hit on each of your turns with a weapon attack takes extra damage equal to
    1d6 + half your barbarian level. The extra damage is necrotic or radiant;
    you choose the type of damage when you gain this feature.

    """
    _name = "Divine Fury"
    source = "Barbarian (Zealot)"

    @property
    def name(self):
        level = self.owner.Barbarian.level
        damage = " (1d6+{:d})".format(level//2)
        return self._name + damage


class WarriorOfTheGods(Feature):
    """At 3rd level, your soul is marked for endless battle. If a spell, such as
    raise dead, has the sole effect of restoring you to life (but not
    undeath), the caster doesn’t need material components to cast the spell
    on you

    """
    name = "Warrior of the Gods"
    source = "Barbarian (Zealot)"


class FanaticalFocus(Feature):
    """Starting at 6th level, the divine power that fuels your rage can protect
    you. If you fail a saving throw while you’re raging, you can reroll it, and
    you must use the new roll. You can use this ability only once per rage.
    """
    name = "Fanatical Focus"
    source = "Barbarian (Zealot)"


class ZealousPresence(Feature):
    """At 10th level, you learn to channel divine power to inspire zealotry in
    others. As a bonus action, you unleash a battle cry infused with divine
    energy. Up to ten other creatures of your choice within 60 feet ofyou that
    can hear you gain advantage on attack rolls and saving throws until the
    start of your next turn. Once you use this feature, you can’t use it again
    until you finish a long rest

    """
    name = "Zealous Presence"
    source = "Barbarian (Zealot)"


class RageBeyondDeath(Feature):
    """Beginning at 14th level, the divine power that fuels your rage allows you
    to shrug off fatal blows. While you’re raging, having 0 hit points doesn’t
    knock you unconscious. You still must make death saving throws, and you
    suffer the normal effects of taking damage while at 0 hit points. However,
    if you would die due to failing death saving throws, you don't die until
    your rage ends, and you die then only if you still have 0 hit points.

    """
    name = "Rage Beyond Death"
    source = "Barbarian (Zealot)"
    

from dungeonsheets import spells
from dungeonsheets.features.features import Feature


# Many Classes
class Darkvision(Feature):
    """Accustomed to life underground, you have superior vision in dark and dim
    conditions. You can see in dim light within 60 feet of you as if it were
    bright light, and in darkness as if it were dim light. You can't discern
    color in darkness, only shades of gray.

    """

    name = "Darkvision (60')"
    source = "Race"


class SuperiorDarkvision(Feature):
    """Accustomed to life underground, you have superior vision in dark and dim
    conditions. You can see in dim light within 120 feet of you as if it were
    bright light, and in darkness as if it were dim light. You can't discern
    color in darkness, only shades of gray.

    """

    name = "Darkvision (120')"
    source = "Race"


class PowerfulBuild(Feature):
    """You count as one size larger when determining your carrying
    capacity and the weight you can push, drag, or lift.

    """

    name = "Powerful Build"
    source = "Race"


class Amphibious(Feature):
    """
    You can breath air and water

    """

    name = "Amphibious"
    source = "Race"


# Dwarves
class DwarvenResilience(Feature):
    """You have advantage on saving throws against poison, and you have resistance
    against poison damage

    """

    name = "Dwarven Resilience"
    source = "Race (Dwarf)"


class Stonecunning(Feature):
    """Whenever you make an Intelligence (History) check related to the origin of
    stonework, you are considered proficient in the History skill and add
    double your proficiency bonus to the check, instead of your normal
    proficiency bonus. Languages.

    """

    name = "Stonecunning"
    source = "Race (Dwarf)"


class DwarvenToughness(Feature):
    """
    Your hit point maximum
    increases by 1, and it increases by 1 every time you gain a level.

    """

    name = "Dwarven Toughness"
    source = "Race (Hill Dwarf)"
    needs_implementation = True


# Elves
class FeyAncestry(Feature):
    """You have advantage on saving throws against being charmed, and magic can't
    put you to sleep.

    """

    name = "Fey Ancestry"
    source = "Race (Elf)"


class Trance(Feature):
    """Elves don't need to sleep. Instead, they meditate deeply, remaining
    semiconscious, for 4 hours a day. (The Common word for such meditation is
    "trance.") While meditating, you can dream after a fashion; such dreams are
    actually mental exercises that have become reflexive through years of
    practice. After resting in this way, you gain the same benefit that a human
    does from 8 hours of sleep.

    """

    name = "Trance"
    source = "Race (Elf)"


class ElfCantrip(Feature):
    """You know one cantrip of your choice from the wizard spell
    list. Intelligence is your spellcasting ability for it.

    """

    name = "Cantrip"
    source = "Race (High-Elf)"
    needs_implementation = True


class MaskOfTheWild(Feature):
    """You can attempt to hide even when you are only lightly obscured by foliage,
    heavy rain, falling snow, mist, and other natural phenomena.

    """

    name = "Mask of the Wild"
    source = "Race (Wood Elf)"


class SunlightSensitivity(Feature):
    """You have disadvantage on attack rolls and on Wisdom (Perception) checks
    that rely on sight when you, the target of your attack, or whatever you are
    trying to perceive is in direct sunlight.

    """

    name = "Sunlight Sensitivity"
    source = "Race (Dark Elf)"


class DrowMagic(Feature):
    """You know the dancing lights cantrip.  When you reach 3rd level, you can
    cast the faerie fire spell once per day. When you reach 5th level, you can
    also cast the darkness spell once per day. Charisma is your spellcasting
    ability for these spells.

    """

    name = "Drow Magic"
    source = "Race (Dark Elf)"
    spells_known = spells_prepared = (spells.DancingLights,)


# Halflings
class Lucky(Feature):
    """When you roll a 1 on an attack roll, ability check, or saving throw, you can
    reroll the die and must use the new roll.

    """

    name = "Lucky"
    source = "Race (Halfling)"


class Brave(Feature):
    """You have advantage on saving throws against being frightened."""

    name = "Brave"
    source = "Race (Halfling)"


class HalflingNimbleness(Feature):
    """
    You can move through the space of any creature that is of a size larger than yours.
    """

    name = "Halfling Nimbleness"
    source = "Race (Halfling)"


class NaturallyStealthy(Feature):
    """You can attempt to hide even when you are obscured only by a creature that
    is at least one size larger than you.

    """

    name = "Naturally Stealthy"
    source = "Race (Lightfoot Halfling)"


class StoutResilience(Feature):
    """You have advantage on saving throws against poison, and you have resistance
    against poison damage.

    """

    name = "Stout Resilience"
    source = "Race (Stout Halfling)"


# Humans

# Dragonborn
class DraconicAncestry(Feature):
    """You have draconic ancestry. Choose one type of dragon from the Draconic
    Ancestry table. Your breath weapon and damage resistance are determined by the
    dragon type.

    ====== =========== ===========================
    Dragon Damage Type Breath Weapon
    ====== =========== ===========================
    Black  Acid        5 by 30 ft. line (DEX save)
    Blue   Lightning   5 by 30 ft. line (DEX save)
    Brass  Fire        5 by 30 ft. line (DEX save)
    Bronze Lightning   5 by 30 ft. line (DEX save)
    Copper Acid        5 by 30 ft. line (DEX save)
    Gold   Fire        15 ft. cone (DEX save)
    Green  Poison      15 ft. cone (CON save)
    Red    Fire        15 ft. cone (DEX save)
    Silver Cold        15 ft. cone (CON save)
    White  White       15 ft. cone (CON save)
    ====== =========== ===========================

    """

    name = "Draconic Ancestry"
    source = "Race (Dragonborn)"


class BreathWeapon(Feature):
    """You can use your action to exhale destructive energy. Your draconic ancestry
    determines the size, shape, and damage type of the exhalation. When you use
    your breath weapon, each creature in the area of the exhalation must make a
    saving throw, the type of which is determined by your draconic
    ancestry. The DC for this saving throw equals 8 + your Constitution
    modifier + your proficiency bonus. A creature takes 2d6 damage on a failed
    save, and half as much damage on a successful one. The damage increases to
    3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use
    your breath weapon, you can't use it again until you complete a short or
    long rest. Damage

    """

    name = "Breath Weapon"
    source = "Race (Dragonborn)"


class DraconicResistance(Feature):
    """You have resistance to the damage type associated with your draconic
    ancestry. Languages.

    """

    name = "Damage Resistance"
    source = "Race (Dragonborn)"


# Gnomes
class GnomeCunning(Feature):
    """You have advantage on all Intelligence, Wisdom, and Charisma saving throws
    against magic.

    """

    name = "Gnome Cunning"
    source = "Race (Gnome)"


class NaturalIllusionist(Feature):
    """You know the minor illusion cantrip. Intelligence is your spellcasting
    ability for it.

    """

    name = "Natural Illusionist"
    source = "Race (Forest Gnome)"


class SpeakWithSmallBeasts(Feature):
    """Through sounds and gestures, you can communicate simple ideas with Small or
    smaller beasts. Forest gnomes love animals and often keep squirrels,
    badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets.


    """

    name = "Speak with Small Beasts"
    source = "Race (Forest Gnome)"


class ArtificersLore(Feature):
    """Whenever you make an Intelligence (History) check related to magic items,
    alchemical objects, or technological devices, you can add twice your
    proficiency bonus, instead of any proficiency bonus you normally
    apply. Tinker.

    """

    name = "Artificer's Lore"
    source = "Race (Rock Gnome)"


class Tinker(Feature):
    """You have proficiency with artisan's tools (tinker's tools). Using those
    tools, you can spend 1 hour and 10 gp worth of materials to construct a
    Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24
    hours (unless you spend 1 hour repairing it to keep the device
    functioning), or when you use your action to dismantle it; at that time,
    you can reclaim the materials used to create it. You can have up to three
    such devices active at a time. When you create a device, choose one of the
    following options:

    *Clockwork Toy*: This toy is a clockwork animal, monster, or person, such as
    a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy
    moves 5 feet across the ground on each of your turns in a random
    direction. It makes noises as appropriate to the creature it represents.

    *Fire Starter*: The device produces a miniature flame, which you can use to
    light a candle, torch, or campfire. Using the device requires your action.

    *Music Box*: When opened, this music box plays a single song at a moderate
    volume. The box stops playing when it reaches the song's end or when

    """

    name = "Tinker"
    source = "Race (Rock Gnome)"


class StoneCamouflage(Feature):
    """
    You have advantage on Dexterity (stealth) checks to hide in rocky terrain.
    """

    name = "Stone Camouflage"
    source = "Race (Deep Gnome)"


# Half-Elves

# Half-Orcs
class RelentlessEndurance(Feature):
    """When you are reduced to 0 hit points but not killed outright, you can drop
    to 1 hit point instead. You can't use this feature again until you finish a
    long rest.

    """

    name = "Relentless Endurance"
    source = "Race (Half-Orc)"


class SavageAttacks(Feature):
    """When you score a critical hit with a melee weapon attack, you can roll one
    of the weapon's damage dice one additional time and add it to the extra
    damage of the critical hit.

    """

    name = "Savage Attacks"
    source = "Race (Half-Orc)"


# Tiefling
class HellishResistance(Feature):
    """You have resistance to fire damage."""

    name = "Hellish Resistance"
    source = "Race (Tiefling)"


class InfernalLegacy(Feature):
    """You know the thaumaturgy cantrip.  Once you reach 3rd level, you can cast
    the hellish rebuke spell once per day as a 2nd-level spell. Once you reach
    5th level, you can also cast the darkness spell once per day. Charisma is
    your spellcasting ability for these spells.

    """

    name = "Infernal Legacy"
    source = "Race (Tiefling)"
    spells_known = spells_prepared = (spells.Thaumaturgy,)


# Aasimar
class CelestialResistance(Feature):
    """
    You have resistance to necrotic damage and radiant damage.

    """

    name = "Celestial Resistance"
    source = "Race (Aasimar)"


class HealingHands(Feature):
    """As an action, you can touch a creature and cause it to regain a number of
    hit points equal to your level. Once you use this trait, you can't use it
    again until you finish a long rest.

    """

    name = "Healing Hands"
    source = "Race (Aasimar)"


class LightBearer(Feature):
    """You know the light cantrip. Charisma is your spellcasting ability for it."""

    name = "Light Bearer"
    source = "Race (Aasimar)"


class RadiantSoul(Feature):
    """Starting at 3rd level, you can use your action to unleash the divine
    energy within yourself, causing your eyes to glimmer and two luminous,
    incorporeal wings to sprout from your back.

    Your transformation lasts for 1 minute or until you end it as a bonus
    action. During it, you have a flying speed of 30 feet, and once on each of
    your turns, you can deal extra radiant damage to one target when you deal
    damage to it with an attack or a spell. The extra radiant damage equals
    your level.

    Once you use this trait, you can't use it again until you finish a long
    rest.

    """

    name = "Radiant Soul"
    source = "Race (Protector Aasimar)"


class RadiantConsumption(Feature):
    """Starting at 3rd level, you can use your action to unleash the divine energy
    within yourself, causing a searing light to radiate from you, pour out of
    your eyes and mouth, and threaten to char you.

    Your transformation lasts for 1 minute or until you end ii as a bonus
    action. During it, you shed bright light in a 10-foot radius and dim light
    for an additional 10 feet,and at the end of each of your turns, you and
    each creature within 10 feet of you take radiant damage equal to half
    your level (rounded up). In addition, once on each of your turns, you can
    deal extra radiant damage to one target when you deal damage to it with an
    attack or a spell. The extra radiant damage equals your level.

    Once you use this trait, you can't use it again until you finish a long
    rest.

    """

    name = "Radiant Consumption"
    source = "Race (Scourge Aasimar)"


class NecroticShroud(Feature):
    """Starting at 3rd level, you can use your action to unleash the divine
    energy within yourself, causing your eyes to turn into pools of darkness and
    two skeletal, ghostly, flightless wings to sprout from your back.
    The instant you transform, other creatures within 10 feet of you that can
    see you must each succeed on a Charisma saving throw (DC 8 + your
    proficiency bonus + your Charisma modifier) or become frightened of you
    until the end of your next turn.

    Your transformation lasts for 1 minute or until you end it as a bonus
    action. During it, once on each of your turns, you can deal extra necrotic
    damage to one target when you deal damage to it with an attack or a spell.
    The extra necrotic damage equals your level.

    Once you use this trait, you can't use it again until you finish a long
    rest.

    """

    name = "Necrotic Shroud"
    source = "Race (Fallen Aasimar)"


# Firbolg
class FirbolgMagic(Feature):
    """You can cast detect magic and disguise self with this trait, using Wisdom
    as your spellcasting ability for them. Once you cast either spell, you
    can't cast it again with this trait until you finish a short or long
    rest. When you use this version of disguise self, you can seem up to 3 feet
    shorter than normal, allowing you to more easily blend in with humans and
    elves.

    """

    name = "Firbolg Magic"
    source = "Race (Firbolg)"


class HiddenStep(Feature):
    """As a bonus action, you can magically turn invisible until the start of your
    next turn or until you attack, make a damage roll, or force someone to make
    a saving throw. Once you use this trait, you can't use it again until you
    finish a short or long rest.

    """

    name = "Hidden Step"
    source = "Race (Firbolg)"


class SpeechOfBeastAndLeaf(Feature):
    """You have the ability to communicate in a limited manner with beasts and
    plants. They can understand the meaning of your words, though you have no
    special ability to understand them in return. You have advantage on all
    Charisma checks you make to influence them.

    """

    name = "Speech of Beast and Leaf"
    source = "Race (Firbolg)"


# Goliath
class StonesEndurance(Feature):
    """You can focus yourself to occasionally shrug off injury. When you take
    damage, you can use your reaction to roll a dl2. Add your Constitution
    modifier to the number rolled, and reduce the damage by that total. After
    you use this trait, you can't use it again until you finish a short or long
    rest.

    """

    name = "Stones Endurance"
    source = "Race (Goliath)"


class MountainBorn(Feature):
    """You're acclimated to high altitude, including elevations above 20,000
    feet. You're also naturally adapted to cold climates, as described in
    chapter 5 of the Dungeon Master's Guide.

    """

    name = "Mountain Born"
    source = "Race (Goliath)"


# Kenku
class ExpertForgery(Feature):
    """You can duplicate other creatures' handwriting and craftwork. You have
    advantage on all checks made to produce forgeries or duplicates of existing
    objects.

    """

    name = "Expert Forgery"
    source = "Race (Kenku)"


class Mimicry(Feature):
    """You can mimic sounds you have heard, including voices. A creature that
    hears the sounds you make can tell they are imitations with a successful
    Wisdom (Insight) check opposed by your Charisma (Deception) check.

    """

    name = "Mimicry"
    source = "Race (Kenku)"


# Lizardfolk
class CunningArtisan(Feature):
    """As part of a short rest, you can harvest bone and hide from a slain
    beast, construct, dragon, monstrosity, or plant creature of size Small or
    larger to create one of the following items: a shield, a club, a javelin,
    or ld4 darts or blowgun needles. To use this trait, you need a blade, such
    as a dagger, or appropriate artisan's tools, such as leatherworker's
    tools.

    """

    name = "Cunning Artisan"
    source = "Race (Lizardfolk)"


class HoldBreath(Feature):
    """
    You can hold your breath for up to 15 minutes at a time.
    """

    name = "Hold Breath"
    source = "Race (Lizardfolk)"


class NaturalArmor(Feature):
    """You have tough, scaly skin. When you aren't wearing armor, your AC is 13 +
    your Dexterity modifier. You can use your natural armor to determine your
    AC if the armor you wear would leave you with a lower AC. A shield's
    benefits apply as normal while you use your natural armor.

    """

    name = "Natural Armor"
    source = "Race (Lizardfolk)"

    def AC_func(self, char, **kwargs):
        """
        Implement the Natural Armor AC option
        """
        ac = 13 + char.dexterity.modifier
        if char.shield is not None:
            ac += char.shield.base_armor_class
        return ac


class HungryJaws(Feature):
    """In battle, you can throw yourself into a vicious feeding frenzy. As a bonus
    action, you can make a special attack with your bite. If the attack hits,
    it deals its normal damage, and you gain temporary hit points (minimum of
    1) equal to your Constitution modifier, and you can't use this trait again
    until you finish a short or long rest.

    """

    name = "Hungry Jaws"
    source = "Race (Lizardfolk)"


# Tabaxi
class FelineAgility(Feature):
    """Your reflexes and agility allow you to meve with a burst of speed. When you
    move on your turn in combat, you can double your speed until the end of the
    turn. Once you use this trait, you can't use it again until you move O feet
    on one of your turns.

    """

    name = "Feline Agility"
    source = "Race (Tabaxi)"


# Triton


class ControlAirAndWater(Feature):
    """A child of the sea, you can call on the magic of elemental air and
    water. You can cast fog cloud with this trait. Starting at 3rd level, you
    can cast gust of wind with it, and starting at 5th level, you can also cast
    wall of water with it (see the spell in the sidebar). Once you cast a spell
    with this trait, you can't do so again until you finish a long
    rest. Charisma is your spellcasting ability for these spells.

    """

    name = "Control Air and Water"
    source = "Race (Triton)"


class EmissaryOfTheSea(Feature):
    """Aquatic beasts have an extraordinary affinity with your people. You can
    communicate simple ideas with beasts that can breathe water. They can
    understand the meaning of your words, though you have no special ability to
    understand them in return.

    """

    name = "Emissary Of The Sea"
    source = "Race (Triton)"


class GuardiansOfTheDepths(Feature):
    """Adapted to even the most extreme ocean depths, you have resistance to cold
    damage, and you ignore any of the drawbacks caused by a deep, underwater
    environment.

    """

    name = "Guardians of the Depths"
    source = "Race (Triton)"


# Aarakocra

# Genasi
class UnendingBreath(Feature):
    """You can hold your breath indefinitely while you're not incapacitated."""

    name = "Unending Breath"
    source = "Race (Air Genasi)"


class MingleWithTheWind(Feature):
    """You can cast the levitate spell once with this trait, requiring no material
    components, and you regain the ability to cast it this way when you finish
    a long rest. Constitution is your spellcasting ability for this spell.

    """

    name = "Mingle with the Wind"
    source = "Race (Air Genasi)"


class EarthWalk(Feature):
    """You can move across difficult terrain made of earth or stone without
    expending extra movement.

    """

    name = "Earth Walk"
    source = "Race (Earth Genasi)"


class MergeWithStone(Feature):
    """You can cast the pass without trace spell once with this trait, requiring
    no material components, and you regain the ability to cast it this way when
    you finish a long rest. Constitution is your spellcasting ability for this
    spell.

    """

    name = "Merge with Stone"
    source = "Race (Earth Genasi)"


class FireResistance(Feature):
    """
    You have resistance to fire damage.
    """

    name = "Fire Resistance"
    source = "Race (Fire Genasi)"


class ReachToTheBlaze(Feature):
    """You know the produce flame cantrip. Once you reach 3rd level, you can cast
    the burning hands spell once with this trait as a 1st-level spell, and you
    regain the ability to cast it this way when you finish a long
    rest. Constitution is your spellcasting ability for these spells.

    """

    name = "Reach to the Blaze"
    source = "Race (Fire Genasi)"


class AcidResistance(Feature):
    """
    You have resistance to acid damage.

    """

    name = "Acid Resistance"
    source = "Race (Water Genasi)"


class CallToTheWave(Feature):
    """You know the shape water cantrip (see chapter 2 EEPC). When you reach 3rd level,
    you can cast the create or destroy water spell as a 2nd-level spell once
    with this trait, and you regain the ability to cast it this way when you
    finish a long rest. Constitution is your spellcasting ability for these
    spells.

    """

    name = "Call to the Wave"
    source = "Race (Water Genasi)"


# RFTLW Races


class DualMind(Feature):
    """
    You have advantage on all Wisdom saving throws.

    """

    name = "Dual Mind"
    source = "Race (Kalashtar)"


class MentalDiscipline(Feature):
    """
    You have resistance to psychic damage.

    """

    name = "Mental Discipline"
    source = "Race (Kalashtar)"


class MindLink(Feature):
    """
    You can speak telepathically to any creature you can see, provided
    the creature is within a number of feet of you equal to 10 times your
    level. You don’t need to share a language with the creature for it to
    understand your telepathic utterances, but the creature must be able
    to understand at least one language.

    When you’re using this trait to speak telepathically to a creature,
    you can use your action to give that creature the ability to speak
    telepathically with you for 1 hour or until you end this effect as
    an action. To use this ability, the creature must be able to see
    you and must be within this trait’s range. You can give this
    ability to only one creature at a time; giving it to a creature
    takes it away from another creature who has it.

    """

    name = "Mind Link"
    source = "Race (Kalashtar)"


class SeveredFromDreams(Feature):
    """
    Kalashtar sleep, but they don't connect to the plane of dreams as
    other creatures do. Instead, their minds draw from the memories of
    the otherworldly spirit while they sleep. As such, you are immune
    to spells and other magical effects that require you to dream,
    like 'dream', but not to spells and other magical effects that put
    you to sleep, like 'sleep'.

    """

    name = "Severed from Dreams"
    source = "Race (Kalashtar)"


# monsterous races
# bugbear
class LongLimbed(Feature):
    """When you make a melee attack on your turn, your reach for it is 5
    feet greater than normal.

    """

    name = "Long-Limbed"
    source = "Race (BugBear)"


class SupriseAttack(Feature):
    """If you surprise a creature and hit it with an attack on your first turn
    in combat, the attack deals an extra 2d6 damage to it. You can use this trait
    only once per combat.

    """

    name = "Suprise Attack"
    source = "Race (BugBear)"


# Goblins
class FuryOfTheSmall(Feature):
    """
    When you damage a creature with an attack or a spell and the creature's
    size is larger than yours, you can cause the attack or spell to deal extra
    damage to the creature. The extra damage equals your level. Once you use
    this trait, you can't use it again until you finish a short or long rest.
    """

    name = "Fury of the Small"
    source = "Race (Goblin)"


class NimbleEscape(Feature):
    """
    You can take the Disengage or Hide action as a bonus action on each of your
    turns.
    """

    name = "Nimble Escape"
    source = "Race (Goblin)"


# HobGoblin
class SavingFace(Feature):
    """Hobgoblins are careful not to show weakness in front of their allies, for fear
    of losing status. If you miss with an attack roll or fail an ability check or a
    saving throw, you can gain a bonus to the roll equal to the number of allies you
    can see within 30 feet of you (maximum bonus of +5). Once you use this trait, you
    can't use it again until you finish a short or long rest.

    """

    name = "Saving Face"
    source = "Race (HobGoblin)"


class MartialTraining(Feature):  # you have to add the weapons of choice to your sheet
    """You are proficient with two martial weapons of your choice and with
    light armor.

    """

    name = "Martial Training"
    source = "Race (HobGoblin)"


# kobold
class GrovelCowerAndBeg(Feature):
    """As an action on your turn, you can cower pathetically to
    distract nearby foes. Until the end of your next turn, your
    allies gain advantage on attack rolls against enemies
    within 10 feet of you that can see you. Once you use this
    trait, you can't use it again until you finish a short
    or long rest

    """

    name = "Grovel Cower and Beg"
    source = "Race (Kobold)"


class PackTactics(Feature):
    """You have advantage on an attack roll against a creature
    if at least one of your allies is within 5 feet of the
    creature and the ally isn't incapacitated.
    """

    name = "Pack Tactics"
    source = "Race (Kobold)"


class Aggressive(Feature):
    """As a bonus action, you can move up to your speed
    toward an enemy of your choice that you can see or hear.
    You must end this move closer to the enemy than you started.

    """

    name = "Aggressive"
    source = "Race (Orc)"


# yuan-ti pureblood
class InnateSpellcasting(Feature):
    """You know the poison spray cantrip. You can cast animal
    friendship an unlimited number of times with this trait,
    but you can target only snakes with it. Starting at 3rd level,
    you can also cast suggestion with this trait. Once you cast it,
    you can't do so again until you finish a long rest. Charisma is
    your spellcasting ability for these spells.

    """

    name = "Innate Spellcasting"
    source = "Race (Yuan-Ti Pureblood)"


class MagicResistance(Feature):
    """You have advantage on saving throws against spells and other magical effects."""

    name = "Magic Resistance"
    source = "Race (Yuan_Ti Pureblood)"


class PoisonImmunity(Feature):
    """You are immune to poison damage and the poi~oned condition."""

    name = "Poison Immunity"
    source = "Race (Yuan_Ti Pureblood)"

from dungeonsheets import spells
from dungeonsheets.features.features import Feature


class _SpecialistSpells(Feature):
    """Starting at 3rd level, you always have certain spells pre­pared after
    you reach particular levels in this class, as shown in the Specialization
    Spells table. These spells count as artificer spells for you, but they
    don't count against the number of artificer spells you prepare.
    """

    _name = "Select One"
    source = "Artificer"
    _spells = {3: [], 5: [], 9: [], 13: [], 17: []}
    spells_known = []
    spells_prepared = []

    @property
    def name(self):
        return "{:s} Spells".format(self._name)

    def __init__(self, owner=None):
        if owner is not None:
            level = owner.Artificer.level
            for lvl, spl in self._spells.items():
                if level >= lvl:
                    self.spells_known.extend(spl)
                    self.spells_prepared.extend(spl)
        super().__init__(owner=owner)


# Alchemist
class ArtificerSpellcasting(Feature):
    """You have studied the workings of magic and how to channel it through
    objects. As a result, you have gained the ability to cast spells. To
    observers, you don't appear to be casting spells in a conventional way; you
    look as if you're producing wonders using mundane items or out­landish
    inventions.

    **Tools Required** You produce your artificer spell effects through your
    tools. You must have a spellcasting focus -- specifically thieves' tools or
    some kind of artisan's tool -- in hand when you cast any spell with this
    Spellcasting feature. You must be proficient with the tool to use it in
    this way. See chapter 5, "Equipment," in the Player's Handbook for
    descriptions of these tools.

    After you gain the Infuse Item feature at 2nd level, you can also use any
    item bearing one of your infusions as a spellcasting focus.
    """

    name = "Spellcasting"
    source = "Artificer"


class ArtificerRitualCasting(Feature):
    """You can cast an artificer spell as a ritual if that spell has the ritual
    tag and you have the spell prepared.
    """

    name = "Ritual Casting"
    source = "Artificer"


class FirearmProficiency(Feature):
    """The secrets of creating and operating gunpowder weapons have been
    discovered in various corners of the D&D multiverse. If your Dungeon Master
    uses the rules on firearms in chapter 9 of the Dungeon Master's Guide and
    your artificer has been exposed to the operation of such weapons, your
    artificer is proficient with them.
    """

    name = "Optional Rule: Firearm Proficiency"
    source = "Artificer"


class MagicalTinkering(Feature):
    """At 1st level, you learn how to invest a spark of magic into mundane
    objects. To use this ability, you must have tinker's tools or
    other artisan's tools in hand. You then touch a Tiny nonmagical
    object as an action and give it one of the following magical
    properties of your choice:

    - The object sheds bright light in a 5-foot radius and dim light
      for an additional 5 feet.
    - Whenever tapped by a creature, the object emits a recorded
      message that can be heard up to 10 feet away. You utter the
      message when you bestow this property on the object, and the
      recording can be no more than 6 seconds long.
    - The object continuously emits your choice of an odor or a
      nonverbal sound (wind, waves, chirping, or the like). The chosen
      phenomenon is perceivable up to 10 feet away.
    - A static visual effect appears on one of the object's
      surfaces. This effect can be a picture, up to 25 words of text,
      lines and shapes, or a mixture of these elements, as you
      like. The chosen property lasts indefinitely. As an action, you
      can touch the object and end the property early. You can bestow
      magic on multiple objects, touching one object each time you use
      this feature, though a single object can only bear one property
      at a time. The maximum number of objects you can affect with
      this feature at one time is equal to your Intelligence modifier
      (minimum of one object). If you try to exceed your maximum, the
      oldest property immediately ends, and then the new property
      applies.

    """

    name = "Magical Tinkering"
    source = "Artificer"


class InfuseItem(Feature):
    """At 2nd level, you gain the ability to imbue mundane items with certain
    magical infusions. The magic items you create with this feature are
    effectively prototypes of permanent items.

    Infusions known
      When you gain this feature, pick four artificer infusions to
      learn, choosing from the "Artificer Infusions" section at the
      end of the class's description. You learn additional infusions
      of your choice when you reach certain levels in this class, as
      shown in the Infusions Known column of the Artificer
      table. Whenever you gain a level in this class, you can re­place
      one of the artificer infusions you learned with a new one.
    Infusing an item
      Whenever you finish a long rest, you can touch a non­magical
      object and imbue it with one of your artificer in­fusions,
      turning it into a magic item. An infusion works on only certain
      kinds of objects, as specified in the infusion's description. If
      the item requires attunement, you can attune yourself to it the
      instant you infuse the item. If you decide to attune to the item
      later, you must do so using the normal process for attunement
      (see "Attunement" in chapter 7 of the Dungeon Master's Guide).
      Your infusion remains in an item indefinitely, but when you die,
      the infusion vanishes after a number of days have passed equal
      to your Intelligence modifier (minimum of 1 day). The infusion
      also vanishes if you give up your knowledge of the infusion for
      another one. You can infuse more than one nonmagical object at
      the end of a long rest; the maximum number of objects appears in
      the Infused Items column of the Artificer table. You must touch
      each of the objects, and each of your infusions can be in only
      one object at a time. Moreover, no object can bear more than one
      of your infusions at a time. If you try to exceed your maximum
      number of in­fusions, the oldest infusion immediately ends, and
      then the new infusion applies.

    """

    _name = "Infuse Item"
    source = "Artificer"
    _infusions = {
        # level: (infusions known, infused items)
        2: (4, 2),
        3: (4, 2),
        4: (4, 2),
        5: (4, 2),
        6: (6, 3),
        7: (6, 3),
        8: (6, 3),
        9: (6, 3),
        10: (8, 4),
        11: (8, 4),
        12: (8, 4),
        13: (8, 4),
        14: (10, 5),
        15: (10, 5),
        16: (10, 5),
        17: (10, 5),
        18: (12, 6),
        19: (12, 6),
        20: (12, 6),
    }

    @property
    def name(self):
        known_infusions = self._infusions[self.owner.Artificer.level][0]
        infused_items = self._infusions[self.owner.Artificer.level][1]
        name_ext = " ({:d} Infusions Known, {:d} Infused Items)"
        return self._name + name_ext.format(known_infusions, infused_items)


class ArtificerSpecialist(Feature):
    """At 3rd level, you choose the type of specialist you are: Alchemist,
    Artillerist, or Battle Smith, each of which is detailed at the end of the
    class's description. Your choice grants you features at 5th level and again
    at 9th and 15th level.
    """

    name = "Artificer Specialist"
    source = "Artificer"


class TheRightToolForTheJob(Feature):
    """At 3rd level, you learn how to produce exactly the tool you need: with
    tinker's tools in hand, you can magically create one set of artisan's tools
    in an unoccupied space within 5 feet of you. This creation requires 1 hour
    of uninterrupted work, which can coincide with a short or long rest.
    Though the product of magic, the tools are nonmagical, and they vanish when
    you use this feature again.
    """

    name = "The Right Tool For The Job"
    source = "Artificer"


class ToolExpertise(Feature):
    """Starting at 6th level, your proficiency bonus is doubled for any ability
    check you make that uses your proficiency with a tool.
    """

    name = "Tool Expertise"
    source = "Artificer"


class FlashOfGenius(Feature):
    """Starting at 7th level, you gain the ability to come up with
    solutions under pressure. When you or another creature you can see
    within 30 feet of you makes an ability check or a saving throw,
    you can use your reaction to add your Intelligence modifier to the
    roll.

    You can use this feature a number of times equal to your
    Intelligence modifier (minimum of once). You regain all expended
    uses when you finish a long rest.

    """

    name = "Flash Of Genius"
    source = "Artificer"


class MagicItemAdept(Feature):
    """When you reach 10th level, you achieve a profound understanding of how
    to use and make magic items:

    - You can attune to up to four magic items at once.
    - If you craft a magic item with a rarity of common or uncommon,
      it takes you a quarter of the normal time, and it costs you half
      as much of the usual gold.

    """

    name = "Magic Item Adept"
    source = "Artificer"


class SpellStoringItem(Feature):
    """At 11th level, you learn how to store a spell in an
    object. Whenever you finish a long rest, you can touch one simple
    or martial weapon or one item that you can use as a spellcasting
    focus, and you store a spell in it, choosing a 1st- or 2nd-level
    spell from the artificer spell list that requires 1 action to cast
    (you needn't have it prepared).

    While holding the object, a creature can take an action to produce
    the spell's effect from it, using your spellcasting ability
    modifier. If the spell requires concentration, the creature must
    concentrate. The spell stays in the object until it's been used a
    number of times equal to twice your Intelligence modifier (minimum
    of twice) or until you use this fe ature again to store a spell in
    an object.
    """

    name = "Spell-Storing Item"
    source = "Artificer"


class MagicItemSavant(Feature):
    """At 14th level, your skill with magic items deepens more:

    - You can attune to up to five magic items at once.
    - You ignore all class, race, spell, and level requirements on
      attuning to or using a magic item.

    """

    name = "Magic Item Savant"
    source = "Artificer"


class MagicItemMaster(Feature):
    """Starting at 18th level, you can attune to up to six magic items at
    once.
    """

    name = "Magic Item Master"
    source = "Artificer"


class SoulOfArtifice(Feature):
    """At 20th level, you develop a mystical connection to your magic items,
    which you can draw on for protection:

    - You gain a +1 bonus to all saving throws per magic item you are currently
      attuned to.
    - If you're reduced to 0 hit points but not killed out­right, you
      can use your reaction to end one of your artificer infusions,
      causing you to drop to 1 hit point instead of 0.

    """

    name = "Soul of Artifice"
    source = "Artificer"


# Alchemist
class AlchemistToolProficiency(Feature):
    """When you adopt this specialization at 3rd level, you gain proficiency
    with alchemist's supplies. If you already have this proficiency, you gain
    proficiency with one other type of artisan's tools of your choice.
    """

    name = "Tool Proficiency"
    source = "Artificer (Alchemist)"


class AlchemistSpells(_SpecialistSpells):
    """Starting at 3rd level, you always have certain spells pre­pared after
    you reach particular levels in this class, as shown in the Alchemist Spells
    table. These spells count as artificer spells for you, but they don't count
    against the number of artificer spells you prepare.
    """

    _name = "Alchemist"
    _spells = {
        3: [spells.HealingWord, spells.RayOfSickness],
        5: [spells.FlamingSphere, spells.MelfsAcidArrow],
        9: [spells.GaseousForm, spells.MassHealingWord],
        13: [spells.Blight, spells.DeathWard],
        17: [spells.Cloudkill, spells.RaiseDead],
    }


class ExperimentalElixir(Feature):
    """Beginning at 3rd level, whenever you finish a long rest, you can
    magically produce an *experimental elixir* in an empty flask you touch.
    Roll on the Experimental Elixir table for the elixir's effect, which is
    triggered when someone drinks the elixir. As an action, a creature can
    drink the elixir or administer it to an incapacitated creature.

    Creating an *experimental elixir* requires you to have alchemist supplies
    on your person, and any elixir you create with this feature lasts until it
    is drunk or until the end of your next long rest.

    When you reach certain levels in this class, you can make more elixirs at
    the end of a long rest: two at 6th level and three at 15th level. Roll for
    each elixir's effect separately. Each elixir requires its own flask.

    You can create additional *experimental elixirs* by expending a spell slot
    of 1st level or higher for each one. When you do so, you use your action to
    create the elixir in an empty flask you touch, and you choose the elixir's
    effect from the Experimental Elixir table.

    **Experimental Elixir**

    roll d6

    **1 -- Healing.** The drinker regains a number of hit points equal to 2d4 +
    your Intelligence modifier.

    **2 -- Swiftness.** The drinker's walking speed increases by 10 feet for 1
    hour.

    **3 -- Resilience.** The drinker gains a +1 bonus to AC for 10 minutes.

    **4 -- Boldness.** The drinker can roll a d4 and add the num­ber rolled to
    every attack roll and saving throw they make for the next minute.

    **5 -- Flight.** The drinker gains a flying speed of 10 feet for 10
    minutes.

    **6 -- Transformation.** The drinker's body is transformed as if by the
    alter self spell. The drinker determines the transformation caused by the
    spell, the effects of which last for 10 minutes.
    """

    name = "Experimental Elixir"
    source = "Artificer (Alchemist)"


class AlchemicalSavant(Feature):
    """At 5th level, you develop masterful command of magical chemicals,
    enhancing the healing and damage you create through them. Whenever you
    cast a spell using your alchemist's supplies as the spellcasting focus, you
    gain a bonus to one roll of the spell. That roll must restore hit points or
    be a damage roll that deals acid, fire, necrotic, or poison damage, and the
    bonus equals your Intelligence modifier (minimum of +1).
    """

    name = "Alchemical Savant"
    source = "Artificer (Alchemist)"


class RestorativeReagents(Feature):
    """Starting at 9th level, you can incorporate restorative reagents
    into some of your works:

    - Whenever a creature drinks an experimental elixir you created,
      the creature gains temporary hit points equal to 2d6 + your
      Intelligence modifier (minimum of 1 temporary hit point).
    - You can cast lesser restoration without expending a spell slot
      and without preparing the spell, provided you use alchemist's
      supplies as the spellcasting focus. You can do so a number of
      times equal to your Intelligence modifier (minimum of once), and
      you regain all expended uses when you finish a long rest.

    """

    name = "Restorative Reagents"
    source = "Artificer (Alchemist)"


class ChemicalMastery(Feature):
    """By 15th level, you have been exposed to so many chemicals that they
    pose little risk to you, and you can use them to quickly end
    certain ailments:

    - You gain resistance to acid damage and poison damage, and you
      are immune to the poisoned condition.
    - You can cast greater restoration and heal without expending a
      spell slot, without preparing the spell, and without material
      components, provided you use alchemist's supplies as the
      spellcasting focus. Once you cast either spell with this
      feature, you can't cast that spell with it again until you
      finish a long rest.

    """

    name = "Chemical Mastery"
    source = "Artificer (Alchemist)"


# Artillerist
class ArtilleristSpells(_SpecialistSpells):
    """Starting at 3rd level, you always have certain spells prepared after
    you reach particular levels in this class, as shown in the Artillerist
    Spells table. These spells count as artificer spells for you, but they
    don't count against the number of artificer spells you prepare.
    """

    _name = "Artillerist"
    _spells = {
        3: [spells.Shield, spells.Thunderwave],
        5: [spells.ScorchingRay, spells.Shatter],
        9: [spells.Fireball, spells.WindWall],
        13: [spells.IceStorm, spells.WallOfFire],
        17: [spells.ConeOfCold, spells.WallOfForce],
    }


class ArtilleristToolProficiency(Feature):
    """When you adopt this specialization at 3rd level, you gain proficiency
    with woodcarver's tools. If you already have this proficiency, you gain
    proficiency with one other type of artisan's tools of your choice.
    """

    name = "Tool Proficiency"
    source = "Artificer (Artillerist)"


class EldritchCannon(Feature):
    """At 3rd level, you learn how to create a magical cannon. Using
    woodcarver's tools or smith's tools, you can take an action to magically
    create a Small or Tiny eldritch cannon in an unoccupied space on a
    horizontal surface within 5 feet of you. A Small eldritch cannon occupies
    its space, and a Tiny one can be held in one hand.

    Once you create a cannon, you can't do so again until you finish a long
    rest or until you expend a spell slot of 1st level or higher. You can have
    only one cannon at a time and can't create one while your cannon is
    present.

    The cannon is a magical object. Regardless of size, the cannon has an AC of
    18 and a number of hit points equal to five times your artificer level. It
    is immune to poison damage, psychic damage, and all conditions. If it is
    forced to make an ability check or a saving throw, treat all its ability
    scores as 10 (+O). If the *mending* spell is cast on it, it regains 2d6 hit
    points. It disappears if it is reduced to 0 hit points or after 1 hour. You
    can dismiss it early as an action.

    When you create the cannon, you determine its appearance and whether it
    has legs. You also decide which type it is, choosing from the options on
    the Eldritch Cannons table. On each of your turns, you can take a bonus
    action to cause the cannon to activate if you are within 60 feet of it. As
    part of the same bonus action, you can direct the cannon to walk or climb
    up to 15 feet to an unoccupied space, provided it has legs.

    **Eldritch Cannons**

    *Flamethrower*: The cannon exhales fire in an adjacent 15-foot cone that
    you designate. Each creature in that area must make a Dexterity saving
    throw against your spell save DC, taking 2d8 fire damage on a failed save
    or half as much damage on a successful one. The fire ignites any flammable
    objects in the area that aren't being worn or carried.

    *Force Ballista*: Make a ranged spell attack, originating from the cannon,
    at one creature or object within 120 feet of it. On a hit, the target takes
    2d8 force damage, and if the target is a creature, it is pushed up to 5
    feet away from the cannon.

    *Protector*: The cannon emits a burst of positive energy
    that grants itself and each creature of your choice within 10 feet of it a
    number of temporary hit points equal to 1d8 + your Intelligence modifier
    (minimum of +1)
    """

    name = "Eldritch Cannon"
    source = "Artificer (Artillerist)"


class ArcaneFirearm(Feature):
    """At 5th level, you know how to turn a wand, staff, or rod into an
    arcane firearm, a conduit for your destructive spells. When you
    finish a long rest, you can use wood­carver's tools to carve
    special sigils into a wand, staff, or rod and thereby turn it into
    your arcane firearm. The sigils disappear from the object if you
    later carve them on a different item. The sigils otherwise last
    indefinitely.

    You can use your arcane firearm as a spellcasting focus for your
    artificer spells. When you cast an artificer spell through the
    firearm, roll a d8, and you gain a bonus to one of the spell's
    damage rolls equal to the number rolled.

    """

    name = "Arcane Firearm"
    source = "Artificer (Artillerist)"


class ExplosiveCannon(Feature):
    """Starting at 9th level, every eldritch cannon you create is more
    destructive:

    - The cannon's damage rolls all increase by 1d8.
    - As an action, you can command the cannon to detonate if you are
      within 60 feet of it. Doing so destroys the cannon and forces
      each creature within 20 feet of it to make a Dexterity saving
      throw against your spell save DC, taking 3d8 force damage on a
      failed save or half as much damage on a successful one.

    """

    name = "Explosive Cannon"
    source = "Artificer (Artillerist)"


class FortifiedPosition(Feature):
    """Starting at 15th level, you're a master at forming well-defended
    emplacements using Eldritch Cannon:

    - You and your allies have half cover while within 10 feet of a
      cannon you create with Eldritch Cannon, as a result of a
      shimmering field of magical protection that the cannon emits.
    - You can now have two cannons at the same time. You can create
      two with the same action (but not the same spell slot), and you
      can activate both of them with the same bonus action. You
      determine whether the cannons are identical to each other or
      different. You can't create a third cannon while you have two.

    """

    name = "Fortified Position"
    source = "Artificer (Artillerist)"


# Battle Smith
class BattleSmithSpells(_SpecialistSpells):
    """Starting at 3rd level, you always have certain spells prepared
    after you reach particular levels in this class, as shown in the
    Battle Smith Spells table. These spells count as artificer spells
    for you, but they don't count against the number of artificer
    spells you prepare.

    """

    _name = "Battle Smith"
    _spells = {
        3: [spells.Heroism, spells.Shield],
        5: [spells.BrandingSmite, spells.WardingBond],
        9: [spells.AuraOfVitality, spells.ConjureBarrage],
        13: [spells.AuraOfPurity, spells.FireShield],
        17: [spells.BanishingSmite, spells.MassCureWounds],
    }


class BattleSmithToolProficiency(Feature):
    """When you adopt this specialization at 3rd level, you gain
    proficiency with smith's tools. If you already have this
    proficiency, you gain proficiency with one other type of artisan's
    tools of your choice.

    """

    name = "Tool Proficiency"
    source = "Artificer (Battle Smith)"


class BattleReady(Feature):
    """When you reach 3rd level, your combat training and your experiments with
    magic have paid off in two ways:

    - You gain proficiency with martial weapons.
    - When you attack with a magic weapon, you can use your
      Intelligence modifier, instead of Strength or Dexterity
      modifier, for the attack and damage rolls.

    """

    name = "Battle Ready"
    source = "Artificer (Battle Smith)"


class SteelDefender(Feature):
    """By 3rd level, your tinkering has borne you a faithful companion, a
    steel defender. It is friendly to you and your companions, and it
    obeys your commands. See this creature's game statistics in the
    steel defender stat block. You determine the creature's appearance
    and whether it has two legs or four; your choice has no effect on
    its game statistics.

    In combat, the steel defender shares your initiative count, but it
    takes its turn immediately after yours. It can move and use its
    reaction on its own, but the only action it takes on its turn is
    the Dodge action, unless you take a bonus action on your turn to
    command it to take one of the actions in its stat block or the
    Dash, Disengage, Help, Hide, or Search action.

    If the *mending* spell is cast on it, it regains 2d6 hit
    points. If it has died within the last hour, you can use your
    smith's tools as an action to revive it, provided you are within 5
    feet of it and you expend a spell slot of 1st level or higher. The
    steel defender returns to life after 1 minute with all its hit
    points restored.

    At the end of a long rest, you can create a new steel defender if
    you have your smith's tools with you. If you already have a steel
    defender from this feature, the first one immediately perishes.

    """

    name = "Steel Defender"
    source = "Artificer (Battle Smith)"


class ExtraAttackBattleSmith(Feature):
    """Starting at 5th level, you can attack twice, rather than once,
    whenever you take the Attack action on your turn.

    """

    name = "Extra Attack"
    source = "Artificer (Battle Smith)"


class ArcaneJolt(Feature):
    """At 9th level, you learn new ways to channel arcane energy to harm
    or heal. When either you hit a target with a magic weapon attack
    or your steel defender hits a target, you can channel magical
    energy through the strike to create one of the following effects:

    - The target takes an extra 2d6 force damage.
    - Choose one creature or object you can see within 30 feet of the
      target.  Healing energy flows into the chosen recipient,
      restoring 2d6 hit points to it. You can use this energy a number
      of times equal to your Intelligence modifier (minimum of once),
      but you can do so no more than once on a turn. You regain all
      expended uses when you finish a long rest

    """

    name = "Arcane Jolt"
    source = "Artificer (Battle Smith)"


class ImprovedDefender(Feature):
    """At 15th level, your Arcane jolt and steel defender be­come more
    powerful:

    - The extra damage and the healing of your Arcane jolt both
      increase to 4d6.
    - Your steel defender gains a +2 bonus to Armor Class.
    - Whenever your steel defender uses its Deflect Attack, the
      attacker takes force damage equal to 1d4 +your Intelligence
      modifier.

    """

    name = "Improved Defender"
    source = "Artificer (Battle Smith)"

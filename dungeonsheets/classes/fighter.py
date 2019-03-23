from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class Champion(SubClass):
    """The archetypal Champion focuses on the development of raw physical power
    honed to deadly perfection. Those who model themselves on this archetype
    combine rigorous training with physical excellence to deal devastating
    blows.

    """
    name = "Champion"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.ImprovedCritical]
    features_by_level[7] = [features.RemarkableAthelete]
    features_by_level[10] = [features.AdditionalFightingStyle]
    features_by_level[15] = [features.SuperiorCritical]
    features_by_level[18] = [features.Survivor]
    

class BattleMaster(SubClass):
    """Those who emulate the archetypal Battle Master employ martial techniques
    passed down through generations. To a Battle Master, combat is an academic
    field, sometimes including subjects beyond battle such as weaponsmithing
    and calligraphy. Not every fighter absorbs the lessons of history, theory,
    and artistry that are reflected in the Battle Master archetype, but those
    who do are well-rounded fighters of great skill and knowledge

    """
    name = "Battle Master"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.CombatSuperiority, features.StudentOfWar]
    features_by_level[7] = [features.KnowYourEnemy]
    features_by_level[15] = [features.Relentless]
    

class EldritchKnight(SubClass):
    """The archetypal Eldritch Knight combines the martial mastery common to all
    fighters with a careful study of magic. Eldritch Knights use magical
    techniques similar to those practiced by wizards. They focus their study on
    two of the eight schools of magic: abjuration and evocation. Abjuration
    spells grant an Eldritch Knight additional protection in battle, and
    evocation spells deal damage to many foes at once, extending the fighter’s
    reach in combat. These knights learn a comparatively small number of
    spells, committing them to memory instead of keeping them in a spellbook.

    """
    name = "Eldritch Knight"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.EldritchKnightSpellcasting,
                            features.WeaponBond]
    features_by_level[7] = [features.WarMagic]
    features_by_level[10] = [features.EldritchStrike]
    features_by_level[15] = [features.ArcaneCharge]
    features_by_level[18] = [features.ImprovedWarMagic]
    spellcasting_ability = 'intelligence'
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        4:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        6:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        7:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        8:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        9:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        10: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        11: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        12: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        13: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        14: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        15: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        16: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        17: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        18: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        19: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        20: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    }
    

# SCAG
class PurpleDragonKnight(SubClass):
    """Purple Dragon knights are warriors who hail from the kingdom of
    Cormyr. Pledged to protect the crown, they take the fight against evil
    beyond their kingdom's borders. They are tasked with wandering the land as
    knights errant, relying on their judgment, bravery, and fidelity to the
    code of chivalry to guide them in defeating evildoers.

    A Purple Dragon knight inspires greatness in others by committing brave
    deeds in battle. The mere presence of a knight in a hamlet is enough to
    cause some ores and bandits to seek easier prey. A lone knight is a skilled
    warrior, but a knight leading a band of allies can transform even the most
    poorly equipped militia into a ferocious war band.

    A knight prefers to lead through deeds, not words. As a knight spearheads
    an attack, the knight's actions can awaken reserves of courage and
    conviction in allies that they never suspected they had.

    """
    name = "Purple Dragon Knight"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.RallyingCry]
    features_by_level[7] = [features.RoyalEnvoy]
    features_by_level[10] = [features.InspiringSurge]
    features_by_level[15] = [features.Bulwark]
    

# XGTE
class ArcaneArcher(SubClass):
    """An Arcane Archer studies a unique elven method of archery that weaves magic
    into attacks to produce supernatural effects. Arcane Archers are some of
    the most elite warriors among the elves. They stand watch over the fringes
    of elven domains, keeping a keen eye out for trespassers and using
    magic—infused arrows to defeat monsters and invaders before they can reach
    elven set— tlements. Over the centuries, the methods of these elf archers
    have been learned by members of other races who can also balance arcane
    aptitude with archery.

    """
    name = "Arcane Archer"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.ArcaneArcherLore, features.ArcaneShot]
    features_by_level[7] = [features.MagicArrow, features.CurvingShot]
    features_by_level[15] = [features.EverReadyShot]
    

class Cavalier(SubClass):
    """The archetypal Cavalier excels at mounted combat. Usually born among the
    nobility and raised at court, a Cavalier is equally at home leading a
    cavalry charge or exchanging repartee at a state dinner. Cavaliers also
    learn how to guard those in their charge from harm, often serving as the
    protectors of their superiors and of the weak. Compelled to right wrongs or
    earn prestige, many of these fighters leave their lives of comfort to
    embark on glorious adventure

    """
    name = "Cavalier"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.BonusProficiencyCavalier,
                            features.BornToTheSaddle, features.UnwaveringMark]
    features_by_level[7] = [features.WardingManeuver]
    features_by_level[10] = [features.HoldTheLine]
    features_by_level[15] = [features.FerociousCharger]
    features_by_level[18] = [features.VigilantDefender]
    

class Samurai(SubClass):
    """The Samurai is a fighter who draws on an implacable fighting spirit to
    overcome enemies. A Samurai’s resolve is nearly unbreakable, and the
    enemies in a Samurai's path have two choices: yield or die fighting

    """
    name = "Samurai"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.BonusProficiencySamurai,
                            features.FightingSpirit]
    features_by_level[7] = [features.ElegantCourtier]
    features_by_level[10] = [features.TirelessSpirit]
    features_by_level[15] = [features.RapidStrike]
    features_by_level[18] = [features.StrengthBeforeDeath]

    
# Custom
class Gunslinger(SubClass):
    """Most warriors and combat specialists spend their years perfecting the
    classic arts of swordplay, archery, or polearm tactics. Whether duelist or
    infantry, martial weapons were seemingly perfected long ago, and the true
    challenge is to master them.

    However, some minds couldn't stop with the innovation of the
    crossbow. Experimentation with alchemical components and rare metals have
    unlocked the secrets of controlled explosive force. The few who survive
    these trials of ingenuity may become the first to create, and deftly wield,
    the first firearms.

    This archetype focuses on the ability to design, craft, and utilize
    powerful, yet dangerous ranged weapons. Through creative innovation and
    immaculate aim, you become a distance force of death on the
    battlefield. However, not being a perfect science, firearms carry an
    inherent instability that can occastionally leave you without a functional
    means of attack. This is the danger of new, untested technologies in a
    world where arcane energies that rule the elements are ever present.

    Should this path of powder, fire, and metal call to you, keep your wits
    about you, hold on to your convictions as a fighter, and let skill meet
    luck to guide your bullets to strike true.

    """
    name = "Gunslinger"
    weapon_proficiencies = (weapons.firearms)
    _proficiencies_text = ('firearms', "tinker's tools")
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.Gunsmith, features.AdeptMarksman]
    features_by_level[7] = [features.QuickDraw]
    features_by_level[10] = [features.RapidRepair]
    features_by_level[15] = [features.LightningReload]
    features_by_level[18] = [features.ViciousIntent,
                             features.HemorrhagingCritical]


class Fighter(CharClass):
    name = 'Fighter'
    hit_dice_faces = 10
    subclass_select_level = 3
    saving_throw_proficiencies = ('strength', 'constitution')
    primary_abilities = ('strength', 'dexterity',)
    _proficiencies_text = ('All armor', 'shields', 'simple weapons',
                           'martial weapons')
    weapon_proficiencies = (weapons.SimpleWeapon, weapons.MartialWeapon)
    multiclass_weapon_proficiencies = weapon_proficiencies
    _multiclass_proficiencies_text = ('light armor', 'medium armor',
                                      'shields', 'simple weapons',
                                      'martial weapons')
    class_skill_choices = ('Acrobatics', 'Animal Handling',
                           'Athletics', 'History', 'Insight', 'Intimidation',
                           'Perception', 'Survival')
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.FighterFightingStyle, features.SecondWind]
    features_by_level[2] = [features.ActionSurge]
    features_by_level[5] = [features.ExtraAttackFighter]
    features_by_level[9] = [features.Indomitable]
    subclasses_available = (Champion, BattleMaster, EldritchKnight,
                            PurpleDragonKnight, ArcaneArcher, Cavalier,
                            Samurai, Gunslinger)

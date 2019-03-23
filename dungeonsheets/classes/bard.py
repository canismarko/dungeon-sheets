from .. import (weapons, features)
from .classes import CharClass, SubClass
from collections import defaultdict


# PHB
class CollegeOfLore(SubClass):
    """Bards of the College o f Lore know something about most things, collecting
    bits of knowledge from sources as diverse as scholarly tomes and peasant
    tales. Whether singing folk ballads in taverns or elaborate compositions in
    royal courts, these bards use their gifts to hold audiences
    spellbound. When the applause dies down, the audience members might find
    themselves questioning everything they held to be true, from their faith in
    the priesthood of the local temple to their loyalty to the king.

    The loyalty of these bards lies in the pursuit of beauty and truth, not in
    fealty to a monarch or following the tenets of a deity. A noble who keeps
    such a bard as a herald or advisor knows that the bard would rather be
    honest than politic.

    The college’s members gather in libraries and sometimes in actual colleges,
    complete with classrooms and dormitories, to share their lore with one
    another. They also meet at festivals or affairs of state, where they can
    expose corruption, unravel lies, and poke fun at selfimportant figures of
    authority.

    """
    name = "College of Lore"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.LoreProficiencies, features.CuttingWords]
    features_by_level[6] = [features.AdditionalMagicalSecrets]
    features_by_level[14] = [features.PeerlessSkill]


class CollegeOfValor(SubClass):
    """Bards of the College of Valor are daring skalds whose tales keep alive the
    memory of the great heroes of the past, and thereby inspire a new
    generation of heroes. These bards gather in mead halls or around great
    bonfires to sing the deeds of the mighty, both past and present. They
    travel the land to witness great events firsthand and to ensure that the
    memory of those events doesn’t pass from the world. With their songs, they
    inspire others to reach the same heights of accomplishment as the heroes of
    old

    """
    name = "College of Valor"
    weapon_proficiencies = (weapons.MartialWeapon,)
    _proficencies_text = ('martial weapons', 'medium armor', 'shields')
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.CombatInspiration]
    features_by_level[6] = [features.BardExtraAttack]
    features_by_level[14] = [features.BardBattleMagic]


# XGTE
class CollegeOfGlamour(SubClass):
    """The College of Glamour is the home Of bards who mas— tered their craft in
    the vibrant realm of the Feywild or under the tutelage Of someone who
    dwelled there. Tutored by satyrs, eladrin, and other fey, these bards
    learn to use their magic to delight and captivate others.

    The bards of this college are regarded with a mixture of awe and
    fear. Their performances are the stuff of legend. These bards are so
    eloquent that a speech or song that one of them performs can cause captors
    tO release the bard unharmed and can lull a furious dragon into
    complacency. The same magic that allows them to quell beasts can also bend
    minds. Villainous bards Of this college can leech Off a community for
    weeks, misusing their magic to turn their hosts into thralls. Heroic bards
    of this college instead use this power to gladden the downtrodden and
    undermine oppressors.

    """
    name = "College of Glamour"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.MantleOfInspiration,
                            features.EnthrallingPerformance]
    features_by_level[6] = [features.MantleOfMajesty]
    features_by_level[14] = [features.UnbreakableMajesty]


class CollegeOfSwords(SubClass):
    """Bards of the College of Swords are called blades, and they entertain
    through daring feats of weapon prowess. Blades perform stunts such as sword
    swallowing, knife throwing and juggling, and mock combats. Though they use
    their weapons to entertain, they are also highly trained and skilled
    warriors in their own right.

    Their talent with weapons inspires many blades to lead double lives. One
    blade might use a circus troupe as cover for nefarious deeds such as
    assassination, robbery, and blackmail. Other blades strike at the wicked,
    bringingjustice to bear against the cruel and powerful. Most troupes are
    happy to accept a blade’s talent for the excitement it adds to a
    performance, but few entertainers fully trust a blade in their ranks.

    Blades who abandon their lives as entertainers have often run into trouble
    that makes maintaining their secret activities impossible. A blade caught
    stealing or engaging in vigilante justice is too great a liability for most
    troupes. With their weapon skills and magic, these blades either take up
    work as enforcers for thieves’ guilds or strike out on their own as
    adventurers.

    """
    name = "College of Swords"
    features_by_level = defaultdict(list)
    weapon_prociciencies = (weapons.Scimitar,)
    _proficiencies_text = ('medium armor', 'scimitar')
    features_by_level[3] = [features.SwordsProficiency,
                            features.BardFightingStyle,
                            features.BladeFlourish]
    features_by_level[6] = [features.BardExtraAttack]
    features_by_level[14] = [features.MastersFlourish]


class CollegeOfWhispers(SubClass):
    """Most folk are happy to welcome a bard into their midst. Bards of the
    College of Whispers use this to their advantage. They appear to be like
    other bards, sharing news, singing songs, and telling tales to the
    audiences they gather. In truth, the College of Whispers teaches its
    students that they are wolves among sheep. These bards use their knowledge
    and magic to uncover secrets and turn them against others through extortion
    and threats.

    Many other bards hate the College of Whispers, viewing it as a parasite
    that uses a bard’s reputation to acquire wealth and power. For this reason,
    members of this college rarely reveal their true nature. They typically
    claim to follow some other college, or they keep their actual calling
    secret in order to infiltrate and exploit royal courts and other settings
    of power

    """
    name = "College of Whispers"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.PsychicBlades, features.WordsOfTerror]
    features_by_level[6] = [features.MantleOfWhispers]
    features_by_level[14] = [features.ShadowLore]


class Bard(CharClass):
    name = 'Bard'
    hit_dice_faces = 8
    subclass_select_level = 3
    saving_throw_proficiencies = ('dexterity', 'charisma')
    primary_abilities = ('charisma',)
    _proficiencies_text = (
        'Light armor', 'simple weapons', 'hand crossbows', 'longswords',
        'rapiers', 'shortswords', 'three musical instruments of your choice')
    weapon_proficiencies = (weapons.HandCrossbow, weapons.Longsword,
                            weapons.Rapier, weapons.Shortsword,
                            weapons.SimpleWeapon)
    class_skill_choices = ('Acrobatics', 'Animal Handling', 'Arcana',
                           'Athletics', 'Deception', 'History', 'Insight',
                           'Intimidation', 'Investigation', 'Medicine',
                           'Nature', 'Perception', 'Performance', 'Persuasion',
                           'Religion', 'Sleight of Hand', 'Stealth',
                           'Survival')
    multiclass_weapon_proficiencies = ()
    _multiclass_proficiencies_text = ('Light Armor', '[choose one skill]',
                                      '[choose one musical instrument]')
    num_skill_choices = 3
    subclasses_available = (CollegeOfLore, CollegeOfValor, CollegeOfGlamour,
                            CollegeOfSwords, CollegeOfWhispers)
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.BardicInspiration]
    features_by_level[2] = [features.SongOfRest, features.JackOfAllTrades]
    features_by_level[3] = [features.BardExpertise]
    features_by_level[5] = [features.FontOfInspiration]
    features_by_level[6] = [features.Countercharm]
    features_by_level[10] = [features.MagicalSecrets]
    features_by_level[20] = [features.SuperiorInspiration]
    spellcasting_ability = 'charisma'
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1:  (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        2:  (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        3:  (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        4:  (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        5:  (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        6:  (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        7:  (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        8:  (3, 4, 3, 3, 2, 0, 0, 0, 0, 0),
        9:  (4, 4, 3, 3, 3, 1, 0, 0, 0, 0),
        10: (4, 4, 3, 3, 3, 2, 0, 0, 0, 0),
        11: (4, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        12: (4, 4, 3, 3, 3, 2, 1, 0, 0, 0),
        13: (4, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        14: (4, 4, 3, 3, 3, 2, 1, 1, 0, 0),
        15: (4, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        16: (4, 4, 3, 3, 3, 2, 1, 1, 1, 0),
        17: (4, 4, 3, 3, 3, 2, 1, 1, 1, 1),
        18: (4, 4, 3, 3, 3, 3, 1, 1, 1, 1),
        19: (4, 4, 3, 3, 3, 3, 2, 1, 1, 1),
        20: (4, 4, 3, 3, 3, 3, 2, 2, 1, 1),
    }

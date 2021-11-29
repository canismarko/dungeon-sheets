from dungeonsheets.features.features import Feature, FeatureSelector
from dungeonsheets.features.fighter import Archery, Dueling, GreatWeaponFighting, TwoWeaponFighting


#Blood Hunter  
class HunterBane(Feature):
    """Beginning at 1st level, you have survived the Hunter’s Bane, a dangerous, long-guarded ritual that alters your life’s blood, forever binding you to the darkness and honing your senses against it. You have advantage on Wisdom (Survival) checks to track fey, fiends, or undead, as well as on Intelligence ability checks to recall information about them.

The Hunter’s Bane also empowers your body to control and shape hemocraft magic, using your own blood and life essence to fuel your abilities. Some of your features require your target to make a saving throw to resist the feature’s effects. The saving throw DC is calculated as follows:

Hemocraft save DC = 8 + your proficiency bonus + your Intelligence modifier.

    """

    name = "Hunter's Bane"
    source = "Blood Hunter"


class BloodMaledict(Feature):
    """At 1st level, you gain the ability to channel, and sometimes sacrifice, a part of your vital essence to curse and manipulate creatures through hemocraft magic. You gain one blood curse of your choice, detailed in the “Blood Curses” section at the end of the class description. You learn one additional blood curse of your choice, and you can choose one of the blood curses you know and replace it with another blood curse, at 6th, 10th, 14th, and 18th level.

When you use your Blood Maledict, you choose which curse to invoke. While invoking a blood curse, but before it affects the target, you can choose to amplify the curse by losing a number of hit points equal to one roll of your hemocraft die, as shown in the Hemocraft Die column of the Blood Hunter table. An amplified curse gains an additional effect, noted in the curse’s description. Creatures that do not have blood in their bodies are immune to blood curses, unless you have amplified the curse.

You can use this feature once. Beginning at 6th level, you can use your Blood Maledict feature twice, at 13th level you can use it three times between rests, and at 17th level, you can use it four times between rests. You regain all expended uses when you finish a short or long rest.

    """

    name = "Blood Maledict"
    source = "Blood Hunter"


class BloodHunterFightingStyle(FeatureSelector):
    """At 2nd level, you adopt a style of fighting as your specialty. Choose one of the following options. You can’t take a Fighting Style option more than once, even if you later get to choose again.
Archery

You gain a +2 bonus to attack rolls you make with ranged weapons.

Dueling

When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.

Great Weapon Fighting

When you roll a 1 or 2 on a non-rite damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll. The weapon must have the two-handed or versatile property for you to gain this benefit.

Two-Weapon Fighting

When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.

    """
    
    options = {
    	"archery": Archery,
        "dueling": Dueling,
        "great": GreatWeaponFighting,
        "great-weapon fighting": GreatWeaponFighting,
        "two-weapon fighting": TwoWeaponFighting,
        "two-weapon": TwoWeaponFighting,
        "dual wield": TwoWeaponFighting,
    }
    name = "Fighting Style (Select One)"
    source = "Blood Hunter"


class CrimsonRites(Feature):
    """At 2nd level, you learn to invoke a rite of hemocraft within your weapon at the cost of your own vitality. Choose one rite from the Primal Rites list below to learn.

As a bonus action, you can activate a crimson rite on a single weapon with the elemental energy of a known rite of your choice that lasts until you finish a short or long rest, or if you aren’t holding the weapon at the end of your turn. When you activate a rite, you lose a number of hit points equal to one roll of your hemocraft die, as shown in the Hemocraft Die column of the Blood Hunter table.

For the duration, attacks from this weapon deal an additional 1d4 damage of the chosen rite’s type. This damage is magical, and increases as you gain levels as a blood hunter, as shown in the Hemocraft Die column of the Blood Hunter table. A weapon can only hold a single active rite at a time.

You learn an additional Primal Rite at 7th level, and access to an Esoteric Rite at 14th level.
   
    """
    
    name = "Crimson Rites"
    source = "Blood Hunter"


class ExtraAttackBloodHunter(Feature):
    """Beginning at 5th level, you can attack twice, instead of once, whenever you
    take the Attack action on your turn.

    """

    name = "Extra Attack (2x)"
    source = "Blood Hunter"


class BrandOfCastigation(Feature):
    """At 6th level, whenever you damage a creature with your Crimson Rite feature, you can choose to sear an arcane brand of hemocraft magic into it (requires no action). You always know the direction to the branded creature, and each time the branded creature deals damage to you or a creature you can see within 5 feet of you, the creature takes psychic damage equal to your Intelligence modifier (minimum of 1 damage).

Your brand lasts until you dismiss it, or you apply a brand to another creature. Your brand counts as a spell for the purposes of dispel magic, and the spell level is equal to half of your blood hunter level (maximum of 9th level spell).

Once you use this feature, you can’t use it again until you finish a short or long rest.
    
    """


class GrimPsychometry(Feature):
    """When you reach 9th level, you have a supernatural talent for discerning the history surrounding mysterious objects or places touched by evil. When making an Intelligence (History) check to recall information about a darker past surrounding an object you are touching, or a location you are present in, you have advantage on the roll. The information gleaned often leans towards the more sinister influences of the past, and sometimes conveys visions of things previously unknown to the character on higher rolls.
    
    """

    name = "Grim Psychometry"
    source = "Blood Hunter"


class DarkAugmentation(Feature):
    """Upon reaching 10th level, arcane blood magic suffuses your body, permanently reinforcing your resilience. Your speed increases by 5 feet, and whenever you make a Strength, Dexterity, or Constitution saving throw, you gain a bonus to the saving throw equal to your Intelligence modifier (minimum of +1).
    
    """

    name = "Dark Augmentation"
    source = "Blood Hunter"
    
    
class BrandOfTethering(Feature):
    """Starting at 13th level, the psychic damage from your Brand of Castigation increases to twice your Intelligence modifier (minimum of 2 damage).

In addition, a branded creature can’t take the Dash action, and if a creature branded by you attempts to teleport or leave their current plane via ability, spell, or portal, they take 4d6 psychic damage and must make a Wisdom saving throw. On a failure, the teleport or plane shift fails.
    
    """
    
    name = "Brand of Thethering"
    source = "Blood Hunter"
    

class HardenedSoul(Feature):
    """When you reach 14th level, you have advantage on saving throws against being charmed and frightened.
    
    """
    
    name = "Hardened Soul"
    source = "Blood Hunter"


class SanguineMastery(Feature):
    """Upon becoming 20th level, you hone your control over blood magic, mitigating your sacrifice and empowering your capability. Once per turn, whenever a blood hunter feature requires you to roll a hemocraft die, you can choose to reroll the die and choose which result to use.

In addition, whenever you score a critical hit with a weapon attack empowered by your Crimson Rite, you regain one expended use of your Blood Maledict feature.
    
    """
    
    name = "Sanguine Mastery"
    source = "Blood Hunter"
    
    
# All Rites
class Rites(Feature):
    """
    A generic Rite. Add details in features/bloodhunter.py
    """

    name = "Unnamed rite"
    source = "BloodHunter (Crimson Rites)"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if "M" in s.components:
            c = list(s.components)
            c.remove("M")
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self, owner):
        super().__init__(owner)
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)


class RiteOfTheFlame(Rites):
    """Your rite damage is fire damage.
    
    """
    
    name = "Rite of the Flame"


class RiteOfTheFrozen(Rites):
    """Your rite damage is cold damage.

    """
    
    name = "Rite of the Frozen"
    
class RiteOfTheStorm(Rites):
    """Your rite damage is lightning damage.
    
    """    
    
    name = "Rite of the Storm"
    

class RiteOfTheDead(Rites):
    """Your rite damage is necrotic damage
    
    **Prerequisite: 14th level**
    
    """
    
    name = "Rite of the Dead"
    

class RiteOfTheOracle(Rites):
    """Your rite damage is psychic damage
    
    **prerequisite: 14th level**
    
    """
    
    name = "Rite of the Oracle"


class RiteOfTheRoar(Rites):
    """Your rite damage is thunder damage
    
    **Prerequisite: 14th level**
    
    """
    
    name = "Rite of the Roar"
    

#Blood Curses
class BloodCurses(Feature):
    """
    A generic BloodCurse. Add details in features/bloodhunter.py
    """

    name = "Unnamed Curse"
    source = "BloodHunter (Blood Maledict)"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if "M" in s.components:
            c = list(s.components)
            c.remove("M")
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self, owner):
        super().__init__(owner)
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)


class BloodCurseoftheAnxious(BloodCurses):
    """As a bonus action, you magnify the adrenaline in the body of a creature within 30 feet of you, making them susceptible to forceful influence. Until the end of your next turn, all creatures have advantage on Charisma (Intimidation) checks directed at the target creature.

Amplify. The next Wisdom saving throw the target makes before this curse ends has disadvantage. Once you’ve amplified this blood curse, you must finish a long rest before you can amplify it again.
    
    """
    
    name = "Blood Curse of the Anxious"
    
    
class BloodCurseofBinding(BloodCurses):
    """As a bonus action, you can attempt to bind a creature you can see within 30 feet of you that is no more than one size larger than you. The target must succeed on a Strength saving throw or have their speed be reduced to 0 and they can’t use reactions until the end of your next turn.

Amplify. This curse lasts for 1 minute and can affect a creature regardless of their size. At the end of each of its turns, the cursed creature can make another Strength saving throw. On a success, this curse ends.
    
    """
    
    name = "Blood Curse of Binding"    


class BloodCurseOfBloatedAgony(BloodCurses):
    """As a bonus action, you curse a creature that you can see within 30 feet of you to painfully swell until the end of your next turn. For the duration of this curse, the creature has disadvantage on Strength and Dexterity ability checks, and suffers 1d8 necrotic damage if it makes more than one melee or ranged attack during its turn.

Amplify. This curse lasts for 1 minute. At the end of each of its turns, the cursed creature can make a Constitution saving throw. On a success, this curse ends.
    
    """
    
    name = "Blood Curse of Bloated Agony"


class BloodCurseOfCorrosion(BloodCurses):
    """**Prerequisite: 15th level, Order of the Mutant**

As a bonus action, a creature within 30 feet of you becomes poisoned. At the end of each of its turns, the target can make another Constitution saving throw. On a success, the curse ends.

Amplify. The cursed creature suffers 4d6 necrotic damage, and suffers this damage again every time it fails its Constitution saving throw to end this curse at the end of its turn.
    
    """
    
    name = "Blood Curse of Corrosion"


class BloodCurseOfTheExorcist(BloodCurses):
    """**Prerequisite: 15th level, Order of the Ghostslayer**

As a bonus action, you can choose one creature you can see within 30 feet of you that is charmed, frightened, or possessed. The target creature is no longer charmed, frightened, or possessed.

Amplify. The creature that charmed, frightened, or possessed the target of your curse suffers 3d6 psychic damage and must make a Wisdom saving throw or be stunned until the end of your next turn.
    
    """
    
    name = "Blood Curse of the Exorcist"


class BloodCurseOfExposure(BloodCurses):
    """When a creature you can see within 30 feet is hit by an attack or spell, you can use your reaction to temporarily weaken their resilience against it. Until the end of the turn, the target loses resistance to the damage types of the triggering attack or spell.

Amplify. The target instead loses invulnerability to the damage types of the triggering attack or spell, having resistance to them until the end of the turn.
    
    """
    
    name = "Blood Curse of Exposure"
    

class BloodCurseOfTheEyeless(BloodCurses):
    """When a creature you can see within 30 feet of you makes an attack roll, you can use your reaction to roll one hemocraft die and subtract the number rolled from the creature’s attack roll. You can choose to use this feature after the creature’s roll, but before the DM determines whether the attack roll succeeds. The creature is immune if it is immune to blindness.

Amplify. You apply this curse to all of the creature’s attack rolls until the end of the turn. You roll a new hemocraft die for each affected attack.
    
    """
    
    name = "Blood Curse of Exposure"
    

class BloodCurseOfTheFallenPuppet(BloodCurses):
    """When a creature you can see within 30 feet of you drops to 0 hit points, you can use your reaction to give that creature a final act of aggression. That creature immediately makes a single weapon attack against a target of your choice within its attack range.

Amplify. You can first move the cursed creature up to half their speed, and you grant a bonus to the cursed creature’s attack roll equal to your Intelligence modifier (minimum of +1).
    
    """
    
    name = "Blood Curse of the Fallen Puppet"
    

class VloodCurseOfTheHowl(BloodCurses):
    """**Prerequisite: 18th level, Order of the Lycan**

As an action, you unleash a blood-curdling howl. Each creature within 30 feet of you that can hear you must succeed on a Wisdom saving throw or become frightened of you until the end of your next turn. If they fail their saving throw by 5 or more, they are stunned while frightened in this way. A creature that succeeds on this saving throw is immune to this blood curse for the next 24 hours.

You can choose any number of creatures you can see to be unaffected by the howl.

Amplify. The range of this curse increases to 60 feet.
    
    """
    
    name = "Blood Curse of the Howl"


class BloodCurseOfTheMarked(BloodCurses):
    """As a bonus action, you can mark a creature that you can see within 30 feet of you. Until the end of your turn, whenever you deal rite damage to the target, you roll an additional hemocraft die of rite damage.

Amplify. The next attack roll you make against the target before the end of your turn has advantage.
    
    """
    
    name = "Blood Curse of the Marked"
    

class BloodCurseOfTheMuddledMind(BloodCurses):
    """As a bonus action, you curse a creature that you can see within 30 feet of you that is concentrating on a spell. That creature has disadvantage on the next Constitution saving throw it must make to maintain concentration before the end of your next turn.

Amplify. The cursed creature has disadvantage on all Constitution saving throws made to maintain concentration of spells until the end of your next turn.
    
    """    
    
    name = "Blood Curse of the Muddled Mind"


class BloodCurseOfTheSouleater(BloodCurses):
    """**Prerequisite: 18th level, Order of the Profane Soul**

When a creature that isn’t a construct or undead is reduced to 0 hit points within 30 feet of you, you can use your reaction to usher their soul to your patron in exchange for power. Until the end of your next turn, your weapon attacks have advantage.

Amplify. In addition, you regain an expended warlock spell slot. Once you’ve amplified this blood curse, you must finish a long rest before you can amplify it again
    
    """    
    
    name = "Blood Curse of the Souleater"


#Order of the Ghostslayer
class CurseSpecialist(Feature):
    """Beginning at 3rd level, your ancient order teaches advanced mastery over blood curses. You gain an additional use of your Blood Maledict feature. In addition, your blood curses can target any creature, whether it has blood or not.
    
    """
    
    name = "Curse Specialist"
    source = "Blood Hunter (Order of the Ghostslayer)"


class RiteOfTheDawn(Rites):
    """When you join this order at 3rd level, you learn the Rite of the Dawn esoteric rite (detailed below).

Rite of the Dawn. Your rite damage is radiant damage. While the rite is active, you gain the following benefits:

    Your weapon sheds bright light out to a radius of 20 feet.
    You have resistance to necrotic damage.
    Your weapon deals one additional hemocraft die of rite damage when you hit an undead

    """
    
    name = "Rite of the Dawn"
    source = "Blood Hunter (Order of the Ghostslayer)"


class EtherealStep(Feature):
    """Upon reaching 7th level, at the start of your turn, if you aren’t incapacitated, you can choose to magically step into the veil between the planes.

You can move through other creatures and objects as if they were difficult terrain, as well as see and affect creatures and objects on the Ethereal Plane. You take 1d10 force damage if you end your turn inside an object. If you are inside an object when this feature ends, you are immediately shunted to the nearest unoccupied space that you can occupy and take force damage equal to twice the number of feet you moved. This feature lasts for a number of rounds equal to your Intelligence modifier (minimum of 1 round).

You can use this feature once. Beginning at 15th level, you can use your Ethereal Step feature twice between rests. You regain all expended uses when you finish a short or long rest.
    
    """
    
    name = "Ethereal Step"
    source = "Blood Hunter (Order of the Ghostslayer)"
    
    
class BrandOfSundering(Feature):
    """Beginning at 11th level, your Brand of Castigation now exposes a fragment of your foe’s essence, leaving them vulnerable to your Crimson Rite. Whenever you damage a branded creature with your Crimson Rite, your weapon deals one additional hemocraft die of rite damage. In addition, the branded creature can’t move through creatures or objects.
    
    """
    
    name = "Brand of Sundering"
    source = "Blood HUnter (Order of the Ghostslayer)"
    
    
class BloodCurseOfTheExorcist(Feature):
    """At 15th level, you’ve honed your hemocraft to tear wicked influence from your allies, punishing those who would infiltrate their body and mind. You gain the Blood Curse of the Exorcist for your Blood Maledict feature. This doesn’t count against your number of blood curses known.
    
    """
    
    name = "Blood Curse of the Exorcist"
    source = "Blood Hunter (Order of the Ghostslayer"
    
    
class RiteRevival(Feature):
    """Upon reaching 18th level, you learn to protect your fading life by absorbing your blood rite. When you are reduced to 0 hit points while you have an active Crimson Rite, but don’t die outright, the rite ends and you drop to 1 hit point instead. If you have rites active on multiple weapons, you choose which one ends.
    
    """
    
    name = "Revival"
    source = "Blood Hunter (Order of the Ghostslayer)"
    
    
#Order of the Lycan
class HeightenedSenses(Feature):
    """Starting when you choose this archetype at 3rd level, you begin to adopt the improved abilities of a natural predator. You gain advantage on Wisdom (Perception) checks that rely on hearing or smell.
    
    """
    
    name = "Revival"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class HybridTransformation(Feature):
    """Upon choosing this archetype at 3rd level, you begin to learn to control the lycanthropic curse that now lives in your blood. As a bonus action, you can transform into your hybrid form for up to 1 hour. You can speak, use equipment, and wear armor in this form. You can revert to your normal form earlier as a bonus action. You automatically revert to your normal form if you fall unconscious, drop to 0 hit points, or die. This feature replaces the rules for Lycanthropy within the Monster’s Manual.

Once you use this feature, you must finish a short or long rest before you can use it again.

While you are transformed, you gain the following features:

Feral Might. You gain a +1 to melee damage rolls. This bonus increases by 1 at 11th and 18th level. You also have advantage on Strength checks and Strength saving throws.

Resilient Hide. You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks not made with silver weapons. While you are not wearing heavy armor, you gain a +1 bonus to your AC.

Predatory Strikes. You can apply your Crimson Rite feature to your unarmed strikes as a single weapon. You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes. When you use the Attack action with an unarmed strike, you can make one unarmed strike as a bonus action.

Your unarmed strikes deal 1d6 slashing damage. The damage increases to 1d8 at 11th level.

Bloodlust. If you begin your turn with no more than half of your maximum hit points, you must succeed on a DC 8 Wisdom saving throw or move directly towards the nearest creature to you and use the Attack action against that creature. You can choose whether or not to use your Extra Attack feature for this frenzied attack. If there is more than one possible target, roll to randomly determine the target. You then regain control for the remainder of your turn.

If you are under an effect that prevents you from concentrating (like the barbarian’s Rage feature), you automatically fail this saving throw.
    
    """
    
    name = "Hybrid Transformation"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class StalkerProwess(Feature):
    """At 7th level, your speed increases by 10 feet. You also can add 10 feet to your long jump distance and 3 feet to your high jump distance. In addition, your hybrid form gains the Improved Predatory Strikes feature.

Improved Predatory Strikes. You gain a +1 bonus to attack rolls made with your unarmed strikes. This bonus increases by 1 at 11th level (+2) and 18th level (+3). In addition, when you have an active Crimson Rite while in your hybrid form, your unarmed strikes are considered magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.
    
    """
    
    name = "Stalker Prowess"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class AdvancedTrasformation(Feature):
    """Starting at 11th level, you learn to unleash and control more of the beast within. You can use your Hybrid Transformation feature twice, regaining all expended uses when you finish a short or long rest. In addition, your hybrid form gains the Lycan Regeneration feature.

Lycan Regeneration. At the start of each of your turns, before you roll for bloodlust, you regain hit points equal to 1 + your Constitution modifier (minimum of one) if you have at least 1 hit point and no more than half of your hit points left.
    
    """
    
    name = "Advanced Transformation"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class BrandOfTheVoracious(Feature):
    """At 15th level, you have advantage on your Wisdom saving throws to maintain control of your bloodlust in hybrid form. In addition, your Brand of Castigation now binds your foe to your hunter’s thirst for savagery. While in your hybrid form, your attacks have advantage against a creature branded by you.
    
    """
    
    name = "Brand of the Voracious"
    source = "Blood Hunter (Order of the Lycan)"
    
    
class HybridTrasformationMastery(Feature):
    """At 18th level, you have wrestled your inner predator and mastered it. You can use your Hybrid Transformation feature an unlimited number of times, and your hybrid form can now last indefinitely.

You also gain the Blood Curse of the Howl for your Blood Maledict feature. This does not count against your number of blood curses known.
    
    """
    
    name = "Hybrid Transformation Mastery"
    source = "Blood Hunter (Order of the Lycan)"
    

#Order of the Mutant
class Formulas(Feature):
    """You begin to uncover forbidden alchemical formulas that temporarily alter your mental and physical abilities.

Beginning at 3rd level, you choose to learn four mutagen formulas. Your formula options are detailed at the end of this order description. You gain an additional formula at 7th level, 11th level, 15th level, and 18th level.

Additionally, when you gain a new mutagen formula, you can choose one of the formulas you already know and replace it with a new mutagen formula.
    
    """
    
    name = "Formulas"
    source = "Blood Hunter (Order of the Mutant)"
    
    
class Mutagencraft(Feature):
    """At 3rd level, you can concoct a single mutagen when you finish a short or long rest. Starting at 7th level, the number of mutagens you can create when you finish a rest increases to two, and at 15th level, you can now create three mutagens.

As a bonus action you can consume a single mutagen, and the effects and side effects last until you finish a short or long rest, unless otherwise specified. While one or more mutagens are affecting you, you can use an action to focus and flush the toxins from your system, ending the effects and side effects of all mutagens.

Mutagens are designed for your biology and have no effect on other creatures. They are also unstable by nature, losing their potency over time and becoming inert if not used before you finish your next short or long rest.
    
    """
    
    name = "Mutagencraft"
    source = "Blood Hunter (Order of the Mutant)"
    
    
class StrangeMetabolism(Feature):
    """Beginning at 7th level, your body has begun to adapt to toxins and venoms, ignoring their corroding effects. You gain immunity to poison damage and the poisoned condition.

In addition, you can instill a burst of adrenaline to temporarily resist the negative effects of a mutagen. As a bonus action, you can choose to ignore the side effect of a mutagen affecting you for 1 minute.

Once you use this feature to resist side effects, you can’t do so again until you finish a long rest.
    
    """
    
    name = "Strange Metabolism"
    source = "Blood Hunter (Order of the Mutant)"


class BrandOfAxiom(Feature):
    """At 11th level, your hemocraft has altered your Brand of Castigation to enforce a foe’s true nature. Any illusions disguising or making a creature invisible when you brand them end, and they can’t benefit from such illusions while branded. If a creature branded by you is polymorphed or has changed shape, they must succeed on a Wisdom saving throw or revert to their true form and be stunned until the end of your next turn. Whenever a branded creature attempts to polymorph or change shape, they must succeed on a Wisdom saving throw or the attempt fails, and they are stunned until the end of your next turn.
    
    """
    
    name = "Brand of Axiom"
    source = "Blood Hunter (Order of the Mutant)"
    
    
class BloodCurseOfCorrosion(Feature):
    """Starting at 15th level, your blood curse can wrack a creature’s body with terrible toxins. You gain the Blood Curse of Corrosion for your Blood Maledict feature. This does not count against your number of blood curses known.
    
    """
    
    name = "Blood Curse of Corrosion"
    source = "Blood Hunter (Order of the Mutant)"
    
    
class ExaltedMutation(Feature):
    """At 18th level, your body has adapted to produce your toxins naturally in a moment of need. As a bonus action, you can choose one mutagen currently affecting you to flush from your system and end, then immediately have a mutagen you know the formula for take effect in its place.

You can use this feature a number of times equal to your Intelligence modifier (minimum of 1). You regain all uses of this feature after you finish a long rest.
    
    """
    
    name = "Exalted Mutation"
    source = "Blood Hunter (Order of the Mutant)"
    
    
#Formulas
class Formulas(Feature):
    """
    A generic Formula. Add details in features/bloodhunter.py
    """

    name = "Unnamed rite"
    source = "BloodHunter (Crimson Rites)"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if "M" in s.components:
            c = list(s.components)
            c.remove("M")
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self, owner):
        super().__init__(owner)
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)
            
            
class Aether(Formulas):
    """**Prerequisite: 11th level.**
You gain a flying speed of 20 feet for 1 hour.
Side effect. You have disadvantage on Strength and Dexterity ability checks for 1 hour.
    
    """
    
    name = "Aether"
    

class Alluring(Formulas):
    """Your skin and voice become malleable, allowing you to slightly enhance your appearance and presence. You have advantage on Charisma ability checks.
Side effect. You have disadvantage on initiative rolls.
    
    """
    
    name = "Alluring"
    
    
class Celerity(Formulas):
    """Your Dexterity score increases by 3, as does your Dexterity maximum. This bonus increases by 1 at 11th and 18th level.
Side effect. You have disadvantage on Wisdom saving throws.
    
    """
    
    name = "Celerity"
    

class Conversant(Formulas):
    """You gain advantage on Intelligence ability checks.
Side effect. You have disadvantage on Wisdom ability checks.
    
    """
    
    name = "Conversant"
    
    
class Cruelty(Formulas):
    """**Prerequisite: 11th level.**
When you use the Attack action, you can make an additional weapon attack as a bonus action.
Side effect. You have disadvantage on Intelligence, Wisdom, and Charisma saving throws.
    
    """
    
    name = "Cruelty"
    
    
class Deftness(Formulas):
    """You gain advantage on Dexterity ability checks.
Side effect. You have disadvantage on Wisdom ability checks.
    
    """
    
    name = "Deftness"
    
    
class Embers(Formulas):
    """You gain resistance to fire damage.
Side effect. You gain vulnerability to cold damage.
    
    """
    
    name = "Embers"
    
    
class Gelid(Formulas):
    """You gain resistance to cold damage.
Side effect. You gain vulnerability to fire damage.

    """
    
    name = "Gelid"
    
    
class Impermeable(Formulas):
    """You gain resistance to piercing damage.
Side effect. You gain vulnerability to slashing damage.
    
    """
    
    name = "Impermeable"
    
    
class Mobility(Formulas):
    """You gain immunity to the grappled and restrained conditions. At 11th level, you also are immune to the paralyzed condition.
Side effect. You have disadvantage on Strength ability checks.
    
    """
    
    name = "Mobility"
    
    
class Nighteye(Formulas):
    """You gain darkvision for up to 60 feet. If you already have darkvision, this increases its range by 60 additional feet.
Side effect. You gain sunlight sensitivity (detailed in the Dark Elf section of the Player’s Handbook).
    
    """
    
    name = "Nighteye"
    
    
class Percipient(Formulas):
    """You gain advantage on Wisdom ability checks.
Side effect. You have disadvantage on Charisma ability checks.
    
    """
    
    name = "Percipient"
    
    
class Potency(Formulas):
    """Your Strength score increases by 3, as does your Strength maximum. This bonus increases by 1 at 11th and 18th level.
Side effect. You have disadvantage on Dexterity saving throws.
    
    """
    
    name = "Potency"
    
    
class Precision(Formulas):
    """**Prerequisite: 11th level**
Your weapon attacks score a critical hit on a roll of 19-20.
Side effect. You have disadvantage on Strength saving throws.
    
    """
    
    name = "Precision"
    

class Rapidity(Formulas):
    """Your speed increases by 10 feet. At 15th level, your speed increases by 15 feet instead.
Side effect. You have disadvantage on Intelligence ability checks.
    
    """
    
    name = "Rapidity"
    
    
class Reconstruction(Formulas):
    """**Prerequisite: 7th level**
For 1 hour, at the start of each of your turns, you regain hit points equal to your proficiency bonus if you have at least 1 hit point, but no more than half of your hit points.
Side effect. Your speed decreases by 10 ft for 1 hour.
    
    """
    
    name = "Reconstruction"
    
    
class Sagacity(Formulas):
    """Your Intelligence score increases by 3, as does your Intelligence maximum. This bonus increases by 1 at 11th and 18th level.
Side effect. You have disadvantage on Charisma saving throws.
    
    """
    
    name = "Sagacity"
    
    
class Shielded(Formulas):
    """You gain resistance to slashing damage.
Side effect. You gain vulnerability to bludgeoning damage.
    
    """
    
    name = "Shielded"
    
    
class Unbreakable(Formulas):
    """You gain resistance to bludgeoning damage.
Side effect. You gain vulnerability to piercing damage.

    """
    
    name = "Unbreakable"
    
    
class Vermillion(Formulas):
    """You gain an additional use of your Blood Maledict feature.
Side effect. You have disadvantage on death saving throws.
    
    """
    
    name = "Vermillion"
    

#Order of the Profane Soul
class ArchfeyPatron(Feature):
    """When you deal rite damage to a creature, it glows with faint light until the end of your next turn. For the duration, the creature can’t benefit from half cover, three-quarters cover, or being invisible.
    
    """
    
    name = "Archfey Patron"
    source = "Blood Hunter (Order of the Profane Soul)"


class CelestialPatron(Feature):
    """You can expend a use of your Blood Maledict feature as a bonus action to heal one creature that you can see within 60 feet of you. They regain a number of hit points hit points equal to one roll of your hemocraft die + your Intelligence modifier (minimum of +1).
    
    """
    
    name = "Celestial Patron"
    source = "Blood Hunter (Order of the Profane Soul) "
    
    
class FiendPatron(Feature):
    """While using the Rite of the Flame, if you roll a 1 or 2 on your rite damage die, you can reroll the die and choose which roll to use.
    
    """
    
    name = "Fiend Patron"
    source = "Blood Hunter (Order of the Profane Soul)"


class GreatOldOnePatron(Feature):
    """When you score a critical hit against a creature while using the weapon, that creature is frightened of you until the end of your next turn.
    
    """
    
    name = "Great Old One Patron"
    source = "Blood Hunter (Order of the Profane Soul) "


class HexbladePatron(Feature):
    """Whenever you target a creature with a blood curse, your next attack against the cursed creature deals additional damage equal to your proficiency modifier.
    
    """
    
    name = "Hexblade Patron"
    source = "Blood Hunter (Order of the Profane Soul)"


class UndyingPatron(Feature):
    """Whenever you reduce a hostile creature to 0 hit points using a weapon attack, you regain a number of hit points equal to one roll of your hemocraft die.
    
    """
    
    name = "Undying Patron"
    source = "Blood Hunter (Order of the Profane Soul)"


class OtherworldlyPatron(FeatureSelector):
    """When you reach 3rd level, you strike a bargain with an otherworldly being of your choice: the Archfey, the Fiend, or the Great Old One, each detailed in the Player’s Handbook, the Undying within the Sword Coast Adventurer’s Guide, and the Celestial or Hexblade in Xanathar’s Guide to Everything. Your choice augments some of your order features.
    
    """
    
    options = {
    	"Archfey": ArchfeyPatron,
    	"Celestial": CelestialPatron,
    	"Fiend": FiendPatron,
    	"Great Old One": GreatOldOnePatron,
    	"Hexblade": HexbladePatron,
    	"Undying": UndyingPatron,
    }
    name = "Otherworldly Patron (Select One)"
    source = "Blood Hunter (Order of the Profane Soul)"
    

class PactMagic(Feature):
    """When you reach 3rd level, you can augment your combat techniques with the ability to cast spells. See chapter 10 of the PHB for the general rules of spellcasting and chapter 11 of the Player’s Handbook for the Warlock spell list.

Cantrips. You learn two cantrips of your choice from the warlock spell list. You learn an additional warlock cantrip of your choice at 10th level.

Spell Slots. The Profane Soul Spellcasting table shows how many spell slots you have. The table also shows what the level of those slots is; all of your spell slots are the same level. To cast one of your warlock spells of 1st level or higher, you must expend a spell slot. You regain all expended spell slots when you finish a short or long rest.

For example, when you are 8th level, you have two 2nd-level spell slots. To cast the 1st-level spell witch bolt, you must spend one of those slots, and you cast it as a 2nd-level spell.

Spells Known of 1st Level and Higher. At 3rd level, you know two 1st-level spells of your choice from the warlock spell list.

The Spells Known column of the Profane Soul table shows when you learn more warlock spells of your choice of 1st level and higher. A spell you choose must be of a level no higher than what’s shown in the table’s Slot Level column for your level. When you reach 11th level, for example, you learn a new warlock spell, which can be 1st, 2nd, or 3rd level.

Additionally, when you gain a level in this class and order, you can choose one of the warlock spells you know and replace it with another spell from the warlock spell list, which also must be of a level for which you have spell slots.

Spellcasting Ability. Intelligence is your spellcasting ability for your warlock spells, so you use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a warlock spell you cast and when making an attack roll with one.

Spell save DC = 8 + your proficiency bonus + your Intelligence modifier

Spell attack modifier = your proficiency bonus + your Intelligence modifier
    
    """
    
    name = "Pact Magic"
    source = "Blood Hunter (Order of the Profane Soul)"


class RiteFocus(Feature):
    """Beginning at 3rd level, your weapon becomes a core to your pact with your chosen dark patron. While you have an active Crimson Rite, you can use your weapon as a spellcasting focus (found in chapter 5 of the Player’s Handbook) for your warlock spells, and you gain a specific benefit based on your chosen pact (outlined below).
    
    The Archfey

When you deal rite damage to a creature, it glows with faint light until the end of your next turn. For the duration, the creature can’t benefit from half cover, three-quarters cover, or being invisible.

The Celestial

You can expend a use of your Blood Maledict feature as a bonus action to heal one creature that you can see within 60 feet of you. They regain a number of hit points hit points equal to one roll of your hemocraft die + your Intelligence modifier (minimum of +1).

The Fiend

While using the Rite of the Flame, if you roll a 1 or 2 on your rite damage die, you can reroll the die and choose which roll to use.

The Great Old One

When you score a critical hit against a creature while using the weapon, that creature is frightened of you until the end of your next turn.

The Hexblade

Whenever you target a creature with a blood curse, your next attack against the cursed creature deals additional damage equal to your proficiency modifier.

The Undying

Whenever you reduce a hostile creature to 0 hit points using a weapon attack, you regain a number of hit points equal to one roll of your hemocraft die.

    """
    
    name = "Rite Focus"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class MysticFrenzy(Feature):
    """Starting at 7th level, when you use your action to cast a cantrip, you can immediately make one weapon attack as a bonus action.
    
    """
    
    name = "Mystic Frenzy"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class RevealedArcana(Feature):
    """At 7th level, your dark patron grants you the rare use of a dangerous arcane spell based on your pact.
The Archfey

You can cast blur once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Celestial

You can cast lesser restoration once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Fiend

You can cast scorching ray once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Great Old One

You can cast detect thoughts once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Hexblade

You can cast branding smite once using a pact magic spell slot. You can’t do so again until you finish a long rest.

The Undying

You can cast blindness/deafness once using a pact magic spell slot. You can’t do so again until you finish a long rest.
    
    """
    
    name = "Revealed Arcana"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class BrandOfTheSappingScar(Feature):
    """Upon reaching 11th level, your Brand of Castigation feature now digs dark, arcane scars into your target, leaving them vulnerable to your magic. A creature branded by you has disadvantage on their saving throws against your warlock spells.
    
    """
    
    name = "Brand of the Sapping Scar"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class UnsealedArcana(Feature):
    """At 15th level, your patron grants you the rare use of an additional arcane spell based on your pact.
The Archfey

You can cast slow once without expending a spell slot. You can’t do so again until you finish a long rest.

The Celestial

You can cast revivify once without expending a spell slot. You can’t do so again until you finish a long rest.

The Fiend

You can cast fireball once without expending a spell slot. You can’t do so again until you finish a long rest.

The Great Old One

You can cast haste once without expending a spell slot. You can’t do so again until you finish a long rest.

The Hexblade

You can cast blink once without expending a spell slot. You can’t do so again until you finish a long rest.

The Undying

You can cast bestow curse once without expending a spell slot. You can’t do so again until you finish a long rest.
    
    """
    
    name = "Unsealed Arcana"
    source = "Blood Hunter (Order of the Profane Soul)"
    
    
class BloodCurseOfTheSouleater(Feature):
    """Starting at 18th level, you’ve learned to siphon the soul from your fallen prey. You gain the Blood Curse of the Souleater for your Blood Maledict feature. This does not count against your number of blood curses known.
    
    """
    
    name = "Blood Curse of the Souleater"
    source = "Blood Hunter (Order of the Profane Soul)"

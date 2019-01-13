"""A collection of monsters. Also useful for building a list of wild
shape forms."""


from .stats import Ability


class Monster():
    """A monster that may be encountered when adventuring."""
    name = "Generic Monster"
    description = ""
    challenge_rating = 0
    armor_class = 0
    skills = "Perception +3, Stealth +4"
    senses = ""
    languages = ""
    strength = Ability()
    dexterity = Ability()
    constitution = Ability()
    intelligence = Ability()
    wisdom = Ability()
    charisma = Ability()
    speed = 30
    swim_speed = 0
    fly_speed = 0
    hp_max = 10
    hit_dice = '1d6'
    
    @property
    def is_beast(self):
        is_beast = 'beast' in self.description.lower()
        return is_beast


class Ankylosaurus(Monster):
    """Thick armor plating covers the body of the plant-eating dinosaur
    ankylosaurus, which defends itself against predators with a
    knobbed tail that delivers a devastating strike.
    
    **Tail:** *Melee Weapon Attack:* +7 to hit, reach 10 ft., one
    target. *Hit:* 18 (4d6+4) bludgeoning damage. If the target is a
    creature, it must succeed on a DC 14 Strength saving throw or be
    knocked prone.
    
    """
    name = "Ankylosaurus"
    description = "Huge beast, unaligned"
    challenge_rating = 3
    armor_class = 15
    skills = ""
    senses = "Passive perception 11"
    strength = Ability(19)
    dexterity = Ability(11)
    constitution = Ability(15)
    intelligence = Ability(2)
    wisdom = Ability(12)
    charisma = Ability(5)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    hp_max = 68
    hit_dice = '8d12+16'


class Ape(Monster):
    """**Multiattack:** The ape makes two fist attacks.
    
    **Fist:** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one
    target. *Hit:* 6 (1d6+3) bludgeoning damage.
    
    **Rock:** *Ranged Weapon Attack:* +5 to hit, range 25/50 ft., one
    target. *Hit:* 6 (1d6+3) bludgeoning damage.
    
    """
    name = "Ape"
    description = "Medium beast, unaligned"
    challenge_rating = 1 / 2
    armor_class = 12
    skills = "Athletics +5, Perception +3"
    senses = "Passive perception 13"
    strength = Ability(16)
    dexterity = Ability(14)
    constitution = Ability(14)
    intelligence = Ability(6)
    wisdom = Ability(12)
    charisma = Ability(7)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    hp_max = 19
    hit_dice = '3d8+6'


class Crocodile(Monster):
    """**Hold Breath:** The crocodile can hold its breath for 15 minutes.
    
    **Bite:** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one
      creature. *Hit:* 7 (1d10+2) piercing damage, and the target is
      Grappled (escape DC 12). Until this grapple ends, the target is
      Restrained, and the crocodile can't bite another target.
    
    """
    name = "Crocodile"
    description = "Large beast, unaligned"
    challenge_rating = 1/2
    armor_class = 12
    skills = "Stealth +2"
    senses = "Passive perception 10"
    strength = Ability(15)
    dexterity = Ability(10)
    constitution = Ability(13)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(5)
    speed = 30
    swim_speed = 30
    fly_speed = 0
    hp_max = 19
    hit_dice = '3d10+3'

class GiantEagle(Monster):
    """A giant eagle is a noble creature that speaks its own language and
    understands Speech in the Common tongue. A mated pair of giant
    eagles typically has up to four eggs or young in their nest (treat
    the young as normal eagles).
    
    **Keen Sight:** The eagle has advantage on Wisdom (Perception)
      checks that rely on sight.
    
    **Multiattack:** The eagle makes two attacks: one with its beak
      and one with its talons.
    
    **Beak:** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one
      target. *Hit:* 6 (1d6 + 3) piercing damage.
    
    **Talons:** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one
      target. *Hit:* 10 (2d6 + 3) slashing damage.
    
    """
    name = "Giant eagle"
    description = "Large beast, neutral good"
    challenge_rating = 1
    armor_class = 13
    skills = "Perception +4"
    senses = "Passive perception 14"
    languages = "Giant Eagle, understands common and Auran but can't speak."
    strength = Ability(16)
    dexterity = Ability(17)
    constitution = Ability(13)
    intelligence = Ability(8)
    wisdom = Ability(14)
    charisma = Ability(10)
    speed = 10
    swim_speed = 0
    fly_speed = 80
    hp_max = 26
    hit_dice = '4d10+4'


class Spider(Monster):
    """**Spider Climb:** The spider can climb difficult surfaces,
    including upside down on ceilings, without needing to make an
    ability check.
    
    **Web Sense:** While in contact with a web, the spider knows the
    exact location of any other creature in contact with the same web.
    
    **Web Walker:** The spider ignores Movement restrictions caused by
    webbing.
    
    **Bite:** Melee Weapon Attack: +4 to hit, reach 5 ft., one
    creature. Hit: 1 piercing damage, and the target must succeed on a
    DC 9 Constitution saving throw or take 2 (1d4) poison damage.
    
    """
    name = "Spider"
    description = "Tiny beast, unaligned"
    challenge_rating = 0
    armor_class = 12
    skills = "Stealth +4"
    senses = "Darkvision 30 Ft., passive Perception 12"
    strength = Ability(2)
    dexterity = Ability(14)
    constitution = Ability(8)
    intelligence = Ability(1)
    wisdom = Ability(10)
    charisma = Ability(2)
    speed = 20
    hp_max = 1
    hit_dice = '1d4-1'


class SwarmOfRats(Monster):
    """**Keen Smell:** The swarm has advantage on Wisdom (Perception)
    checks that rely on smell.
    
    **Swarm:** The swarm can occupy another creature's space and vice
      versa, and the swarm can move through any opening large enough
      for a Tiny rat. The swarm can't regain Hit Points or gain
      Temporary Hit Points.
    
    **Bites:** Melee Weapon Attack: +2 to hit, reach 0 ft., one target
      in the swarm's space. Hit: 7 (2d6) piercing damage, or 3 (1d6)
      piercing damage if the swarm has half of its Hit Points or
      fewer.
    
    """
    name = "Swarm of Rats"
    description = "Medium swarm of tiny beasts, unaligned"
    challenge_rating = 1/4
    armor_class = 10
    skills = ""
    senses = "Darkvision 30 Ft., passive Perception 10"
    damage_resistance = "Bludgeoning, Piercing, Slashing"
    condition_immunities = ("Charmed, Frightened, Grappled, Paralyzed, "
                            "Petrified, Prone, Restrained, Stunned")
    strength = Ability(9)
    dexterity = Ability(11)
    constitution = Ability(9)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(3)
    speed = 30
    hp_max = 24
    hit_dice = '7d8-7'


class Rat(Monster):
    """**Keen Smell:** The rat has advantage on Wisdom (Perception) checks
    that rely on smell.
    
    **Bite:** Melee Weapon Attack: +0 to hit, reach 5 ft., one
    target. Hit: 1 piercing damage.
    
    """
    name = "Rat"
    description = "Tiny beast, unaligned"
    challenge_rating = 0
    armor_class = 10
    skills = ""
    senses = "Darkvision 30 Ft., passive Perception 10"
    strength = Ability(2)
    dexterity = Ability(11)
    constitution = Ability(9)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(4)
    speed = 20
    hp_max = 1
    hit_dice = '1d4-2'


class Wolf(Monster):
    """**Keen Hearing and Smell.** The wolf has advantage on Wisdom
    (Perception) checks that rely on hearing or smell.
    
    **Pack Tactics.** The wolf has advantage on an attack roll against a
    creature if at least one of the wolf's allies is within 5 ft. of
    the creature and the ally isn't incapacitated.  Actions
    
    **Bite.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one
    target. *Hit:* (2d4+2) piercing damage. If the target is a
    creature, it must succeed on a DC 11 Strength saving throw or be
    knocked prone
    
    """
    name = "Wolf"
    description = "Medium beast, unaligned"
    challenge_rating = 1/4
    armor_class = 13
    skills = "Perception +3, Stealth +4"
    senses = "Passive Perception 13"
    strength = Ability(12)
    dexterity = Ability(15)
    constitution = Ability(12)
    intelligence = Ability(6)
    wisdom = Ability(12)
    charisma = Ability(6)
    speed = 40
    hp_max = 11
    hit_dice = '2d8+2'

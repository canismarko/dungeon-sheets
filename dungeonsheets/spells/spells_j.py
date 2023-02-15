from dungeonsheets.spells.spells import Spell


class JimsGlowingCoin(Spell):
	"""Of the many tactics employed by master magician and renowned 
	adventurer Jim Darkmagic, the old glowing coin trick is a time-honored 
	classic. When you cast the spell, you hurl the coin that is the spell's 
	material component to any spot within range. The coin lights up as if 
	under the effect of a light spell. Each creature of your choice that 
	you can see within 30 feet of the coin must succeed on a Wisdom saving 
	throw or be distracted for the duration. While distracted, a creature 
	has disadvantage on Wisdom (Perception) checks and initiative rolls.
	
	"""

	name = "Jims Glowing Coin"
	level = "2"
	casting_time = "Action"
	casting_range = "60 feet"
	components = "S, M, R"
	materials = "a coin
2 gp"
	duration = "1 minute"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Wizard")
class JimsMagicMissile(Spell):
	"""“Jim's magic missile is an ancient and powerful spell, as well as 
	being the name of my band in Wizard Academy.”— Jim DarkmagicAny 
	apprentice wizard can cast a boring old magic missile. Sure, it always 
	strikes its target. Yawn. Do away with the drudgery of your 
	grandfather's magic with this improved version of the spell, as used by 
	Jim Darkmagic!You create three twisting, whistling, hypoallergenic, 
	gluten-free darts of magical force. Each dart targets a creature of 
	your choice that you can see within range. Make a ranged spell attack 
	for each missile. On a hit, a missile deals 2d4 force damage to its 
	target.If the attack roll scores a critical hit, the target of that 
	missile takes 5d4 force damage instead of you rolling damage twice for 
	a critical hit. If the attack roll for any missile is a 1, all missiles 
	miss their targets and blow up in your face, dealing 1 force damage per 
	missile to you.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	2nd level or higher, the spell creates one more dart, and the royalty 
	component increases by 1 gp, for each slot level above 1st."""

	name = "Jims Magic Missile"
	level = "1"
	casting_time = "Action"
	casting_range = "120 feet"
	components = "V, S, R"
	materials = "1 gp"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Wizard")
class Jump(Spell):
	"""You touch a creature. The creature's jump distance is tripled until 
	the spell ends.
	
	"""

	name = "Jump"
	level = "1"
	casting_time = "Action"
	casting_range = "Touch"
	components = "V, S, M"
	materials = "a grasshopper's hind leg"
	duration = "1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Druid", "Ranger", "Sorcerer", "Wizard")

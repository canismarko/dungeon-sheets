from dungeonsheets.spells.spells import Spell


class UnearthlyChorus(Spell):
	"""Music of a style you choose fills the air around you in a 30-foot 
	radius. The music spreads around corners and can be heard from up to 
	100 feet away. The music moves with you, centered on you for the 
	duration.Until the spell ends, you make Charisma (Performance) checks 
	with advantage. In addition, you can use a bonus action on each of your 
	turns to beguile one creature you choose within 30 feet of you that can 
	see you and hear the music. The creature must make a Charisma saving 
	throw. If you or your companions are attacking it, the creature 
	automatically succeeds on the saving throw. On a failure, the creature 
	becomes friendly to you for as long as it can hear the music and for 1 
	hour thereafter. You make Charisma (Deception) checks and Charisma 
	(Persuasion) checks against creatures made friendly by this spell with 
	advantage.
	
	"""

	name = "Unearthly Chorus"
	level = 1
	casting_time = "Action"
	casting_range = "Self (30-foot radius)"
	components = ("V")
	materials = ""
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Illusion"
	classes = ("Bard")
class UnseenServant(Spell):
	"""This spell creates an invisible, mindless, shapeless, Medium force 
	that performs simple tasks at your command until the spell ends. The 
	servant springs into existence in an unoccupied space on the ground 
	within range. It has AC 10, 1 hit point, and a Strength of 2, and it 
	can't attack. If it drops to 0 hit points, the spell ends.Once on each 
	of your turns as a bonus action, you can mentally command the servant 
	to move up to 15 feet and interact with an object. The servant can 
	perform simple tasks that a human servant could do, such as fetching 
	things, cleaning, mending, folding clothes, lighting fires, serving 
	food, and pouring wine. Once you give the command, the servant performs 
	the task to the best of its ability until it completes the task, then 
	waits for your next command.If you command the servant to perform a 
	task that would move it more than 60 feet away from you, the spell ends.
	
	"""

	name = "Unseen Servant"
	level = 1
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a piece of string and a bit of wood;"
	duration = "1 hour"
	ritual = True
	magic_school = "Conjuration"
	classes = ("Bard", "Warlock", "Wizard")

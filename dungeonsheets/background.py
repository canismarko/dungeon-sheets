class Background():
    name = "Generic background"
    skill_proficiencies = ()
    languages = ()


class Acolyte(Background):
    name = "Acolyte"
    skill_proficiencies = ('insight', 'religion')
    languages = ("[choose one]", "[choose one]")


class Charlatan(Background):
    name = "Charlatan"
    skill_proficiencies = ('deception', 'sleight of hand')


class Criminal(Background):
    name = "Criminal"
    skill_proficiencies = ('deception', 'stealth')


class Spy(Criminal):
    name = "Spy"


class Entertainer(Background):
    name = "Entertainer"
    skill_proficiencies = ('acrobatic', 'performance')


class Gladiator(Entertainer):
    name = "Gladiator"


class FolkHero(Background):
    name = "Folk Hero"
    skill_proficiencies = ('animal handling', 'survival')


class GuildArtisan(Background):
    name = "Guild Artisan"
    skill_proficiencies = ('insight', 'persuasion')
    languages = ("[choose one]", "[choose one]")


class GuildMerchant(GuildArtisan):
    name = "Guild Merchant"


class Hermit(Background):
    name = "Hermit"
    skill_proficiencies = ("medicine", "religion")
    languages = ("[choose one]")


class Noble(Background):
    name = "Noble"
    skill_proficiencies = ("history", 'persuasion')
    languages = ("[choose one]", )


class Knight(Noble):
    name = "Knight"


class Outlander(Background):
    name = "Outlander"
    skill_proficiencies = ('athletics', 'survival')
    languages = ("[choose one]", )


class Sage(Background):
    name = "Sage"
    skill_proficiencies = ('arcana', 'history')
    languages = ("[choose one]", '[choose one]')


class Sailor(Background):
    name = "Sailor"
    skill_proficiencies = ('athletics', 'perception')


class Pirate(Sailor):
    name = "Pirate"


class Soldier(Background):
    name = "Soldier"
    skill_proficiencies = ('athletics', 'intimidation')


class Urchin(Background):
    name = "Urchin"
    skill_proficiencies = ('sleight of hand', 'stealth')

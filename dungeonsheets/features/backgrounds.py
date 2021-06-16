from dungeonsheets.features.features import Feature


class ShelterOfTheFaithful(Feature):
    """As an acolyte, you command the respect of those who share your faith, and
    you can perform the religious ceremonies of your deity. You and your
    adventuring companions can expect to receive free healing and care at a
    temple, shrine, or other established presence of your faith, though you
    must provide any material components needed for spells. Those who share
    your religion will support you (but only you) at a modest lifestyle.

    You might also have ties to a specific temple dedicated to your chosen
    deity or pantheon, and you have a residence there. This could be the temple
    where you used to serve, if you remain on good terms with it, or a temple
    where you have found a new home. While near your temple, you can call upon
    the priests for assistance, provided the assistance you ask for is not
    hazardous and you remain in good standing with your temple.

    """

    name = "Shelter of the Faithful"
    source = "Background (Acolyte)"


class FalseIdentity(Feature):
    """You have created a second identity that includes documentation, established
    acquaintances, and disguises that allow you to assume that
    persona. Additionally, you can forge documents including official papers
    and personal letters, as long as you have seen an example of the kind of
    document or the handwriting you are trying to copy.

    """

    name = "False Identity"
    source = "Background (Charlattan)"


class CriminalContact(Feature):
    """You have a reliable and trustworthy contact who acts as your liaison to a
    network of other criminals. You know how to get messages to and from your
    contact, even over great distances; specifically, you know the local
    messengers, corrupt caravan masters, and seedy sailors who can deliver
    messages for you.

    """

    name = "Criminal Contact"
    source = "Background (Criminal)"


class ByPopularDemand(Feature):
    """You can always find a place to perform, usually in an inn or tavern but
    possibly with a circus, at a theater, or even in a noble's court. At such a
    place, you receive free lodging and food of a modest or comfortable
    standard (depending on the quality of the establishment), as long as you
    perform each night. In addition, your performance makes you something of a
    local figure. When strangers recognize you in a town where you have
    performed, they typically take a liking to you.

    """

    name = "By Popular Demand"
    source = "Background (Entertainer)"


class RusticHospitality(Feature):
    """Since you come from the ranks of the common folk, you fit in among them
    with ease. You can find a place to hide, rest, or recuperate among other
    commoners, unless you have shown yourself to be a danger to them. They will
    shield you from the law or anyone else searching for you, though they will
    not risk their lives for you.

    """

    name = "Rustic Hospitality"
    source = "Background (Folk Hero)"


class GuildMembership(Feature):
    """As an established and respected member of a guild, you can rely on certain
    benefits that membership provides. Your fellow guild members will provide
    you with lodging and food if necessary, and pay for your funeral if
    needed. In some cities and towns, a guildhall offers a central place to
    meet other members of your profession, which can be a good place to meet
    potential patrons, allies, or hirelings.

    Guilds often wield tremendous political power. If you are accused of a
    crime, your guild will support you if a good case can be made for your
    innocence or the crime is justifiable. You can also gain access to powerful
    political figures through the guild, if you are a member in good
    standing. Such connections might require the donation of money or magic
    items to the guild's coffers.

    You must pay dues of 5 gp per month to the guild. If you miss payments, you
    must make up back dues to remain in the guild's good graces.

    """

    name = "Guild Membership"
    source = "Background (Guild Artisan)"


class Discovery(Feature):
    """The quiet seclusion of your extended hermitage gave you access to a unique
    and powerful discovery. The exact nature of this revelation depends on the
    nature of your seclusion. It might be a great truth about the cosmos, the
    deities, the powerful beings of the outer planes, or the forces of
    nature. It could be a site that no one else has ever seen. You might have
    uncovered a fact that has long been forgotten, or unearthed some relic of
    the past that could rewrite history. It might be information that would be
    damaging to the people who or consigned you to exile, and hence the reason
    for your return to society.

    Work with your DM to determine the details of
    your discovery and its impact on the campaign.

    """

    name = "Discovery"
    source = "Background (Hermit)"


class PositionOfPrivilege(Feature):
    """Thanks to your noble birth, people are inclined to think the best of
    you. You are welcome in high society, and people assume you have the right
    to be wherever you are. The common folk make every effort to accommodate
    you and avoid your displeasure, and other people of high birth treat you as
    a member of the same social sphere. You can secure an audience with a local
    noble if you need to.

    """

    name = "Position of Privilege"
    source = "Background (Noble)"


class Wanderer(Feature):
    """You have an excellent memory for maps and geography, and you can always
    recall the general layout of terrain, settlements, and other features
    around you. In addition, you can find food and fresh water for yourself and
    up to five other people each day, provided that the land offers berries,
    small game, water, and so forth.

    """

    name = "Wanderer"
    source = "Background (Outlander)"


class Researcher(Feature):
    """When you attempt to learn or recall a piece of lore, if you do not know
    that information, you often know where and from whom you can obtain
    it. Usually, this information comes from a library, scriptorium,
    university, or a sage or other learned person or creature. Your DM might
    rule that the knowledge you seek is secreted away in an almost inaccessible
    place, or that it simply cannot be found. Unearthing the deepest secrets of
    the multiverse can require an adventure or even a whole campaign.
    """

    name = "Researcher"
    source = "Background (Sage)"


class ShipsPassage(Feature):
    """When you need to, you can secure free passage on a sailing ship for
    yourself and your adventuring companions. You might sail on the ship you
    served on, or another ship you have good relations with (perhaps one
    captained by a former crewmate). Because you're calling in a favor, you
    can't be certain of a schedule or route that will meet your every
    need. Your Dungeon Master will determine how long it takes to get where you
    need to go. In return for your free passage, you and your companions are
    expected to assist the crew during the voyage

    """

    name = "Ship's Passage"
    source = "Background (Sailor)"


class MilitaryRank(Feature):
    """You have a military rank from your career as a soldier. Soldiers loyal to
    your former military organization still recognize your authority and
    influence, and they defer to you if they are of a lower rank. You can
    invoke your rank to exert influence over other soldiers and requisition
    simple equipment or horses for temporary use. You can also usually gain
    access to friendly military encampments and fortresses where your rank is
    recognized.

    """

    name = "Military Rank"
    source = "Background (Soldier)"


class CitySecrets(Feature):
    """You know the secret patterns and flow to cities and can find passages
    through the urban sprawl that others would miss. When you are not in
    combat, you (and companions you lead) can travel between any two locations
    in the city twice as fast as your speed would normally allow.

    """

    name = "City Secrets"
    source = "Background (Urchin)"


# Swords Coast Adventurer's Guide
class AllEyesOnYou(Feature):
    """Your accent, mannerisms, figures of speech, and perhaps even your
    appearance all mark you as foreign. Curious glances are directed your way
    wherever you go, which can be a nuisance, but you also gain the friendly
    interest of scholars and others intrigued by far-off lands, to say nothing
    of everyday folk who are eager to hear stories of your homeland.

    You can parley this attention into access to people and places you might
    not otherwise have, for you and your traveling companions. Noble lords,
    scholars, and merchant princes, to name a few, might be interested in
    hearing about your distant homeland and people.

    """

    name = "All Eyes on You"
    source = "Background (Far Traveler)"


class EarToTheGround(Feature):
    """You are in frequent contact with people in the segment of society that your
    chosen quarries move through. These people might be associated with the
    criminal underworld, the rough-and-tumble folk of the streets, or members
    of high society. This connection comes in the form of a contact in any city
    you visit, a person who provides information about the people and places of
    the local area.

    """

    name = "Ear to the Ground"
    source = "Background (Urban Bounty Hunter)"


class WatchersEye(Feature):
    """Your experience in enforcing the law, and dealing with lawbreakers, gives
    you a feel for local laws and criminals. You can easily find the local
    outpost of the watch or a simila r organization, and just as easily pick
    out the dens of criminal activity in a community, although you're more
    likely to be welcome in the former locations rather than the latter.

    """

    name = "Watcher's Eye"
    source = "Background (City Watch)"


class RespectOfTheStoutFolk(Feature):
    """As well respected as clan crafters are among outsiders, no one esteems them
    quite so highly as dwarves do. You always have free room and board in any
    place where shield dwarves or gold dwarves dwell, and the individuals in
    such a settlement might vie among themselves to determine who can offer you
    (and possibly your compatriots) the finest accommodations and assistance.

    """

    name = "Respect of the Stout Folk"
    source = "Background (Clan Crafter)"


class LibraryAccess(Feature):
    """Though others must often endure extensive interviews and significant fees to
    gain access to even the most common archives in your library, you have free
    and easy access to the majority of the library, though it might also have
    repositories of lore that are too valuable, magical, or secret to permit
    anyone immediate access.

    You have a working knowledge of your cloister's personnel and bureaucracy,
    and you know how to navigate those connections with some ease.

    Additionally, you are likely to gain preferential treatment at other
    libraries across the Realms, as professional courtesy shown to a fellow
    scholar.

    """

    name = "Library Access"
    source = "Background (Cloistered Scholar)"


class CourtFunctionary(Feature):
    """Your knowledge of how bureaucracies function lets you gain access to the
    records and inner workings of any noble court or government you
    encounter. You know who the movers and shakers are, whom to go to for the
    favors you seek, and what the current intrigues of interest in the group
    are.

    """

    name = "Court Functionary"
    source = "Background (Courtier)"


class SafeHaven(Feature):
    """As a faction agent, you have access to a secret network of supporters and
    operatives who can provide assistance on your adventures. You know a set
    of secret signs and passwords you can use to identify such operatives , who
    can provide you with access to a hidden safe house, free room and board, or
    assistance in finding information. These agents never risk their lives
    for you or risk revealing their true identities.

    """

    name = "Save Haven"
    source = "Background (Faction Agent)"


class Inheritance(Feature):
    """Choose or randomly determine your inheritance from among the possibilities
    in the table in SCAG. Work with your Dungeon Master to come up with
    details: Why is your inheritance so important, and what is its full story?
    You might prefer for the DM to invent these details as part of the game,
    allowing you to learn more about your inheritance as your character does.

    The Dungeon Master is free to use your inheritance as a story hook, sending
    you on quests to learn more about its history or true nature, or
    confronting you with foes who want to claim it for themselves or prevent
    you from learning what you seek. The DM also determines the properties of
    your inheritance and how they figure into the item's history and
    importance. For instance, the object might be a minor magic item, or one
    that begins with a modest ability and increases in potency with the passage
    of time. Or, the true nature of your inheritance might not be apparent at
    first and is revealed only when certain conditions are met.

    When you begin your adventuring career, you can decide whether to tell your
    companions about your inheritance right away. Rather than attracting
    attention to yourself, you might want to keep your inheritance a secret
    until you learn more about what it means to you and what it can do for you.

    """

    name = "Inheritance"
    source = "Background (Inheritor)"


class InsideInformant(Feature):
    """You have connections to your previous employer or other groups you
    dealt with during your previous employment. You can communicate
    with your contacts, gaining information at the DM's discretion.

    """

    name = "Inside Informant"
    source = "Background (Rival Intern)"


class KnightlyRegard(Feature):
    """You receive shelter and succor from members of your knightly order and those
    who are sympathetic to its aims. If your order is a religious one, you can
    gain aid from temples and other religious communities of your
    deity. Knights of civic orders can get help from the community- whether a
    lone settlement or a great nation- that they serve, and knights of
    philosophical orders can find help from those they have aided in pursuit of
    their ideals , and those who share those ideals.

    This help comes in the form of shelter and meals, and healing when
    appropriate, as well as occasionally risky assistance, such as a band of
    local citizens rallying to aid a sorely pressed knight in a fight , or
    those who support the order helping to smuggle a knight out of town when
    he or she is being hunted unjustly.

    """

    name = "Knightly Regard"
    source = "Background (Knight of the Order)"


class MercenaryLife(Feature):
    """You know the mercenary life as only someone who has experienced it can. You
    are able to identify mercenary companies by their emblems, and you know a
    little about any such company, including the names and reputations of its
    commanders and leaders, and who has hired them recently. You can find the
    taverns and festhalls where mercenaries abide in any area, as long as you
    speak the language. You can find mercenary work between adventures
    sufficient to maintain a comfortable lifestyle (see "Practicing a
    Profession" under "Downtime Activities" in chapter 8 of the Player's
    Handbook).

    """

    name = "Mercenary Life"
    source = "Background (Mercenary Veteran)"


class UthgardtHeritage(Feature):
    """You have an excellent knowledge of not only your tribe's territory, but also
    the terrain and natural resources of the rest of the North. You are
    familiar enough with any wilderness area that you find twice as much food
    and water as you normally would when you forage there.

    Additionally, you can call upon the hospitality of your people, and those
    folk allied with your tribe, often including members of druid circles,
    tribes of nomadic elves, the Harpers, and the priesthoods devoted to the
    gods of the First Circle.

    """

    name = "Uthgardt Heritage"
    source = "Background (Uthgardt Tribe Member)"


class KeptInStyle(Feature):
    """While you are in Waterdeep or elsewhere in the North your house sees to
    your everyday needs. Your name and signet are sufficient to cover most of
    your expenses; the inns, taverns, and festhalls you frequent are glad to
    record your debt and send an accounting to your family's estate in Waterdeep
    to settle what you owe.

    This advantage enables you to live a comfortable lifestyle without having
    to pay 2 gp a day for it, or reduces the cost of a wealthy or aristocratic
    lifestyle by that amount. You may not maintain a less affluent lifestyle
    and use the difference as income-the benefit is a line of credit, not an
    actual monetary reward.

    """

    name = "Kept in Style"
    source = "Background (Waterdhavian Noble)"

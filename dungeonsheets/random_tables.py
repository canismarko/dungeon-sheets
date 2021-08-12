from abc import ABCMeta
from typing import Sequence

from dungeonsheets.content import Content
from dungeonsheets.content_registry import default_content_registry


default_content_registry.add_module(__name__)


class SubtableFactory(ABCMeta):
    """Meta class to append subtables to the docstring of a RandomTable..
    
    For classes using this metaclass, the *subtables* attribute, if
    present, should be a list of subtables that are to be
    included. For each entry on that list, it will first be resolved
    into a RandomTable class, if appropriate, then its docstring will
    be added to the docstring of the calling class.
    
    """
    def __init__(self, name, bases, attrs):
        # Resolve subtables to RandomTable classes
        for idx, subtable in enumerate(self.subtables):
            TheTable = self._resolve_mechanic(subtable, SuperClass=RandomTable)
            self.subtables[idx] = TheTable
        # Append docstrings for subtables
        docstring = self.__doc__ if self.__doc__ is not None else ""
        for table in self.subtables:
            docstring += f"\n\n**{table.name}**\n\n{table.__doc__}\n"
        self.__doc__ = docstring


class RandomTable(Content, metaclass=SubtableFactory):
    """A generic table for rolling treasure, monsters, etc.

    Additional tables can be included by using the *subtables*
    attribute. A use case for this is to create a table for rolling
    random treasure, which may include subtables for gems, art, magic
    items, etc. By including these as subtables, each subtable could
    be included by itself if the verbosity of the full *Treasure*
    table is not needed.

    Attributes
    ==========
    subtables
      A sequence of other random tables that will be included in this
      table.
    
    """
    name = "Generic Random Table"
    subtables: Sequence = []


class ConjureAnimals(RandomTable):
    """
    +-----+-----------------------------------------------+
    | 1d4 | Number of Beasts                              |
    +=====+===============================================+
    | 1   | One beast of challenge rating 2               |
    +-----+-----------------------------------------------+
    | 2   | Two beasts of challenge rating 1              |
    +-----+-----------------------------------------------+
    | 3   | Four beasts of challenge rating 1/2           |
    +-----+-----------------------------------------------+
    | 4   | Eight beasts of challenge rating 1/4 or lower |
    +-----+-----------------------------------------------+
    
    +-------+---------------------------+
    | 1d20  | CR2 Beasts                |
    +=======+===========================+
    | 1-2   | Allosaurus                |
    +-------+---------------------------+
    | 3-4   | Giant Boar                |
    +-------+---------------------------+
    | 5-6   | Giant Constrictor Snake   |
    +-------+---------------------------+
    | 7-8   | Giant Elk                 |
    +-------+---------------------------+
    | 9-10  | Hunter Shark              |
    +-------+---------------------------+
    | 11    | Plesiosaurus              |
    +-------+---------------------------+
    | 12-13 | Polar Bear                |
    +-------+---------------------------+
    | 14-15 | Rhinoceros                |
    +-------+---------------------------+
    | 16-17 | Saber-toothed Tiger       |
    +-------+---------------------------+
    | 18-19 | Swarm of Poisonous Snakes |
    +-------+---------------------------+
    | 20    | Roll on CR 1 Beast Table  |
    +-------+---------------------------+
    
    +------+----------------------------+
    | 1d12 | Challenge Rating 1 Beasts  |
    +======+============================+
    | 1    | Brown Bear                 |
    +------+----------------------------+
    | 2    | Dire Wolf                  |
    +------+----------------------------+
    | 3    | Fire Snake                 |
    +------+----------------------------+
    | 4    | Giant Eagle                |
    +------+----------------------------+
    | 5    | Giant Hyena                |
    +------+----------------------------+
    | 6    | Giant Octopus              |
    +------+----------------------------+
    | 7    | Giant Spider               |
    +------+----------------------------+
    | 8    | Giant Toad                 |
    +------+----------------------------+
    | 9    | Giant Vulture              |
    +------+----------------------------+
    | 10   | Lion                       |
    +------+----------------------------+
    | 11   | Tiger                      |
    +------+----------------------------+
    | 12   | Roll on CR 1/2 Beast Table |
    +------+----------------------------+
    
    +-------+---------------------------------+
    | 1d20  | Challenge Rating 1/2 Beasts     |
    +=======+=================================+
    | 1-2   | Ape                             |
    +-------+---------------------------------+
    | 3-4   | Black Bear                      |
    +-------+---------------------------------+
    | 5-6   | Crocodile                       |
    +-------+---------------------------------+
    | 7-8   | Giant Goat                      |
    +-------+---------------------------------+
    | 9-10  | Giant Sea Horse                 |
    +-------+---------------------------------+
    | 11-12 | Giant Wasp                      |
    +-------+---------------------------------+
    | 13-14 | Reef Shark                      |
    +-------+---------------------------------+
    | 15-16 | Swarm of Insects (below)        |
    +-------+---------------------------------+
    | 17-18 | Warhorse                        |
    +-------+---------------------------------+
    | 19    | Worg                            |
    +-------+---------------------------------+
    | 20    | Roll on Lesser Beast Menu Table |
    +-------+---------------------------------+
    
    +-----+------------------+
    | 1d6 | Swarm of Insects |
    +=====+==================+
    | 1   | Ant              |
    +-----+------------------+
    | 2   | Beatles          |
    +-----+------------------+
    | 3   | Centipedes       |
    +-----+------------------+
    | 4   | Locusts          |
    +-----+------------------+
    | 5   | Spiders          |
    +-----+------------------+
    | 6   | Wasps            |
    +-----+------------------+
    
    +-----+------------------------------+
    | 1d6 | CR 1/4 and Lesser Beast Menu |
    +=====+==============================+
    | 1-2 | Menu A                       |
    +-----+------------------------------+
    | 3-4 | Menu B                       |
    +-----+------------------------------+
    | 5-6 | Menu C                       |
    +-----+------------------------------+
    
    +------+---------------------+
    | 1d20 | Lesser Beast Menu A |
    +======+=====================+
    | 1    | Axe Beak            |
    +------+---------------------+
    | 2    | Baboon              |
    +------+---------------------+
    | 3    | Badger              |
    +------+---------------------+
    | 4    | Bat                 |
    +------+---------------------+
    | 5    | Blood Hawk          |
    +------+---------------------+
    | 6    | Boar                |
    +------+---------------------+
    | 7    | Camel               |
    +------+---------------------+
    | 8    | Cat                 |
    +------+---------------------+
    | 9    | Chicken¹            |
    +------+---------------------+
    | 10   | Constrictor Snake   |
    +------+---------------------+
    | 11   | Crab                |
    +------+---------------------+
    | 12   | Deer                |
    +------+---------------------+
    | 13   | Draft Horse         |
    +------+---------------------+
    | 14   | Eagle               |
    +------+---------------------+
    | 15   | Elk                 |
    +------+---------------------+
    | 16   | Flying Snake        |
    +------+---------------------+
    | 17   | Frog                |
    +------+---------------------+
    | 18   | Giant Badger        |
    +------+---------------------+
    | 19   | Giant Bat           |
    +------+---------------------+
    | 20   | Giant Centipede     |
    +------+---------------------+
    
    ¹Chicken
      Raven stats with Advantage on checks to wake up targets instead
      of mimicry
    
    +------+--------------------------+
    | 1d20 | Lesser Beast Menu B      |
    +======+==========================+
    | 1    | Giant Crab               |
    +------+--------------------------+
    | 2    | Giant Fire Beetle        |
    +------+--------------------------+
    | 3    | Giant Frog               |
    +------+--------------------------+
    | 4    | Giant Lizard             |
    +------+--------------------------+
    | 5    | Giant Owl                |
    +------+--------------------------+
    | 6    | Giant Poisonous Snake    |
    +------+--------------------------+
    | 7    | Giant Rat                |
    +------+--------------------------+
    | 8    | Giant Weasel             |
    +------+--------------------------+
    | 9    | Giant Wolf Spider        |
    +------+--------------------------+
    | 10   | Goat                     |
    +------+--------------------------+
    | 11   | Hawk                     |
    +------+--------------------------+
    | 12   | Hyena                    |
    +------+--------------------------+
    | 13   | Jackal                   |
    +------+--------------------------+
    | 14   | Lemur²                   |
    +------+--------------------------+
    | 15   | Lizard                   |
    +------+--------------------------+
    | 16   | Mastiff                  |
    +------+--------------------------+
    | 17   | Mule                     |
    +------+--------------------------+
    | 18   | Newt³                    |
    +------+--------------------------+
    | 19   | Octopus                  |
    +------+--------------------------+
    | 20   | Octopus, Cascadian Tree⁴ |
    +------+--------------------------+
    
    ²Lemur
      Weasel stats with a common Climb speed instead of a bite attack
    ³Newt
      Lizard stats with Amphibious instead of a bite attack
    ⁴Octopus, Cascadian Tree:
      Octopus stats with Amphibious and a 10 ft land speed instead of
      camouflage
    
    +------+---------------------+
    | 1d20 | Lesser Beast Menu C |
    +======+=====================+
    | 1    | Owl                 |
    +------+---------------------+
    | 2    | Panther             |
    +------+---------------------+
    | 3    | Poisonous Snake     |
    +------+---------------------+
    | 4    | Pony                |
    +------+---------------------+
    | 5    | Pteranodon          |
    +------+---------------------+
    | 6    | Quipper             |
    +------+---------------------+
    | 7    | Rat                 |
    +------+---------------------+
    | 8    | Raven               |
    +------+---------------------+
    | 9    | Riding Horse        |
    +------+---------------------+
    | 10   | Scorpion            |
    +------+---------------------+
    | 11   | Sea Horse           |
    +------+---------------------+
    | 12   | Shocker Lizard⁵     |
    +------+---------------------+
    | 13   | Spider              |
    +------+---------------------+
    | 14   | Swarm of Bats       |
    +------+---------------------+
    | 15   | Swarm of Rats       |
    +------+---------------------+
    | 16   | Swarm of Ravens     |
    +------+---------------------+
    | 17   | Turtle⁶             |
    +------+---------------------+
    | 18   | Vulture             |
    +------+---------------------+
    | 19   | Weasel              |
    +------+---------------------+
    | 20   | Wolf                |
    +------+---------------------+
    
    ⁵Shocker Lizard
      Lizard stats with Static Electricity ranged attack of 1d6
      Electricity damage Close/Medium.
    ⁶Turtle
      Lizard stats with 14 natural armor and no climb speed.
    
    """
    # https://the-azure-triskele.obsidianportal.com/wikis/conjure-animals-table
    name = "Conjure Animals"

class CharacterFileFormatError(ValueError):
    """The given file is not a valid Dungeons and Dragons file."""

class DiceError(ValueError):
    """Improper formatting for a dice string."""

class LatexError(OSError):
    """PDFLatex did not execute correctly."""

class LatexNotFoundError(LatexError):
    """PDFLatex did not execute correctly."""    

class MonsterError(AttributeError):
    """Error retriving or using a D&D Monster."""

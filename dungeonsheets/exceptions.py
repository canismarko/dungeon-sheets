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


class JSONFormatError(RuntimeError):
    """The JSON file doesn't conform to the understood formats."""


class UnknownFileType(RuntimeError):
    """The input file does not match one of the known formats."""


class UnknownOutputFormat(RuntimeError):
    """The output format requested is not one of the known outputs."""


class ContentNotFound(ValueError):
    """The requested content could not be resolved."""

class AmbiguousContent(ValueError):
    """Multiple valid content entries were found."""

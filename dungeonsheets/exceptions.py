class DiceError(ValueError):
    """Improper formatting for a dice string."""

class LatexError(OSError):
    """PDFLatex did not execute correctly."""

class LatexNotFoundError(LatexError):
    """PDFLatex did not execute correctly."""    

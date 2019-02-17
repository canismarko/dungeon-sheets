def create_feature(**params):
    """Create a new subclass of ``Feature`` with given default parameters.
        
        Parameters
        ----------
        params : optional
        Saved as attributes of the new class.
        
        Returns
        -------
        NewFeature
        New feature class, subclass of ``Feature``, with given params.
        """
    NewFeature = type('UnknownFeature', (Feature,), params)
    return NewFeature

class Feature():
    """A special feature of the character."""
    name = "Unknown feature"
    type = "race"
    
    def __str__(self):
        s = self.name
        # Indicate if this is a race, class, or special feature
        s += f' ({", ".join(self.type)})'
        return s
    
    def __repr__(self):
        return f'<{self.name}>'


class Darkvision(Feature):
    """Accustomed to twilit forests and the night
    sky, you have superior vision in dark and dim conditions.
    You can see in dim light within 60 feet of you as if it
    were bright light, and in darkness as if it were dim light.
    You can't discern color in darkness, onIy shades of gray.
        
    """
    name = "Darkvision"
    type = "race"

class ArcaneRecovery(Feature):
    """You can regain some of your magical energy by
        studying your spellbook. Once per day during a short rest, you can
        choose to recover expended spell slots with a combined level equal
        to or less than half your wizard level (rounded up).
        
        """
    name = "Arcane Recovery"
    type = "class"

class FeyAncestry(Feature):
    """You have advantage on saving throws against being
        charmed, and magic can’t put you to sleep.
        
        """
    name = "Fey Ancestry"
    type = "race"

class Trance(Feature):
    """Elves don’t need to sleep. They meditate deeply, remaining
        semiconscious, for 4 hours a day and gain the same benefit a human
        does from 8 hours of sleep.
        
        """
    name = "Trance"
    type = "race"

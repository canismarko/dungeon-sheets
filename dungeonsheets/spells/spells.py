def create_spell(**params):
    """Create a new subclass of ``Spell`` with given default parameters.
    
    Useful for spells that haven't been entered into the ``spells.py``
    file yet.
    
    Parameters
    ----------
    params : optional
      Saved as attributes of the new class.
    
    Returns
    -------
    NewSpell
      New spell class, subclass of ``Spell``, with given params.
    """
    NewSpell = Spell
    NewSpell.name = params.get('name', 'Unknown Spell')
    NewSpell.level = params.get('level', 9)
    return NewSpell


class Spell():
    """A magical spell castable by a player character."""
    level = 0
    name = "Unknown spell"
    casting_time = "1 action"
    casting_range = "60 ft"
    components = ()
    materials = ""
    duration = "instantaneous"
    ritual = False
    _concentration = False
    magic_school = ""
    classes = ()
    
    def __str__(self):
        if len(self.components) == 0:
            s = self.name
        else:
            s = self.name + ' ({:s}) '.format(','.join(self.components))
        # Indicate if this is a ritual or a concentration
        indicators = [('R', self.ritual), ('C', self.concentration), ('$', self.special_material)]
        indicators = tuple(letter for letter, is_active in indicators if is_active)
        if len(indicators):
            s += f' ({", ".join(indicators)})'
        return s
    
    def __repr__(self):
        return "\"{:s}\"".format(self.name)

    def __eq__(self, other):
        return (self.name == other.name) and (self.level == other.level)

    def __hash__(self):
        return 0
    
    @property
    def component_string(self):
        s = f'{", ".join(self.components)}'
        if "M" in self.components:
            s += f' ({self.materials})'
        return s
    
    @property
    def concentration(self):
        return ('concentration' in self.duration.lower()) or self._concentration

    @concentration.setter
    def concentration(self, val: bool):
        self._concentration = val

    @property
    def special_material(self):
        return ('worth at least' in self.materials.lower())


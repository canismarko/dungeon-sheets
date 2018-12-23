from .features import Feature


class DraconicResilience(Feature):
    """As magic flows through your body, it causes physical traits of your dragon
    ancestors to emerge. At 1st level, your hit point maximum increases by 1
    and increases by 1 again whenever you gain a level in this class.

    Additionally, parts of your skin are covered by a thin sheen of dragon-like
    scales. When you aren’t wearing armor, your AC equals 13 + your Dexterity
    modifier.

    This bonus is computed in the AC given on the Character Sheet above.

    """
    name = "Draconic Resilience"
    source = "Sorceror (Draconic Bloodline)"

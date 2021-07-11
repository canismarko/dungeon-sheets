import re

from jinja2 import Environment, PackageLoader


from dungeonsheets.stats import mod_str, ability_mod_str, stat_abbreviation


# A dice string, with optional backticks: ``1d6 + 3``
dice_re = re.compile(r"`*(\d+d\d+(?:\s*\+\s*\d+)?)`*")


def jinja_environment():
    """Prepare a new environment for Jinja templates.

    This function loads filters that are agnostic to the output
    format. Format specific filters (e.g. html, latex, etc.) should be
    added to ``jinja_env.filters``.

    Returns
    -------
    jinja_env
      The newly created jinja environment.

    """
    jinja_env = Environment(
        loader=PackageLoader("dungeonsheets", "forms"),
        block_start_string="[%",
        block_end_string="%]",
        variable_start_string="[[",
        variable_end_string="]]",
    )
    jinja_env.filters["mod_str"] = mod_str
    jinja_env.filters["ability_mod_str"] = ability_mod_str
    jinja_env.filters["stat_abbreviation"] = stat_abbreviation
    return jinja_env

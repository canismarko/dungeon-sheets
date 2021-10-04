from collections import namedtuple

from dungeonsheets.content import Content

XPThreshold = namedtuple("XPThreshold", ("easy", "medium", "hard", "deadly"))


xp_thresholds_by_character_level = {
    1: XPThreshold(25, 50, 75, 100),
    2: XPThreshold(50, 100, 150, 200),
    3: XPThreshold(75, 150, 225, 400),
    4: XPThreshold(125, 250, 375, 500),
    5: XPThreshold(250, 500, 750, 1100),
    6: XPThreshold(300, 600, 900, 1400),
    7: XPThreshold(350, 750, 1100, 1700),
    8: XPThreshold(450, 900, 1400, 2100),
    9: XPThreshold(550, 1100, 1600, 2400),
    10: XPThreshold(600, 1200, 1900, 2800),
    11: XPThreshold(800, 1600, 2400, 3600),
    12: XPThreshold(1000, 2000, 3000, 4500),
    13: XPThreshold(1100, 2200, 3400, 5100),
    14: XPThreshold(1250, 2500, 3800, 5700),
    15: XPThreshold(1400, 2800, 4300, 6400),
    16: XPThreshold(1600, 3200, 4800, 7200),
    17: XPThreshold(2000, 3900, 5900, 8800),
    18: XPThreshold(2100, 4200, 6300, 9500),
    19: XPThreshold(2400, 4900, 7300, 10900),
    20: XPThreshold(2800, 5700, 8500, 12700),
}


def xp_thresholds(party):
    thresholds = []
    for member in party:
        xp_th = xp_thresholds_by_character_level.get(
            getattr(member, 'level', 0), XPThreshold(0, 0, 0, 0))
        thresholds.append(xp_th)
    final_thresholds = XPThreshold(
        easy=sum(th.easy for th in thresholds),
        medium=sum(th.medium for th in thresholds),
        hard=sum(th.hard for th in thresholds),
        deadly=sum(th.deadly for th in thresholds),
    )
    return final_thresholds


class Encounter(Content):
    pass

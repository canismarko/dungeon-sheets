import random


def roll(d, n=1):
    """roll(6, 2) means roll 2d6"""
    return sum([random.randint(1, d) for _ in range(n)])
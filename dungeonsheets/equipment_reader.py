#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:41:46 2022

@author: mauricio
"""
import warnings
import re
from dungeonsheets.weapons import simple_weapons, martial_weapons, firearms
from dungeonsheets.armor import all_armors

all_weapons = simple_weapons + martial_weapons + firearms
item_reader = re.compile(r"(\d*)(\s*)(.+)")
gear_weight = {"abacus":2,
               "alms box":3,
               "vial of acid":1,
               "acid vials":1,
               "flask of alchemist's fire":1,
               "flasks of alchemist's fire":1,
               "flask of oil":1,
               "flasks of oil":1,
               "arrows":1/20,
               "arrow":1/20,
               "bowgun needles": 1/50,
               "crosbow bolts":1.5/20,
               "sling bullets":1.5/20,
               "antitoxin":0,
               "crystal":1,
               "orb":3,
               "rod":2,
               "staff":4,
               "wand":1,
               "backpack":5,
               "ball bearings":2/1000,
               "barrel":70,
               "basked":2,
               "bedroll":7,
               "bell":0,
               "blanket":3,
               "block and tackle":5,
               "block of incense":1/20,
               "blocks of incense":1/20,
               "censer":1/25,
               "book":5,
               "book of lore":5,
               "glass bottle":2,
               "bucket":2,
               "caltrops":2/20,
               "candle":0,
               "candles":0,
               "crosbow bolt case":1,
               "scroll case":1,
               "map case":1,
               "cases for maps and scrolls":1,
               "feet of chain":1,
               "feet chain":1,
               "chalk":0,
               "chest":25,
               "climber's kit":12,
               "common clothes":3,
               "costume":4,
               "costumes":4,
               "fine clothes":6,
               "traveler's clothes":4,
               "component pouch":2,
               "crowbar": 5,
               "sprig of mistletoe":0,
               "totem":0,
               "wooden staff":4,
               "yew wand":1,
               "fishing tackle":4,
               "flask":1,
               "tankard":1,
               "grappling hook":4,
               "hammer":3,
               "knife":1,
               "small knife":1,
               "sacrificial knife":1,
               "sledge hammer":10,
               "healer's kit":3,
               "amulet":1,
               "emblem":0,
               "reliquary":2,
               "flask of holy water":1,
               "hourglass":1,
               "hunting trap":25,
               "bottle of ink":0,
               "ink pen":0,
               "jug":4,
               "pitcher":4,
               "ladder":25,
               "lamp":1,
               "bullseye lantern":2,
               "hooded lantern":2,
               "lock":1,
               "magnifying glass":0,
               "manacles":6,
               "mess kit":1,
               "steel mirror":0.5,
               "flask of oil":1,
               "paper sheet":0,
               "parchment":0,
               "sheets of parchment":0,
               "vial of perfume":0,
               "miner's pick":10,
               "piton":0.25,
               "pitons":0.25,
               "vial of poison":0,
               "feet pole":7,
               "iron pot":10,
               "potion of healing":0.5,
               "pouch":1,
               "little bag of sand":1,
               "quiver":1,
               "portable ram":35,
               "days of rations":2,
               "day of ration":2,
               "robes":4,
               "feet of hempen rope":10/50,
               "feet hempen rope":10/50,
               "feet of silk rope":5/50,
               "feet of string":1/50,
               "feet silk rope":5/50,
               "sack":0.5,
               "merchant's scale":3,
               "sealing wax":0,
               "shovel":5,
               "signal whistle":0,
               "signet ring":0,
               "soap":0,
               "spell book":3,
               "iron spikes":5/10,
               "spyglass":1,
               "two-person tent":20,
               "tinderbox":1,
               "torch":1,
               "torches":1,
               "vial":0,
               "vestments":3,
               "waterskin":5,
               "wheatstone":1, 
               "moonstone":1/20,
               "quartz":1/20,
               "gemstone":1/20}

tools_weight = {"alchemist's supplies":8,
                "brewer's supplies":9,
                "calligrapher's supplies":5,
                "capenter's tools":6,
                "cartographer's tools":6,
                "cobbler's tools":5,
                "cook's utensils":8,
                "glassblower's tools":5,
                "jeweler's tools":2,
                "leatherworker's tools":5,
                "mason's tools":8,
                "painter's supplies":5,
                "potter's tools":3,
                "smith's tools":8,
                "tinker's tools":10,
                "weaver's tools":5,
                "woodcarver's tools":5,
                "disguise kit":3,
                "forgery kit":5,
                "dice set":0,
                "set of bone dice":0,
                "dragonchess set":0.5,
                "playing card set":0,
                "three-dragon ante set":0,
                "herbalism kit":3,
                "bagpipes":6,
                "drum":3,
                "dulcimer":10,
                "flute":1,
                "lute":2,
                "lyre":2,
                "horn":2,
                "pan flute":2,
                "shawm":1,
                "viol":1,
                "navigator's tools":2,
                "poisoner's kit":2,
                "thieves' tools":1}

gear_weight.update(tools_weight)
gear_weight.update({armor.name.lower():armor.weight for armor in all_armors})
gear_weight.update({w.name.lower():w.weight for w in all_weapons})

burglars_pack = """backpack, {ball_bearings} ball bearings, 
{string} feet of string, bell, {candles} candles, crowbar, hammer, 
{pitons} pitons, hooded lantern, 
{oil} flasks of oil, {rations} days of rations, tinderbox, waterskin, 
{rope} feet of hempen rope"""
diplomats_pack = """chest, {cases} cases for maps and scrolls, 
fine clothes, bottle of ink, ink pen, lamp, {oil} flasks of oil, 
{paper} paper sheet, vial of perfume, sealing wax, soap"""
dungeoneers_pack = """backpack, crowbar, hammer, {pitons} pitons, 
{torches} torches, tinderbox, {rations} days of rations, waterskin,
{rope} feet of hempen rope"""
entertainers_pack = """backpack, bedroll, {costumes} costumes, 
{candles} candles, {rations} days of rations, waterskin, disguise kit"""
explorers_pack = """backpack, bedroll, mess kit, tinderbox, {torches} torches,
{rations} days of rations, waterskin, {rope} feet of hempen rope"""
priests_pack = """backpack, blanket, {candles} candles, tinderbox, alms box, 
{incense} blocks of incense, censer, vestments, {rations} days of rations, 
waterskin"""
scholars_pack = """backpack, book of lore, bottle of ink, ink pen, 
{parchment} sheets of parchment, little bag of sand, small knife"""


def equipment_weight_parser(equipment, gear_dict={}):
    if not equipment.strip():
        return 0
    gear_w = gear_weight.copy()
    gear_w.update(gear_dict)
    weight = 0
    for gear in equipment.split(','):
        gear = gear.lower().strip().strip(".")
        q, _, item = item_reader.match(gear).groups()
        if q:
            q = int(q)
        else:
            q = 1
        if not(item in gear_w.keys()):
            msg = f'{item} not found in gear_weight dictionary, please add.'
            warnings.warn(msg)
            continue
        weight = weight + q*gear_w[item]
    return weight
    

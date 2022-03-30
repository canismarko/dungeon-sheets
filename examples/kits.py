#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 01:04:23 2022

@author: mauricio
"""



burglars_pack = """backpack, {ball_bearings} ball bearings, 
{string} feet of string, bell, {candles} candles, crowbar, hammer, 
{pitons} pitons, hooded lantern, 
{oil} flasks of oil, {rations} days of rations, tinderbox, waterskin, 
{rope} feet of hempen rope."""
diplomats_pack = """chest, {cases} cases for maps and scrolls, 
fine clothes, bottle of ink, ink pen, lamp, {oil} flasks of oil, 
{paper} paper sheet, vial of perfume, sealing wax, soap."""
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


if __name__ == "__main__":
    from dungeonsheets.equipment_reader import equipment_weight_parser
    quantities = {"ball_bearings":350, "string": 23, "candles": 4,
                  "pitons":18, "oil":3, "rations":2, "rope":15,
                  "cases":3, "paper":5, "torches":7, "costumes":2,
                  "incense":3, "parchment":17}
    for kit in (burglars_pack, diplomats_pack, dungeoneers_pack, 
                entertainers_pack, explorers_pack, priests_pack,
                scholars_pack):
        equip = kit.format(**quantities)
        print("EQUIPMENT: " + equip)
        equip_weight = equipment_weight_parser(equip)
        print("WEIGHT: " + str(equip_weight) + " lbs.")
        print("="*15)

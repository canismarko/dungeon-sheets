from unittest import TestCase
from dungeonsheets import equipment_reader as equip

class TestEquipmentReader(TestCase):
    
    def test_equipment_weight_parser(self):
        content = """backpack, bedroll, mess kit, tinderbox, 10 torches,
        9 days of rations, waterskin, 50 feet of hempen rope, Herbalism Kit, 
        component pouch"""
        eq_weight = equip.equipment_weight_parser(content)
        self.assertEqual(eq_weight, 62)
        # Check additional equipment dict
        equipment_weight_dict = {"human skin mask":0.5}
        content = content + ", human skin mask"
        eq_weight = equip.equipment_weight_parser(content, equipment_weight_dict)
        self.assertEqual(eq_weight, 62.5)
        
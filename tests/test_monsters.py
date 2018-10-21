#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets import monsters, exceptions


class MonsterTestCase(TestCase):
    def test_ability_scores(self):
        wolf = monsters.Wolf()
        self.assertEqual(wolf.strength.value, 12)
        self.assertEqual(wolf.strength.modifier, 1)
        self.assertEqual(wolf.strength.saving_throw, 1)

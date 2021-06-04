#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets import features, character
from dungeonsheets.features import create_feature, Feature, all_features, bard


class TestFeatures(TestCase):
    """Tests for features and feature-related activities."""

    def test_all_features(self):
        # Make sure only features are returned
        for ThisFeature in all_features():
            self.assertTrue(
                isinstance(ThisFeature, type),
                f"``all_features`` returned {ThisFeature} (not a class)",
            )
            self.assertTrue(
                issubclass(ThisFeature, Feature),
                f"``all_features`` returned {ThisFeature} (not a feature)",
            )
        # Pick a couple of known features to spot-check for
        all_the_features = list(all_features())
        self.assertIn(features.FalseIdentity, all_the_features)
        self.assertIn(features.DivineSmite, all_the_features)

    def test_create_feature(self):
        NewFeature = create_feature(name="Hello world")
        self.assertTrue(issubclass(NewFeature, Feature))
        self.assertEqual(NewFeature.name, "Hello world")
        feature = NewFeature()
        print(feature, feature.__class__, type(feature))


class BardTests(TestCase):
    def test_bardic_inspiration(self):
        # Level 1-4 Bard
        char = character.Character(classes=["bard"], levels=[2])
        bi = bard.BardicInspiration(owner=char)
        self.assertEqual(bi.name, "Bardic Inspiration (1d6/LR)")
        # Level 5-9 Bard
        char = character.Character(classes=["bard"], levels=[5])
        bi = bard.BardicInspiration(owner=char)
        self.assertEqual(bi.name, "Bardic Inspiration (1d8/SR)")
        # Level 10-14 Bard
        char = character.Character(classes=["bard"], levels=[10])
        bi = bard.BardicInspiration(owner=char)
        self.assertEqual(bi.name, "Bardic Inspiration (1d10/SR)")
        # Level 15+ Bard
        char = character.Character(classes=["bard"], levels=[15])
        bi = bard.BardicInspiration(owner=char)
        self.assertEqual(bi.name, "Bardic Inspiration (1d12/SR)")

    def test_song_of_rest(self):
        # Level 1-8 Bard
        char = character.Character(classes=["bard"], levels=[2])
        sor = bard.SongOfRest(owner=char)
        self.assertEqual(sor.name, "Song of Rest (1d6)")
        # Level 9-12 Bard
        char = character.Character(classes=["bard"], levels=[9])
        sor = bard.SongOfRest(owner=char)
        self.assertEqual(sor.name, "Song of Rest (1d8)")
        # Level 13-16 Bard
        char = character.Character(classes=["bard"], levels=[13])
        sor = bard.SongOfRest(owner=char)
        self.assertEqual(sor.name, "Song of Rest (1d10)")
        # Level 17+ Bard
        char = character.Character(classes=["bard"], levels=[17])
        sor = bard.SongOfRest(owner=char)
        self.assertEqual(sor.name, "Song of Rest (1d12)")

    def test_mantle_of_inspiration(self):
        for lvl in range(1, 5):
            char = character.Character(classes=["bard"], levels=[lvl])
            moi = bard.MantleOfInspiration(owner=char)
            self.assertEqual(moi.name, "Mantle of Inspiration (5HP)")
        for lvl in range(5, 10):
            char = character.Character(classes=["bard"], levels=[lvl])
            moi = bard.MantleOfInspiration(owner=char)
            self.assertEqual(moi.name, "Mantle of Inspiration (8HP)")
        for lvl in range(10, 15):
            char = character.Character(classes=["bard"], levels=[lvl])
            moi = bard.MantleOfInspiration(owner=char)
            self.assertEqual(moi.name, "Mantle of Inspiration (11HP)")
        for lvl in range(15, 20):
            char = character.Character(classes=["bard"], levels=[lvl])
            moi = bard.MantleOfInspiration(owner=char)
            self.assertEqual(moi.name, "Mantle of Inspiration (14HP)")

    def test_psychic_blades(self):
        for lvl in range(1, 5):
            char = character.Character(classes=["bard"], levels=[lvl])
            pb = bard.PsychicBlades(owner=char)
            self.assertEqual(pb.name, "Psychic Blades (2d6)")
        for lvl in range(5, 10):
            char = character.Character(classes=["bard"], levels=[lvl])
            pb = bard.PsychicBlades(owner=char)
            self.assertEqual(pb.name, "Psychic Blades (3d6)")
        for lvl in range(10, 15):
            char = character.Character(classes=["bard"], levels=[lvl])
            pb = bard.PsychicBlades(owner=char)
            self.assertEqual(pb.name, "Psychic Blades (5d6)")
        for lvl in range(15, 20):
            char = character.Character(classes=["bard"], levels=[lvl])
            pb = bard.PsychicBlades(owner=char)
            self.assertEqual(pb.name, "Psychic Blades (8d6)")

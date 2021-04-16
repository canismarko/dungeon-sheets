#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets import features
from dungeonsheets.features import create_feature, Feature, all_features


class TestFeatures(TestCase):
    """Tests for features and feature-related activities."""
    def test_all_features(self):
        # Make sure only features are returned
        for ThisFeature in all_features():
            self.assertTrue(isinstance(ThisFeature, type),
                            f"``all_features`` returned {ThisFeature} (not a class)")
            self.assertTrue(issubclass(ThisFeature, Feature),
                            f"``all_features`` returned {ThisFeature} (not a feature)")
        # Pick a couple of known features to spot-check for
        all_the_features = list(all_features())
        self.assertIn(features.FalseIdentity, all_the_features)
        self.assertIn(features.DivineSmite, all_the_features)
    
    def test_create_feature(self):
        NewFeature = create_feature(name="Hello world")
        self.assertTrue(issubclass(NewFeature, Feature))
        self.assertEqual(NewFeature.name, 'Hello world')
        feature = NewFeature()
        print(feature, feature.__class__, type(feature))

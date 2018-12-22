#!/usr/bin/env python

from unittest import TestCase

from dungeonsheets.features import create_feature, Feature


class TestFeatures(TestCase):
    """Tests for features and feature-related activities."""
    
    def test_create_feature(self):
        NewFeature = create_feature(name="Hello world")
        self.assertTrue(issubclass(NewFeature, Feature))
        self.assertEqual(NewFeature.name, 'Hello world')
        feature = NewFeature()
        print(feature, feature.__class__, type(feature))

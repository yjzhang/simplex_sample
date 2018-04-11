import unittest
from unittest import TestCase

import numpy as np

import simplex_sample

class SimplexSampleTest(TestCase):

    def setUp(self):
        pass

    def testRandomGenerate(self):
        sample = simplex_sample.sample(2, 100)
        self.assertTrue((sample>=0).all())
        self.assertTrue((sample.sum(1)==1).all())
        sample = simplex_sample.sample(20, 1000)
        self.assertTrue((sample>=0).all())
        self.assertTrue((sample.sum(1)==1).all())

    def testDataSample(self):
        points = simplex_sample.sample(8, 1000)
        indices = simplex_sample.data_sample(points.T, points)
        for i, index in enumerate(indices):
            self.assertEqual(i, index)

    def testSamplingWithoutReplacement(self):
        points = simplex_sample.sample(8, 1000)
        sample_points = simplex_sample.sample(8, 500)
        indices = simplex_sample.data_sample(points.T, sample_points,
                replace=False)
        self.assertEqual(len(indices), len(set(indices)))

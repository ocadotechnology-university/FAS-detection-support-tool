import os
import unittest
import numpy as np
from implementation.raport.generator.raport_generator import RaportGenerator


class TestRaportGenerator(unittest.TestCase):

    def test_init(self):
        generator = RaportGenerator()

        # check if the paths are read correctly and the file opens
        self.assertEqual(generator.path, "resources")
        self.assertEqual(generator.child_data, "child_data.csv")

        # check if the gender is correct
        self.assertIn(generator.gender, ['f', 'm'])

        # check the arrays
        self.assertIsInstance(generator.child_age_weight_array_X, list)
        self.assertIsInstance(generator.child_age_weight_array_Y, list)
        self.assertTrue(len(generator.child_age_weight_array_X) > 0)
        self.assertTrue(len(generator.child_age_weight_array_Y) > 0)
        self.assertIsInstance(generator.age_weight_array, np.ndarray)
        self.assertTrue(generator.age_weight_array.shape[0] > 0)
        self.assertTrue(generator.age_weight_array.shape[1] > 0)

    def test_generate(self):
        generator = RaportGenerator()
        generator.generate()

        # check whether the files are saved
        self.assertTrue("growth.pdf" in os.listdir(generator.path))
        self.assertTrue("growth.png" in os.listdir(generator.path))

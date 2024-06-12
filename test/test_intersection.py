import unittest
import utils.intersection as intersection

class Test_intersection(unittest.TestCase):
    def test_1_true(self):
        self.assertTrue(intersection.intersection(
            intersection.Point(2, 2),
            intersection.Point(10, 7),
            intersection.Point(3, 8),
            intersection.Point(8, 1)
        ))

    def test_2_true(self):
        self.assertTrue(intersection.intersection(
            intersection.Point(1, 1),
            intersection.Point(5, 5),
            intersection.Point(3, 3),
            intersection.Point(6, 6)
        ))

    def test_3_true(self):
        self.assertTrue(intersection.intersection(
            intersection.Point(1, 1),
            intersection.Point(5, 5),
            intersection.Point(3, 3),
            intersection.Point(4, 4)
        ))

    def test_4_true(self):
        self.assertTrue(intersection.intersection(
            intersection.Point(1, 1),
            intersection.Point(5, 5),
            intersection.Point(3, 3),
            intersection.Point(5, 2)
        ))

    def test_5_true(self):
        self.assertTrue(intersection.intersection(
            intersection.Point(2, 1),
            intersection.Point(4, 3),
            intersection.Point(4, 3),
            intersection.Point(4, 6)
        ))

    def test_6_true(self):
        self.assertTrue(intersection.intersection(
            intersection.Point(2, 1),
            intersection.Point(2, 6),
            intersection.Point(2, 5),
            intersection.Point(5, 5)
        ))

    def test_1_false(self):
        self.assertFalse(intersection.intersection(
            intersection.Point(1, 2),
            intersection.Point(7, 6),
            intersection.Point(7, 3),
            intersection.Point(9, 1)
        ))

    def test_2_false(self):
        self.assertFalse(intersection.intersection(
            intersection.Point(1, 1),
            intersection.Point(5, 5),
            intersection.Point(6, 6),
            intersection.Point(7, 7)
        ))

    def test_3_false(self):
        self.assertFalse(intersection.intersection(
            intersection.Point(2, 2),
            intersection.Point(4, 4),
            intersection.Point(5, 4),
            intersection.Point(8, 4)
        ))

    def test_4_false(self):
        self.assertFalse(intersection.intersection(
            intersection.Point(1, 3),
            intersection.Point(3, 3),
            intersection.Point(5, 3),
            intersection.Point(7, 3)
        ))
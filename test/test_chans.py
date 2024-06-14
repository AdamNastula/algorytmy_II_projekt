import unittest
from utils.intersection import Point
import utils.chans_algorithm as chan

class Test_Chans_algorithm(unittest.TestCase):
    def test1(self):
        points = [
            Point(10, 33),
            Point(25, 47),
            Point(4, 12),
            Point(39, 22),
            Point(45, 18),
            Point(27, 30),
            Point(17, 8),
            Point(30, 42),
            Point(6, 15),
            Point(23, 9),
            Point(12, 34),
            Point(5, 28),
            Point(16, 21),
            Point(40, 49),
            Point(18, 24),
            Point(35, 36),
            Point(2, 44),
            Point(28, 3),
            Point(14, 31),
            Point(8, 26),
            Point(41, 11),
            Point(50, 39),
            Point(22, 17),
            Point(33, 13),
            Point(1, 46),
            Point(38, 19),
            Point(9, 20),
            Point(31, 6),
            Point(11, 43),
            Point(48, 7),
            Point(19, 14),
            Point(47, 29),
            Point(21, 25),
            Point(32, 37),
            Point(44, 2),
            Point(7, 40),
            Point(20, 5),
            Point(46, 1),
            Point(37, 32),
            Point(13, 35),
            Point(26, 27),
            Point(36, 4),
            Point(43, 16),
            Point(34, 23),
            Point(3, 38)
        ]

        expected_hull = [
            Point(40, 49),
            Point(50, 39),
            Point(48, 7),
            Point(46, 1),
            Point(28, 3),
            Point(20, 5),
            Point(4, 12),
            Point(1, 46)
        ]

        hull = chan.calculate_hull(points)['convex_hull']
        for pair in zip(expected_hull, hull):
            self.assertEqual(pair[0], pair[1])

    def test2(self):
        points = [
            Point(42, 67),
            Point(15, 89),
            Point(73, 35),
            Point(84, 56),
            Point(23, 78),
            Point(67, 12),
            Point(45, 98),
            Point(12, 54),
            Point(90, 32),
            Point(37, 76),
            Point(54, 23),
            Point(61, 87),
            Point(30, 40),
            Point(21, 92),
            Point(79, 61),
            Point(56, 15),
            Point(34, 85),
            Point(63, 47),
            Point(92, 70),
            Point(28, 19),
            Point(77, 44),
            Point(49, 83),
            Point(88, 51),
            Point(31, 72),
            Point(66, 38),
            Point(40, 95),
            Point(13, 59),
            Point(82, 21),
            Point(58, 75),
            Point(26, 46),
            Point(72, 34),
            Point(50, 91),
            Point(35, 27),
            Point(97, 68),
            Point(19, 84),
            Point(64, 31),
            Point(85, 49),
            Point(47, 93),
            Point(25, 62),
            Point(78, 29),
            Point(51, 77),
            Point(16, 88),
            Point(83, 37),
            Point(59, 99),
            Point(36, 58)
        ]

        expected_hull = [            
            Point(59, 99),
            Point(97, 68),
            Point(90, 32),
            Point(82, 21),
            Point(67, 12),
            Point(28, 19),
            Point(12, 54),
            Point(15, 89),
            Point(21, 92),
            Point(45, 98)
        ]

        hull = chan.calculate_hull(points)['convex_hull']
        for pair in zip(expected_hull, hull):
            self.assertEqual(pair[0], pair[1])

    def test3(self):
        points = [
            Point(4, 4),
            Point(4, 6),
            Point(4, 7),
            Point(10, 10),
            Point(1, 1),
            Point(1, 1),
            Point(5, 6),
            Point(5, 7)
        ]

        expected_hull = [
            Point(10, 10),
            Point(1, 1),
            Point(4, 7)
        ]

        hull = chan.calculate_hull(points)['convex_hull']
        for pair in zip(expected_hull, hull):
            self.assertEqual(pair[0], pair[1])

    def test4(self):
        points = [        
            Point(1, 10),
            Point(10, 1),
            Point(10, 10),
            Point(3, 2),
            Point(1, 1)
        ]

        expected_hull = [
            Point(1, 10),
            Point(10, 10), 
            Point(10, 1), 
            Point(1, 1)
        ]

        hull = chan.calculate_hull(points)['convex_hull']
        for pair in zip(expected_hull, hull):
            self.assertAlmostEqual(pair[0], pair[1])
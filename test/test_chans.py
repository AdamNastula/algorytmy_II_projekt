import unittest
import intersection as intersection
import chans_algorithm as chan

class Test_Chans_algorithm(unittest.TestCase):
    def test_1(self):
        points = [
            intersection.Point(10, 33),
            intersection.Point(25, 47),
            intersection.Point(4, 12),
            intersection.Point(39, 22),
            intersection.Point(45, 18),
            intersection.Point(27, 30),
            intersection.Point(17, 8),
            intersection.Point(30, 42),
            intersection.Point(6, 15),
            intersection.Point(23, 9),
            intersection.Point(12, 34),
            intersection.Point(5, 28),
            intersection.Point(16, 21),
            intersection.Point(40, 49),
            intersection.Point(18, 24),
            intersection.Point(35, 36),
            intersection.Point(2, 44),
            intersection.Point(28, 3),
            intersection.Point(14, 31),
            intersection.Point(8, 26),
            intersection.Point(41, 11),
            intersection.Point(50, 39),
            intersection.Point(22, 17),
            intersection.Point(33, 13),
            intersection.Point(1, 46),
            intersection.Point(38, 19),
            intersection.Point(9, 20),
            intersection.Point(31, 6),
            intersection.Point(11, 43),
            intersection.Point(48, 7),
            intersection.Point(19, 14),
            intersection.Point(47, 29),
            intersection.Point(21, 25),
            intersection.Point(32, 37),
            intersection.Point(44, 2),
            intersection.Point(7, 40),
            intersection.Point(20, 5),
            intersection.Point(46, 1),
            intersection.Point(37, 32),
            intersection.Point(13, 35),
            intersection.Point(26, 27),
            intersection.Point(36, 4),
            intersection.Point(43, 16),
            intersection.Point(34, 23),
            intersection.Point(3, 38)
        ]

        expected_hull = [
            intersection.Point(40, 49),
            intersection.Point(50, 39),
            intersection.Point(48, 7),
            intersection.Point(46, 1),
            intersection.Point(28, 3),
            intersection.Point(20, 5),
            intersection.Point(4, 12),
            intersection.Point(1, 46)
        ]

        hull = chan.calculate_hull(points)['convex_hull']
        for pair in zip(expected_hull, hull):
            self.assertEqual(pair[0], pair[1])

    def test_2(self):
        points = [
        intersection.Point(42, 67),
        intersection.Point(15, 89),
        intersection.Point(73, 35),
        intersection.Point(84, 56),
        intersection.Point(23, 78),
        intersection.Point(67, 12),
        intersection.Point(45, 98),
        intersection.Point(12, 54),
        intersection.Point(90, 32),
        intersection.Point(37, 76),
        intersection.Point(54, 23),
        intersection.Point(61, 87),
        intersection.Point(30, 40),
        intersection.Point(21, 92),
        intersection.Point(79, 61),
        intersection.Point(56, 15),
        intersection.Point(34, 85),
        intersection.Point(63, 47),
        intersection.Point(92, 70),
        intersection.Point(28, 19),
        intersection.Point(77, 44),
        intersection.Point(49, 83),
        intersection.Point(88, 51),
        intersection.Point(31, 72),
        intersection.Point(66, 38),
        intersection.Point(40, 95),
        intersection.Point(13, 59),
        intersection.Point(82, 21),
        intersection.Point(58, 75),
        intersection.Point(26, 46),
        intersection.Point(72, 34),
        intersection.Point(50, 91),
        intersection.Point(35, 27),
        intersection.Point(97, 68),
        intersection.Point(19, 84),
        intersection.Point(64, 31),
        intersection.Point(85, 49),
        intersection.Point(47, 93),
        intersection.Point(25, 62),
        intersection.Point(78, 29),
        intersection.Point(51, 77),
        intersection.Point(16, 88),
        intersection.Point(83, 37),
        intersection.Point(59, 99),
        intersection.Point(36, 58)
        ]

        expected_hull = [            
            intersection.Point(59, 99),
            intersection.Point(97, 68),
            intersection.Point(90, 32), 
            intersection.Point(82, 21), 
            intersection.Point(67, 12), 
            intersection.Point(28, 19), 
            intersection.Point(12, 54), 
            intersection.Point(15, 89), 
            intersection.Point(21, 92), 
            intersection.Point(45, 98)
        ]

        hull = chan.calculate_hull(points)['convex_hull']
        for pair in zip(expected_hull, hull):
            self.assertEqual(pair[0], pair[1])

    def test_3(self):
        points = [
            intersection.Point(4, 4),
            intersection.Point(4, 6), 
            intersection.Point(4, 7),
            intersection.Point(10, 10), 
            intersection.Point(1, 1), 
            intersection.Point(1, 1), 
            intersection.Point(5, 6), 
            intersection.Point(5, 7)
        ]

        expected_hull = [
            intersection.Point(x=10, y=10), 
            intersection.Point(x=1, y=1), 
            intersection.Point(x=4, y=7)
        ]

        hull = chan.calculate_hull(points)['convex_hull']
        for pair in zip(expected_hull, hull):
            self.assertEqual(pair[0], pair[1])

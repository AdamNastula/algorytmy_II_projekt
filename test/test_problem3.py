import unittest
import problem3.greedy_alg as gr
from problem3.bruteforce import test_bruteforce
from utils.towers import Tower

class TestBM(unittest.TestCase):
    def test1(self):
        return_list=[]
        return_list_greedy=[]
        towers=[
            Tower(40, 49, 73),
            Tower(18, 24, 70),
            Tower(35, 36, 48),
            Tower(2, 44, 80),
            Tower(28, 3, 5),
            Tower(14, 31, 15),
            Tower(8, 26, 45),
            Tower(41, 11, 65),
            Tower(15, 4, 78),
            Tower(19, 16, 45),
            Tower(8, 25, 54),
            Tower(2, 19, 88),
            Tower(26, 12, 20),
            Tower(9, 6, 61),
            Tower(11, 28, 47),
            Tower(1, 7, 59),
            Tower(14, 29, 32),
            Tower(20, 3, 74),
            Tower(40, 49, 73)
        ]
        m = 3
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)


        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test2(self):
        return_list=[]
        return_list_greedy=[]
        towers=[
            Tower(3, 10, 42),
            Tower(14, 5, 78),
            Tower(17, 7, 91),
            Tower(8, 16, 14),
            Tower(19, 9, 68),
            Tower(6, 4, 53),
            Tower(2, 19, 81),
            Tower(5, 8, 37),
            Tower(11, 3, 95),
            Tower(10, 12, 25),
            Tower(13, 0, 63),
            Tower(18, 15, 10),
            Tower(7, 18, 84),
            Tower(1, 11, 49),
            Tower(16, 6, 20),
            Tower(12, 1, 73),
            Tower(9, 13, 31),
            Tower(4, 17, 57),
            Tower(0, 14, 5),
            Tower(15, 2, 89),
            Tower(0, 0, 27),
            Tower(8, 20, 90),
            Tower(11, 9, 46),
            Tower(18, 13, 72),
            Tower(7, 3, 18),
            Tower(1, 12, 40),
            Tower(16, 7, 61),
            Tower(10, 5, 83),
            Tower(5, 18, 94),
            Tower(3, 1, 74),
            Tower(3, 10, 42)
        ]
        m = 2
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)


        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test3(self):
        return_list=[]
        return_list_greedy=[]
        towers=[
            Tower(14, 16, 35),
            Tower(9, 2, 79),
            Tower(1, 5, 58),
            Tower(18, 10, 12),
            Tower(6, 15, 87),
            Tower(12, 4, 42),
            Tower(3, 19, 70),
            Tower(17, 8, 23),
            Tower(10, 11, 50),
            Tower(5, 1, 99),
            Tower(0, 13, 31),
            Tower(15, 6, 66),
            Tower(7, 12, 15),
            Tower(2, 17, 38),
            Tower(19, 14, 82),
            Tower(4, 3, 63),
            Tower(11, 18, 47),
            Tower(16, 0, 7),
            Tower(8, 7, 56),
            Tower(13, 9, 91),
            Tower(14, 16, 35)
        ]
        m = 3
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)


        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test4(self):
        return_list=[]
        return_list_greedy=[]
        towers=[
            Tower(5, 4, 39),
            Tower(18, 16, 85),
            Tower(2, 3, 25),
            Tower(13, 11, 68),
            Tower(7, 0, 54),
            Tower(12, 5, 9),
            Tower(9, 7, 76),
            Tower(1, 19, 94),
            Tower(16, 2, 61),
            Tower(0, 13, 28),
            Tower(14, 15, 88),
            Tower(3, 12, 42),
            Tower(8, 6, 17),
            Tower(19, 10, 72),
            Tower(6, 1, 82),
            Tower(11, 8, 37),
            Tower(4, 17, 49),
            Tower(17, 14, 64),
            Tower(10, 9, 95),
            Tower(15, 18, 21),
            Tower(5, 4, 39)
        ]
        m = 4
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)


        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)
    def test5(self):
        return_list=[]
        return_list_greedy=[]
        towers=[
            Tower(5, 16, 11),
            Tower(18, 3, 90),
            Tower(2, 7, 55),
            Tower(13, 4, 33),
            Tower(7, 12, 77),
            Tower(12, 1, 66),
            Tower(9, 18, 22),
            Tower(1, 2, 44),
            Tower(16, 11, 99),
            Tower(0, 10, 73),
            Tower(14, 6, 8),
            Tower(3, 19, 59),
            Tower(8, 15, 32),
            Tower(19, 9, 20),
            Tower(6, 0, 89),
            Tower(11, 8, 51),
            Tower(4, 17, 14),
            Tower(17, 13, 69),
            Tower(10, 5, 96),
            Tower(15, 14, 45),
            Tower(5, 16, 11)
        ]
        m = 2
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)


        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test6(self):
        return_list = []
        return_list_greedy = []
        towers = [
            Tower(5, 3, 18),
            Tower(18, 12, 62),
            Tower(2, 9, 87),
            Tower(13, 6, 40),
            Tower(7, 15, 4),
            Tower(12, 2, 56),
            Tower(9, 19, 79),
            Tower(1, 11, 13),
            Tower(16, 10, 84),
            Tower(0, 4, 71),
            Tower(14, 7, 36),
            Tower(3, 18, 93),
            Tower(8, 14, 28),
            Tower(19, 8, 95),
            Tower(6, 17, 10),
            Tower(11, 0, 53),
            Tower(4, 16, 16),
            Tower(17, 14, 60),
            Tower(10, 6, 81),
            Tower(15, 13, 25),
            Tower(5, 3, 18),
        ]
        m = 5
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)
    def test7(self):
        return_list=[]
        return_list_greedy=[]
        towers=[
            Tower(15, 12, 57),
            Tower(5, 2, 99),
            Tower(18, 9, 24),
            Tower(2, 15, 70),
            Tower(13, 3, 36),
            Tower(7, 11, 93),
            Tower(12, 0, 40),
            Tower(9, 16, 13),
            Tower(1, 4, 66),
            Tower(16, 6, 29),
            Tower(0, 15, 86),
            Tower(14, 8, 54),
            Tower(3, 1, 1),
            Tower(8, 11, 39),
            Tower(19, 16, 88),
            Tower(6, 9, 55),
            Tower(11, 2, 72),
            Tower(4, 19, 31),
            Tower(17, 12, 95),
            Tower(10, 8, 22),
            Tower(15, 12, 57)
        ]
        m = 2
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)


        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test8(self):
        return_list = []
        return_list_greedy = []
        towers = [
            Tower(5, 13, 89),
            Tower(18, 7, 27),
            Tower(2, 4, 63),
            Tower(13, 12, 98),
            Tower(7, 1, 41),
            Tower(12, 16, 6),
            Tower(9, 3, 80),
            Tower(1, 17, 75),
            Tower(16, 5, 48),
            Tower(0, 14, 21),
            Tower(14, 9, 67),
            Tower(3, 0, 35),
            Tower(8, 10, 92),
            Tower(19, 15, 50),
            Tower(6, 8, 18),
            Tower(11, 1, 61),
            Tower(4, 18, 84),
            Tower(17, 11, 38),
            Tower(10, 7, 3),
            Tower(5, 13, 89)
        ]
        m = 6
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test9(self):
        return_list = []
        return_list_greedy = []
        towers = [
            Tower(15, 13, 49),
            Tower(5, 14, 2),
            Tower(18, 8, 34),
            Tower(2, 5, 91),
            Tower(13, 13, 62),
            Tower(7, 2, 45),
            Tower(12, 17, 19),
            Tower(9, 4, 73),
            Tower(1, 18, 81),
            Tower(16, 4, 30),
            Tower(0, 16, 97),
            Tower(14, 10, 58),
            Tower(3, 19, 32),
            Tower(8, 12, 14),
            Tower(19, 17, 69),
            Tower(6, 10, 76),
            Tower(11, 3, 42),
            Tower(4, 0, 83),
            Tower(17, 13, 4),
            Tower(10, 9, 60),
            Tower(15, 14, 23),
            Tower(15, 13, 49),
        ]
        m = 2
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test10(self):
        return_list = []
        return_list_greedy = []
        towers = [
            Tower(5, 1, 64),
            Tower(18, 18, 8),
            Tower(2, 7, 42),
            Tower(13, 16, 30),
            Tower(7, 3, 85),
            Tower(12, 10, 19),
            Tower(9, 0, 71),
            Tower(1, 14, 47),
            Tower(16, 12, 92),
            Tower(0, 5, 55),
            Tower(14, 2, 24),
            Tower(3, 11, 77),
            Tower(8, 6, 98),
            Tower(19, 4, 63),
            Tower(6, 13, 11),
            Tower(11, 17, 82),
            Tower(4, 9, 34),
            Tower(17, 5, 70),
            Tower(10, 3, 16),
            Tower(15, 19, 39),
            Tower(5, 1, 64),
        ]
        m = 5
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test11(self):
        return_list = []
        return_list_greedy = []
        towers = [
            Tower(5, 8, 90),
            Tower(18, 15, 26),
            Tower(2, 2, 72),
            Tower(13, 0, 48),
            Tower(7, 10, 3),
            Tower(12, 19, 68),
            Tower(9, 6, 97),
            Tower(1, 16, 44),
            Tower(16, 11, 20),
            Tower(0, 1, 79),
            Tower(14, 3, 56),
            Tower(3, 12, 37),
            Tower(8, 7, 7),
            Tower(19, 5, 51),
            Tower(6, 14, 29),
            Tower(11, 18, 86),
            Tower(4, 10, 12),
            Tower(17, 6, 94),
            Tower(10, 4, 67),
            Tower(15, 18, 41),
            Tower(5, 8, 90)
        ]
        m = 3
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test12(self):
        return_list = []
        return_list_greedy = []
        towers = [
            Tower(5, 9, 21),
            Tower(18, 14, 76),
            Tower(2, 3, 4),
            Tower(13, 1, 61),
            Tower(7, 11, 83),
            Tower(12, 18, 33),
            Tower(9, 5, 17),
            Tower(1, 15, 69),
            Tower(16, 13, 32),
            Tower(0, 0, 5),
            Tower(14, 4, 88),
            Tower(3, 13, 58),
            Tower(8, 8, 25),
            Tower(19, 6, 73),
            Tower(6, 15, 49),
            Tower(11, 19, 91),
            Tower(4, 11, 40),
            Tower(17, 7, 2),
            Tower(10, 5, 78),
            Tower(15, 17, 15),
            Tower(5, 9, 21)
        ]
        m = 4
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)
    def test13(self):
        return_list = []
        return_list_greedy = []
        towers = [
            Tower(5, 10, 74),
            Tower(18, 4, 47),
            Tower(2, 13, 22),
            Tower(13, 7, 93),
            Tower(7, 16, 8),
            Tower(12, 3, 51),
            Tower(9, 14, 29),
            Tower(1, 6, 86),
            Tower(16, 1, 59),
            Tower(0, 11, 12),
            Tower(14, 17, 77),
            Tower(3, 2, 41),
            Tower(8, 18, 65),
            Tower(19, 9, 90),
            Tower(6, 5, 3),
            Tower(11, 15, 67),
            Tower(4, 1, 35),
            Tower(17, 10, 1),
            Tower(10, 16, 54),
            Tower(15, 8, 71),
            Tower(5, 10, 74)
        ]
        m = 5
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test14(self):
        return_list = []
        return_list_greedy = []
        towers = [
            Tower(5, 0, 94),
            Tower(18, 19, 61),
            Tower(2, 12, 39),
            Tower(13, 6, 14),
            Tower(7, 17, 70),
            Tower(12, 4, 82),
            Tower(9, 15, 44),
            Tower(1, 7, 26),
            Tower(16, 0, 56),
            Tower(0, 12, 98),
            Tower(14, 18, 16),
            Tower(3, 3, 33),
            Tower(8, 19, 68),
            Tower(19, 8, 88),
            Tower(6, 6, 48),
            Tower(11, 14, 17),
            Tower(4, 2, 80),
            Tower(17, 11, 4),
            Tower(10, 17, 25),
            Tower(15, 9, 72),
            Tower(5, 0, 94)
        ]
        m = 2
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    def test15(self):
        return_list_greedy = []
        towers = [
            Tower(5, 14, 23),
            Tower(18, 0, 71),
            Tower(2, 8, 16),
            Tower(13, 17, 92),
            Tower(7, 4, 60),
            Tower(12, 11, 36),
            Tower(9, 1, 84),
            Tower(1, 15, 49),
            Tower(16, 3, 75),
            Tower(0, 6, 32),
            Tower(14, 11, 57),
            Tower(3, 13, 29),
            Tower(8, 9, 91),
            Tower(19, 7, 8),
            Tower(6, 16, 64),
            Tower(11, 12, 22),
            Tower(4, 8, 68),
            Tower(17, 4, 96),
            Tower(10, 2, 55),
            Tower(15, 19, 19),
            Tower(5, 10, 35),
            Tower(18, 6, 80),
            Tower(2, 3, 1),
            Tower(13, 2, 79),
            Tower(7, 12, 56),
            Tower(12, 18, 88),
            Tower(9, 5, 52),
            Tower(1, 16, 45),
            Tower(16, 4, 76),
            Tower(0, 7, 20),
            Tower(14, 1, 74),
            Tower(3, 14, 43),
            Tower(8, 10, 21),
            Tower(19, 6, 93),
            Tower(6, 17, 38),
            Tower(11, 13, 5),
            Tower(4, 9, 72),
            Tower(17, 5, 89),
            Tower(10, 3, 17),
            Tower(15, 18, 62),
            Tower(5, 15, 31),
            Tower(18, 1, 97),
            Tower(2, 9, 58),
            Tower(13, 18, 13),
            Tower(7, 5, 77),
            Tower(12, 12, 30),
            Tower(9, 2, 83),
            Tower(1, 17, 7),
            Tower(16, 5, 41),
            Tower(0, 8, 67),
            Tower(14, 12, 54),
            Tower(3, 15, 87),
            Tower(8, 11, 2),
            Tower(19, 5, 24),
            Tower(6, 18, 70),
            Tower(11, 14, 86),
            Tower(4, 10, 46),
            Tower(17, 6, 63),
            Tower(10, 4, 11),
            Tower(15, 17, 28),
            Tower(5, 11, 50),
            Tower(18, 2, 82),
            Tower(2, 10, 4),
            Tower(13, 19, 27),
            Tower(7, 6, 74),
            Tower(12, 13, 19),
            Tower(9, 3, 61),
            Tower(1, 18, 99),
            Tower(16, 6, 40),
            Tower(0, 9, 85),
            Tower(14, 13, 15),
            Tower(3, 16, 90),
            Tower(8, 12, 37),
            Tower(19, 4, 53),
            Tower(6, 19, 96),
            Tower(11, 15, 33),
            Tower(4, 11, 5),
            Tower(17, 7, 79),
            Tower(10, 5, 20),
            Tower(15, 16, 49),
            Tower(5, 12, 18),
            Tower(18, 3, 64),
            Tower(2, 11, 85),
            Tower(13, 0, 7),
            Tower(7, 7, 45),
            Tower(12, 14, 24),
            Tower(9, 4, 77),
            Tower(1, 19, 82),
            Tower(16, 7, 1),
            Tower(0, 10, 65),
            Tower(14, 14, 81),
            Tower(3, 17, 59),
            Tower(8, 13, 32),
            Tower(19, 3, 68),
            Tower(6, 0, 89),
            Tower(11, 16, 14),
            Tower(4, 12, 69),
            Tower(17, 8, 42),
            Tower(10, 6, 23),
            Tower(15, 15, 98),
            Tower(5, 13, 56),
            Tower(18, 4, 31),
            Tower(2, 12, 46),
            Tower(13, 1, 76),
            Tower(7, 8, 12),
            Tower(12, 15, 60),
            Tower(9, 0, 6),
            Tower(1, 20, 51),
            Tower(16, 8, 84),
            Tower(0, 11, 25),
            Tower(14, 15, 41),
            Tower(3, 18, 71),
            Tower(8, 14, 99),
            Tower(19, 2, 15),
            Tower(6, 1, 73),
            Tower(11, 17, 52),
            Tower(4, 13, 97),
            Tower(17, 9, 88),
            Tower(10, 7, 54),
            Tower(15, 14, 21),
            Tower(5, 14, 39),
            Tower(18, 5, 26),
            Tower(2, 13, 17),
            Tower(13, 2, 64),
            Tower(7, 9, 93),
            Tower(12, 16, 48),
            Tower(9, 1, 10),
            Tower(1, 21, 78),
            Tower(16, 9, 62),
            Tower(0, 12, 36),
            Tower(14, 16, 83),
            Tower(3, 19, 55),
            Tower(8, 15, 4),
            Tower(19, 1, 72),
            Tower(6, 2, 20),
            Tower(11, 18, 47),
            Tower(4, 14, 2),
            Tower(17, 10, 65),
            Tower(10, 8, 43),
            Tower(15, 13, 80),
            Tower(5, 15, 97),
            Tower(18, 6, 67),
            Tower(2, 14, 30),
            Tower(13, 3, 1),
            Tower(7, 10, 58),
            Tower(12, 17, 82),
            Tower(9, 2, 38),
            Tower(1, 22, 11),
            Tower(16, 10, 79),
            Tower(0, 13, 45),
            Tower(14, 17, 22),
            Tower(3, 0, 78),
            Tower(8, 16, 52),
            Tower(19, 0, 28),
            Tower(6, 3, 63),
            Tower(11, 19, 9),
            Tower(4, 15, 87),
            Tower(17, 11, 5),
            Tower(10, 9, 72),
            Tower(15, 12, 58),
            Tower(5, 16, 39),
            Tower(18, 7, 14),
            Tower(2, 15, 98),
            Tower(13, 4, 16),
            Tower(14, 14, 81),
            Tower(3, 17, 59),
            Tower(8, 13, 32),
            Tower(19, 3, 68),
            Tower(6, 0, 89),
            Tower(11, 16, 14),
            Tower(4, 12, 69),
            Tower(17, 8, 42),
            Tower(10, 6, 23),
            Tower(15, 15, 98),
            Tower(5, 13, 56),
            Tower(18, 4, 31),
            Tower(2, 12, 46),
            Tower(13, 1, 76),
            Tower(7, 8, 12),
            Tower(12, 15, 60),
            Tower(9, 0, 6),
            Tower(1, 20, 51),
            Tower(16, 8, 84),
            Tower(0, 11, 25),
            Tower(14, 15, 41),
            Tower(3, 18, 71),
            Tower(8, 14, 99),
            Tower(19, 2, 15),
            Tower(6, 1, 73),
            Tower(11, 17, 52),
            Tower(4, 13, 97),
            Tower(17, 9, 88),
            Tower(10, 7, 54),
            Tower(15, 14, 21),
            Tower(5, 14, 39),
            Tower(18, 5, 26),
            Tower(2, 13, 17),
            Tower(13, 2, 64),
            Tower(7, 9, 93),
            Tower(12, 16, 48),
            Tower(9, 1, 10),
            Tower(1, 21, 78),
            Tower(16, 9, 62),
            Tower(0, 12, 36),
            Tower(14, 16, 83),
            Tower(3, 19, 55),
            Tower(8, 15, 4),
            Tower(19, 1, 72),
            Tower(6, 2, 20),
            Tower(11, 18, 47),
            Tower(4, 14, 2),
            Tower(17, 10, 65),
            Tower(10, 8, 43),
            Tower(15, 13, 80),
            Tower(5, 15, 97),
            Tower(18, 6, 67),
            Tower(2, 14, 30),
            Tower(13, 3, 1),
            Tower(7, 10, 58),
            Tower(12, 17, 82),
            Tower(9, 2, 38),
            Tower(1, 22, 11),
            Tower(16, 10, 79),
            Tower(0, 13, 45),
            Tower(14, 17, 22),
            Tower(3, 0, 78),
            Tower(8, 16, 52),
            Tower(19, 0, 28),
            Tower(6, 3, 63),
            Tower(11, 19, 9),
            Tower(4, 15, 87),
            Tower(17, 11, 5),
            Tower(10, 9, 72),
            Tower(15, 12, 58),
            Tower(5, 16, 39),
            Tower(18, 7, 14),
        ]
        m = 6
        greedy_rests = gr.find_rest_spots(0, None, m, 0, towers, return_list_greedy)

        self.assertAlmostEqual(8, greedy_rests)




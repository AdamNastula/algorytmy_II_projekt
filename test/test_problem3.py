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
            Tower(20, 3, 74)
        ]
        m = 3
        greedy_rests = 0
        gr.find_rest_spots(0, None, m, greedy_rests, towers, return_list_greedy)


        self.assertAlmostEqual(test_bruteforce(0, None, m, 0, towers, return_list), greedy_rests)

    # def test2(self):
    #     return_list = []
    #     towers = [
    #
    #         [1, 13, 78],
    #         [10, 19, 6],
    #         [23, 5, 89],
    #         [5, 29, 44],
    #         [17, 12, 57],
    #         [20, 7, 93],
    #         [14, 25, 60],
    #         [8, 30, 37],
    #         [5, 28, 33],
    #         [16, 21, 8],
    #         [29, 18, 73],
    #         [11, 9, 34],
    #         [3, 16, 82],
    #         [21, 14, 99],
    #         [7, 4, 24],
    #         [12, 8, 45]

    #     ]
    #     m = 2
    #
    #     self.assertAlmostEqual(bf.test_bruteforce(0, None, m, 0, towers, return_list), 0)
    #
    # def test3(self):
    #     return_list = []
    #     towers = [
    #         [7, 15, 93],
    #         [4, 20, 48],
    #         [12, 2, 19],
    #         [29, 9, 84],
    #         [6, 27, 37],
    #         [18, 11, 65],
    #         [3, 8, 52],
    #         [25, 47, 13],
    #         [4, 12, 31],
    #         [39, 22, 18],
    #         [45, 18, 50],
    #         [27, 30, 72],
    #         [17, 8, 57],
    #         [30, 42, 4],
    #         [6, 15, 53],
    #         [23, 9, 7],
    #         [12, 34, 38]

    #     ]
    #     m = 2
    #
    #     self.assertAlmostEqual(bf.test_bruteforce(0, None, m, 0, towers, return_list), 0)
    #
    # def test4(self):
    #     return_list = []
    #     towers = [
    #         [15, 4, 78],
    #         [19, 16, 45],
    #         [8, 25, 54],
    #         [2, 19, 88],
    #         [26, 12, 20],
    #         [9, 6, 61],
    #         [11, 28, 47],
    #         [1, 13, 78],
    #         [10, 19, 6],
    #         [23, 5, 89],
    #         [45, 18, 50],
    #         [27, 30, 72],
    #         [17, 8, 57],
    #         [30, 42, 4],
    #         [6, 15, 53],
    #         [22, 14, 73],
    #         [10, 30, 6],
    #         [5, 13, 91],

    #     ]
    #     m = 2
    #
    #     self.assertAlmostEqual(bf.test_bruteforce(0, None, m, 0, towers, return_list), 0)
import unittest

import problem2.Boyer_Moore as bm

class TestBM(unittest.TestCase):
    def test1(self):
        self.assertAlmostEqual([5, 13], bm.bm_search("ABCDBABCABBCDABCAB", "ABCAB", ['A', 'B', 'C', 'D']))

    def test2(self):
        self.assertAlmostEqual([5, 20, 38, 63], bm.bm_search("AABBABABAAAABBBABBAABABAABBBBBAABBAAAABABAABBABBBBBABBABBBABABBBABAABBBAABBABBA", "BABAA", ['A', 'B']))

    def test3(self):
        self.assertAlmostEqual([], bm.bm_search("AAAABAAACCCCACACACBBAAAAAAAAAAAADDDDDAAAAADADADADACCCCCCCCCCCAAAABBBBBBBBBBB", "DACA", ['A', 'B', 'C', 'D']))

    def test4(self):
        self.assertAlmostEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], bm.bm_search("VVVVVVVVVVVVVVVVVVVV", "V", ['V']))

    def test5(self):
        self.assertAlmostEqual([], bm.bm_search("AAAABABABABAAABB", "AC", ['A', 'B']))

    def test6(self):
        self.assertAlmostEqual([70], bm.bm_search("ABCDEFGHJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVWABCDEFGHIJKLMNOPQRSTUVWYZXYZ", "XYZ", ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    def test7(self):
        self.assertAlmostEqual([0, 5, 18], bm.bm_search("123@#123@#123456@#123@#123@#", "123@#123", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#']))
    def test8(self):
        self.assertAlmostEqual([5,8], bm.bm_search("ABCABXYZXYZXYZCBA", "XYZXYZ", ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
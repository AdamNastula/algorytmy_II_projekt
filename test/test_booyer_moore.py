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
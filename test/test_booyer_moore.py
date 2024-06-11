import unittest

import problem2.Boyer_Moore as bm

class TestBM(unittest.TestCase):
    def test1(self):
        self.assertAlmostEqual([5, 13], bm.bm_search("ABCDBABCABBCDABCAB", "ABCAB", ['A', 'B', 'C', 'D']))

    def test2(self):
        self.assertAlmostEqual([5, 20, 38, 63], bm.bm_search("AABBABABAAAABBBABBAABABAABBBBBAABBAAAABABAABBABBBBBABBABBBABABBBABAABBBAABBABBA", "BABAA", ['A', 'B']))

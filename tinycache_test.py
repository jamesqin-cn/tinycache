# -*- coding: utf-8 -*-
__author__ = 'james'

import unittest
import time
from tinycache.tinycache import WithCache

@WithCache(3)
def Add(a, b):
    return a + b

class Test_CacheUtil(unittest.TestCase):
    def test_WithCache(self):
        s1 = Add(1, 2)
        s2 = Add(1, 2)
        self.assertEqual(s1, 3)
        self.assertEqual(s1, s2)

if __name__ == '__main__':
    unittest.main()

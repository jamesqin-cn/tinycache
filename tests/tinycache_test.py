# -*- coding: utf-8 -*-
__author__ = 'james'

import unittest
import time
import logging
from tinycache import WithCache

@WithCache(5)
def Add(a, b):
    return a + b

class Foo():
    @WithCache(5)
    def Bar(self, a, b):
        return a - b

class Test_CacheUtil(unittest.TestCase):
    def test_WithCacheInFun(self):
        s1 = Add(1, 2)
        s2 = Add(1, 2)
        self.assertEqual(s1, 3)
        self.assertEqual(s1, s2)

    def test_WithCacheInMethod(self):
        s1 = Foo().Bar(3, 1)
        s2 = Foo().Bar(3, 1)
        self.assertEqual(s1, 2)
        self.assertEqual(s1, s2)

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    unittest.main()

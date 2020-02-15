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
    def __init__(self, a):
        self.a = a

    @WithCache(5)
    def Bar(self, b):
        return self.a - b

class Test_CacheUtil(unittest.TestCase):
    def test_WithCacheInFun(self):
        s1 = Add(1, 2)
        s2 = Add(1, 2)
        self.assertEqual(s1, 3)
        self.assertEqual(s1, s2)

    def test_WithCacheInMethod(self):
        s1 = Foo(3).Bar(1)
        s2 = Foo(4).Bar(1)
        s3 = Foo(3).Bar(1)
        self.assertEqual(s1, 2)
        self.assertEqual(s2, 3)
        self.assertEqual(s3, 2)

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    unittest.main()

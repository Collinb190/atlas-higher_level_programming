#!/usr/bin/python3
"""Unittest for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    def testRegularCase(self):
        self.assertEqual(max_integer([1 ,2 ,3 ,4]), 4)

    def testUnorderedCase(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def testEmptyList(self):
        self.assertIsNone(max_integer([]))

    def testSigleValueList(self):
        self.assertEqual(max_integer([5]), 5)

    def testNegativeCase(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def testMixedCase(self):
        self.assertEqual(max_integer([2, -7, 0, 10, -3]), 10)

if __name__ == '__main__':
    unittest.main()

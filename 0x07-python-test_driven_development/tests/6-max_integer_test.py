#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_randomVals(self):
        self.assertEqual(max_integer([2, 5, 10]), 10)
        self.assertEqual(max_integer([-100, -5, 10]), 10)
        self.assertEqual(max_integer([-0, +0, 10]), 10)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([10, 10.5, 10.9]), 10.9)

    def test_raisedErrors(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "6"])
        self.assertRaises(TypeError, max_integer, [6, None])
        self.assertRaises(TypeError, max_integer, [6, 4, [2, 4]])


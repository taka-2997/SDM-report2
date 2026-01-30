#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):

    # 正常系（同値分割）
    def test_normal_values(self):
        self.assertEqual(21, calc(3, 7))
        self.assertEqual(1, calc(1, 1))
        self.assertEqual(998001, calc(999, 999))

    # 境界値テスト（下限・上限）
    def test_boundary_values(self):
        self.assertEqual(-1, calc(0, 5))
        self.assertEqual(-1, calc(1000, 5)) 
        self.assertEqual(-1, calc(5, 0))
        self.assertEqual(-1, calc(5, 1000))

    # 異常系：文字列入力（同値分割）
    def test_invalid_type_string(self):
        self.assertEqual(-1, calc('a', 'b'))
        self.assertEqual(-1, calc('1', 5))

    # 異常系：小数入力（同値分割）
    def test_invalid_type_float(self):
        self.assertEqual(-1, calc(0.1, 999))
        self.assertEqual(-1, calc(5, 3.5))

    # 異常系：負の数
    def test_negative_values(self):
        self.assertEqual(-1, calc(-1, 5))
        self.assertEqual(-1, calc(5, -10))

import unittest
from fractions import Fraction

from timedata.color import make, COLORS


class MakeTest(unittest.TestCase):
    def test_color(self):
        self.assertEqual(make.color('red'), COLORS.red)
        self.assertEqual(make.color((255, 0, 0)), COLORS.red)
        self.assertEqual(make.color(255), COLORS.white)

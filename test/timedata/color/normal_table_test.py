import unittest
from timedata.color.normal_table import NormalTable


class NormalTableTest(unittest.TestCase):
    def test_simple(self):
        colors = NormalTable()
        self.assertEqual(colors.to_color('RED'), (1, 0, 0))
        self.assertEqual(colors.to_string((1, 0, 0)), 'Red')
        with self.assertRaises(ValueError):
            colors.to_color('rod')

    def test_all_named_colors(self):
        colors = NormalTable()
        all_colors = sorted(colors)
        self.assertEqual(962, len(all_colors))
        actual = all_colors[:4] + all_colors[-4:]
        expected = [
            'Absolute Zero',
            'Acid green',
            'Aero',
            'Aero blue',
            'Yellow-green (Color Wheel)',
            'Yellow-green (Crayola)',
            'Zaffre',
            'Zomp']

        self.assertEqual(actual, expected)

import unittest
from timedata.color import table, COLORS


class TableTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(table.get_color('RED'), (255, 0, 0))
        self.assertEqual(table.get_name((255, 0, 0)), 'Red')
        self.assertIs(table.get_color('rod'), None)

    def test_all_named_colors(self):
        all_colors = sorted(COLORS)
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

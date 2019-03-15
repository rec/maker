import unittest
from timedata.color import table


class TableTest(unittest.TestCase):
    def test_simple(self):
        colors = table.Table()
        self.assertEqual(colors.name_to_color('RED'), (255, 0, 0))
        self.assertEqual(colors.color_to_name((255, 0, 0)), 'Red')
        self.assertIs(colors.get_color('rod'), None)

    def test_all_named_colors(self):
        colors = table.Table()
        all_colors = sorted(colors.colors)
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

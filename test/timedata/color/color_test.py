import unittest

from timedata.color import COLORS, names, table


class NamesTest(unittest.TestCase):
    def test_colors(self):
        self.assertEqual(COLORS.red, (255, 0, 0))
        self.assertEqual(names.color_to_name((0, 0, 0)), 'Black')
        self.assertEqual(COLORS.BurntSienna, (0xe9, 0x74, 0x51))
        self.assertEqual(
            names.color_to_name((0xe9, 0x74, 0x51)), 'Burnt sienna')

    def test_toggle(self):
        self.assertEqual(names.toggle('red'), '(255, 0, 0)')
        self.assertEqual(names.toggle('(255, 0, 0)'), 'Red')
        self.assertEqual(names.toggle('(0, 0, 0)'), 'Black')
        self.assertEqual(names.toggle('(0xe9, 0x74, 0x51)'), 'Burnt sienna')

        self.assertEqual(names.toggle('#e97451'), 'Burnt sienna')
        self.assertEqual(names.toggle('0xe97451'), 'Burnt sienna')

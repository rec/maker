import unittest

from timedata.color import COLORS, names, table


class NamesTest(unittest.TestCase):
    def test_colors(self):
        self.assertEqual(COLORS.red, (255, 0, 0))
        self.assertEqual(names.color_to_name((0, 0, 0)), 'black')
        self.assertEqual(
            names.color_to_name((0x8a, 0x36, 0x0f)), 'burnt sienna')

    def test_toggle(self):
        self.assertEqual(names.toggle('red'), '(255, 0, 0)')
        self.assertEqual(names.toggle('(255, 0, 0)'), 'red')
        self.assertEqual(names.toggle('(0, 0, 0)'), 'black')
        self.assertEqual(names.toggle('(0x8a, 0x36, 0x0f)'), 'burnt sienna')

        self.assertEqual(names.toggle('#8a360f'), 'burnt sienna')
        self.assertEqual(names.toggle('0x8a360f'), 'burnt sienna')

import unittest

from timedata.color import table, COLORS


class NamesTest(unittest.TestCase):
    def test_colors(self):
        t = table.Table()
        self.assertEqual(COLORS.red, (255, 0, 0))
        self.assertEqual(t.color_to_name((0, 0, 0)), 'Black')
        self.assertEqual(COLORS.BurntSienna, (0xe9, 0x74, 0x51))
        self.assertEqual(t.color_to_name((0xe9, 0x74, 0x51)), 'Burnt sienna')

    def test_toggle(self):
        toggle = table.Table().toggle
        self.assertEqual(toggle('red'), '(255, 0, 0)')
        self.assertEqual(toggle('(255, 0, 0)'), 'Red')
        self.assertEqual(toggle('(0, 0, 0)'), 'Black')
        self.assertEqual(toggle('(0xe9, 0x74, 0x51)'), 'Burnt sienna')

        self.assertEqual(toggle('#e97451'), 'Burnt sienna')
        self.assertEqual(toggle('0xe97451'), 'Burnt sienna')

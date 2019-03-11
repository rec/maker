import unittest
from timedata.color import table, COLORS


class TableTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(table.get_color('RED'), (255, 0, 0))
        self.assertEqual(table.get_name((255, 0, 0)), 'red')
        self.assertIs(table.get_color('rod'), None)

    def test_new_colors(self):
        self.assertIs(table.get_color('frog'), None)

        frog = 1, 255, 2
        table.set_user_colors({'Frog': frog})
        try:
            self.assertEqual(table.get_color('RED'), (255, 0, 0))
            self.assertEqual(table.get_name((255, 0, 0)), 'red')
            self.assertEqual(table.get_color('frog'), frog)
            self.assertEqual(table.get_name(frog), 'Frog')
        finally:
            table.set_user_colors({})

        self.assertIs(table.get_color('frog'), None)

    def test_override_colors(self):
        self.assertEqual(table.get_color('RED'), (255, 0, 0))
        self.assertEqual(table.get_name((255, 0, 0)), 'red')

        wrong_red = 6, 6, 6
        table.set_user_colors({'red': wrong_red})
        try:
            self.assertEqual(table.get_color('RED'), wrong_red)
            self.assertEqual(table.get_name(wrong_red), 'red')
            # Ooops! but what else to do?
            self.assertEqual(table.get_name((255, 0, 0)), 'red')
        finally:
            table.set_user_colors({})

        self.assertEqual(table.get_color('RED'), (255, 0, 0))
        self.assertEqual(table.get_name((255, 0, 0)), 'red')

    def test_all_named_colors(self):
        all_colors = sorted(COLORS)
        self.assertEqual(476, len(all_colors))
        actual = all_colors[:4] + all_colors[-4:]
        expected = [
            ('aliceblue', (240, 248, 255)),
            ('antiquewhite', (250, 235, 215)),
            ('antiquewhite1', (255, 239, 219)),
            ('antiquewhite2', (238, 223, 204)),
            ('yellow2', (238, 238, 0)),
            ('yellow3', (205, 205, 0)),
            ('yellow4', (139, 139, 0)),
            ('yellowgreen', (154, 205, 50))]

        self.assertEqual(actual, expected)

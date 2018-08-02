import unittest
from controly import fill


class Bar:
    def __eq__(self, other):
        return isinstance(other, Bar)


class FillTest(unittest.TestCase):
    def test_trivial(self):
        fill.fill({})

    def test_simple(self):
        a = {'typename': 'test.controly.fill_test.Bar'}
        expected = dict(a, _class=Bar, _object=Bar())

        fill.fill(a)
        self.assertEquals(a, expected)

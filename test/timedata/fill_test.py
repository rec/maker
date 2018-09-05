import unittest
from timedata import fill


class Bar:
    @classmethod
    def __eq__(cls, other):
        return isinstance(other, cls)


class BazSimple(Bar):
    TIMEDATA_ATTRIBUTES = ['foo', 'bar']


class Baz(Bar):
    TIMEDATA_ATTRIBUTES = {
        'foo': True,
        'bar': lambda x: print('!!!') or (1 + x)
    }


class FillTest(unittest.TestCase):
    def test_trivial(self):
        fill.fill({})

    def test_simple(self):
        a = {'typename': 'test.timedata.fill_test.Bar', 'foo': 'foo', 'bar': 2}
        expected = dict(a, _class=Bar, _object=Bar())

        fill.fill(a)
        self.assertEquals(a, expected)
        self.assertEquals(a['_object'].foo, 'foo')
        self.assertEquals(a['_object'].bar, 2)

    def test_attributes_simple(self):
        a = {'typename': 'test.timedata.fill_test.BazSimple',
             'foo': 'foo', 'bar': 2}
        expected = dict(a, _class=BazSimple, _object=BazSimple())
        fill.fill(a)
        self.assertEquals(a, expected)
        self.assertEquals(a['_object'].foo, 'foo')
        self.assertEquals(a['_object'].bar, 2)

    def test_attributes(self):
        a = {'typename': 'test.timedata.fill_test.Baz',
             'foo': 'foo', 'bar': 2}
        expected = dict(a, _class=Baz, _object=Baz())
        fill.fill(a)
        self.assertEquals(a, expected)
        self.assertEquals(a['_object'].foo, 'foo')
        self.assertEquals(a['_object'].bar, 2)

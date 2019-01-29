import unittest
from timedata import serialize

TESTS = 'a', ['b', 1], True, None, {},


class SerializeTest(unittest.TestCase):
    def test_all(self):
        for t in TESTS:
            dump = serialize.dump(t)
            load = serialize.load(dump)
            self.assertEquals(load, t)

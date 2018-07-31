import unittest
from control import data

TESTS = 'a', ['b', 1], True, None, {},


class DataTest(unittest.TestCase):
    def test_all(self):
        for t in TESTS:
            dump = data.dump(t)
            load = data.load(dump)
            self.assertEquals(load, t)

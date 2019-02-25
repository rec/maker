import os, unittest
from . import_all import import_all

BLACKLIST = []
DONT_WARN = ['timedata.control.keyboard']
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class ImportAllTest(unittest.TestCase):
    def test_all(self):
        _, fail = import_all(PROJECT_ROOT, 'timedata', BLACKLIST, DONT_WARN)
        self.assertEqual(fail, [])

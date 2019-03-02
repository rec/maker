import os, platform, unittest
from . import_all import import_all

IS_TRAVIS = os.getenv('TRAVIS', '').lower().startswith('t')
BLACKLIST = ['timedata.control.keyboard'] if IS_TRAVIS else []
DONT_WARN = 'timedata.control.keyboard', 'timedata.instruments.dmx.laser.laser'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class ImportAllTest(unittest.TestCase):
    def test_all(self):
        _, fail = import_all(PROJECT_ROOT, 'timedata', BLACKLIST, DONT_WARN)
        self.assertEqual(fail, [])

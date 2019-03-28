import os, unittest
from . import_all import import_all

IS_TRAVIS = os.getenv('TRAVIS', '').lower().startswith('t')
BLACKLIST = (['timedata.control.keyboard'] if IS_TRAVIS else []) + [
    'timedata.instruments.dmx.laser.laser',
    'timedata.ui.ui_test',
    'timedata.instruments.dmx.laser.window_test',
    'timedata.instruments.dmx.laser.window_test2']
DONT_WARN = 'timedata.control.keyboard',
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class ImportAllTest(unittest.TestCase):
    def DONT_test_all(self):
        _, fail = import_all(PROJECT_ROOT, 'timedata', BLACKLIST, DONT_WARN)
        self.assertEqual(fail, [])

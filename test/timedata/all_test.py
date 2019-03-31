import os, unittest
from . import_all import import_all

IS_TRAVIS = os.getenv('TRAVIS', '').lower().startswith('t')
BLACKLIST = [
    'timedata.control.keyboard',
    'timedata.instruments.laser.abs_lfo_fader',
    'timedata.instruments.laser.dmx_levels',
    'timedata.instruments.laser.laser',
    'timedata.instruments.laser.loose_buttons',
    'timedata.instruments.laser.main',
    'timedata.instruments.laser.one_laser',
    'timedata.instruments.laser.selectors',
    'timedata.instruments.laser.wombat',
    'timedata.instruments.old_laser.six_faders',
    'timedata.instruments.old_laser.six_lasers',
    'timedata.instruments.old_laser.top_window',
    'timedata.ui.bang',
    'timedata.ui.box_layout',
    'timedata.ui.int_entry',
    'timedata.ui.int_slider',
    'timedata.ui.notes_held',
    'timedata.ui.selector',
    'timedata.ui.switch_button',
    'timedata.ui.ui_test']
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class ImportAllTest(unittest.TestCase):
    maxDiff = 5000

    def test_all(self):
        _, fail = import_all(PROJECT_ROOT, 'timedata', [])
        fail = [m for (m, e) in fail]
        self.assertEqual(fail, BLACKLIST)

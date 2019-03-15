"""
Convert back and forth between colors and string names.
"""

import numbers
from . import table

COLORS = table.Table()

name_to_color = COLORS.name_to_color
color_to_name = COLORS.color_to_name
toggle = COLORS.toggle
to_color = COLORS.to_color

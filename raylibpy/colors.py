import raylibpy.core as core
from typing import Final

__all__ = [
    'LIGHTGRAY',
    'GRAY',
    'DARKGRAY',
    'YELLOW',
    'GOLD',
    'ORANGE',
    'PINK',
    'RED',
    'MAROON',
    'GREEN',
    'LIME',
    'DARKGREEN',
    'SKYBLUE',
    'BLUE',
    'DARKBLUE',
    'PURPLE',
    'VIOLET',
    'DARKPURPLE',
    'BEIGE',
    'BROWN',
    'DARKBROWN',
    'WHITE',
    'BLACK',
    'BLANK',
    'MAGENTA',
    'RAYWHITE',
]

# ---------------------------------------------------------
# region COLOR CONSTANTS

LIGHTGRAY: Final[core.Color] = core.Color(200, 200, 200, 255)  # Light Gray
GRAY: Final[core.Color] = core.Color(130, 130, 130, 255)  # Gray
DARKGRAY: Final[core.Color] = core.Color(80, 80, 80, 255)  # Dark Gray
YELLOW: Final[core.Color] = core.Color(253, 249, 0, 255)  # Yellow
GOLD: Final[core.Color] = core.Color(255, 203, 0, 255)  # Gold
ORANGE: Final[core.Color] = core.Color(255, 161, 0, 255)  # Orange
PINK: Final[core.Color] = core.Color(255, 109, 194, 255)  # Pink
RED: Final[core.Color] = core.Color(230, 41, 55, 255)  # Red
MAROON: Final[core.Color] = core.Color(190, 33, 55, 255)  # Maroon
GREEN: Final[core.Color] = core.Color(0, 228, 48, 255)  # Green
LIME: Final[core.Color] = core.Color(0, 158, 47, 255)  # Lime
DARKGREEN: Final[core.Color] = core.Color(0, 117, 44, 255)  # Dark Green
SKYBLUE: Final[core.Color] = core.Color(102, 191, 255, 255)  # Sky Blue
BLUE: Final[core.Color] = core.Color(0, 121, 241, 255)  # Blue
DARKBLUE: Final[core.Color] = core.Color(0, 82, 172, 255)  # Dark Blue
PURPLE: Final[core.Color] = core.Color(200, 122, 255, 255)  # Purple
VIOLET: Final[core.Color] = core.Color(135, 60, 190, 255)  # Violet
DARKPURPLE: Final[core.Color] = core.Color(112, 31, 126, 255)  # Dark Purple
BEIGE: Final[core.Color] = core.Color(211, 176, 131, 255)  # Beige
BROWN: Final[core.Color] = core.Color(127, 106, 79, 255)  # Brown
DARKBROWN: Final[core.Color] = core.Color(76, 63, 47, 255)  # Dark Brown
WHITE: Final[core.Color] = core.Color(255, 255, 255, 255)  # White
BLACK: Final[core.Color] = core.Color(0, 0, 0, 255)  # Black
BLANK: Final[core.Color] = core.Color(0, 0, 0, 0)  # Blank (Transparent)
MAGENTA: Final[core.Color] = core.Color(255, 0, 255, 255)  # Magenta
RAYWHITE: Final[core.Color] = core.Color(245, 245, 245, 255)  # My own White (raylib logo)

# endregion (color constants)
# ---------------------------------------------------------

import os
from ctypes import CDLL, WinDLL

__all__ = [
    'rl'
]

rl = CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'raylib.dll'))
# rl = WinDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'raylib.dll'))

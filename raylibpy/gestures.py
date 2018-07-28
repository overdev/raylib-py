from structures import *
from ctypes import byref
from typing import Tuple
from library import rl as _rl

__all__ = [
    'set_gestures_enabled',
    'is_gesture_detected',
    'get_gesture_detected',
    'get_touch_points_count',
    'get_gesture_hold_duration',
    'get_gesture_drag_vector',
    'get_gesture_drag_angle',
    'get_gesture_pinch_vector',
    'get_gesture_pinch_angle',

    'byref',
]


_NOARGS = []


# -----------------------------------------------------------------------------------
# Gestures and Touch Handling Functions (Module: gestures)
# -----------------------------------------------------------------------------------
_rl.SetGesturesEnabled.argtypes = [Uint]
_rl.SetGesturesEnabled.restype = None
def set_gestures_enabled(gesture_flags: int) -> None:
    '''Enable a set of gestures using flags'''
    return _rl.SetGesturesEnabled(gesture_flags)


_rl.IsGestureDetected.argtypes = [Int]
_rl.IsGestureDetected.restype = Bool
def is_gesture_detected(gesture: int) -> bool:
    '''Check if a gesture have been detected'''
    return _rl.IsGestureDetected(gesture)


_rl.GetGestureDetected.argtypes = _NOARGS
_rl.GetGestureDetected.restype = Int
def get_gesture_detected() -> int:
    '''Get latest detected gesture'''
    return _rl.GetGestureDetected()


_rl.GetTouchPointsCount.argtypes = _NOARGS
_rl.GetTouchPointsCount.restype = Int
def get_touch_points_count() -> int:
    '''Get touch points count'''
    return _rl.GetTouchPointsCount()


_rl.GetGestureHoldDuration.argtypes = _NOARGS
_rl.GetGestureHoldDuration.restype = Float
def get_gesture_hold_duration() -> float:
    '''Get gesture hold time in milliseconds'''
    return _rl.GetGestureHoldDuration()


_rl.GetGestureDragVector.argtypes = _NOARGS
_rl.GetGestureDragVector.restype = Vector2
def get_gesture_drag_vector() -> Vector2:
    '''Get gesture drag vector'''
    return _rl.GetGestureDragVector()


_rl.GetGestureDragAngle.argtypes = _NOARGS
_rl.GetGestureDragAngle.restype = Float
def get_gesture_drag_angle() -> float:
    '''Get gesture drag angle'''
    return _rl.GetGestureDragAngle()


_rl.GetGesturePinchVector.argtypes = _NOARGS
_rl.GetGesturePinchVector.restype = Vector2
def get_gesture_pinch_vector() -> Vector2:
    '''Get gesture pinch delta'''
    return _rl.GetGesturePinchVector()


_rl.GetGesturePinchAngle.argtypes = _NOARGS
_rl.GetGesturePinchAngle.restype = Float
def get_gesture_pinch_angle() -> float:
    '''Get gesture pinch angle'''
    return _rl.GetGesturePinchAngle()

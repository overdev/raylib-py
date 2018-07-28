from library import rl as _rl
from structures import *
from ctypes import byref
from typing import Tuple


__all__ = [
    'set_camera_mode',
    'update_camera',
    'set_camera_pan_control',
    'set_camera_alt_control',
    'set_camera_smooth_zoom_control',
    'set_camera_move_controls',
]

_NOARGS = []


# -----------------------------------------------------------------------------------
# Camera System Functions (Module: camera)
# -----------------------------------------------------------------------------------
_rl.SetCameraMode.argtypes = [Camera, Int]
_rl.SetCameraMode.restype = None
def set_camera_mode(camera: Camera, mode: int) -> None:
    '''Set camera mode (multiple camera modes available)'''
    return _rl.SetCameraMode(camera, mode)


_rl.UpdateCamera.argtypes = [CameraPtr]
_rl.UpdateCamera.restype = None
def update_camera(camera: CameraPtr) -> None:
    '''Update camera position for selected mode'''
    return _rl.UpdateCamera(camera)


_rl.SetCameraPanControl.argtypes = [Int]
_rl.SetCameraPanControl.restype = None
def set_camera_pan_control(pan_key: int) -> None:
    '''Set camera pan key to combine with mouse movement (free camera)'''
    return _rl.SetCameraPanControl(pan_key)


_rl.SetCameraAltControl.argtypes = [Int]
_rl.SetCameraAltControl.restype = None
def set_camera_alt_control(alt_key: int) -> None:
    '''Set camera alt key to combine with mouse movement (free camera)'''
    return _rl.SetCameraAltControl(alt_key)


_rl.SetCameraSmoothZoomControl.argtypes = [Int]
_rl.SetCameraSmoothZoomControl.restype = None
def set_camera_smooth_zoom_control(sz_key: int) -> None:
    '''Set camera smooth zoom key to combine with mouse (free camera)'''
    return _rl.SetCameraSmoothZoomControl(sz_key)


_rl.SetCameraMoveControls.argtypes = [Int, Int, Int, Int, Int, Int]
_rl.SetCameraMoveControls.restype = None
def set_camera_move_controls(front_key: int, back_ey: int, right_key: int,
                             left_key: int, up_key: int, down_key: int) -> None:
    '''Set camera move controls (1st person and 3rd person cameras)'''
    return _rl.SetCameraMoveControls(front_key, back_ey, right_key, left_key, up_key, down_key)

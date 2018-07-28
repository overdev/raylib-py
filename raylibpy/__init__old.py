# __init__.py

import os
from math import pi as PI
from ctypes import (
    c_bool,
    c_char_p,
    c_byte,
    c_ubyte,
    c_int,
    c_int32,
    c_uint,
    c_uint32,
    c_short,
    c_ushort,
    c_void_p,
    c_ssize_t,
    c_size_t,
    c_float,
    c_double,
    POINTER,
    CDLL,
    Structure,
    byref
)

_raylib = CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'raylib.dll'))


def _ct(s):
    argtypes = []
    argtp = None

    if s == '':
        return argtypes

    sig = s + '_'
    for ch in sig:
        if ch is '*':
            if argtp is None:
                raise ValueError('Pointer marker without preceding type.')
            argtp = POINTER(argtp)
            continue
        elif ch is '_':
            if argtp:
                argtypes.append(argtp)
            return argtypes

        if argtp is not None:
            argtypes.append(argtp)
        argtp = {
            '?': c_bool,
            'c': c_char_p,
            'b': c_byte,
            'B': c_ubyte,
            'h': c_short,
            'H': c_ushort,
            'i': c_int32,
            'I': c_uint32,
            'f': c_float,
            'd': c_double,
            'p': POINTER(c_ubyte),
            'P': c_void_p,
            'n': c_ssize_t,
            'N': c_size_t,
        }[ch]


_NOARGS = []

# CONSTANT DEFINITIONS
# -------------------------------------------------------------------

DEG2RAD = PI / 180.
RAD2DEG = 180. / PI

FLAG_SHOW_LOGO = 1
FLAG_FULLSCREEN_MODE = 2
FLAG_WINDOW_RESIZABLE = 4
FLAG_WINDOW_UNDECORATED = 8
FLAG_WINDOW_TRANSPARENT = 16
FLAG_MSAA_4X_HINT = 32
FLAG_VSYNC_HINT = 64


KEY_SPACE = 32
KEY_ESCAPE = 256
KEY_ENTER = 257
KEY_TAB = 258
KEY_BACKSPACE = 259
KEY_INSERT = 260
KEY_DELETE = 261
KEY_RIGHT = 262
KEY_LEFT = 263
KEY_DOWN = 264
KEY_UP = 265
KEY_PAGE_UP = 266
KEY_PAGE_DOWN = 267
KEY_HOME = 268
KEY_END = 269
KEY_CAPS_LOCK = 280
KEY_SCROLL_LOCK = 281
KEY_NUM_LOCK = 282
KEY_PRINT_SCREEN = 283
KEY_PAUSE = 284
KEY_F1 = 290
KEY_F2 = 291
KEY_F3 = 292
KEY_F4 = 293
KEY_F5 = 294
KEY_F6 = 295
KEY_F7 = 296
KEY_F8 = 297
KEY_F9 = 298
KEY_F10 = 299
KEY_F11 = 300
KEY_F12 = 301
KEY_LEFT_SHIFT = 340
KEY_LEFT_CONTROL = 341
KEY_LEFT_ALT = 342
KEY_RIGHT_SHIFT = 344
KEY_RIGHT_CONTROL = 345
KEY_RIGHT_ALT = 346
KEY_GRAVE = 96
KEY_SLASH = 47
KEY_BACKSLASH = 92

# Keyboard Alpha Numeric Keys
KEY_ZERO = 48
KEY_ONE = 49
KEY_TWO = 50
KEY_THREE = 51
KEY_FOUR = 52
KEY_FIVE = 53
KEY_SIX = 54
KEY_SEVEN = 55
KEY_EIGHT = 56
KEY_NINE = 57
KEY_A = 65
KEY_B = 66
KEY_C = 67
KEY_D = 68
KEY_E = 69
KEY_F = 70
KEY_G = 71
KEY_H = 72
KEY_I = 73
KEY_J = 74
KEY_K = 75
KEY_L = 76
KEY_M = 77
KEY_N = 78
KEY_O = 79
KEY_P = 80
KEY_Q = 81
KEY_R = 82
KEY_S = 83
KEY_T = 84
KEY_U = 85
KEY_V = 86
KEY_W = 87
KEY_X = 88
KEY_Y = 89
KEY_Z = 90

# Android Physical Buttons
KEY_BACK = 4
KEY_MENU = 82
KEY_VOLUME_UP = 24
KEY_VOLUME_DOWN = 25

# Mouse Buttons
MOUSE_LEFT_BUTTON = 0
MOUSE_RIGHT_BUTTON = 1
MOUSE_MIDDLE_BUTTON = 2

# Touch points registered
MAX_TOUCH_POINTS = 2

# Gamepad Number
GAMEPAD_PLAYER1 = 0
GAMEPAD_PLAYER2 = 1
GAMEPAD_PLAYER3 = 2
GAMEPAD_PLAYER4 = 3

# Gamepad Buttons/Axis

# PS3 USB Controller Buttons
GAMEPAD_PS3_BUTTON_TRIANGLE = 0
GAMEPAD_PS3_BUTTON_CIRCLE = 1
GAMEPAD_PS3_BUTTON_CROSS = 2
GAMEPAD_PS3_BUTTON_SQUARE = 3
GAMEPAD_PS3_BUTTON_L1 = 6
GAMEPAD_PS3_BUTTON_R1 = 7
GAMEPAD_PS3_BUTTON_L2 = 4
GAMEPAD_PS3_BUTTON_R2 = 5
GAMEPAD_PS3_BUTTON_START = 8
GAMEPAD_PS3_BUTTON_SELECT = 9
GAMEPAD_PS3_BUTTON_UP = 24
GAMEPAD_PS3_BUTTON_RIGHT = 25
GAMEPAD_PS3_BUTTON_DOWN = 26
GAMEPAD_PS3_BUTTON_LEFT = 27
GAMEPAD_PS3_BUTTON_PS = 12

# PS3 USB Controller Axis
GAMEPAD_PS3_AXIS_LEFT_X = 0
GAMEPAD_PS3_AXIS_LEFT_Y = 1
GAMEPAD_PS3_AXIS_RIGHT_X = 2
GAMEPAD_PS3_AXIS_RIGHT_Y = 5
GAMEPAD_PS3_AXIS_L2 = 3       # [1..-1] (pressure-level)
GAMEPAD_PS3_AXIS_R2 = 4       # [1..-1] (pressure-level)

# Xbox360 USB Controller Buttons
GAMEPAD_XBOX_BUTTON_A = 0
GAMEPAD_XBOX_BUTTON_B = 1
GAMEPAD_XBOX_BUTTON_X = 2
GAMEPAD_XBOX_BUTTON_Y = 3
GAMEPAD_XBOX_BUTTON_LB = 4
GAMEPAD_XBOX_BUTTON_RB = 5
GAMEPAD_XBOX_BUTTON_SELECT = 6
GAMEPAD_XBOX_BUTTON_START = 7
GAMEPAD_XBOX_BUTTON_UP = 10
GAMEPAD_XBOX_BUTTON_RIGHT = 11
GAMEPAD_XBOX_BUTTON_DOWN = 12
GAMEPAD_XBOX_BUTTON_LEFT = 13
GAMEPAD_XBOX_BUTTON_HOME = 8

# Android Gamepad Controller (SNES CLASSIC)
GAMEPAD_ANDROID_DPAD_UP = 19
GAMEPAD_ANDROID_DPAD_DOWN = 20
GAMEPAD_ANDROID_DPAD_LEFT = 21
GAMEPAD_ANDROID_DPAD_RIGHT = 22
GAMEPAD_ANDROID_DPAD_CENTER = 23

GAMEPAD_ANDROID_BUTTON_A = 96
GAMEPAD_ANDROID_BUTTON_B = 97
GAMEPAD_ANDROID_BUTTON_C = 98
GAMEPAD_ANDROID_BUTTON_X = 99
GAMEPAD_ANDROID_BUTTON_Y = 100
GAMEPAD_ANDROID_BUTTON_Z = 101
GAMEPAD_ANDROID_BUTTON_L1 = 102
GAMEPAD_ANDROID_BUTTON_R1 = 103
GAMEPAD_ANDROID_BUTTON_L2 = 104
GAMEPAD_ANDROID_BUTTON_R2 = 105

MAX_SHADER_LOCATIONS = 32
MAX_MATERIAL_MAPS = 12


# STRUCTURES DEFINITIONS
# -------------------------------------------------------------------

class Vector2(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float)
    ]


class Vector3(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
    ]


class Vector4(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
        ('w', c_float),
    ]


class Matrix(Structure):
    _fields_ = [
        ('m0', c_float),
        ('m4', c_float),
        ('m8', c_float),
        ('m12', c_float),
        ('m1', c_float),
        ('m5', c_float),
        ('m9', c_float),
        ('m13', c_float),
        ('m2', c_float),
        ('m6', c_float),
        ('m10', c_float),
        ('m14', c_float),
        ('m3', c_float),
        ('m7', c_float),
        ('m11', c_float),
        ('m15', c_float),
    ]


class Color(Structure):
    _fields_ = [
        ('r', c_ubyte),
        ('g', c_ubyte),
        ('b', c_ubyte),
        ('a', c_ubyte),
    ]


class Rectangle(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('width', c_float),
        ('height', c_float),
    ]


class Image(Structure):
    _fields_ = [
        ('data', c_void_p),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]


class Texture2D(Structure):
    _fields_ = [
        ('data', c_void_p),
        ('id', c_uint),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]


class Texture(Structure):
    _fields_ = [
        ('data', c_void_p),
        ('id', c_uint),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]


class RenderTexture2D(Structure):
    _fields_ = [
        ('id', c_uint),
        ('texture', Texture2D),
        ('depth', Texture2D),
    ]


class RenderTexture(Structure):
    _fields_ = [
        ('id', c_uint),
        ('texture', Texture2D),
        ('depth', Texture2D),
    ]


class CharInfo(Structure):
    _fields_ = [
        ('value', c_int),
        ('rec', Rectangle),
        ('offsetX', c_int),
        ('offsetY', c_int),
        ('advanceX', c_int),
        ('data', c_char_p),
    ]


class Font(Structure):
    _fields_ = [
        ('texture', Texture2D),
        ('baseSize', c_int),
        ('charsCount', c_int),
        ('chars', POINTER(CharInfo)),
    ]


class SpriteFont(Structure):
    _fields_ = [
        ('texture', Texture2D),
        ('baseSize', c_int),
        ('charsCount', c_int),
        ('chars', POINTER(CharInfo)),
    ]


class Camera3D(Structure):
    _fields_ = [
        ('position', Vector3),
        ('target', Vector3),
        ('up', Vector3),
        ('fovy', c_float),
        ('type', c_int),
    ]


class Camera(Structure):
    _fields_ = [
        ('position', Vector3),
        ('target', Vector3),
        ('up', Vector3),
        ('fovy', c_float),
        ('type', c_int),
    ]


class Camera2D(Structure):
    _fields_ = [
        ('offset', Vector2),
        ('target', Vector2),
        ('rotation', c_float),
        ('zoom', c_float),
    ]


class BoundingBox(Structure):
    _fields_ = [
        ('min', Vector3),
        ('max', Vector3),
    ]


class Mesh(Structure):
    _fields_ = [
        ('vertexCount', c_int),
        ('triangleCount', c_int),

        ('vertices', POINTER(c_float)),
        ('texcoords', POINTER(c_float)),
        ('texcoords2', POINTER(c_float)),
        ('normals', POINTER(c_float)),
        ('tangents', POINTER(c_float)),
        ('colors', POINTER(c_ubyte)),
        ('indices', POINTER(c_ushort)),

        ('baseVertices', POINTER(c_float)),
        ('baseNormals', POINTER(c_float)),
        ('weightBias', POINTER(c_float)),
        ('weightId', POINTER(c_int)),

        ('vaoId', c_uint),
        ('vboId', c_uint * 7),
    ]


class Shader(Structure):
    _fields_ = [
        ('id', c_uint),
        ('locs', c_int * MAX_SHADER_LOCATIONS),
    ]


class MaterialMap(Structure):
    _fields_ = [
        ('texture', Texture2D),
        ('color', Color),
        ('value', c_float),
    ]


class Material(Structure):
    _fields_ = [
        ('shader', Shader),
        ('maps', MaterialMap * MAX_MATERIAL_MAPS),
        ('params', POINTER(c_float)),
    ]


class Model(Structure):
    _fields_ = [
        ('mesh', Mesh),
        ('transform', Matrix),
        ('material', Material),
    ]


class Ray(Structure):
    _fields_ = [
        ('position', Vector3),
        ('direction', Vector3),
    ]


class RayHitInfo(Structure):
    _fields_ = [
        ('hit', c_bool),
        ('distance', c_float),
        ('position', Vector3),
        ('normal', Vector3),
    ]


class Wave(Structure):
    _fields_ = [
        ('sampleCount', c_uint),
        ('sampleRate', c_uint),
        ('SampleSize', c_uint),
        ('channels', c_uint),
        ('data', c_void_p),
    ]


class Sound(Structure):
    _fields_ = [
        ('audioBuffer', c_void_p),
        ('source', c_uint),
        ('buffer', c_uint),
        ('format', c_int),
    ]


class Music(Structure):
    pass


MusicData = POINTER(Music)


class AudioStream(Structure):
    _fields_ = [
        ('sampleRate', c_uint),
        ('SampleSize', c_uint),
        ('channels', c_uint),

        ('audioBuffer', c_void_p),

        ('format', c_int),
        ('source', c_uint),
        ('buffers', c_uint * 2),
    ]


class VrDeviceInfo(Structure):
    _fields_ = [
        ('hResolution', c_int),
        ('vResolution', c_int),
        ('hScreenSize', c_float),
        ('vScreenSize', c_float),
        ('vScreenCenter', c_float),
        ('eyeToScreenDistance', c_float),
        ('lensSeparationDistance', c_float),
        ('interpupillaryDistance', c_float),
        ('lensDistortionValues', c_float * 4),
        ('chromaAbCorrection', c_float * 4),
    ]


# ENUMERATORS DEFINITIONS
# -------------------------------------------------------------------

# LogType
LOG_INFO = 1
LOG_WARNING = 2
LOG_ERROR = 4
LOG_DEBUG = 8
LOG_OTHER = 16

# ShaderLocationIndex
LOC_VERTEX_POSITION = 0
LOC_VERTEX_TEXCOORD01 = 1
LOC_VERTEX_TEXCOORD02 = 2
LOC_VERTEX_NORMAL = 3
LOC_VERTEX_TANGENT = 4
LOC_VERTEX_COLOR = 5
LOC_MATRIX_MVP = 6
LOC_MATRIX_MODEL = 7
LOC_MATRIX_VIEW = 8
LOC_MATRIX_PROJECTION = 9
LOC_VECTOR_VIEW = 10
LOC_COLOR_DIFFUSE = 11
LOC_COLOR_SPECULAR = 12
LOC_COLOR_AMBIENT = 13
LOC_MAP_ALBEDO = 14      # LOC_MAP_DIFFUSE
LOC_MAP_METALNESS = 15   # LOC_MAP_SPECULAR
LOC_MAP_NORMAL = 16
LOC_MAP_ROUGHNESS = 17
LOC_MAP_OCCLUSION = 18
LOC_MAP_EMISSION = 19
LOC_MAP_HEIGHT = 20
LOC_MAP_CUBEMAP = 21
LOC_MAP_IRRADIANCE = 22
LOC_MAP_PREFILTER = 23
LOC_MAP_BRDF = 24
LOC_MAP_DIFFUSE = LOC_MAP_ALBEDO
LOC_MAP_SPECULAR = LOC_MAP_METALNESS

# TexmapIndex
MAP_ALBEDO = 0          # MAP_DIFFUSE
MAP_METALNESS = 1          # MAP_SPECULAR
MAP_NORMAL = 2
MAP_ROUGHNESS = 3
MAP_OCCLUSION = 4
MAP_EMISSION = 5
MAP_HEIGHT = 6
MAP_CUBEMAP = 7                # NOTE: Uses GL_TEXTURE_CUBE_MAP
MAP_IRRADIANCE = 8             # NOTE: Uses GL_TEXTURE_CUBE_MAP
MAP_PREFILTER = 9              # NOTE: Uses GL_TEXTURE_CUBE_MAP
MAP_BRDF = 10
MAP_DIFFUSE = MAP_ALBEDO
MAP_SPECULAR = MAP_METALNESS

# PixelFormat
UNCOMPRESSED_GRAYSCALE = 1          # 8 bit per pixel (no alpha)
UNCOMPRESSED_GRAY_ALPHA = 2         # 8*2 bpp (2 channels)
UNCOMPRESSED_R5G6B5 = 3             # 16 bpp
UNCOMPRESSED_R8G8B8 = 4             # 24 bpp
UNCOMPRESSED_R5G5B5A1 = 5           # 16 bpp (1 bit alpha)
UNCOMPRESSED_R4G4B4A4 = 6           # 16 bpp (4 bit alpha)
UNCOMPRESSED_R8G8B8A8 = 7           # 32 bpp
UNCOMPRESSED_R32 = 8                # 32 bpp (1 channel - float)
UNCOMPRESSED_R32G32B32 = 9          # 32*3 bpp (3 channels - float)
UNCOMPRESSED_R32G32B32A32 = 10      # 32*4 bpp (4 channels - float)
COMPRESSED_DXT1_RGB = 11            # 4 bpp (no alpha)
COMPRESSED_DXT1_RGBA = 12           # 4 bpp (1 bit alpha)
COMPRESSED_DXT3_RGBA = 13           # 8 bpp
COMPRESSED_DXT5_RGBA = 14           # 8 bpp
COMPRESSED_ETC1_RGB = 15            # 4 bpp
COMPRESSED_ETC2_RGB = 16            # 4 bpp
COMPRESSED_ETC2_EAC_RGBA = 17       # 8 bpp
COMPRESSED_PVRT_RGB = 18            # 4 bpp
COMPRESSED_PVRT_RGBA = 19           # 4 bpp
COMPRESSED_ASTC_4x4_RGBA = 20       # 8 bpp
COMPRESSED_ASTC_8x8_RGBA = 21       # 2 bpp


# TextureFilterMode
FILTER_POINT = 0                  # No filter =  just pixel aproximation
FILTER_BILINEAR = 1               # Linear filtering
FILTER_TRILINEAR = 2              # Trilinear filtering (linear with mipmaps)
FILTER_ANISOTROPIC_4X = 3         # Anisotropic filtering 4x
FILTER_ANISOTROPIC_8X = 4         # Anisotropic filtering 8x
FILTER_ANISOTROPIC_16X = 5        # Anisotropic filtering 16x


# TextureWrapMode
WRAP_REPEAT = 0
WRAP_CLAMP = 1
WRAP_MIRROR = 2


# BlendMode
BLEND_ALPHA = 0
BLEND_ADDITIVE = 1
BLEND_MULTIPLIED = 2

# Gestures
GESTURE_NONE = 0
GESTURE_TAP = 1
GESTURE_DOUBLETAP = 2
GESTURE_HOLD = 4
GESTURE_DRAG = 8
GESTURE_SWIPE_RIGHT = 16
GESTURE_SWIPE_LEFT = 32
GESTURE_SWIPE_UP = 64
GESTURE_SWIPE_DOWN = 128
GESTURE_PINCH_IN = 256
GESTURE_PINCH_OUT = 512


# CameraMode
CAMERA_CUSTOM = 0,
CAMERA_FREE = 1
CAMERA_ORBITAL = 2
CAMERA_FIRST_PERSON = 3
CAMERA_THIRD_PERSON = 4


# CameraType
CAMERA_PERSPECTIVE = 0
CAMERA_ORTHOGRAPHIC = 1


# VrDeviceType
HMD_DEFAULT_DEVICE = 0,
HMD_OCULUS_RIFT_DK2 = 1
HMD_OCULUS_RIFT_CV1 = 2
HMD_OCULUS_GO = 3
HMD_VALVE_HTC_VIVE = 4
HMD_SONY_PSVR = 5



# WINDOW AND GRAPHICS DEVICE FUNCTIONS
# Module: core
# -------------------------------------------------------------------

# Window-related functions
init_window = _raylib.InitWindow
init_window.argtypes = _ct('iiP')
init_window.restype = None

close_window = _raylib.CloseWindow
close_window.argtypes = _NOARGS
close_window.restype = None

is_window_ready = _raylib.IsWindowReady
is_window_ready.argtypes = _NOARGS
is_window_ready.restype = c_bool

window_should_close = _raylib.WindowShouldClose
window_should_close.argtypes = _NOARGS
window_should_close.restype = c_bool

is_window_minimized = _raylib.IsWindowMinimized
is_window_minimized.argtypes = _NOARGS
is_window_minimized.restype = c_bool

toggle_fullscreen = _raylib.ToggleFullscreen
toggle_fullscreen.argtypes = _NOARGS
toggle_fullscreen.restype = None

set_window_icon = _raylib.SetWindowIcon
set_window_icon.argtypes = [Image]
set_window_icon.restype = None

set_window_title = _raylib.SetWindowTitle
set_window_title.argtypes = _ct('c')
set_window_title.restype = None

set_window_position = _raylib.SetWindowPosition
set_window_position.argtypes = _ct('ii')
set_window_position.restype = None

set_window_monitor = _raylib.SetWindowMonitor
set_window_monitor.argtypes = _ct('i')
set_window_monitor.restype = None

set_window_min_size = _raylib.SetWindowMinSize
set_window_min_size.argtypes = _ct('ii')
set_window_min_size.restype = None

set_window_size = _raylib.SetWindowSize
set_window_size.argtypes = _ct('ii')
set_window_size.restype = None

get_screen_width = _raylib.GetScreenWidth
get_screen_width.argtypes = _NOARGS
get_screen_width.restype = c_int

get_screen_height = _raylib.GetScreenHeight
get_screen_height.argtypes = _NOARGS
get_screen_height.restype = c_int


# Cursor-related functions
show_cursor = _raylib.ShowCursor
show_cursor.argtypes = _NOARGS
show_cursor.restype = None

hide_cursor = _raylib.HideCursor
hide_cursor.argtypes = _NOARGS
hide_cursor.restype = None

is_cursor_hidden = _raylib.IsCursorHidden
is_cursor_hidden.argtypes = _NOARGS
is_cursor_hidden.restype = c_bool

enable_cursor = _raylib.EnableCursor
enable_cursor.argtypes = _NOARGS
enable_cursor.restype = None

disable_cursor = _raylib.DisableCursor
disable_cursor.argtypes = _NOARGS
disable_cursor.restype = None


# Drawing-related functions
clear_background = _raylib.ClearBackground
clear_background.argtypes = [Color]
clear_background.restype = None

begin_drawing = _raylib.BeginDrawing
begin_drawing.argtypes = _NOARGS
begin_drawing.restype = None

end_drawing = _raylib.EndDrawing
end_drawing.argtypes = _NOARGS
end_drawing.restype = None

begin_mode2D = _raylib.BeginMode2D
begin_mode2D.argtypes = [Camera2D]
begin_mode2D.restype = None

end_mode2D = _raylib.EndMode2D
end_mode2D.argtypes = _NOARGS
end_mode2D.restype = None

begin_mode3D = _raylib.BeginMode3D
begin_mode3D.argtypes = [Camera]
begin_mode3D.restype = None

end_mode3D = _raylib.EndMode3D
end_mode3D.argtypes = _NOARGS
end_mode3D.restype = None

begin_texture_mode = _raylib.BeginTextureMode
begin_texture_mode.argtypes = [RenderTexture2D]
begin_texture_mode.restype = None

end_texture_mode = _raylib.EndTextureMode
end_texture_mode.argtypes = _NOARGS
end_texture_mode.restype = None


# Screen-space-related functions
get_mouse_ray = _raylib.GetMouseRay
get_mouse_ray.argtypes = [Vector2, Camera]
get_mouse_ray.restype = Ray

get_world_to_screen = _raylib.GetWorldToScreen
get_world_to_screen.argtypes = [Vector3, Camera]
get_world_to_screen.restype = Vector2

get_camera_matrix = _raylib.GetCameraMatrix
get_camera_matrix.argtypes = [Camera]
get_camera_matrix.restype = Matrix


# Timing-related functions
set_target_fps = _raylib.SetTargetFPS
set_target_fps.argtypes = _ct('i')
set_target_fps.restype = None

get_fps = _raylib.GetFPS
get_fps.argtypes = _NOARGS
get_fps.restype = c_int

get_frame_time = _raylib.GetFrameTime
get_frame_time.argtypes = _NOARGS
get_frame_time.restype = c_float

get_time = _raylib.GetTime
get_time.argtypes = _NOARGS
get_time.restype = c_double


# Color-related functions

color_to_int = _raylib.ColorToInt
color_to_int.argtypes = [Color]
color_to_int.restype = c_int

color_normalize = _raylib.ColorNormalize
color_normalize.argtypes = [Color]
color_normalize.restype = Vector4

color_to_hsv = _raylib.ColorToHSV
color_to_hsv.argtypes = [Color]
color_to_hsv.restype = Vector3

get_color = _raylib.GetColor
get_color.argtypes = [c_int]
get_color.restype = Color

fade = _raylib.Fade
fade.argtypes = [Color, c_float]
fade.restype = Color

'''
# Math functions (available from raymath.h)
vector_to_float = _raylib.VectorToFloat
vector_to_float.argtypes = [Vector3]
vector_to_float.restype = POINTER(c_float)

matrix_to_float = _raylib.MatrixToFloat
matrix_to_float.argtypes = [Matrix]
matrix_to_float.restype = POINTER(c_float)

vector3_zero = _raylib.Vector3Zero
vector3_zero.argtypes = _NOARGS
vector3_zero.restype = Vector3

vector3_one = _raylib.Vector3One
vector3_one.argtypes = _NOARGS
vector3_one.restype = Vector3

matrix_identity = _raylib.MatrixIdentity
matrix_identity.argtypes = _NOARGS
matrix_identity.restype = Matrix
'''

# Misc. functions
show_logo = _raylib.ShowLogo
show_logo.argtypes = _NOARGS
show_logo.restype = None

set_config_flags = _raylib.SetConfigFlags
set_config_flags.argtypes = _ct('b')
set_config_flags.restype = None

set_trace_log = _raylib.TraceLog
set_trace_log.argtypes = _ct('ic')
set_trace_log.restype = None

take_screenshot = _raylib.TakeScreenshot
take_screenshot.argtypes = _ct('c')
take_screenshot.restype = None

get_random_value = _raylib.GetRandomValue
get_random_value.argtypes = _ct('ii')
get_random_value.restype = c_int

# Files management functions
is_file_extension = _raylib.IsFileExtension
is_file_extension.argtypes = _ct('cc')
is_file_extension.restype = c_bool

get_extension = _raylib.GetExtension
get_extension.argtypes = _ct('c')
get_extension.restype = c_char_p

get_extension = _raylib.GetFileName
get_extension.argtypes = _ct('c')
get_extension.restype = c_char_p

get_directory_path = _raylib.GetDirectoryPath
get_directory_path.argtypes = _ct('c')
get_directory_path.restype = c_char_p

get_working_directory = _raylib.GetWorkingDirectory
get_working_directory.argtypes = _NOARGS
get_working_directory.restype = c_char_p

change_directory = _raylib.ChangeDirectory
change_directory.argtypes = _ct('c')
change_directory.restype = c_bool

is_file_dropped = _raylib.IsFileDropped
is_file_dropped.argtypes = _NOARGS
is_file_dropped.restype = c_bool

get_dropped_files = _raylib.GetDroppedFiles
get_dropped_files.argtypes = _ct('i*')
get_dropped_files.restype = POINTER(c_char_p)

clear_dropped_files = _raylib.ClearDroppedFiles
clear_dropped_files.argtypes = _NOARGS
clear_dropped_files.restype = None

# Persistent storage management
storage_save_value = _raylib.StorageSaveValue
storage_save_value.argtypes = _ct('ii')
storage_save_value.restype = None

storage_load_value = _raylib.StorageLoadValue
storage_load_value.argtypes = _ct('i')
storage_load_value.restype = c_int


# INPUT HANDLING FUNCTIONS
# MODULE: core
# -------------------------------------------------------------------

# Input-related functions: keyboard
is_key_pressed = _raylib.IsKeyPressed
is_key_pressed.argtypes = _ct('i')
is_key_pressed.restype = c_bool

is_key_down = _raylib.IsKeyDown
is_key_down.argtypes = _ct('i')
is_key_down.restype = c_bool

is_key_released = _raylib.IsKeyReleased
is_key_released.argtypes = _ct('i')
is_key_released.restype = c_bool

is_key_up = _raylib.IsKeyUp
is_key_up.argtypes = _ct('i')
is_key_up.restype = c_bool

get_key_pressed = _raylib.GetKeyPressed
get_key_pressed.argtypes = _NOARGS
get_key_pressed.restype = c_int

set_exit_key = _raylib.SetExitKey
set_exit_key.argtypes = _ct('i')
set_exit_key.restype = None


# Input-related functions: gamepads
is_gamepad_available = _raylib.IsGamepadAvailable
is_gamepad_available.argtypes = _ct('i')
is_gamepad_available.restype = c_bool

is_gamepad_name = _raylib.IsGamepadName
is_gamepad_name.argtypes = _ct('ic')
is_gamepad_name.restype = c_bool

get_gamepad_name = _raylib.GetGamepadName
get_gamepad_name.argtypes = _ct('i')
get_gamepad_name.restype = c_char_p

is_gamepad_button_pressed = _raylib.IsGamepadButtonPressed
is_gamepad_button_pressed.argtypes = _ct('ii')
is_gamepad_button_pressed.restype = c_bool

is_gamepad_button_down = _raylib.IsGamepadButtonDown
is_gamepad_button_down.argtypes = _ct('ii')
is_gamepad_button_down.restype = c_bool

is_gamepad_button_released = _raylib.IsGamepadButtonReleased
is_gamepad_button_released.argtypes = _ct('ii')
is_gamepad_button_released.restype = c_bool

is_gamepat_button_up = _raylib.IsGamepadButtonUp
is_gamepat_button_up.argtypes = _ct('ii')
is_gamepat_button_up.restype = c_bool

get_gamepad_button_pressed = _raylib.GetGamepadButtonPressed
get_gamepad_button_pressed.argtypes = _NOARGS
get_gamepad_button_pressed.restype = c_int

get_gamepad_axis_count = _raylib.GetGamepadAxisCount
get_gamepad_axis_count.argtypes = _ct('i')
get_gamepad_axis_count.restype = c_int

get_gamepad_axis_movement = _raylib.GetGamepadAxisMovement
get_gamepad_axis_movement.argtypes = _ct('ii')
get_gamepad_axis_movement.restype = c_float


# Input-related functions: mouse
is_mouse_button_pressed = _raylib.IsMouseButtonPressed
is_mouse_button_pressed.argtypes = _ct('i')
is_mouse_button_pressed.restype = c_bool

is_mouse_button_down = _raylib.IsMouseButtonDown
is_mouse_button_down.argtypes = _ct('i')
is_mouse_button_down.restype = c_bool

is_mouse_button_released = _raylib.IsMouseButtonReleased
is_mouse_button_released.argtypes = _ct('i')
is_mouse_button_released.restype = c_bool

is_mouse_button_up = _raylib.IsMouseButtonUp
is_mouse_button_up.argtypes = _ct('i')
is_mouse_button_up.restype = c_bool

get_mouse_x = _raylib.GetMouseX
get_mouse_x.argtypes = _NOARGS
get_mouse_x.restype = c_int

get_mouse_y = _raylib.GetMouseY
get_mouse_y.argtypes = _NOARGS
get_mouse_y.restype = c_int

get_mouse_position = _raylib.GetMousePosition
get_mouse_position.argtypes = _NOARGS
get_mouse_position.restype = Vector2

set_mouse_scale = _raylib.SetMousePosition
set_mouse_scale.argtypes = [Vector2]
set_mouse_scale.restype = None

get_mouse_wheel_move = _raylib.GetMouseWheelMove
get_mouse_wheel_move.argtypes = _NOARGS
get_mouse_wheel_move.restype = c_int


# Input-related functions: touch
get_touch_x = _raylib.GetTouchX
get_touch_x.argtypes = _NOARGS
get_touch_x.restype = c_int

get_touch_y = _raylib.GetTouchY
get_touch_y.argtypes = _NOARGS
get_touch_y.restype = c_int

get_touch_position = _raylib.GetTouchPosition
get_touch_position.argtypes = _ct('i')
get_touch_position.restype = Vector2


# GESTURES AND TOUCH HANDLING FUNCTIONS
# MODULE: gestures
# -------------------------------------------------------------------

set_gestures_enabled = _raylib.SetGesturesEnabled
set_gestures_enabled.argtypes = _ct('I')
set_gestures_enabled.restype = None

is_gesture_detected = _raylib.IsGestureDetected
is_gesture_detected.argtypes = _ct('i')
is_gesture_detected.restype = c_bool

get_gesture_detected = _raylib.GetGestureDetected
get_gesture_detected.argtypes = _NOARGS
get_gesture_detected.restype = c_int

get_touch_points_count = _raylib.GetTouchPointsCount
get_touch_points_count.argtypes = _NOARGS
get_touch_points_count.restype = c_int

get_gesture_hold_duration = _raylib.GetGestureHoldDuration
get_gesture_hold_duration.argtypes = _NOARGS
get_gesture_hold_duration.restype = c_float

get_gesture_drag_vector = _raylib.GetGestureDragVector
get_gesture_drag_vector.argtypes = _NOARGS
get_gesture_drag_vector.restype = Vector2

get_gesture_drag_angle = _raylib.GetGestureDragAngle
get_gesture_drag_angle.argtypes = _NOARGS
get_gesture_drag_angle.restype = c_float

get_gesture_pich_vector = _raylib.GetGesturePinchVector
get_gesture_pich_vector.argtypes = _NOARGS
get_gesture_pich_vector.restype = Vector2

get_gesture_pinch_angle = _raylib.GetGesturePinchAngle
get_gesture_pinch_angle.argtypes = _NOARGS
get_gesture_pinch_angle.restype = c_float


# CAMERA SYSTEM FUNCTIONS
# MODULE: camera
# -------------------------------------------------------------------

set_camera_mode = _raylib.SetCameraMode
set_camera_mode.argtypes = [Camera, c_int]
set_camera_mode.restype = None

update_camera = _raylib.UpdateCamera
update_camera.argtypes = [POINTER(Camera)]
update_camera.restype = None

set_camera_pan_control = _raylib.SetCameraPanControl
set_camera_pan_control.argtypes = _ct('i')
set_camera_pan_control.restype = None

set_camera_alt_control = _raylib.SetCameraAltControl
set_camera_alt_control.argtypes = _ct('i')
set_camera_alt_control.restype = None

set_camera_smoothzoom_control = _raylib.SetCameraSmoothZoomControl
set_camera_smoothzoom_control.argtypes = _ct('i')
set_camera_smoothzoom_control.restype = None

set_camera_move_controls = _raylib.SetCameraMoveControls
set_camera_move_controls.argtypes = _ct('iiiiii')
set_camera_move_controls.restype = None


# BASIC SHAPES DRAWING FUNCTIONS
# MODULE: shapes
# -------------------------------------------------------------------

draw_pixel = _raylib.DrawPixel
draw_pixel.argtypes = [c_int, c_int, Color]
draw_pixel.restype = None

draw_pixel_v = _raylib.DrawPixelV
draw_pixel_v.argtypes = [Vector2, Color]
draw_pixel_v.restype = None

draw_line = _raylib.DrawLine
draw_line.argtypes = _ct('iiii') + [Color]
draw_line.restype = None

draw_line_v = _raylib.DrawLineV
draw_line_v.argtypes = [Vector2, Vector2, Color]
draw_line_v.restype = None

draw_line_ex = _raylib.DrawLineEx
draw_line_ex.argtypes = [Vector2, Vector2, c_float, Color]
draw_line_ex.restype = None

draw_line_bezier = _raylib.DrawLineBezier
draw_line_bezier.argtypes = [Vector2, Vector2, c_float, Color]
draw_line_bezier.restype = None

draw_circle = _raylib.DrawCircle
draw_circle.argtypes = _ct('iif') + [Color]
draw_circle.restype = None

draw_circle_gradient = _raylib.DrawCircleGradient
draw_circle_gradient.argtypes = _ct('iif') + [Color, Color]
draw_circle_gradient.restype = None

draw_circle_v = _raylib.DrawCircleV
draw_circle_v.argtypes = [Vector2, c_float, Color]
draw_circle_v.restype = None

draw_circle_lines = _raylib.DrawCircleLines
draw_circle_lines.argtypes = _ct('iif') + [Color]
draw_circle_lines.restype = None

draw_rectangle = _raylib.DrawRectangle
draw_rectangle.argtypes = _ct('iiii') + [Color]
draw_rectangle.restype = None

draw_rectangle_v = _raylib.DrawRectangleV
draw_rectangle_v.argtypes = [Vector2, Vector2, Color]
draw_rectangle_v.restype = None

draw_rectangle_rec = _raylib.DrawRectangleRec
draw_rectangle_rec.argtypes = [Rectangle, Color]
draw_rectangle_rec.restype = None

draw_rectangle_pro = _raylib.DrawRectanglePro
draw_rectangle_pro.argtypes = [Rectangle, Vector2, c_float, Color]
draw_rectangle_pro.restype = None

draw_rectangle_gradient_v = _raylib.DrawRectangleGradientV
draw_rectangle_gradient_v.argtypes = _ct('iiii') + [Color, Color]
draw_rectangle_gradient_v.restype = None

draw_rectangle_gradient_h = _raylib.DrawRectangleGradientH
draw_rectangle_gradient_h.argtypes = _ct('iiii') + [Color, Color]
draw_rectangle_gradient_h.restype = None

draw_rectangle_gradient_ex = _raylib.DrawRectangleGradientEx
draw_rectangle_gradient_ex.argtypes = [Rectangle, Color, Color, Color, Color]
draw_rectangle_gradient_ex.restype = None

draw_rectangle_lines = _raylib.DrawRectangleLines
draw_rectangle_lines.argtypes = _ct('iiii') + [Color]
draw_rectangle_lines.restype = None

draw_triangle = _raylib.DrawTriangle
draw_triangle.argtypes = [Vector2, Vector2, Vector2, Color]
draw_triangle.restype = None

draw_triangle_lines = _raylib.DrawTriangleLines
draw_triangle_lines.argtypes = [Vector2, Vector2, Vector2, Color]
draw_triangle_lines.restype = None

draw_poly = _raylib.DrawPoly
draw_poly.argtypes = [Vector2] + _ct('iff') + [Color]
draw_poly.restype = None

draw_poly_ex = _raylib.DrawPolyEx
draw_poly_ex.argtypes = [POINTER(Vector2), c_int, Color]
draw_poly_ex.restype = None

draw_poly_ex_lines = _raylib.DrawPolyExLines
draw_poly_ex_lines.argtypes = [POINTER(Vector2), c_int, Color]
draw_poly_ex_lines.restype = None


# Basic shapes collision detection functions
check_collision_recs = _raylib.CheckCollisionRecs
check_collision_recs.argtypes = [Rectangle, Rectangle]
check_collision_recs.restype = c_bool

check_collision_circles = _raylib.CheckCollisionCircles
check_collision_circles.argtypes = [Vector2, c_float, Vector2, c_float]
check_collision_circles.restype = c_bool

check_collision_circle_rec = _raylib.CheckCollisionCircleRec
check_collision_circle_rec.argtypes = [Vector2, c_float, Rectangle]
check_collision_circle_rec.restype = c_bool

get_collision_rec = _raylib.GetCollisionRec
get_collision_rec.argtypes = [Rectangle, Rectangle]
get_collision_rec.restype = Rectangle

check_collision_point_rec = _raylib.CheckCollisionPointRec
check_collision_point_rec.argtypes = [Vector2, Rectangle]
check_collision_point_rec.restype = c_bool

check_collision_point_circle = _raylib.CheckCollisionPointCircle
check_collision_point_circle.argtypes = [Vector2, Vector2, c_float]
check_collision_point_circle.restype = c_bool

check_collision_point_triangle = _raylib.CheckCollisionPointTriangle
check_collision_point_triangle.argtypes = [Vector2, Vector2, Vector2, Vector2]
check_collision_point_triangle.restype = c_bool


# TEXTURE LOADING AND DRAWING FUNCTIONS
# MODULE: textures
# -------------------------------------------------------------------

# Image/Texture2D data loading/unloading/saving functions
load_image = _raylib.LoadImage
load_image.argtypes = _ct('c')
load_image.restype = Image

load_image_ex = _raylib.LoadImageEx
load_image_ex.argtypes = [POINTER(Color)] + _ct('ii')
load_image_ex.restype = Image

load_image_pro = _raylib.LoadImagePro
load_image_pro.argtypes = _ct('Piii')
load_image_pro.restype = Image

load_image_raw = _raylib.LoadImageRaw
load_image_raw.argtypes = _ct('ciii')
load_image_raw.restype = Image

export_image = _raylib.LoadImageRaw
export_image.argtypes = [c_char_p, Image]
export_image.restype = Image

load_texture = _raylib.LoadTexture
load_texture.argtypes = _ct('c')
load_texture.restype = Texture2D

load_texture_from_image = _raylib.LoadTextureFromImage
load_texture_from_image.argtypes = [Image]
load_texture_from_image.restype = Texture2D

load_render_texture = _raylib.LoadRenderTexture
load_render_texture.argtypes = _ct('ii')
load_render_texture.restype = RenderTexture2D

unload_image = _raylib.UnloadImage
unload_image.argtypes = [Image]
unload_image.restype = None

unload_texture = _raylib.UnloadTexture
unload_texture.argtypes = [Texture2D]
unload_texture.restype = None

unload_render_texture = _raylib.UnloadRenderTexture
unload_render_texture.argtypes = [RenderTexture2D]
unload_render_texture.restype = None

get_image_data = _raylib.GetImageData
get_image_data.argtypes = [Image]
get_image_data.restype = POINTER(Color)

get_image_data_normalized = _raylib.GetImageDataNormalized
get_image_data_normalized.argtypes = [Image]
get_image_data_normalized.restype = POINTER(Vector4)

get_texture_data = _raylib.GetTextureData
get_texture_data.argtypes = [Texture2D]
get_texture_data.restype = Image

update_texture = _raylib.UpdateTexture
update_texture.argtypes = [Texture2D, c_void_p]
update_texture.restype = None


# Image manipulation functions
image_copy = _raylib.ImageCopy
image_copy.argtypes = [POINTER(Image)]
image_copy.restype = Image

image_to_pot = _raylib.ImageToPOT
image_to_pot.argtypes = [POINTER(Image), Color]
image_to_pot.restype = None

image_format = _raylib.ImageFormat
image_format.argtypes = [POINTER(Image), c_int]
image_format.restype = None

image_alpha_mask = _raylib.ImageAlphaMask
image_alpha_mask.argtypes = [POINTER(Image), Image]
image_alpha_mask.restype = None

image_alpha_clear = _raylib.ImageAlphaClear
image_alpha_clear.argtypes = [POINTER(Image), Color, c_float]
image_alpha_clear.restype = None

image_alpha_crop = _raylib.ImageAlphaCrop
image_alpha_crop.argtypes = [POINTER(Image), c_float]
image_alpha_crop.restype = None

image_alpha_premultiply = _raylib.ImageAlphaPremultiply
image_alpha_premultiply.argtypes = [POINTER(Image)]
image_alpha_premultiply.restype = None

image_crop = _raylib.ImageCrop
image_crop.argtypes = [POINTER(Image), Rectangle]
image_crop.restype = None

image_resize = _raylib.ImageResize
image_resize.argtypes = [POINTER(Image)] + _ct('ii')
image_resize.restype = None

image_resize_nn = _raylib.ImageResizeNN
image_resize_nn.argtypes = [POINTER(Image)] + _ct('ii')
image_resize_nn.restype = None

image_resize_canvas = _raylib.ImageResizeCanvas
image_resize_canvas.argtypes = [POINTER(Image)] + _ct('iiii') + [Color]
image_resize_canvas.restype = None

image_mipmaps = _raylib.ImageMipmaps
image_mipmaps.argtypes = [POINTER(Image)]
image_mipmaps.restype = None

image_dither = _raylib.ImageDither
image_dither.argtypes = [POINTER(Image)] + _ct('iiii')
image_dither.restype = None

image_text = _raylib.ImageText
image_text.argtypes = _ct('ci') + [Color]
image_text.restype = Image

image_text_ex = _raylib.ImageTextEx
image_text_ex.argtypes = [SpriteFont] + _ct('cfi') + [Color]
image_text_ex.restype = Image

image_draw = _raylib.ImageDraw
image_draw.argtypes = [POINTER(Image), Image, Rectangle, Rectangle]
image_draw.restype = None

image_draw = _raylib.ImageDrawRectangle
image_draw.argtypes = [POINTER(Image), Vector2, Rectangle, Color]
image_draw.restype = None

image_draw_text = _raylib.ImageDrawText
image_draw_text.argtypes = [POINTER(Image), Vector2] + _ct('ci') + [Color]
image_draw_text.restype = None

image_draw_text_ex = _raylib.ImageDrawTextEx
image_draw_text_ex.argtypes = [POINTER(Image), Vector2, SpriteFont, c_char_p]
image_draw_text_ex.restype = None

image_flip_vertical = _raylib.ImageFlipVertical
image_flip_vertical.argtypes = [POINTER(Image)]
image_flip_vertical.restype = None

image_flip_horizontal = _raylib.ImageFlipHorizontal
image_flip_horizontal.argtypes = [POINTER(Image)]
image_flip_horizontal.restype = None

image_rotate_cw = _raylib.ImageRotateCW
image_rotate_cw.argtypes = [POINTER(Image)]
image_rotate_cw.restype = None

image_rotate_ccw = _raylib.ImageRotateCCW
image_rotate_ccw.argtypes = [POINTER(Image)]
image_rotate_ccw.restype = None

image_color_tint = _raylib.ImageColorTint
image_color_tint.argtypes = [POINTER(Image), Color]
image_color_tint.restype = None

image_color_invert = _raylib.ImageColorInvert
image_color_invert.argtypes = [POINTER(Image)]
image_color_invert.restype = None

image_color_grayscale = _raylib.ImageColorGrayscale
image_color_grayscale.argtypes = [POINTER(Image)]
image_color_grayscale.restype = None

image_color_contrast = _raylib.ImageColorContrast
image_color_contrast.argtypes = [POINTER(Image), c_float]
image_color_contrast.restype = None

image_color_brightness = _raylib.ImageColorBrightness
image_color_brightness.argtypes = [POINTER(Image), c_int]
image_color_brightness.restype = None

image_color_replace = _raylib.ImageColorReplace
image_color_replace.argtypes = [POINTER(Image), Color, Color]
image_color_replace.restype = None


# image generation functions
gen_image_color = _raylib.GenImageColor
gen_image_color.argtypes = _ct('ii') + [Color]
gen_image_color.restype = Image

gen_image_gradient_v = _raylib.GenImageGradientV
gen_image_gradient_v.argtypes = _ct('ii') + [Color, Color]
gen_image_gradient_v.restype = Image

gen_image_gradient_h = _raylib.GenImageGradientH
gen_image_gradient_h.argtypes = _ct('ii') + [Color, Color]
gen_image_gradient_h.restype = Image

gen_image_gradient_radial = _raylib.GenImageGradientRadial
gen_image_gradient_radial.argtypes = _ct('iif') + [Color, Color]
gen_image_gradient_radial.restype = Image

gen_image_checked = _raylib.GenImageChecked
gen_image_checked.argtypes = _ct('iiii') + [Color, Color]
gen_image_checked.restype = Image

gen_image_white_noise = _raylib.GenImageWhiteNoise
gen_image_white_noise.argtypes = _ct('iif')
gen_image_white_noise.restype = Image

gen_image_perlin_noise = _raylib.GenImagePerlinNoise
gen_image_perlin_noise.argtypes = _ct('iif')
gen_image_perlin_noise.restype = Image

gen_image_cellular = _raylib.GenImageCellular
gen_image_cellular.argtypes = _ct('iii')
gen_image_cellular.restype = Image


# Texture2D configuration functions
gen_texture_mipmaps = _raylib.GenTextureMipmaps
gen_texture_mipmaps.argtypes = [POINTER(Texture2D)]
gen_texture_mipmaps.restype = None

set_texture_filter = _raylib.SetTextureFilter
set_texture_filter.argtypes = [Texture2D, c_int]
set_texture_filter.restype = None

set_texture_wrap = _raylib.SetTextureWrap
set_texture_wrap.argtypes = [Texture2D, c_int]
set_texture_wrap.restype = None


# Texture2D drawing functions
draw_texture = _raylib.DrawTexture
draw_texture.argtypes = [Texture2D] + _ct('ii') + [Color]
draw_texture.restype = None

draw_texture_v = _raylib.DrawTextureV
draw_texture_v.argtypes = [Texture2D, Vector2, Color]
draw_texture_v.restype = None

draw_texture_ex = _raylib.DrawTextureEx
draw_texture_ex.argtypes = [Texture2D] + _ct('ff') + [Color]
draw_texture_ex.restype = None

draw_texture_rec = _raylib.DrawTextureRec
draw_texture_rec.argtypes = [Texture2D, Rectangle, Vector2, Color]
draw_texture_rec.restype = None

draw_texture_pro = _raylib.DrawTexturePro
draw_texture_pro.argtypes = [Texture2D, Rectangle, Rectangle, Vector2, c_float, Color]
draw_texture_pro.restype = None


# FONT LOADING AND TEXT DRAWING FUNCTIONS
# MODULE: text
# -------------------------------------------------------------------

# Font loading/unloading functions
get_font_default = _raylib.GetFontDefault
get_font_default.argtypes = _NOARGS
get_font_default.restype = Font

load_font = _raylib.LoadFont
load_font.argtypes = _ct('c')
load_font.restype = Font

load_font_ex = _raylib.LoadFontEx
load_font_ex.argtypes = _ct('ciii*')
load_font_ex.restype = Font

load_font_ex = _raylib.LoadFontData
load_font_ex.argtypes = _ct('cii*i?')
load_font_ex.restype = POINTER(CharInfo)

gen_image_font_atlas = _raylib.GenImageFontAtlas
gen_image_font_atlas.argtypes = [POINTER(CharInfo)] + _ct('iiii')
gen_image_font_atlas.restype = Image

unload_font = _raylib.UnloadFont
unload_font.argtypes = [Font]
unload_font.restype = None


# Text drawing functions
draw_fps = _raylib.DrawFPS
draw_fps.argtypes = _ct('ii')
draw_fps.restype = None

draw_text = _raylib.DrawText
draw_text.argtypes = _ct('ciii') + [Color]
draw_text.restype = None

draw_text_ex = _raylib.DrawTextEx
draw_text_ex.argtypes = [Font, c_char_p, Vector2] + _ct('ff') + [Color]
draw_text_ex.restype = None


# Text misc. functions
measure_text = _raylib.MeasureText
measure_text.argtypes = _ct('ci')
measure_text.restype = c_int

measure_text_ex = _raylib.MeasureTextEx
measure_text_ex.argtypes = [Font] + _ct('cff')
measure_text_ex.restype = Vector2

format_text = _raylib.FormatText
format_text.argtypes = _ct('c')
format_text.restype = c_char_p

sub_text = _raylib.SubText
sub_text.argtypes = _ct('cii')
sub_text.restype = c_char_p

sub_text = _raylib.GetGlyphIndex
sub_text.argtypes = [Font, c_int]
sub_text.restype = c_int


# BASIC 3D SHAPES DRAWING FUNCTIONS
# MODULE: models
# -------------------------------------------------------------------

# Basic geometric 3D shapes drawing functions
draw_line_3d = _raylib.DrawLine3D
draw_line_3d.argtypes = [Vector3, Vector3, Color]
draw_line_3d.restype = None

draw_circle_3d = _raylib.DrawCircle3D
draw_circle_3d.argtypes = [Vector3, c_float, Vector3, c_float, Color]
draw_circle_3d.restype = None

draw_cube = _raylib.DrawCube
draw_cube.argtypes = [Vector3] + _ct('fff') + [Color]
draw_cube.restype = None

draw_cube_v = _raylib.DrawCubeV
draw_cube_v.argtypes = [Vector3, Vector3, Color]
draw_cube_v.restype = None

draw_cube_wires = _raylib.DrawCubeWires
draw_cube_wires.argtypes = [Vector3] + _ct('fff') + [Color]
draw_cube_wires.restype = None

draw_cube_texture = _raylib.DrawCubeTexture
draw_cube_texture.argtypes = [Texture2D, Vector3] + _ct('fff') + [Color]
draw_cube_texture.restype = None

draw_sphere = _raylib.DrawSphere
draw_sphere.argtypes = [Vector3, c_float, Color]
draw_sphere.restype = None

draw_sphere_ex = _raylib.DrawSphereEx
draw_sphere_ex.argtypes = [Vector3] + _ct('fii') + [Color]
draw_sphere_ex.restype = None

draw_sphere_wires = _raylib.DrawSphereWires
draw_sphere_wires.argtypes = [Vector3] + _ct('fii') + [Color]
draw_sphere_wires.restype = None

draw_cylinder = _raylib.DrawCylinder
draw_cylinder.argtypes = [Vector3] + _ct('fffi') + [Color]
draw_cylinder.restype = None

draw_cylinder_wires = _raylib.DrawCylinderWires
draw_cylinder_wires.argtypes = [Vector3] + _ct('fffi') + [Color]
draw_cylinder_wires.restype = None

draw_plane = _raylib.DrawPlane
draw_plane.argtypes = [Vector3, Vector2, Color]
draw_plane.restype = None

draw_ray = _raylib.DrawRay
draw_ray.argtypes = [Ray, Color]
draw_ray.restype = None

draw_grid = _raylib.DrawGrid
draw_grid.argtypes = _ct('if')
draw_grid.restype = None

draw_gizmo = _raylib.DrawGizmo
draw_gizmo.argtypes = [Vector3]
draw_gizmo.restype = None


# MODEL 3D LOADING AND DRAWING FUNCTIONS
# MODULE: models
# -------------------------------------------------------------------

# Model loading/unloading functions
load_model = _raylib.LoadModel
load_model.argtypes = _ct('c')
load_model.restype = Model

load_model_from_mesh = _raylib.LoadModelFromMesh
load_model_from_mesh.argtypes = [Mesh]
load_model_from_mesh.restype = Model

unload_model = _raylib.UnloadModel
unload_model.argtypes = [Mesh]
unload_model.restype = None


# Mesh loading/unloading functions
load_mesh = _raylib.LoadMesh
load_mesh.argtypes = _ct('c')
load_mesh.restype = Mesh

unload_mesh = _raylib.UnloadMesh
unload_mesh.argtypes = [POINTER(Mesh)]
unload_mesh.restype = None

export_mesh = _raylib.ExportMesh
export_mesh.argtypes = [c_char_p, Mesh]
export_mesh.restype = None


# Mesh manipulation functions
mesh_bounding_box = _raylib.MeshBoundingBox
mesh_bounding_box.argtypes = [Mesh]
mesh_bounding_box.restype = BoundingBox

mesh_tangents = _raylib.MeshTangents
mesh_tangents.argtypes = [POINTER(Mesh)]
mesh_tangents.restype = None

mesh_binormals = _raylib.MeshBinormals
mesh_binormals.argtypes = [POINTER(Mesh)]
mesh_binormals.restype = None


# Mesh generation functions
gen_mesh_plane = _raylib.GenMeshPlane
gen_mesh_plane.argtypes = _ct('ffii')
gen_mesh_plane.restype = Mesh

gen_mesh_cube = _raylib.GenMeshCube
gen_mesh_cube.argtypes = _ct('fff')
gen_mesh_cube.restype = Mesh

gen_mesh_shpere = _raylib.GenMeshSphere
gen_mesh_shpere.argtypes = _ct('fii')
gen_mesh_shpere.restype = Mesh

gen_mesh_hemisphere = _raylib.GenMeshHemiSphere
gen_mesh_hemisphere.argtypes = _ct('fii')
gen_mesh_hemisphere.restype = Mesh

gen_mesh_cylinder = _raylib.GenMeshCylinder
gen_mesh_cylinder.argtypes = _ct('ffi')
gen_mesh_cylinder.restype = Mesh

gen_mesh_torus = _raylib.GenMeshTorus
gen_mesh_torus.argtypes = _ct('ffii')
gen_mesh_torus.restype = Mesh

gen_mesh_knot = _raylib.GenMeshKnot
gen_mesh_knot.argtypes = _ct('ffii')
gen_mesh_knot.restype = Mesh

gen_mesh_heightmap = _raylib.GenMeshHeightmap
gen_mesh_heightmap.argtypes = [Image, Vector3]
gen_mesh_heightmap.restype = Mesh

gen_mesh_cubicmap = _raylib.GenMeshCubicmap
gen_mesh_cubicmap.argtypes = [Image, Vector3]
gen_mesh_cubicmap.restype = Mesh


# Material loading/unloading functions
load_material = _raylib.LoadMaterial
load_material.argtypes = _ct('c')
load_material.restype = Material

load_material_default = _raylib.LoadMaterialDefault
load_material_default.argtypes = _NOARGS
load_material_default.restype = Material

unload_material = _raylib.UnloadMaterial
unload_material.argtypes = [Material]
unload_material.restype = None


# Model drawing functions
draw_model = _raylib.DrawModel
draw_model.argtypes = [Model, Vector3, c_float, Color]
draw_model.restype = None

draw_model_ex = _raylib.DrawModelEx
draw_model_ex.argtypes = [Model, Vector3, Vector3, c_float, Vector3, Color]
draw_model_ex.restype = None

draw_model_wires = _raylib.DrawModelWires
draw_model_wires.argtypes = [Model, Vector3, c_float, Color]
draw_model_wires.restype = None

draw_model_wires_ex = _raylib.DrawModelWiresEx
draw_model_wires_ex.argtypes = [Model, Vector3, Vector3, c_float, Vector3, Color]
draw_model_wires_ex.restype = None

draw_bounding_box = _raylib.DrawBoundingBox
draw_bounding_box.argtypes = [BoundingBox, Color]
draw_bounding_box.restype = None

draw_billboard = _raylib.DrawBillboard
draw_billboard.argtypes = [Camera, Texture2D, Vector3, c_float, Color]
draw_billboard.restype = None

draw_billboard_rec = _raylib.DrawBillboardRec
draw_billboard_rec.argtypes = [Camera, Texture2D, Rectangle, Vector3, c_float, Color]
draw_billboard_rec.restype = None


# Collision detection functions
check_collision_spheres = _raylib.CheckCollisionSpheres
check_collision_spheres.argtypes = [Vector3, c_float, Vector3, c_float]
check_collision_spheres.restype = c_bool

check_collision_boxes = _raylib.CheckCollisionBoxes
check_collision_boxes.argtypes = [BoundingBox, BoundingBox]
check_collision_boxes.restype = c_bool

check_collision_box_sphere = _raylib.CheckCollisionBoxSphere
check_collision_box_sphere.argtypes = [BoundingBox, Vector3, c_float]
check_collision_box_sphere.restype = c_bool

check_collision_ray_sphere = _raylib.CheckCollisionRaySphere
check_collision_ray_sphere.argtypes = [Ray, Vector3, c_float]
check_collision_ray_sphere.restype = c_bool

check_collision_ray_sphere_ex = _raylib.CheckCollisionRaySphereEx
check_collision_ray_sphere_ex.argtypes = [Ray, Vector3, c_float, POINTER(Vector3)]
check_collision_ray_sphere_ex.restype = c_bool

check_collision_ray_box = _raylib.CheckCollisionRayBox
check_collision_ray_box.argtypes = [Ray, BoundingBox]
check_collision_ray_box.restype = c_bool

check_collision_ray_model = _raylib.GetCollisionRayModel
check_collision_ray_model.argtypes = [Ray, POINTER(Mesh)]
check_collision_ray_model.restype = RayHitInfo

check_collision_ray_triangle = _raylib.GetCollisionRayTriangle
check_collision_ray_triangle.argtypes = [Ray, Vector3, Vector3, Vector3]
check_collision_ray_triangle.restype = RayHitInfo

check_collision_ray_ground = _raylib.GetCollisionRayGround
check_collision_ray_ground.argtypes = [Ray, c_float]
check_collision_ray_ground.restype = RayHitInfo


# SHADERS SYSTEM FUNCTIONS
# MODULE: rlgl
# NOTE: This functions are useless when using OpenGL 1.1
# -------------------------------------------------------------------

# Shader loading/unloading functions
load_text = _raylib.LoadText
load_text.argtypes = _ct('c')
load_text.restype = c_char_p

load_shader = _raylib.LoadShader
load_shader.argtypes = _ct('cc')
load_shader.restype = Shader

load_shader = _raylib.LoadShaderCode
load_shader.argtypes = _ct('cc')
load_shader.restype = Shader

unload_shader = _raylib.UnloadShader
unload_shader.argtypes = [Shader]
unload_shader.restype = None

get_shader_default = _raylib.GetShaderDefault
get_shader_default.argtypes = _NOARGS
get_shader_default.restype = Shader

get_texture_default = _raylib.GetTextureDefault
get_texture_default.argtypes = _NOARGS
get_texture_default.restype = Texture2D


# Shader configuration functions
get_shader_location = _raylib.GetShaderLocation
get_shader_location.argtypes = [Shader, c_char_p]
get_shader_location.restype = c_int

set_shader_value = _raylib.SetShaderValue
set_shader_value.argtypes = [Shader] + _ct('if*i')
set_shader_value.restype = None

set_shader_value_i = _raylib.SetShaderValuei
set_shader_value_i.argtypes = [Shader] + _ct('ii*i')
set_shader_value_i.restype = None

set_shader_value_matrix = _raylib.SetShaderValueMatrix
set_shader_value_matrix.argtypes = [Shader, c_int, Matrix]
set_shader_value_matrix.restype = None

set_matrix_projection = _raylib.SetMatrixProjection
set_matrix_projection.argtypes = [Matrix]
set_matrix_projection.restype = None

set_matrix_modelview = _raylib.SetMatrixModelview
set_matrix_modelview.argtypes = [Matrix]
set_matrix_modelview.restype = None

get_matrix_modelview = _raylib.GetMatrixModelview
get_matrix_modelview.argtypes = _NOARGS
get_matrix_modelview.restype = Matrix


# Texture maps generation (PBR)
# NOTE: Required shaders should be provided
gen_texture_cubemap = _raylib.GenTextureCubemap
gen_texture_cubemap.argtypes = [Shader, Texture2D, c_int]
gen_texture_cubemap.restype = Texture2D

gen_texture_irradiance = _raylib.GenTextureIrradiance
gen_texture_irradiance.argtypes = [Shader, Texture2D, c_int]
gen_texture_irradiance.restype = Texture2D

gen_texture_prefilter = _raylib.GenTexturePrefilter
gen_texture_prefilter.argtypes = [Shader, Texture2D, c_int]
gen_texture_prefilter.restype = Texture2D

gen_texture_brdf = _raylib.GenTextureBRDF
gen_texture_brdf.argtypes = [Shader, Texture2D, c_int]
gen_texture_brdf.restype = Texture2D


# Shading begin/end functions
begin_shader_mode = _raylib.BeginShaderMode
begin_shader_mode.argtypes = [Shader]
begin_shader_mode.restype = None

end_shader_mode = _raylib.EndShaderMode
end_shader_mode.argtypes = _NOARGS
end_shader_mode.restype = None

begin_blend_mode = _raylib.BeginBlendMode
begin_blend_mode.argtypes = [c_int]
begin_blend_mode.restype = None

end_blend_mode = _raylib.EndBlendMode
end_blend_mode.argtypes = _NOARGS
end_blend_mode.restype = None


# VR control functions
get_vr_devide_info = _raylib.GetVrDeviceInfo
get_vr_devide_info.argtypes = [c_int]
get_vr_devide_info.restype = VrDeviceInfo

init_vr_simulator = _raylib.InitVrSimulator
init_vr_simulator.argtypes = [VrDeviceInfo]
init_vr_simulator.restype = None

close_vr_simulator = _raylib.CloseVrSimulator
close_vr_simulator.argtypes = _NOARGS
close_vr_simulator.restype = None

is_vr_simulator_ready = _raylib.IsVrSimulatorReady
is_vr_simulator_ready.argtypes = _NOARGS
is_vr_simulator_ready.restype = c_bool

set_vr_distortion_shader = _raylib.SetVrDistortionShader
set_vr_distortion_shader.argtypes = [Shader]
set_vr_distortion_shader.restype = None

update_vr_tracking = _raylib.UpdateVrTracking
update_vr_tracking.argtypes = [POINTER(Camera)]
update_vr_tracking.restype = None

toggle_vr_mode = _raylib.ToggleVrMode
toggle_vr_mode.argtypes = _NOARGS
toggle_vr_mode.restype = None

begin_vr_drawing = _raylib.BeginVrDrawing
begin_vr_drawing.argtypes = _NOARGS
begin_vr_drawing.restype = None

end_vr_drawing = _raylib.EndVrDrawing
end_vr_drawing.argtypes = _NOARGS
end_vr_drawing.restype = None


# AUDIO LOADING AND PLAYING FUNCTIONS
# MODULE: audio
# -------------------------------------------------------------------

# Audio device management functions
init_audio_device = _raylib.InitAudioDevice
init_audio_device.argtypes = _NOARGS
init_audio_device.restype = None

close_audio_device = _raylib.CloseAudioDevice
close_audio_device.argtypes = _NOARGS
close_audio_device.restype = None

is_audio_device_ready = _raylib.IsAudioDeviceReady
is_audio_device_ready.argtypes = _NOARGS
is_audio_device_ready.restype = c_bool

set_master_volume = _raylib.SetMasterVolume
set_master_volume.argtypes = [c_float]
set_master_volume.restype = None


# Wave/sound loading/unloading functions
load_wave = _raylib.LoadWave
load_wave.argtypes = [c_char_p]
load_wave.restype = Wave

load_wave_ex = _raylib.LoadWaveEx
load_wave_ex.argtypes = _ct('Piiii')
load_wave_ex.restype = Wave

load_sound = _raylib.LoadSound
load_sound.argtypes = [c_char_p]
load_sound.restype = Sound

load_sound_from_wave = _raylib.LoadSoundFromWave
load_sound_from_wave.argtypes = [Wave]
load_sound_from_wave.restype = Sound

update_sound = _raylib.UpdateSound
update_sound.argtypes = [Sound] + _ct('Pi')
update_sound.restype = None

unload_wave = _raylib.UnloadWave
unload_wave.argtypes = [Wave]
unload_wave.restype = None

unload_sound = _raylib.UnloadSound
unload_sound.argtypes = [Sound]
unload_sound.restype = None


# Wave/Sound management functions
play_sound = _raylib.PlaySound
play_sound.argtypes = [Sound]
play_sound.restype = None

pause_sound = _raylib.PauseSound
pause_sound.argtypes = [Sound]
pause_sound.restype = None

resume_sound = _raylib.ResumeSound
resume_sound.argtypes = [Sound]
resume_sound.restype = None

stop_sound = _raylib.StopSound
stop_sound.argtypes = [Sound]
stop_sound.restype = None

is_sound_playing = _raylib.IsSoundPlaying
is_sound_playing.argtypes = [Sound]
is_sound_playing.restype = c_bool

set_sound_volume = _raylib.SetSoundVolume
set_sound_volume.argtypes = [Sound, c_float]
set_sound_volume.restype = None

set_sound_pitch = _raylib.SetSoundPitch
set_sound_pitch.argtypes = [Sound, c_float]
set_sound_pitch.restype = None

wave_format = _raylib.WaveFormat
wave_format.argtypes = [POINTER(Wave)] + _ct('iii')
wave_format.restype = None

wave_copy = _raylib.WaveCopy
wave_copy.argtypes = [Wave]
wave_copy.restype = Wave

wave_crop = _raylib.WaveCrop
wave_crop.argtypes = [POINTER(Wave)] + _ct('ii')
wave_crop.restype = None

get_wave_data = _raylib.GetWaveData
get_wave_data.argtypes = [Wave]
get_wave_data.restype = POINTER(c_float)


# Music management functions
load_music_stream = _raylib.LoadMusicStream
load_music_stream.argtypes = [c_char_p]
load_music_stream.restype = Music

unload_music_stream = _raylib.UnloadMusicStream
unload_music_stream.argtypes = [Music]
unload_music_stream.restype = None

play_music_stream = _raylib.PlayMusicStream
play_music_stream.argtypes = [Music]
play_music_stream.restype = None

update_music_stream = _raylib.UpdateMusicStream
update_music_stream.argtypes = [Music]
update_music_stream.restype = None

stop_music_stream = _raylib.StopMusicStream
stop_music_stream.argtypes = [Music]
stop_music_stream.restype = None

pause_music_stream = _raylib.PauseMusicStream
pause_music_stream.argtypes = [Music]
pause_music_stream.restype = None

resume_music_stream = _raylib.ResumeMusicStream
resume_music_stream.argtypes = [Music]
resume_music_stream.restype = None

is_music_playing = _raylib.IsMusicPlaying
is_music_playing.argtypes = [Music]
is_music_playing.restype = c_bool

set_music_volume = _raylib.SetMusicVolume
set_music_volume.argtypes = [Music, c_float]
set_music_volume.restype = None

set_music_pitch = _raylib.SetMusicPitch
set_music_pitch.argtypes = [Music, c_float]
set_music_pitch.restype = None

set_music_loop_count = _raylib.SetMusicLoopCount
set_music_loop_count.argtypes = [Music, c_float]
set_music_loop_count.restype = None

get_music_time_length = _raylib.GetMusicTimeLength
get_music_time_length.argtypes = [Music]
get_music_time_length.restype = c_float

get_music_time_played = _raylib.GetMusicTimePlayed
get_music_time_played.argtypes = [Music]
get_music_time_played.restype = c_float


# AudioStream management functions
init_audio_stream = _raylib.InitAudioStream
init_audio_stream.argtypes = _ct('III')
init_audio_stream.restype = AudioStream

update_audio_stream = _raylib.UpdateAudioStream
update_audio_stream.argtypes = [AudioStream] + _ct('Pi')
update_audio_stream.restype = None

close_audio_stream = _raylib.CloseAudioStream
close_audio_stream.argtypes = [AudioStream]
close_audio_stream.restype = None

is_audio_buffer_processed = _raylib.IsAudioBufferProcessed
is_audio_buffer_processed.argtypes = [AudioStream]
is_audio_buffer_processed.restype = c_bool

play_audio_stream = _raylib.PlayAudioStream
play_audio_stream.argtypes = [AudioStream]
play_audio_stream.restype = None

pause_audio_stream = _raylib.PauseAudioStream
pause_audio_stream.argtypes = [AudioStream]
pause_audio_stream.restype = None

resume_audio_stream = _raylib.ResumeAudioStream
resume_audio_stream.argtypes = [AudioStream]
resume_audio_stream.restype = None

is_audio_stream_playing = _raylib.IsAudioStreamPlaying
is_audio_stream_playing.argtypes = [AudioStream]
is_audio_stream_playing.restype = c_bool

stop_audio_stream = _raylib.StopAudioStream
stop_audio_stream.argtypes = [AudioStream]
stop_audio_stream.restype = None

set_audio_stream_volume = _raylib.SetAudioStreamVolume
set_audio_stream_volume.argtypes = [AudioStream, c_float]
set_audio_stream_volume.restype = None

set_audio_stream_pitch = _raylib.SetAudioStreamPitch
set_audio_stream_pitch.argtypes = [AudioStream, c_float]
set_audio_stream_pitch.restype = None


del os, _ct, _raylib, _NOARGS
del (
    c_bool,
    c_char_p,
    c_byte,
    c_ubyte,
    c_int,
    c_int32,
    c_uint,
    c_uint32,
    c_short,
    c_ushort,
    c_void_p,
    c_ssize_t,
    c_size_t,
    c_float,
    c_double,
    POINTER,
    CDLL,
    Structure,
)

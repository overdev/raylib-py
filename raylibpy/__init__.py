import sys
import os
import colorsys
from math import modf
from enum import IntEnum, IntFlag
from typing import Tuple, List, Union, Sequence, AnyStr, Optional, Iterator, Type
from ctypes import (
    c_bool,
    c_char_p,
    c_byte,
    c_ubyte,
    c_int,
    # c_int32,
    c_uint,
    # c_uint32,
    c_short,
    c_ushort,
    c_void_p,
    # c_ssize_t,
    # c_size_t,
    c_float,
    c_double,
    POINTER,
    CDLL,
    Structure,
    byref
)

_lib_filename = {
    'win32': 'libraylib_shared.dll',
    'linux': 'libraylib.so.2.0.0',
    'darwin': 'libraylib.2.0.0.dylib',
}
_platform = sys.platform

ENABLE_V2_0_0_FEATURE_DRAWTEXTURENPATCH = False
ENABLE_V2_0_0_FEATURE_CLIPRECT = False

if "ENABLE_V2_0_0_FEATURE_DRAWTEXTURENPATCH" in os.environ:
    ENABLE_V2_0_0_FEATURE_DRAWTEXTURENPATCH = True

if "ENABLE_V2_0_0_FEATURE_CLIPRECT" in os.environ:
    ENABLE_V2_0_0_FEATURE_CLIPRECT = True

RAYLIB_BIN_PATH = None
if "RAYLIB_BIN_PATH" in os.environ:
    env_path = os.environ['RAYLIB_BIN_PATH']
    if env_path == '__main__':
        RAYLIB_BIN_PATH = os.path.dirname(sys.modules['__main__'].__file__)
    elif env_path == '__file__':
        RAYLIB_BIN_PATH = os.path.abspath(os.path.dirname(__file__))
    elif os.path.exists(env_path) and os.path.isdir(env_path):
        RAYLIB_BIN_PATH = env_path
else:
    first_path = os.path.abspath(os.path.dirname(__file__))
    second_path = os.path.dirname(sys.modules['__main__'].__file__)
    if os.path.exists(os.path.join(first_path, _lib_filename[_platform])):
        RAYLIB_BIN_PATH = first_path
    elif os.path.exists(os.path.join(second_path, _lib_filename[_platform])):
        RAYLIB_BIN_PATH = second_path
    else:
        s = ("'{}' is expected to be located\n"
            "in the directory specified by the environment variable\n"
            "RAYLIB_BIN_PATH, in the program's entry point (__main__)\n"
            "directory, or in the raylibpy package __init__ directory.\n"
            "The library file is not in any of these locations.")
        print(s.format(_lib_filename[_platform]))
        raise RuntimeError("Unable to find raylib library ('{}').".format(_lib_filename[_platform]))

if RAYLIB_BIN_PATH:
    _rl = CDLL(os.path.join(RAYLIB_BIN_PATH, _lib_filename[_platform]))


__all__ = [
    # CONSTANTS
    'PI',
    'DEG2RAD',
    'RAD2DEG',
    'FLAG_SHOW_LOGO',
    'FLAG_FULLSCREEN_MODE',
    'FLAG_WINDOW_RESIZABLE',
    'FLAG_WINDOW_UNDECORATED',
    'FLAG_WINDOW_TRANSPARENT',
    'FLAG_MSAA_4X_HINT',
    'FLAG_VSYNC_HINT',
    'KEY_SPACE',
    'KEY_ESCAPE',
    'KEY_ENTER',
    'KEY_TAB',
    'KEY_BACKSPACE',
    'KEY_INSERT',
    'KEY_DELETE',
    'KEY_RIGHT',
    'KEY_LEFT',
    'KEY_DOWN',
    'KEY_UP',
    'KEY_PAGE_UP',
    'KEY_PAGE_DOWN',
    'KEY_HOME',
    'KEY_END',
    'KEY_CAPS_LOCK',
    'KEY_SCROLL_LOCK',
    'KEY_NUM_LOCK',
    'KEY_PRINT_SCREEN',
    'KEY_PAUSE',
    'KEY_F1',
    'KEY_F2',
    'KEY_F3',
    'KEY_F4',
    'KEY_F5',
    'KEY_F6',
    'KEY_F7',
    'KEY_F8',
    'KEY_F9',
    'KEY_F10',
    'KEY_F11',
    'KEY_F12',
    'KEY_LEFT_SHIFT',
    'KEY_LEFT_CONTROL',
    'KEY_LEFT_ALT',
    'KEY_RIGHT_SHIFT',
    'KEY_RIGHT_CONTROL',
    'KEY_RIGHT_ALT',
    'KEY_GRAVE',
    'KEY_SLASH',
    'KEY_BACKSLASH',
    'KEY_ZERO',
    'KEY_ONE',
    'KEY_TWO',
    'KEY_THREE',
    'KEY_FOUR',
    'KEY_FIVE',
    'KEY_SIX',
    'KEY_SEVEN',
    'KEY_EIGHT',
    'KEY_NINE',
    'KEY_A',
    'KEY_B',
    'KEY_C',
    'KEY_D',
    'KEY_E',
    'KEY_F',
    'KEY_G',
    'KEY_H',
    'KEY_I',
    'KEY_J',
    'KEY_K',
    'KEY_L',
    'KEY_M',
    'KEY_N',
    'KEY_O',
    'KEY_P',
    'KEY_Q',
    'KEY_R',
    'KEY_S',
    'KEY_T',
    'KEY_U',
    'KEY_V',
    'KEY_W',
    'KEY_X',
    'KEY_Y',
    'KEY_Z',
    'KEY_BACK',
    'KEY_MENU',
    'KEY_VOLUME_UP',
    'KEY_VOLUME_DOWN',
    'MOUSE_LEFT_BUTTON',
    'MOUSE_RIGHT_BUTTON',
    'MOUSE_MIDDLE_BUTTON',
    'MAX_TOUCH_POINTS',
    'GAMEPAD_PLAYER1',
    'GAMEPAD_PLAYER2',
    'GAMEPAD_PLAYER3',
    'GAMEPAD_PLAYER4',
    'GAMEPAD_PS3_BUTTON_TRIANGLE',
    'GAMEPAD_PS3_BUTTON_CIRCLE',
    'GAMEPAD_PS3_BUTTON_CROSS',
    'GAMEPAD_PS3_BUTTON_SQUARE',
    'GAMEPAD_PS3_BUTTON_L1',
    'GAMEPAD_PS3_BUTTON_R1',
    'GAMEPAD_PS3_BUTTON_L2',
    'GAMEPAD_PS3_BUTTON_R2',
    'GAMEPAD_PS3_BUTTON_START',
    'GAMEPAD_PS3_BUTTON_SELECT',
    'GAMEPAD_PS3_BUTTON_UP',
    'GAMEPAD_PS3_BUTTON_RIGHT',
    'GAMEPAD_PS3_BUTTON_DOWN',
    'GAMEPAD_PS3_BUTTON_LEFT',
    'GAMEPAD_PS3_BUTTON_PS',
    'GAMEPAD_PS3_AXIS_LEFT_X',
    'GAMEPAD_PS3_AXIS_LEFT_Y',
    'GAMEPAD_PS3_AXIS_RIGHT_X',
    'GAMEPAD_PS3_AXIS_RIGHT_Y',
    'GAMEPAD_PS3_AXIS_L2',
    'GAMEPAD_PS3_AXIS_R2',
    'GAMEPAD_XBOX_BUTTON_A',
    'GAMEPAD_XBOX_BUTTON_B',
    'GAMEPAD_XBOX_BUTTON_X',
    'GAMEPAD_XBOX_BUTTON_Y',
    'GAMEPAD_XBOX_BUTTON_LB',
    'GAMEPAD_XBOX_BUTTON_RB',
    'GAMEPAD_XBOX_BUTTON_SELECT',
    'GAMEPAD_XBOX_BUTTON_START',
    'GAMEPAD_XBOX_BUTTON_UP',
    'GAMEPAD_XBOX_BUTTON_RIGHT',
    'GAMEPAD_XBOX_BUTTON_DOWN',
    'GAMEPAD_XBOX_BUTTON_LEFT',
    'GAMEPAD_XBOX_BUTTON_HOME',
    'GAMEPAD_ANDROID_DPAD_UP',
    'GAMEPAD_ANDROID_DPAD_DOWN',
    'GAMEPAD_ANDROID_DPAD_LEFT',
    'GAMEPAD_ANDROID_DPAD_RIGHT',
    'GAMEPAD_ANDROID_DPAD_CENTER',
    'GAMEPAD_ANDROID_BUTTON_A',
    'GAMEPAD_ANDROID_BUTTON_B',
    'GAMEPAD_ANDROID_BUTTON_C',
    'GAMEPAD_ANDROID_BUTTON_X',
    'GAMEPAD_ANDROID_BUTTON_Y',
    'GAMEPAD_ANDROID_BUTTON_Z',
    'GAMEPAD_ANDROID_BUTTON_L1',
    'GAMEPAD_ANDROID_BUTTON_R1',
    'GAMEPAD_ANDROID_BUTTON_L2',
    'GAMEPAD_ANDROID_BUTTON_R2',
    'MAX_SHADER_LOCATIONS',
    'MAX_MATERIAL_MAPS',

    # enumerations
    'LogType',
    'LOG_INFO',
    'LOG_WARNING',
    'LOG_ERROR',
    'LOG_DEBUG',
    'LOG_OTHER',
    'ShaderLocationIndex',
    'LOC_VERTEX_POSITION',
    'LOC_VERTEX_TEXCOORD01',
    'LOC_VERTEX_TEXCOORD02',
    'LOC_VERTEX_NORMAL',
    'LOC_VERTEX_TANGENT',
    'LOC_VERTEX_COLOR',
    'LOC_MATRIX_MVP',
    'LOC_MATRIX_MODEL',
    'LOC_MATRIX_VIEW',
    'LOC_MATRIX_PROJECTION',
    'LOC_VECTOR_VIEW',
    'LOC_COLOR_DIFFUSE',
    'LOC_COLOR_SPECULAR',
    'LOC_COLOR_AMBIENT',
    'LOC_MAP_ALBEDO',
    'LOC_MAP_METALNESS',
    'LOC_MAP_NORMAL',
    'LOC_MAP_ROUGHNESS',
    'LOC_MAP_OCCLUSION',
    'LOC_MAP_EMISSION',
    'LOC_MAP_HEIGHT',
    'LOC_MAP_CUBEMAP',
    'LOC_MAP_IRRADIANCE',
    'LOC_MAP_PREFILTER',
    'LOC_MAP_BRDF',
    'LOC_MAP_DIFFUSE',
    'LOC_MAP_SPECULAR',
    'TexmapIndex',
    'MAP_ALBEDO',
    'MAP_METALNESS',
    'MAP_NORMAL',
    'MAP_ROUGHNESS',
    'MAP_OCCLUSION',
    'MAP_EMISSION',
    'MAP_HEIGHT',
    'MAP_CUBEMAP',
    'MAP_IRRADIANCE',
    'MAP_PREFILTER',
    'MAP_BRDF',
    'MAP_DIFFUSE',
    'MAP_SPECULAR',
    'PixelFormat',
    'UNCOMPRESSED_GRAYSCALE',
    'UNCOMPRESSED_GRAY_ALPHA',
    'UNCOMPRESSED_R5G6B5',
    'UNCOMPRESSED_R8G8B8',
    'UNCOMPRESSED_R5G5B5A1',
    'UNCOMPRESSED_R4G4B4A4',
    'UNCOMPRESSED_R8G8B8A8',
    'UNCOMPRESSED_R32',
    'UNCOMPRESSED_R32G32B32',
    'UNCOMPRESSED_R32G32B32A32',
    'COMPRESSED_DXT1_RGB',
    'COMPRESSED_DXT1_RGBA',
    'COMPRESSED_DXT3_RGBA',
    'COMPRESSED_DXT5_RGBA',
    'COMPRESSED_ETC1_RGB',
    'COMPRESSED_ETC2_RGB',
    'COMPRESSED_ETC2_EAC_RGBA',
    'COMPRESSED_PVRT_RGB',
    'COMPRESSED_PVRT_RGBA',
    'COMPRESSED_ASTC_4x4_RGBA',
    'COMPRESSED_ASTC_8x8_RGBA',
    'TextureFilterMode',
    'FILTER_POINT',
    'FILTER_BILINEAR',
    'FILTER_TRILINEAR',
    'FILTER_ANISOTROPIC_4X',
    'FILTER_ANISOTROPIC_8X',
    'FILTER_ANISOTROPIC_16X',
    'TextureWrapMode',
    'WRAP_REPEAT',
    'WRAP_CLAMP',
    'WRAP_MIRROR',
    'BlendMode',
    'BLEND_ALPHA',
    'BLEND_ADDITIVE',
    'BLEND_MULTIPLIED',
    'Gestures',
    'GESTURE_NONE',
    'GESTURE_TAP',
    'GESTURE_DOUBLETAP',
    'GESTURE_HOLD',
    'GESTURE_DRAG',
    'GESTURE_SWIPE_RIGHT',
    'GESTURE_SWIPE_LEFT',
    'GESTURE_SWIPE_UP',
    'GESTURE_SWIPE_DOWN',
    'GESTURE_PINCH_IN',
    'GESTURE_PINCH_OUT',
    'CameraMode',
    'CAMERA_CUSTOM',
    'CAMERA_FREE',
    'CAMERA_ORBITAL',
    'CAMERA_FIRST_PERSON',
    'CAMERA_THIRD_PERSON',
    'CameraType',
    'CAMERA_PERSPECTIVE',
    'CAMERA_ORTHOGRAPHIC',
    'VrDeviceType',
    'HMD_DEFAULT_DEVICE',
    'HMD_OCULUS_RIFT_DK2',
    'HMD_OCULUS_RIFT_CV1',
    'HMD_OCULUS_GO',
    'HMD_VALVE_HTC_VIVE',
    'HMD_SONY_PSVR',
    'NPatchType',
    'NPT_9PATCH',
    'NPT_3PATCH_VERTICAL',
    'NPT_3PATCH_HORIZONTAL',

    # raylib types
    'AudioStream',
    'BoundingBox',
    'Camera',
    'CameraPtr',
    'Camera2D',
    'Camera3D',
    'Camera3DPtr',
    'CharInfo',
    'CharInfoPtr',
    'Color',
    'ColorPtr',
    'Font',
    'Image',
    'ImagePtr',
    'Material',
    'MaterialMap',
    'Matrix',
    'Mesh',
    'MeshPtr',
    'Model',
    'ModelPtr',
    'Music',
    'MusicData',
    'Ray',
    'RayHitInfo',
    'Rectangle',
    'RenderTexture',
    'RenderTexture2D',
    'NPatchInfo',
    'Shader',
    'Sound',
    'SpriteFont',
    'Texture',
    'Texture2D',
    'Texture2DPtr',
    'Vector2',
    'Vector2Ptr',
    'Vector3',
    'Vector3Ptr',
    'Vector4',
    'Vector4Ptr',
    'VrDeviceInfo',
    'Wave',
    'WavePtr',
    # C types
    'Bool',
    'VoidPtr',
    'CharPtr',
    'CharPtrPrt',
    'UCharPtr',
    'IntPtr',
    'UIntPtr',
    'FloatPtr',
    'Char',
    'UChar',
    'Byte',
    'Short',
    'Int',
    'UInt',
    'Float',
    'Double',
    # Module: CORE
    # window
    'init_window',
    'close_window',
    'is_window_ready',
    'window_should_close',
    'is_window_minimized',
    'toggle_fullscreen',
    'set_window_icon',
    'set_window_title',
    'set_window_position',
    'set_window_monitor',
    'set_window_min_size',
    'set_window_size',
    'get_screen_width',
    'get_screen_height',
    'show_cursor',
    'hide_cursor',
    'is_cursor_hidden',
    'enable_cursor',
    'disable_cursor',
    'clear_background',
    'begin_drawing',
    'end_drawing',
    'begin_mode2d',
    'end_mode2d',
    'begin_mode3d',
    'end_mode3d',
    'begin_texture_mode',
    'end_texture_mode',
    'get_mouse_ray',
    'get_world_to_screen',
    'get_camera_matrix',
    'set_target_fps',
    'get_fps',
    'get_frame_time',
    'get_time',
    'color_to_int',
    'color_normalize',
    'color_to_hsv',
    'get_color',
    'fade',
    'show_logo',
    'set_config_flags',
    'set_trace_log',
    'trace_log',
    'take_screenshot',
    'get_random_value',
    'is_file_extension',
    'get_extension',
    'get_file_name',
    'get_directory_path',
    'get_working_directory',
    'change_directory',
    'is_file_dropped',
    'get_dropped_files',
    'clear_dropped_files',
    'storage_save_value',
    'storage_load_value',
    # input
    'is_key_pressed',
    'is_key_down',
    'is_key_released',
    'is_key_up',
    'get_key_pressed',
    'set_exit_key',
    'is_gamepad_available',
    'is_gamepad_name',
    'get_gamepad_name',
    'is_gamepad_button_pressed',
    'is_gamepad_button_down',
    'is_gamepad_button_released',
    'is_gamepad_button_up',
    'get_gamepad_button_pressed',
    'get_gamepad_axis_count',
    'get_gamepad_axis_movement',
    'is_mouse_button_pressed',
    'is_mouse_button_down',
    'is_mouse_button_released',
    'is_mouse_button_up',
    'get_mouse_x',
    'get_mouse_y',
    'get_mouse_position',
    'set_mouse_position',
    'set_mouse_scale',
    'get_mouse_wheel_move',
    'get_touch_x',
    'get_touch_y',
    'get_touch_position',

    # Module: GESTURES
    'set_gestures_enabled',
    'is_gesture_detected',
    'get_gesture_detected',
    'get_touch_points_count',
    'get_gesture_hold_duration',
    'get_gesture_drag_vector',
    'get_gesture_drag_angle',
    'get_gesture_pinch_vector',
    'get_gesture_pinch_angle',

    # Module: CAMERA
    'set_camera_mode',
    'update_camera',
    'set_camera_pan_control',
    'set_camera_alt_control',
    'set_camera_smooth_zoom_control',
    'set_camera_move_controls',

    # Module: SHAPES
    'draw_pixel',
    'draw_pixel_v',
    'draw_line',
    'draw_line_v',
    'draw_line_ex',
    'draw_line_bezier',
    'draw_circle',
    'draw_circle_gradient',
    'draw_circle_v',
    'draw_circle_lines',
    'draw_rectangle',
    'draw_rectangle_v',
    'draw_rectangle_rec',
    'draw_rectangle_pro',
    'draw_rectangle_gradient_v',
    'draw_rectangle_gradient_h',
    'draw_rectangle_gradient_ex',
    'draw_rectangle_lines',
    'draw_rectangle_lines_ex',
    'draw_triangle',
    'draw_triangle_lines',
    'draw_poly',
    'draw_poly_ex',
    'draw_poly_ex_lines',
    # Basic shapes collision detection functions
    'check_collision_recs',
    'check_collision_circles',
    'check_collision_circle_rec',
    'get_collision_rec',
    'check_collision_point_rec',
    'check_collision_point_circle',
    'check_collision_point_triangle',

    # Module: TEXTURES
    'load_image',
    'load_image_ex',
    'load_image_pro',
    'load_image_raw',
    'export_image',
    'load_texture',
    'load_texture_from_image',
    'load_render_texture',
    'unload_image',
    'unload_texture',
    'unload_render_texture',
    'get_image_data',
    'get_image_data_normalized',
    'get_pixel_data_size',
    'get_texture_data',
    'update_texture',
    'image_copy',
    'image_to_pot',
    'image_format',
    'image_alpha_mask',
    'image_alpha_clear',
    'image_alpha_crop',
    'image_alpha_premultiply',
    'image_crop',
    'image_resize',
    'image_resize_nn',
    'image_resize_canvas',
    'image_mipmaps',
    'image_dither',
    'image_text',
    'image_text_ex',
    'image_draw',
    'image_draw_rectangle',
    'image_draw_text',
    'image_draw_text_ex',
    'image_flip_vertical',
    'image_flip_horizontal',
    'image_rotate_cw',
    'image_rotate_ccw',
    'image_color_tint',
    'image_color_invert',
    'image_color_grayscale',
    'image_color_contrast',
    'image_color_brightness',
    'image_color_replace',
    'gen_image_color',
    'gen_image_gradient_v',
    'gen_image_gradient_h',
    'gen_image_gradient_radial',
    'gen_image_checked',
    'gen_image_white_noise',
    'gen_image_perlin_noise',
    'gen_image_cellular',
    'gen_texture_mipmaps',
    'set_texture_filter',
    'set_texture_wrap',
    'draw_texture',
    'draw_texture_v',
    'draw_texture_ex',
    'draw_texture_rec',
    'draw_texture_pro',
    'draw_texture_npatch',

    # Module: TEXT
    'get_font_default',
    'load_font',
    'load_font_ex',
    'load_font_data',
    'gen_image_font_atlas',
    'unload_font',
    'draw_fps',
    'draw_text',
    'draw_text_ex',
    'measure_text',
    'measure_text_ex',
    'format_text',
    'sub_text',
    'get_glyph_index',

    # Module: MODELS
    'draw_line3_d',
    'draw_circle3_d',
    'draw_cube',
    'draw_cube_v',
    'draw_cube_wires',
    'draw_cube_texture',
    'draw_sphere',
    'draw_sphere_ex',
    'draw_sphere_wires',
    'draw_cylinder',
    'draw_cylinder_wires',
    'draw_plane',
    'draw_ray',
    'draw_grid',
    'draw_gizmo',
    'load_model',
    'load_model_from_mesh',
    'unload_model',
    'load_mesh',
    'unload_mesh',
    'export_mesh',
    'mesh_bounding_box',
    'mesh_tangents',
    'mesh_binormals',
    'gen_mesh_plane',
    'gen_mesh_cube',
    'gen_mesh_sphere',
    'gen_mesh_hemi_sphere',
    'gen_mesh_cylinder',
    'gen_mesh_torus',
    'gen_mesh_knot',
    'gen_mesh_heightmap',
    'gen_mesh_cubicmap',
    'load_material',
    'load_material_default',
    'unload_material',
    'draw_model',
    'draw_model_ex',
    'draw_model_wires',
    'draw_model_wires_ex',
    'draw_bounding_box',
    'draw_billboard',
    'draw_billboard_rec',
    'check_collision_spheres',
    'check_collision_boxes',
    'check_collision_box_sphere',
    'check_collision_ray_sphere',
    'check_collision_ray_sphere_ex',
    'check_collision_ray_box',
    'get_collision_ray_model',
    'get_collision_ray_triangle',
    'get_collision_ray_ground',

    # Module: RLGL
    'load_text',
    'load_shader',
    'load_shader_code',
    'unload_shader',
    'get_shader_default',
    'get_texture_default',
    'get_shader_location',
    'set_shader_value',
    'set_shader_valuei',
    'set_shader_value_matrix',
    'set_matrix_projection',
    'set_matrix_modelview',
    'get_matrix_modelview',
    'gen_texture_cubemap',
    'gen_texture_irradiance',
    'gen_texture_prefilter',
    'gen_texture_brdf',
    'begin_shader_mode',
    'end_shader_mode',
    'begin_blend_mode',
    'begin_clip_rec',
    'end_clip_rec',
    'end_blend_mode',
    'get_vr_device_info',
    'init_vr_simulator',
    'close_vr_simulator',
    'is_vr_simulator_ready',
    'set_vr_distortion_shader',
    'update_vr_tracking',
    'toggle_vr_mode',
    'begin_vr_drawing',
    'end_vr_drawing',

    # Module: AUDIO
    'init_audio_device',
    'close_audio_device',
    'is_audio_device_ready',
    'set_master_volume',
    'load_wave',
    'load_wave_ex',
    'load_sound',
    'load_sound_from_wave',
    'update_sound',
    'unload_wave',
    'unload_sound',
    'play_sound',
    'pause_sound',
    'resume_sound',
    'stop_sound',
    'is_sound_playing',
    'set_sound_volume',
    'set_sound_pitch',
    'wave_format',
    'wave_copy',
    'wave_crop',
    'get_wave_data',
    'load_music_stream',
    'unload_music_stream',
    'play_music_stream',
    'update_music_stream',
    'stop_music_stream',
    'pause_music_stream',
    'resume_music_stream',
    'is_music_playing',
    'set_music_volume',
    'set_music_pitch',
    'set_music_loop_count',
    'get_music_time_length',
    'get_music_time_played',
    'init_audio_stream',
    'update_audio_stream',
    'close_audio_stream',
    'is_audio_buffer_processed',
    'play_audio_stream',
    'pause_audio_stream',
    'resume_audio_stream',
    'is_audio_stream_playing',
    'stop_audio_stream',
    'set_audio_stream_volume',
    'set_audio_stream_pitch',

    # Colors
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

    'byref',
]


# -----------------------------------------------------------------------------------
# Package utility functions and types
# ----------------------------------------------------------------------------------

Bool = c_bool
VoidPtr = c_void_p
CharPtr = c_char_p
CharPtrPrt = POINTER(c_char_p)
UCharPtr = POINTER(c_ubyte)
IntPtr = POINTER(c_int)
UIntPtr = POINTER(c_uint)
FloatPtr = POINTER(c_float)
Char = c_byte
UChar = c_ubyte
Byte = c_byte
Short = c_short
Int = c_int
UInt = c_uint
Float = c_float
Double = c_double

Number = Union[int, float]
Seq = Sequence[Number]
VectorN = Union[Seq, 'Vector4', 'Vector3', 'Vector2']

def _float(value) -> float:
    return float(value) if isinstance(value, int) else value


def _int(value) -> int:
    return int(value) if isinstance(value, float) else value


def _str_in(value: bytes) -> str:
    return value.encode('utf-8', 'ignore') if isinstance(value, str) else value


def _str_out(value: str) -> bytes:
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


def _vec2(seq: Sequence[Number]) -> 'Vector2':
    if isinstance(seq, Vector2):
        return seq
    x, y = seq
    return Vector2(_float(x), _float(y))


def _vec3(seq: Sequence[Number]) -> 'Vector3':
    if isinstance(seq, Vector3):
        return seq
    x, y, z = seq
    return Vector3(_float(x), _float(y), _float(z))


def _vec4(seq: Sequence[Number]) -> 'Vector3':
    if isinstance(seq, Vector4):
        return seq
    x, y, z, w = seq
    return Vector4(_float(x), _float(y), _float(z), _float(w))


def _rect(seq: Sequence[Number]) -> 'Rectangle':
    if isinstance(seq, Rectangle):
        return seq
    x, y, w, h = seq
    return Rectangle(_float(x), _float(y), _float(w), _float(h))


def _color(seq: Sequence[Number]) -> 'Color':
    if isinstance(seq, Color):
        return seq
    r, g, b, q = seq
    return Color(_float(r), _float(r), _float(b), _float(q))


def _attr_swizzle(attr: str, size: int, write: bool=False) -> Tuple[bool, str]:
    if len(attr) not in (1, 2, 3, 4):
        return False, "Wrong number of components to swizzle (must be 1, 2, 3 or 4; not {}).".format(len(attr))
    if size not in (2, 3, 4):
        return False, "Wrong vector size (must be 2, 3 or 4; not {}).".format(size)

    groups = ['xyzw', 'uv', 'rgba']
    if size == 3:
        groups = ['xyz', 'uv', 'rgb']
    elif size == 2:
        groups = ['xy', 'uv', '']

    if attr[0] in groups[0]:
        group = 0
    elif attr[0] in groups[1]:
        group = 1
    elif attr[0] in groups[2]:
        group = 2
    else:
        return False, "Invalid component '{}' in swizzled Vector{} attribute.".format(attr[0], size)

    already_set = []
    result = ''
    for i, c in enumerate(attr):
        if c not in groups[group]:
            return False, "Invalid component '{}' in swizzled attribute.".format(c)
        if write and c in already_set:
            return False, "Component '{}' in swizzled attribute is set more than once.".format(c)
        if write:
            already_set.append(c)
        result += groups[0][groups[group].index(c)]
    return True, result


def _color_swizzle(attr: str, size: int, write: bool=False) -> Tuple[bool, str]:
    if len(attr) not in (1, 2, 3, 4):
        return False, "Wrong number of components to swizzle (must be 1, 2, 3 or 4; not {}).".format(len(attr))
    if size not in (3, 4):
        return False, "Wrong vector size (must be 3 or 4; not {}).".format(size)

    groups = ['rgba']
    if size == 3:
        groups = ['rgb']

    if attr[0] in groups[0]:
        group = 0
    else:
        return False, "Invalid component '{}' in swizzled Color attribute.".format(attr[0])

    already_set = []
    result = ''
    for i, c in enumerate(attr):
        if c not in groups[group]:
            return False, "Invalid component '{}' in swizzled attribute.".format(c)
        if write and c in already_set:
            return False, "Component '{}' in swizzled attribute is set more than once.".format(c)
        if write:
            already_set.append(c)
        result += groups[0][groups[group].index(c)]
    return True, result


def _flatten(filter_types: List[Type], *values, map_to: Optional[Type]=None) -> list:
    result = []
    for v in values:
        if isinstance(v, filter_types):
            result.append(map_to(v) if map_to is not None else v)
        else:
            result.extend(_flatten(filter_types, *v, map_to=map_to))
    return result


_NOARGS = []

PI = 3.14159265358979323846

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

class _Vector2(Structure):
    """
    Wrapper for raylib Vector2 struct:
    
        typedef struct Vector2 {
            float x;
            float y;
        } Vector2;
    """
    _fields_ = [
        ('x', c_float),
        ('y', c_float)
    ]


class Vector2(_Vector2):

    @classmethod
    def zero(cls) -> 'Vector2':
        return Vector2(0., 0.)

    @classmethod
    def one(cls) -> 'Vector2':
        return Vector2(1., 1.)

    def __init__(self, *args) -> None:
        result = _flatten((int, float), *args, map_to=float)
        if len(result) != 2:
            raise ValueError("Too many or too few initializers ({} instead of 2).".format(len(result)))
        super(Vector2, self).__init__(*result)

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)

    def __repr__(self) -> str:
        return "{}({}, {})".format(self.__class__.__qualname__, self.x, self.y)

    def __getattr__(self, name: str) -> Union[float, 'Vector2', 'Vector3', 'Vector4']:
        is_valid, result = _attr_swizzle(name, 2)
        if is_valid:
            comps = {'x': self.x, 'y': self.y, 'z': 0.0, 'w': 0.0}
            n = len(result)
            v = [comps[comp] for comp in result]
            if n == 2:
                return Vector2(*v)
            if n == 3:
                return Vector3(*v)
            if n == 4:
                return Vector4(*v)

        raise AttributeError(result)

    def __setattr__(self, name: str, value: Union[float, 'Vector2', 'Vector3', 'Vector4']) -> None:
        is_valid, result = _attr_swizzle(name, 2, True)  # True for setattr, so components can't be set more than once.
        if is_valid:
            if len(name) == 1:
                v = float(value)
                super(Vector2, self).__setattr__(result, v)
            else:
                values = _flatten((int, float), *value, map_to=float)
                if len(name) != len(values):
                    raise ValueError("Too many or too few values ({} instead of {}".format(
                        len(values), len(name)
                    ))
                for i, c in enumerate(result):
                    super(Vector2, self).__setattr__(c, float(values[i]))
        else:
            raise AttributeError(result)

    def __len__(self) -> int:
        return 2

    def __iter__(self) -> Iterator[float]:
        return (self.x, self.y).__iter__()

    def __getitem__(self, key: Union[str, int, slice]) -> Union[float, Seq]:
        assert isinstance(key, (str, int, slice)), "KeyTypeError: {} not supported as subscription key.".format(key.__class__.__name__)

        if isinstance(key, (int, slice)):
            return [self.x, self.y][key]
        elif isinstance(key, str):
            return {'x': self.x, 'y': self.y}[key]

    def __setitem__(self, key: Union[str, int], value: Number) -> None:
        assert isinstance(key, (str, int)), "KeyTypeError: {} not supported as subscription key.".format(key.__class__.__name__)

        if isinstance(key, int):
            a = [self.x, self.y]
            a[key] = value
            self.x, self.y = a
        elif isinstance(key, str):
            a = {'x': self.x, 'y': self.y}
            assert key in a, "KeyError: invalid key '{}'.".format(key)
            a[key] = value
            self.x, self.y = tuple(a.values())

    def __pos__(self) -> 'Vector2':
        return Vector2(+self.x, +self.y)

    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __invert__(self) -> 'Vector2':
        return Vector2(~self.x, ~self.y)

    def __abs__(self) -> 'Vector2':
        return Vector2(abs(self.x), abs(self.y))

    def __add__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        other = _vec2(other) if not isinstance(other, Vector2) else other
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        other = _vec2(other) if not isinstance(other, Vector2) else other
        return Vector2(self.x - other.x, self.y - other.y)

    def __truediv__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        if isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)
        other = _vec2(other) if not isinstance(other, Vector2) else other
        return Vector2(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        if isinstance(other, (int, float)):
            return Vector2(float(self.x // other), float(self.y // other))
        other = _vec2(other) if not isinstance(other, Vector2) else other
        return Vector2(float(self.x // other.x), float(self.y // other.y))

    def __mod__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        if isinstance(other, (int, float)):
            return Vector2(self.x % other, self.y % other)
        other = _vec2(other) if not isinstance(other, Vector2) else other
        return Vector2(self.x % other.x, self.y % other.y)

    def __mul__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        other = _vec2(other) if not isinstance(other, Vector2) else other
        return Vector2(self.x * other.x, self.y * other.y)

    def __iadd__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        other = _vec2(other) if not isinstance(other, Vector2) else other
        self.x += other.x
        self.y += other.y

    def __isub__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        other = _vec2(other) if not isinstance(other, Vector2) else other
        self.x -= other.x
        self.y -= other.y

    def __itruediv__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        if isinstance(other, (int, float)):
            self.x /= other
            self.y /= other
        else:
            other = _vec2(other) if not isinstance(other, Vector2) else other
            self.x /= other.x
            self.y /= other.y
        return self

    def __ifloordiv__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        if isinstance(other, (int, float)):
            self.x = float(self.x // other)
            self.y = float(self.y // other)
        else:
            other = _vec2(other) if not isinstance(other, Vector2) else other
            self.x = float(self.x // other.x)
            self.y = float(self.y // other.y)
        return self

    def __imod__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        if isinstance(other, (int, float)):
            self.x %= other
            self.y %= other
        else:
            other = _vec2(other) if not isinstance(other, Vector2) else other
            self.x %= other.x
            self.y %= other.y
        return self

    def __imul__(self, other: Union['Vector2', Seq]) -> 'Vector2':
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
        else:
            other = _vec2(other) if not isinstance(other, Vector2) else other
            self.x *= other.x
            self.y *= other.y
        return self


Vector2Ptr = POINTER(Vector2)


class _Vector3(Structure):
    """
    Wrapper for raylib Vector3 struct:
    
        typedef struct Vector3 {
            float x;
            float y;
            float z;
        } Vector3;
    """
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
    ]


class Vector3(_Vector3):

    @classmethod
    def zero(cls) -> 'Vector3':
        return Vector3(0., 0., 0.)

    @classmethod
    def one(cls) -> 'Vector3':
        return Vector3(1., 1., 1.)

    def __init__(self, *args) -> None:
        result = _flatten((int, float), *args, map_to=float)
        if len(result) != 3:
            raise ValueError("Too many or too few initializers ({} instead of 3).".format(len(result)))
        super(Vector3, self).__init__(*result)

    def __str__(self) -> str:
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self) -> str:
        return "{}({}, {}, {})".format(self.__class__.__qualname__, self.x, self.y, self.z)

    def __getattr__(self, name: str) -> Union[float, 'Vector2', 'Vector3', 'Vector4']:
        is_valid, result = _attr_swizzle(name, 3)
        if is_valid:
            comps = {'x': self.x, 'y': self.y, 'z': self.z, 'w': 0.0}
            n = len(result)
            v = [comps[comp] for comp in result]
            if n == 2:
                return Vector2(*v)
            if n == 3:
                return Vector3(*v)
            if n == 4:
                return Vector4(*v)

        raise AttributeError(result)

    def __setattr__(self, name: str, value: Union[float, 'Vector2', 'Vector3', 'Vector4']) -> None:
        is_valid, result = _attr_swizzle(name, 3, True)  # True for setattr, so components can't be set more than once.
        if is_valid:
            if len(name) == 1:
                v = float(value)
                super(Vector3, self).__setattr__(result, v)
            else:
                values = _flatten((int, float), *value, map_to=float)
                if len(name) != len(values):
                    raise ValueError("Too many or too few values ({} instead of {}".format(
                        len(values), len(name)
                    ))
                for i, c in enumerate(result):
                    super(Vector3, self).__setattr__(c, float(values[i]))
        else:
            raise AttributeError(result)

    def __len__(self) -> int:
        return 3

    def __iter__(self) -> Iterator[float]:
        return (self.x, self.y, self.w).__iter__()

    def __getitem__(self, key: Union[str, int, slice]) -> Union[float, Seq]:
        assert isinstance(key, (str, int, slice)), "KeyTypeError: {} not supported as subscription key.".format(key.__class__.__name__)

        if isinstance(key, (int, slice)):
            return [self.x, self.y, self.z][key]
        elif isinstance(key, str):
            return {'x': self.x, 'y': self.y, 'z': self.z}[key]

    def __setitem__(self, key: Union[str, int], value: Number) -> None:
        assert isinstance(key, (str, int)), "KeyTypeError: {} not supported as subscription key.".format(key.__class__.__name__)

        if isinstance(key, int):
            a = [self.x, self.y, self.z]
            a[key] = value
            self.x, self.y, self.z = a
        elif isinstance(key, str):
            a = {'x': self.x, 'y': self.y, 'z': self.z}
            assert key in a, "KeyError: invalid key '{}'.".format(key)
            a[key] = value
            self.x, self.y, self.z = tuple(a.values())

    def __pos__(self) -> 'Vector3':
        return Vector3(+self.x, +self.y, -self.z)

    def __neg__(self) -> 'Vector3':
        return Vector3(-self.x, -self.y, +self.z)

    def __invert__(self) -> 'Vector3':
        return Vector3(~self.x, ~self.y, ~self.z)

    def __abs__(self) -> 'Vector3':
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def __add__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        other = _vec3(other) if not isinstance(other, Vector3) else other
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        other = _vec3(other) if not isinstance(other, Vector3) else other
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        if isinstance(other, (int, float)):
            return Vector3(self.x / other, self.y / other, self.z / other)
        other = _vec3(other) if not isinstance(other, Vector3) else other
        return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)

    def __floordiv__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        if isinstance(other, (int, float)):
            return Vector3(float(self.x // other), float(self.y // other), float(self.z // other))
        other = _vec3(other) if not isinstance(other, Vector3) else other
        return Vector3(float(self.x // other.x), float(self.y // other.y), float(self.z // other.z))

    def __mod__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        if isinstance(other, (int, float)):
            return Vector3(self.x % other, self.y % other, self.z % other)
        other = _vec3(other) if not isinstance(other, Vector3) else other
        return Vector3(self.x % other.x, self.y % other.y, self.z % other.z)

    def __mul__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        if isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        other = _vec3(other) if not isinstance(other, Vector3) else other
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __iadd__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        other = _vec3(other) if not isinstance(other, Vector3) else other
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        other = _vec3(other) if not isinstance(other, Vector3) else other
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __itruediv__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        if isinstance(other, (int, float)):
            self.x /= other
            self.y /= other
            self.z /= other
        else:
            other = _vec3(other) if not isinstance(other, Vector3) else other
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        return self

    def __ifloordiv__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        if isinstance(other, (int, float)):
            self.x = float(self.x // other)
            self.y = float(self.y // other)
            self.z = float(self.z // other)
        else:
            other = _vec3(other) if not isinstance(other, Vector3) else other
            self.x = float(self.x // other.x)
            self.y = float(self.y // other.y)
            self.z = float(self.z // other.z)
        return self

    def __imod__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        if isinstance(other, (int, float)):
            self.x %= other
            self.y %= other
            self.z %= other
        else:
            other = _vec3(other) if not isinstance(other, Vector3) else other
            self.x %= other.x
            self.y %= other.y
            self.z %= other.z
        return self

    def __imul__(self, other: Union['Vector3', Seq]) -> 'Vector3':
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            self.z *= other
        else:
            other = _vec3(other) if not isinstance(other, Vector3) else other
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        return self


Vector3Ptr = POINTER(Vector3)


class _Vector4(Structure):
    """
    Wrapper for raylib Vector4 struct:
    
        typedef struct Vector4 {
            float x;
            float y;
            float z;
            float w;
        } Vector4;
    """
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
        ('w', c_float),
    ]

class Vector4(_Vector4):

    @classmethod
    def zero(cls) -> 'Vector4':
        return Vector4(0., 0., 0., 1.)

    @classmethod
    def one(cls) -> 'Vector4':
        return Vector4(1., 1., 1., 1.)

    def __init__(self, *args) -> None:
        result = _flatten((int, float), *args, map_to=float)
        if len(result) != 4:
            raise ValueError("Too many or too few initializers ({} instead of 4).".format(len(result)))
        super(Vector4, self).__init__(*result)

    def __str__(self) -> str:
        return "({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)

    def __repr__(self) -> str:
        return "{}({}, {}, {}, {})".format(self.__class__.__qualname__, self.x, self.y, self.z, self.w)

    def __getattr__(self, name: str) -> Union[float, 'Vector2', 'Vector3', 'Vector4']:
        is_valid, result = _attr_swizzle(name, 4)
        if is_valid:
            comps = {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}
            n = len(result)
            v = [comps[comp] for comp in result]
            if n == 2:
                return Vector2(*v)
            if n == 3:
                return Vector3(*v)
            if n == 4:
                return Vector4(*v)

        raise AttributeError(result)

    def __setattr__(self, name: str, value: Union[float, 'Vector2', 'Vector3', 'Vector4']) -> None:
        is_valid, result = _attr_swizzle(name, 4, True)  # True for setattr, so components can't be set more than once.
        if is_valid:
            if len(name) == 1:
                v = float(value)
                super(Vector4, self).__setattr__(result, v)
            else:
                values = _flatten((int, float), *value, map_to=float)
                if len(name) != len(values):
                    raise ValueError("Too many or too few values ({} instead of {}".format(
                        len(values), len(name)
                    ))
                for i, c in enumerate(result):
                    super(Vector4, self).__setattr__(c, float(values[i]))
        else:
            raise AttributeError(result)

    def __len__(self) -> int:
        return 4

    def __iter__(self) -> Iterator[float]:
        return (self.x, self.y, self.w, self.z).__iter__()

    def __getitem__(self, key: Union[str, int, slice]) -> Union[float, Seq]:
        assert isinstance(key, (str, int, slice)), "KeyTypeError: {} not supported as subscription key.".format(key.__class__.__name__)

        if isinstance(key, (int, slice)):
            return [self.x, self.y, self.z, self.w][key]
        elif isinstance(key, str):
            return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}[key]

    def __setitem__(self, key: Union[str, int], value: Number) -> None:
        assert isinstance(key, (str, int)), "KeyTypeError: {} not supported as subscription key.".format(key.__class__.__name__)

        if isinstance(key, int):
            a = [self.x, self.y, self.z, self.w]
            a[key] = value
            self.x, self.y, self.z, self.w = a
        elif isinstance(key, str):
            a = {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}
            assert key in a, "KeyError: invalid key '{}'.".format(key)
            a[key] = value
            self.x, self.y, self.z, self.w = tuple(a.values())

    def __pos__(self) -> 'Vector4':
        return Vector4(+self.x, +self.y, -self.z, 1.)

    def __neg__(self) -> 'Vector4':
        return Vector4(-self.x, -self.y, +self.z, 1.)

    def __invert__(self) -> 'Vector4':
        return Vector4(~self.x, ~self.y, ~self.z, 1.)

    def __abs__(self) -> 'Vector4':
        return Vector4(abs(self.x), abs(self.y), abs(self.z), 1.)

    def __add__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        other = _vec4(other) if not isinstance(other, Vector4) else other
        return Vector4(self.x + other.x, self.y + other.y, self.z + other.z, 1.)

    def __sub__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        other = _vec4(other) if not isinstance(other, Vector4) else other
        return Vector4(self.x - other.x, self.y - other.y, self.z - other.z, 1.)

    def __truediv__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        if isinstance(other, (int, float)):
            return Vector4(self.x / other, self.y / other, self.z / other, 1.)
        other = _vec4(other) if not isinstance(other, Vector4) else other
        return Vector4(self.x / other.x, self.y / other.y, self.z / other.z, 1.)

    def __floordiv__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        if isinstance(other, (int, float)):
            return Vector4(float(self.x // other), float(self.y // other), float(self.z // other), 1.)
        other = _vec4(other) if not isinstance(other, Vector4) else other
        return Vector4(float(self.x // other.x), float(self.y // other.y), float(self.z // other.z), 1.)

    def __mod__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        if isinstance(other, (int, float)):
            return Vector4(self.x % other, self.y % other, self.z % other, 1.)
        other = _vec4(other) if not isinstance(other, Vector4) else other
        return Vector4(self.x % other.x, self.y % other.y, self.z % other.z, 1.)

    def __mul__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        if isinstance(other, (int, float)):
            return Vector4(self.x * other, self.y * other, self.z * other, 1.)
        other = _vec4(other) if not isinstance(other, Vector4) else other
        return Vector4(self.x * other.x, self.y * other.y, self.z * other.z, 1.)

    def __iadd__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        other = _vec4(other) if not isinstance(other, Vector4) else other
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        other = _vec4(other) if not isinstance(other, Vector4) else other
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __itruediv__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        if isinstance(other, (int, float)):
            self.x /= other
            self.y /= other
            self.z /= other
        else:
            other = _vec4(other) if not isinstance(other, Vector4) else other
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        return self

    def __ifloordiv__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        if isinstance(other, (int, float)):
            self.x = float(self.x // other)
            self.y = float(self.y // other)
            self.z = float(self.z // other)
        else:
            other = _vec4(other) if not isinstance(other, Vector4) else other
            self.x = float(self.x // other.x)
            self.y = float(self.y // other.y)
            self.z = float(self.z // other.z)
        return self

    def __imod__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        if isinstance(other, (int, float)):
            self.x %= other
            self.y %= other
            self.z %= other
        else:
            other = _vec4(other) if not isinstance(other, Vector4) else other
            self.x %= other.x
            self.y %= other.y
            self.z %= other.z
        return self

    def __imul__(self, other: Union['Vector4', Seq]) -> 'Vector4':
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            self.z *= other
        else:
            other = _vec4(other) if not isinstance(other, Vector4) else other
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        return self


Vector4Ptr = POINTER(Vector4)


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

    def __str__(self) -> str:
        return "(MATRIX: [{}, {}, {}, {}] [{}, {}, {}, {}] [{}, {}, {}, {}] [{}, {}, {}, {}])".format(
            self.m0, self.m4, self.m8, self.m12,
            self.m1, self.m5, self.m9, self.m13,
            self.m2, self.m6, self.m10, self.m14,
            self.m3, self.m7, self.m11, self.m15
        )


class _Color(Structure):
    _fields_ = [
        ('r', c_ubyte),
        ('g', c_ubyte),
        ('b', c_ubyte),
        ('a', c_ubyte),
    ]


class Color(_Color):

    @classmethod
    def zero(cls) -> 'Color':
        return cls(0, 0, 0, 255)

    @classmethod
    def one(cls) -> 'Color':
        return cls(255, 255, 255, 255)

    @classmethod
    def from_int(cls, value: int) -> 'Color':
        return get_color(max(0, value))

    def __init__(self, *args) -> None:
        """Constructor."""
        result = _flatten((int, float), *args, map_to=int)
        if len(result) != 4:
            raise ValueError("Too many or too few initializers ({} instead of 2).".format(len(result)))
        super(Color, self).__init__(*result)

    def __int__(self) -> int:
        """Packs the color into an integer."""
        return color_to_int(self)

    def __bytes__(self) -> bytes:
        return bytes(bytearray(self))

    def __str__(self) -> str:
        return "({}, {}, {}, {})".format(self.r, self.g, self.b, self.a)

    def __repr__(self) -> str:
        return "{}({}, {}, {}, {})".format(self.__class__.__qualname__, self.r, self.g, self.b, self.a)

    def __len__(self) -> int:
        return 4

    def __getattr__(self, name: str) -> Union[int, 'Color']:
        is_valid, result = _color_swizzle(name, 4)
        if is_valid:
            comps = {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}
            n = len(result)
            v = [comps[comp] for comp in result]
            if n == 2:
                return v[:2]
            if n == 3:
                return v[:3]
            if n == 4:
                return Color(*v)

        raise AttributeError(result)

    def __setattr__(self, name: str, value: Union[int, Seq, 'Color']) -> None:
        is_valid, result = _color_swizzle(name, 4, True)  # True for setattr, so components can't be set more than once.
        if is_valid:
            if len(name) == 1:
                v = int(value)
                super(Color, self).__setattr__(result, v)
            else:
                values = _flatten((int, float), *value, map_to=int)
                if len(name) != len(values):
                    raise ValueError("Too many or too few values ({} instead of {}".format(
                        len(values), len(name)
                    ))
                for i, c in enumerate(result):
                    super(Color, self).__setattr__(c, int(values[i]))
        else:
            raise AttributeError(result)

    def __getitem__(self, key: Union[str, int, slice]) -> Union[float, Seq]:
        assert isinstance(key, (str, int, slice)), "KeyTypeError: {} not supported as subscription key.".format(key.__class__.__name__)

        if isinstance(key, (int, slice)):
            return [self.r, self.g, self.b, self.a][key]
        elif isinstance(key, str):
            return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}[key]

    def __setitem__(self, key: Union[str, int], value: Number) -> None:
        assert isinstance(key, (str, int)), "KeyTypeError: {} not supported as subscription key.".format(key.__class__.__name__)

        if isinstance(key, int):
            a = [self.r, self.g, self.b, self.a]
            a[key] = value
            self.r, self.g, self.b, self.a = a
        elif isinstance(key, str):
            a = {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}
            assert key in a, "KeyError: invalid key '{}'.".format(key)
            a[key] = value
            self.r, self.g, self.b, self.a = tuple(a.values())

    @property
    def normalized(self) -> 'Vector4':
        """Gets or sets a normalized Vector4 color."""
        return Vector4(
            self.r / 255.0,
            self.g / 255.0,
            self.b / 255.0,
            self.a / 255.0
        )

    @normalized.setter
    def normalized(self, value: Union[Seq, Vector4, Vector3]) -> None:
        value = _flatten((int, float), *value, map_to=float)
        if len(result) not in (3, 4):
            raise ValueError("Too many or too few values (expected 3 or 4, not {})".format(len(result)))
            self.r = int(value[0] * 255.0)
            self.g = int(value[1] * 255.0)
            self.b = int(value[2] * 255.0)
            if len(value) == 4:
                self.a = int(value[3] * 255.0)

    @property
    def hsv(self) -> 'Vector4':
        """Gets a normalized color in HSV colorspace."""
        return Vector4(*colorsys.rgb_to_hsv(*self.normalized[:3]), self.a / 255.)

    @hsv.setter
    def hsv(self, value: Union[Seq, Vector4, Vector3]) -> None:
        result = _flatten((int, float), *value, map_to=float)
        if len(result) not in (3, 4):
            raise ValueError("Too many or too few values (expected 3 or 4, not {})".format(len(result)))
        self.normalized = colorsys.hsv_to_rgb(result[:3])

    @property
    def hls(self) -> 'Vector4':
        """Gets a normalized color in HLS colorspace."""
        return Vector4(*colorsys.rgb_to_hls(*self.normalized[:3]), self.a / 255.)

    @hls.setter
    def hls(self, value: Union[Seq, Vector4, Vector3]) -> None:
        result = _flatten((int, float), *value, map_to=float)
        if len(result) not in (3, 4):
            raise ValueError("Too many or too few values (expected 3 or 4, not {})".format(len(result)))
        self.normalized = colorsys.hls_to_rgb(result[:3])

    @property
    def yiq(self) -> 'Vector4':
        """Gets or sets a normalized color in YIQ colorspace."""
        return Vector4(*colorsys.rgb_to_yiq(*self.normalized[:3]), self.a / 255.)

    @yiq.setter
    def yiq(self, value: Union[Seq, Vector4, Vector3]) -> None:
        result = _flatten((int, float), *value, map_to=float)
        if len(result) not in (3, 4):
            raise ValueError("Too many or too few values (expected 3 or 4, not {})".format(len(result)))
        self.normalized = colorsys.yiq_to_rgb(result[:3])


ColorPtr = POINTER(Color)


class _Rectangle(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('width', c_float),
        ('height', c_float),
    ]


class Rectangle(_Rectangle):

    @classmethod
    def from_ltrb(cls, *args) -> 'Rectangle':
        """Alternate constructor."""
        result = _flatten((int, float), *args, map_to=float)
        if len(result) != 4:
            raise ValueError("Too many or too few initializers ({} instead of 4).".format(len(result)))

        l, t, r, b = result
        return cls(l, t, r - l, t - b)

    def __init__(self, *args) -> None:
        """Constructor."""
        result = _flatten((int, float), *args, map_to=float)
        if len(result) != 4:
            raise ValueError("Too many or too few initializers ({} instead of 4).".format(len(result)))
        super(Rectangle, self).__init__(*result)

    def __str__(self) -> str:
        return "({}, {}, {}, {})".format(self.x, self.y, self.width, self.height)

    def __repr__(self) -> str:
        return "{}({}, {}, {}, {})".format(self.__class__.__qualname__, self.x, self.y, self.width, self.height)

    @property
    def empty(self) -> bool:
        """Returns whether the rec's width or height is below or equal zero."""
        return self.width <= 0 or self.height <= 0

    @property
    def r(self) -> float:
        """Gets or sets the right-most rect coordinate."""
        return self.x + self.width
    
    @r.setter
    def r(self, value: float) -> None:
        self.x = float(value) - self.width

    @property
    def b(self) -> float:
        """Gets or sets the bottom-most rect coordinate."""
        return self.y + self.height
    
    @b.setter
    def b(self, value: float) -> None:
        self.y = float(value) - self.height

    @property
    def center(self) -> Vector2:
        """Gets or sets the rec position relative to its center."""
        return Vector2(self.x + self.width * 0.5,
                       self.y + self.height * 0.5)

    @center.setter
    def center(self, value: Union[Seq, Vector2]) -> None:
        self.pos = _vec2(value) - self.size * 0.5

    @property
    def pos(self) -> Vector2:
        """Gets or sets the rec top-left coordinate."""
        return Vector2(self.x, self.y)

    @pos.setter
    def pos(self, value: Union[Seq, Vector2]) -> None:
        self.x, self.y = map(float, value)

    @property
    def size(self) -> Vector2:
        """Gets or sets the rec dimensions."""
        return Vector2(self.width, self.height)

    @size.setter
    def size(self, value: Union[Seq, Vector2]) -> None:
        self.width, self.height = map(float, value)


class Image(Structure):
    _fields_ = [
        ('data', c_void_p),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]

    def __str__(self) -> str:
        return "(IMAGE: {}w, {}h, mipmap: {}, format: {})".format(self.width, self.height, self.mipmaps, self.format)


ImagePtr = POINTER(Image)


class Texture2D(Structure):
    _fields_ = [
        ('id', c_uint),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]

    def __str__(self) -> str:
        return "(TEXTURE2D: {}w, {}h, mipmap: {}, format: {})".format(self.width, self.height, self.mipmaps, self.format)


Texture2DPtr = POINTER(Texture2D)


class Texture(Structure):
    _fields_ = [
        ('data', c_void_p),
        ('id', c_uint),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]

    def __str__(self) -> str:
        return "(TEXTURE: {}w, {}h, id: {}, mipmap: {}, format: {})".format(self.width, self.height, self.id, self.mipmaps, self.format)


class RenderTexture2D(Structure):
    _fields_ = [
        ('id', c_uint),
        ('texture', Texture2D),
        ('depth', Texture2D),
    ]

    def __str__(self) -> str:
        return "(RENDERTEXTURE2D: {}w, {}h, texture: {}, depth: {})".format(self.width, self.height, self.texture, self.depth)


class RenderTexture(Structure):
    _fields_ = [
        ('id', c_uint),
        ('texture', Texture2D),
        ('depth', Texture2D),
    ]

    def __str__(self) -> str:
        return "(RENDERTEXTURE: {}w, {}h, texture: {}, depth: {})".format(self.width, self.height, self.texture, self.depth)


if ENABLE_V2_0_0_FEATURE_DRAWTEXTURENPATCH:
    class _NPatchInfo(Structure):
        _fields_ = [
            ('sourceRec', Rectangle),
            ('left', c_int),
            ('top', c_int),
            ('right', c_int),
            ('bottom', c_int),
            ('type', c_int),
        ]

    class NPatchInfo(_NPatchInfo):

        def __init__(self, source_rec: 'Rectangle', left: int=1, top:int=1, right: int=1, bottom: int=1, npatch_type: Union[int, 'NPatchType']=0) -> None:
            if npatch_type not in NPatchType:
                npatch_type = {
                    0: NPT_9PATCH,
                    1: NPT_3PATCH_VERTICAL,
                    2: NPT_3PATCH_VERTICAL
                }.get(npatch_type, NPT_9PATCH)

            super(NPatchInfo, self).__init__(source_rec, left, top, right, bottom, npatch_type)

        def __str__(self) -> str:
            """Textual representation."""
            npt = {
                0: NPT_9PATCH,
                1: NPT_3PATCH_VERTICAL,
                2: NPT_3PATCH_VERTICAL
            }.get(self.type, NPT_9PATCH).name
            return "(NPATCHINFO: rec: {0.sourceRec}, ltrb: [{0.left}, {0.top}, {0.right}, {0.bottom}], type: {1})".format(self, npt)

        def __repr__(self) -> str:
            rc = repr(self.sourceRec)
            npt = {
                0: NPT_9PATCH,
                1: NPT_3PATCH_VERTICAL,
                2: NPT_3PATCH_VERTICAL
            }.get(self.type, NPT_9PATCH).name
            return "{0.__class__.__qualname__}({1}, {0.left}, {0.top}, {0.right}, {0.bottom}, {2})".format(self, rc, npt)
else:
    class NPatchInfo:
        __slots__ = 'source_rec', 'left', 'top', 'right', 'bottom', 'type'
        pass

class CharInfo(Structure):
    _fields_ = [
        ('value', c_int),
        ('rec', Rectangle),
        ('offsetX', c_int),
        ('offsetY', c_int),
        ('advanceX', c_int),
        ('data', c_char_p),
    ]

    def __str__(self) -> str:
        return "(CHARINFO: {}, rec: {}, offset: ({}, {}), advanceX: {})".format(self.value, self.rec, self.offsetY, self.offsetY, self.advanceX)


CharInfoPtr = POINTER(CharInfo)


class Font(Structure):
    _fields_ = [
        ('texture', Texture2D),
        ('baseSize', c_int),
        ('charsCount', c_int),
        ('chars', POINTER(CharInfo)),
    ]

    def __str__(self) -> str:
        return "(FONT: texture: {}, baseSize: {}, charsCount: {})".format(self.width, self.height, self.mipmaps, self.format)


SpriteFont = Font


class Camera3D(Structure):
    _fields_ = [
        ('position', Vector3),
        ('target', Vector3),
        ('up', Vector3),
        ('fovy', c_float),
        ('type', c_int),
    ]

    def __str__(self) -> str:
        ct = "PERSPECTIVE" if self.type == 0 else "ORTHOGRAPHIC"
        return "(CAMERA3D: position: {}, target: {}, up: {}, fovy: {}°, type: {})".format(
            self.position, self.target, self.up, self.fovy, ct
        )


Camera3DPtr = POINTER(Camera3D)
Camera = Camera3D
CameraPtr = Camera3DPtr


class Camera2D(Structure):
    _fields_ = [
        ('offset', Vector2),
        ('target', Vector2),
        ('rotation', c_float),
        ('zoom', c_float),
    ]

    def __str__(self) -> str:
        return "(CAMERA2D: offset: {}, target: {}, rotation: {}, zoom: {})".format(
            self.offset, self.target, self.rotation, self.zoom
        )


class BoundingBox(Structure):
    _fields_ = [
        ('min', Vector3),
        ('max', Vector3),
    ]

    def __str__(self) -> str:
        return "(BOUNDINGBOX: min: {}, max: {})".format(
            self.min, self.max
        )


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

    def __str__(self) -> str:
        return "(MESH: vertexCount: {}, triangleCount: {})".format(
            self.vertexCount, self.triangleCount
        )


MeshPtr = POINTER(Mesh)


class Shader(Structure):
    _fields_ = [
        ('id', c_uint),
        ('locs', c_int * MAX_SHADER_LOCATIONS),
    ]

    def __str__(self) -> str:
        return "(SHADER: id: {})".format(
            self.id
        )


class MaterialMap(Structure):
    _fields_ = [
        ('texture', Texture2D),
        ('color', Color),
        ('value', c_float),
    ]

    def __str__(self) -> str:
        return "(MATERIALMAP: texture: {}, color: {}, value: {})".format(
            self.texture, self.color, self.value
        )


class Material(Structure):
    _fields_ = [
        ('shader', Shader),
        ('maps', MaterialMap * MAX_MATERIAL_MAPS),
        ('params', POINTER(c_float)),
    ]

    def __str__(self) -> str:
        return "(MATERIAL: shader: {})".format(
            self.shader
        )


class Model(Structure):
    _fields_ = [
        ('mesh', Mesh),
        ('transform', Matrix),
        ('material', Material),
    ]

    def __str__(self) -> str:
        return "(MODEL: mesh: {}, transform: {}, material: {})".format(
            self.mesh, self.transform, self.material
        )


ModelPtr = POINTER(Model)


class Ray(Structure):
    _fields_ = [
        ('position', Vector3),
        ('direction', Vector3),
    ]

    def __str__(self) -> str:
        return "(RAY: position: {}, direction: {})".format(
            self.position, self.direction
        )


class RayHitInfo(Structure):
    _fields_ = [
        ('hit', c_bool),
        ('distance', c_float),
        ('position', Vector3),
        ('normal', Vector3),
    ]

    def __str__(self) -> str:
        return "(RAYHITINFO: hit: {}, distance: {}, position: {}, normal: {})".format(
            self.hit, self.distance, self.position, self.normal
        )


RayHitInfoPtr = POINTER(RayHitInfo)


class Wave(Structure):
    _fields_ = [
        ('sampleCount', c_uint),
        ('sampleRate', c_uint),
        ('SampleSize', c_uint),
        ('channels', c_uint),
        ('data', c_void_p),
    ]

    def __str__(self) -> str:
        return "(WAVE: sampleCount: {}, sampleRate: {}, sampleSize: {}, channels: {})".format(
            self.sampleCount, self.sampleRate, self.sampleSize, self.channels
        )


WavePtr = POINTER(Wave)


class Sound(Structure):
    _fields_ = [
        ('audioBuffer', c_void_p),
        ('source', c_uint),
        ('buffer', c_uint),
        ('format', c_int),
    ]

    def __str__(self) -> str:
        return "(SOUND: audioBuffer: {}, source: {}, buffer: {}, format: {})".format(
            self.audioBuffer, self.source, self.buffer, self.format
        )


class Music(Structure):
    
    def __str__(self) -> str:
        return "(MUSIC: <no info>)"



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


# Some Basic Colors
# NOTE: Custom raylib color palette for amazing visuals on WHITE background
LIGHTGRAY = Color(200, 200, 200, 255)   # Light Gray
GRAY = Color(130, 130, 130, 255)        # Gray
DARKGRAY = Color(80, 80, 80, 255)       # Dark Gray
YELLOW = Color(253, 249, 0, 255)        # Yellow
GOLD = Color(255, 203, 0, 255)          # Gold
ORANGE = Color(255, 161, 0, 255)        # Orange
PINK = Color(255, 109, 194, 255)        # Pink
RED = Color(230, 41, 55, 255)           # Red
MAROON = Color(190, 33, 55, 255)        # Maroon
GREEN = Color(0, 228, 48, 255)          # Green
LIME = Color(0, 158, 47, 255)           # Lime
DARKGREEN = Color(0, 117, 44, 255)      # Dark Green
SKYBLUE = Color(102, 191, 255, 255)     # Sky Blue
BLUE = Color(0, 121, 241, 255)          # Blue
DARKBLUE = Color(0, 82, 172, 255)       # Dark Blue
PURPLE = Color(200, 122, 255, 255)      # Purple
VIOLET = Color(135, 60, 190, 255)       # Violet
DARKPURPLE = Color(112, 31, 126, 255)   # Dark Purple
BEIGE = Color(211, 176, 131, 255)       # Beige
BROWN = Color(127, 106, 79, 255)        # Brown
DARKBROWN = Color(76, 63, 47, 255)      # Dark Brown
WHITE = Color(255, 255, 255, 255)       # White
BLACK = Color(0, 0, 0, 255)             # Black
BLANK = Color(0, 0, 0, 0)               # Blank (Transparent)
MAGENTA = Color(255, 0, 255, 255)       # Magenta
RAYWHITE = Color(245, 245, 245, 255)    # My own White (raylib logo)

# ---------------------------------------------------------------------------------
# Enumerators Definition
# ---------------------------------------------------------------------------------
# Trace log type
class LogType(IntEnum):
    LOG_INFO = 1
    LOG_WARNING = 2
    LOG_ERROR = 4
    LOG_DEBUG = 8
    LOG_OTHER = 16


LOG_INFO = LogType.LOG_INFO
LOG_WARNING = LogType.LOG_WARNING
LOG_ERROR = LogType.LOG_ERROR
LOG_DEBUG = LogType.LOG_DEBUG
LOG_OTHER = LogType.LOG_OTHER


# Shader location point type
class ShaderLocationIndex(IntEnum):
    LOC_VERTEX_POSITION = 1
    LOC_VERTEX_TEXCOORD01 = 2
    LOC_VERTEX_TEXCOORD02 = 3
    LOC_VERTEX_NORMAL = 4
    LOC_VERTEX_TANGENT = 5
    LOC_VERTEX_COLOR = 6
    LOC_MATRIX_MVP = 7
    LOC_MATRIX_MODEL = 8
    LOC_MATRIX_VIEW = 9
    LOC_MATRIX_PROJECTION = 10
    LOC_VECTOR_VIEW = 11
    LOC_COLOR_DIFFUSE = 12
    LOC_COLOR_SPECULAR = 13
    LOC_COLOR_AMBIENT = 14
    LOC_MAP_ALBEDO = 15
    LOC_MAP_METALNESS = 16
    LOC_MAP_NORMAL = 17
    LOC_MAP_ROUGHNESS = 18
    LOC_MAP_OCCLUSION = 19
    LOC_MAP_EMISSION = 20
    LOC_MAP_HEIGHT = 21
    LOC_MAP_CUBEMAP = 22
    LOC_MAP_IRRADIANCE = 23
    LOC_MAP_PREFILTER = 24
    LOC_MAP_BRDF = 25


LOC_VERTEX_POSITION = ShaderLocationIndex.LOC_VERTEX_POSITION
LOC_VERTEX_TEXCOORD01 = ShaderLocationIndex.LOC_VERTEX_TEXCOORD01
LOC_VERTEX_TEXCOORD02 = ShaderLocationIndex.LOC_VERTEX_TEXCOORD02
LOC_VERTEX_NORMAL = ShaderLocationIndex.LOC_VERTEX_NORMAL
LOC_VERTEX_TANGENT = ShaderLocationIndex.LOC_VERTEX_TANGENT
LOC_VERTEX_COLOR = ShaderLocationIndex.LOC_VERTEX_COLOR
LOC_MATRIX_MVP = ShaderLocationIndex.LOC_MATRIX_MVP
LOC_MATRIX_MODEL = ShaderLocationIndex.LOC_MATRIX_MODEL
LOC_MATRIX_VIEW = ShaderLocationIndex.LOC_MATRIX_VIEW
LOC_MATRIX_PROJECTION = ShaderLocationIndex.LOC_MATRIX_PROJECTION
LOC_VECTOR_VIEW = ShaderLocationIndex.LOC_VECTOR_VIEW
LOC_COLOR_DIFFUSE = ShaderLocationIndex.LOC_COLOR_DIFFUSE
LOC_COLOR_SPECULAR = ShaderLocationIndex.LOC_COLOR_SPECULAR
LOC_COLOR_AMBIENT = ShaderLocationIndex.LOC_COLOR_AMBIENT
LOC_MAP_ALBEDO = ShaderLocationIndex.LOC_MAP_ALBEDO
LOC_MAP_METALNESS = ShaderLocationIndex.LOC_MAP_METALNESS
LOC_MAP_NORMAL = ShaderLocationIndex.LOC_MAP_NORMAL
LOC_MAP_ROUGHNESS = ShaderLocationIndex.LOC_MAP_ROUGHNESS
LOC_MAP_OCCLUSION = ShaderLocationIndex.LOC_MAP_OCCLUSION
LOC_MAP_EMISSION = ShaderLocationIndex.LOC_MAP_EMISSION
LOC_MAP_HEIGHT = ShaderLocationIndex.LOC_MAP_HEIGHT
LOC_MAP_CUBEMAP = ShaderLocationIndex.LOC_MAP_CUBEMAP
LOC_MAP_IRRADIANCE = ShaderLocationIndex.LOC_MAP_IRRADIANCE
LOC_MAP_PREFILTER = ShaderLocationIndex.LOC_MAP_PREFILTER
LOC_MAP_BRDF = ShaderLocationIndex.LOC_MAP_BRDF
LOC_MAP_DIFFUSE = ShaderLocationIndex.LOC_MAP_ALBEDO
LOC_MAP_SPECULAR = ShaderLocationIndex.LOC_MAP_METALNESS


# Material map type
class TexmapIndex(IntEnum):
    MAP_ALBEDO = 0
    MAP_METALNESS = 1
    MAP_NORMAL = 2
    MAP_ROUGHNESS = 3
    MAP_OCCLUSION = 4
    MAP_EMISSION = 5
    MAP_HEIGHT = 6
    MAP_CUBEMAP = 7
    MAP_IRRADIANCE = 8
    MAP_PREFILTER = 9
    MAP_BRDF = 10


MAP_ALBEDO = TexmapIndex.MAP_ALBEDO
MAP_METALNESS = TexmapIndex.MAP_METALNESS
MAP_NORMAL = TexmapIndex.MAP_NORMAL
MAP_ROUGHNESS = TexmapIndex.MAP_ROUGHNESS
MAP_OCCLUSION = TexmapIndex.MAP_OCCLUSION
MAP_EMISSION = TexmapIndex.MAP_EMISSION
MAP_HEIGHT = TexmapIndex.MAP_HEIGHT
MAP_CUBEMAP = TexmapIndex.MAP_CUBEMAP
MAP_IRRADIANCE = TexmapIndex.MAP_IRRADIANCE
MAP_PREFILTER = TexmapIndex.MAP_PREFILTER
MAP_BRDF = TexmapIndex.MAP_BRDF
MAP_DIFFUSE = TexmapIndex.MAP_ALBEDO
MAP_SPECULAR = TexmapIndex.MAP_METALNESS


class PixelFormat(IntEnum):
    UNCOMPRESSED_GRAYSCALE = 1
    UNCOMPRESSED_GRAY_ALPHA = 2
    UNCOMPRESSED_R5G6B5 = 3
    UNCOMPRESSED_R8G8B8 = 4
    UNCOMPRESSED_R5G5B5A1 = 5
    UNCOMPRESSED_R4G4B4A4 = 6
    UNCOMPRESSED_R8G8B8A8 = 7
    UNCOMPRESSED_R32 = 8
    UNCOMPRESSED_R32G32B32 = 9
    UNCOMPRESSED_R32G32B32A32 = 10
    COMPRESSED_DXT1_RGB = 11
    COMPRESSED_DXT1_RGBA = 12
    COMPRESSED_DXT3_RGBA = 13
    COMPRESSED_DXT5_RGBA = 14
    COMPRESSED_ETC1_RGB = 15
    COMPRESSED_ETC2_RGB = 16
    COMPRESSED_ETC2_EAC_RGBA = 17
    COMPRESSED_PVRT_RGB = 18
    COMPRESSED_PVRT_RGBA = 19
    COMPRESSED_ASTC_4x4_RGBA = 20
    COMPRESSED_ASTC_8x8_RGBA = 21


UNCOMPRESSED_GRAYSCALE = PixelFormat.UNCOMPRESSED_GRAYSCALE
UNCOMPRESSED_GRAY_ALPHA = PixelFormat.UNCOMPRESSED_GRAY_ALPHA
UNCOMPRESSED_R5G6B5 = PixelFormat.UNCOMPRESSED_R5G6B5
UNCOMPRESSED_R8G8B8 = PixelFormat.UNCOMPRESSED_R8G8B8
UNCOMPRESSED_R5G5B5A1 = PixelFormat.UNCOMPRESSED_R5G5B5A1
UNCOMPRESSED_R4G4B4A4 = PixelFormat.UNCOMPRESSED_R4G4B4A4
UNCOMPRESSED_R8G8B8A8 = PixelFormat.UNCOMPRESSED_R8G8B8A8
UNCOMPRESSED_R32 = PixelFormat.UNCOMPRESSED_R32
UNCOMPRESSED_R32G32B32 = PixelFormat.UNCOMPRESSED_R32G32B32
UNCOMPRESSED_R32G32B32A32 = PixelFormat.UNCOMPRESSED_R32G32B32A32
COMPRESSED_DXT1_RGB = PixelFormat.COMPRESSED_DXT1_RGB
COMPRESSED_DXT1_RGBA = PixelFormat.COMPRESSED_DXT1_RGBA
COMPRESSED_DXT3_RGBA = PixelFormat.COMPRESSED_DXT3_RGBA
COMPRESSED_DXT5_RGBA = PixelFormat.COMPRESSED_DXT5_RGBA
COMPRESSED_ETC1_RGB = PixelFormat.COMPRESSED_ETC1_RGB
COMPRESSED_ETC2_RGB = PixelFormat.COMPRESSED_ETC2_RGB
COMPRESSED_ETC2_EAC_RGBA = PixelFormat.COMPRESSED_ETC2_EAC_RGBA
COMPRESSED_PVRT_RGB = PixelFormat.COMPRESSED_PVRT_RGB
COMPRESSED_PVRT_RGBA = PixelFormat.COMPRESSED_PVRT_RGBA
COMPRESSED_ASTC_4x4_RGBA = PixelFormat.COMPRESSED_ASTC_4x4_RGBA
COMPRESSED_ASTC_8x8_RGBA = PixelFormat.COMPRESSED_ASTC_8x8_RGBA


class TextureFilterMode(IntEnum):
    FILTER_POINT = 0
    FILTER_BILINEAR = 1
    FILTER_TRILINEAR = 2
    FILTER_ANISOTROPIC_4X = 3
    FILTER_ANISOTROPIC_8X = 4
    FILTER_ANISOTROPIC_16X = 5


FILTER_POINT = TextureFilterMode.FILTER_POINT
FILTER_BILINEAR = TextureFilterMode.FILTER_BILINEAR
FILTER_TRILINEAR = TextureFilterMode.FILTER_TRILINEAR
FILTER_ANISOTROPIC_4X = TextureFilterMode.FILTER_ANISOTROPIC_4X
FILTER_ANISOTROPIC_8X = TextureFilterMode.FILTER_ANISOTROPIC_8X
FILTER_ANISOTROPIC_16X = TextureFilterMode.FILTER_ANISOTROPIC_16X


class TextureWrapMode(IntEnum):
    WRAP_REPEAT = 0
    WRAP_CLAMP = 1
    WRAP_MIRROR = 2


WRAP_REPEAT = TextureWrapMode.WRAP_REPEAT
WRAP_CLAMP = TextureWrapMode.WRAP_CLAMP
WRAP_MIRROR = TextureWrapMode.WRAP_MIRROR


class BlendMode(IntEnum):
    BLEND_ALPHA = 0
    BLEND_ADDITIVE = 1
    BLEND_MULTIPLIED = 2


BLEND_ALPHA = BlendMode.BLEND_ALPHA
BLEND_ADDITIVE = BlendMode.BLEND_ADDITIVE
BLEND_MULTIPLIED = BlendMode.BLEND_MULTIPLIED

class Gestures(IntFlag):
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


GESTURE_NONE = Gestures.GESTURE_NONE
GESTURE_TAP = Gestures.GESTURE_TAP
GESTURE_DOUBLETAP = Gestures.GESTURE_DOUBLETAP
GESTURE_HOLD = Gestures.GESTURE_HOLD
GESTURE_DRAG = Gestures.GESTURE_DRAG
GESTURE_SWIPE_RIGHT = Gestures.GESTURE_SWIPE_RIGHT
GESTURE_SWIPE_LEFT = Gestures.GESTURE_SWIPE_LEFT
GESTURE_SWIPE_UP = Gestures.GESTURE_SWIPE_UP
GESTURE_SWIPE_DOWN = Gestures.GESTURE_SWIPE_DOWN
GESTURE_PINCH_IN = Gestures.GESTURE_PINCH_IN
GESTURE_PINCH_OUT = Gestures.GESTURE_PINCH_OUT


class CameraMode(IntEnum):
    CAMERA_CUSTOM = 0
    CAMERA_FREE = 1
    CAMERA_ORBITAL = 2
    CAMERA_FIRST_PERSON = 3
    CAMERA_THIRD_PERSON = 4

CAMERA_CUSTOM = CameraMode.CAMERA_CUSTOM
CAMERA_FREE = CameraMode.CAMERA_FREE
CAMERA_ORBITAL = CameraMode.CAMERA_ORBITAL
CAMERA_FIRST_PERSON = CameraMode.CAMERA_FIRST_PERSON
CAMERA_THIRD_PERSON = CameraMode.CAMERA_THIRD_PERSON


class CameraType(IntEnum):
    CAMERA_PERSPECTIVE = 0
    CAMERA_ORTHOGRAPHIC = 1


CAMERA_PERSPECTIVE = CameraType.CAMERA_PERSPECTIVE
CAMERA_ORTHOGRAPHIC = CameraType.CAMERA_ORTHOGRAPHIC


class VrDeviceType(IntEnum):
    HMD_DEFAULT_DEVICE = 0
    HMD_OCULUS_RIFT_DK2 = 1
    HMD_OCULUS_RIFT_CV1 = 2
    HMD_OCULUS_GO = 3
    HMD_VALVE_HTC_VIVE = 4
    HMD_SONY_PSVR = 5

HMD_DEFAULT_DEVICE = VrDeviceType.HMD_DEFAULT_DEVICE
HMD_OCULUS_RIFT_DK2 = VrDeviceType.HMD_OCULUS_RIFT_DK2
HMD_OCULUS_RIFT_CV1 = VrDeviceType.HMD_OCULUS_RIFT_CV1
HMD_OCULUS_GO = VrDeviceType.HMD_OCULUS_GO
HMD_VALVE_HTC_VIVE = VrDeviceType.HMD_VALVE_HTC_VIVE
HMD_SONY_PSVR = VrDeviceType.HMD_SONY_PSVR


class NPatchType(IntEnum):
    NPT_9PATCH = 0
    NPT_3PATCH_VERTICAL = 1
    NPT_3PATCH_HORIZONTAL = 2


NPT_9PATCH = NPatchType.NPT_9PATCH
NPT_3PATCH_VERTICAL = NPatchType.NPT_3PATCH_VERTICAL
NPT_3PATCH_HORIZONTAL = NPatchType.NPT_3PATCH_HORIZONTAL

# -----------------------------------------------------------------------------------
# Window and Graphics Device Functions (Module: core)
# ----------------------------------------------------------------------------------

# Window-related functions
_rl.InitWindow.argtypes = [Int, Int, CharPtr]
_rl.InitWindow.restype = None
def init_window(width: int, height: int, title: AnyStr) -> None:
    """Initialize window and OpenGL context"""
    return _rl.InitWindow(_int(width), _int(height), _str_in(title))


def init_window_v(size: Union[Vector2, Seq], title: AnyStr) -> None:
    """Initialize window (with a sequence type as size) and OpenGL context"""
    size = _vec2(size)
    init_window(size.x, size.y, title)


_rl.CloseWindow.argtypes = _NOARGS
_rl.CloseWindow.restype = None
def close_window() -> None:
    """Close window and unload OpenGL context"""
    return _rl.CloseWindow()


_rl.IsWindowReady.argtypes = _NOARGS
_rl.IsWindowReady.restype = Bool
def is_window_ready() -> None:
    """Check if window has been initialized successfully"""
    return _rl.IsWindowReady()


_rl.WindowShouldClose.argtypes = _NOARGS
_rl.WindowShouldClose.restype = Bool
def window_should_close() -> bool:
    """Check if KEY_ESCAPE pressed or Close icon pressed"""
    return _rl.WindowShouldClose()


_rl.IsWindowMinimized.argtypes = _NOARGS
_rl.IsWindowMinimized.restype = Bool
def is_window_minimized() -> bool:
    """Check if window has been minimized (or lost focus)"""
    return _rl.IsWindowMinimized()


_rl.ToggleFullscreen.argtypes = []
_rl.ToggleFullscreen.restype = None
def toggle_fullscreen() -> None:
    """Toggle fullscreen mode (only PLATFORM_DESKTOP)"""
    return _rl.ToggleFullscreen()


_rl.SetWindowIcon.argtypes = [Image]
_rl.SetWindowIcon.restype = None
def set_window_icon(image: Image) -> None:
    """Set icon for window (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowIcon(image)


_rl.SetWindowTitle.argtypes = [CharPtr]
_rl.SetWindowTitle.restype = None
def set_window_title(title: AnyStr) -> None:
    """Set title for window (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowTitle(_str_in(title))


_rl.SetWindowPosition.argtypes = [Int, Int]
_rl.SetWindowPosition.restype = None
def set_window_position(x: int, y: int) -> None:
    """Set window position on screen (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowPosition(_int(x), _int(y))

def set_window_position_v(pos: Union[Vector2, Seq]) -> None:
    """Set window position on screen (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowPosition(_vec2(pos))


_rl.SetWindowMonitor.argtypes = [Int]
_rl.SetWindowMonitor.restype = None
def set_window_monitor(monitor: int) -> None:
    """Set monitor for the current window (fullscreen mode)"""
    return _rl.SetWindowMonitor(_int(monitor))


_rl.SetWindowMinSize.argtypes = [Int, Int]
_rl.SetWindowMinSize.restype = None
def set_window_min_size(width: int, height: int) -> None:
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
    return _rl.SetWindowMinSize(_int(width), _int(height))


_rl.SetWindowSize.argtypes = [Int, Int]
_rl.SetWindowSize.restype = None
def set_window_size(width: int, height: int) -> None:
    """Set window dimensions"""
    return _rl.SetWindowSize(_int(width), _int(height))


_rl.GetScreenWidth.argtypes = _NOARGS
_rl.GetScreenWidth.restype = Int
def get_screen_width() -> int:
    """Get current screen width"""
    return _rl.GetScreenWidth()


_rl.GetScreenHeight.argtypes = _NOARGS
_rl.GetScreenHeight.restype = Int
def get_screen_height() -> int:
    """Get current screen height"""
    return _rl.GetScreenHeight()


# Cursor-related functions
_rl.ShowCursor.argtypes = _NOARGS
_rl.ShowCursor.restype = None
def show_cursor() -> None:
    """Shows cursor"""
    return _rl.ShowCursor()


_rl.HideCursor.argtypes = _NOARGS
_rl.HideCursor.restype = None
def hide_cursor() -> None:
    """Hides cursor"""
    return _rl.HideCursor()


_rl.IsCursorHidden.argtypes = _NOARGS
_rl.IsCursorHidden.restype = Bool
def is_cursor_hidden() -> bool:
    """Check if cursor is not visible"""
    return _rl.IsCursorHidden()


_rl.EnableCursor.argtypes = _NOARGS
_rl.EnableCursor.restype = None
def enable_cursor() -> None:
    """Enables cursor (unlock cursor)"""
    return _rl.EnableCursor()


_rl.DisableCursor.argtypes = _NOARGS
_rl.DisableCursor.restype = None
def disable_cursor() -> None:
    """Disables cursor (lock cursor)"""
    return _rl.DisableCursor()


# Drawing-related functions
_rl.ClearBackground.argtypes = [Color]
_rl.ClearBackground.restype = None
def clear_background(color: Union[Color, Seq]) -> None:
    """Set background color (framebuffer clear color)"""
    return _rl.ClearBackground(_color(color))


_rl.BeginDrawing.argtypes = _NOARGS
_rl.BeginDrawing.restype = None
def begin_drawing() -> None:
    """Setup canvas (framebuffer) to start drawing"""
    return _rl.BeginDrawing()


_rl.EndDrawing.argtypes = _NOARGS
_rl.EndDrawing.restype = None
def end_drawing() -> None:
    """End canvas drawing and swap buffers (double buffering)"""
    return _rl.EndDrawing()


_rl.BeginMode2D.argtypes = [Camera2D]
_rl.BeginMode2D.restype = None
def begin_mode2d(camera: Camera2D) -> None:
    """Initialize 2D mode with custom camera (2D)"""
    return _rl.BeginMode2D(camera)


_rl.EndMode2D.argtypes = _NOARGS
_rl.EndMode2D.restype = None
def end_mode2d() -> None:
    """Ends 2D mode with custom camera"""
    return _rl.EndMode2D()


_rl.BeginMode3D.argtypes = [Camera3D]
_rl.BeginMode3D.restype = None
def begin_mode3d(camera: Camera3D) -> None:
    """Initializes 3D mode with custom camera (3D)"""
    return _rl.BeginMode3D(camera)


_rl.EndMode3D.argtypes = _NOARGS
_rl.EndMode3D.restype = None
def end_mode3d() -> None:
    """Ends 3D mode and returns to default 2D orthographic mode"""
    return _rl.EndMode3D()


_rl.BeginTextureMode.argtypes = [RenderTexture2D]
_rl.BeginTextureMode.restype = None
def begin_texture_mode(target: RenderTexture2D) -> None:
    """Initializes render texture for drawing"""
    return _rl.BeginTextureMode(target)


_rl.EndTextureMode.argtypes = _NOARGS
_rl.EndTextureMode.restype = None
def end_texture_mode() -> None:
    """Ends drawing to render texture"""
    return _rl.EndTextureMode()


# Screen-space-related functions
_rl.GetMouseRay.argtypes = [Vector2, Camera]
_rl.GetMouseRay.restype = Ray
def get_mouse_ray(mouse_position: Union[Vector2, Seq], camera: Camera) -> Ray:
    """Returns a ray trace from mouse position"""
    return _rl.GetMouseRay(_vec2(mouse_position), camera)


_rl.GetWorldToScreen.argtypes = [Vector3, Camera]
_rl.GetWorldToScreen.restype = Vector2
def get_world_to_screen(position: Union[Vector3, Seq], camera: Camera) -> Vector2:
    """Returns the screen space position for a 3d world space position"""
    return _rl.GetWorldToScreen(_vec3(position), camera)


_rl.GetCameraMatrix.argtypes = [Camera]
_rl.GetCameraMatrix.restype = Matrix
def get_camera_matrix(camera: Camera) -> Matrix:
    """Returns camera transform matrix (view matrix)"""
    return _rl.GetCameraMatrix(camera)


# Timming-related functions
_rl.SetTargetFPS.argtypes = [Int]
_rl.SetTargetFPS.restype = None
def set_target_fps(fps: int) -> None:
    """Set target FPS (maximum)"""
    return _rl.SetTargetFPS(fps)


_rl.GetFPS.argtypes = _NOARGS
_rl.GetFPS.restype = Int
def get_fps() -> int:
    """Returns current FPS"""
    return _rl.GetFPS()


_rl.GetFrameTime.argtypes = _NOARGS
_rl.GetFrameTime.restype = Float
def get_frame_time() -> float:
    """Returns time in seconds for last frame drawn"""
    return _rl.GetFrameTime()


_rl.GetTime.argtypes = _NOARGS
_rl.GetTime.restype = Double
def get_time() -> float:
    """Returns elapsed time in seconds since InitWindow()"""
    return _rl.GetTime()


# Color-related functions
_rl.ColorToInt.argtypes = [Color]
_rl.ColorToInt.restype = Int
def color_to_int(color: Union[Color, Seq]) -> int:
    """Returns hexadecimal value for a Color"""
    return _rl.ColorToInt(_color(color))


_rl.ColorNormalize.argtypes = [Color]
_rl.ColorNormalize.restype = Vector4
def color_normalize(color: Union[Color, Seq]) -> Vector4:
    """Returns color normalized as float [0..1]"""
    return _rl.ColorNormalize(_color(color))


_rl.ColorToHSV.argtypes = [Color]
_rl.ColorToHSV.restype = Vector3
def color_to_hsv(color: Union[Color, Seq]) -> Vector3:
    """Returns HSV values for a Color"""
    return _rl.ColorToHSV(_color(color))


_rl.GetColor.argtypes = [Int]
_rl.GetColor.restype = Color
def get_color(hex_value: int) -> Color:
    """Returns a Color struct from hexadecimal value"""
    return _rl.GetColor(hex_value)


_rl.Fade.argtypes = [Color, Float]
_rl.Fade.restype = Color
def fade(color: Union[Color, Seq], alpha: float) -> Color:
    """Color fade-in or fade-out, alpha goes from 0.0f to 1.0f"""
    return _rl.Fade(_color(color), alpha)


# Misc. functions
_rl.ShowLogo.argtypes = _NOARGS
_rl.ShowLogo.restype = None
def show_logo() -> None:
    """Activate raylib logo at startup (can be done with flags)"""
    return _rl.ShowLogo()


_rl.SetConfigFlags.argtypes = [UChar]
_rl.SetConfigFlags.restype = None
def set_config_flags(flags: int) -> None:
    """Setup window configuration flags (view FLAGS)"""
    return _rl.SetConfigFlags(flags)


_rl.SetTraceLog.argtypes = [UChar]
_rl.SetTraceLog.restype = None
def set_trace_log(types: int) -> None:
    """Enable trace log message types (bit flags based)"""
    return _rl.SetTraceLog(types)


_rl.TraceLog.argtypes = [Int, CharPtr]
_rl.TraceLog.restype = None
def trace_log(log_type: int, text: AnyStr, *args) -> None:
    """Show trace log messages (LOG_INFO, LOG_WARNING, LOG_ERROR, LOG_DEBUG)"""
    return _rl.TraceLog(log_type, _str_in(text), *args)


_rl.TakeScreenshot.argtypes = [CharPtr]
_rl.TakeScreenshot.restype = None
def take_screenshot(file_name: AnyStr):
    """Takes a screenshot of current screen (saved a .png)"""
    return _rl.TakeScreenshot(_str_in(file_name))


_rl.GetRandomValue.argtypes = [Int, Int]
_rl.GetRandomValue.restype = Int
def get_random_value(min_val: int, max_val: int) -> int:
    """Returns a random value between min and max (both included)"""
    return _rl.GetRandomValue(min_val, max_val)

# Files management functions
_rl.IsFileExtension.argtypes = [CharPtr, CharPtr]
_rl.IsFileExtension.restype = Bool
def is_file_extension(file_name: AnyStr, ext: bytes) -> bool:
    """Check file extension"""
    return _rl.IsFileExtension(_str_in(file_name), ext)


_rl.GetExtension.argtypes = [CharPtr]
_rl.GetExtension.restype = CharPtr
def get_extension(file_name: AnyStr) -> bytes:
    """Get pointer to extension for a filename string"""
    return _rl.GetExtension(_str_in(file_name))


_rl.GetFileName.argtypes = [CharPtr]
_rl.GetFileName.restype = CharPtr
def get_file_name(file_path: AnyStr) -> bytes:
    """Get pointer to filename for a path string"""
    return _rl.GetFileName(_str_in(file_path))


_rl.GetDirectoryPath.argtypes = [CharPtr]
_rl.GetDirectoryPath.restype = CharPtr
def get_directory_path(file_name: AnyStr) -> bytes:
    """Get full path for a given file_name (uses static string)"""
    return _rl.GetDirectoryPath(_str_in(file_name))


_rl.GetWorkingDirectory.argtypes = _NOARGS
_rl.GetWorkingDirectory.restype = CharPtr
def get_working_directory() -> str:
    """Get current working directory (uses static string)"""
    return _str_out(_rl.GetWorkingDirectory())


_rl.ChangeDirectory.argtypes = [CharPtr]
_rl.ChangeDirectory.restype = Bool
def change_directory(directory: AnyStr) -> bool:
    """Change working directory, returns true if success"""
    return _rl.ChangeDirectory(_str_in(directory))


_rl.IsFileDropped.argtypes = _NOARGS
_rl.IsFileDropped.restype = Bool
def is_file_dropped() -> bool:
    """Check if a file has been dropped into window"""
    return _rl.IsFileDropped()


_rl.GetDroppedFiles.argtypes = [IntPtr]
_rl.GetDroppedFiles.restype = CharPtrPrt
def get_dropped_files() -> Tuple[str, ...]:
    """Get dropped files names"""
    count = Int(0)
    result = _rl.GetDroppedFiles(byref(count))
    files: list = []
    for i in range(count.value):
        files.append(result[i].decode('utf-8'))
    return tuple(files)


_rl.ClearDroppedFiles.argtypes = _NOARGS
_rl.ClearDroppedFiles.restype = None
def clear_dropped_files() -> None:
    """Clear dropped files paths buffer"""
    return _rl.ClearDroppedFiles()


# Persistent storage management
_rl.StorageSaveValue.argtypes = [Int, Int]
_rl.StorageSaveValue.restype = None
def storage_save_value(position: int, value: int) -> None:
    """Save integer value to storage file (to defined position)"""
    return _rl.StorageSaveValue(_int(position), _int(value))


_rl.StorageLoadValue.argtypes = [Int]
_rl.StorageLoadValue.restype = Int
def storage_load_value(position: int) -> int:
    """Load integer value from storage file (from defined position)"""
    return _rl.StorageLoadValue(_int(position))


#------------------------------------------------------------------------------------
# Input Handling Functions (Module: core)
# -----------------------------------------------------------------------------------

# Input-related functions: keyboard
_rl.IsKeyPressed.argtypes = [Int]
_rl.IsKeyPressed.restype = Bool
def is_key_pressed(key: int) -> bool:
    """Detect if a key has been pressed once"""
    return _rl.IsKeyPressed(_int(key))


_rl.IsKeyDown.argtypes = [Int]
_rl.IsKeyDown.restype = Bool
def is_key_down(key: int) -> bool:
    """Detect if a key is being pressed"""
    return _rl.IsKeyDown(_int(key))


_rl.IsKeyReleased.argtypes = [Int]
_rl.IsKeyReleased.restype = Bool
def is_key_released(key: int) -> bool:
    """Detect if a key has been released once"""
    return _rl.IsKeyReleased(_int(key))


_rl.IsKeyUp.argtypes = [Int]
_rl.IsKeyUp.restype = Bool
def is_key_up(key: int) -> bool:
    """Detect if a key is NOT being pressed"""
    return _rl.IsKeyUp(_int(key))


_rl.GetKeyPressed.argtypes = _NOARGS
_rl.GetKeyPressed.restype = Int
def get_key_pressed() -> int:
    """Get latest key pressed"""
    return _rl.GetKeyPressed()


_rl.SetExitKey.argtypes = [Int]
_rl.SetExitKey.restype = None
def set_exit_key(key: int) -> None:
    """Set a custom key to exit program (default is ESC)"""
    return _rl.SetExitKey(_int(key))


_rl.IsGamepadAvailable.argtypes = [Int]
_rl.IsGamepadAvailable.restype = Bool
def is_gamepad_available(gamepad: int) -> bool:
    """Detect if a gamepad is available"""
    return _rl.IsGamepadAvailable(gamepad)


_rl.IsGamepadName.argtypes = [Int, CharPtr]
_rl.IsGamepadName.restype = Bool
def is_gamepad_name(gamepad: int, name: AnyStr) -> bool:
    """Check gamepad name (if available)"""
    return _rl.IsGamepadName(_int(gamepad), _str_in(name))


_rl.GetGamepadName.argtypes = [Int]
_rl.GetGamepadName.restype = CharPtr
def get_gamepad_name(gamepad: int) -> bytes:
    """Return gamepad internal name id"""
    return _rl.GetGamepadName(_int(gamepad))


_rl.IsGamepadButtonPressed.argtypes = [Int, Int]
_rl.IsGamepadButtonPressed.restype = Bool
def is_gamepad_button_pressed(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button has been pressed once"""
    return _rl.IsGamepadButtonPressed(_int(gamepad), button)


_rl.IsGamepadButtonDown.argtypes = [Int, Int]
_rl.IsGamepadButtonDown.restype = Bool
def is_gamepad_button_down(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button is being pressed"""
    return _rl.IsGamepadButtonDown(_int(gamepad), button)


_rl.IsGamepadButtonReleased.argtypes = [Int, Int]
_rl.IsGamepadButtonReleased.restype = Bool
def is_gamepad_button_released(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button has been released once"""
    return _rl.IsGamepadButtonReleased(_int(gamepad), button)


_rl.IsGamepadButtonUp.argtypes = [Int, Int]
_rl.IsGamepadButtonUp.restype = Bool
def is_gamepad_button_up(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button is NOT being pressed"""
    return _rl.IsGamepadButtonUp(_int(gamepad), button)


_rl.GetGamepadButtonPressed.argtypes = _NOARGS
_rl.GetGamepadButtonPressed.restype = Int
def get_gamepad_button_pressed():
    """Get the last gamepad button pressed"""
    return _rl.GetGamepadButtonPressed()


_rl.GetGamepadAxisCount.argtypes = [Int]
_rl.GetGamepadAxisCount.restype = Int
def get_gamepad_axis_count(gamepad: int) -> int:
    """Return gamepad axis count for a gamepad"""
    return _rl.GetGamepadAxisCount(_int(gamepad))


_rl.GetGamepadAxisMovement.argtypes = [Int, Int]
_rl.GetGamepadAxisMovement.restype = Float
def get_gamepad_axis_movement(gamepad: int, axis: int) -> float:
    """Return axis movement value for a gamepad axis"""
    return _rl.GetGamepadAxisMovement(_int(gamepad), _int(axis))


_rl.IsMouseButtonPressed.argtypes = [Int]
_rl.IsMouseButtonPressed.restype = Bool
def is_mouse_button_pressed(button: int) -> bool:
    """Detect if a mouse button has been pressed once"""
    return _rl.IsMouseButtonPressed(_int(button))


_rl.IsMouseButtonDown.argtypes = [Int]
_rl.IsMouseButtonDown.restype = Bool
def is_mouse_button_down(button: int) -> bool:
    """Detect if a mouse button is being pressed"""
    return _rl.IsMouseButtonDown(_int(button))


_rl.IsMouseButtonReleased.argtypes = [Int]
_rl.IsMouseButtonReleased.restype = Bool
def is_mouse_button_released(button: int) -> bool:
    """Detect if a mouse button has been released once"""
    return _rl.IsMouseButtonReleased(_int(button))


_rl.IsMouseButtonUp.argtypes = [Int]
_rl.IsMouseButtonUp.restype = Bool
def is_mouse_button_up(button: int) -> bool:
    """Detect if a mouse button is NOT being pressed"""
    return _rl.IsMouseButtonUp(_int(button))


_rl.GetMouseX.argtypes = _NOARGS
_rl.GetMouseX.restype = Int
def get_mouse_x() -> int:
    """Returns mouse position X"""
    return _rl.GetMouseX()


_rl.GetMouseY.argtypes = _NOARGS
_rl.GetMouseY.restype = Int
def get_mouse_y() -> int:
    """Returns mouse position Y"""
    return _rl.GetMouseY()


_rl.GetMousePosition.argtypes = _NOARGS
_rl.GetMousePosition.restype = Vector2
def get_mouse_position() -> Vector2:
    """Returns mouse position XY"""
    return _rl.GetMousePosition()


_rl.SetMousePosition.argtypes = [Vector2]
_rl.SetMousePosition.restype = None
def set_mouse_position(position: Union[Vector2, Seq]) -> None:
    """Set mouse position XY"""
    return _rl.SetMousePosition(_vec2(position))


_rl.SetMouseScale.argtypes = [Float]
_rl.SetMouseScale.restype = None
def set_mouse_scale(scale: float) -> None:
    """Set mouse scaling"""
    return _rl.SetMouseScale(_float(scale))


_rl.GetMouseWheelMove.argtypes = _NOARGS
_rl.GetMouseWheelMove.restype = Int
def get_mouse_wheel_move() -> int:
    """Returns mouse wheel movement Y"""
    return _rl.GetMouseWheelMove()


_rl.GetTouchX.argtypes = _NOARGS
_rl.GetTouchX.restype = Int
def get_touch_x() -> int:
    """Returns touch position X for touch point 0 (relative to screen size)"""
    return _rl.GetTouchX()


_rl.GetTouchY.argtypes = _NOARGS
_rl.GetTouchY.restype = Int
def get_touch_y() -> int:
    """Returns touch position Y for touch point 0 (relative to screen size)"""
    return _rl.GetTouchY()


_rl.GetTouchPosition.argtypes = [Int]
_rl.GetTouchPosition.restype = Vector2
def get_touch_position(index: int) -> Vector2:
    """Returns touch position XY for a touch point index (relative to screen size)"""
    return _rl.GetTouchPosition(_int(index))


# -----------------------------------------------------------------------------------
# Gestures and Touch Handling Functions (Module: gestures)
# -----------------------------------------------------------------------------------
_rl.SetGesturesEnabled.argtypes = [UInt]
_rl.SetGesturesEnabled.restype = None
def set_gestures_enabled(gesture_flags: Union[int, Gestures]) -> None:
    """Enable a set of gestures using flags"""
    return _rl.SetGesturesEnabled(_int(gesture_flags))


_rl.IsGestureDetected.argtypes = [Int]
_rl.IsGestureDetected.restype = Bool
def is_gesture_detected(gesture: int) -> bool:
    """Check if a gesture have been detected"""
    return _rl.IsGestureDetected(_int(gesture))


_rl.GetGestureDetected.argtypes = _NOARGS
_rl.GetGestureDetected.restype = Int
def get_gesture_detected() -> int:
    """Get latest detected gesture"""
    return _rl.GetGestureDetected()


_rl.GetTouchPointsCount.argtypes = _NOARGS
_rl.GetTouchPointsCount.restype = Int
def get_touch_points_count() -> int:
    """Get touch points count"""
    return _rl.GetTouchPointsCount()


_rl.GetGestureHoldDuration.argtypes = _NOARGS
_rl.GetGestureHoldDuration.restype = Float
def get_gesture_hold_duration() -> float:
    """Get gesture hold time in milliseconds"""
    return _rl.GetGestureHoldDuration()


_rl.GetGestureDragVector.argtypes = _NOARGS
_rl.GetGestureDragVector.restype = Vector2
def get_gesture_drag_vector() -> Vector2:
    """Get gesture drag vector"""
    return _rl.GetGestureDragVector()


_rl.GetGestureDragAngle.argtypes = _NOARGS
_rl.GetGestureDragAngle.restype = Float
def get_gesture_drag_angle() -> float:
    """Get gesture drag angle"""
    return _rl.GetGestureDragAngle()


_rl.GetGesturePinchVector.argtypes = _NOARGS
_rl.GetGesturePinchVector.restype = Vector2
def get_gesture_pinch_vector() -> Vector2:
    """Get gesture pinch delta"""
    return _rl.GetGesturePinchVector()


_rl.GetGesturePinchAngle.argtypes = _NOARGS
_rl.GetGesturePinchAngle.restype = Float
def get_gesture_pinch_angle() -> float:
    """Get gesture pinch angle"""
    return _rl.GetGesturePinchAngle()


# -----------------------------------------------------------------------------------
# Camera System Functions (Module: camera)
# -----------------------------------------------------------------------------------
_rl.SetCameraMode.argtypes = [Camera, Int]
_rl.SetCameraMode.restype = None
def set_camera_mode(camera: Camera, mode: Union[int, CameraMode]) -> None:
    """Set camera mode (multiple camera modes available)"""
    return _rl.SetCameraMode(camera, _int(mode))


_rl.UpdateCamera.argtypes = [CameraPtr]
_rl.UpdateCamera.restype = None
def update_camera(camera: CameraPtr) -> None:
    """Update camera position for selected mode"""
    return _rl.UpdateCamera(camera)


_rl.SetCameraPanControl.argtypes = [Int]
_rl.SetCameraPanControl.restype = None
def set_camera_pan_control(pan_key: int) -> None:
    """Set camera pan key to combine with mouse movement (free camera)"""
    return _rl.SetCameraPanControl(_int(pan_key))


_rl.SetCameraAltControl.argtypes = [Int]
_rl.SetCameraAltControl.restype = None
def set_camera_alt_control(alt_key: int) -> None:
    """Set camera alt key to combine with mouse movement (free camera)"""
    return _rl.SetCameraAltControl(_int(alt_key))


_rl.SetCameraSmoothZoomControl.argtypes = [Int]
_rl.SetCameraSmoothZoomControl.restype = None
def set_camera_smooth_zoom_control(sz_key: int) -> None:
    """Set camera smooth zoom key to combine with mouse (free camera)"""
    return _rl.SetCameraSmoothZoomControl(_int(sz_key))


_rl.SetCameraMoveControls.argtypes = [Int, Int, Int, Int, Int, Int]
_rl.SetCameraMoveControls.restype = None
def set_camera_move_controls(front_key: int, back_ey: int, right_key: int,
                             left_key: int, up_key: int, down_key: int) -> None:
    """Set camera move controls (1st person and 3rd person cameras)"""
    return _rl.SetCameraMoveControls(_int(front_key), _int(back_ey), _int(right_key),
                                     _int(left_key), _int(up_key), _int(down_key))


# -----------------------------------------------------------------------------------
# Basic Shapes Drawing Functions (Module: shapes)
# -----------------------------------------------------------------------------------

# Basic shapes drawing functions
_rl.DrawPixel.argtypes = [Int, Int, Color]
_rl.DrawPixel.restype = None
def draw_pixel(pos_x: int, pos_y: int, color: Union[Color, Seq]) -> None:
    """Draw a pixel"""
    return _rl.DrawPixel(_int(pos_x), _int(pos_y), _color(color))


_rl.DrawPixelV.argtypes = [Vector2, Color]
_rl.DrawPixelV.restype = None
def draw_pixel_v(position: Union[Vector2, Seq], color: Union[Color, Seq]) -> None:
    """Draw a pixel (Vector version)"""
    return _rl.DrawPixelV(_vec2(position), _color(color))


_rl.DrawLine.argtypes = [Int, Int, Int, Int, Color]
_rl.DrawLine.restype = None
def draw_line(start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: Union[Color, Seq]) -> None:
    """Draw a line"""
    return _rl.DrawLine(_int(start_pos_x), _int(start_pos_y), _int(end_pos_x), _int(end_pos_y), _color(color))


_rl.DrawLineV.argtypes = [Vector2, Vector2, Color]
_rl.DrawLineV.restype = None
def draw_line_v(start_pos: Union[Vector2, Seq], end_pos: Union[Vector2, Seq], color: Union[Color, Seq]) -> None:
    """Draw a line (Vector version)"""
    return _rl.DrawLineV(_vec2(start_pos), _vec2(end_pos), _color(color))


_rl.DrawLineEx.argtypes = [Vector2, Vector2, Float, Color]
_rl.DrawLineEx.restype = None
def draw_line_ex(start_pos: Union[Vector2, Seq], end_pos: Union[Vector2, Seq], thick: float, color: Union[Color, Seq]) -> None:
    """Draw a line defining thickness"""
    return _rl.DrawLineEx(_vec2(start_pos), _vec2(end_pos), _float(_vec2(thick)), _color(color))


_rl.DrawLineBezier.argtypes = [Vector2, Vector2, Float, Color]
_rl.DrawLineBezier.restype = None
def draw_line_bezier(start_pos: Union[Vector2, Seq], end_pos: Union[Vector2, Seq], thick: float, color: Union[Color, Seq]) -> None:
    """Draw a line using cubic-bezier curves in-out"""
    return _rl.DrawLineBezier(_vec2(start_pos), _vec2(end_pos), _float(thick), _color(color))


_rl.DrawCircle.argtypes = [Int, Int, Float, Color]
_rl.DrawCircle.restype = None
def draw_circle(center_x: int, center_y: int, radius: float, color: Union[Color, Seq]) -> None:
    """Draw a color-filled circle"""
    return _rl.DrawCircle(_int(center_x), _int(center_y), _float(radius), _color(color))


_rl.DrawCircleGradient.argtypes = [Int, Int, Float, Color, Color]
_rl.DrawCircleGradient.restype = None
def draw_circle_gradient(center_x: int, center_y: int, radius: float, color1: Union[Color, Seq], color2: Union[Color, Seq]) -> None:
    """Draw a gradient-filled circle"""
    return _rl.DrawCircleGradient(_int(center_x), _int(center_y), _float(radius), _color(color1), _color(color2))


_rl.DrawCircleV.argtypes = [Vector2, Float, Color]
_rl.DrawCircleV.restype = None
def draw_circle_v(center: Union[Vector2, Seq], radius: float, color: Union[Color, Seq]) -> None:
    """Draw a color-filled circle (Vector version)"""
    return _rl.DrawCircleV(_vec2(center), _float(radius), _color(color))


_rl.DrawCircleLines.argtypes = [Int, Int, Float, Color]
_rl.DrawCircleLines.restype = None
def draw_circle_lines(center_x: int, center_y: int, radius: float, color: Union[Color, Seq]) -> None:
    """Draw circle outline"""
    return _rl.DrawCircleLines(_int(center_x), _int(center_y), _float(radius), _color(color))


_rl.DrawRectangle.argtypes = [Int, Int, Int, Int, Color]
_rl.DrawRectangle.restype = None
def draw_rectangle(pos_x: int, pos_y: int, width: int, height: int, color: Union[Color, Seq]) -> None:
    """Draw a color-filled rectangle"""
    return _rl.DrawRectangle(_int(pos_x), _int(pos_y), _int(width), _int(height), _color(color))


_rl.DrawRectangleV.argtypes = [Vector2, Vector2, Color]
_rl.DrawRectangleV.restype = None
def draw_rectangle_v(position: Union[Vector2, Seq], size: Union[Vector2, Seq], color: Union[Color, Seq]) -> None:
    """Draw a color-filled rectangle (Vector version)"""
    return _rl.DrawRectangleV(_vec2(position), _vec2(size), _color(color))


_rl.DrawRectangleRec.argtypes = [Rectangle, Color]
_rl.DrawRectangleRec.restype = None
def draw_rectangle_rec(rec: Union[Rectangle, Seq], color: Union[Color, Seq]) -> None:
    """Draw a color-filled rectangle"""
    return _rl.DrawRectangleRec(rec, _color(color))


_rl.DrawRectanglePro.argtypes = [Rectangle, Vector2, Float, Color]
_rl.DrawRectanglePro.restype = None
def draw_rectangle_pro(rec: Union[Rectangle, Seq], origin: Union[Vector2, Seq], rotation: float, color: Union[Color, Seq]) -> None:
    """Draw a color-filled rectangle with pro parameters"""
    return _rl.DrawRectanglePro(rec, _vec2(origin), _float(rotation), _color(color))


_rl.DrawRectangleGradientV.argtypes = [Int, Int, Int, Int, Color, Color]
_rl.DrawRectangleGradientV.restype = None
def draw_rectangle_gradient_v(pos_x: int, pos_y: int, width: int, height: int, color1: Union[Color, Seq], color2: Union[Color, Seq]) -> None:
    """Draw a vertical-gradient-filled rectangle"""
    return _rl.DrawRectangleGradientV(_int(pos_x), _int(pos_y), _int(width), _int(height), _color(color1), _color(color2))


_rl.DrawRectangleGradientH.argtypes = [Int, Int, Int, Int, Color, Color]
_rl.DrawRectangleGradientH.restype = None
def draw_rectangle_gradient_h(pos_x: int, pos_y: int, width: int, height: int, color1: Union[Color, Seq], color2: Union[Color, Seq]) -> None:
    """Draw a horizontal-gradient-filled rectangle"""
    return _rl.DrawRectangleGradientH(_int(pos_x), _int(pos_y), _int(width), _int(height), _color(color1), _color(color2))


_rl.DrawRectangleGradientEx.argtypes = [Rectangle, Color, Color, Color, Color]
_rl.DrawRectangleGradientEx.restype = None
def draw_rectangle_gradient_ex(rec: Union[Rectangle, Seq], col1: Union[Color, Seq], col2: Union[Color, Seq], col3: Union[Color, Seq], col4: Union[Color, Seq]) -> None:
    """Draw a gradient-filled rectangle with custom vertex colors"""
    return _rl.DrawRectangleGradientEx(rec, _color(col1), _color(col2), _color(col3), _color(col4))


_rl.DrawRectangleLines.argtypes = [Int, Int, Int, Int, Color]
_rl.DrawRectangleLines.restype = None
def draw_rectangle_lines(pos_x: int, pos_y: int, width: int, height: int, color: Union[Color, Seq]) -> None:
    """Draw rectangle outline"""
    return _rl.DrawRectangleLines(_int(pos_x), _int(pos_y), _int(width), _int(height), _color(color))


_rl.DrawRectangleLinesEx.argtypes = [Rectangle, Int, Color]
_rl.DrawRectangleLinesEx.restype = None
def draw_rectangle_lines_ex(rec: Union[Rectangle, Seq], line_thick: int, color: Union[Color, Seq]) -> None:
    """Draw rectangle outline with extended parameters"""
    return _rl.DrawRectangleLinesEx(rec, _int(line_thick), _color(color))


_rl.DrawTriangle.argtypes = [Vector2, Vector2, Vector2, Color]
_rl.DrawTriangle.restype = None
def draw_triangle(v1: Union[Vector2, Seq], v2: Union[Vector2, Seq], v3: Vector2, color: Union[Color, Seq]) -> None:
    """Draw a color-filled triangle"""
    return _rl.DrawTriangle(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


_rl.DrawTriangleLines.argtypes = [Vector2, Vector2, Vector2, Color]
_rl.DrawTriangleLines.restype = None
def draw_triangle_lines(v1: Union[Vector2, Seq], v2: Union[Vector2, Seq], v3: Union[Vector2, Seq], color: Union[Color, Seq]) -> None:
    """Draw triangle outline"""
    return _rl.DrawTriangleLines(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


_rl.DrawPoly.argtypes = [Vector2, Int, Float, Float, Color]
_rl.DrawPoly.restype = None
def draw_poly(center: Union[Vector2, Seq], sides: int, radius: float, rotation: float, color: Union[Color, Seq]) -> None:
    """Draw a regular polygon (Vector version)"""
    return _rl.DrawPoly(_vec2(center), _int(sides), _float(radius), _float(rotation), _color(color))


_rl.DrawPolyEx.argtypes = [Vector2Ptr, Int, Color]
_rl.DrawPolyEx.restype = None
def draw_poly_ex(points: Vector2Ptr, num_points: int, color: Union[Color, Seq]) -> None:
    """Draw a closed polygon defined by points"""
    return _rl.DrawPolyEx(points, _int(num_points), _color(color))


_rl.DrawPolyExLines.argtypes = [Vector2Ptr, Int, Color]
_rl.DrawPolyExLines.restype = None
def draw_poly_ex_lines(points: Vector2Ptr, num_points: int, color: Union[Color, Seq]) -> None:
    """Draw polygon lines"""
    return _rl.DrawPolyExLines(points, _int(num_points), _color(color))


# Basic shapes collision detection functions
_rl.CheckCollisionRecs.argtypes = [Rectangle, Rectangle]
_rl.CheckCollisionRecs.restype = Bool
def check_collision_recs(rec1: Union[Rectangle, Seq], rec2: Union[Rectangle, Seq]) -> bool:
    """Check collision between two rectangles"""
    return _rl.CheckCollisionRecs(_rect(rec1), _rect(rec2))


_rl.CheckCollisionCircles.argtypes = [Vector2, Float, Vector2, Float]
_rl.CheckCollisionCircles.restype = Bool
def check_collision_circles(center1: Union[Vector2, Seq], radius1: float, center2: Union[Vector2, Seq], radius2: float) -> bool:
    """Check collision between two circles"""
    return _rl.CheckCollisionCircles(_vec2(center1), _float(radius1), _vec2(center2), _float(radius2))


_rl.CheckCollisionCircleRec.argtypes = [Vector2, Float, Rectangle]
_rl.CheckCollisionCircleRec.restype = Bool
def check_collision_circle_rec(center: Union[Vector2, Seq], radius: float, rec: Union[Rectangle, Seq]) -> bool:
    """Check collision between circle and rectangle"""
    return _rl.CheckCollisionCircleRec(_vec2(center), _float(radius), _rect(rec))


_rl.GetCollisionRec.argtypes = [Rectangle, Rectangle]
_rl.GetCollisionRec.restype = Rectangle
def get_collision_rec(rec1: Union[Rectangle, Seq], rec2: Union[Rectangle, Seq]):
    """Get collision rectangle for two rectangles collision"""
    return _rl.GetCollisionRec(_rect(rec1), _rect(rec2))


_rl.CheckCollisionPointRec.argtypes = [Vector2, Rectangle]
_rl.CheckCollisionPointRec.restype = Bool
def check_collision_point_rec(point: Union[Vector2, Seq], rec: Union[Rectangle, Seq]) -> bool:
    """Check if point is inside rectangle"""
    return _rl.CheckCollisionPointRec(_vec2(point), _rect(rec))


_rl.CheckCollisionPointCircle.argtypes = [Vector2, Vector2, Float]
_rl.CheckCollisionPointCircle.restype = Bool
def check_collision_point_circle(point: Union[Vector2, Seq], center: Union[Vector2, Seq], radius: float) -> bool:
    """Check if point is inside circle"""
    return _rl.CheckCollisionPointCircle(_vec2(point), _vec2(center), _float(radius))


_rl.CheckCollisionPointTriangle.argtypes = [Vector2, Vector2, Vector2, Vector2]
_rl.CheckCollisionPointTriangle.restype = Bool
def check_collision_point_triangle(point: Union[Vector2, Seq], p1: Union[Vector2, Seq], p2: Union[Vector2, Seq], p3: Union[Vector2, Seq]) -> bool:
    """Check if point is inside a triangle"""
    return _rl.CheckCollisionPointTriangle(_vec2(point), _vec2(p1), _vec2(p2), _vec2(p3))

# -----------------------------------------------------------------------------------
# Texture Loading and Drawing Functions (Module: textures)
# -----------------------------------------------------------------------------------

# Image/Texture2D data loading/unloading/saving functions
_rl.LoadImage.argtypes = [CharPtr]
_rl.LoadImage.restype = Image
def load_image(file_name: AnyStr) -> Image:
    """Load image from file into CPU memory (RAM)"""
    return _rl.LoadImage(_str_in(file_name))


_rl.LoadImageEx.argtypes = [ColorPtr, Int, Int]
_rl.LoadImageEx.restype = Image
def load_image_ex(pixels: ColorPtr, width: int, height: int) -> Image:
    """Load image from Color array data (RGBA - 32bit)"""
    return _rl.LoadImageEx(pixels, _int(width), _int(height))


_rl.LoadImagePro.argtypes = [VoidPtr, Int, Int, Int]
_rl.LoadImagePro.restype = Image
def load_image_pro(data: Union[VoidPtr, bytes], width: int, height: int, img_format: Union[int, PixelFormat]) -> Image:
    """Load image from raw data with parameters"""
    return _rl.LoadImagePro(data, _int(width), _int(height), _int(img_format))


_rl.LoadImageRaw.argtypes = [CharPtr, Int, Int, Int, Int]
_rl.LoadImageRaw.restype = Image
def load_image_raw(file_name: AnyStr, width: int, height: int, img_format: Union[int, PixelFormat], header_size: int) -> Image:
    """Load image from RAW file data"""
    return _rl.LoadImageRaw(_str_in(file_name), _int(width), _int(height), _int(img_format), _int(header_size))


_rl.ExportImage.argtypes = [CharPtr, Image]
_rl.ExportImage.restype = None
def export_image(file_name: AnyStr, image: Image) -> None:
    """Export image as a PNG file"""
    return _rl.ExportImage(_str_in(file_name), image)


_rl.LoadTexture.argtypes = [CharPtr]
_rl.LoadTexture.restype = Texture2D
def load_texture(file_name: AnyStr) -> Texture2D:
    """Load texture from file into GPU memory (VRAM)"""
    return _rl.LoadTexture(_str_in(file_name))


_rl.LoadTextureFromImage.argtypes = [Image]
_rl.LoadTextureFromImage.restype = Texture2D
def load_texture_from_image(image: Image) -> Texture2D:
    """Load texture from image data"""
    return _rl.LoadTextureFromImage(image)


_rl.LoadRenderTexture.argtypes = [Int, Int]
_rl.LoadRenderTexture.restype = RenderTexture2D
def load_render_texture(width: int, height: int) -> RenderTexture2D:
    """Load texture for rendering (framebuffer)"""
    return _rl.LoadRenderTexture(_int(width), _int(height))


_rl.UnloadImage.argtypes = [Image]
_rl.UnloadImage.restype = None
def unload_image(image: Image) -> None:
    """Unload image from CPU memory (RAM)"""
    return _rl.UnloadImage(image)


_rl.UnloadTexture.argtypes = [Texture2D]
_rl.UnloadTexture.restype = None
def unload_texture(texture: Texture2D) -> None:
    """Unload texture from GPU memory (VRAM)"""
    return _rl.UnloadTexture(texture)


_rl.UnloadRenderTexture.argtypes = [RenderTexture2D]
_rl.UnloadRenderTexture.restype = None
def unload_render_texture(target: RenderTexture2D) -> None:
    """Unload render texture from GPU memory (VRAM)"""
    return _rl.UnloadRenderTexture(target)


_rl.GetImageData.argtypes = [Image]
_rl.GetImageData.restype = ColorPtr
def get_image_data(image: Image) -> ColorPtr:
    """Get pixel data from image as a Color struct array"""
    return _rl.GetImageData(image)


_rl.GetImageDataNormalized.argtypes = [Image]
_rl.GetImageDataNormalized.restype = Vector4Ptr
def get_image_data_normalized(image: Image) -> Vector4Ptr:
    """Get pixel data from image as Vector4 array (float normalized)"""
    return _rl.GetImageDataNormalized(image)


_rl.GetPixelDataSize.argtypes = [Int, Int, Int]
_rl.GetPixelDataSize.restype = Int
def get_pixel_data_size(width: int, height: int, pxl_format: Union[int, PixelFormat]) -> int:
    """Get pixel data size in bytes (image or texture)"""
    return _rl.GetPixelDataSize(_int(width), _int(height), _int(pxl_format))


_rl.GetTextureData.argtypes = [Texture2D]
_rl.GetTextureData.restype = Image
def get_texture_data(texture: Texture2D) -> Image:
    """Get pixel data from GPU texture and return an Image"""
    return _rl.GetTextureData(texture)


_rl.UpdateTexture.argtypes = [Texture2D, VoidPtr]
_rl.UpdateTexture.restype = None
def update_texture(texture: Texture2D, pixels: Union[VoidPtr, bytes]) -> None:
    """Update GPU texture with new data"""
    return _rl.UpdateTexture(texture, pixels)


# Image manipulation functions
_rl.ImageCopy.argtypes = [Image]
_rl.ImageCopy.restype = Image
def image_copy(image: Image):
    """Create an image duplicate (useful for transformations)"""
    return _rl.ImageCopy(image)


_rl.ImageToPOT.argtypes = [ImagePtr, Color]
_rl.ImageToPOT.restype = None
def image_to_pot(image: Image, fill_color: Union[Color, Seq]) -> None:
    """Convert image to POT (power-of-two)"""
    return _rl.ImageToPOT(image, _color(fill_color))


_rl.ImageFormat.argtypes = [ImagePtr, Int]
_rl.ImageFormat.restype = None
def image_format(image: Image, new_format: Union[int, PixelFormat]) -> None:
    """Convert image data to desired format"""
    return _rl.ImageFormat(image, _int(new_format))


_rl.ImageAlphaMask.argtypes = [ImagePtr, Image]
_rl.ImageAlphaMask.restype = None
def image_alpha_mask(image: Image, alpha_mask: Image) -> None:
    """Apply alpha mask to image"""
    return _rl.ImageAlphaMask(image, alpha_mask)


_rl.ImageAlphaClear.argtypes = [ImagePtr, Color, Float]
_rl.ImageAlphaClear.restype = None
def image_alpha_clear(image: Image, color: Union[Color, Seq], threshold: float) -> None:
    """Clear alpha channel to desired color"""
    return _rl.ImageAlphaClear(image, _color(color), _float(threshold))


_rl.ImageAlphaCrop.argtypes = [ImagePtr, Float]
_rl.ImageAlphaCrop.restype = None
def image_alpha_crop(image: Image, threshold: float) -> None:
    """Crop image depending on alpha value"""
    return _rl.ImageAlphaCrop(image, _float(threshold))


_rl.ImageAlphaPremultiply.argtypes = [ImagePtr]
_rl.ImageAlphaPremultiply.restype = None
def image_alpha_premultiply(image: Image) -> None:
    """Premultiply alpha channel"""
    return _rl.ImageAlphaPremultiply(image)


_rl.ImageCrop.argtypes = [ImagePtr, Rectangle]
_rl.ImageCrop.restype = None
def image_crop(image: Image, crop: Rectangle) -> None:
    """Crop an image to a defined rectangle"""
    return _rl.ImageCrop(image, _rect(crop))


_rl.ImageResize.argtypes = [ImagePtr, Int, Int]
_rl.ImageResize.restype = None
def image_resize(image: Image, new_width: int, new_height: int) -> None:
    """Resize image (bilinear filtering)"""
    return _rl.ImageResize(image, _int(new_width), _int(new_height))


_rl.ImageResizeNN.argtypes = [ImagePtr, Int, Int]
_rl.ImageResizeNN.restype = None
def image_resize_nn(image: Image, new_width: int, new_height: int) -> None:
    """Resize image (Nearest-Neighbor scaling algorithm)"""
    return _rl.ImageResizeNN(image, _int(new_width), _int(new_height))


_rl.ImageResizeCanvas.argtypes = [ImagePtr, Int, Int, Int, Int, Color]
_rl.ImageResizeCanvas.restype = None
def image_resize_canvas(image: Image, new_width: int, new_height: int, offset_x: int, offset_y: int, color: Union[Color, Seq]) -> None:
    """Resize canvas and fill with color"""
    return _rl.ImageResizeCanvas(image, _int(new_width), _int(new_height), _int(offset_x), _int(offset_y), _color(color))


_rl.ImageMipmaps.argtypes = [ImagePtr]
_rl.ImageMipmaps.restype = None
def image_mipmaps(image: Image) -> None:
    """Generate all mipmap levels for a provided image"""
    return _rl.ImageMipmaps(image)


_rl.ImageDither.argtypes = [ImagePtr, Int, Int, Int, Int]
_rl.ImageDither.restype = None
def image_dither(image: Image, r_bpp: int, g_bpp: int, b_bpp: int, a_bpp: int) -> None:
    """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
    return _rl.ImageDither(image, _int(r_bpp), _int(g_bpp), _int(b_bpp), _int(a_bpp))


_rl.ImageText.argtypes = [CharPtr, Int, Color]
_rl.ImageText.restype = Image
def image_text(text: AnyStr, font_size: int, color: Union[Color, Seq]) -> Image:
    """Create an image from text (default font)"""
    return _rl.ImageText(_str_in(text), _int(font_size), _color(color))


_rl.ImageTextEx.argtypes = [Font, CharPtr, Float, Float, Color]
_rl.ImageTextEx.restype = Image
def image_text_ex(font: Font, text: AnyStr, font_size: float, spacing: float, tint: Union[Color, Seq]) -> Image:
    """Create an image from text (custom sprite font)"""
    return _rl.ImageTextEx(font, _str_in(text), _float(font_size), _float(spacing), _color(tint))


_rl.ImageDraw.argtypes = [ImagePtr, Image, Rectangle, Rectangle]
_rl.ImageDraw.restype = None
def image_draw(dst: Image, src: Image, src_rec: Union[Rectangle, Seq], dst_rec: Union[Rectangle, Seq]) -> None:
    """Draw a source image within a destination image"""
    return _rl.ImageDraw(dst, src, _rect(src_rec), _rect(dst_rec))


_rl.ImageDrawRectangle.argtypes = [ImagePtr, Vector2, Rectangle, Color]
_rl.ImageDrawRectangle.restype = None
def image_draw_rectangle(dst: Image, position: Union[Vector2, Seq], rec: Union[Rectangle, Seq], color: Union[Color, Seq]) -> None:
    """Draw rectangle within an image"""
    return _rl.ImageDrawRectangle(dst, _vec2(position), _rect(rec), _color(color))


_rl.ImageDrawText.argtypes = [ImagePtr, Vector2, CharPtr, Int, Color]
_rl.ImageDrawText.restype = None
def image_draw_text(dst: Image, position: Union[Vector2, Seq], text: AnyStr, font_size: int, color: Union[Color, Seq]) -> None:
    """Draw text (default font) within an image (destination)"""
    return _rl.ImageDrawText(dst, _vec2(position), _str_in(text), _int(font_size), _color(color))


_rl.ImageDrawTextEx.argtypes = [ImagePtr, Vector2, Font, CharPtr, Float, Float, Color]
_rl.ImageDrawTextEx.restype = None
def image_draw_text_ex(dst: Image, position: Union[Vector2, Seq], font: Font, text: AnyStr, font_size: float, spacing: float, color: Union[Color, Seq]) -> None:
    """Draw text (custom sprite font) within an image (destination)"""
    return _rl.ImageDrawTextEx(dst, _vec2(position), font, _str_in(text), _float(font_size), _float(spacing), _color(color))


_rl.ImageFlipVertical.argtypes = [ImagePtr]
_rl.ImageFlipVertical.restype = None
def image_flip_vertical(image: Image) -> None:
    """Flip image vertically"""
    return _rl.ImageFlipVertical(image)


_rl.ImageFlipHorizontal.argtypes = [ImagePtr]
_rl.ImageFlipHorizontal.restype = None
def image_flip_horizontal(image: Image) -> None:
    """Flip image horizontally"""
    return _rl.ImageFlipHorizontal(image)


_rl.ImageRotateCW.argtypes = [ImagePtr]
_rl.ImageRotateCW.restype = None
def image_rotate_cw(image: Image) -> None:
    """Rotate image clockwise 90deg"""
    return _rl.ImageRotateCW(image)


_rl.ImageRotateCCW.argtypes = [ImagePtr]
_rl.ImageRotateCCW.restype = None
def image_rotate_ccw(image: Image) -> None:
    """Rotate image counter-clockwise 90deg"""
    return _rl.ImageRotateCCW(image)


_rl.ImageColorTint.argtypes = [ImagePtr, Color]
_rl.ImageColorTint.restype = None
def image_color_tint(image: Image, color: Union[Color, Seq]) -> None:
    """Modify image color: tint"""
    return _rl.ImageColorTint(image, _color(color))


_rl.ImageColorInvert.argtypes = [ImagePtr]
_rl.ImageColorInvert.restype = None
def image_color_invert(image: Image) -> None:
    """Modify image color: invert"""
    return _rl.ImageColorInvert(image)


_rl.ImageColorGrayscale.argtypes = [ImagePtr]
_rl.ImageColorGrayscale.restype = None
def image_color_grayscale(image: Image) -> None:
    """Modify image color: grayscale"""
    return _rl.ImageColorGrayscale(image)


_rl.ImageColorContrast.argtypes = [ImagePtr, Float]
_rl.ImageColorContrast.restype = None
def image_color_contrast(image: Image, contrast: float) -> None:
    """Modify image color: contrast (-100 to 100)"""
    return _rl.ImageColorContrast(image, _float(contrast))


_rl.ImageColorBrightness.argtypes = [ImagePtr, Int]
_rl.ImageColorBrightness.restype = None
def image_color_brightness(image: Image, brightness: int) -> None:
    """Modify image color: brightness (-255 to 255)"""
    return _rl.ImageColorBrightness(image, _int(brightness))


_rl.ImageColorReplace.argtypes = [ImagePtr, Color, Color]
_rl.ImageColorReplace.restype = None
def image_color_replace(image: Image, color: Union[Color, Seq], replace: Union[Color, Seq]) -> None:
    """Modify image color: replace color"""
    return _rl.ImageColorReplace(image, _color(color), _color(replace))


_rl.GenImageColor.argtypes = [Int, Int, Color]
_rl.GenImageColor.restype = Image
def gen_image_color(width: int, height: int, color: Union[Color, Seq]) -> Image:
    """Generate image: plain color"""
    return _rl.GenImageColor(width, _int(height), _color(color))


_rl.GenImageGradientV.argtypes = [Int, Int, Color, Color]
_rl.GenImageGradientV.restype = Image
def gen_image_gradient_v(width: int, height: int, top: Union[Color, Seq], bottom: Union[Color, Seq]) -> Image:
    """Generate image: vertical gradient"""
    return _rl.GenImageGradientV(_int(width), _int(height), _color(top), _color(bottom))


_rl.GenImageGradientH.argtypes = [Int, Int, Color, Color]
_rl.GenImageGradientH.restype = Image
def gen_image_gradient_h(width: int, height: int, left: Union[Color, Seq], right: Union[Color, Seq]) -> Image:
    """Generate image: horizontal gradient"""
    return _rl.GenImageGradientH(_int(width), _int(height), _color(left), _color(right))


_rl.GenImageGradientRadial.argtypes = [Int, Int, Float, Color, Color]
_rl.GenImageGradientRadial.restype = Image
def gen_image_gradient_radial(width: int, height: int, density: float, inner: Union[Color, Seq], outer: Union[Color, Seq]) -> Image:
    """Generate image: radial gradient"""
    return _rl.GenImageGradientRadial(_int(width), _int(height), _float(density), _color(inner), _color(outer))


_rl.GenImageChecked.argtypes = [Int, Int, Int, Int, Color, Color]
_rl.GenImageChecked.restype = Image
def gen_image_checked(width: int, height: int, checks_x: int, checks_y: int, col1: Union[Color, Seq], col2: Union[Color, Seq]) -> Image:
    """Generate image: checked"""
    return _rl.GenImageChecked(_int(width), _int(height), _int(checks_x), _int(checks_y), _color(col1), _color(col2))


_rl.GenImageWhiteNoise.argtypes = [Int, Int, Float]
_rl.GenImageWhiteNoise.restype = Image
def gen_image_white_noise(width: int, height: int, factor: float) -> Image:
    """Generate image: white noise"""
    return _rl.GenImageWhiteNoise(_int(width), _int(height), _float(factor))


_rl.GenImagePerlinNoise.argtypes = [Int, Int, Int, Int, Float]
_rl.GenImagePerlinNoise.restype = Image
def gen_image_perlin_noise(width: int, height: int, offset_x: int, offset_y: int, scale: float) -> Image:
    """Generate image: perlin noise"""
    return _rl.GenImagePerlinNoise(_int(width), _int(height), _int(offset_x), _int(offset_y), _float(scale))


_rl.GenImageCellular.argtypes = [Int, Int, Int]
_rl.GenImageCellular.restype = Image
def gen_image_cellular(width: int, height: int, tile_size: int) -> Image:
    """Generate image: cellular algorithm. Bigger tileSize means bigger cells"""
    return _rl.GenImageCellular(_int(width), _int(height), _int(tile_size))


_rl.GenTextureMipmaps.argtypes = [Texture2DPtr]
_rl.GenTextureMipmaps.restype = None
def gen_texture_mipmaps(texture: Texture2DPtr) -> None:
    """Generate GPU mipmaps for a texture"""
    return _rl.GenTextureMipmaps(texture)


_rl.SetTextureFilter.argtypes = [Texture2D, Int]
_rl.SetTextureFilter.restype = None
def set_texture_filter(texture: Texture2D, filter_mode: int) -> None:
    """Set texture scaling filter mode"""
    return _rl.SetTextureFilter(texture, _int(filter_mode))


_rl.SetTextureWrap.argtypes = [Texture2D, Int]
_rl.SetTextureWrap.restype = None
def set_texture_wrap(texture: Texture2D, wrap_mode: int) -> None:
    """Set texture wrapping mode"""
    return _rl.SetTextureWrap(texture, _int(wrap_mode))


_rl.DrawTexture.argtypes = [Texture2D, Int, Int, Color]
_rl.DrawTexture.restype = None
def draw_texture(texture: Texture2D, pos_x: int, pos_y: int, tint: Union[Color, Seq]) -> None:
    """Draw a Texture2D"""
    return _rl.DrawTexture(texture, _int(pos_x), _int(pos_y), _color(tint))


_rl.DrawTextureV.argtypes = [Texture2D, Vector2, Color]
_rl.DrawTextureV.restype = None
def draw_texture_v(texture: Texture2D, position: Union[Vector2, Seq], tint: Union[Color, Seq]) -> None:
    """Draw a Texture2D with position defined as Vector2"""
    return _rl.DrawTextureV(texture, _vec2(position), _color(tint))


_rl.DrawTextureEx.argtypes = [Texture2D, Vector2, Float, Float, Color]
_rl.DrawTextureEx.restype = None
def draw_texture_ex(texture: Texture2D, position: Union[Vector2, Seq], rotation: float, scale: float, tint: Union[Color, Seq]) -> None:
    """Draw a Texture2D with extended parameters"""
    return _rl.DrawTextureEx(texture, _vec2(position), _float(rotation), _float(scale), _color(tint))


_rl.DrawTextureRec.argtypes = [Texture2D, Rectangle, Vector2, Color]
_rl.DrawTextureRec.restype = None
def draw_texture_rec(texture: Texture2D, source_rec: Union[Rectangle, Seq], position: Union[Vector2, Seq], tint: Union[Color, Seq]) -> None:
    """Draw a part of a texture defined by a rectangle"""
    return _rl.DrawTextureRec(texture, _rect(source_rec), _vec2(position), _color(tint))


_rl.DrawTexturePro.argtypes = [Texture2D, Rectangle, Rectangle, Vector2, Float, Color]
_rl.DrawTexturePro.restype = None
def draw_texture_pro(texture: Texture2D, source_rec: Union[Rectangle, Seq], dest_rec: Union[Rectangle, Seq], origin: Union[Vector2, Seq], rotation: float, tint: Union[Color, Seq]) -> None:
    """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
    return _rl.DrawTexturePro(texture, _rect(source_rec), _rect(dest_rec), _vec2(origin), _float(rotation), _color(tint))

if ENABLE_V2_0_0_FEATURE_DRAWTEXTURENPATCH:
    _rl.DrawTextureNPatch.argtypes = [Texture2D, NPatchInfo, Rectangle, Vector2, Float, Color]
    _rl.DrawTextureNPatch.restype = None
    def draw_texture_npatch(texture: Texture2D, npatch_info: NPatchInfo, dest_rec: Union[Rectangle, Seq], origin: Union[Vector2, Seq], rotation: float, tint: Union[Color, Seq]) -> None:
        """Draws a textures that stretches and shrinks nicely."""
        return _rl.DrawNPatch(texture, npatch_info, _rect(dest_rec), _vec2(origin), _float(rotation), _color(tint))
else:
    def draw_texture_npatch(*args, **kwargs) -> None:
        """WARNING: THIS FUNCTION HAS NO EFFECT!"""
        pass

# -----------------------------------------------------------------------------------
# Font Loading and Text Drawing Functions (Module: text)
# -----------------------------------------------------------------------------------

# Font loading/unloading functions
_rl.GetFontDefault.argtypes = []
_rl.GetFontDefault.restype = Font
def get_font_default() -> Font:
    """Get the default Font"""
    return _rl.GetFontDefault()


_rl.LoadFont.argtypes = [CharPtr]
_rl.LoadFont.restype = Font
def load_font(file_name: AnyStr) -> Font:
    """Load font from file into GPU memory (VRAM)"""
    return _rl.LoadFont(_str_in(file_name))


_rl.LoadFontEx.argtypes = [CharPtr, Int, Int, IntPtr]
_rl.LoadFontEx.restype = Font
def load_font_ex(file_name: AnyStr, font_size: int, chars_count: int, font_chars: int) -> Font:
    """Load font from file with extended parameters"""
    return _rl.LoadFontEx(_str_in(file_name), _int(font_size), _int(chars_count), _int(font_chars))


_rl.LoadFontData.argtypes = [CharPtr, Int, IntPtr, Int, Bool]
_rl.LoadFontData.restype = CharInfoPtr
def load_font_data(file_name: AnyStr, font_size: int, font_chars: int, chars_count: int, sdf: bool) -> CharInfoPtr:
    """Load font data for further use"""
    return _rl.LoadFontData(_str_in(file_name), _int(font_size), font_chars, _int(chars_count), sdf)


_rl.GenImageFontAtlas.argtypes = [CharInfoPtr, Int, Int, Int, Int]
_rl.GenImageFontAtlas.restype = Image
def gen_image_font_atlas(chars: CharInfoPtr, font_size: int, chars_count: int, padding: int, pack_method: int) -> Image:
    """Generate image font atlas using chars info"""
    return _rl.GenImageFontAtlas(chars, _int(font_size), _int(chars_count), _int(padding), _int(pack_method))


_rl.UnloadFont.argtypes = [Font]
_rl.UnloadFont.restype = None
def unload_font(font: Font) -> None:
    """Unload Font from GPU memory (VRAM)"""
    return _rl.UnloadFont(font)

# Text drawing functions
_rl.DrawFPS.argtypes = [Int, Int]
_rl.DrawFPS.restype = None
def draw_fps(pos_x: int, pos_y: int) -> None:
    """Shows current FPS"""
    return _rl.DrawFPS(_int(pos_x), _int(pos_y))


_rl.DrawText.argtypes = [CharPtr, Int, Int, Int, Color]
_rl.DrawText.restype = None
def draw_text(text: AnyStr, pos_x: int, pos_y: int, font_size: int, color: Union[Color, Seq]) -> None:
    """Draw text (using default font)"""
    return _rl.DrawText(_str_in(text), _int(pos_x), _int(pos_y), _int(font_size), _color(color))


_rl.DrawTextEx.argtypes = [Font, CharPtr, Vector2, Float, Float, Color]
_rl.DrawTextEx.restype = None
def draw_text_ex(font: Font, text: AnyStr, position: Union[Vector2, Seq], font_size: float, spacing: float, tint: Union[Color, Seq]) -> None:
    """Draw text using font and additional parameters"""
    return _rl.DrawTextEx(font, _str_in(text), position, _float(font_size), _float(spacing), _color(tint))


# Text misc. functions
_rl.MeasureText.argtypes = [CharPtr, Int]
_rl.MeasureText.restype = Int
def measure_text(text: AnyStr, font_size: int) -> int:
    """Measure string width for default font"""
    return _rl.MeasureText(_str_in(text), _int(font_size))


_rl.MeasureTextEx.argtypes = [Font, CharPtr, Float, Float]
_rl.MeasureTextEx.restype = Vector2
def measure_text_ex(font: Font, text: AnyStr, font_size: float, spacing: float) -> Vector2:
    """Measure string size for Font"""
    return _rl.MeasureTextEx(font, _str_in(text), _float(font_size), _float(spacing))


_rl.FormatText.argtypes = [CharPtr]
_rl.FormatText.restype = CharPtr
def format_text(text: AnyStr, *args) -> bytes:
    """Formatting of text with variables to 'embed'"""
    return _rl.FormatText(_str_in(text), *args)


_rl.SubText.argtypes = [CharPtr, Int, Int]
_rl.SubText.restype = CharPtr
def sub_text(text: AnyStr, position: int, length: int) -> bytes:
    """Get a piece of a text string"""
    return _rl.SubText(_str_in(text), _int(position), _int(length))


_rl.GetGlyphIndex.argtypes = [Font, Int]
_rl.GetGlyphIndex.restype = Int
def get_glyph_index(font: Font, character: int) -> int:
    """Get index position for a unicode character on font"""
    return _rl.GetGlyphIndex(font, _int(character))


# -----------------------------------------------------------------------------------
# Basic 3d Shapes Drawing Functions (Module: models)
# -----------------------------------------------------------------------------------

# Basic geometric 3D shapes drawing functions
_rl.DrawLine3D.argtypes = [Vector3, Vector3, Color]
_rl.DrawLine3D.restype = None
def draw_line3_d(start_pos: Union[Vector3, Seq], end_pos: Union[Vector3, Seq], color: Union[Color, Seq]) -> None:
    """Draw a line in 3D world space"""
    return _rl.DrawLine3D(_vec3(start_pos), _vec3(end_pos), _color(color))


_rl.DrawCircle3D.argtypes = [Vector3, Float, Vector3, Float, Color]
_rl.DrawCircle3D.restype = None
def draw_circle3_d(center: Union[Vector3, Seq], radius: float, rotation_axis: Union[Vector3, Seq], rotation_angle: float, color: Union[Color, Seq]) -> None:
    """Draw a circle in 3D world space"""
    return _rl.DrawCircle3D(_vec3(center), _float(radius), _vec3(rotation_axis), _float(rotation_angle), _color(color))


_rl.DrawCube.argtypes = [Vector3, Float, Float, Float, Color]
_rl.DrawCube.restype = None
def draw_cube(position: Union[Vector3, Seq], width: float, height: float, length: float, color: Union[Color, Seq]) -> None:
    """Draw cube"""
    return _rl.DrawCube(_vec3(position), _float(width), _float(height), _float(length), _color(color))


_rl.DrawCubeV.argtypes = [Vector3, Vector3, Color]
_rl.DrawCubeV.restype = None
def draw_cube_v(position: Union[Vector3, Seq], size: Union[Vector3, Seq], color: Union[Color, Seq]) -> None:
    """Draw cube (Vector version)"""
    return _rl.DrawCubeV(_vec3(position), _vec3(size), _color(color))


_rl.DrawCubeWires.argtypes = [Vector3, Float, Float, Float, Color]
_rl.DrawCubeWires.restype = None
def draw_cube_wires(position: Union[Vector3, Seq], width: float, height: float, length: float, color: Union[Color, Seq]) -> None:
    """Draw cube wires"""
    return _rl.DrawCubeWires(_vec3(position), _float(width), _float(height), _float(length), _color(color))


_rl.DrawCubeTexture.argtypes = [Texture2D, Vector3, Float, Float, Float, Color]
_rl.DrawCubeTexture.restype = None
def draw_cube_texture(texture: Texture2D, position: Union[Vector3, Seq], width: float, height: float, length: float, color: Union[Color, Seq]) -> None:
    """Draw cube textured"""
    return _rl.DrawCubeTexture(texture, _vec3(position), _float(width), _float(height), _float(length), _color(color))


_rl.DrawSphere.argtypes = [Vector3, Float, Color]
_rl.DrawSphere.restype = None
def draw_sphere(center_pos: Union[Vector3, Seq], radius: float, color: Union[Color, Seq]) -> None:
    """Draw sphere"""
    return _rl.DrawSphere(_vec3(center_pos), _float(radius), _color(color))


_rl.DrawSphereEx.argtypes = [Vector3, Float, Int, Int, Color]
_rl.DrawSphereEx.restype = None
def draw_sphere_ex(center_pos: Union[Vector3, Seq], radius: float, rings: int, slices: int, color: Union[Color, Seq]) -> None:
    """Draw sphere with extended parameters"""
    return _rl.DrawSphereEx(_vec3(center_pos), _float(radius), _int(rings), _int(slices), _color(color))


_rl.DrawSphereWires.argtypes = [Vector3, Float, Int, Int, Color]
_rl.DrawSphereWires.restype = None
def draw_sphere_wires(center_pos: Union[Vector3, Seq], radius: float, rings: int, slices: int, color: Union[Color, Seq]) -> None:
    """Draw sphere wires"""
    return _rl.DrawSphereWires(_vec3(center_pos), _float(radius), _int(rings), _int(slices), _color(color))


_rl.DrawCylinder.argtypes = [Vector3, Float, Float, Float, Int, Color]
_rl.DrawCylinder.restype = None
def draw_cylinder(position: Union[Vector3, Seq], radius_top: float, radius_bottom: float, height: float, slices: int, color: Union[Color, Seq]) -> None:
    """Draw a cylinder/cone"""
    return _rl.DrawCylinder(_vec3(position), _float(radius_top), _float(radius_bottom), _float(height), _int(slices), _color(color))


_rl.DrawCylinderWires.argtypes = [Vector3, Float, Float, Float, Int, Color]
_rl.DrawCylinderWires.restype = None
def draw_cylinder_wires(position: Union[Vector3, Seq], radius_top: float, radius_bottom: float, height: float, slices: int, color: Union[Color, Seq]) -> None:
    """Draw a cylinder/cone wires"""
    return _rl.DrawCylinderWires(_vec3(position), _float(radius_top), _float(radius_bottom), _float(height), _int(slices), _color(color))


_rl.DrawPlane.argtypes = [Vector3, Vector2, Color]
_rl.DrawPlane.restype = None
def draw_plane(center_pos: Union[Vector3, Seq], size: Union[Vector2, Seq], color: Union[Color, Seq]) -> None:
    """Draw a plane XZ"""
    return _rl.DrawPlane(_vec3(center_pos), _vec2(size), _color(color))


_rl.DrawRay.argtypes = [Ray, Color]
_rl.DrawRay.restype = None
def draw_ray(ray: Ray, color: Union[Color, Seq]) -> None:
    """Draw a ray line"""
    return _rl.DrawRay(ray, _color(color))


_rl.DrawGrid.argtypes = [Int, Float]
_rl.DrawGrid.restype = None
def draw_grid(slices: int, spacing: float) -> None:
    """Draw a grid (centered at (0, 0, 0))"""
    return _rl.DrawGrid(_int(slices), _float(spacing))


_rl.DrawGizmo.argtypes = [Vector3]
_rl.DrawGizmo.restype = None
def draw_gizmo(position: Union[Vector3, Seq]) -> None:
    """Draw simple gizmo"""
    return _rl.DrawGizmo(_vec3(position))


# -----------------------------------------------------------------------------------
# Model 3d Loading and Drawing Functions (Module: models)
# -----------------------------------------------------------------------------------

# Model loading/unloading functions
_rl.LoadModel.argtypes = [CharPtr]
_rl.LoadModel.restype = Model
def load_model(file_name: AnyStr) -> Mesh:
    """Load model from files (mesh and material)"""
    return _rl.LoadModel(_str_in(_int(file_name)))


_rl.LoadModelFromMesh.argtypes = [Mesh]
_rl.LoadModelFromMesh.restype = Model
def load_model_from_mesh(mesh: Mesh) -> Mesh:
    """Load model from generated mesh"""
    return _rl.LoadModelFromMesh(mesh)


_rl.UnloadModel.argtypes = [Model]
_rl.UnloadModel.restype = None
def unload_model(model: Model) -> None:
    """Unload model from memory (RAM and/or VRAM)"""
    return _rl.UnloadModel(model)


# Mesh loading/unloading functions
_rl.LoadMesh.argtypes = [CharPtr]
_rl.LoadMesh.restype = Mesh
def load_mesh(file_name: AnyStr) -> Mesh:
    """Load mesh from file"""
    return _rl.LoadMesh(_str_in(_int(file_name)))


_rl.UnloadMesh.argtypes = [MeshPtr]
_rl.UnloadMesh.restype = None
def unload_mesh(mesh: Mesh) -> None:
    """Unload mesh from memory (RAM and/or VRAM)"""
    return _rl.UnloadMesh(mesh)


_rl.ExportMesh.argtypes = [CharPtr, Mesh]
_rl.ExportMesh.restype = None
def export_mesh(file_name: AnyStr, mesh: Mesh) -> None:
    """Export mesh as an OBJ file"""
    return _rl.ExportMesh(_str_in(_int(file_name)), mesh)


# Mesh manipulation functions
_rl.MeshBoundingBox.argtypes = [Mesh]
_rl.MeshBoundingBox.restype = BoundingBox
def mesh_bounding_box(mesh: Mesh) -> BoundingBox:
    """Compute mesh bounding box limits"""
    return _rl.MeshBoundingBox(mesh)


_rl.MeshTangents.argtypes = [MeshPtr]
_rl.MeshTangents.restype = None
def mesh_tangents(mesh: MeshPtr) -> None:
    """Compute mesh tangents"""
    return _rl.MeshTangents(mesh)


_rl.MeshBinormals.argtypes = [MeshPtr]
_rl.MeshBinormals.restype = None
def mesh_binormals(mesh: MeshPtr) -> None:
    """Compute mesh binormals"""
    return _rl.MeshBinormals(mesh)


# Mesh generation functions
_rl.GenMeshPlane.argtypes = [Float, Float, Int, Int]
_rl.GenMeshPlane.restype = Mesh
def gen_mesh_plane(width: float, length: float, res_x: int, res_z: int) -> Mesh:
    """Generate plane mesh (with subdivisions)"""
    return _rl.GenMeshPlane(width, _float(length), _int(res_x), _int(res_z))


_rl.GenMeshCube.argtypes = [Float, Float, Float]
_rl.GenMeshCube.restype = Mesh
def gen_mesh_cube(width: float, height: float, length: float) -> Mesh:
    """Generate cuboid mesh"""
    return _rl.GenMeshCube(_float(width), _float(height), _float(length))


_rl.GenMeshSphere.argtypes = [Float, Int, Int]
_rl.GenMeshSphere.restype = Mesh
def gen_mesh_sphere(radius: float, rings: int, slices: int) -> Mesh:
    """Generate sphere mesh (standard sphere)"""
    return _rl.GenMeshSphere(_float(radius), _int(rings), _int(slices))


_rl.GenMeshHemiSphere.argtypes = [Float, Int, Int]
_rl.GenMeshHemiSphere.restype = Mesh
def gen_mesh_hemi_sphere(radius: float, rings: int, slices: int) -> Mesh:
    """Generate half-sphere mesh (no bottom cap)"""
    return _rl.GenMeshHemiSphere(_float(radius), _int(rings), _int(slices))


_rl.GenMeshCylinder.argtypes = [Float, Float, Int]
_rl.GenMeshCylinder.restype = Mesh
def gen_mesh_cylinder(radius: float, height: float, slices: int) -> Mesh:
    """Generate cylinder mesh"""
    return _rl.GenMeshCylinder(_float(radius), _float(height), _int(slices))


_rl.GenMeshTorus.argtypes = [Float, Float, Int, Int]
_rl.GenMeshTorus.restype = Mesh
def gen_mesh_torus(radius: float, size: float, rad_seg: int, sides: int) -> Mesh:
    """Generate torus mesh"""
    return _rl.GenMeshTorus(_float(radius), _float(size), _int(rad_seg), _int(sides))


_rl.GenMeshKnot.argtypes = [Float, Float, Int, Int]
_rl.GenMeshKnot.restype = Mesh
def gen_mesh_knot(radius: float, size: float, rad_seg: int, sides: int) -> Mesh:
    """Generate trefoil knot mesh"""
    return _rl.GenMeshKnot(_float(radius), _float(size), _int(rad_seg), _int(sides))


_rl.GenMeshHeightmap.argtypes = [Image, Vector3]
_rl.GenMeshHeightmap.restype = Mesh
def gen_mesh_heightmap(heightmap: Image, size: Union[Vector3, Seq]) -> Mesh:
    """Generate heightmap mesh from image data"""
    return _rl.GenMeshHeightmap(heightmap, _vec3(size))


_rl.GenMeshCubicmap.argtypes = [Image, Vector3]
_rl.GenMeshCubicmap.restype = Mesh
def gen_mesh_cubicmap(cubicmap: Image, cube_size: Union[Vector3, Seq]) -> Mesh:
    """Generate cubes-based map mesh from image data"""
    return _rl.GenMeshCubicmap(cubicmap, _vec3(cube_size))


# Material loading/unloading functions
_rl.LoadMaterial.argtypes = [CharPtr]
_rl.LoadMaterial.restype = Material
def load_material(file_name: AnyStr) -> Material:
    """Load material from file"""
    return _rl.LoadMaterial(file_name)


_rl.LoadMaterialDefault.argtypes = _NOARGS
_rl.LoadMaterialDefault.restype = Material
def load_material_default() -> Material:
    """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
    return _rl.LoadMaterialDefault()


_rl.UnloadMaterial.argtypes = [Material]
_rl.UnloadMaterial.restype = None
def unload_material(material: Material) -> None:
    """Unload material from GPU memory (VRAM)"""
    return _rl.UnloadMaterial(material)


# Model drawing functions
_rl.DrawModel.argtypes = [Model, Vector3, Float, Color]
_rl.DrawModel.restype = None
def draw_model(model: Model, position: Union[Vector3, Seq], scale: float, tint: Union[Color, Seq]) -> None:
    """Draw a model (with texture if set)"""
    return _rl.DrawModel(model, _vec3(position), _float(scale), _color(tint))


_rl.DrawModelEx.argtypes = [Model, Vector3, Vector3, Float, Vector3, Color]
_rl.DrawModelEx.restype = None
def draw_model_ex(model: Model, position: Vector3, rotation_axis: Vector3, rotation_angle: float, scale: Vector3, tint: Color) -> None:
    """Draw a model with extended parameters"""
    return _rl.DrawModelEx(model, _vec3(position), _vec3(rotation_axis), _float(rotation_angle), _vec3(scale), _color(tint))


_rl.DrawModelWires.argtypes = [Model, Vector3, Float, Color]
_rl.DrawModelWires.restype = None
def draw_model_wires(model: Model, position: Union[Vector3, Seq], scale: float, tint: Union[Color, Seq]) -> None:
    """Draw a model wires (with texture if set)"""
    return _rl.DrawModelWires(model, _vec3(position), _float(scale), _color(tint))


_rl.DrawModelWiresEx.argtypes = [Model, Vector3, Vector3, Float, Vector3, Color]
_rl.DrawModelWiresEx.restype = None
def draw_model_wires_ex(model: Model, position: Union[Vector3, Seq], rotation_axis: Union[Vector3, Seq], rotation_angle: float, scale: Union[Vector3, Seq], tint: Union[Color, Seq]) -> None:
    """Draw a model wires (with texture if set) with extended parameters"""
    return _rl.DrawModelWiresEx(model, _vec3(position), _vec3(rotation_axis), _float(rotation_angle), _vec3(scale), _color(tint))


_rl.DrawBoundingBox.argtypes = [BoundingBox, Color]
_rl.DrawBoundingBox.restype = None
def draw_bounding_box(box: BoundingBox, color: Union[Color, Seq]) -> None:
    """Draw bounding box (wires)"""
    return _rl.DrawBoundingBox(box, _color(color))


_rl.DrawBillboard.argtypes = [Camera, Texture2D, Vector3, Float, Color]
_rl.DrawBillboard.restype = None
def draw_billboard(camera: Camera, texture: Texture2D, center: Union[Vector3, Seq], size: float, tint: Union[Color, Seq]) -> None:
    """Draw a billboard texture"""
    return _rl.DrawBillboard(camera, texture, _vec3(center), _float(size), _color(tint))


_rl.DrawBillboardRec.argtypes = [Camera, Texture2D, Rectangle, Vector3, Float, Color]
_rl.DrawBillboardRec.restype = None
def draw_billboard_rec(camera: Camera, texture: Texture2D, source_rec: Union[Rectangle, Seq], center: Union[Vector3, Seq], size: float, tint: Union[Color, Seq]) -> None:
    """Draw a billboard texture defined by source_rec"""
    return _rl.DrawBillboardRec(camera, texture, _rect(source_rec), _vec3(center), _float(size), _color(tint))


# Collision detection functions
_rl.CheckCollisionSpheres.argtypes = [Vector3, Float, Vector3, Float]
_rl.CheckCollisionSpheres.restype = Bool
def check_collision_spheres(center_a: Union[Vector3, Seq], radius_a: float, center_b: Union[Vector3, Seq], radius_b: float) -> bool:
    """Detect collision between two spheres"""
    return _rl.CheckCollisionSpheres(_vec3(center_a), _float(radius_a), _vec3(center_b), _float(radius_b))


_rl.CheckCollisionBoxes.argtypes = [BoundingBox, BoundingBox]
_rl.CheckCollisionBoxes.restype = Bool
def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> bool:
    """Detect collision between two bounding boxes"""
    return _rl.CheckCollisionBoxes(box1, box2)


_rl.CheckCollisionBoxSphere.argtypes = [BoundingBox, Vector3, Float]
_rl.CheckCollisionBoxSphere.restype = Bool
def check_collision_box_sphere(box: BoundingBox, center_sphere: Union[Vector3, Seq], radius_sphere: float) -> bool:
    """Detect collision between box and sphere"""
    return _rl.CheckCollisionBoxSphere(box, _vec3(center_sphere), _float(radius_sphere))


_rl.CheckCollisionRaySphere.argtypes = [Ray, Vector3, Float]
_rl.CheckCollisionRaySphere.restype = Bool
def check_collision_ray_sphere(ray: Ray, sphere_position: Union[Vector3, Seq], sphere_radius: float) -> bool:
    """Detect collision between ray and sphere"""
    return _rl.CheckCollisionRaySphere(ray, _vec3(sphere_position), _float(sphere_radius))


_rl.CheckCollisionRaySphereEx.argtypes = [Ray, Vector3, Float, Vector3Ptr]
_rl.CheckCollisionRaySphereEx.restype = Bool
def check_collision_ray_sphere_ex(ray: Ray, sphere_position: Union[Vector3, Seq], sphere_radius: float, collision_point: Vector3Ptr) -> bool:
    """Detect collision between ray and sphere, returns collision point"""
    return _rl.CheckCollisionRaySphereEx(ray, _vec3(sphere_position), _float(sphere_radius), collision_point)


_rl.CheckCollisionRayBox.argtypes = [Ray, BoundingBox]
_rl.CheckCollisionRayBox.restype = Bool
def check_collision_ray_box(ray: Ray, box: BoundingBox) -> bool:
    """Detect collision between ray and box"""
    return _rl.CheckCollisionRayBox(ray, box)


_rl.GetCollisionRayModel.argtypes = [Ray, ModelPtr]
_rl.GetCollisionRayModel.restype = RayHitInfo
def get_collision_ray_model(ray: Ray, model: ModelPtr) -> RayHitInfo:
    """Get collision info between ray and model"""
    return _rl.GetCollisionRayModel(ray, model)


_rl.GetCollisionRayTriangle.argtypes = [Ray, Vector3, Vector3, Vector3]
_rl.GetCollisionRayTriangle.restype = RayHitInfo
def get_collision_ray_triangle(ray: Ray, p1: Union[Vector3, Seq], p2: Union[Vector3, Seq], p3: Union[Vector3, Seq]) -> RayHitInfo:
    """Get collision info between ray and triangle"""
    return _rl.GetCollisionRayTriangle(ray, _vec3(p1), _vec3(p2), _vec3(p3))


_rl.GetCollisionRayGround.argtypes = [Ray, Float]
_rl.GetCollisionRayGround.restype = RayHitInfo
def get_collision_ray_ground(ray: Ray, ground_height: float) -> RayHitInfo:
    """Get collision info between ray and ground plane (Y-normal plane)"""
    return _rl.GetCollisionRayGround(ray, _float(ground_height))


# -----------------------------------------------------------------------------------
# Shaders System Functions (Module: rlgl)
# NOTE: This functions are useless when using OpenGL 1.1
# -----------------------------------------------------------------------------------

# Shader loading/unloading functions
_rl.LoadText.argtypes = [CharPtr]
_rl.LoadText.restype = CharPtr
def load_text(file_name: AnyStr) -> str:
    """Load bytes array from text file"""
    return _str_in(_rl.LoadText(_str_in(file_name)))


_rl.LoadShader.argtypes = [CharPtr, CharPtr]
_rl.LoadShader.restype = Shader
def load_shader(vs_file_name: AnyStr, fs_filen_name: AnyStr) -> Shader:
    """Load shader from files and bind default locations"""
    return _rl.LoadShader(_str_in(vs_file_name), _str_in(fs_filen_name))


_rl.LoadShaderCode.argtypes = [CharPtr, CharPtr]
_rl.LoadShaderCode.restype = Shader
def load_shader_code(vs_code: AnyStr, fs_code: AnyStr) -> Shader:
    """Load shader from code strings and bind default locations"""
    return _rl.LoadShaderCode(_str_in(vs_code), _str_in(fs_code))


_rl.UnloadShader.argtypes = [Shader]
_rl.UnloadShader.restype = None
def unload_shader(shader: Shader) -> None:
    """Unload shader from GPU memory (VRAM)"""
    return _rl.UnloadShader(shader)


_rl.GetShaderDefault.argtypes = _NOARGS
_rl.GetShaderDefault.restype = Shader
def get_shader_default() -> Shader:
    """Get default shader"""
    return _rl.GetShaderDefault()


_rl.GetTextureDefault.argtypes = _NOARGS
_rl.GetTextureDefault.restype = Texture2D
def get_texture_default() -> Texture2D:
    """Get default texture"""
    return _rl.GetTextureDefault()


# Shader configuration functions
_rl.GetShaderLocation.argtypes = [Shader, CharPtr]
_rl.GetShaderLocation.restype = Int
def get_shader_location(shader: Shader, uniform_name: AnyStr) -> int:
    """Get shader uniform location"""
    return _rl.GetShaderLocation(shader, _str_in(uniform_name))


_rl.SetShaderValue.argtypes = [Shader, Int, FloatPtr, Int]
_rl.SetShaderValue.restype = None
def set_shader_value(shader: Shader, uniform_loc: int, value: FloatPtr, size: int) -> None:
    """Set shader uniform value (float)"""
    return _rl.SetShaderValue(shader, _int(uniform_loc), value, _int(size))


_rl.SetShaderValuei.argtypes = [Shader, Int, IntPtr, Int]
_rl.SetShaderValuei.restype = None
def set_shader_valuei(shader: Shader, uniform_loc: int, value: IntPtr, size: int) -> None:
    """Set shader uniform value (int)"""
    return _rl.SetShaderValuei(shader, _int(uniform_loc), value, _int(size))


_rl.SetShaderValueMatrix.argtypes = [Shader, Int, Matrix]
_rl.SetShaderValueMatrix.restype = None
def set_shader_value_matrix(shader: Shader, uniform_loc: Int, mat: Matrix) -> None:
    """Set shader uniform value (matrix 4x4)"""
    return _rl.SetShaderValueMatrix(shader, _int(uniform_loc), mat)


_rl.SetMatrixProjection.argtypes = [Matrix]
_rl.SetMatrixProjection.restype = None
def set_matrix_projection(proj: Matrix) -> None:
    """Set a custom projection matrix (replaces internal projection matrix)"""
    return _rl.SetMatrixProjection(proj)


_rl.SetMatrixModelview.argtypes = [Matrix]
_rl.SetMatrixModelview.restype = None
def set_matrix_modelview(view: Matrix) -> None:
    """Set a custom modelview matrix (replaces internal modelview matrix)"""
    return _rl.SetMatrixModelview(view)


_rl.GetMatrixModelview.argtypes = _NOARGS
_rl.GetMatrixModelview.restype = Matrix
def get_matrix_modelview() -> Matrix:
    """Get internal modelview matrix"""
    return _rl.GetMatrixModelview()


# Texture maps generation (PBR)
# NOTE: Required shaders should be provided
_rl.GenTextureCubemap.argtypes = [Shader, Texture2D, Int]
_rl.GenTextureCubemap.restype = Texture2D
def gen_texture_cubemap(shader: Shader, sky_hdr: Texture2D, size: int) -> Texture2D:
    """Generate cubemap texture from HDR texture"""
    return _rl.GenTextureCubemap(shader, sky_hdr, _int(size))


_rl.GenTextureIrradiance.argtypes = [Shader, Texture2D, Int]
_rl.GenTextureIrradiance.restype = Texture2D
def gen_texture_irradiance(shader: Shader, cubemap: Texture2D, size: int) -> Texture2D:
    """Generate irradiance texture using cubemap data"""
    return _rl.GenTextureIrradiance(shader, cubemap, _int(size))


_rl.GenTexturePrefilter.argtypes = [Shader, Texture2D, Int]
_rl.GenTexturePrefilter.restype = Texture2D
def gen_texture_prefilter(shader: Shader, cubemap: Texture2D, size: int) -> Texture2D:
    """Generate prefilter texture using cubemap data"""
    return _rl.GenTexturePrefilter(shader, cubemap, _int(size))


_rl.GenTextureBRDF.argtypes = [Shader, Texture2D, Int]
_rl.GenTextureBRDF.restype = Texture2D
def gen_texture_brdf(shader: Shader, cubemap: Texture2D, size: int) -> Texture2D:
    """Generate BRDF texture using cubemap data"""
    return _rl.GenTextureBRDF(shader, cubemap, _int(size))


# Shading begin/end functions
_rl.BeginShaderMode.argtypes = [Shader]
_rl.BeginShaderMode.restype = None
def begin_shader_mode(shader: Shader) -> None:
    """Begin custom shader drawing"""
    return _rl.BeginShaderMode(shader)


_rl.EndShaderMode.argtypes = _NOARGS
_rl.EndShaderMode.restype = None
def end_shader_mode() -> None:
    """End custom shader drawing (use default shader)"""
    return _rl.EndShaderMode()


_rl.BeginBlendMode.argtypes = [Int]
_rl.BeginBlendMode.restype = None
def begin_blend_mode(mode: Union[int, BlendMode]) -> None:
    """Begin blending mode (alpha, additive, multiplied)"""
    return _rl.BeginBlendMode(_int(mode))


_rl.EndBlendMode.argtypes = _NOARGS
_rl.EndBlendMode.restype = None
def end_blend_mode() -> None:
    """End blending mode (reset to default: alpha blending)"""
    return _rl.EndBlendMode()

if ENABLE_V2_0_0_FEATURE_CLIPRECT:
    _rl.BeginClipRec.argtypes = [Rectangle]
    _rl.BeginClipRec.restype = None
    def begin_clip_rec(rec: Rectangle) -> None:
        """Drawing functions change only pixels inside rec.

        Can be nested.
        """
        _rl.BeginClipRec(_rect(rec))

    _rl.EndClipRec.argtypes = _NOARGS
    _rl.EndClipRec.restype = None
    def end_clip_rec() -> None:
        """Restore previous clip rec."""
        _rl.EndClipRec()
else:
    def begin_clip_rec(rec: Rectangle) -> None:
        """WARNING: THIS FUNCTION HAS NO EFFECT."""
        pass

    def end_clip_rec() -> None:
        """WARNING: THIS FUNCTION HAS NO EFFECT."""
        pass

# VR control functions
_rl.GetVrDeviceInfo.argtypes = [Int]
_rl.GetVrDeviceInfo.restype = VrDeviceInfo
def get_vr_device_info(vr_device_type: Union[int, VrDeviceType]):
    """Get VR device information for some standard devices"""
    return _rl.GetVrDeviceInfo(_int(vr_device_type))


_rl.InitVrSimulator.argtypes = [VrDeviceInfo]
_rl.InitVrSimulator.restype = None
def init_vr_simulator(info: VrDeviceInfo) -> None:
    """Init VR simulator for selected device parameters"""
    return _rl.InitVrSimulator(info)


_rl.CloseVrSimulator.argtypes = _NOARGS
_rl.CloseVrSimulator.restype = None
def close_vr_simulator() -> None:
    """Close VR simulator for current device"""
    return _rl.CloseVrSimulator()


_rl.IsVrSimulatorReady.argtypes = _NOARGS
_rl.IsVrSimulatorReady.restype = bool
def is_vr_simulator_ready():
    """Detect if VR simulator is ready"""
    return _rl.IsVrSimulatorReady()


_rl.SetVrDistortionShader.argtypes = [Shader]
_rl.SetVrDistortionShader.restype = None
def set_vr_distortion_shader(shader: Shader) -> None:
    """Set VR distortion shader for stereoscopic rendering"""
    return _rl.SetVrDistortionShader(shader)


_rl.UpdateVrTracking.argtypes = [CameraPtr]
_rl.UpdateVrTracking.restype = None
def update_vr_tracking(camera: CameraPtr) -> None:
    """Update VR tracking (position and orientation) and camera"""
    return _rl.UpdateVrTracking(camera)


_rl.ToggleVrMode.argtypes = _NOARGS
_rl.ToggleVrMode.restype = None
def toggle_vr_mode() -> None:
    """Enable/Disable VR experience"""
    return _rl.ToggleVrMode()


_rl.BeginVrDrawing.argtypes = _NOARGS
_rl.BeginVrDrawing.restype = None
def begin_vr_drawing() -> None:
    """Begin VR simulator stereo rendering"""
    return _rl.BeginVrDrawing()


_rl.EndVrDrawing.argtypes = _NOARGS
_rl.EndVrDrawing.restype = None
def end_vr_drawing() -> None:
    """End VR simulator stereo rendering"""
    return _rl.EndVrDrawing()


# -----------------------------------------------------------------------------------
# Audio Loading and Playing Functions (Module: audio)
# -----------------------------------------------------------------------------------

# Audio device management functions
_rl.InitAudioDevice.argtypes = _NOARGS
_rl.InitAudioDevice.restype = None
def init_audio_device() -> None:
    """Initialize audio device and context"""
    return _rl.InitAudioDevice()


_rl.CloseAudioDevice.argtypes = _NOARGS
_rl.CloseAudioDevice.restype = None
def close_audio_device() -> None:
    """Close the audio device and context"""
    return _rl.CloseAudioDevice()


_rl.IsAudioDeviceReady.argtypes = _NOARGS
_rl.IsAudioDeviceReady.restype = Bool
def is_audio_device_ready():
    """Check if audio device has been initialized successfully"""
    return _rl.IsAudioDeviceReady()


_rl.SetMasterVolume.argtypes = [Float]
_rl.SetMasterVolume.restype = None
def set_master_volume(volume: float) -> None:
    """Set master volume (listener)"""
    return _rl.SetMasterVolume(_float(volume))


# Wave/Sound loading/unloading functions
_rl.LoadWave.argtypes = [CharPtr]
_rl.LoadWave.restype = Wave
def load_wave(file_name: CharPtr) -> Wave:
    """Load wave data from file"""
    return _rl.LoadWave(_str_in(file_name))

_rl.LoadWaveEx.argtypes = [VoidPtr, Int, Int, Int, Int]
_rl.LoadWaveEx.restype = Wave
def load_wave_ex(data: VoidPtr, sample_count: int, sample_rate: int, sample_size: int, channels: int) -> Wave:
    """Load wave data from raw array data"""
    return _rl.LoadWaveEx(data, _int(sample_count), _int(sample_rate), _int(sample_size), _int(channels))


_rl.LoadSound.argtypes = [CharPtr]
_rl.LoadSound.restype = Sound
def load_sound(file_name: CharPtr) -> Sound:
    """Load sound from file"""
    return _rl.LoadSound(_str_in(file_name))


_rl.LoadSoundFromWave.argtypes = [Wave]
_rl.LoadSoundFromWave.restype = Sound
def load_sound_from_wave(wave: Wave) -> Sound:
    """Load sound from wave data"""
    return _rl.LoadSoundFromWave(wave)


_rl.UpdateSound.argtypes = [Sound, VoidPtr, Int]
_rl.UpdateSound.restype = None
def update_sound(sound: Sound, data: VoidPtr, samples_count: int) -> None:
    """Update sound buffer with new data"""
    return _rl.UpdateSound(sound, data, _int(samples_count))


_rl.UnloadWave.argtypes = [Wave]
_rl.UnloadWave.restype = None
def unload_wave(wave: Wave) -> None:
    """Unload wave data"""
    return _rl.UnloadWave(wave)


_rl.UnloadSound.argtypes = [Sound]
_rl.UnloadSound.restype = None
def unload_sound(sound: Sound) -> None:
    """Unload sound"""
    return _rl.UnloadSound(sound)


# Wave/Sound management functions
_rl.PlaySound.argtypes = [Sound]
_rl.PlaySound.restype = None
def play_sound(sound: Sound) -> None:
    """Play a sound"""
    return _rl.PlaySound(sound)


_rl.PauseSound.argtypes = [Sound]
_rl.PauseSound.restype = None
def pause_sound(sound: Sound) -> None:
    """Pause a sound"""
    return _rl.PauseSound(sound)


_rl.ResumeSound.argtypes = [Sound]
_rl.ResumeSound.restype = None
def resume_sound(sound: Sound) -> None:
    """Resume a paused sound"""
    return _rl.ResumeSound(sound)


_rl.StopSound.argtypes = [Sound]
_rl.StopSound.restype = None
def stop_sound(sound: Sound) -> None:
    """Stop playing a sound"""
    return _rl.StopSound(sound)


_rl.IsSoundPlaying.argtypes = [Sound]
_rl.IsSoundPlaying.restype = Bool
def is_sound_playing(sound: Sound) -> bool:
    """Check if a sound is currently playing"""
    return _rl.IsSoundPlaying(sound)


_rl.SetSoundVolume.argtypes = [Sound, Float]
_rl.SetSoundVolume.restype = None
def set_sound_volume(sound: Sound, volume: float) -> None:
    """Set volume for a sound (1.0 is max level)"""
    return _rl.SetSoundVolume(sound, _float(volume))


_rl.SetSoundPitch.argtypes = [Sound, Float]
_rl.SetSoundPitch.restype = None
def set_sound_pitch(sound: Sound, pitch: float) -> None:
    """Set pitch for a sound (1.0 is base level)"""
    return _rl.SetSoundPitch(sound, _float(pitch))


_rl.WaveFormat.argtypes = [WavePtr, Int, Int, Int]
_rl.WaveFormat.restype = None
def wave_format(wave: WavePtr, sample_rate: int, sample_size: int, channels: int) -> None:
    """Convert wave data to desired format"""
    return _rl.WaveFormat(wave, _int(sample_rate), _int(sample_size), _int(channels))


_rl.WaveCopy.argtypes = [Wave]
_rl.WaveCopy.restype = Wave
def wave_copy(wave: Wave) -> Wave:
    """Copy a wave to a new wave"""
    return _rl.WaveCopy(wave)


_rl.WaveCrop.argtypes = [WavePtr, Int, Int]
_rl.WaveCrop.restype = None
def wave_crop(wave: WavePtr, init_sample: int, final_sample: int) -> None:
    """Crop a wave to defined samples range"""
    return _rl.WaveCrop(wave, _int(init_sample), _int(final_sample))


_rl.GetWaveData.argtypes = [Wave]
_rl.GetWaveData.restype = FloatPtr
def get_wave_data(wave: Wave) -> FloatPtr:
    """Get samples data from wave as a floats array"""
    return _rl.GetWaveData(wave)


# Music management functions
_rl.LoadMusicStream.argtypes = [CharPtr]
_rl.LoadMusicStream.restype = Music
def load_music_stream(file_name: CharPtr) -> Music:
    """Load music stream from file"""
    return _rl.LoadMusicStream(_str_in(file_name))


_rl.UnloadMusicStream.argtypes = [Music]
_rl.UnloadMusicStream.restype = None
def unload_music_stream(music: Music) -> None:
    """Unload music stream"""
    return _rl.UnloadMusicStream(music)


_rl.PlayMusicStream.argtypes = [Music]
_rl.PlayMusicStream.restype = None
def play_music_stream(music: Music) -> None:
    """Start music playing"""
    return _rl.PlayMusicStream(music)


_rl.UpdateMusicStream.argtypes = [Music]
_rl.UpdateMusicStream.restype = None
def update_music_stream(music: Music) -> None:
    """Updates buffers for music streaming"""
    return _rl.UpdateMusicStream(music)


_rl.StopMusicStream.argtypes = [Music]
_rl.StopMusicStream.restype = None
def stop_music_stream(music: Music) -> None:
    """Stop music playing"""
    return _rl.StopMusicStream(music)


_rl.PauseMusicStream.argtypes = [Music]
_rl.PauseMusicStream.restype = None
def pause_music_stream(music: Music) -> None:
    """Pause music playing"""
    return _rl.PauseMusicStream(music)


_rl.ResumeMusicStream.argtypes = [Music]
_rl.ResumeMusicStream.restype = None
def resume_music_stream(music: Music) -> None:
    """Resume playing paused music"""
    return _rl.ResumeMusicStream(music)


_rl.IsMusicPlaying.argtypes = [Music]
_rl.IsMusicPlaying.restype = Bool
def is_music_playing(music: Music):
    """Check if music is playing"""
    return _rl.IsMusicPlaying(music)


_rl.SetMusicVolume.argtypes = [Music, Float]
_rl.SetMusicVolume.restype = None
def set_music_volume(music: Music, volume: float) -> None:
    """Set volume for music (1.0 is max level)"""
    return _rl.SetMusicVolume(music, _float(volume))


_rl.SetMusicPitch.argtypes = [Music, Float]
_rl.SetMusicPitch.restype = None
def set_music_pitch(music: Music, pitch: float) -> None:
    """Set pitch for a music (1.0 is base level)"""
    return _rl.SetMusicPitch(music, _float(pitch))


_rl.SetMusicLoopCount.argtypes = [Music, Int]
_rl.SetMusicLoopCount.restype = None
def set_music_loop_count(music: Music, count: int) -> None:
    """Set music loop count (loop repeats)"""
    return _rl.SetMusicLoopCount(music, _int(count))


_rl.GetMusicTimeLength.argtypes = [Music]
_rl.GetMusicTimeLength.restype = Float
def get_music_time_length(music: Music) -> float:
    """Get music time length (in seconds)"""
    return _rl.GetMusicTimeLength(music)


_rl.GetMusicTimePlayed.argtypes = [Music]
_rl.GetMusicTimePlayed.restype = Float
def get_music_time_played(music: Music) -> float:
    """Get current music time played (in seconds)"""
    return _rl.GetMusicTimePlayed(music)


# AudioStream management functions
_rl.InitAudioStream.argtypes = [UInt, UInt, UInt]
_rl.InitAudioStream.restype = AudioStream
def init_audio_stream(sample_rate: int, sample_size: int, channels: int) -> AudioStream:
    """Init audio stream (to stream raw audio pcm data)"""
    return _rl.InitAudioStream(_int(sample_rate), _int(sample_size), _int(channels))


_rl.UpdateAudioStream.argtypes = [AudioStream, VoidPtr, Int]
_rl.UpdateAudioStream.restype = None
def update_audio_stream(stream: AudioStream, data: VoidPtr, samples_count: int) -> None:
    """Update audio stream buffers with data"""
    return _rl.UpdateAudioStream(stream, data, _int(samples_count))


_rl.CloseAudioStream.argtypes = [AudioStream]
_rl.CloseAudioStream.restype = None
def close_audio_stream(stream: AudioStream) -> None:
    """Close audio stream and free memory"""
    return _rl.CloseAudioStream(stream)


_rl.IsAudioBufferProcessed.argtypes = [AudioStream]
_rl.IsAudioBufferProcessed.restype = Bool
def is_audio_buffer_processed(stream: AudioStream) -> bool:
    """Check if any audio stream buffers requires refill"""
    return _rl.IsAudioBufferProcessed(stream)


_rl.PlayAudioStream.argtypes = [AudioStream]
_rl.PlayAudioStream.restype = None
def play_audio_stream(stream: AudioStream) -> None:
    """Play audio stream"""
    return _rl.PlayAudioStream(stream)


_rl.PauseAudioStream.argtypes = [AudioStream]
_rl.PauseAudioStream.restype = None
def pause_audio_stream(stream: AudioStream) -> None:
    """Pause audio stream"""
    return _rl.PauseAudioStream(stream)


_rl.ResumeAudioStream.argtypes = [AudioStream]
_rl.ResumeAudioStream.restype = None
def resume_audio_stream(stream: AudioStream) -> None:
    """Resume audio stream"""
    return _rl.ResumeAudioStream(stream)


_rl.IsAudioStreamPlaying.argtypes = [AudioStream]
_rl.IsAudioStreamPlaying.restype = Bool
def is_audio_stream_playing(stream: AudioStream) -> bool:
    """Check if audio stream is playing"""
    return _rl.IsAudioStreamPlaying(stream)


_rl.StopAudioStream.argtypes = [AudioStream]
_rl.StopAudioStream.restype = None
def stop_audio_stream(stream: AudioStream) -> None:
    """Stop audio stream"""
    return _rl.StopAudioStream(stream)


_rl.SetAudioStreamVolume.argtypes = [AudioStream, Float]
_rl.SetAudioStreamVolume.restype = None
def set_audio_stream_volume(stream: AudioStream, volume: float) -> None:
    """Set volume for audio stream (1.0 is max level)"""
    return _rl.SetAudioStreamVolume(stream, _float(volume))


_rl.SetAudioStreamPitch.argtypes = [AudioStream, Float]
_rl.SetAudioStreamPitch.restype = None
def set_audio_stream_pitch(stream: AudioStream, pitch: float) -> None:
    """Set pitch for audio stream (1.0 is base level)"""
    return _rl.SetAudioStreamPitch(stream, _float(pitch))

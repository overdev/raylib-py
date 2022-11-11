
import sys
import re
import os
import platform
import ctypes
from enum import IntEnum
from contextlib import contextmanager
from typing import Optional as Opt, Any, Sequence as Seq, Union
from ctypes import (
    CDLL, wintypes,
    c_bool, c_char, c_byte, c_short, c_long, c_longlong, c_ubyte, c_ushort, c_ulong, c_ulonglong, c_float, c_double, c_char_p, c_void_p,
    Structure, POINTER, CFUNCTYPE, byref, cast
) 


__all__ = [
    'rlapi',
    'Bool',
    'BoolPtr',
    'Byte',
    'BytePtr',
    'Char',
    'CharPtr',
    'Short',
    'ShortPtr',
    'Int',
    'IntPtr',
    'Long',
    'LongPtr',
    'UByte',
    'UBytePtr',
    'UShort',
    'UShortPtr',
    'UInt',
    'UIntPtr',
    'ULong',
    'ULongPtr',
    'Float',
    'FloatPtr',
    'Double',
    'DoublePtr',
    'VoidPtr',
    'VoidPtrPtr',

    'Vector2',
    'Vector3',
    'Vector4',
    'Matrix',
    'Color',
    'Rectangle',
    'Image',
    'Texture',
    'RenderTexture',
    'NPatchInfo',
    'GlyphInfo',
    'Font',
    'Camera3D',
    'Camera2D',
    'Mesh',
    'Shader',
    'MaterialMap',
    'Material',
    'Transform',
    'BoneInfo',
    'Model',
    'ModelAnimation',
    'Ray',
    'RayCollision',
    'BoundingBox',
    'Wave',
    'AudioStream',
    'Sound',
    'Music',
    'VrDeviceInfo',
    'VrStereoConfig',
    'FilePathList',
    'RAYLIB_VERSION',
    'PI',
    'DEG2RAD',
    'RAD2DEG',
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
    'Quaternion',
    'Texture2D',
    'TextureCubemap',
    'RenderTexture2D',
    'Camera',
    'ConfigFlags',
    'FLAG_VSYNC_HINT',
    'FLAG_FULLSCREEN_MODE',
    'FLAG_WINDOW_RESIZABLE',
    'FLAG_WINDOW_UNDECORATED',
    'FLAG_WINDOW_HIDDEN',
    'FLAG_WINDOW_MINIMIZED',
    'FLAG_WINDOW_MAXIMIZED',
    'FLAG_WINDOW_UNFOCUSED',
    'FLAG_WINDOW_TOPMOST',
    'FLAG_WINDOW_ALWAYS_RUN',
    'FLAG_WINDOW_TRANSPARENT',
    'FLAG_WINDOW_HIGHDPI',
    'FLAG_WINDOW_MOUSE_PASSTHROUGH',
    'FLAG_MSAA_4X_HINT',
    'FLAG_INTERLACED_HINT',
    'TraceLogLevel',
    'LOG_ALL',
    'LOG_TRACE',
    'LOG_DEBUG',
    'LOG_INFO',
    'LOG_WARNING',
    'LOG_ERROR',
    'LOG_FATAL',
    'LOG_NONE',
    'KeyboardKey',
    'KEY_NULL',
    'KEY_APOSTROPHE',
    'KEY_COMMA',
    'KEY_MINUS',
    'KEY_PERIOD',
    'KEY_SLASH',
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
    'KEY_SEMICOLON',
    'KEY_EQUAL',
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
    'KEY_LEFT_BRACKET',
    'KEY_BACKSLASH',
    'KEY_RIGHT_BRACKET',
    'KEY_GRAVE',
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
    'KEY_LEFT_SUPER',
    'KEY_RIGHT_SHIFT',
    'KEY_RIGHT_CONTROL',
    'KEY_RIGHT_ALT',
    'KEY_RIGHT_SUPER',
    'KEY_KB_MENU',
    'KEY_KP_0',
    'KEY_KP_1',
    'KEY_KP_2',
    'KEY_KP_3',
    'KEY_KP_4',
    'KEY_KP_5',
    'KEY_KP_6',
    'KEY_KP_7',
    'KEY_KP_8',
    'KEY_KP_9',
    'KEY_KP_DECIMAL',
    'KEY_KP_DIVIDE',
    'KEY_KP_MULTIPLY',
    'KEY_KP_SUBTRACT',
    'KEY_KP_ADD',
    'KEY_KP_ENTER',
    'KEY_KP_EQUAL',
    'KEY_BACK',
    'KEY_MENU',
    'KEY_VOLUME_UP',
    'KEY_VOLUME_DOWN',
    'MouseButton',
    'MOUSE_BUTTON_LEFT',
    'MOUSE_BUTTON_RIGHT',
    'MOUSE_BUTTON_MIDDLE',
    'MOUSE_BUTTON_SIDE',
    'MOUSE_BUTTON_EXTRA',
    'MOUSE_BUTTON_FORWARD',
    'MOUSE_BUTTON_BACK',
    'MouseCursor',
    'MOUSE_CURSOR_DEFAULT',
    'MOUSE_CURSOR_ARROW',
    'MOUSE_CURSOR_IBEAM',
    'MOUSE_CURSOR_CROSSHAIR',
    'MOUSE_CURSOR_POINTING_HAND',
    'MOUSE_CURSOR_RESIZE_EW',
    'MOUSE_CURSOR_RESIZE_NS',
    'MOUSE_CURSOR_RESIZE_NWSE',
    'MOUSE_CURSOR_RESIZE_NESW',
    'MOUSE_CURSOR_RESIZE_ALL',
    'MOUSE_CURSOR_NOT_ALLOWED',
    'GamepadButton',
    'GAMEPAD_BUTTON_UNKNOWN',
    'GAMEPAD_BUTTON_LEFT_FACE_UP',
    'GAMEPAD_BUTTON_LEFT_FACE_RIGHT',
    'GAMEPAD_BUTTON_LEFT_FACE_DOWN',
    'GAMEPAD_BUTTON_LEFT_FACE_LEFT',
    'GAMEPAD_BUTTON_RIGHT_FACE_UP',
    'GAMEPAD_BUTTON_RIGHT_FACE_RIGHT',
    'GAMEPAD_BUTTON_RIGHT_FACE_DOWN',
    'GAMEPAD_BUTTON_RIGHT_FACE_LEFT',
    'GAMEPAD_BUTTON_LEFT_TRIGGER_1',
    'GAMEPAD_BUTTON_LEFT_TRIGGER_2',
    'GAMEPAD_BUTTON_RIGHT_TRIGGER_1',
    'GAMEPAD_BUTTON_RIGHT_TRIGGER_2',
    'GAMEPAD_BUTTON_MIDDLE_LEFT',
    'GAMEPAD_BUTTON_MIDDLE',
    'GAMEPAD_BUTTON_MIDDLE_RIGHT',
    'GAMEPAD_BUTTON_LEFT_THUMB',
    'GAMEPAD_BUTTON_RIGHT_THUMB',
    'GamepadAxis',
    'GAMEPAD_AXIS_LEFT_X',
    'GAMEPAD_AXIS_LEFT_Y',
    'GAMEPAD_AXIS_RIGHT_X',
    'GAMEPAD_AXIS_RIGHT_Y',
    'GAMEPAD_AXIS_LEFT_TRIGGER',
    'GAMEPAD_AXIS_RIGHT_TRIGGER',
    'MaterialMapIndex',
    'MATERIAL_MAP_ALBEDO',
    'MATERIAL_MAP_METALNESS',
    'MATERIAL_MAP_NORMAL',
    'MATERIAL_MAP_ROUGHNESS',
    'MATERIAL_MAP_OCCLUSION',
    'MATERIAL_MAP_EMISSION',
    'MATERIAL_MAP_HEIGHT',
    'MATERIAL_MAP_CUBEMAP',
    'MATERIAL_MAP_IRRADIANCE',
    'MATERIAL_MAP_PREFILTER',
    'MATERIAL_MAP_BRDF',
    'ShaderLocationIndex',
    'SHADER_LOC_VERTEX_POSITION',
    'SHADER_LOC_VERTEX_TEXCOORD01',
    'SHADER_LOC_VERTEX_TEXCOORD02',
    'SHADER_LOC_VERTEX_NORMAL',
    'SHADER_LOC_VERTEX_TANGENT',
    'SHADER_LOC_VERTEX_COLOR',
    'SHADER_LOC_MATRIX_MVP',
    'SHADER_LOC_MATRIX_VIEW',
    'SHADER_LOC_MATRIX_PROJECTION',
    'SHADER_LOC_MATRIX_MODEL',
    'SHADER_LOC_MATRIX_NORMAL',
    'SHADER_LOC_VECTOR_VIEW',
    'SHADER_LOC_COLOR_DIFFUSE',
    'SHADER_LOC_COLOR_SPECULAR',
    'SHADER_LOC_COLOR_AMBIENT',
    'SHADER_LOC_MAP_ALBEDO',
    'SHADER_LOC_MAP_METALNESS',
    'SHADER_LOC_MAP_NORMAL',
    'SHADER_LOC_MAP_ROUGHNESS',
    'SHADER_LOC_MAP_OCCLUSION',
    'SHADER_LOC_MAP_EMISSION',
    'SHADER_LOC_MAP_HEIGHT',
    'SHADER_LOC_MAP_CUBEMAP',
    'SHADER_LOC_MAP_IRRADIANCE',
    'SHADER_LOC_MAP_PREFILTER',
    'SHADER_LOC_MAP_BRDF',
    'ShaderUniformDataType',
    'SHADER_UNIFORM_FLOAT',
    'SHADER_UNIFORM_VEC2',
    'SHADER_UNIFORM_VEC3',
    'SHADER_UNIFORM_VEC4',
    'SHADER_UNIFORM_INT',
    'SHADER_UNIFORM_IVEC2',
    'SHADER_UNIFORM_IVEC3',
    'SHADER_UNIFORM_IVEC4',
    'SHADER_UNIFORM_SAMPLER2D',
    'ShaderAttributeDataType',
    'SHADER_ATTRIB_FLOAT',
    'SHADER_ATTRIB_VEC2',
    'SHADER_ATTRIB_VEC3',
    'SHADER_ATTRIB_VEC4',
    'PixelFormat',
    'PIXELFORMAT_UNCOMPRESSED_GRAYSCALE',
    'PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA',
    'PIXELFORMAT_UNCOMPRESSED_R5G6B5',
    'PIXELFORMAT_UNCOMPRESSED_R8G8B8',
    'PIXELFORMAT_UNCOMPRESSED_R5G5B5A1',
    'PIXELFORMAT_UNCOMPRESSED_R4G4B4A4',
    'PIXELFORMAT_UNCOMPRESSED_R8G8B8A8',
    'PIXELFORMAT_UNCOMPRESSED_R32',
    'PIXELFORMAT_UNCOMPRESSED_R32G32B32',
    'PIXELFORMAT_UNCOMPRESSED_R32G32B32A32',
    'PIXELFORMAT_COMPRESSED_DXT1_RGB',
    'PIXELFORMAT_COMPRESSED_DXT1_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT3_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT5_RGBA',
    'PIXELFORMAT_COMPRESSED_ETC1_RGB',
    'PIXELFORMAT_COMPRESSED_ETC2_RGB',
    'PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA',
    'PIXELFORMAT_COMPRESSED_PVRT_RGB',
    'PIXELFORMAT_COMPRESSED_PVRT_RGBA',
    'PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA',
    'PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA',
    'TextureFilter',
    'TEXTURE_FILTER_POINT',
    'TEXTURE_FILTER_BILINEAR',
    'TEXTURE_FILTER_TRILINEAR',
    'TEXTURE_FILTER_ANISOTROPIC_4X',
    'TEXTURE_FILTER_ANISOTROPIC_8X',
    'TEXTURE_FILTER_ANISOTROPIC_16X',
    'TextureWrap',
    'TEXTURE_WRAP_REPEAT',
    'TEXTURE_WRAP_CLAMP',
    'TEXTURE_WRAP_MIRROR_REPEAT',
    'TEXTURE_WRAP_MIRROR_CLAMP',
    'CubemapLayout',
    'CUBEMAP_LAYOUT_AUTO_DETECT',
    'CUBEMAP_LAYOUT_LINE_VERTICAL',
    'CUBEMAP_LAYOUT_LINE_HORIZONTAL',
    'CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR',
    'CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE',
    'CUBEMAP_LAYOUT_PANORAMA',
    'FontType',
    'FONT_DEFAULT',
    'FONT_BITMAP',
    'FONT_SDF',
    'BlendMode',
    'BLEND_ALPHA',
    'BLEND_ADDITIVE',
    'BLEND_MULTIPLIED',
    'BLEND_ADD_COLORS',
    'BLEND_SUBTRACT_COLORS',
    'BLEND_ALPHA_PREMULTIPLY',
    'BLEND_CUSTOM',
    'Gesture',
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
    'CameraProjection',
    'CAMERA_PERSPECTIVE',
    'CAMERA_ORTHOGRAPHIC',
    'NPatchLayout',
    'NPATCH_NINE_PATCH',
    'NPATCH_THREE_PATCH_VERTICAL',
    'NPATCH_THREE_PATCH_HORIZONTAL',
    'TraceLogCallback',
    'LoadFileDataCallback',
    'SaveFileDataCallback',
    'LoadFileTextCallback',
    'SaveFileTextCallback',
    'AudioCallback',
    'init_window',
    'window_should_close',
    'close_window',
    'is_window_ready',
    'is_window_fullscreen',
    'is_window_hidden',
    'is_window_minimized',
    'is_window_maximized',
    'is_window_focused',
    'is_window_resized',
    'is_window_state',
    'set_window_state',
    'clear_window_state',
    'toggle_fullscreen',
    'maximize_window',
    'minimize_window',
    'restore_window',
    'set_window_icon',
    'set_window_title',
    'set_window_position',
    'set_window_monitor',
    'set_window_min_size',
    'set_window_size',
    'set_window_opacity',
    'get_window_handle',
    'get_screen_width',
    'get_screen_height',
    'get_render_width',
    'get_render_height',
    'get_monitor_count',
    'get_current_monitor',
    'get_monitor_position',
    'get_monitor_width',
    'get_monitor_height',
    'get_monitor_physical_width',
    'get_monitor_physical_height',
    'get_monitor_refresh_rate',
    'get_window_position',
    'get_window_scale_dpi',
    'get_monitor_name',
    'set_clipboard_text',
    'get_clipboard_text',
    'enable_event_waiting',
    'disable_event_waiting',
    'swap_screen_buffer',
    'poll_input_events',
    'wait_time',
    'show_cursor',
    'hide_cursor',
    'is_cursor_hidden',
    'enable_cursor',
    'disable_cursor',
    'is_cursor_on_screen',
    'clear_background',
    'begin_drawing',
    'end_drawing',
    'begin_mode2d',
    'end_mode2d',
    'begin_mode3d',
    'end_mode3d',
    'begin_texture_mode',
    'end_texture_mode',
    'begin_shader_mode',
    'end_shader_mode',
    'begin_blend_mode',
    'end_blend_mode',
    'begin_scissor_mode',
    'end_scissor_mode',
    'begin_vr_stereo_mode',
    'end_vr_stereo_mode',
    'load_vr_stereo_config',
    'unload_vr_stereo_config',
    'load_shader',
    'load_shader_from_memory',
    'get_shader_location',
    'get_shader_location_attrib',
    'set_shader_value',
    'set_shader_value_v',
    'set_shader_value_matrix',
    'set_shader_value_texture',
    'unload_shader',
    'get_mouse_ray',
    'get_camera_matrix',
    'get_camera_matrix2d',
    'get_world_to_screen',
    'get_screen_to_world2d',
    'get_world_to_screen_ex',
    'get_world_to_screen2d',
    'set_target_fps',
    'get_fps',
    'get_frame_time',
    'get_time',
    'get_random_value',
    'set_random_seed',
    'take_screenshot',
    'set_config_flags',
    'trace_log',
    'set_trace_log_level',
    'mem_alloc',
    'mem_realloc',
    'mem_free',
    'open_url',
    'set_trace_log_callback',
    'set_load_file_data_callback',
    'set_save_file_data_callback',
    'set_load_file_text_callback',
    'set_save_file_text_callback',
    'load_file_data',
    'unload_file_data',
    'save_file_data',
    'export_data_as_code',
    'load_file_text',
    'unload_file_text',
    'save_file_text',
    'file_exists',
    'directory_exists',
    'is_file_extension',
    'get_file_length',
    'get_file_extension',
    'get_file_name',
    'get_file_name_without_ext',
    'get_directory_path',
    'get_prev_directory_path',
    'get_working_directory',
    'get_application_directory',
    'change_directory',
    'is_path_file',
    'load_directory_files',
    'load_directory_files_ex',
    'unload_directory_files',
    'is_file_dropped',
    'load_dropped_files',
    'unload_dropped_files',
    'get_file_mod_time',
    'compress_data',
    'decompress_data',
    'encode_data_base64',
    'decode_data_base64',
    'is_key_pressed',
    'is_key_down',
    'is_key_released',
    'is_key_up',
    'set_exit_key',
    'get_key_pressed',
    'get_char_pressed',
    'is_gamepad_available',
    'get_gamepad_name',
    'is_gamepad_button_pressed',
    'is_gamepad_button_down',
    'is_gamepad_button_released',
    'is_gamepad_button_up',
    'get_gamepad_button_pressed',
    'get_gamepad_axis_count',
    'get_gamepad_axis_movement',
    'set_gamepad_mappings',
    'is_mouse_button_pressed',
    'is_mouse_button_down',
    'is_mouse_button_released',
    'is_mouse_button_up',
    'get_mouse_x',
    'get_mouse_y',
    'get_mouse_position',
    'get_mouse_delta',
    'set_mouse_position',
    'set_mouse_offset',
    'set_mouse_scale',
    'get_mouse_wheel_move',
    'get_mouse_wheel_move_v',
    'set_mouse_cursor',
    'get_touch_x',
    'get_touch_y',
    'get_touch_position',
    'get_touch_point_id',
    'get_touch_point_count',
    'set_gestures_enabled',
    'is_gesture_detected',
    'get_gesture_detected',
    'get_gesture_hold_duration',
    'get_gesture_drag_vector',
    'get_gesture_drag_angle',
    'get_gesture_pinch_vector',
    'get_gesture_pinch_angle',
    'set_camera_mode',
    'update_camera',
    'set_camera_pan_control',
    'set_camera_alt_control',
    'set_camera_smooth_zoom_control',
    'set_camera_move_controls',
    'set_shapes_texture',
    'draw_pixel',
    'draw_pixel_v',
    'draw_line',
    'draw_line_v',
    'draw_line_ex',
    'draw_line_bezier',
    'draw_line_bezier_quad',
    'draw_line_bezier_cubic',
    'draw_line_strip',
    'draw_circle',
    'draw_circle_sector',
    'draw_circle_sector_lines',
    'draw_circle_gradient',
    'draw_circle_v',
    'draw_circle_lines',
    'draw_ellipse',
    'draw_ellipse_lines',
    'draw_ring',
    'draw_ring_lines',
    'draw_rectangle',
    'draw_rectangle_v',
    'draw_rectangle_rec',
    'draw_rectangle_pro',
    'draw_rectangle_gradient_v',
    'draw_rectangle_gradient_h',
    'draw_rectangle_gradient_ex',
    'draw_rectangle_lines',
    'draw_rectangle_lines_ex',
    'draw_rectangle_rounded',
    'draw_rectangle_rounded_lines',
    'draw_triangle',
    'draw_triangle_lines',
    'draw_triangle_fan',
    'draw_triangle_strip',
    'draw_poly',
    'draw_poly_lines',
    'draw_poly_lines_ex',
    'check_collision_recs',
    'check_collision_circles',
    'check_collision_circle_rec',
    'check_collision_point_rec',
    'check_collision_point_circle',
    'check_collision_point_triangle',
    'check_collision_lines',
    'check_collision_point_line',
    'get_collision_rec',
    'load_image',
    'load_image_raw',
    'load_image_anim',
    'load_image_from_memory',
    'load_image_from_texture',
    'load_image_from_screen',
    'unload_image',
    'export_image',
    'export_image_as_code',
    'gen_image_color',
    'gen_image_gradient_v',
    'gen_image_gradient_h',
    'gen_image_gradient_radial',
    'gen_image_checked',
    'gen_image_white_noise',
    'gen_image_cellular',
    'image_copy',
    'image_from_image',
    'image_text',
    'image_text_ex',
    'image_format',
    'image_to_pot',
    'image_crop',
    'image_alpha_crop',
    'image_alpha_clear',
    'image_alpha_mask',
    'image_alpha_premultiply',
    'image_resize',
    'image_resize_nn',
    'image_resize_canvas',
    'image_mipmaps',
    'image_dither',
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
    'load_image_colors',
    'load_image_palette',
    'unload_image_colors',
    'unload_image_palette',
    'get_image_alpha_border',
    'get_image_color',
    'image_clear_background',
    'image_draw_pixel',
    'image_draw_pixel_v',
    'image_draw_line',
    'image_draw_line_v',
    'image_draw_circle',
    'image_draw_circle_v',
    'image_draw_rectangle',
    'image_draw_rectangle_v',
    'image_draw_rectangle_rec',
    'image_draw_rectangle_lines',
    'image_draw',
    'image_draw_text',
    'image_draw_text_ex',
    'load_texture',
    'load_texture_from_image',
    'load_texture_cubemap',
    'load_render_texture',
    'unload_texture',
    'unload_render_texture',
    'update_texture',
    'update_texture_rec',
    'gen_texture_mipmaps',
    'set_texture_filter',
    'set_texture_wrap',
    'draw_texture',
    'draw_texture_v',
    'draw_texture_ex',
    'draw_texture_rec',
    'draw_texture_quad',
    'draw_texture_tiled',
    'draw_texture_pro',
    'draw_texture_npatch',
    'draw_texture_poly',
    'fade',
    'color_to_int',
    'color_normalize',
    'color_from_normalized',
    'color_to_hsv',
    'color_from_hsv',
    'color_alpha',
    'color_alpha_blend',
    'get_color',
    'get_pixel_color',
    'set_pixel_color',
    'get_pixel_data_size',
    'get_font_default',
    'load_font',
    'load_font_ex',
    'load_font_from_image',
    'load_font_from_memory',
    'load_font_data',
    'gen_image_font_atlas',
    'unload_font_data',
    'unload_font',
    'export_font_as_code',
    'draw_fps',
    'draw_text',
    'draw_text_ex',
    'draw_text_pro',
    'draw_text_codepoint',
    'draw_text_codepoints',
    'measure_text',
    'measure_text_ex',
    'get_glyph_index',
    'get_glyph_info',
    'get_glyph_atlas_rec',
    'load_codepoints',
    'unload_codepoints',
    'get_codepoint_count',
    'get_codepoint',
    'codepoint_to_utf8',
    'text_codepoints_to_utf8',
    'text_copy',
    'text_is_equal',
    'text_length',
    'text_format',
    'text_subtext',
    'text_replace',
    'text_insert',
    'text_join',
    'text_split',
    'text_append',
    'text_find_index',
    'text_to_upper',
    'text_to_lower',
    'text_to_pascal',
    'text_to_integer',
    'draw_line3d',
    'draw_point3d',
    'draw_circle3d',
    'draw_triangle3d',
    'draw_triangle_strip3d',
    'draw_cube',
    'draw_cube_v',
    'draw_cube_wires',
    'draw_cube_wires_v',
    'draw_cube_texture',
    'draw_cube_texture_rec',
    'draw_sphere',
    'draw_sphere_ex',
    'draw_sphere_wires',
    'draw_cylinder',
    'draw_cylinder_ex',
    'draw_cylinder_wires',
    'draw_cylinder_wires_ex',
    'draw_plane',
    'draw_ray',
    'draw_grid',
    'load_model',
    'load_model_from_mesh',
    'unload_model',
    'unload_model_keep_meshes',
    'get_model_bounding_box',
    'draw_model',
    'draw_model_ex',
    'draw_model_wires',
    'draw_model_wires_ex',
    'draw_bounding_box',
    'draw_billboard',
    'draw_billboard_rec',
    'draw_billboard_pro',
    'upload_mesh',
    'update_mesh_buffer',
    'unload_mesh',
    'draw_mesh',
    'draw_mesh_instanced',
    'export_mesh',
    'get_mesh_bounding_box',
    'gen_mesh_tangents',
    'gen_mesh_poly',
    'gen_mesh_plane',
    'gen_mesh_cube',
    'gen_mesh_sphere',
    'gen_mesh_hemi_sphere',
    'gen_mesh_cylinder',
    'gen_mesh_cone',
    'gen_mesh_torus',
    'gen_mesh_knot',
    'gen_mesh_heightmap',
    'gen_mesh_cubicmap',
    'load_materials',
    'load_material_default',
    'unload_material',
    'set_material_texture',
    'set_model_mesh_material',
    'load_model_animations',
    'update_model_animation',
    'unload_model_animation',
    'unload_model_animations',
    'is_model_animation_valid',
    'check_collision_spheres',
    'check_collision_boxes',
    'check_collision_box_sphere',
    'get_ray_collision_sphere',
    'get_ray_collision_box',
    'get_ray_collision_mesh',
    'get_ray_collision_triangle',
    'get_ray_collision_quad',
    'init_audio_device',
    'close_audio_device',
    'is_audio_device_ready',
    'set_master_volume',
    'load_wave',
    'load_wave_from_memory',
    'load_sound',
    'load_sound_from_wave',
    'update_sound',
    'unload_wave',
    'unload_sound',
    'export_wave',
    'export_wave_as_code',
    'play_sound',
    'stop_sound',
    'pause_sound',
    'resume_sound',
    'play_sound_multi',
    'stop_sound_multi',
    'get_sounds_playing',
    'is_sound_playing',
    'set_sound_volume',
    'set_sound_pitch',
    'set_sound_pan',
    'wave_copy',
    'wave_crop',
    'wave_format',
    'load_wave_samples',
    'unload_wave_samples',
    'load_music_stream',
    'load_music_stream_from_memory',
    'unload_music_stream',
    'play_music_stream',
    'is_music_stream_playing',
    'update_music_stream',
    'stop_music_stream',
    'pause_music_stream',
    'resume_music_stream',
    'seek_music_stream',
    'set_music_volume',
    'set_music_pitch',
    'set_music_pan',
    'get_music_time_length',
    'get_music_time_played',
    'load_audio_stream',
    'unload_audio_stream',
    'update_audio_stream',
    'is_audio_stream_processed',
    'play_audio_stream',
    'pause_audio_stream',
    'resume_audio_stream',
    'is_audio_stream_playing',
    'stop_audio_stream',
    'set_audio_stream_volume',
    'set_audio_stream_pitch',
    'set_audio_stream_pan',
    'set_audio_stream_buffer_size_default',
    'set_audio_stream_callback',
    'attach_audio_stream_processor',
    'detach_audio_stream_processor',
    'drawing',
    'scissor_mode',
    'blend_mode',
    'mode2d',
    'mode3d',
    'shader_mode',
    'texture_mode',
    'vr_stereo_mode',
    'clamp',
    'lerp',
    'normalize',
    'remap',
    'wrap',
    'float_equals',
    'vector2zero',
    'vector2one',
    'vector2add',
    'vector2add_value',
    'vector2subtract',
    'vector2subtract_value',
    'vector2length',
    'vector2length_sqr',
    'vector2dot_product',
    'vector2distance',
    'vector2distance_sqr',
    'vector2angle',
    'vector2scale',
    'vector2multiply',
    'vector2negate',
    'vector2divide',
    'vector2normalize',
    'vector2transform',
    'vector2lerp',
    'vector2reflect',
    'vector2rotate',
    'vector2move_towards',
    'vector2invert',
    'vector2clamp',
    'vector2clamp_value',
    'vector2equals',
    'vector3zero',
    'vector3one',
    'vector3add',
    'vector3add_value',
    'vector3subtract',
    'vector3subtract_value',
    'vector3scale',
    'vector3multiply',
    'vector3cross_product',
    'vector3perpendicular',
    'vector3length',
    'vector3length_sqr',
    'vector3dot_product',
    'vector3distance',
    'vector3distance_sqr',
    'vector3angle',
    'vector3negate',
    'vector3divide',
    'vector3normalize',
    'vector3ortho_normalize',
    'vector3transform',
    'vector3rotate_by_quaternion',
    'vector3rotate_by_axis_angle',
    'vector3lerp',
    'vector3reflect',
    'vector3min',
    'vector3max',
    'vector3barycenter',
    'vector3unproject',
    'vector3to_float_v',
    'vector3invert',
    'vector3clamp',
    'vector3clamp_value',
    'vector3equals',
    'vector3refract',
    'matrix_determinant',
    'matrix_trace',
    'matrix_transpose',
    'matrix_invert',
    'matrix_identity',
    'matrix_add',
    'matrix_subtract',
    'matrix_multiply',
    'matrix_translate',
    'matrix_rotate',
    'matrix_rotate_x',
    'matrix_rotate_y',
    'matrix_rotate_z',
    'matrix_rotate_xyz',
    'matrix_rotate_zyx',
    'matrix_scale',
    'matrix_frustum',
    'matrix_perspective',
    'matrix_ortho',
    'matrix_look_at',
    'matrix_to_float_v',
    'quaternion_add',
    'quaternion_add_value',
    'quaternion_subtract',
    'quaternion_subtract_value',
    'quaternion_identity',
    'quaternion_length',
    'quaternion_normalize',
    'quaternion_invert',
    'quaternion_multiply',
    'quaternion_scale',
    'quaternion_divide',
    'quaternion_nlerp',
    'quaternion_slerp',
    'quaternion_from_vector3to_vector3',
    'quaternion_to_matrix',
    'quaternion_from_matrix',
    'quaternion_from_axis_angle',
    'quaternion_to_axis_angle',
    'quaternion_from_euler',
    'quaternion_to_euler',
    'quaternion_transform',
    'quaternion_equals',
    'rlVertexBuffer',
    'rlDrawCall',
    'rlRenderBatch',
    'Matrix',
    'RLGL_VERSION',
    'RL_DEFAULT_BATCH_BUFFER_ELEMENTS',
    'RL_DEFAULT_BATCH_BUFFERS',
    'RL_DEFAULT_BATCH_DRAWCALLS',
    'RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS',
    'RL_MAX_MATRIX_STACK_SIZE',
    'RL_MAX_SHADER_LOCATIONS',
    'RL_CULL_DISTANCE_NEAR',
    'RL_CULL_DISTANCE_FAR',
    'RL_TEXTURE_WRAP_S',
    'RL_TEXTURE_WRAP_T',
    'RL_TEXTURE_MAG_FILTER',
    'RL_TEXTURE_MIN_FILTER',
    'RL_TEXTURE_FILTER_NEAREST',
    'RL_TEXTURE_FILTER_LINEAR',
    'RL_TEXTURE_FILTER_MIP_NEAREST',
    'RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR',
    'RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST',
    'RL_TEXTURE_FILTER_MIP_LINEAR',
    'RL_TEXTURE_FILTER_ANISOTROPIC',
    'RL_TEXTURE_WRAP_REPEAT',
    'RL_TEXTURE_WRAP_CLAMP',
    'RL_TEXTURE_WRAP_MIRROR_REPEAT',
    'RL_TEXTURE_WRAP_MIRROR_CLAMP',
    'RL_MODELVIEW',
    'RL_PROJECTION',
    'RL_TEXTURE',
    'RL_LINES',
    'RL_TRIANGLES',
    'RL_QUADS',
    'RL_UNSIGNED_BYTE',
    'RL_FLOAT',
    'RL_STREAM_DRAW',
    'RL_STREAM_READ',
    'RL_STREAM_COPY',
    'RL_STATIC_DRAW',
    'RL_STATIC_READ',
    'RL_STATIC_COPY',
    'RL_DYNAMIC_DRAW',
    'RL_DYNAMIC_READ',
    'RL_DYNAMIC_COPY',
    'RL_FRAGMENT_SHADER',
    'RL_VERTEX_SHADER',
    'RL_COMPUTE_SHADER',
    'rlGlVersion',
    'OPENGL_11',
    'OPENGL_21',
    'OPENGL_33',
    'OPENGL_43',
    'OPENGL_ES_20',
    'rlFramebufferAttachType',
    'RL_ATTACHMENT_COLOR_CHANNEL0',
    'RL_ATTACHMENT_COLOR_CHANNEL1',
    'RL_ATTACHMENT_COLOR_CHANNEL2',
    'RL_ATTACHMENT_COLOR_CHANNEL3',
    'RL_ATTACHMENT_COLOR_CHANNEL4',
    'RL_ATTACHMENT_COLOR_CHANNEL5',
    'RL_ATTACHMENT_COLOR_CHANNEL6',
    'RL_ATTACHMENT_COLOR_CHANNEL7',
    'RL_ATTACHMENT_DEPTH',
    'RL_ATTACHMENT_STENCIL',
    'rlFramebufferAttachTextureType',
    'RL_ATTACHMENT_CUBEMAP_POSITIVE_X',
    'RL_ATTACHMENT_CUBEMAP_NEGATIVE_X',
    'RL_ATTACHMENT_CUBEMAP_POSITIVE_Y',
    'RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y',
    'RL_ATTACHMENT_CUBEMAP_POSITIVE_Z',
    'RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z',
    'RL_ATTACHMENT_TEXTURE2D',
    'RL_ATTACHMENT_RENDERBUFFER',
    'rlTraceLogLevel',
    'RL_LOG_ALL',
    'RL_LOG_TRACE',
    'RL_LOG_DEBUG',
    'RL_LOG_INFO',
    'RL_LOG_WARNING',
    'RL_LOG_ERROR',
    'RL_LOG_FATAL',
    'RL_LOG_NONE',
    'rlPixelFormat',
    'RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE',
    'RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA',
    'RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5',
    'RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8',
    'RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1',
    'RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4',
    'RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8',
    'RL_PIXELFORMAT_UNCOMPRESSED_R32',
    'RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32',
    'RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32',
    'RL_PIXELFORMAT_COMPRESSED_DXT1_RGB',
    'RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_ETC1_RGB',
    'RL_PIXELFORMAT_COMPRESSED_ETC2_RGB',
    'RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_PVRT_RGB',
    'RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA',
    'rlTextureFilter',
    'RL_TEXTURE_FILTER_POINT',
    'RL_TEXTURE_FILTER_BILINEAR',
    'RL_TEXTURE_FILTER_TRILINEAR',
    'RL_TEXTURE_FILTER_ANISOTROPIC_4X',
    'RL_TEXTURE_FILTER_ANISOTROPIC_8X',
    'RL_TEXTURE_FILTER_ANISOTROPIC_16X',
    'rlBlendMode',
    'RL_BLEND_ALPHA',
    'RL_BLEND_ADDITIVE',
    'RL_BLEND_MULTIPLIED',
    'RL_BLEND_ADD_COLORS',
    'RL_BLEND_SUBTRACT_COLORS',
    'RL_BLEND_ALPHA_PREMULTIPLY',
    'RL_BLEND_CUSTOM',
    'rlShaderLocationIndex',
    'RL_SHADER_LOC_VERTEX_POSITION',
    'RL_SHADER_LOC_VERTEX_TEXCOORD01',
    'RL_SHADER_LOC_VERTEX_TEXCOORD02',
    'RL_SHADER_LOC_VERTEX_NORMAL',
    'RL_SHADER_LOC_VERTEX_TANGENT',
    'RL_SHADER_LOC_VERTEX_COLOR',
    'RL_SHADER_LOC_MATRIX_MVP',
    'RL_SHADER_LOC_MATRIX_VIEW',
    'RL_SHADER_LOC_MATRIX_PROJECTION',
    'RL_SHADER_LOC_MATRIX_MODEL',
    'RL_SHADER_LOC_MATRIX_NORMAL',
    'RL_SHADER_LOC_VECTOR_VIEW',
    'RL_SHADER_LOC_COLOR_DIFFUSE',
    'RL_SHADER_LOC_COLOR_SPECULAR',
    'RL_SHADER_LOC_COLOR_AMBIENT',
    'RL_SHADER_LOC_MAP_ALBEDO',
    'RL_SHADER_LOC_MAP_METALNESS',
    'RL_SHADER_LOC_MAP_NORMAL',
    'RL_SHADER_LOC_MAP_ROUGHNESS',
    'RL_SHADER_LOC_MAP_OCCLUSION',
    'RL_SHADER_LOC_MAP_EMISSION',
    'RL_SHADER_LOC_MAP_HEIGHT',
    'RL_SHADER_LOC_MAP_CUBEMAP',
    'RL_SHADER_LOC_MAP_IRRADIANCE',
    'RL_SHADER_LOC_MAP_PREFILTER',
    'RL_SHADER_LOC_MAP_BRDF',
    'rlShaderUniformDataType',
    'RL_SHADER_UNIFORM_FLOAT',
    'RL_SHADER_UNIFORM_VEC2',
    'RL_SHADER_UNIFORM_VEC3',
    'RL_SHADER_UNIFORM_VEC4',
    'RL_SHADER_UNIFORM_INT',
    'RL_SHADER_UNIFORM_IVEC2',
    'RL_SHADER_UNIFORM_IVEC3',
    'RL_SHADER_UNIFORM_IVEC4',
    'RL_SHADER_UNIFORM_SAMPLER2D',
    'rlShaderAttributeDataType',
    'RL_SHADER_ATTRIB_FLOAT',
    'RL_SHADER_ATTRIB_VEC2',
    'RL_SHADER_ATTRIB_VEC3',
    'RL_SHADER_ATTRIB_VEC4',
    'rl_matrix_mode',
    'rl_push_matrix',
    'rl_pop_matrix',
    'rl_load_identity',
    'rl_translatef',
    'rl_rotatef',
    'rl_scalef',
    'rl_mult_matrixf',
    'rl_frustum',
    'rl_ortho',
    'rl_viewport',
    'rl_begin',
    'rl_end',
    'rl_vertex2i',
    'rl_vertex2f',
    'rl_vertex3f',
    'rl_tex_coord2f',
    'rl_normal3f',
    'rl_color4ub',
    'rl_color3f',
    'rl_color4f',
    'rl_enable_vertex_array',
    'rl_disable_vertex_array',
    'rl_enable_vertex_buffer',
    'rl_disable_vertex_buffer',
    'rl_enable_vertex_buffer_element',
    'rl_disable_vertex_buffer_element',
    'rl_enable_vertex_attribute',
    'rl_disable_vertex_attribute',
    'rl_active_texture_slot',
    'rl_enable_texture',
    'rl_disable_texture',
    'rl_enable_texture_cubemap',
    'rl_disable_texture_cubemap',
    'rl_texture_parameters',
    'rl_enable_shader',
    'rl_disable_shader',
    'rl_enable_framebuffer',
    'rl_disable_framebuffer',
    'rl_active_draw_buffers',
    'rl_enable_color_blend',
    'rl_disable_color_blend',
    'rl_enable_depth_test',
    'rl_disable_depth_test',
    'rl_enable_depth_mask',
    'rl_disable_depth_mask',
    'rl_enable_backface_culling',
    'rl_disable_backface_culling',
    'rl_enable_scissor_test',
    'rl_disable_scissor_test',
    'rl_scissor',
    'rl_enable_wire_mode',
    'rl_disable_wire_mode',
    'rl_set_line_width',
    'rl_get_line_width',
    'rl_enable_smooth_lines',
    'rl_disable_smooth_lines',
    'rl_enable_stereo_render',
    'rl_disable_stereo_render',
    'rl_is_stereo_render_enabled',
    'rl_clear_color',
    'rl_clear_screen_buffers',
    'rl_check_errors',
    'rl_set_blend_mode',
    'rl_set_blend_factors',
    'rlgl_init',
    'rlgl_close',
    'rl_load_extensions',
    'rl_get_version',
    'rl_set_framebuffer_width',
    'rl_get_framebuffer_width',
    'rl_set_framebuffer_height',
    'rl_get_framebuffer_height',
    'rl_get_texture_id_default',
    'rl_get_shader_id_default',
    'rl_get_shader_locs_default',
    'rl_load_render_batch',
    'rl_unload_render_batch',
    'rl_draw_render_batch',
    'rl_set_render_batch_active',
    'rl_draw_render_batch_active',
    'rl_check_render_batch_limit',
    'rl_set_texture',
    'rl_load_vertex_array',
    'rl_load_vertex_buffer',
    'rl_load_vertex_buffer_element',
    'rl_update_vertex_buffer',
    'rl_update_vertex_buffer_elements',
    'rl_unload_vertex_array',
    'rl_unload_vertex_buffer',
    'rl_set_vertex_attribute',
    'rl_set_vertex_attribute_divisor',
    'rl_set_vertex_attribute_default',
    'rl_draw_vertex_array',
    'rl_draw_vertex_array_elements',
    'rl_draw_vertex_array_instanced',
    'rl_draw_vertex_array_elements_instanced',
    'rl_load_texture',
    'rl_load_texture_depth',
    'rl_load_texture_cubemap',
    'rl_update_texture',
    'rl_get_gl_texture_formats',
    'rl_get_pixel_format_name',
    'rl_unload_texture',
    'rl_gen_texture_mipmaps',
    'rl_read_texture_pixels',
    'rl_read_screen_pixels',
    'rl_load_framebuffer',
    'rl_framebuffer_attach',
    'rl_framebuffer_complete',
    'rl_unload_framebuffer',
    'rl_load_shader_code',
    'rl_compile_shader',
    'rl_load_shader_program',
    'rl_unload_shader_program',
    'rl_get_location_uniform',
    'rl_get_location_attrib',
    'rl_set_uniform',
    'rl_set_uniform_matrix',
    'rl_set_uniform_sampler',
    'rl_set_shader',
    'rl_load_compute_shader_program',
    'rl_compute_shader_dispatch',
    'rl_load_shader_buffer',
    'rl_unload_shader_buffer',
    'rl_update_shader_buffer_elements',
    'rl_get_shader_buffer_size',
    'rl_read_shader_buffer_elements',
    'rl_bind_shader_buffer',
    'rl_copy_buffers_elements',
    'rl_bind_image_texture',
    'rl_get_matrix_modelview',
    'rl_get_matrix_projection',
    'rl_get_matrix_transform',
    'rl_get_matrix_projection_stereo',
    'rl_get_matrix_view_offset_stereo',
    'rl_set_matrix_projection',
    'rl_set_matrix_modelview',
    'rl_set_matrix_projection_stereo',
    'rl_set_matrix_view_offset_stereo',
    'rl_load_draw_cube',
    'rl_load_draw_quad',
]

# region LIBRARY LOADING

# region CDLLEX

if sys.platform == 'win32':
    DONT_RESOLVE_DLL_REFERENCES = 0x00000001
    LOAD_LIBRARY_AS_DATAFILE = 0x00000002
    LOAD_WITH_ALTERED_SEARCH_PATH = 0x00000008
    LOAD_IGNORE_CODE_AUTHZ_LEVEL = 0x00000010  # NT 6.1
    LOAD_LIBRARY_AS_IMAGE_RESOURCE = 0x00000020  # NT 6.0
    LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE = 0x00000040  # NT 6.0

    # These cannot be combined with LOAD_WITH_ALTERED_SEARCH_PATH.
    # Install update KB2533623 for NT 6.0 & 6.1.
    LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR = 0x00000100
    LOAD_LIBRARY_SEARCH_APPLICATION_DIR = 0x00000200
    LOAD_LIBRARY_SEARCH_USER_DIRS = 0x00000400
    LOAD_LIBRARY_SEARCH_SYSTEM32 = 0x00000800
    LOAD_LIBRARY_SEARCH_DEFAULT_DIRS = 0x00001000

    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)


    def check_bool(result, func, args):
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return args


    kernel32.LoadLibraryExW.errcheck = check_bool
    kernel32.LoadLibraryExW.restype = wintypes.HMODULE
    kernel32.LoadLibraryExW.argtypes = (wintypes.LPCWSTR,
                                        wintypes.HANDLE,
                                        wintypes.DWORD)


    class CDLLEx(ctypes.CDLL):
        def __init__(self, name, mode=0, handle=None,
                    use_errno=True, use_last_error=False):
            if handle is None:
                handle = kernel32.LoadLibraryExW(name, None, mode)
            super(CDLLEx, self).__init__(name, mode, handle,
                                        use_errno, use_last_error)


    class WinDLLEx(ctypes.WinDLL):
        def __init__(self, name, mode=0, handle=None,
                    use_errno=False, use_last_error=True):
            if handle is None:
                handle = kernel32.LoadLibraryExW(name, None, mode)
            super(WinDLLEx, self).__init__(name, mode, handle,
                                        use_errno, use_last_error)


# endregion (cdllex)


_lib_fname = {
    'win32': 'raylib.dll',
    'linux': 'libraylib.so.4.2.0',
    'darwin': 'libraylib.4.2.0.dylib'
}

_lib_platform = sys.platform

if _lib_platform == 'win32':
    _bitness = platform.architecture()[0]
else:
    _bitness = '64bit' if sys.maxsize > 2 ** 32 else '32bit'

_lib_fname_abspath = os.path.join(os.path.dirname(__file__), 'bin', _bitness, _lib_fname[_lib_platform])
_lib_fname_abspath = os.path.normcase(os.path.normpath(_lib_fname_abspath))

print(
    """Library loading info:
    platform: {}
    bitness: {}
    absolute path: {}
    exists: {}
    is file: {}
    """.format(
        _lib_platform,
        _bitness,
        _lib_fname_abspath,
        'yes' if os.path.exists(_lib_fname_abspath) else 'no',
        'yes' if os.path.isfile(_lib_fname_abspath) else 'no'
    )
)

rlapi = None
if _lib_platform == 'win32':

    try:
        rlapi = CDLLEx(_lib_fname_abspath, LOAD_WITH_ALTERED_SEARCH_PATH)
    except OSError:
        print("Unable to load {}.".format(_lib_fname[_lib_platform]))
        rlapi = None
else:
    rlapi = CDLL(_lib_fname_abspath)

if rlapi is None:
    print("Failed to load shared library.")
    exit()
else:
    print("Shared library loaded succesfully.", rlapi)



Bool = c_bool
BoolPtr = POINTER(c_bool)
Byte = c_byte
BytePtr = POINTER(c_byte)
Char = c_char
CharPtr = POINTER(c_char)
Short = c_short
ShortPtr = POINTER(c_short)
Int = c_long
IntPtr = POINTER(c_long)
Long = c_long
LongPtr = POINTER(c_long)
LongLong = c_longlong
LongLongPtr = POINTER(c_longlong)
UChar = c_ubyte
UCharPtr = POINTER(c_ubyte)
UByte = c_ubyte
UBytePtr = POINTER(c_ubyte)
UShort = c_ushort
UShortPtr = POINTER(c_ushort)
UInt = c_ulong
UIntPtr = POINTER(c_ulong)
ULong = c_ulong
ULongPtr = POINTER(c_ulong)
ULongLong = c_ulonglong
ULongLongPtr = POINTER(c_ulonglong)
Float = c_float
FloatPtr = POINTER(c_float)
Double = c_double
DoublePtr = POINTER(c_double)
VoidPtr = c_void_p
VoidPtrPtr = POINTER(c_void_p)
CharPtr = c_char_p
CharPtrPtr = POINTER(c_char_p)


# Vector component swizzling helppers
_VEC2_GET_SWZL = re.compile(r'[xy]{,4}')
_VEC3_GET_SWZL = re.compile(r'[xyz]{,4}')
_VEC4_GET_SWZL = re.compile(r'[xyzw]{,4}')
_RGBA_GET_SWZL = re.compile(r'[rgba]{4}')
_RECT_GET_SWZL = re.compile(r'(width|height|[xywh]{4})')

_VEC2_SET_SWZL = re.compile(r'[xy]{,2}')
_VEC3_SET_SWZL = re.compile(r'[xyz]{,3}')
_VEC4_SET_SWZL = re.compile(r'[xyzw]{,4}')
_RGBA_SET_SWZL = re.compile(r'[rgba]{1,4}')
_RECT_SET_SWZL = re.compile(r'(width|height|[xywh]{1,4})')

# region FUNCTIONS


def _clsname(obj):
    return obj.__class__.__name__


def is_number(obj):
    return isinstance(obj, (int, float))


def is_component(value):
    return isinstance(value, int) and 0 <= value <= 255


def _clamp_rgba(*args):
    return tuple(value & 255 for value in args)


def _str_in(value):
    return value.encode('utf-8', 'ignore') if isinstance(value, str) else value


def _str_in2(values):
    return _arr_in(CharPtr, tuple(_str_in(value) for value in values))


def _str_out(value):
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


def _arr_in(typ, data):
    if isinstance(data, POINTER(typ)):
        return data
    return (typ * len(data))(*data)


def _arr2_in(typ, data):
    arr = typ * len(data[0])
    return (arr * len(data))(*data)


def _arr_out(data):
    return data.values


def _ptr_out(ptr, length=0):
    [ptr.contents] if length == 1 else ([] if not length else ptr[:length])

# region TYPE CAST FUNCS


def _float(value):
    return float(value)


def _int(value, ranged=None):
    if ranged:
        return max(ranged[0], min(int(value), ranged[1]))
    return int(value)


def _vec2(seq):
    if isinstance(seq, Vector2):
        return seq
    x, y = seq
    return Vector2(_float(x), _float(y))


def _vec3(seq):
    if isinstance(seq, Vector3):
        return seq
    x, y, z = seq
    return Vector3(float(x), float(y), float(z))


def _vec4(seq):
    if isinstance(seq, Vector4):
        return seq
    x, y, z, w = seq
    return Vector4(float(x), float(y), float(z), float(w))


def _rect(seq):
    if isinstance(seq, Rectangle):
        return seq
    x, y, w, h = seq
    return Rectangle(float(x), float(y), float(w), float(h))


def _color(seq):
    if isinstance(seq, Color):
        return seq
    r, g, b, q = seq
    rng = 0, 255
    return Color(_int(r, rng), _int(r, rng), _int(b, rng), _int(q, rng))

# endregion (type cast funcs)


def _wrap(api, argtypes, restype):
    api.argtypes = argtypes
    api.restype = restype
    return api

# endregion (functions)


# Struct not exposed in raylib.h
class rAudioBufferPtr(Structure):
    pass


# Struct not exposed in raylib.h
class rAudioProcessorPtr(Structure):
    pass



class Vector2(Structure):
    '''Vector2, 2 components'''
    _fields_ = [
        ('x', Float),
        ('y', Float),
    ]


    @classmethod
    def array_of(cls, vector2_sequence):
        '''Creates and returns an array of Vector2s'''
        arr = cls * len(vector2_sequence)
        return arr(*vector2_sequence)

    @classmethod
    def one():
        # type: () -> Vector2
        """Vector with components value 1.0f"""
        result = _Vector2One()
        return result


    def __init__(self, x=None, y=None):
        # type: (float, float) -> None
        '''Initializes this Vector2 struct'''
        super(Vector2, self).__init__(
            x or 0.0,
            y or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Vector2 instance'''
        return byref(self)


    def __len__(self):
        return 2

    def __getitem__(self, key):
        return (self.x, self.y).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC2_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("Vector2 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC2_SET_SWZL.match(attr)
        if not m:
            raise AttributeError("Vector2 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector2, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector2, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector2's components'''
        return {'x': self.x, 'y': self.y}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector2's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))


    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Vector2{}".format(self.__str__())

    @property
    def length(self):
        # type: (Vector2) -> float
        """Calculate vector length"""
        result = _Vector2Length(self)
        return result

    @property
    def length_sqr(self):
        # type: (Vector2) -> float
        """Calculate vector square length"""
        result = _Vector2LengthSqr(self)
        return result

    def dot_product(self, v2):
        # type: (Vector2, Vector2) -> float
        """Calculate two vectors dot product"""
        result = _Vector2DotProduct(self, _vec2(v2))
        return result

    def distance(self, v2):
        # type: (Vector2, Vector2) -> float
        """Calculate distance between two vectors"""
        result = _Vector2Distance(self, _vec2(v2))
        return result

    def distance_sqr(self, v2):
        # type: (Vector2, Vector2) -> float
        """Calculate square distance between two vectors"""
        result = _Vector2DistanceSqr(self, _vec2(v2))
        return result

    def angle(self, v2):
        # type: (Vector2, Vector2) -> float
        """Calculate angle from two vectors"""
        result = _Vector2Angle(self, _vec2(v2))
        return result

    def normalize(self):
        # type: (Vector2) -> Vector2
        """Normalize provided vector"""
        self.xy = _Vector2Normalize(self)
        return self

    def transform(self, mat):
        # type: (Vector2, Matrix) -> Vector2
        """Transforms a Vector2 by a given Matrix"""
        self.xy = _Vector2Transform(self, mat)
        return self

    def lerp(self, v2, amount):
        # type: (Vector2, Vector2, float) -> Vector2
        """Calculate linear interpolation between two vectors"""
        self.xy = _Vector2Lerp(self, _vec2(v2), float(amount))
        return self

    def reflect(self, normal):
        # type: (Vector2, Vector2) -> Vector2
        """Calculate reflected vector to normal"""
        self.xy = _Vector2Reflect(self, _vec2(normal))
        return self

    def rotate(self, angle):
        # type: (Vector2, float) -> Vector2
        """Rotate vector by angle"""
        self.xy = _Vector2Rotate(self, float(angle))
        return self

    def move_towards(self, target, max_distance):
        # type: (Vector2, Vector2, float) -> Vector2
        """Move Vector towards target"""
        self.xy = _Vector2MoveTowards(self, _vec2(target), float(max_distance))
        return self

    def clamp(self, min_, max_):
        # type: (Vector2, Vector2, Vector2) -> Vector2
        """Clamp the components of the vector between min and max values specified by the given vectors"""
        self.xy = _Vector2Clamp(self, _vec2(min_), _vec2(max_))
        return self

    def clamp_value(self, min_, max_):
        # type: (Vector2, float, float) -> Vector2
        """Clamp the magnitude of the vector between two min and max values"""
        self.xy = _Vector2ClampValue(self, float(min_), float(max_))
        return self


# Pointer type to Vector2s
Vector2Ptr = POINTER(Vector2)



class Vector3(Structure):
    '''Vector3, 3 components'''
    _fields_ = [
        ('x', Float),
        ('y', Float),
        ('z', Float),
    ]


    @classmethod
    def array_of(cls, vector3_sequence):
        '''Creates and returns an array of Vector3s'''
        arr = cls * len(vector3_sequence)
        return arr(*vector3_sequence)

    @classmethod
    def one():
        # type: () -> Vector3
        """Vector with components value 1.0f"""
        result = _Vector3One()
        return result


    def __init__(self, x=None, y=None, z=None):
        # type: (float, float, float) -> None
        '''Initializes this Vector3 struct'''
        super(Vector3, self).__init__(
            x or 0.0,
            y or 0.0,
            z or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Vector3 instance'''
        return byref(self)


    def __len__(self):
        return 3

    def __getitem__(self, key):
        return (self.x, self.y, self.z).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC3_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("Vector3 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC3_SET_SWZL.match(attr)
        if not m:
            raise AttributeError("Vector3 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector3, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector3, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector3's components'''
        return {'x': self.x, 'y': self.y, 'z': self.z}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector3's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.z = float(d.get('z', self.z))

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Vector3{}".format(self.__str__())

    @property
    def length(self):
        # type: (Vector3) -> float
        """Calculate vector length"""
        result = _Vector3Length(self)
        return result

    @property
    def length_sqr(self):
        # type: (Vector3) -> float
        """Calculate vector square length"""
        result = _Vector3LengthSqr(self)
        return result

    def cross_product(self, v2):
        # type: (Vector3, Vector3) -> float
        """Calculate two vectors cross product"""
        result = _Vector3CrossProduct(self, _vec3(v2))
        return result

    def perpendicular(self):
        # type: (Vector3) -> Vector3
        """Calculate one vector perpendicular vector"""
        self.xyz = _Vector3Perpendicular(self)
        return self

    def dot_product(self, v2):
        # type: (Vector3, Vector3) -> float
        """Calculate two vectors dot product"""
        result = _Vector3DotProduct(self, _vec3(v2))
        return result

    def distance(self, v2):
        # type: (Vector3, Vector3) -> float
        """Calculate distance between two vectors"""
        result = _Vector3Distance(self, _vec3(v2))
        return result

    def distance_sqr(self, v2):
        # type: (Vector3, Vector3) -> float
        """Calculate square distance between two vectors"""
        result = _Vector3DistanceSqr(self, _vec3(v2))
        return result

    def angle(self, v2):
        # type: (Vector3, Vector3) -> float
        """Calculate angle between two vectors"""
        result = _Vector3Angle(self, _vec3(v2))
        return result

    def normalize(self):
        # type: (Vector3) -> Vector3
        """Normalize provided vector"""
        self.xyz = _Vector3Normalize(self)
        return self

    def ortho_normalize(self, v2):
        # type: (Vector3Ptr, Vector3Ptr) -> Vector3
        """Makes vectors normalized and orthogonal to each other"""
        self.xyz = _Vector3OrthoNormalize(self, _vec3(v2))
        return self

    def transform(self, mat):
        # type: (Vector3, Matrix) -> Vector3
        """Transforms a Vector3 by a given Matrix"""
        self.xyz = _Vector3Transform(self, mat)
        return self

    def rotate_by_quaternion(self, q):
        # type: (Vector3, Quaternion) -> Vector3
        """Transform a vector by quaternion rotation"""
        self.xyz = _Vector3RotateByQuaternion(self, q)
        return self

    def rotate_by_axis_angle(self, axis, angle):
        # type: (Vector3, Vector3, float) -> Vector3
        """Rotates a vector around an axis"""
        self.xyz = _Vector3RotateByAxisAngle(self, _vec3(axis), float(angle))
        return self

    def lerp(self, v2, amount):
        # type: (Vector3, Vector3, float) -> Vector3
        """Calculate linear interpolation between two vectors"""
        self.xyz = _Vector3Lerp(self, _vec3(v2), float(amount))
        return self

    def reflect(self, normal):
        # type: (Vector3, Vector3) -> Vector3
        """Calculate reflected vector to normal"""
        self.xyz = _Vector3Reflect(self, _vec3(normal))
        return self

    def min(self, v2):
        # type: (Vector3, Vector3) -> Vector3
        """Get min value for each pair of components"""
        self.xyz = _Vector3Min(self, _vec3(v2))
        return self

    def max(self, v2):
        # type: (Vector3, Vector3) -> Vector3
        """Get max value for each pair of components"""
        self.xyz = _Vector3Max(self, _vec3(v2))
        return self

    def barycenter(self, a, b, c):
        # type: (Vector3, Vector3, Vector3, Vector3) -> Vector3
        """Compute barycenter coordinates (u, v, w) for point p with respect to triangle (a, b, c). Assumes P is on the plane of the triangle"""
        self.xyz = _Vector3Barycenter(self, _vec3(a), _vec3(b), _vec3(c))
        return self

    def unproject(self, projection, view):
        # type: (Vector3, Matrix, Matrix) -> Vector3
        """Projects a Vector3 from screen space into object space"""
        self.xyz = _Vector3Unproject(self, projection, view)
        return self

    def to_float_v(self):
        # type: (Vector3) -> Seq[float]
        """Get Vector3 as float array"""
        result = _Vector3ToFloatV(self)
        return result

    def clamp(self, min_, max_):
        # type: (Vector3, Vector3, Vector3) -> Vector3
        """Clamp the components of the vector between min and max values specified by the given vectors"""
        self.xyz = _Vector3Clamp(self, _vec3(min_), _vec3(max_))
        return self

    def clamp_value(self, min_, max_):
        # type: (Vector3, float, float) -> Vector3
        """Clamp the magnitude of the vector between two values"""
        self.xyz = _Vector3ClampValue(self, float(min_), float(max_))
        return self

    def refract(self, n, r):
        # type: (Vector3, Vector3, float) -> int
        """Compute the direction of a refracted ray where v specifies the normalized direction of the incoming ray, n specifies the normalized normal vector of the interface of two optical media, and r specifies the ratio of the refractive index of the medium from where the ray comes to the refractive index of the medium on the other side of the surface"""
        result = _Vector3Refract(self, _vec3(n), float(r))
        return result


# Pointer type to Vector3s
Vector3Ptr = POINTER(Vector3)



class Vector4(Structure):
    '''Vector4, 4 components'''
    _fields_ = [
        ('x', Float),
        ('y', Float),
        ('z', Float),
        ('w', Float),
    ]


    @classmethod
    def array_of(cls, vector4_sequence):
        '''Creates and returns an array of Vector4s'''
        arr = cls * len(vector4_sequence)
        return arr(*vector4_sequence)


    def __init__(self, x=None, y=None, z=None, w=None):
        # type: (float, float, float, float) -> None
        '''Initializes this Vector4 struct'''
        super(Vector4, self).__init__(
            x or 0.0,
            y or 0.0,
            z or 0.0,
            w or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Vector4 instance'''
        return byref(self)


    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self.x, self.y. self.z, self.w).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC4_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("Vector4 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC4_SET_SWZL.match(attr)
        if not m:
            raise AttributeError("Vector4 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector4, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector4, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector4's components'''
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector4's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.z = float(d.get('z', self.z))
        self.w = float(d.get('w', self.w))


    def __str__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)

    def __repr__(self):
        return "Vector4{}".format(self.__str__())


# Pointer type to Vector4s
Vector4Ptr = POINTER(Vector4)


# Quaternion, 4 components (Vector4 alias)
Quaternion = Vector4
QuaternionPtr = Vector4Ptr

class Matrix(Structure):
    '''Matrix, 4x4 components, column major, OpenGL style, right handed'''
    _fields_ = [
        ('m0', Float),
        ('m4', Float),
        ('m8', Float),
        ('m12', Float),
        ('m1', Float),
        ('m5', Float),
        ('m9', Float),
        ('m13', Float),
        ('m2', Float),
        ('m6', Float),
        ('m10', Float),
        ('m14', Float),
        ('m3', Float),
        ('m7', Float),
        ('m11', Float),
        ('m15', Float),
    ]


    @classmethod
    def array_of(cls, matrix_sequence):
        '''Creates and returns an array of Matrixs'''
        arr = cls * len(matrix_sequence)
        return arr(*matrix_sequence)

    @classmethod
    def identity():
        # type: () -> Matrix
        """Get identity matrix"""
        result = _MatrixIdentity()
        return result

    @classmethod
    def translate(cls, x, y, z):
        # type: (float, float, float) -> Matrix
        """Get translation matrix"""
        result = _MatrixTranslate(float(x), float(y), float(z))
        return result

    @classmethod
    def rotate(cls, axis, angle):
        # type: (Vector3, float) -> Matrix
        """Create rotation matrix from axis and angle. Angle should be provided in radians"""
        result = _MatrixRotate(_vec3(axis), float(angle))
        return result

    @classmethod
    def rotate_x(cls, angle):
        # type: (float) -> Matrix
        """Get x-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateX(float(angle))
        return result

    @classmethod
    def rotate_y(cls, angle):
        # type: (float) -> Matrix
        """Get y-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateY(float(angle))
        return result

    @classmethod
    def rotate_z(cls, angle):
        # type: (float) -> Matrix
        """Get z-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateZ(float(angle))
        return result

    @classmethod
    def rotate_xyz(cls, angle):
        # type: (Vector3) -> Matrix
        """Get xyz-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateXYZ(_vec3(angle))
        return result

    @classmethod
    def rotate_zyx(cls, angle):
        # type: (Vector3) -> Matrix
        """Get zyx-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateZYX(_vec3(angle))
        return result

    @classmethod
    def scale(cls, x, y, z):
        # type: (float, float, float) -> Matrix
        """Get scaling matrix"""
        result = _MatrixScale(float(x), float(y), float(z))
        return result

    @classmethod
    def frustum(cls, left, right, bottom, top, near, far):
        # type: (float, float, float, float, float, float) -> Matrix
        """Get perspective projection matrix"""
        result = _MatrixFrustum(float(left), float(right), float(bottom), float(top), float(near), float(far))
        return result

    @classmethod
    def perspective(cls, fovy, aspect, near, far):
        # type: (float, float, float, float) -> Matrix
        """Get perspective projection matrix. Fovy angle must be provided in radians"""
        result = _MatrixPerspective(float(fovy), float(aspect), float(near), float(far))
        return result

    @classmethod
    def ortho(cls, left, right, bottom, top, near, far):
        # type: (float, float, float, float, float, float) -> Matrix
        """Get orthographic projection matrix"""
        result = _MatrixOrtho(float(left), float(right), float(bottom), float(top), float(near), float(far))
        return result

    @classmethod
    def look_at(cls, eye, target, up):
        # type: (Vector3, Vector3, Vector3) -> Matrix
        """Get camera look-at matrix (view matrix)"""
        result = _MatrixLookAt(_vec3(eye), _vec3(target), _vec3(up))
        return result


    def __init__(self, m0=None,
                 m4=None,
                 m8=None,
                 m12=None,
                 m1=None,
                 m5=None,
                 m9=None,
                 m13=None,
                 m2=None,
                 m6=None,
                 m10=None,
                 m14=None,
                 m3=None,
                 m7=None,
                 m11=None,
                 m15=None):
        # type: (float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float) -> None
        '''Initializes this Matrix struct'''
        super(Matrix, self).__init__(
            m0 or 0.0,
            m4 or 0.0,
            m8 or 0.0,
            m12 or 0.0,
            m1 or 0.0,
            m5 or 0.0,
            m9 or 0.0,
            m13 or 0.0,
            m2 or 0.0,
            m6 or 0.0,
            m10 or 0.0,
            m14 or 0.0,
            m3 or 0.0,
            m7 or 0.0,
            m11 or 0.0,
            m15 or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Matrix instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def determinant(self):
        # type: (Matrix) -> float
        """Compute matrix determinant"""
        result = _MatrixDeterminant(self)
        return result

    def trace(self):
        # type: (Matrix) -> float
        """Get the trace of the matrix (sum of the values along the diagonal)"""
        result = _MatrixTrace(self)
        return result

    def transpose(self):
        # type: (Matrix) -> Matrix
        """Get the trace of the matrix (sum of the values along the diagonal)"""
        result = _MatrixTranspose(self)
        return result

    def invert(self):
        # type: (Matrix) -> Matrix
        """Invert provided matrix"""
        result = _MatrixInvert(self)
        return result


# Pointer type to Matrixs
MatrixPtr = POINTER(Matrix)



class Color(Structure):
    '''Color, 4 components, R8G8B8A8 (32bit)'''
    _fields_ = [
        ('r', UChar),
        ('g', UChar),
        ('b', UChar),
        ('a', UChar),
    ]


    @classmethod
    def array_of(cls, color_sequence):
        '''Creates and returns an array of Colors'''
        arr = cls * len(color_sequence)
        return arr(*color_sequence)


    def __init__(self, r=None, g=None, b=None, a=None):
        # type: (int, int, int, int) -> None
        '''Initializes this Color struct'''
        super(Color, self).__init__(
            r or 0,
            g or 0,
            b or 0,
            a or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Color instance'''
        return byref(self)


    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self.r, self.g, self.b, self.a).__getitem__(key)

    def __getattr__(self, attr):
        m = _RGBA_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("Color object does not have attribute '{}'.".format(attr))
        cls = {1: int, 4: Color}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _RGBA_SET_SWZL.match(attr)
        if not m:
            raise AttributeError("Color object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Color, self).__setattr__(attr, int(value))
        else:
            for i, ch in enumerate(attr):
                super(Color, self).__setattr__(ch, int(value[i]))

    def todict(self):
        '''Returns a dict mapping this Color's components'''
        return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Color's components'''
        self.r = int(d.get('r', self.r))
        self.g = int(d.get('g', self.g))
        self.b = int(d.get('b', self.b))
        self.a = int(d.get('a', self.a))


    def __str__(self):
        return "({: 3}, {: 3}, {: 3}, {: 3})".format(self.r, self.g, self.b, self.a)

    def __repr__(self):
        return "Color{}".format(self.__str__())

    def fade(self, alpha):
        # type: (Color, float) -> Color
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        result = _Fade(self, float(alpha))
        return result

    def to_int(self):
        # type: (Color) -> int
        """Get hexadecimal value for a Color"""
        result = _ColorToInt(self)
        return result

    def to_hsv(self):
        # type: (Color) -> Vector3
        """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
        result = _ColorToHSV(self)
        return result

    def from_hsv(self, saturation, value):
        # type: (float, float, float) -> Color
        """Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
        result = _ColorFromHSV(self, float(saturation), float(value))
        return result

    def alpha(self, alpha):
        # type: (Color, float) -> Color
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        result = _ColorAlpha(self, float(alpha))
        return result

    def alpha_blend(self, src, tint):
        # type: (Color, Color, Color) -> Color
        """Get src alpha-blended into dst color with tint"""
        result = _ColorAlphaBlend(self, _color(src), _color(tint))
        return result


# Pointer type to Colors
ColorPtr = POINTER(Color)



class Rectangle(Structure):
    '''Rectangle, 4 components'''
    _fields_ = [
        ('x', Float),
        ('y', Float),
        ('width', Float),
        ('height', Float),
    ]


    @classmethod
    def array_of(cls, rectangle_sequence):
        '''Creates and returns an array of Rectangles'''
        arr = cls * len(rectangle_sequence)
        return arr(*rectangle_sequence)


    def __init__(self, x=None, y=None, width=None, height=None):
        # type: (float, float, float, float) -> None
        '''Initializes this Rectangle struct'''
        super(Rectangle, self).__init__(
            x or 0.0,
            y or 0.0,
            width or 0.0,
            height or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Rectangle instance'''
        return byref(self)


    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self.x, self.y. self.width, self.height).__getitem__(key)

    def __getattr__(self, attr):
        m = _RECT_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("Rectangle object does not have attribute '{}'.".format(attr))
        cls = {1: float, 4: Rectangle}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _RECT_SET_SWZL.match(attr)
        if not m:
            raise AttributeError("Rectangle object does not have attribute '{}'.".format(attr))
        if attr in ('width', 'height') or len(attr) == 1:
            super(Rectangle, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Rectangle, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Rectangle's components'''
        return {'x': self.x, 'y': self.y, 'w': self.width, 'h': self.height}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Rectangle's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.width = float(d.get('w', self.width))
        self.height = float(d.get('h', self.height))



# Pointer type to Rectangles
RectanglePtr = POINTER(Rectangle)



class Image(Structure):
    '''Image, pixel data stored in CPU memory (RAM)'''
    _fields_ = [
        ('data', VoidPtr),
        ('width', Int),
        ('height', Int),
        ('mipmaps', Int),
        ('format', Int),
    ]


    @classmethod
    def array_of(cls, image_sequence):
        '''Creates and returns an array of Images'''
        arr = cls * len(image_sequence)
        return arr(*image_sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Union[str, CharPtr]) -> Image
        """Load image from file into CPU memory (RAM)"""
        result = _LoadImage(_str_in(file_name))
        return result

    @classmethod
    def load_raw(cls, file_name, width, height, format, header_size):
        # type: (Union[str, CharPtr], int, int, int, int) -> Image
        """Load image from RAW file data"""
        result = _LoadImageRaw(_str_in(file_name), int(width), int(height), int(format), int(header_size))
        return result

    @classmethod
    def load_anim(cls, file_name, frames):
        # type: (Union[str, CharPtr], Union[Seq[int], IntPtr]) -> Image
        """Load image sequence from file (frames appended to image.data)"""
        result = _LoadImageAnim(_str_in(file_name), frames)
        return result

    @classmethod
    def load_from_memory(cls, file_type, file_data, data_size):
        # type: (Union[str, CharPtr], Union[Seq[int], UCharPtr], int) -> Image
        """Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
        result = _LoadImageFromMemory(_str_in(file_type), _str_in(file_data), int(data_size))
        return result

    @classmethod
    def load_from_texture(cls, texture):
        # type: (Texture2D) -> Image
        """Load image from GPU texture data"""
        result = _LoadImageFromTexture(texture)
        return result

    @classmethod
    def load_from_screen():
        # type: () -> Image
        """Load image from screen buffer and (screenshot)"""
        result = _LoadImageFromScreen()
        return result

    @classmethod
    def gen_color(cls, width, height, color):
        # type: (int, int, Color) -> Image
        """Generate image: plain color"""
        result = _GenImageColor(int(width), int(height), _color(color))
        return result

    @classmethod
    def gen_gradient_h(cls, width, height, left, right):
        # type: (int, int, Color, Color) -> Image
        """Generate image: horizontal gradient"""
        result = _GenImageGradientH(int(width), int(height), _color(left), _color(right))
        return result

    @classmethod
    def gen_gradient_v(cls, width, height, top, bottom):
        # type: (int, int, Color, Color) -> Image
        """Generate image: vertical gradient"""
        result = _GenImageGradientV(int(width), int(height), _color(top), _color(bottom))
        return result

    @classmethod
    def gen_gradient_radial(cls, width, height, density, inner, outer):
        # type: (int, int, float, Color, Color) -> Image
        """Generate image: radial gradient"""
        result = _GenImageGradientRadial(int(width), int(height), float(density), _color(inner), _color(outer))
        return result

    @classmethod
    def gen_checked(cls, width, height, checks_x, checks_y, col1, col2):
        # type: (int, int, int, int, Color, Color) -> Image
        """Generate image: checked"""
        result = _GenImageChecked(int(width), int(height), int(checks_x), int(checks_y), _color(col1), _color(col2))
        return result

    @classmethod
    def gen_white_noise(cls, width, height, factor):
        # type: (int, int, float) -> Image
        """Generate image: white noise"""
        result = _GenImageWhiteNoise(int(width), int(height), float(factor))
        return result

    @classmethod
    def gen_cellular(cls, width, height, tile_size):
        # type: (int, int, int) -> Image
        """Generate image: cellular algorithm, bigger tileSize means bigger cells"""
        result = _GenImageCellular(int(width), int(height), int(tile_size))
        return result

    @classmethod
    def from_image(cls, image, rec):
        # type: (Image, Rectangle) -> Image
        """Create an image from another image piece"""
        result = _ImageFromImage(image, _rect(rec))
        return result

    @classmethod
    def text(cls, text, font_size, color):
        # type: (Union[str, CharPtr], int, Color) -> Image
        """Create an image from text (default font)"""
        result = _ImageText(_str_in(text), int(font_size), _color(color))
        return result

    @classmethod
    def text_ex(cls, font, text, font_size, spacing, tint):
        # type: (Font, Union[str, CharPtr], float, float, Color) -> Image
        """Create an image from text (custom sprite font)"""
        result = _ImageTextEx(font, _str_in(text), float(font_size), float(spacing), _color(tint))
        return result


    def __init__(self, data=None,
                 width=None,
                 height=None,
                 mipmaps=None,
                 format=None):
        # type: (bytes, int, int, int, int) -> None
        '''Initializes this Image struct'''
        super(Image, self).__init__(
            data,
            width or 0,
            height or 0,
            mipmaps or 0,
            format or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Image instance'''
        return byref(self)


    def unload(self):
        # type: (Image) -> None
        """Unload image from CPU memory (RAM)"""
        _UnloadImage(self)

    def export(self, file_name):
        # type: (Image, Union[str, CharPtr]) -> bool
        """Export image data to file, returns true on success"""
        result = _ExportImage(self, _str_in(file_name))
        return result

    def export_as_code(self, file_name):
        # type: (Image, Union[str, CharPtr]) -> bool
        """Export image as code file defining an array of bytes, returns true on success"""
        result = _ExportImageAsCode(self, _str_in(file_name))
        return result

    def copy(self):
        # type: (Image) -> Image
        """Create an image duplicate (useful for transformations)"""
        result = _ImageCopy(self)
        return result

    def format(self, new_format):
        # type: (ImagePtr, int) -> None
        """Convert image data to desired format"""
        _ImageFormat(self.byref, int(new_format))

    def to_pot(self, fill):
        # type: (ImagePtr, Color) -> None
        """Convert image to POT (power-of-two)"""
        _ImageToPOT(self.byref, _color(fill))

    def crop(self, crop):
        # type: (ImagePtr, Rectangle) -> None
        """Crop an image to a defined rectangle"""
        _ImageCrop(self.byref, _rect(crop))

    def alpha_crop(self, threshold):
        # type: (ImagePtr, float) -> None
        """Crop image depending on alpha value"""
        _ImageAlphaCrop(self.byref, float(threshold))

    def alpha_clear(self, color, threshold):
        # type: (ImagePtr, Color, float) -> None
        """Clear alpha channel to desired color"""
        _ImageAlphaClear(self.byref, _color(color), float(threshold))

    def alpha_mask(self, alpha_mask):
        # type: (ImagePtr, Image) -> None
        """Apply alpha mask to image"""
        _ImageAlphaMask(self.byref, alpha_mask)

    def alpha_premultiply(self):
        # type: (ImagePtr) -> None
        """Premultiply alpha channel"""
        _ImageAlphaPremultiply(self.byref)

    def resize(self, new_width, new_height):
        # type: (ImagePtr, int, int) -> None
        """Resize image (Bicubic scaling algorithm)"""
        _ImageResize(self.byref, int(new_width), int(new_height))

    def resize_nn(self, new_width, new_height):
        # type: (ImagePtr, int, int) -> None
        """Resize image (Nearest-Neighbor scaling algorithm)"""
        _ImageResizeNN(self.byref, int(new_width), int(new_height))

    def resize_canvas(self, new_width, new_height, offset_x, offset_y, fill):
        # type: (ImagePtr, int, int, int, int, Color) -> None
        """Resize canvas and fill with color"""
        _ImageResizeCanvas(self.byref, int(new_width), int(new_height), int(offset_x), int(offset_y), _color(fill))

    def mipmaps(self):
        # type: (ImagePtr) -> None
        """Compute all mipmap levels for a provided image"""
        _ImageMipmaps(self.byref)

    def dither(self, r_bpp, g_bpp, b_bpp, a_bpp):
        # type: (ImagePtr, int, int, int, int) -> None
        """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
        _ImageDither(self.byref, int(r_bpp), int(g_bpp), int(b_bpp), int(a_bpp))

    def flip_vertical(self):
        # type: (ImagePtr) -> None
        """Flip image vertically"""
        _ImageFlipVertical(self.byref)

    def flip_horizontal(self):
        # type: (ImagePtr) -> None
        """Flip image horizontally"""
        _ImageFlipHorizontal(self.byref)

    def rotate_cw(self):
        # type: (ImagePtr) -> None
        """Rotate image clockwise 90deg"""
        _ImageRotateCW(self.byref)

    def rotate_ccw(self):
        # type: (ImagePtr) -> None
        """Rotate image counter-clockwise 90deg"""
        _ImageRotateCCW(self.byref)

    def color_tint(self, color):
        # type: (ImagePtr, Color) -> None
        """Modify image color: tint"""
        _ImageColorTint(self.byref, _color(color))

    def color_invert(self):
        # type: (ImagePtr) -> None
        """Modify image color: invert"""
        _ImageColorInvert(self.byref)

    def color_grayscale(self):
        # type: (ImagePtr) -> None
        """Modify image color: grayscale"""
        _ImageColorGrayscale(self.byref)

    def color_contrast(self, contrast):
        # type: (ImagePtr, float) -> None
        """Modify image color: contrast (-100 to 100)"""
        _ImageColorContrast(self.byref, float(contrast))

    def color_brightness(self, brightness):
        # type: (ImagePtr, int) -> None
        """Modify image color: brightness (-255 to 255)"""
        _ImageColorBrightness(self.byref, int(brightness))

    def color_replace(self, color, replace):
        # type: (ImagePtr, Color, Color) -> None
        """Modify image color: replace color"""
        _ImageColorReplace(self.byref, _color(color), _color(replace))

    def clear_background(self, color):
        # type: (ImagePtr, Color) -> None
        """Clear image background with given color"""
        _ImageClearBackground(self.byref, _color(color))

    def draw_pixel(self, pos_x, pos_y, color):
        # type: (ImagePtr, int, int, Color) -> None
        """Draw pixel within an image"""
        _ImageDrawPixel(self.byref, int(pos_x), int(pos_y), _color(color))

    def draw_pixel_v(self, position, color):
        # type: (ImagePtr, Vector2, Color) -> None
        """Draw pixel within an image (Vector version)"""
        _ImageDrawPixelV(self.byref, _vec2(position), _color(color))

    def draw_line(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y, color):
        # type: (ImagePtr, int, int, int, int, Color) -> None
        """Draw line within an image"""
        _ImageDrawLine(self.byref, int(start_pos_x), int(start_pos_y), int(end_pos_x), int(end_pos_y), _color(color))

    def draw_line_v(self, start, end, color):
        # type: (ImagePtr, Vector2, Vector2, Color) -> None
        """Draw line within an image (Vector version)"""
        _ImageDrawLineV(self.byref, _vec2(start), _vec2(end), _color(color))

    def draw_circle(self, center_x, center_y, radius, color):
        # type: (ImagePtr, int, int, int, Color) -> None
        """Draw circle within an image"""
        _ImageDrawCircle(self.byref, int(center_x), int(center_y), int(radius), _color(color))

    def draw_circle_v(self, center, radius, color):
        # type: (ImagePtr, Vector2, int, Color) -> None
        """Draw circle within an image (Vector version)"""
        _ImageDrawCircleV(self.byref, _vec2(center), int(radius), _color(color))

    def draw_rectangle(self, pos_x, pos_y, width, height, color):
        # type: (ImagePtr, int, int, int, int, Color) -> None
        """Draw rectangle within an image"""
        _ImageDrawRectangle(self.byref, int(pos_x), int(pos_y), int(width), int(height), _color(color))

    def draw_rectangle_v(self, position, size, color):
        # type: (ImagePtr, Vector2, Vector2, Color) -> None
        """Draw rectangle within an image (Vector version)"""
        _ImageDrawRectangleV(self.byref, _vec2(position), _vec2(size), _color(color))

    def draw_rectangle_rec(self, rec, color):
        # type: (ImagePtr, Rectangle, Color) -> None
        """Draw rectangle within an image"""
        _ImageDrawRectangleRec(self.byref, _rect(rec), _color(color))

    def draw_rectangle_lines(self, rec, thick, color):
        # type: (ImagePtr, Rectangle, int, Color) -> None
        """Draw rectangle lines within an image"""
        _ImageDrawRectangleLines(self.byref, _rect(rec), int(thick), _color(color))

    def draw(self, src, src_rec, dst_rec, tint):
        # type: (ImagePtr, Image, Rectangle, Rectangle, Color) -> None
        """Draw a source image within a destination image (tint applied to source)"""
        _ImageDraw(self.byref, src, _rect(src_rec), _rect(dst_rec), _color(tint))

    def draw_text(self, text, pos_x, pos_y, font_size, color):
        # type: (ImagePtr, Union[str, CharPtr], int, int, int, Color) -> None
        """Draw text (using default font) within an image (destination)"""
        _ImageDrawText(self.byref, _str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))

    def draw_text_ex(self, font, text, position, font_size, spacing, tint):
        # type: (ImagePtr, Font, Union[str, CharPtr], Vector2, float, float, Color) -> None
        """Draw text (custom sprite font) within an image (destination)"""
        _ImageDrawTextEx(self.byref, font, _str_in(text), _vec2(position), float(font_size), float(spacing), _color(tint))

    def load_colors(self):
        # type: (Image) -> ColorPtr
        """Load color data from image as a Color array (RGBA - 32bit)"""
        result = _ptr_out(_LoadImageColors(self))
        return result

    def load_palette(self, max_palette_size):
        # type: (Image, int) -> ColorPtr
        """Load colors palette from image as a Color array (RGBA - 32bit)"""
        color_count = Int(0)
        result = _ptr_out(_LoadImagePalette(self, int(max_palette_size), byref(color_count)), color_count.value)
        return result

    def get_alpha_border(self, threshold):
        # type: (Image, float) -> Rectangle
        """Get image alpha border rectangle"""
        result = _GetImageAlphaBorder(self, float(threshold))
        return result

    def get_color(self, x, y):
        # type: (Image, int, int) -> Color
        """Get image pixel color at (x, y) position"""
        result = _GetImageColor(self, int(x), int(y))
        return result

    @staticmethod
    def unload_colors(colors):
        # type: (ColorPtr) -> None
        """Unload color data loaded with LoadImageColors()"""
        _UnloadImageColors(_color(colors))

    @staticmethod
    def unload_palette(colors):
        # type: (ColorPtr) -> None
        """Unload colors palette loaded with LoadImagePalette()"""
        _UnloadImagePalette(_color(colors))


# Pointer type to Images
ImagePtr = POINTER(Image)



class Texture(Structure):
    '''Texture, tex data stored in GPU memory (VRAM)'''
    _fields_ = [
        ('id', UInt),
        ('width', Int),
        ('height', Int),
        ('mipmaps', Int),
        ('format', Int),
    ]


    @classmethod
    def array_of(cls, texture_sequence):
        '''Creates and returns an array of Textures'''
        arr = cls * len(texture_sequence)
        return arr(*texture_sequence)


    def __init__(self, id=None,
                 width=None,
                 height=None,
                 mipmaps=None,
                 format=None):
        # type: (int, int, int, int, int) -> None
        '''Initializes this Texture struct'''
        super(Texture, self).__init__(
            id or 0,
            width or 0,
            height or 0,
            mipmaps or 0,
            format or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Texture instance'''
        return byref(self)



# Pointer type to Textures
TexturePtr = POINTER(Texture)


# Texture2D, same as Texture
Texture2D = Texture
Texture2DPtr = TexturePtr
# TextureCubemap, same as Texture
TextureCubemap = Texture
TextureCubemapPtr = TexturePtr

class RenderTexture(Structure):
    '''RenderTexture, fbo for texture rendering'''
    _fields_ = [
        ('id', UInt),
        ('texture', Texture),
        ('depth', Texture),
    ]


    @classmethod
    def array_of(cls, render_texture_sequence):
        '''Creates and returns an array of RenderTextures'''
        arr = cls * len(render_texture_sequence)
        return arr(*render_texture_sequence)


    def __init__(self, id=None, texture=None, depth=None):
        # type: (int, Texture, Texture) -> None
        '''Initializes this RenderTexture struct'''
        super(RenderTexture, self).__init__(
            id or 0,
            texture or Texture(),
            depth or Texture()
        )


    @property
    def byref(self):
        '''Gets a reference to this RenderTexture instance'''
        return byref(self)



# Pointer type to RenderTextures
RenderTexturePtr = POINTER(RenderTexture)


# RenderTexture2D, same as RenderTexture
RenderTexture2D = RenderTexture
RenderTexture2DPtr = RenderTexturePtr

class NPatchInfo(Structure):
    '''NPatchInfo, n-patch layout info'''
    _fields_ = [
        ('source', Rectangle),
        ('left', Int),
        ('top', Int),
        ('right', Int),
        ('bottom', Int),
        ('layout', Int),
    ]


    @classmethod
    def array_of(cls, npatch_info_sequence):
        '''Creates and returns an array of NPatchInfos'''
        arr = cls * len(npatch_info_sequence)
        return arr(*npatch_info_sequence)


    def __init__(self, source=None,
                 left=None,
                 top=None,
                 right=None,
                 bottom=None,
                 layout=None):
        # type: (Rectangle, int, int, int, int, int) -> None
        '''Initializes this NPatchInfo struct'''
        super(NPatchInfo, self).__init__(
            source or Rectangle(),
            left or 0,
            top or 0,
            right or 0,
            bottom or 0,
            layout or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this NPatchInfo instance'''
        return byref(self)



# Pointer type to NPatchInfos
NPatchInfoPtr = POINTER(NPatchInfo)



class GlyphInfo(Structure):
    '''GlyphInfo, font characters glyphs info'''
    _fields_ = [
        ('value', Int),
        ('offset_x', Int),
        ('offset_y', Int),
        ('advance_x', Int),
        ('image', Image),
    ]


    @classmethod
    def array_of(cls, glyph_info_sequence):
        '''Creates and returns an array of GlyphInfos'''
        arr = cls * len(glyph_info_sequence)
        return arr(*glyph_info_sequence)


    def __init__(self, value=None,
                 offset_x=None,
                 offset_y=None,
                 advance_x=None,
                 image=None):
        # type: (int, int, int, int, Image) -> None
        '''Initializes this GlyphInfo struct'''
        super(GlyphInfo, self).__init__(
            value or 0,
            offset_x or 0,
            offset_y or 0,
            advance_x or 0,
            image or Image()
        )


    @property
    def byref(self):
        '''Gets a reference to this GlyphInfo instance'''
        return byref(self)



# Pointer type to GlyphInfos
GlyphInfoPtr = POINTER(GlyphInfo)



class Font(Structure):
    '''Font, font texture and GlyphInfo array data'''
    _fields_ = [
        ('base_size', Int),
        ('glyph_count', Int),
        ('glyph_padding', Int),
        ('texture', Texture2D),
        ('recs', RectanglePtr),
        ('glyphs', GlyphInfoPtr),
    ]


    @classmethod
    def array_of(cls, font_sequence):
        '''Creates and returns an array of Fonts'''
        arr = cls * len(font_sequence)
        return arr(*font_sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Union[str, CharPtr]) -> Font
        """Load font from file into GPU memory (VRAM)"""
        result = _LoadFont(_str_in(file_name))
        return result

    @classmethod
    def load_ex(cls, file_name, font_size, font_chars, glyph_count):
        # type: (Union[str, CharPtr], int, Union[Seq[int], IntPtr], int) -> Font
        """Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set"""
        result = _LoadFontEx(_str_in(file_name), int(font_size), font_chars, int(glyph_count))
        return result

    @classmethod
    def load_from_image(cls, image, key, first_char):
        # type: (Image, Color, int) -> Font
        """Load font from Image (XNA style)"""
        result = _LoadFontFromImage(image, _color(key), int(first_char))
        return result

    @classmethod
    def load_from_memory(cls, file_type, file_data, data_size, font_size, font_chars, glyph_count):
        # type: (Union[str, CharPtr], Union[Seq[int], UCharPtr], int, int, Union[Seq[int], IntPtr], int) -> Font
        """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
        result = _LoadFontFromMemory(_str_in(file_type), _str_in(file_data), int(data_size), int(font_size), font_chars, int(glyph_count))
        return result


    def __init__(self, base_size=None,
                 glyph_count=None,
                 glyph_padding=None,
                 texture=None,
                 recs=None,
                 glyphs=None):
        # type: (int, int, int, Texture2D, RectanglePtr, GlyphInfoPtr) -> None
        '''Initializes this Font struct'''
        super(Font, self).__init__(
            base_size or 0,
            glyph_count or 0,
            glyph_padding or 0,
            texture or Texture2D(),
            recs,
            glyphs
        )


    @property
    def byref(self):
        '''Gets a reference to this Font instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def unload(self):
        # type: (Font) -> None
        """Unload font from GPU memory (VRAM)"""
        _UnloadFont(self)

    def draw_text_ex(self, text, position, font_size, spacing, tint):
        # type: (Font, Union[str, CharPtr], Vector2, float, float, Color) -> None
        """Draw text using font and additional parameters"""
        _DrawTextEx(self, _str_in(text), _vec2(position), float(font_size), float(spacing), _color(tint))

    def draw_text_pro(self, text, position, origin, rotation, font_size, spacing, tint):
        # type: (Font, Union[str, CharPtr], Vector2, Vector2, float, float, float, Color) -> None
        """Draw text using Font and pro parameters (rotation)"""
        _DrawTextPro(self, _str_in(text), _vec2(position), _vec2(origin), float(rotation), float(font_size), float(spacing), _color(tint))

    def draw_text_codepoint(self, codepoint, position, font_size, tint):
        # type: (Font, int, Vector2, float, Color) -> None
        """Draw one character (codepoint)"""
        _DrawTextCodepoint(self, int(codepoint), _vec2(position), float(font_size), _color(tint))

    def draw_text_codepoints(self, codepoints, position, font_size, spacing, tint):
        # type: (Font, Union[Seq[int], IntPtr], Vector2, float, float, Color) -> None
        """Draw multiple character (codepoint)"""
        _DrawTextCodepoints(self, _str_in(codepoints), len(codepoints), _vec2(position), float(font_size), float(spacing), _color(tint))

    def measure_text_ex(self, text, font_size, spacing):
        # type: (Font, Union[str, CharPtr], float, float) -> Vector2
        """Measure string size for Font"""
        result = _MeasureTextEx(self, _str_in(text), float(font_size), float(spacing))
        return result

    def get_glyph_index(self, codepoint):
        # type: (Font, int) -> int
        """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
        result = _GetGlyphIndex(self, int(codepoint))
        return result

    def get_glyph_info(self, codepoint):
        # type: (Font, int) -> GlyphInfo
        """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
        result = _GetGlyphInfo(self, int(codepoint))
        return result

    def get_glyph_atlas_rec(self, codepoint):
        # type: (Font, int) -> Rectangle
        """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
        result = _GetGlyphAtlasRec(self, int(codepoint))
        return result

    @staticmethod
    def load_data(file_data, data_size, font_size, font_chars, glyph_count, type):
        # type: (Union[Seq[int], UCharPtr], int, int, Union[Seq[int], IntPtr], int, int) -> GlyphInfoPtr
        """Load font data for further use"""
        result = _ptr_out(_LoadFontData(_str_in(file_data), int(data_size), int(font_size), font_chars, int(glyph_count), int(type)))
        return result

    @staticmethod
    def unload_data(chars, glyph_count):
        # type: (GlyphInfoPtr, int) -> None
        """Unload font chars info data (RAM)"""
        _UnloadFontData(chars, int(glyph_count))


# Pointer type to Fonts
FontPtr = POINTER(Font)



class Camera3D(Structure):
    '''Camera, defines position/orientation in 3d space'''
    _fields_ = [
        ('position', Vector3),
        ('target', Vector3),
        ('up', Vector3),
        ('fovy', Float),
        ('projection', Int),
    ]


    @classmethod
    def array_of(cls, camera3d_sequence):
        '''Creates and returns an array of Camera3Ds'''
        arr = cls * len(camera3d_sequence)
        return arr(*camera3d_sequence)


    def __init__(self, position=None,
                 target=None,
                 up=None,
                 fovy=None,
                 projection=None):
        # type: (Vector3, Vector3, Vector3, float, int) -> None
        '''Initializes this Camera3D struct'''
        super(Camera3D, self).__init__(
            position or Vector3(),
            target or Vector3(),
            up or Vector3(),
            fovy or 0.0,
            projection or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Camera3D instance'''
        return byref(self)


    def __enter__(self):
        _BeginMode3D(self)

    def __leave__(self, exc_type, exc_value, traceback):
        _EndMode3D()

    def set_mode(self, mode):
        # type: (Camera, int) -> None
        """Set camera mode (multiple camera modes available)"""
        _SetCameraMode(self, int(mode))


# Pointer type to Camera3Ds
Camera3DPtr = POINTER(Camera3D)


# Camera type fallback, defaults to Camera3D
Camera = Camera3D
CameraPtr = Camera3DPtr

class Camera2D(Structure):
    '''Camera2D, defines position/orientation in 2d space'''
    _fields_ = [
        ('offset', Vector2),
        ('target', Vector2),
        ('rotation', Float),
        ('zoom', Float),
    ]


    @classmethod
    def array_of(cls, camera2d_sequence):
        '''Creates and returns an array of Camera2Ds'''
        arr = cls * len(camera2d_sequence)
        return arr(*camera2d_sequence)


    def __init__(self, offset=None, target=None, rotation=None, zoom=None):
        # type: (Vector2, Vector2, float, float) -> None
        '''Initializes this Camera2D struct'''
        super(Camera2D, self).__init__(
            offset or Vector2(),
            target or Vector2(),
            rotation or 0.0,
            zoom or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Camera2D instance'''
        return byref(self)


    def __enter__(self):
        _BeginMode2D(self)

    def __leave__(self, exc_type, exc_value, traceback):
        _EndMode2D()


# Pointer type to Camera2Ds
Camera2DPtr = POINTER(Camera2D)



class Mesh(Structure):
    '''Mesh, vertex data and vao/vbo'''
    _fields_ = [
        ('vertex_count', Int),
        ('triangle_count', Int),
        ('vertices', FloatPtr),
        ('texcoords', FloatPtr),
        ('texcoords2', FloatPtr),
        ('normals', FloatPtr),
        ('tangents', FloatPtr),
        ('colors', UCharPtr),
        ('indices', UShortPtr),
        ('anim_vertices', FloatPtr),
        ('anim_normals', FloatPtr),
        ('bone_ids', UCharPtr),
        ('bone_weights', FloatPtr),
        ('vao_id', UInt),
        ('vbo_id', UIntPtr),
    ]


    @classmethod
    def array_of(cls, mesh_sequence):
        '''Creates and returns an array of Meshs'''
        arr = cls * len(mesh_sequence)
        return arr(*mesh_sequence)

    @classmethod
    def gen_poly(cls, sides, radius):
        # type: (int, float) -> Mesh
        """Generate polygonal mesh"""
        result = _GenMeshPoly(int(sides), float(radius))
        return result

    @classmethod
    def gen_plane(cls, width, length, res_x, res_z):
        # type: (float, float, int, int) -> Mesh
        """Generate plane mesh (with subdivisions)"""
        result = _GenMeshPlane(float(width), float(length), int(res_x), int(res_z))
        return result

    @classmethod
    def gen_cube(cls, width, height, length):
        # type: (float, float, float) -> Mesh
        """Generate cuboid mesh"""
        result = _GenMeshCube(float(width), float(height), float(length))
        return result

    @classmethod
    def gen_sphere(cls, radius, rings, slices):
        # type: (float, int, int) -> Mesh
        """Generate sphere mesh (standard sphere)"""
        result = _GenMeshSphere(float(radius), int(rings), int(slices))
        return result

    @classmethod
    def gen_hemi_sphere(cls, radius, rings, slices):
        # type: (float, int, int) -> Mesh
        """Generate half-sphere mesh (no bottom cap)"""
        result = _GenMeshHemiSphere(float(radius), int(rings), int(slices))
        return result

    @classmethod
    def gen_cylinder(cls, radius, height, slices):
        # type: (float, float, int) -> Mesh
        """Generate cylinder mesh"""
        result = _GenMeshCylinder(float(radius), float(height), int(slices))
        return result

    @classmethod
    def gen_cone(cls, radius, height, slices):
        # type: (float, float, int) -> Mesh
        """Generate cone/pyramid mesh"""
        result = _GenMeshCone(float(radius), float(height), int(slices))
        return result

    @classmethod
    def gen_torus(cls, radius, size, rad_seg, sides):
        # type: (float, float, int, int) -> Mesh
        """Generate torus mesh"""
        result = _GenMeshTorus(float(radius), float(size), int(rad_seg), int(sides))
        return result

    @classmethod
    def gen_knot(cls, radius, size, rad_seg, sides):
        # type: (float, float, int, int) -> Mesh
        """Generate trefoil knot mesh"""
        result = _GenMeshKnot(float(radius), float(size), int(rad_seg), int(sides))
        return result

    @classmethod
    def gen_heightmap(cls, heightmap, size):
        # type: (Image, Vector3) -> Mesh
        """Generate heightmap mesh from image data"""
        result = _GenMeshHeightmap(heightmap, _vec3(size))
        return result

    @classmethod
    def gen_cubicmap(cls, cubicmap, cube_size):
        # type: (Image, Vector3) -> Mesh
        """Generate cubes-based map mesh from image data"""
        result = _GenMeshCubicmap(cubicmap, _vec3(cube_size))
        return result


    def __init__(self, vertex_count=None,
                 triangle_count=None,
                 vertices=None,
                 texcoords=None,
                 texcoords2=None,
                 normals=None,
                 tangents=None,
                 colors=None,
                 indices=None,
                 anim_vertices=None,
                 anim_normals=None,
                 bone_ids=None,
                 bone_weights=None,
                 vao_id=None,
                 vbo_id=None):
        # type: (int, int, Union[Seq[float], FloatPtr], Union[Seq[float], FloatPtr], Union[Seq[float], FloatPtr], Union[Seq[float], FloatPtr], Union[Seq[float], FloatPtr], Union[Seq[int], UCharPtr], Union[Seq[int], UShortPtr], Union[Seq[float], FloatPtr], Union[Seq[float], FloatPtr], Union[Seq[int], UCharPtr], Union[Seq[float], FloatPtr], int, Union[Seq[int], UIntPtr]) -> None
        '''Initializes this Mesh struct'''
        super(Mesh, self).__init__(
            vertex_count or 0,
            triangle_count or 0,
            vertices,
            texcoords,
            texcoords2,
            normals,
            tangents,
            colors,
            indices,
            anim_vertices,
            anim_normals,
            bone_ids,
            bone_weights,
            vao_id or 0,
            vbo_id
        )


    @property
    def byref(self):
        '''Gets a reference to this Mesh instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def upload(self, dynamic):
        # type: (MeshPtr, bool) -> None
        """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
        _UploadMesh(self.byref, bool(dynamic))

    def update_buffer(self, index, data, data_size, offset):
        # type: (Mesh, int, bytes, int, int) -> None
        """Update mesh vertex data in GPU for a specific buffer index"""
        _UpdateMeshBuffer(self, int(index), data, int(data_size), int(offset))

    def unload(self):
        # type: (Mesh) -> None
        """Unload mesh data from CPU and GPU"""
        _UnloadMesh(self)

    def draw(self, material, transform):
        # type: (Mesh, Material, Matrix) -> None
        """Draw a 3d mesh with material and transform"""
        _DrawMesh(self, material, transform)

    def draw_instanced(self, material, transforms, instances):
        # type: (Mesh, Material, MatrixPtr, int) -> None
        """Draw multiple mesh instances with material and different transforms"""
        _DrawMeshInstanced(self, material, transforms, int(instances))

    def export(self, file_name):
        # type: (Mesh, Union[str, CharPtr]) -> bool
        """Export mesh data to file, returns true on success"""
        result = _ExportMesh(self, _str_in(file_name))
        return result

    def get_bounding_box(self):
        # type: (Mesh) -> BoundingBox
        """Compute mesh bounding box limits"""
        result = _GetMeshBoundingBox(self)
        return result

    def gen_tangents(self):
        # type: (MeshPtr) -> None
        """Compute mesh tangents"""
        _GenMeshTangents(self.byref)


# Pointer type to Meshs
MeshPtr = POINTER(Mesh)



class Shader(Structure):
    '''Shader'''
    _fields_ = [
        ('id', UInt),
        ('locs', IntPtr),
    ]


    @classmethod
    def array_of(cls, shader_sequence):
        '''Creates and returns an array of Shaders'''
        arr = cls * len(shader_sequence)
        return arr(*shader_sequence)

    @classmethod
    def load(cls, vs_file_name, fs_file_name):
        # type: (Union[str, CharPtr], Union[str, CharPtr]) -> Shader
        """Load shader from files and bind default locations"""
        result = _LoadShader(_str_in(vs_file_name), _str_in(fs_file_name))
        return result

    @classmethod
    def load_from_memory(cls, vs_code, fs_code):
        # type: (Union[str, CharPtr], Union[str, CharPtr]) -> Shader
        """Load shader from code strings and bind default locations"""
        result = _LoadShaderFromMemory(_str_in(vs_code), _str_in(fs_code))
        return result


    def __init__(self, id=None, locs=None):
        # type: (int, Union[Seq[int], IntPtr]) -> None
        '''Initializes this Shader struct'''
        super(Shader, self).__init__(
            id or 0,
            locs
        )


    @property
    def byref(self):
        '''Gets a reference to this Shader instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def __enter__(self):
        _BeginShaderMode(self)

    def __leave__(self, exc_type, exc_value, traceback):
        _EndShaderMode()

    def get_location(self, uniform_name):
        # type: (Shader, Union[str, CharPtr]) -> int
        """Get shader uniform location"""
        result = _GetShaderLocation(self, _str_in(uniform_name))
        return result

    def get_location_attrib(self, attrib_name):
        # type: (Shader, Union[str, CharPtr]) -> int
        """Get shader attribute location"""
        result = _GetShaderLocationAttrib(self, _str_in(attrib_name))
        return result

    def set_value(self, loc_index, value, uniform_type):
        # type: (Shader, int, bytes, int) -> None
        """Set shader uniform value"""
        _SetShaderValue(self, int(loc_index), value, int(uniform_type))

    def set_value_v(self, loc_index, value, uniform_type, count):
        # type: (Shader, int, bytes, int, int) -> None
        """Set shader uniform value vector"""
        _SetShaderValueV(self, int(loc_index), value, int(uniform_type), int(count))

    def set_value_matrix(self, loc_index, mat):
        # type: (Shader, int, Matrix) -> None
        """Set shader uniform value (matrix 4x4)"""
        _SetShaderValueMatrix(self, int(loc_index), mat)

    def set_value_texture(self, loc_index, texture):
        # type: (Shader, int, Texture2D) -> None
        """Set shader uniform value for texture (sampler2d)"""
        _SetShaderValueTexture(self, int(loc_index), texture)

    def unload(self):
        # type: (Shader) -> None
        """Unload shader from GPU memory (VRAM)"""
        _UnloadShader(self)


# Pointer type to Shaders
ShaderPtr = POINTER(Shader)



class MaterialMap(Structure):
    '''MaterialMap'''
    _fields_ = [
        ('texture', Texture2D),
        ('color', Color),
        ('value', Float),
    ]


    @classmethod
    def array_of(cls, material_map_sequence):
        '''Creates and returns an array of MaterialMaps'''
        arr = cls * len(material_map_sequence)
        return arr(*material_map_sequence)


    def __init__(self, texture=None, color=None, value=None):
        # type: (Texture2D, Color, float) -> None
        '''Initializes this MaterialMap struct'''
        super(MaterialMap, self).__init__(
            texture or Texture2D(),
            color or Color(),
            value or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this MaterialMap instance'''
        return byref(self)



# Pointer type to MaterialMaps
MaterialMapPtr = POINTER(MaterialMap)



class Material(Structure):
    '''Material, includes shader and maps'''
    _fields_ = [
        ('shader', Shader),
        ('maps', MaterialMapPtr),
        ('params', Float * 4),
    ]


    @classmethod
    def array_of(cls, material_sequence):
        '''Creates and returns an array of Materials'''
        arr = cls * len(material_sequence)
        return arr(*material_sequence)

    @classmethod
    def load_materials(cls, file_name):
        # type: (Union[str, CharPtr]) -> MaterialPtr
        """Load materials from model file"""
        material_count = Int(0)
        result = _ptr_out(_LoadMaterials(_str_in(file_name), byref(material_count)), material_count.value)
        return result

    @classmethod
    def load_default():
        # type: () -> Material
        """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
        result = _LoadMaterialDefault()
        return result


    def __init__(self, shader=None, maps=None, params=None):
        # type: (Shader, MaterialMapPtr, Seq[float]) -> None
        '''Initializes this Material struct'''
        super(Material, self).__init__(
            shader or Shader(),
            maps,
            params
        )


    @property
    def byref(self):
        '''Gets a reference to this Material instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def unload(self):
        # type: (Material) -> None
        """Unload material from GPU memory (VRAM)"""
        _UnloadMaterial(self)

    def set_texture(self, map_type, texture):
        # type: (MaterialPtr, int, Texture2D) -> None
        """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
        _SetMaterialTexture(self, int(map_type), texture)


# Pointer type to Materials
MaterialPtr = POINTER(Material)



class Transform(Structure):
    '''Transform, vectex transformation data'''
    _fields_ = [
        ('translation', Vector3),
        ('rotation', Quaternion),
        ('scale', Vector3),
    ]


    @classmethod
    def array_of(cls, transform_sequence):
        '''Creates and returns an array of Transforms'''
        arr = cls * len(transform_sequence)
        return arr(*transform_sequence)


    def __init__(self, translation=None, rotation=None, scale=None):
        # type: (Vector3, Quaternion, Vector3) -> None
        '''Initializes this Transform struct'''
        super(Transform, self).__init__(
            translation or Vector3(),
            rotation or Quaternion(),
            scale or Vector3()
        )


    @property
    def byref(self):
        '''Gets a reference to this Transform instance'''
        return byref(self)



# Pointer type to Transforms
TransformPtr = POINTER(Transform)



class BoneInfo(Structure):
    '''Bone, skeletal animation bone'''
    _fields_ = [
        ('name', CharPtr),
        ('parent', Int),
    ]


    @classmethod
    def array_of(cls, bone_info_sequence):
        '''Creates and returns an array of BoneInfos'''
        arr = cls * len(bone_info_sequence)
        return arr(*bone_info_sequence)


    def __init__(self, name=None, parent=None):
        # type: (str, int) -> None
        '''Initializes this BoneInfo struct'''
        super(BoneInfo, self).__init__(
            name,
            parent or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this BoneInfo instance'''
        return byref(self)



# Pointer type to BoneInfos
BoneInfoPtr = POINTER(BoneInfo)



class Model(Structure):
    '''Model, meshes, materials and animation data'''
    _fields_ = [
        ('transform', Matrix),
        ('mesh_count', Int),
        ('material_count', Int),
        ('meshes', MeshPtr),
        ('materials', MaterialPtr),
        ('mesh_material', IntPtr),
        ('bone_count', Int),
        ('bones', BoneInfoPtr),
        ('bind_pose', TransformPtr),
    ]


    @classmethod
    def array_of(cls, model_sequence):
        '''Creates and returns an array of Models'''
        arr = cls * len(model_sequence)
        return arr(*model_sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Union[str, CharPtr]) -> Model
        """Load model from files (meshes and materials)"""
        result = _LoadModel(_str_in(file_name))
        return result

    @classmethod
    def load_from_mesh(cls, mesh):
        # type: (Mesh) -> Model
        """Load model from generated mesh (default material)"""
        result = _LoadModelFromMesh(mesh)
        return result


    def __init__(self, transform=None,
                 mesh_count=None,
                 material_count=None,
                 meshes=None,
                 materials=None,
                 mesh_material=None,
                 bone_count=None,
                 bones=None,
                 bind_pose=None):
        # type: (Matrix, int, int, MeshPtr, MaterialPtr, Union[Seq[int], IntPtr], int, BoneInfoPtr, TransformPtr) -> None
        '''Initializes this Model struct'''
        super(Model, self).__init__(
            transform or Matrix(),
            mesh_count or 0,
            material_count or 0,
            meshes,
            materials,
            mesh_material,
            bone_count or 0,
            bones,
            bind_pose
        )


    @property
    def byref(self):
        '''Gets a reference to this Model instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def is_animation_valid(self, anim):
        # type: (Model, ModelAnimation) -> bool
        """Check model animation skeleton match"""
        result = _IsModelAnimationValid(self, anim)
        return result

    def update_animation(self, anim, frame):
        # type: (Model, ModelAnimation, int) -> None
        """Update model animation pose"""
        _UpdateModelAnimation(self, anim, int(frame))

    def set_mesh_material(self, mesh_id, material_id):
        # type: (ModelPtr, int, int) -> None
        """Set material for a mesh"""
        _SetModelMeshMaterial(self.byref, int(mesh_id), int(material_id))

    def unload(self):
        # type: (Model) -> None
        """Unload model (including meshes) from memory (RAM and/or VRAM)"""
        _UnloadModel(self)

    def unload_keep_meshes(self):
        # type: (Model) -> None
        """Unload model (but not meshes) from memory (RAM and/or VRAM)"""
        _UnloadModelKeepMeshes(self)

    def get_bounding_box(self):
        # type: (Model) -> BoundingBox
        """Compute model bounding box limits (considers all meshes)"""
        result = _GetModelBoundingBox(self)
        return result

    def draw(self, position, scale, tint):
        # type: (Model, Vector3, float, Color) -> None
        """Draw a model (with texture if set)"""
        _DrawModel(self, _vec3(position), float(scale), _color(tint))

    def draw_ex(self, position, rotation_axis, rotation_angle, scale, tint):
        # type: (Model, Vector3, Vector3, float, Vector3, Color) -> None
        """Draw a model with extended parameters"""
        _DrawModelEx(self, _vec3(position), _vec3(rotation_axis), float(rotation_angle), _vec3(scale), _color(tint))

    def draw_wires(self, position, scale, tint):
        # type: (Model, Vector3, float, Color) -> None
        """Draw a model wires (with texture if set)"""
        _DrawModelWires(self, _vec3(position), float(scale), _color(tint))

    def draw_wires_ex(self, position, rotation_axis, rotation_angle, scale, tint):
        # type: (Model, Vector3, Vector3, float, Vector3, Color) -> None
        """Draw a model wires (with texture if set) with extended parameters"""
        _DrawModelWiresEx(self, _vec3(position), _vec3(rotation_axis), float(rotation_angle), _vec3(scale), _color(tint))


# Pointer type to Models
ModelPtr = POINTER(Model)



class ModelAnimation(Structure):
    '''ModelAnimation'''
    _fields_ = [
        ('bone_count', Int),
        ('frame_count', Int),
        ('bones', BoneInfoPtr),
        ('frame_poses', TransformPtr),
    ]


    @classmethod
    def array_of(cls, model_animation_sequence):
        '''Creates and returns an array of ModelAnimations'''
        arr = cls * len(model_animation_sequence)
        return arr(*model_animation_sequence)


    def __init__(self, bone_count=None, frame_count=None, bones=None, frame_poses=None):
        # type: (int, int, BoneInfoPtr, TransformPtr) -> None
        '''Initializes this ModelAnimation struct'''
        super(ModelAnimation, self).__init__(
            bone_count or 0,
            frame_count or 0,
            bones,
            frame_poses
        )


    @property
    def byref(self):
        '''Gets a reference to this ModelAnimation instance'''
        return byref(self)



# Pointer type to ModelAnimations
ModelAnimationPtr = POINTER(ModelAnimation)



class Ray(Structure):
    '''Ray, ray for raycasting'''
    _fields_ = [
        ('position', Vector3),
        ('direction', Vector3),
    ]


    @classmethod
    def array_of(cls, ray_sequence):
        '''Creates and returns an array of Rays'''
        arr = cls * len(ray_sequence)
        return arr(*ray_sequence)


    def __init__(self, position=None, direction=None):
        # type: (Vector3, Vector3) -> None
        '''Initializes this Ray struct'''
        super(Ray, self).__init__(
            position or Vector3(),
            direction or Vector3()
        )


    @property
    def byref(self):
        '''Gets a reference to this Ray instance'''
        return byref(self)



# Pointer type to Rays
RayPtr = POINTER(Ray)



class RayCollision(Structure):
    '''RayCollision, ray hit information'''
    _fields_ = [
        ('hit', Bool),
        ('distance', Float),
        ('point', Vector3),
        ('normal', Vector3),
    ]


    @classmethod
    def array_of(cls, ray_collision_sequence):
        '''Creates and returns an array of RayCollisions'''
        arr = cls * len(ray_collision_sequence)
        return arr(*ray_collision_sequence)


    def __init__(self, hit=None, distance=None, point=None, normal=None):
        # type: (bool, float, Vector3, Vector3) -> None
        '''Initializes this RayCollision struct'''
        super(RayCollision, self).__init__(
            hit or False,
            distance or 0.0,
            point or Vector3(),
            normal or Vector3()
        )


    @property
    def byref(self):
        '''Gets a reference to this RayCollision instance'''
        return byref(self)



# Pointer type to RayCollisions
RayCollisionPtr = POINTER(RayCollision)



class BoundingBox(Structure):
    '''BoundingBox'''
    _fields_ = [
        ('min', Vector3),
        ('max', Vector3),
    ]


    @classmethod
    def array_of(cls, bounding_box_sequence):
        '''Creates and returns an array of BoundingBoxs'''
        arr = cls * len(bounding_box_sequence)
        return arr(*bounding_box_sequence)


    def __init__(self, min=None, max=None):
        # type: (Vector3, Vector3) -> None
        '''Initializes this BoundingBox struct'''
        super(BoundingBox, self).__init__(
            min or Vector3(),
            max or Vector3()
        )


    @property
    def byref(self):
        '''Gets a reference to this BoundingBox instance'''
        return byref(self)



# Pointer type to BoundingBoxs
BoundingBoxPtr = POINTER(BoundingBox)



class Wave(Structure):
    '''Wave, audio wave data'''
    _fields_ = [
        ('frame_count', UInt),
        ('sample_rate', UInt),
        ('sample_size', UInt),
        ('channels', UInt),
        ('data', VoidPtr),
    ]


    @classmethod
    def array_of(cls, wave_sequence):
        '''Creates and returns an array of Waves'''
        arr = cls * len(wave_sequence)
        return arr(*wave_sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Union[str, CharPtr]) -> Wave
        """Load wave data from file"""
        result = _LoadWave(_str_in(file_name))
        return result

    @classmethod
    def load_from_memory(cls, file_type, file_data, data_size):
        # type: (Union[str, CharPtr], Union[Seq[int], UCharPtr], int) -> Wave
        """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
        result = _LoadWaveFromMemory(_str_in(file_type), _str_in(file_data), int(data_size))
        return result


    def __init__(self, frame_count=None,
                 sample_rate=None,
                 sample_size=None,
                 channels=None,
                 data=None):
        # type: (int, int, int, int, bytes) -> None
        '''Initializes this Wave struct'''
        super(Wave, self).__init__(
            frame_count or 0,
            sample_rate or 0,
            sample_size or 0,
            channels or 0,
            data
        )


    @property
    def byref(self):
        '''Gets a reference to this Wave instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def copy(self):
        # type: (Wave) -> Wave
        """Copy a wave to a new wave"""
        result = _WaveCopy(self)
        return result

    def crop(self, init_sample, final_sample):
        # type: (WavePtr, int, int) -> None
        """Crop a wave to defined samples range"""
        _WaveCrop(self.byref, int(init_sample), int(final_sample))

    def format(self, sample_rate, sample_size, channels):
        # type: (WavePtr, int, int, int) -> None
        """Convert wave data to desired format"""
        _WaveFormat(self.byref, int(sample_rate), int(sample_size), int(channels))

    def format(self):
        # type: (Wave) -> Union[Seq[float], FloatPtr]
        """Load samples data from wave as a 32bit float data array"""
        result = _ptr_out(_LoadWaveSamples(self.byref))
        return result

    def export(self, file_name):
        # type: (Wave, Union[str, CharPtr]) -> bool
        """Export wave data to file, returns true on success"""
        result = _ExportWave(self, _str_in(file_name))
        return result

    def export_as_code(self, file_name):
        # type: (Wave, Union[str, CharPtr]) -> bool
        """Export wave sample data to code (.h), returns true on success"""
        result = _ExportWaveAsCode(self, _str_in(file_name))
        return result

    def unload(self):
        # type: (Wave) -> None
        """Unload wave data"""
        _UnloadWave(self)

    def unload_samples(self):
        # type: (Union[Seq[float], FloatPtr]) -> None
        """Unload samples data loaded with LoadWaveSamples()"""
        _UnloadWaveSamples(self)


# Pointer type to Waves
WavePtr = POINTER(Wave)



class AudioStream(Structure):
    '''AudioStream, custom audio stream'''
    _fields_ = [
        ('buffer', rAudioBufferPtr),
        ('processor', rAudioProcessorPtr),
        ('sample_rate', UInt),
        ('sample_size', UInt),
        ('channels', UInt),
    ]


    @classmethod
    def array_of(cls, audio_stream_sequence):
        '''Creates and returns an array of AudioStreams'''
        arr = cls * len(audio_stream_sequence)
        return arr(*audio_stream_sequence)

    @classmethod
    def load(cls, sample_rate, sample_size, channels):
        # type: (int, int, int) -> AudioStream
        """Load audio stream (to stream raw audio pcm data)"""
        result = _LoadAudioStream(sample_rate, sample_size, channels)
        return result


    def __init__(self, buffer=None,
                 processor=None,
                 sample_rate=None,
                 sample_size=None,
                 channels=None):
        # type: (rAudioBufferPtr, rAudioProcessorPtr, int, int, int) -> None
        '''Initializes this AudioStream struct'''
        super(AudioStream, self).__init__(
            buffer,
            processor,
            sample_rate or 0,
            sample_size or 0,
            channels or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this AudioStream instance'''
        return byref(self)


    def __str__(self):
        return "[{} Playing: {}]".format(self.__class__.__name__, _IsAudioStreamPlaying(self))

    def __repr__(self):
        return self.__str__()

    def unload(self):
        # type: (AudioStream) -> None
        """Unload audio stream and free memory"""
        _UnloadAudioStream(self)

    def update(self, data, frame_count):
        # type: (AudioStream, bytes, int) -> None
        """Update audio stream buffers with data"""
        _UpdateAudioStream(self, data, int(frame_count))

    def is_processed(self):
        # type: (AudioStream) -> bool
        """Check if any audio stream buffers requires refill"""
        result = _IsAudioStreamProcessed(self)
        return result

    def play(self):
        # type: (AudioStream) -> None
        """Play audio stream"""
        _PlayAudioStream(self)

    def pause(self):
        # type: (AudioStream) -> None
        """Pause audio stream"""
        _PauseAudioStream(self)

    def resume(self):
        # type: (AudioStream) -> None
        """Resume audio stream"""
        _ResumeAudioStream(self)

    def is_playing(self):
        # type: (AudioStream) -> bool
        """Check if audio stream is playing"""
        result = _IsAudioStreamPlaying(self)
        return result

    def stop(self):
        # type: (AudioStream) -> None
        """Stop audio stream"""
        _StopAudioStream(self)

    def set_volume(self, volume):
        # type: (AudioStream, float) -> None
        """Set volume for audio stream (1.0 is max level)"""
        _SetAudioStreamVolume(self, float(volume))

    def set_pitch(self, pitch):
        # type: (AudioStream, float) -> None
        """Set pitch for audio stream (1.0 is base level)"""
        _SetAudioStreamPitch(self, float(pitch))

    def set_pan(self, pan):
        # type: (AudioStream, float) -> None
        """Set pan for audio stream (0.5 is centered)"""
        _SetAudioStreamPan(self, float(pan))

    def set_buffer_size_default(self):
        # type: (int) -> None
        """Default size for new audio streams"""
        _SetAudioStreamBufferSizeDefault(self)

    def set_callback(self, callback):
        # type: (AudioStream, AudioCallback) -> None
        """Audio thread callback to request new data"""
        _SetAudioStreamCallback(self, callback)

    def attach_processor(self, processor):
        # type: (AudioStream, AudioCallback) -> None
        """"""
        _AttachAudioStreamProcessor(self, processor)

    def detach_processor(self, processor):
        # type: (AudioStream, AudioCallback) -> None
        """"""
        _DetachAudioStreamProcessor(self, processor)


# Pointer type to AudioStreams
AudioStreamPtr = POINTER(AudioStream)



class Sound(Structure):
    '''Sound'''
    _fields_ = [
        ('stream', AudioStream),
        ('frame_count', UInt),
    ]


    @classmethod
    def array_of(cls, sound_sequence):
        '''Creates and returns an array of Sounds'''
        arr = cls * len(sound_sequence)
        return arr(*sound_sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Union[str, CharPtr]) -> Sound
        """Load sound from file"""
        result = _LoadSound(_str_in(file_name))
        return result

    @classmethod
    def load_from_wave(cls, wave):
        # type: (Wave) -> Sound
        """Load sound from wave data"""
        result = _LoadSoundFromWave(wave)
        return result


    def __init__(self, stream=None, frame_count=None):
        # type: (AudioStream, int) -> None
        '''Initializes this Sound struct'''
        super(Sound, self).__init__(
            stream or AudioStream(),
            frame_count or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this Sound instance'''
        return byref(self)


    def __str__(self):
        return "[{} Playing: {}]".format(self.__class__.__name__, _IsSoundPlaying(self))

    def __repr__(self):
        return self.__str__()

    def play(self):
        # type: (Sound) -> None
        """Play a sound"""
        _PlaySound(self)

    def stop(self):
        # type: (Sound) -> None
        """Stop playing a sound"""
        _StopSound(self)

    def pause(self):
        # type: (Sound) -> None
        """Pause a sound"""
        _PauseSound(self)

    def resume(self):
        # type: (Sound) -> None
        """Resume a paused sound"""
        _ResumeSound(self)

    def play_multi(self):
        # type: (Sound) -> None
        """Play a sound (using multichannel buffer pool)"""
        _PlaySoundMulti(self)

    def is_playing(self):
        # type: (Sound) -> bool
        """Check if a sound is currently playing"""
        result = _IsSoundPlaying(self)
        return result

    def set_volume(self, volume):
        # type: (Sound, float) -> None
        """Set volume for a sound (1.0 is max level)"""
        _SetSoundVolume(self, float(volume))

    def set_pitch(self, pitch):
        # type: (Sound, float) -> None
        """Set pitch for a sound (1.0 is base level)"""
        _SetSoundPitch(self, float(pitch))

    def set_pan(self, pan):
        # type: (Sound, float) -> None
        """Set pan for a sound (0.5 is center)"""
        _SetSoundPan(self, float(pan))

    def unload(self):
        # type: (Sound) -> None
        """Unload sound"""
        _UnloadSound(self)

    def update(self, data, sample_count):
        # type: (Sound, bytes, int) -> None
        """Update sound buffer with new data"""
        _UpdateSound(self, data, int(sample_count))

    @staticmethod
    def get_sounds_playing():
        # type: () -> int
        """Get number of sounds playing in the multichannel"""
        result = _GetSoundsPlaying()
        return result

    @staticmethod
    def stop_multi():
        # type: () -> None
        """Stop any sound playing (using multichannel buffer pool)"""
        _StopSoundMulti()


# Pointer type to Sounds
SoundPtr = POINTER(Sound)



class Music(Structure):
    '''Music, audio stream, anything longer than ~10 seconds should be streamed'''
    _fields_ = [
        ('stream', AudioStream),
        ('frame_count', UInt),
        ('looping', Bool),
        ('ctx_type', Int),
        ('ctx_data', VoidPtr),
    ]


    @classmethod
    def array_of(cls, music_sequence):
        '''Creates and returns an array of Musics'''
        arr = cls * len(music_sequence)
        return arr(*music_sequence)


    def __init__(self, stream=None,
                 frame_count=None,
                 looping=None,
                 ctx_type=None,
                 ctx_data=None):
        # type: (AudioStream, int, bool, int, bytes) -> None
        '''Initializes this Music struct'''
        super(Music, self).__init__(
            stream or AudioStream(),
            frame_count or 0,
            looping or False,
            ctx_type or 0,
            ctx_data
        )


    @property
    def byref(self):
        '''Gets a reference to this Music instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def play(self):
        # type: (Music) -> None
        """Start music playing"""
        _PlayMusicStream(self)

    def is_playing(self):
        # type: (Music) -> bool
        """Check if music is playing"""
        result = _IsMusicStreamPlaying(self)
        return result

    def update(self):
        # type: (Music) -> None
        """Updates buffers for music streaming"""
        _UpdateMusicStream(self)

    def stop(self):
        # type: (Music) -> None
        """Stop music playing"""
        _StopMusicStream(self)

    def pause(self):
        # type: (Music) -> None
        """Pause music playing"""
        _PauseMusicStream(self)

    def resume(self):
        # type: (Music) -> None
        """Resume playing paused music"""
        _ResumeMusicStream(self)

    def seek(self, position):
        # type: (Music, float) -> None
        """Seek music to a position (in seconds)"""
        _SeekMusicStream(self, float(position))

    def set_volume(self, volume):
        # type: (Music, float) -> None
        """Set volume for music (1.0 is max level)"""
        _SetMusicVolume(self, float(volume))

    def set_pitch(self, pitch):
        # type: (Music, float) -> None
        """Set pitch for a music (1.0 is base level)"""
        _SetMusicPitch(self, float(pitch))

    def set_pan(self, pan):
        # type: (Music, float) -> None
        """Set pan for a music (0.5 is center)"""
        _SetMusicPan(self, float(pan))

    def get_time_length(self):
        # type: (Music) -> float
        """Get music time length (in seconds)"""
        result = _GetMusicTimeLength(self)
        return result

    def get_time_played(self):
        # type: (Music) -> float
        """Get current music time played (in seconds)"""
        result = _GetMusicTimePlayed(self)
        return result

    @staticmethod
    def load(file_name):
        # type: (Union[str, CharPtr]) -> Music
        """Load music stream from file"""
        result = _LoadMusicStream(_str_in(file_name))
        return result

    @staticmethod
    def load_from_memory(file_type, data, data_size):
        # type: (Union[str, CharPtr], Union[Seq[int], UCharPtr], int) -> Music
        """Load music stream from data"""
        result = _LoadMusicStreamFromMemory(_str_in(file_type), _str_in(data), int(data_size))
        return result


# Pointer type to Musics
MusicPtr = POINTER(Music)



class VrDeviceInfo(Structure):
    '''VrDeviceInfo, Head-Mounted-Display device parameters'''
    _fields_ = [
        ('h_resolution', Int),
        ('v_resolution', Int),
        ('h_screen_size', Float),
        ('v_screen_size', Float),
        ('v_screen_center', Float),
        ('eye_to_screen_distance', Float),
        ('lens_separation_distance', Float),
        ('interpupillary_distance', Float),
        ('lens_distortion_values', Float * 4),
        ('chroma_ab_correction', Float * 4),
    ]


    @classmethod
    def array_of(cls, vr_device_info_sequence):
        '''Creates and returns an array of VrDeviceInfos'''
        arr = cls * len(vr_device_info_sequence)
        return arr(*vr_device_info_sequence)


    def __init__(self, h_resolution=None,
                 v_resolution=None,
                 h_screen_size=None,
                 v_screen_size=None,
                 v_screen_center=None,
                 eye_to_screen_distance=None,
                 lens_separation_distance=None,
                 interpupillary_distance=None,
                 lens_distortion_values=None,
                 chroma_ab_correction=None):
        # type: (int, int, float, float, float, float, float, float, Seq[float], Seq[float]) -> None
        '''Initializes this VrDeviceInfo struct'''
        super(VrDeviceInfo, self).__init__(
            h_resolution or 0,
            v_resolution or 0,
            h_screen_size or 0.0,
            v_screen_size or 0.0,
            v_screen_center or 0.0,
            eye_to_screen_distance or 0.0,
            lens_separation_distance or 0.0,
            interpupillary_distance or 0.0,
            lens_distortion_values,
            chroma_ab_correction
        )


    @property
    def byref(self):
        '''Gets a reference to this VrDeviceInfo instance'''
        return byref(self)



# Pointer type to VrDeviceInfos
VrDeviceInfoPtr = POINTER(VrDeviceInfo)



class VrStereoConfig(Structure):
    '''VrStereoConfig, VR stereo rendering configuration for simulator'''
    _fields_ = [
        ('projection', Matrix * 2),
        ('view_offset', Matrix * 2),
        ('left_lens_center', Float * 2),
        ('right_lens_center', Float * 2),
        ('left_screen_center', Float * 2),
        ('right_screen_center', Float * 2),
        ('scale', Float * 2),
        ('scale_in', Float * 2),
    ]


    @classmethod
    def array_of(cls, vr_stereo_config_sequence):
        '''Creates and returns an array of VrStereoConfigs'''
        arr = cls * len(vr_stereo_config_sequence)
        return arr(*vr_stereo_config_sequence)


    def __init__(self, projection=None,
                 view_offset=None,
                 left_lens_center=None,
                 right_lens_center=None,
                 left_screen_center=None,
                 right_screen_center=None,
                 scale=None,
                 scale_in=None):
        # type: (Seq[Matrix], Seq[Matrix], Seq[float], Seq[float], Seq[float], Seq[float], Seq[float], Seq[float]) -> None
        '''Initializes this VrStereoConfig struct'''
        super(VrStereoConfig, self).__init__(
            projection,
            view_offset,
            left_lens_center,
            right_lens_center,
            left_screen_center,
            right_screen_center,
            scale,
            scale_in
        )


    @property
    def byref(self):
        '''Gets a reference to this VrStereoConfig instance'''
        return byref(self)


    def __enter__(self):
        _BeginVrStereoMode(self)

    def __leave__(self, exc_type, exc_value, traceback):
        _EndVrStereoMode()


# Pointer type to VrStereoConfigs
VrStereoConfigPtr = POINTER(VrStereoConfig)



class FilePathList(Structure):
    '''File path list'''
    _fields_ = [
        ('capacity', UInt),
        ('count', UInt),
        ('paths', CharPtrPtr),
    ]


    @classmethod
    def array_of(cls, file_path_list_sequence):
        '''Creates and returns an array of FilePathLists'''
        arr = cls * len(file_path_list_sequence)
        return arr(*file_path_list_sequence)


    def __init__(self, capacity=None, count=None, paths=None):
        # type: (int, int, Seq[Union[str, CharPtr]]) -> None
        '''Initializes this FilePathList struct'''
        super(FilePathList, self).__init__(
            capacity or 0,
            count or 0,
            paths
        )


    @property
    def byref(self):
        '''Gets a reference to this FilePathList instance'''
        return byref(self)



# Pointer type to FilePathLists
FilePathListPtr = POINTER(FilePathList)



class rlVertexBuffer(Structure):
    '''Dynamic vertex buffers (position + texcoords + colors + indices arrays)'''
    _fields_ = [
        ('element_count', Int),
        ('vertices', FloatPtr),
        ('texcoords', FloatPtr),
        ('colors', UCharPtr),
        ('indices', UIntPtr),
        ('vao_id', UInt),
        ('vbo_id', Int * 4),
    ]


    @classmethod
    def array_of(cls, rl_vertex_buffer_sequence):
        '''Creates and returns an array of rlVertexBuffers'''
        arr = cls * len(rl_vertex_buffer_sequence)
        return arr(*rl_vertex_buffer_sequence)


    def __init__(self, element_count=None,
                 vertices=None,
                 texcoords=None,
                 colors=None,
                 indices=None,
                 vao_id=None,
                 vbo_id=None):
        # type: (int, Union[Seq[float], FloatPtr], Union[Seq[float], FloatPtr], Union[Seq[int], UCharPtr], Union[Seq[int], UIntPtr], int, Seq[int]) -> None
        '''Initializes this rlVertexBuffer struct'''
        super(rlVertexBuffer, self).__init__(
            element_count or 0,
            vertices,
            texcoords,
            colors,
            indices,
            vao_id or 0,
            vbo_id
        )


    @property
    def byref(self):
        '''Gets a reference to this rlVertexBuffer instance'''
        return byref(self)



# Pointer type to rlVertexBuffers
rlVertexBufferPtr = POINTER(rlVertexBuffer)



class rlDrawCall(Structure):
    '''of those state-change happens (this is done in core module)'''
    _fields_ = [
        ('mode', Int),
        ('vertex_count', Int),
        ('vertex_alignment', Int),
        ('texture_id', UInt),
    ]


    @classmethod
    def array_of(cls, rl_draw_call_sequence):
        '''Creates and returns an array of rlDrawCalls'''
        arr = cls * len(rl_draw_call_sequence)
        return arr(*rl_draw_call_sequence)


    def __init__(self, mode=None, vertex_count=None, vertex_alignment=None, texture_id=None):
        # type: (int, int, int, int) -> None
        '''Initializes this rlDrawCall struct'''
        super(rlDrawCall, self).__init__(
            mode or 0,
            vertex_count or 0,
            vertex_alignment or 0,
            texture_id or 0
        )


    @property
    def byref(self):
        '''Gets a reference to this rlDrawCall instance'''
        return byref(self)



# Pointer type to rlDrawCalls
rlDrawCallPtr = POINTER(rlDrawCall)



class rlRenderBatch(Structure):
    '''rlRenderBatch type'''
    _fields_ = [
        ('buffer_count', Int),
        ('current_buffer', Int),
        ('vertex_buffer', rlVertexBufferPtr),
        ('draws', rlDrawCallPtr),
        ('draw_counter', Int),
        ('current_depth', Float),
    ]


    @classmethod
    def array_of(cls, rl_render_batch_sequence):
        '''Creates and returns an array of rlRenderBatchs'''
        arr = cls * len(rl_render_batch_sequence)
        return arr(*rl_render_batch_sequence)


    def __init__(self, buffer_count=None,
                 current_buffer=None,
                 vertex_buffer=None,
                 draws=None,
                 draw_counter=None,
                 current_depth=None):
        # type: (int, int, rlVertexBufferPtr, rlDrawCallPtr, int, float) -> None
        '''Initializes this rlRenderBatch struct'''
        super(rlRenderBatch, self).__init__(
            buffer_count or 0,
            current_buffer or 0,
            vertex_buffer,
            draws,
            draw_counter or 0,
            current_depth or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this rlRenderBatch instance'''
        return byref(self)



# Pointer type to rlRenderBatchs
rlRenderBatchPtr = POINTER(rlRenderBatch)



class Matrix(Structure):
    '''Matrix, 4x4 components, column major, OpenGL style, right handed'''
    _fields_ = [
        ('m0', Float),
        ('m4', Float),
        ('m8', Float),
        ('m12', Float),
        ('m1', Float),
        ('m5', Float),
        ('m9', Float),
        ('m13', Float),
        ('m2', Float),
        ('m6', Float),
        ('m10', Float),
        ('m14', Float),
        ('m3', Float),
        ('m7', Float),
        ('m11', Float),
        ('m15', Float),
    ]


    @classmethod
    def array_of(cls, matrix_sequence):
        '''Creates and returns an array of Matrixs'''
        arr = cls * len(matrix_sequence)
        return arr(*matrix_sequence)

    @classmethod
    def identity():
        # type: () -> Matrix
        """Get identity matrix"""
        result = _MatrixIdentity()
        return result

    @classmethod
    def translate(cls, x, y, z):
        # type: (float, float, float) -> Matrix
        """Get translation matrix"""
        result = _MatrixTranslate(float(x), float(y), float(z))
        return result

    @classmethod
    def rotate(cls, axis, angle):
        # type: (Vector3, float) -> Matrix
        """Create rotation matrix from axis and angle. Angle should be provided in radians"""
        result = _MatrixRotate(_vec3(axis), float(angle))
        return result

    @classmethod
    def rotate_x(cls, angle):
        # type: (float) -> Matrix
        """Get x-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateX(float(angle))
        return result

    @classmethod
    def rotate_y(cls, angle):
        # type: (float) -> Matrix
        """Get y-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateY(float(angle))
        return result

    @classmethod
    def rotate_z(cls, angle):
        # type: (float) -> Matrix
        """Get z-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateZ(float(angle))
        return result

    @classmethod
    def rotate_xyz(cls, angle):
        # type: (Vector3) -> Matrix
        """Get xyz-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateXYZ(_vec3(angle))
        return result

    @classmethod
    def rotate_zyx(cls, angle):
        # type: (Vector3) -> Matrix
        """Get zyx-rotation matrix. Angle must be provided in radians"""
        result = _MatrixRotateZYX(_vec3(angle))
        return result

    @classmethod
    def scale(cls, x, y, z):
        # type: (float, float, float) -> Matrix
        """Get scaling matrix"""
        result = _MatrixScale(float(x), float(y), float(z))
        return result

    @classmethod
    def frustum(cls, left, right, bottom, top, near, far):
        # type: (float, float, float, float, float, float) -> Matrix
        """Get perspective projection matrix"""
        result = _MatrixFrustum(float(left), float(right), float(bottom), float(top), float(near), float(far))
        return result

    @classmethod
    def perspective(cls, fovy, aspect, near, far):
        # type: (float, float, float, float) -> Matrix
        """Get perspective projection matrix. Fovy angle must be provided in radians"""
        result = _MatrixPerspective(float(fovy), float(aspect), float(near), float(far))
        return result

    @classmethod
    def ortho(cls, left, right, bottom, top, near, far):
        # type: (float, float, float, float, float, float) -> Matrix
        """Get orthographic projection matrix"""
        result = _MatrixOrtho(float(left), float(right), float(bottom), float(top), float(near), float(far))
        return result

    @classmethod
    def look_at(cls, eye, target, up):
        # type: (Vector3, Vector3, Vector3) -> Matrix
        """Get camera look-at matrix (view matrix)"""
        result = _MatrixLookAt(_vec3(eye), _vec3(target), _vec3(up))
        return result


    def __init__(self, m0=None,
                 m4=None,
                 m8=None,
                 m12=None,
                 m1=None,
                 m5=None,
                 m9=None,
                 m13=None,
                 m2=None,
                 m6=None,
                 m10=None,
                 m14=None,
                 m3=None,
                 m7=None,
                 m11=None,
                 m15=None):
        # type: (float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float) -> None
        '''Initializes this Matrix struct'''
        super(Matrix, self).__init__(
            m0 or 0.0,
            m4 or 0.0,
            m8 or 0.0,
            m12 or 0.0,
            m1 or 0.0,
            m5 or 0.0,
            m9 or 0.0,
            m13 or 0.0,
            m2 or 0.0,
            m6 or 0.0,
            m10 or 0.0,
            m14 or 0.0,
            m3 or 0.0,
            m7 or 0.0,
            m11 or 0.0,
            m15 or 0.0
        )


    @property
    def byref(self):
        '''Gets a reference to this Matrix instance'''
        return byref(self)


    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def determinant(self):
        # type: (Matrix) -> float
        """Compute matrix determinant"""
        result = _MatrixDeterminant(self)
        return result

    def trace(self):
        # type: (Matrix) -> float
        """Get the trace of the matrix (sum of the values along the diagonal)"""
        result = _MatrixTrace(self)
        return result

    def transpose(self):
        # type: (Matrix) -> Matrix
        """Get the trace of the matrix (sum of the values along the diagonal)"""
        result = _MatrixTranspose(self)
        return result

    def invert(self):
        # type: (Matrix) -> Matrix
        """Invert provided matrix"""
        result = _MatrixInvert(self)
        return result


# Pointer type to Matrixs
MatrixPtr = POINTER(Matrix)


class ConfigFlags(IntEnum):
    """System/Window config flags"""

    FLAG_VSYNC_HINT = 64
    """Set to try enabling V-Sync on GPU"""

    FLAG_FULLSCREEN_MODE = 2
    """Set to run program in fullscreen"""

    FLAG_WINDOW_RESIZABLE = 4
    """Set to allow resizable window"""

    FLAG_WINDOW_UNDECORATED = 8
    """Set to disable window decoration (frame and buttons)"""

    FLAG_WINDOW_HIDDEN = 128
    """Set to hide window"""

    FLAG_WINDOW_MINIMIZED = 512
    """Set to minimize window (iconify)"""

    FLAG_WINDOW_MAXIMIZED = 1024
    """Set to maximize window (expanded to monitor)"""

    FLAG_WINDOW_UNFOCUSED = 2048
    """Set to window non focused"""

    FLAG_WINDOW_TOPMOST = 4096
    """Set to window always on top"""

    FLAG_WINDOW_ALWAYS_RUN = 256
    """Set to allow windows running while minimized"""

    FLAG_WINDOW_TRANSPARENT = 16
    """Set to allow transparent framebuffer"""

    FLAG_WINDOW_HIGHDPI = 8192
    """Set to support HighDPI"""

    FLAG_WINDOW_MOUSE_PASSTHROUGH = 16384
    """Set to support mouse passthrough, only supported when FLAG_WINDOW_UNDECORATED"""

    FLAG_MSAA_4X_HINT = 32
    """Set to try enabling MSAA 4X"""

    FLAG_INTERLACED_HINT = 65536
    """Set to try enabling interlaced video format (for V3D)"""



FLAG_VSYNC_HINT = ConfigFlags.FLAG_VSYNC_HINT
FLAG_FULLSCREEN_MODE = ConfigFlags.FLAG_FULLSCREEN_MODE
FLAG_WINDOW_RESIZABLE = ConfigFlags.FLAG_WINDOW_RESIZABLE
FLAG_WINDOW_UNDECORATED = ConfigFlags.FLAG_WINDOW_UNDECORATED
FLAG_WINDOW_HIDDEN = ConfigFlags.FLAG_WINDOW_HIDDEN
FLAG_WINDOW_MINIMIZED = ConfigFlags.FLAG_WINDOW_MINIMIZED
FLAG_WINDOW_MAXIMIZED = ConfigFlags.FLAG_WINDOW_MAXIMIZED
FLAG_WINDOW_UNFOCUSED = ConfigFlags.FLAG_WINDOW_UNFOCUSED
FLAG_WINDOW_TOPMOST = ConfigFlags.FLAG_WINDOW_TOPMOST
FLAG_WINDOW_ALWAYS_RUN = ConfigFlags.FLAG_WINDOW_ALWAYS_RUN
FLAG_WINDOW_TRANSPARENT = ConfigFlags.FLAG_WINDOW_TRANSPARENT
FLAG_WINDOW_HIGHDPI = ConfigFlags.FLAG_WINDOW_HIGHDPI
FLAG_WINDOW_MOUSE_PASSTHROUGH = ConfigFlags.FLAG_WINDOW_MOUSE_PASSTHROUGH
FLAG_MSAA_4X_HINT = ConfigFlags.FLAG_MSAA_4X_HINT
FLAG_INTERLACED_HINT = ConfigFlags.FLAG_INTERLACED_HINT


class TraceLogLevel(IntEnum):
    """Trace log level"""

    LOG_ALL = 0
    """Display all logs"""

    LOG_TRACE = 1
    """Trace logging, intended for internal use only"""

    LOG_DEBUG = 2
    """Debug logging, used for internal debugging, it should be disabled on release builds"""

    LOG_INFO = 3
    """Info logging, used for program execution info"""

    LOG_WARNING = 4
    """Warning logging, used on recoverable failures"""

    LOG_ERROR = 5
    """Error logging, used on unrecoverable failures"""

    LOG_FATAL = 6
    """Fatal logging, used to abort program: exit(EXIT_FAILURE)"""

    LOG_NONE = 7
    """Disable logging"""



LOG_ALL = TraceLogLevel.LOG_ALL
LOG_TRACE = TraceLogLevel.LOG_TRACE
LOG_DEBUG = TraceLogLevel.LOG_DEBUG
LOG_INFO = TraceLogLevel.LOG_INFO
LOG_WARNING = TraceLogLevel.LOG_WARNING
LOG_ERROR = TraceLogLevel.LOG_ERROR
LOG_FATAL = TraceLogLevel.LOG_FATAL
LOG_NONE = TraceLogLevel.LOG_NONE


class KeyboardKey(IntEnum):
    """Keyboard keys (US keyboard layout)"""

    KEY_NULL = 0
    """Key: NULL, used for no key pressed"""

    KEY_APOSTROPHE = 39
    """Key: '"""

    KEY_COMMA = 44
    """Key: ,"""

    KEY_MINUS = 45
    """Key: -"""

    KEY_PERIOD = 46
    """Key: ."""

    KEY_SLASH = 47
    """Key: /"""

    KEY_ZERO = 48
    """Key: 0"""

    KEY_ONE = 49
    """Key: 1"""

    KEY_TWO = 50
    """Key: 2"""

    KEY_THREE = 51
    """Key: 3"""

    KEY_FOUR = 52
    """Key: 4"""

    KEY_FIVE = 53
    """Key: 5"""

    KEY_SIX = 54
    """Key: 6"""

    KEY_SEVEN = 55
    """Key: 7"""

    KEY_EIGHT = 56
    """Key: 8"""

    KEY_NINE = 57
    """Key: 9"""

    KEY_SEMICOLON = 59
    """Key: ;"""

    KEY_EQUAL = 61
    """Key: ="""

    KEY_A = 65
    """Key: A | a"""

    KEY_B = 66
    """Key: B | b"""

    KEY_C = 67
    """Key: C | c"""

    KEY_D = 68
    """Key: D | d"""

    KEY_E = 69
    """Key: E | e"""

    KEY_F = 70
    """Key: F | f"""

    KEY_G = 71
    """Key: G | g"""

    KEY_H = 72
    """Key: H | h"""

    KEY_I = 73
    """Key: I | i"""

    KEY_J = 74
    """Key: J | j"""

    KEY_K = 75
    """Key: K | k"""

    KEY_L = 76
    """Key: L | l"""

    KEY_M = 77
    """Key: M | m"""

    KEY_N = 78
    """Key: N | n"""

    KEY_O = 79
    """Key: O | o"""

    KEY_P = 80
    """Key: P | p"""

    KEY_Q = 81
    """Key: Q | q"""

    KEY_R = 82
    """Key: R | r"""

    KEY_S = 83
    """Key: S | s"""

    KEY_T = 84
    """Key: T | t"""

    KEY_U = 85
    """Key: U | u"""

    KEY_V = 86
    """Key: V | v"""

    KEY_W = 87
    """Key: W | w"""

    KEY_X = 88
    """Key: X | x"""

    KEY_Y = 89
    """Key: Y | y"""

    KEY_Z = 90
    """Key: Z | z"""

    KEY_LEFT_BRACKET = 91
    """Key: ["""

    KEY_BACKSLASH = 92
    """Key: '\'"""

    KEY_RIGHT_BRACKET = 93
    """Key: ]"""

    KEY_GRAVE = 96
    """Key: `"""

    KEY_SPACE = 32
    """Key: Space"""

    KEY_ESCAPE = 256
    """Key: Esc"""

    KEY_ENTER = 257
    """Key: Enter"""

    KEY_TAB = 258
    """Key: Tab"""

    KEY_BACKSPACE = 259
    """Key: Backspace"""

    KEY_INSERT = 260
    """Key: Ins"""

    KEY_DELETE = 261
    """Key: Del"""

    KEY_RIGHT = 262
    """Key: Cursor right"""

    KEY_LEFT = 263
    """Key: Cursor left"""

    KEY_DOWN = 264
    """Key: Cursor down"""

    KEY_UP = 265
    """Key: Cursor up"""

    KEY_PAGE_UP = 266
    """Key: Page up"""

    KEY_PAGE_DOWN = 267
    """Key: Page down"""

    KEY_HOME = 268
    """Key: Home"""

    KEY_END = 269
    """Key: End"""

    KEY_CAPS_LOCK = 280
    """Key: Caps lock"""

    KEY_SCROLL_LOCK = 281
    """Key: Scroll down"""

    KEY_NUM_LOCK = 282
    """Key: Num lock"""

    KEY_PRINT_SCREEN = 283
    """Key: Print screen"""

    KEY_PAUSE = 284
    """Key: Pause"""

    KEY_F1 = 290
    """Key: F1"""

    KEY_F2 = 291
    """Key: F2"""

    KEY_F3 = 292
    """Key: F3"""

    KEY_F4 = 293
    """Key: F4"""

    KEY_F5 = 294
    """Key: F5"""

    KEY_F6 = 295
    """Key: F6"""

    KEY_F7 = 296
    """Key: F7"""

    KEY_F8 = 297
    """Key: F8"""

    KEY_F9 = 298
    """Key: F9"""

    KEY_F10 = 299
    """Key: F10"""

    KEY_F11 = 300
    """Key: F11"""

    KEY_F12 = 301
    """Key: F12"""

    KEY_LEFT_SHIFT = 340
    """Key: Shift left"""

    KEY_LEFT_CONTROL = 341
    """Key: Control left"""

    KEY_LEFT_ALT = 342
    """Key: Alt left"""

    KEY_LEFT_SUPER = 343
    """Key: Super left"""

    KEY_RIGHT_SHIFT = 344
    """Key: Shift right"""

    KEY_RIGHT_CONTROL = 345
    """Key: Control right"""

    KEY_RIGHT_ALT = 346
    """Key: Alt right"""

    KEY_RIGHT_SUPER = 347
    """Key: Super right"""

    KEY_KB_MENU = 348
    """Key: KB menu"""

    KEY_KP_0 = 320
    """Key: Keypad 0"""

    KEY_KP_1 = 321
    """Key: Keypad 1"""

    KEY_KP_2 = 322
    """Key: Keypad 2"""

    KEY_KP_3 = 323
    """Key: Keypad 3"""

    KEY_KP_4 = 324
    """Key: Keypad 4"""

    KEY_KP_5 = 325
    """Key: Keypad 5"""

    KEY_KP_6 = 326
    """Key: Keypad 6"""

    KEY_KP_7 = 327
    """Key: Keypad 7"""

    KEY_KP_8 = 328
    """Key: Keypad 8"""

    KEY_KP_9 = 329
    """Key: Keypad 9"""

    KEY_KP_DECIMAL = 330
    """Key: Keypad ."""

    KEY_KP_DIVIDE = 331
    """Key: Keypad /"""

    KEY_KP_MULTIPLY = 332
    """Key: Keypad *"""

    KEY_KP_SUBTRACT = 333
    """Key: Keypad -"""

    KEY_KP_ADD = 334
    """Key: Keypad +"""

    KEY_KP_ENTER = 335
    """Key: Keypad Enter"""

    KEY_KP_EQUAL = 336
    """Key: Keypad ="""

    KEY_BACK = 4
    """Key: Android back button"""

    KEY_MENU = 82
    """Key: Android menu button"""

    KEY_VOLUME_UP = 24
    """Key: Android volume up button"""

    KEY_VOLUME_DOWN = 25
    """Key: Android volume down button"""



KEY_NULL = KeyboardKey.KEY_NULL
KEY_APOSTROPHE = KeyboardKey.KEY_APOSTROPHE
KEY_COMMA = KeyboardKey.KEY_COMMA
KEY_MINUS = KeyboardKey.KEY_MINUS
KEY_PERIOD = KeyboardKey.KEY_PERIOD
KEY_SLASH = KeyboardKey.KEY_SLASH
KEY_ZERO = KeyboardKey.KEY_ZERO
KEY_ONE = KeyboardKey.KEY_ONE
KEY_TWO = KeyboardKey.KEY_TWO
KEY_THREE = KeyboardKey.KEY_THREE
KEY_FOUR = KeyboardKey.KEY_FOUR
KEY_FIVE = KeyboardKey.KEY_FIVE
KEY_SIX = KeyboardKey.KEY_SIX
KEY_SEVEN = KeyboardKey.KEY_SEVEN
KEY_EIGHT = KeyboardKey.KEY_EIGHT
KEY_NINE = KeyboardKey.KEY_NINE
KEY_SEMICOLON = KeyboardKey.KEY_SEMICOLON
KEY_EQUAL = KeyboardKey.KEY_EQUAL
KEY_A = KeyboardKey.KEY_A
KEY_B = KeyboardKey.KEY_B
KEY_C = KeyboardKey.KEY_C
KEY_D = KeyboardKey.KEY_D
KEY_E = KeyboardKey.KEY_E
KEY_F = KeyboardKey.KEY_F
KEY_G = KeyboardKey.KEY_G
KEY_H = KeyboardKey.KEY_H
KEY_I = KeyboardKey.KEY_I
KEY_J = KeyboardKey.KEY_J
KEY_K = KeyboardKey.KEY_K
KEY_L = KeyboardKey.KEY_L
KEY_M = KeyboardKey.KEY_M
KEY_N = KeyboardKey.KEY_N
KEY_O = KeyboardKey.KEY_O
KEY_P = KeyboardKey.KEY_P
KEY_Q = KeyboardKey.KEY_Q
KEY_R = KeyboardKey.KEY_R
KEY_S = KeyboardKey.KEY_S
KEY_T = KeyboardKey.KEY_T
KEY_U = KeyboardKey.KEY_U
KEY_V = KeyboardKey.KEY_V
KEY_W = KeyboardKey.KEY_W
KEY_X = KeyboardKey.KEY_X
KEY_Y = KeyboardKey.KEY_Y
KEY_Z = KeyboardKey.KEY_Z
KEY_LEFT_BRACKET = KeyboardKey.KEY_LEFT_BRACKET
KEY_BACKSLASH = KeyboardKey.KEY_BACKSLASH
KEY_RIGHT_BRACKET = KeyboardKey.KEY_RIGHT_BRACKET
KEY_GRAVE = KeyboardKey.KEY_GRAVE
KEY_SPACE = KeyboardKey.KEY_SPACE
KEY_ESCAPE = KeyboardKey.KEY_ESCAPE
KEY_ENTER = KeyboardKey.KEY_ENTER
KEY_TAB = KeyboardKey.KEY_TAB
KEY_BACKSPACE = KeyboardKey.KEY_BACKSPACE
KEY_INSERT = KeyboardKey.KEY_INSERT
KEY_DELETE = KeyboardKey.KEY_DELETE
KEY_RIGHT = KeyboardKey.KEY_RIGHT
KEY_LEFT = KeyboardKey.KEY_LEFT
KEY_DOWN = KeyboardKey.KEY_DOWN
KEY_UP = KeyboardKey.KEY_UP
KEY_PAGE_UP = KeyboardKey.KEY_PAGE_UP
KEY_PAGE_DOWN = KeyboardKey.KEY_PAGE_DOWN
KEY_HOME = KeyboardKey.KEY_HOME
KEY_END = KeyboardKey.KEY_END
KEY_CAPS_LOCK = KeyboardKey.KEY_CAPS_LOCK
KEY_SCROLL_LOCK = KeyboardKey.KEY_SCROLL_LOCK
KEY_NUM_LOCK = KeyboardKey.KEY_NUM_LOCK
KEY_PRINT_SCREEN = KeyboardKey.KEY_PRINT_SCREEN
KEY_PAUSE = KeyboardKey.KEY_PAUSE
KEY_F1 = KeyboardKey.KEY_F1
KEY_F2 = KeyboardKey.KEY_F2
KEY_F3 = KeyboardKey.KEY_F3
KEY_F4 = KeyboardKey.KEY_F4
KEY_F5 = KeyboardKey.KEY_F5
KEY_F6 = KeyboardKey.KEY_F6
KEY_F7 = KeyboardKey.KEY_F7
KEY_F8 = KeyboardKey.KEY_F8
KEY_F9 = KeyboardKey.KEY_F9
KEY_F10 = KeyboardKey.KEY_F10
KEY_F11 = KeyboardKey.KEY_F11
KEY_F12 = KeyboardKey.KEY_F12
KEY_LEFT_SHIFT = KeyboardKey.KEY_LEFT_SHIFT
KEY_LEFT_CONTROL = KeyboardKey.KEY_LEFT_CONTROL
KEY_LEFT_ALT = KeyboardKey.KEY_LEFT_ALT
KEY_LEFT_SUPER = KeyboardKey.KEY_LEFT_SUPER
KEY_RIGHT_SHIFT = KeyboardKey.KEY_RIGHT_SHIFT
KEY_RIGHT_CONTROL = KeyboardKey.KEY_RIGHT_CONTROL
KEY_RIGHT_ALT = KeyboardKey.KEY_RIGHT_ALT
KEY_RIGHT_SUPER = KeyboardKey.KEY_RIGHT_SUPER
KEY_KB_MENU = KeyboardKey.KEY_KB_MENU
KEY_KP_0 = KeyboardKey.KEY_KP_0
KEY_KP_1 = KeyboardKey.KEY_KP_1
KEY_KP_2 = KeyboardKey.KEY_KP_2
KEY_KP_3 = KeyboardKey.KEY_KP_3
KEY_KP_4 = KeyboardKey.KEY_KP_4
KEY_KP_5 = KeyboardKey.KEY_KP_5
KEY_KP_6 = KeyboardKey.KEY_KP_6
KEY_KP_7 = KeyboardKey.KEY_KP_7
KEY_KP_8 = KeyboardKey.KEY_KP_8
KEY_KP_9 = KeyboardKey.KEY_KP_9
KEY_KP_DECIMAL = KeyboardKey.KEY_KP_DECIMAL
KEY_KP_DIVIDE = KeyboardKey.KEY_KP_DIVIDE
KEY_KP_MULTIPLY = KeyboardKey.KEY_KP_MULTIPLY
KEY_KP_SUBTRACT = KeyboardKey.KEY_KP_SUBTRACT
KEY_KP_ADD = KeyboardKey.KEY_KP_ADD
KEY_KP_ENTER = KeyboardKey.KEY_KP_ENTER
KEY_KP_EQUAL = KeyboardKey.KEY_KP_EQUAL
KEY_BACK = KeyboardKey.KEY_BACK
KEY_MENU = KeyboardKey.KEY_MENU
KEY_VOLUME_UP = KeyboardKey.KEY_VOLUME_UP
KEY_VOLUME_DOWN = KeyboardKey.KEY_VOLUME_DOWN


class MouseButton(IntEnum):
    """Mouse buttons"""

    MOUSE_BUTTON_LEFT = 0
    """Mouse button left"""

    MOUSE_BUTTON_RIGHT = 1
    """Mouse button right"""

    MOUSE_BUTTON_MIDDLE = 2
    """Mouse button middle (pressed wheel)"""

    MOUSE_BUTTON_SIDE = 3
    """Mouse button side (advanced mouse device)"""

    MOUSE_BUTTON_EXTRA = 4
    """Mouse button extra (advanced mouse device)"""

    MOUSE_BUTTON_FORWARD = 5
    """Mouse button fordward (advanced mouse device)"""

    MOUSE_BUTTON_BACK = 6
    """Mouse button back (advanced mouse device)"""



MOUSE_BUTTON_LEFT = MouseButton.MOUSE_BUTTON_LEFT
MOUSE_BUTTON_RIGHT = MouseButton.MOUSE_BUTTON_RIGHT
MOUSE_BUTTON_MIDDLE = MouseButton.MOUSE_BUTTON_MIDDLE
MOUSE_BUTTON_SIDE = MouseButton.MOUSE_BUTTON_SIDE
MOUSE_BUTTON_EXTRA = MouseButton.MOUSE_BUTTON_EXTRA
MOUSE_BUTTON_FORWARD = MouseButton.MOUSE_BUTTON_FORWARD
MOUSE_BUTTON_BACK = MouseButton.MOUSE_BUTTON_BACK


class MouseCursor(IntEnum):
    """Mouse cursor"""

    MOUSE_CURSOR_DEFAULT = 0
    """Default pointer shape"""

    MOUSE_CURSOR_ARROW = 1
    """Arrow shape"""

    MOUSE_CURSOR_IBEAM = 2
    """Text writing cursor shape"""

    MOUSE_CURSOR_CROSSHAIR = 3
    """Cross shape"""

    MOUSE_CURSOR_POINTING_HAND = 4
    """Pointing hand cursor"""

    MOUSE_CURSOR_RESIZE_EW = 5
    """Horizontal resize/move arrow shape"""

    MOUSE_CURSOR_RESIZE_NS = 6
    """Vertical resize/move arrow shape"""

    MOUSE_CURSOR_RESIZE_NWSE = 7
    """Top-left to bottom-right diagonal resize/move arrow shape"""

    MOUSE_CURSOR_RESIZE_NESW = 8
    """The top-right to bottom-left diagonal resize/move arrow shape"""

    MOUSE_CURSOR_RESIZE_ALL = 9
    """The omni-directional resize/move cursor shape"""

    MOUSE_CURSOR_NOT_ALLOWED = 10
    """The operation-not-allowed shape"""



MOUSE_CURSOR_DEFAULT = MouseCursor.MOUSE_CURSOR_DEFAULT
MOUSE_CURSOR_ARROW = MouseCursor.MOUSE_CURSOR_ARROW
MOUSE_CURSOR_IBEAM = MouseCursor.MOUSE_CURSOR_IBEAM
MOUSE_CURSOR_CROSSHAIR = MouseCursor.MOUSE_CURSOR_CROSSHAIR
MOUSE_CURSOR_POINTING_HAND = MouseCursor.MOUSE_CURSOR_POINTING_HAND
MOUSE_CURSOR_RESIZE_EW = MouseCursor.MOUSE_CURSOR_RESIZE_EW
MOUSE_CURSOR_RESIZE_NS = MouseCursor.MOUSE_CURSOR_RESIZE_NS
MOUSE_CURSOR_RESIZE_NWSE = MouseCursor.MOUSE_CURSOR_RESIZE_NWSE
MOUSE_CURSOR_RESIZE_NESW = MouseCursor.MOUSE_CURSOR_RESIZE_NESW
MOUSE_CURSOR_RESIZE_ALL = MouseCursor.MOUSE_CURSOR_RESIZE_ALL
MOUSE_CURSOR_NOT_ALLOWED = MouseCursor.MOUSE_CURSOR_NOT_ALLOWED


class GamepadButton(IntEnum):
    """Gamepad buttons"""

    GAMEPAD_BUTTON_UNKNOWN = 0
    """Unknown button, just for error checking"""

    GAMEPAD_BUTTON_LEFT_FACE_UP = 1
    """Gamepad left DPAD up button"""

    GAMEPAD_BUTTON_LEFT_FACE_RIGHT = 2
    """Gamepad left DPAD right button"""

    GAMEPAD_BUTTON_LEFT_FACE_DOWN = 3
    """Gamepad left DPAD down button"""

    GAMEPAD_BUTTON_LEFT_FACE_LEFT = 4
    """Gamepad left DPAD left button"""

    GAMEPAD_BUTTON_RIGHT_FACE_UP = 5
    """Gamepad right button up (i.e. PS3: Triangle, Xbox: Y)"""

    GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = 6
    """Gamepad right button right (i.e. PS3: Square, Xbox: X)"""

    GAMEPAD_BUTTON_RIGHT_FACE_DOWN = 7
    """Gamepad right button down (i.e. PS3: Cross, Xbox: A)"""

    GAMEPAD_BUTTON_RIGHT_FACE_LEFT = 8
    """Gamepad right button left (i.e. PS3: Circle, Xbox: B)"""

    GAMEPAD_BUTTON_LEFT_TRIGGER_1 = 9
    """Gamepad top/back trigger left (first), it could be a trailing button"""

    GAMEPAD_BUTTON_LEFT_TRIGGER_2 = 10
    """Gamepad top/back trigger left (second), it could be a trailing button"""

    GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = 11
    """Gamepad top/back trigger right (one), it could be a trailing button"""

    GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = 12
    """Gamepad top/back trigger right (second), it could be a trailing button"""

    GAMEPAD_BUTTON_MIDDLE_LEFT = 13
    """Gamepad center buttons, left one (i.e. PS3: Select)"""

    GAMEPAD_BUTTON_MIDDLE = 14
    """Gamepad center buttons, middle one (i.e. PS3: PS, Xbox: XBOX)"""

    GAMEPAD_BUTTON_MIDDLE_RIGHT = 15
    """Gamepad center buttons, right one (i.e. PS3: Start)"""

    GAMEPAD_BUTTON_LEFT_THUMB = 16
    """Gamepad joystick pressed button left"""

    GAMEPAD_BUTTON_RIGHT_THUMB = 17
    """Gamepad joystick pressed button right"""



GAMEPAD_BUTTON_UNKNOWN = GamepadButton.GAMEPAD_BUTTON_UNKNOWN
GAMEPAD_BUTTON_LEFT_FACE_UP = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_UP
GAMEPAD_BUTTON_LEFT_FACE_RIGHT = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_RIGHT
GAMEPAD_BUTTON_LEFT_FACE_DOWN = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_DOWN
GAMEPAD_BUTTON_LEFT_FACE_LEFT = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_LEFT
GAMEPAD_BUTTON_RIGHT_FACE_UP = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_UP
GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_RIGHT
GAMEPAD_BUTTON_RIGHT_FACE_DOWN = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_DOWN
GAMEPAD_BUTTON_RIGHT_FACE_LEFT = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_LEFT
GAMEPAD_BUTTON_LEFT_TRIGGER_1 = GamepadButton.GAMEPAD_BUTTON_LEFT_TRIGGER_1
GAMEPAD_BUTTON_LEFT_TRIGGER_2 = GamepadButton.GAMEPAD_BUTTON_LEFT_TRIGGER_2
GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = GamepadButton.GAMEPAD_BUTTON_RIGHT_TRIGGER_1
GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = GamepadButton.GAMEPAD_BUTTON_RIGHT_TRIGGER_2
GAMEPAD_BUTTON_MIDDLE_LEFT = GamepadButton.GAMEPAD_BUTTON_MIDDLE_LEFT
GAMEPAD_BUTTON_MIDDLE = GamepadButton.GAMEPAD_BUTTON_MIDDLE
GAMEPAD_BUTTON_MIDDLE_RIGHT = GamepadButton.GAMEPAD_BUTTON_MIDDLE_RIGHT
GAMEPAD_BUTTON_LEFT_THUMB = GamepadButton.GAMEPAD_BUTTON_LEFT_THUMB
GAMEPAD_BUTTON_RIGHT_THUMB = GamepadButton.GAMEPAD_BUTTON_RIGHT_THUMB


class GamepadAxis(IntEnum):
    """Gamepad axis"""

    GAMEPAD_AXIS_LEFT_X = 0
    """Gamepad left stick X axis"""

    GAMEPAD_AXIS_LEFT_Y = 1
    """Gamepad left stick Y axis"""

    GAMEPAD_AXIS_RIGHT_X = 2
    """Gamepad right stick X axis"""

    GAMEPAD_AXIS_RIGHT_Y = 3
    """Gamepad right stick Y axis"""

    GAMEPAD_AXIS_LEFT_TRIGGER = 4
    """Gamepad back trigger left, pressure level: [1..-1]"""

    GAMEPAD_AXIS_RIGHT_TRIGGER = 5
    """Gamepad back trigger right, pressure level: [1..-1]"""



GAMEPAD_AXIS_LEFT_X = GamepadAxis.GAMEPAD_AXIS_LEFT_X
GAMEPAD_AXIS_LEFT_Y = GamepadAxis.GAMEPAD_AXIS_LEFT_Y
GAMEPAD_AXIS_RIGHT_X = GamepadAxis.GAMEPAD_AXIS_RIGHT_X
GAMEPAD_AXIS_RIGHT_Y = GamepadAxis.GAMEPAD_AXIS_RIGHT_Y
GAMEPAD_AXIS_LEFT_TRIGGER = GamepadAxis.GAMEPAD_AXIS_LEFT_TRIGGER
GAMEPAD_AXIS_RIGHT_TRIGGER = GamepadAxis.GAMEPAD_AXIS_RIGHT_TRIGGER


class MaterialMapIndex(IntEnum):
    """Material map index"""

    MATERIAL_MAP_ALBEDO = 0
    """Albedo material (same as: MATERIAL_MAP_DIFFUSE)"""

    MATERIAL_MAP_METALNESS = 1
    """Metalness material (same as: MATERIAL_MAP_SPECULAR)"""

    MATERIAL_MAP_NORMAL = 2
    """Normal material"""

    MATERIAL_MAP_ROUGHNESS = 3
    """Roughness material"""

    MATERIAL_MAP_OCCLUSION = 4
    """Ambient occlusion material"""

    MATERIAL_MAP_EMISSION = 5
    """Emission material"""

    MATERIAL_MAP_HEIGHT = 6
    """Heightmap material"""

    MATERIAL_MAP_CUBEMAP = 7
    """Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)"""

    MATERIAL_MAP_IRRADIANCE = 8
    """Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)"""

    MATERIAL_MAP_PREFILTER = 9
    """Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)"""

    MATERIAL_MAP_BRDF = 10
    """Brdf material"""



MATERIAL_MAP_ALBEDO = MaterialMapIndex.MATERIAL_MAP_ALBEDO
MATERIAL_MAP_METALNESS = MaterialMapIndex.MATERIAL_MAP_METALNESS
MATERIAL_MAP_NORMAL = MaterialMapIndex.MATERIAL_MAP_NORMAL
MATERIAL_MAP_ROUGHNESS = MaterialMapIndex.MATERIAL_MAP_ROUGHNESS
MATERIAL_MAP_OCCLUSION = MaterialMapIndex.MATERIAL_MAP_OCCLUSION
MATERIAL_MAP_EMISSION = MaterialMapIndex.MATERIAL_MAP_EMISSION
MATERIAL_MAP_HEIGHT = MaterialMapIndex.MATERIAL_MAP_HEIGHT
MATERIAL_MAP_CUBEMAP = MaterialMapIndex.MATERIAL_MAP_CUBEMAP
MATERIAL_MAP_IRRADIANCE = MaterialMapIndex.MATERIAL_MAP_IRRADIANCE
MATERIAL_MAP_PREFILTER = MaterialMapIndex.MATERIAL_MAP_PREFILTER
MATERIAL_MAP_BRDF = MaterialMapIndex.MATERIAL_MAP_BRDF


class ShaderLocationIndex(IntEnum):
    """Shader location index"""

    SHADER_LOC_VERTEX_POSITION = 0
    """Shader location: vertex attribute: position"""

    SHADER_LOC_VERTEX_TEXCOORD01 = 1
    """Shader location: vertex attribute: texcoord01"""

    SHADER_LOC_VERTEX_TEXCOORD02 = 2
    """Shader location: vertex attribute: texcoord02"""

    SHADER_LOC_VERTEX_NORMAL = 3
    """Shader location: vertex attribute: normal"""

    SHADER_LOC_VERTEX_TANGENT = 4
    """Shader location: vertex attribute: tangent"""

    SHADER_LOC_VERTEX_COLOR = 5
    """Shader location: vertex attribute: color"""

    SHADER_LOC_MATRIX_MVP = 6
    """Shader location: matrix uniform: model-view-projection"""

    SHADER_LOC_MATRIX_VIEW = 7
    """Shader location: matrix uniform: view (camera transform)"""

    SHADER_LOC_MATRIX_PROJECTION = 8
    """Shader location: matrix uniform: projection"""

    SHADER_LOC_MATRIX_MODEL = 9
    """Shader location: matrix uniform: model (transform)"""

    SHADER_LOC_MATRIX_NORMAL = 10
    """Shader location: matrix uniform: normal"""

    SHADER_LOC_VECTOR_VIEW = 11
    """Shader location: vector uniform: view"""

    SHADER_LOC_COLOR_DIFFUSE = 12
    """Shader location: vector uniform: diffuse color"""

    SHADER_LOC_COLOR_SPECULAR = 13
    """Shader location: vector uniform: specular color"""

    SHADER_LOC_COLOR_AMBIENT = 14
    """Shader location: vector uniform: ambient color"""

    SHADER_LOC_MAP_ALBEDO = 15
    """Shader location: sampler2d texture: albedo (same as: SHADER_LOC_MAP_DIFFUSE)"""

    SHADER_LOC_MAP_METALNESS = 16
    """Shader location: sampler2d texture: metalness (same as: SHADER_LOC_MAP_SPECULAR)"""

    SHADER_LOC_MAP_NORMAL = 17
    """Shader location: sampler2d texture: normal"""

    SHADER_LOC_MAP_ROUGHNESS = 18
    """Shader location: sampler2d texture: roughness"""

    SHADER_LOC_MAP_OCCLUSION = 19
    """Shader location: sampler2d texture: occlusion"""

    SHADER_LOC_MAP_EMISSION = 20
    """Shader location: sampler2d texture: emission"""

    SHADER_LOC_MAP_HEIGHT = 21
    """Shader location: sampler2d texture: height"""

    SHADER_LOC_MAP_CUBEMAP = 22
    """Shader location: samplerCube texture: cubemap"""

    SHADER_LOC_MAP_IRRADIANCE = 23
    """Shader location: samplerCube texture: irradiance"""

    SHADER_LOC_MAP_PREFILTER = 24
    """Shader location: samplerCube texture: prefilter"""

    SHADER_LOC_MAP_BRDF = 25
    """Shader location: sampler2d texture: brdf"""



SHADER_LOC_VERTEX_POSITION = ShaderLocationIndex.SHADER_LOC_VERTEX_POSITION
SHADER_LOC_VERTEX_TEXCOORD01 = ShaderLocationIndex.SHADER_LOC_VERTEX_TEXCOORD01
SHADER_LOC_VERTEX_TEXCOORD02 = ShaderLocationIndex.SHADER_LOC_VERTEX_TEXCOORD02
SHADER_LOC_VERTEX_NORMAL = ShaderLocationIndex.SHADER_LOC_VERTEX_NORMAL
SHADER_LOC_VERTEX_TANGENT = ShaderLocationIndex.SHADER_LOC_VERTEX_TANGENT
SHADER_LOC_VERTEX_COLOR = ShaderLocationIndex.SHADER_LOC_VERTEX_COLOR
SHADER_LOC_MATRIX_MVP = ShaderLocationIndex.SHADER_LOC_MATRIX_MVP
SHADER_LOC_MATRIX_VIEW = ShaderLocationIndex.SHADER_LOC_MATRIX_VIEW
SHADER_LOC_MATRIX_PROJECTION = ShaderLocationIndex.SHADER_LOC_MATRIX_PROJECTION
SHADER_LOC_MATRIX_MODEL = ShaderLocationIndex.SHADER_LOC_MATRIX_MODEL
SHADER_LOC_MATRIX_NORMAL = ShaderLocationIndex.SHADER_LOC_MATRIX_NORMAL
SHADER_LOC_VECTOR_VIEW = ShaderLocationIndex.SHADER_LOC_VECTOR_VIEW
SHADER_LOC_COLOR_DIFFUSE = ShaderLocationIndex.SHADER_LOC_COLOR_DIFFUSE
SHADER_LOC_COLOR_SPECULAR = ShaderLocationIndex.SHADER_LOC_COLOR_SPECULAR
SHADER_LOC_COLOR_AMBIENT = ShaderLocationIndex.SHADER_LOC_COLOR_AMBIENT
SHADER_LOC_MAP_ALBEDO = ShaderLocationIndex.SHADER_LOC_MAP_ALBEDO
SHADER_LOC_MAP_METALNESS = ShaderLocationIndex.SHADER_LOC_MAP_METALNESS
SHADER_LOC_MAP_NORMAL = ShaderLocationIndex.SHADER_LOC_MAP_NORMAL
SHADER_LOC_MAP_ROUGHNESS = ShaderLocationIndex.SHADER_LOC_MAP_ROUGHNESS
SHADER_LOC_MAP_OCCLUSION = ShaderLocationIndex.SHADER_LOC_MAP_OCCLUSION
SHADER_LOC_MAP_EMISSION = ShaderLocationIndex.SHADER_LOC_MAP_EMISSION
SHADER_LOC_MAP_HEIGHT = ShaderLocationIndex.SHADER_LOC_MAP_HEIGHT
SHADER_LOC_MAP_CUBEMAP = ShaderLocationIndex.SHADER_LOC_MAP_CUBEMAP
SHADER_LOC_MAP_IRRADIANCE = ShaderLocationIndex.SHADER_LOC_MAP_IRRADIANCE
SHADER_LOC_MAP_PREFILTER = ShaderLocationIndex.SHADER_LOC_MAP_PREFILTER
SHADER_LOC_MAP_BRDF = ShaderLocationIndex.SHADER_LOC_MAP_BRDF


class ShaderUniformDataType(IntEnum):
    """Shader uniform data type"""

    SHADER_UNIFORM_FLOAT = 0
    """Shader uniform type: float"""

    SHADER_UNIFORM_VEC2 = 1
    """Shader uniform type: vec2 (2 float)"""

    SHADER_UNIFORM_VEC3 = 2
    """Shader uniform type: vec3 (3 float)"""

    SHADER_UNIFORM_VEC4 = 3
    """Shader uniform type: vec4 (4 float)"""

    SHADER_UNIFORM_INT = 4
    """Shader uniform type: int"""

    SHADER_UNIFORM_IVEC2 = 5
    """Shader uniform type: ivec2 (2 int)"""

    SHADER_UNIFORM_IVEC3 = 6
    """Shader uniform type: ivec3 (3 int)"""

    SHADER_UNIFORM_IVEC4 = 7
    """Shader uniform type: ivec4 (4 int)"""

    SHADER_UNIFORM_SAMPLER2D = 8
    """Shader uniform type: sampler2d"""



SHADER_UNIFORM_FLOAT = ShaderUniformDataType.SHADER_UNIFORM_FLOAT
SHADER_UNIFORM_VEC2 = ShaderUniformDataType.SHADER_UNIFORM_VEC2
SHADER_UNIFORM_VEC3 = ShaderUniformDataType.SHADER_UNIFORM_VEC3
SHADER_UNIFORM_VEC4 = ShaderUniformDataType.SHADER_UNIFORM_VEC4
SHADER_UNIFORM_INT = ShaderUniformDataType.SHADER_UNIFORM_INT
SHADER_UNIFORM_IVEC2 = ShaderUniformDataType.SHADER_UNIFORM_IVEC2
SHADER_UNIFORM_IVEC3 = ShaderUniformDataType.SHADER_UNIFORM_IVEC3
SHADER_UNIFORM_IVEC4 = ShaderUniformDataType.SHADER_UNIFORM_IVEC4
SHADER_UNIFORM_SAMPLER2D = ShaderUniformDataType.SHADER_UNIFORM_SAMPLER2D


class ShaderAttributeDataType(IntEnum):
    """Shader attribute data types"""

    SHADER_ATTRIB_FLOAT = 0
    """Shader attribute type: float"""

    SHADER_ATTRIB_VEC2 = 1
    """Shader attribute type: vec2 (2 float)"""

    SHADER_ATTRIB_VEC3 = 2
    """Shader attribute type: vec3 (3 float)"""

    SHADER_ATTRIB_VEC4 = 3
    """Shader attribute type: vec4 (4 float)"""



SHADER_ATTRIB_FLOAT = ShaderAttributeDataType.SHADER_ATTRIB_FLOAT
SHADER_ATTRIB_VEC2 = ShaderAttributeDataType.SHADER_ATTRIB_VEC2
SHADER_ATTRIB_VEC3 = ShaderAttributeDataType.SHADER_ATTRIB_VEC3
SHADER_ATTRIB_VEC4 = ShaderAttributeDataType.SHADER_ATTRIB_VEC4


class PixelFormat(IntEnum):
    """Pixel formats"""

    PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1
    """8 bit per pixel (no alpha)"""

    PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2
    """8*2 bpp (2 channels)"""

    PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3
    """16 bpp"""

    PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4
    """24 bpp"""

    PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5
    """16 bpp (1 bit alpha)"""

    PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6
    """16 bpp (4 bit alpha)"""

    PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7
    """32 bpp"""

    PIXELFORMAT_UNCOMPRESSED_R32 = 8
    """32 bpp (1 channel - float)"""

    PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9
    """32*3 bpp (3 channels - float)"""

    PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10
    """32*4 bpp (4 channels - float)"""

    PIXELFORMAT_COMPRESSED_DXT1_RGB = 11
    """4 bpp (no alpha)"""

    PIXELFORMAT_COMPRESSED_DXT1_RGBA = 12
    """4 bpp (1 bit alpha)"""

    PIXELFORMAT_COMPRESSED_DXT3_RGBA = 13
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_DXT5_RGBA = 14
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_ETC1_RGB = 15
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ETC2_RGB = 16
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 17
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_PVRT_RGB = 18
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_PVRT_RGBA = 19
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 20
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 21
    """2 bpp"""



PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = PixelFormat.PIXELFORMAT_UNCOMPRESSED_GRAYSCALE
PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = PixelFormat.PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA
PIXELFORMAT_UNCOMPRESSED_R5G6B5 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R5G6B5
PIXELFORMAT_UNCOMPRESSED_R8G8B8 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R8G8B8
PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R5G5B5A1
PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R4G4B4A4
PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R8G8B8A8
PIXELFORMAT_UNCOMPRESSED_R32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32
PIXELFORMAT_UNCOMPRESSED_R32G32B32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32G32B32
PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32G32B32A32
PIXELFORMAT_COMPRESSED_DXT1_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_DXT1_RGB
PIXELFORMAT_COMPRESSED_DXT1_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT1_RGBA
PIXELFORMAT_COMPRESSED_DXT3_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT3_RGBA
PIXELFORMAT_COMPRESSED_DXT5_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT5_RGBA
PIXELFORMAT_COMPRESSED_ETC1_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_ETC1_RGB
PIXELFORMAT_COMPRESSED_ETC2_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_ETC2_RGB
PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA
PIXELFORMAT_COMPRESSED_PVRT_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_PVRT_RGB
PIXELFORMAT_COMPRESSED_PVRT_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_PVRT_RGBA
PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA
PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA


class TextureFilter(IntEnum):
    """Texture parameters: filter mode"""

    TEXTURE_FILTER_POINT = 0
    """No filter, just pixel approximation"""

    TEXTURE_FILTER_BILINEAR = 1
    """Linear filtering"""

    TEXTURE_FILTER_TRILINEAR = 2
    """Trilinear filtering (linear with mipmaps)"""

    TEXTURE_FILTER_ANISOTROPIC_4X = 3
    """Anisotropic filtering 4x"""

    TEXTURE_FILTER_ANISOTROPIC_8X = 4
    """Anisotropic filtering 8x"""

    TEXTURE_FILTER_ANISOTROPIC_16X = 5
    """Anisotropic filtering 16x"""



TEXTURE_FILTER_POINT = TextureFilter.TEXTURE_FILTER_POINT
TEXTURE_FILTER_BILINEAR = TextureFilter.TEXTURE_FILTER_BILINEAR
TEXTURE_FILTER_TRILINEAR = TextureFilter.TEXTURE_FILTER_TRILINEAR
TEXTURE_FILTER_ANISOTROPIC_4X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_4X
TEXTURE_FILTER_ANISOTROPIC_8X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_8X
TEXTURE_FILTER_ANISOTROPIC_16X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_16X


class TextureWrap(IntEnum):
    """Texture parameters: wrap mode"""

    TEXTURE_WRAP_REPEAT = 0
    """Repeats texture in tiled mode"""

    TEXTURE_WRAP_CLAMP = 1
    """Clamps texture to edge pixel in tiled mode"""

    TEXTURE_WRAP_MIRROR_REPEAT = 2
    """Mirrors and repeats the texture in tiled mode"""

    TEXTURE_WRAP_MIRROR_CLAMP = 3
    """Mirrors and clamps to border the texture in tiled mode"""



TEXTURE_WRAP_REPEAT = TextureWrap.TEXTURE_WRAP_REPEAT
TEXTURE_WRAP_CLAMP = TextureWrap.TEXTURE_WRAP_CLAMP
TEXTURE_WRAP_MIRROR_REPEAT = TextureWrap.TEXTURE_WRAP_MIRROR_REPEAT
TEXTURE_WRAP_MIRROR_CLAMP = TextureWrap.TEXTURE_WRAP_MIRROR_CLAMP


class CubemapLayout(IntEnum):
    """Cubemap layouts"""

    CUBEMAP_LAYOUT_AUTO_DETECT = 0
    """Automatically detect layout type"""

    CUBEMAP_LAYOUT_LINE_VERTICAL = 1
    """Layout is defined by a vertical line with faces"""

    CUBEMAP_LAYOUT_LINE_HORIZONTAL = 2
    """Layout is defined by an horizontal line with faces"""

    CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = 3
    """Layout is defined by a 3x4 cross with cubemap faces"""

    CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = 4
    """Layout is defined by a 4x3 cross with cubemap faces"""

    CUBEMAP_LAYOUT_PANORAMA = 5
    """Layout is defined by a panorama image (equirectangular map)"""



CUBEMAP_LAYOUT_AUTO_DETECT = CubemapLayout.CUBEMAP_LAYOUT_AUTO_DETECT
CUBEMAP_LAYOUT_LINE_VERTICAL = CubemapLayout.CUBEMAP_LAYOUT_LINE_VERTICAL
CUBEMAP_LAYOUT_LINE_HORIZONTAL = CubemapLayout.CUBEMAP_LAYOUT_LINE_HORIZONTAL
CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = CubemapLayout.CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR
CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = CubemapLayout.CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE
CUBEMAP_LAYOUT_PANORAMA = CubemapLayout.CUBEMAP_LAYOUT_PANORAMA


class FontType(IntEnum):
    """Font type, defines generation method"""

    FONT_DEFAULT = 0
    """Default font generation, anti-aliased"""

    FONT_BITMAP = 1
    """Bitmap font generation, no anti-aliasing"""

    FONT_SDF = 2
    """SDF font generation, requires external shader"""



FONT_DEFAULT = FontType.FONT_DEFAULT
FONT_BITMAP = FontType.FONT_BITMAP
FONT_SDF = FontType.FONT_SDF


class BlendMode(IntEnum):
    """Color blending modes (pre-defined)"""

    BLEND_ALPHA = 0
    """Blend textures considering alpha (default)"""

    BLEND_ADDITIVE = 1
    """Blend textures adding colors"""

    BLEND_MULTIPLIED = 2
    """Blend textures multiplying colors"""

    BLEND_ADD_COLORS = 3
    """Blend textures adding colors (alternative)"""

    BLEND_SUBTRACT_COLORS = 4
    """Blend textures subtracting colors (alternative)"""

    BLEND_ALPHA_PREMULTIPLY = 5
    """Blend premultiplied textures considering alpha"""

    BLEND_CUSTOM = 6
    """Blend textures using custom src/dst factors (use rlSetBlendMode())"""



BLEND_ALPHA = BlendMode.BLEND_ALPHA
BLEND_ADDITIVE = BlendMode.BLEND_ADDITIVE
BLEND_MULTIPLIED = BlendMode.BLEND_MULTIPLIED
BLEND_ADD_COLORS = BlendMode.BLEND_ADD_COLORS
BLEND_SUBTRACT_COLORS = BlendMode.BLEND_SUBTRACT_COLORS
BLEND_ALPHA_PREMULTIPLY = BlendMode.BLEND_ALPHA_PREMULTIPLY
BLEND_CUSTOM = BlendMode.BLEND_CUSTOM


class Gesture(IntEnum):
    """Gesture"""

    GESTURE_NONE = 0
    """No gesture"""

    GESTURE_TAP = 1
    """Tap gesture"""

    GESTURE_DOUBLETAP = 2
    """Double tap gesture"""

    GESTURE_HOLD = 4
    """Hold gesture"""

    GESTURE_DRAG = 8
    """Drag gesture"""

    GESTURE_SWIPE_RIGHT = 16
    """Swipe right gesture"""

    GESTURE_SWIPE_LEFT = 32
    """Swipe left gesture"""

    GESTURE_SWIPE_UP = 64
    """Swipe up gesture"""

    GESTURE_SWIPE_DOWN = 128
    """Swipe down gesture"""

    GESTURE_PINCH_IN = 256
    """Pinch in gesture"""

    GESTURE_PINCH_OUT = 512
    """Pinch out gesture"""



GESTURE_NONE = Gesture.GESTURE_NONE
GESTURE_TAP = Gesture.GESTURE_TAP
GESTURE_DOUBLETAP = Gesture.GESTURE_DOUBLETAP
GESTURE_HOLD = Gesture.GESTURE_HOLD
GESTURE_DRAG = Gesture.GESTURE_DRAG
GESTURE_SWIPE_RIGHT = Gesture.GESTURE_SWIPE_RIGHT
GESTURE_SWIPE_LEFT = Gesture.GESTURE_SWIPE_LEFT
GESTURE_SWIPE_UP = Gesture.GESTURE_SWIPE_UP
GESTURE_SWIPE_DOWN = Gesture.GESTURE_SWIPE_DOWN
GESTURE_PINCH_IN = Gesture.GESTURE_PINCH_IN
GESTURE_PINCH_OUT = Gesture.GESTURE_PINCH_OUT


class CameraMode(IntEnum):
    """Camera system modes"""

    CAMERA_CUSTOM = 0
    """Custom camera"""

    CAMERA_FREE = 1
    """Free camera"""

    CAMERA_ORBITAL = 2
    """Orbital camera"""

    CAMERA_FIRST_PERSON = 3
    """First person camera"""

    CAMERA_THIRD_PERSON = 4
    """Third person camera"""



CAMERA_CUSTOM = CameraMode.CAMERA_CUSTOM
CAMERA_FREE = CameraMode.CAMERA_FREE
CAMERA_ORBITAL = CameraMode.CAMERA_ORBITAL
CAMERA_FIRST_PERSON = CameraMode.CAMERA_FIRST_PERSON
CAMERA_THIRD_PERSON = CameraMode.CAMERA_THIRD_PERSON


class CameraProjection(IntEnum):
    """Camera projection"""

    CAMERA_PERSPECTIVE = 0
    """Perspective projection"""

    CAMERA_ORTHOGRAPHIC = 1
    """Orthographic projection"""



CAMERA_PERSPECTIVE = CameraProjection.CAMERA_PERSPECTIVE
CAMERA_ORTHOGRAPHIC = CameraProjection.CAMERA_ORTHOGRAPHIC


class NPatchLayout(IntEnum):
    """N-patch layout"""

    NPATCH_NINE_PATCH = 0
    """Npatch layout: 3x3 tiles"""

    NPATCH_THREE_PATCH_VERTICAL = 1
    """Npatch layout: 1x3 tiles"""

    NPATCH_THREE_PATCH_HORIZONTAL = 2
    """Npatch layout: 3x1 tiles"""



NPATCH_NINE_PATCH = NPatchLayout.NPATCH_NINE_PATCH
NPATCH_THREE_PATCH_VERTICAL = NPatchLayout.NPATCH_THREE_PATCH_VERTICAL
NPATCH_THREE_PATCH_HORIZONTAL = NPatchLayout.NPATCH_THREE_PATCH_HORIZONTAL


class rlGlVersion(IntEnum):
    """"""

    OPENGL_11 = 1
    """"""

    OPENGL_21 = 2
    """"""

    OPENGL_33 = 3
    """"""

    OPENGL_43 = 4
    """"""

    OPENGL_ES_20 = 5
    """"""



OPENGL_11 = rlGlVersion.OPENGL_11
OPENGL_21 = rlGlVersion.OPENGL_21
OPENGL_33 = rlGlVersion.OPENGL_33
OPENGL_43 = rlGlVersion.OPENGL_43
OPENGL_ES_20 = rlGlVersion.OPENGL_ES_20


class rlFramebufferAttachType(IntEnum):
    """"""

    RL_ATTACHMENT_COLOR_CHANNEL0 = 0
    """"""

    RL_ATTACHMENT_COLOR_CHANNEL1 = 1
    """"""

    RL_ATTACHMENT_COLOR_CHANNEL2 = 2
    """"""

    RL_ATTACHMENT_COLOR_CHANNEL3 = 3
    """"""

    RL_ATTACHMENT_COLOR_CHANNEL4 = 4
    """"""

    RL_ATTACHMENT_COLOR_CHANNEL5 = 5
    """"""

    RL_ATTACHMENT_COLOR_CHANNEL6 = 6
    """"""

    RL_ATTACHMENT_COLOR_CHANNEL7 = 7
    """"""

    RL_ATTACHMENT_DEPTH = 100
    """"""

    RL_ATTACHMENT_STENCIL = 200
    """"""



RL_ATTACHMENT_COLOR_CHANNEL0 = rlFramebufferAttachType.RL_ATTACHMENT_COLOR_CHANNEL0
RL_ATTACHMENT_COLOR_CHANNEL1 = rlFramebufferAttachType.RL_ATTACHMENT_COLOR_CHANNEL1
RL_ATTACHMENT_COLOR_CHANNEL2 = rlFramebufferAttachType.RL_ATTACHMENT_COLOR_CHANNEL2
RL_ATTACHMENT_COLOR_CHANNEL3 = rlFramebufferAttachType.RL_ATTACHMENT_COLOR_CHANNEL3
RL_ATTACHMENT_COLOR_CHANNEL4 = rlFramebufferAttachType.RL_ATTACHMENT_COLOR_CHANNEL4
RL_ATTACHMENT_COLOR_CHANNEL5 = rlFramebufferAttachType.RL_ATTACHMENT_COLOR_CHANNEL5
RL_ATTACHMENT_COLOR_CHANNEL6 = rlFramebufferAttachType.RL_ATTACHMENT_COLOR_CHANNEL6
RL_ATTACHMENT_COLOR_CHANNEL7 = rlFramebufferAttachType.RL_ATTACHMENT_COLOR_CHANNEL7
RL_ATTACHMENT_DEPTH = rlFramebufferAttachType.RL_ATTACHMENT_DEPTH
RL_ATTACHMENT_STENCIL = rlFramebufferAttachType.RL_ATTACHMENT_STENCIL


class rlFramebufferAttachTextureType(IntEnum):
    """"""

    RL_ATTACHMENT_CUBEMAP_POSITIVE_X = 0
    """"""

    RL_ATTACHMENT_CUBEMAP_NEGATIVE_X = 1
    """"""

    RL_ATTACHMENT_CUBEMAP_POSITIVE_Y = 2
    """"""

    RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y = 3
    """"""

    RL_ATTACHMENT_CUBEMAP_POSITIVE_Z = 4
    """"""

    RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z = 5
    """"""

    RL_ATTACHMENT_TEXTURE2D = 100
    """"""

    RL_ATTACHMENT_RENDERBUFFER = 200
    """"""



RL_ATTACHMENT_CUBEMAP_POSITIVE_X = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_POSITIVE_X
RL_ATTACHMENT_CUBEMAP_NEGATIVE_X = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_NEGATIVE_X
RL_ATTACHMENT_CUBEMAP_POSITIVE_Y = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_POSITIVE_Y
RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y
RL_ATTACHMENT_CUBEMAP_POSITIVE_Z = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_POSITIVE_Z
RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z
RL_ATTACHMENT_TEXTURE2D = rlFramebufferAttachTextureType.RL_ATTACHMENT_TEXTURE2D
RL_ATTACHMENT_RENDERBUFFER = rlFramebufferAttachTextureType.RL_ATTACHMENT_RENDERBUFFER


class rlTraceLogLevel(IntEnum):
    """Trace log level"""

    RL_LOG_ALL = 0
    """Display all logs"""

    RL_LOG_TRACE = 1
    """Trace logging, intended for internal use only"""

    RL_LOG_DEBUG = 2
    """Debug logging, used for internal debugging, it should be disabled on release builds"""

    RL_LOG_INFO = 3
    """Info logging, used for program execution info"""

    RL_LOG_WARNING = 4
    """Warning logging, used on recoverable failures"""

    RL_LOG_ERROR = 5
    """Error logging, used on unrecoverable failures"""

    RL_LOG_FATAL = 6
    """Fatal logging, used to abort program: exit(EXIT_FAILURE)"""

    RL_LOG_NONE = 7
    """Disable logging"""



RL_LOG_ALL = rlTraceLogLevel.RL_LOG_ALL
RL_LOG_TRACE = rlTraceLogLevel.RL_LOG_TRACE
RL_LOG_DEBUG = rlTraceLogLevel.RL_LOG_DEBUG
RL_LOG_INFO = rlTraceLogLevel.RL_LOG_INFO
RL_LOG_WARNING = rlTraceLogLevel.RL_LOG_WARNING
RL_LOG_ERROR = rlTraceLogLevel.RL_LOG_ERROR
RL_LOG_FATAL = rlTraceLogLevel.RL_LOG_FATAL
RL_LOG_NONE = rlTraceLogLevel.RL_LOG_NONE


class rlPixelFormat(IntEnum):
    """Texture formats (support depends on OpenGL version)"""

    RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1
    """8 bit per pixel (no alpha)"""

    RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = 2
    """8*2 bpp (2 channels)"""

    RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5 = 3
    """16 bpp"""

    RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8 = 4
    """24 bpp"""

    RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = 5
    """16 bpp (1 bit alpha)"""

    RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = 6
    """16 bpp (4 bit alpha)"""

    RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = 7
    """32 bpp"""

    RL_PIXELFORMAT_UNCOMPRESSED_R32 = 8
    """32 bpp (1 channel - float)"""

    RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32 = 9
    """32*3 bpp (3 channels - float)"""

    RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = 10
    """32*4 bpp (4 channels - float)"""

    RL_PIXELFORMAT_COMPRESSED_DXT1_RGB = 11
    """4 bpp (no alpha)"""

    RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA = 12
    """4 bpp (1 bit alpha)"""

    RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA = 13
    """8 bpp"""

    RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA = 14
    """8 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ETC1_RGB = 15
    """4 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ETC2_RGB = 16
    """4 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 17
    """8 bpp"""

    RL_PIXELFORMAT_COMPRESSED_PVRT_RGB = 18
    """4 bpp"""

    RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA = 19
    """4 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 20
    """8 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 21
    """2 bpp"""



RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE
RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA
RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5
RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8
RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1
RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4
RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8
RL_PIXELFORMAT_UNCOMPRESSED_R32 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R32
RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32
RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32
RL_PIXELFORMAT_COMPRESSED_DXT1_RGB = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_DXT1_RGB
RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA
RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA
RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA
RL_PIXELFORMAT_COMPRESSED_ETC1_RGB = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_ETC1_RGB
RL_PIXELFORMAT_COMPRESSED_ETC2_RGB = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_ETC2_RGB
RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA
RL_PIXELFORMAT_COMPRESSED_PVRT_RGB = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_PVRT_RGB
RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA
RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA
RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = rlPixelFormat.RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA


class rlTextureFilter(IntEnum):
    """Texture parameters: filter mode"""

    RL_TEXTURE_FILTER_POINT = 0
    """No filter, just pixel approximation"""

    RL_TEXTURE_FILTER_BILINEAR = 1
    """Linear filtering"""

    RL_TEXTURE_FILTER_TRILINEAR = 2
    """Trilinear filtering (linear with mipmaps)"""

    RL_TEXTURE_FILTER_ANISOTROPIC_4X = 3
    """Anisotropic filtering 4x"""

    RL_TEXTURE_FILTER_ANISOTROPIC_8X = 4
    """Anisotropic filtering 8x"""

    RL_TEXTURE_FILTER_ANISOTROPIC_16X = 5
    """Anisotropic filtering 16x"""



RL_TEXTURE_FILTER_POINT = rlTextureFilter.RL_TEXTURE_FILTER_POINT
RL_TEXTURE_FILTER_BILINEAR = rlTextureFilter.RL_TEXTURE_FILTER_BILINEAR
RL_TEXTURE_FILTER_TRILINEAR = rlTextureFilter.RL_TEXTURE_FILTER_TRILINEAR
RL_TEXTURE_FILTER_ANISOTROPIC_4X = rlTextureFilter.RL_TEXTURE_FILTER_ANISOTROPIC_4X
RL_TEXTURE_FILTER_ANISOTROPIC_8X = rlTextureFilter.RL_TEXTURE_FILTER_ANISOTROPIC_8X
RL_TEXTURE_FILTER_ANISOTROPIC_16X = rlTextureFilter.RL_TEXTURE_FILTER_ANISOTROPIC_16X


class rlBlendMode(IntEnum):
    """Color blending modes (pre-defined)"""

    RL_BLEND_ALPHA = 0
    """Blend textures considering alpha (default)"""

    RL_BLEND_ADDITIVE = 1
    """Blend textures adding colors"""

    RL_BLEND_MULTIPLIED = 2
    """Blend textures multiplying colors"""

    RL_BLEND_ADD_COLORS = 3
    """Blend textures adding colors (alternative)"""

    RL_BLEND_SUBTRACT_COLORS = 4
    """Blend textures subtracting colors (alternative)"""

    RL_BLEND_ALPHA_PREMULTIPLY = 5
    """Blend premultiplied textures considering alpha"""

    RL_BLEND_CUSTOM = 6
    """Blend textures using custom src/dst factors (use rlSetBlendFactors())"""



RL_BLEND_ALPHA = rlBlendMode.RL_BLEND_ALPHA
RL_BLEND_ADDITIVE = rlBlendMode.RL_BLEND_ADDITIVE
RL_BLEND_MULTIPLIED = rlBlendMode.RL_BLEND_MULTIPLIED
RL_BLEND_ADD_COLORS = rlBlendMode.RL_BLEND_ADD_COLORS
RL_BLEND_SUBTRACT_COLORS = rlBlendMode.RL_BLEND_SUBTRACT_COLORS
RL_BLEND_ALPHA_PREMULTIPLY = rlBlendMode.RL_BLEND_ALPHA_PREMULTIPLY
RL_BLEND_CUSTOM = rlBlendMode.RL_BLEND_CUSTOM


class rlShaderLocationIndex(IntEnum):
    """Shader location point type"""

    RL_SHADER_LOC_VERTEX_POSITION = 0
    """Shader location: vertex attribute: position"""

    RL_SHADER_LOC_VERTEX_TEXCOORD01 = 1
    """Shader location: vertex attribute: texcoord01"""

    RL_SHADER_LOC_VERTEX_TEXCOORD02 = 2
    """Shader location: vertex attribute: texcoord02"""

    RL_SHADER_LOC_VERTEX_NORMAL = 3
    """Shader location: vertex attribute: normal"""

    RL_SHADER_LOC_VERTEX_TANGENT = 4
    """Shader location: vertex attribute: tangent"""

    RL_SHADER_LOC_VERTEX_COLOR = 5
    """Shader location: vertex attribute: color"""

    RL_SHADER_LOC_MATRIX_MVP = 6
    """Shader location: matrix uniform: model-view-projection"""

    RL_SHADER_LOC_MATRIX_VIEW = 7
    """Shader location: matrix uniform: view (camera transform)"""

    RL_SHADER_LOC_MATRIX_PROJECTION = 8
    """Shader location: matrix uniform: projection"""

    RL_SHADER_LOC_MATRIX_MODEL = 9
    """Shader location: matrix uniform: model (transform)"""

    RL_SHADER_LOC_MATRIX_NORMAL = 10
    """Shader location: matrix uniform: normal"""

    RL_SHADER_LOC_VECTOR_VIEW = 11
    """Shader location: vector uniform: view"""

    RL_SHADER_LOC_COLOR_DIFFUSE = 12
    """Shader location: vector uniform: diffuse color"""

    RL_SHADER_LOC_COLOR_SPECULAR = 13
    """Shader location: vector uniform: specular color"""

    RL_SHADER_LOC_COLOR_AMBIENT = 14
    """Shader location: vector uniform: ambient color"""

    RL_SHADER_LOC_MAP_ALBEDO = 15
    """Shader location: sampler2d texture: albedo (same as: RL_SHADER_LOC_MAP_DIFFUSE)"""

    RL_SHADER_LOC_MAP_METALNESS = 16
    """Shader location: sampler2d texture: metalness (same as: RL_SHADER_LOC_MAP_SPECULAR)"""

    RL_SHADER_LOC_MAP_NORMAL = 17
    """Shader location: sampler2d texture: normal"""

    RL_SHADER_LOC_MAP_ROUGHNESS = 18
    """Shader location: sampler2d texture: roughness"""

    RL_SHADER_LOC_MAP_OCCLUSION = 19
    """Shader location: sampler2d texture: occlusion"""

    RL_SHADER_LOC_MAP_EMISSION = 20
    """Shader location: sampler2d texture: emission"""

    RL_SHADER_LOC_MAP_HEIGHT = 21
    """Shader location: sampler2d texture: height"""

    RL_SHADER_LOC_MAP_CUBEMAP = 22
    """Shader location: samplerCube texture: cubemap"""

    RL_SHADER_LOC_MAP_IRRADIANCE = 23
    """Shader location: samplerCube texture: irradiance"""

    RL_SHADER_LOC_MAP_PREFILTER = 24
    """Shader location: samplerCube texture: prefilter"""

    RL_SHADER_LOC_MAP_BRDF = 25
    """Shader location: sampler2d texture: brdf"""



RL_SHADER_LOC_VERTEX_POSITION = rlShaderLocationIndex.RL_SHADER_LOC_VERTEX_POSITION
RL_SHADER_LOC_VERTEX_TEXCOORD01 = rlShaderLocationIndex.RL_SHADER_LOC_VERTEX_TEXCOORD01
RL_SHADER_LOC_VERTEX_TEXCOORD02 = rlShaderLocationIndex.RL_SHADER_LOC_VERTEX_TEXCOORD02
RL_SHADER_LOC_VERTEX_NORMAL = rlShaderLocationIndex.RL_SHADER_LOC_VERTEX_NORMAL
RL_SHADER_LOC_VERTEX_TANGENT = rlShaderLocationIndex.RL_SHADER_LOC_VERTEX_TANGENT
RL_SHADER_LOC_VERTEX_COLOR = rlShaderLocationIndex.RL_SHADER_LOC_VERTEX_COLOR
RL_SHADER_LOC_MATRIX_MVP = rlShaderLocationIndex.RL_SHADER_LOC_MATRIX_MVP
RL_SHADER_LOC_MATRIX_VIEW = rlShaderLocationIndex.RL_SHADER_LOC_MATRIX_VIEW
RL_SHADER_LOC_MATRIX_PROJECTION = rlShaderLocationIndex.RL_SHADER_LOC_MATRIX_PROJECTION
RL_SHADER_LOC_MATRIX_MODEL = rlShaderLocationIndex.RL_SHADER_LOC_MATRIX_MODEL
RL_SHADER_LOC_MATRIX_NORMAL = rlShaderLocationIndex.RL_SHADER_LOC_MATRIX_NORMAL
RL_SHADER_LOC_VECTOR_VIEW = rlShaderLocationIndex.RL_SHADER_LOC_VECTOR_VIEW
RL_SHADER_LOC_COLOR_DIFFUSE = rlShaderLocationIndex.RL_SHADER_LOC_COLOR_DIFFUSE
RL_SHADER_LOC_COLOR_SPECULAR = rlShaderLocationIndex.RL_SHADER_LOC_COLOR_SPECULAR
RL_SHADER_LOC_COLOR_AMBIENT = rlShaderLocationIndex.RL_SHADER_LOC_COLOR_AMBIENT
RL_SHADER_LOC_MAP_ALBEDO = rlShaderLocationIndex.RL_SHADER_LOC_MAP_ALBEDO
RL_SHADER_LOC_MAP_METALNESS = rlShaderLocationIndex.RL_SHADER_LOC_MAP_METALNESS
RL_SHADER_LOC_MAP_NORMAL = rlShaderLocationIndex.RL_SHADER_LOC_MAP_NORMAL
RL_SHADER_LOC_MAP_ROUGHNESS = rlShaderLocationIndex.RL_SHADER_LOC_MAP_ROUGHNESS
RL_SHADER_LOC_MAP_OCCLUSION = rlShaderLocationIndex.RL_SHADER_LOC_MAP_OCCLUSION
RL_SHADER_LOC_MAP_EMISSION = rlShaderLocationIndex.RL_SHADER_LOC_MAP_EMISSION
RL_SHADER_LOC_MAP_HEIGHT = rlShaderLocationIndex.RL_SHADER_LOC_MAP_HEIGHT
RL_SHADER_LOC_MAP_CUBEMAP = rlShaderLocationIndex.RL_SHADER_LOC_MAP_CUBEMAP
RL_SHADER_LOC_MAP_IRRADIANCE = rlShaderLocationIndex.RL_SHADER_LOC_MAP_IRRADIANCE
RL_SHADER_LOC_MAP_PREFILTER = rlShaderLocationIndex.RL_SHADER_LOC_MAP_PREFILTER
RL_SHADER_LOC_MAP_BRDF = rlShaderLocationIndex.RL_SHADER_LOC_MAP_BRDF


class rlShaderUniformDataType(IntEnum):
    """Shader uniform data type"""

    RL_SHADER_UNIFORM_FLOAT = 0
    """Shader uniform type: float"""

    RL_SHADER_UNIFORM_VEC2 = 1
    """Shader uniform type: vec2 (2 float)"""

    RL_SHADER_UNIFORM_VEC3 = 2
    """Shader uniform type: vec3 (3 float)"""

    RL_SHADER_UNIFORM_VEC4 = 3
    """Shader uniform type: vec4 (4 float)"""

    RL_SHADER_UNIFORM_INT = 4
    """Shader uniform type: int"""

    RL_SHADER_UNIFORM_IVEC2 = 5
    """Shader uniform type: ivec2 (2 int)"""

    RL_SHADER_UNIFORM_IVEC3 = 6
    """Shader uniform type: ivec3 (3 int)"""

    RL_SHADER_UNIFORM_IVEC4 = 7
    """Shader uniform type: ivec4 (4 int)"""

    RL_SHADER_UNIFORM_SAMPLER2D = 8
    """Shader uniform type: sampler2d"""



RL_SHADER_UNIFORM_FLOAT = rlShaderUniformDataType.RL_SHADER_UNIFORM_FLOAT
RL_SHADER_UNIFORM_VEC2 = rlShaderUniformDataType.RL_SHADER_UNIFORM_VEC2
RL_SHADER_UNIFORM_VEC3 = rlShaderUniformDataType.RL_SHADER_UNIFORM_VEC3
RL_SHADER_UNIFORM_VEC4 = rlShaderUniformDataType.RL_SHADER_UNIFORM_VEC4
RL_SHADER_UNIFORM_INT = rlShaderUniformDataType.RL_SHADER_UNIFORM_INT
RL_SHADER_UNIFORM_IVEC2 = rlShaderUniformDataType.RL_SHADER_UNIFORM_IVEC2
RL_SHADER_UNIFORM_IVEC3 = rlShaderUniformDataType.RL_SHADER_UNIFORM_IVEC3
RL_SHADER_UNIFORM_IVEC4 = rlShaderUniformDataType.RL_SHADER_UNIFORM_IVEC4
RL_SHADER_UNIFORM_SAMPLER2D = rlShaderUniformDataType.RL_SHADER_UNIFORM_SAMPLER2D


class rlShaderAttributeDataType(IntEnum):
    """Shader attribute data types"""

    RL_SHADER_ATTRIB_FLOAT = 0
    """Shader attribute type: float"""

    RL_SHADER_ATTRIB_VEC2 = 1
    """Shader attribute type: vec2 (2 float)"""

    RL_SHADER_ATTRIB_VEC3 = 2
    """Shader attribute type: vec3 (3 float)"""

    RL_SHADER_ATTRIB_VEC4 = 3
    """Shader attribute type: vec4 (4 float)"""



RL_SHADER_ATTRIB_FLOAT = rlShaderAttributeDataType.RL_SHADER_ATTRIB_FLOAT
RL_SHADER_ATTRIB_VEC2 = rlShaderAttributeDataType.RL_SHADER_ATTRIB_VEC2
RL_SHADER_ATTRIB_VEC3 = rlShaderAttributeDataType.RL_SHADER_ATTRIB_VEC3
RL_SHADER_ATTRIB_VEC4 = rlShaderAttributeDataType.RL_SHADER_ATTRIB_VEC4



RAYLIB_VERSION = '4.2'

PI = 3.141592653589793

DEG2RAD = (PI / 180.0)

RAD2DEG = (180.0 / PI)
# Light Gray
LIGHTGRAY = Color( 200, 200, 200, 255 )
# Gray
GRAY = Color( 130, 130, 130, 255 )
# Dark Gray
DARKGRAY = Color( 80, 80, 80, 255 )
# Yellow
YELLOW = Color( 253, 249, 0, 255 )
# Gold
GOLD = Color( 255, 203, 0, 255 )
# Orange
ORANGE = Color( 255, 161, 0, 255 )
# Pink
PINK = Color( 255, 109, 194, 255 )
# Red
RED = Color( 230, 41, 55, 255 )
# Maroon
MAROON = Color( 190, 33, 55, 255 )
# Green
GREEN = Color( 0, 228, 48, 255 )
# Lime
LIME = Color( 0, 158, 47, 255 )
# Dark Green
DARKGREEN = Color( 0, 117, 44, 255 )
# Sky Blue
SKYBLUE = Color( 102, 191, 255, 255 )
# Blue
BLUE = Color( 0, 121, 241, 255 )
# Dark Blue
DARKBLUE = Color( 0, 82, 172, 255 )
# Purple
PURPLE = Color( 200, 122, 255, 255 )
# Violet
VIOLET = Color( 135, 60, 190, 255 )
# Dark Purple
DARKPURPLE = Color( 112, 31, 126, 255 )
# Beige
BEIGE = Color( 211, 176, 131, 255 )
# Brown
BROWN = Color( 127, 106, 79, 255 )
# Dark Brown
DARKBROWN = Color( 76, 63, 47, 255 )
# White
WHITE = Color( 255, 255, 255, 255 )
# Black
BLACK = Color( 0, 0, 0, 255 )
# Blank (Transparent)
BLANK = Color( 0, 0, 0, 0 )
# Magenta
MAGENTA = Color( 255, 0, 255, 255 )
# My own White (raylib logo)
RAYWHITE = Color( 245, 245, 245, 255 )

RLGL_VERSION = '4.0'

RL_DEFAULT_BATCH_BUFFER_ELEMENTS = 8192

RL_DEFAULT_BATCH_BUFFERS = 1

RL_DEFAULT_BATCH_DRAWCALLS = 256

RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS = 4

RL_MAX_MATRIX_STACK_SIZE = 32

RL_MAX_SHADER_LOCATIONS = 32

RL_CULL_DISTANCE_NEAR = 0.01

RL_CULL_DISTANCE_FAR = 1000.0

RL_TEXTURE_WRAP_S = 10242

RL_TEXTURE_WRAP_T = 10243

RL_TEXTURE_MAG_FILTER = 10240

RL_TEXTURE_MIN_FILTER = 10241

RL_TEXTURE_FILTER_NEAREST = 9728

RL_TEXTURE_FILTER_LINEAR = 9729

RL_TEXTURE_FILTER_MIP_NEAREST = 9984

RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR = 9986

RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST = 9985

RL_TEXTURE_FILTER_MIP_LINEAR = 9987

RL_TEXTURE_FILTER_ANISOTROPIC = 12288

RL_TEXTURE_WRAP_REPEAT = 10497

RL_TEXTURE_WRAP_CLAMP = 33071

RL_TEXTURE_WRAP_MIRROR_REPEAT = 33648

RL_TEXTURE_WRAP_MIRROR_CLAMP = 34626

RL_MODELVIEW = 5888

RL_PROJECTION = 5889

RL_TEXTURE = 5890

RL_LINES = 1

RL_TRIANGLES = 4

RL_QUADS = 7

RL_UNSIGNED_BYTE = 5121

RL_FLOAT = 5126

RL_STREAM_DRAW = 35040

RL_STREAM_READ = 35041

RL_STREAM_COPY = 35042

RL_STATIC_DRAW = 35044

RL_STATIC_READ = 35045

RL_STATIC_COPY = 35046

RL_DYNAMIC_DRAW = 35048

RL_DYNAMIC_READ = 35049

RL_DYNAMIC_COPY = 35050

RL_FRAGMENT_SHADER = 35632

RL_VERTEX_SHADER = 35633

RL_COMPUTE_SHADER = 37305

# Logging: Redirect trace log messages
TraceLogCallback = CFUNCTYPE(None, Int, CharPtr, VoidPtr)

# FileIO: Load binary data
LoadFileDataCallback = CFUNCTYPE(UCharPtr, CharPtr, UIntPtr)

# FileIO: Save binary data
SaveFileDataCallback = CFUNCTYPE(Bool, CharPtr, VoidPtr, UInt)

# FileIO: Load text data
LoadFileTextCallback = CFUNCTYPE(CharPtr, CharPtr)

# FileIO: Save text data
SaveFileTextCallback = CFUNCTYPE(Bool, CharPtr, CharPtr)

# 
AudioCallback = CFUNCTYPE(None, VoidPtr, UInt)
_InitWindow = _wrap(rlapi.InitWindow, [Int, Int, CharPtr], None)
_WindowShouldClose = _wrap(rlapi.WindowShouldClose, [], Bool)
_CloseWindow = _wrap(rlapi.CloseWindow, [], None)
_IsWindowReady = _wrap(rlapi.IsWindowReady, [], Bool)
_IsWindowFullscreen = _wrap(rlapi.IsWindowFullscreen, [], Bool)
_IsWindowHidden = _wrap(rlapi.IsWindowHidden, [], Bool)
_IsWindowMinimized = _wrap(rlapi.IsWindowMinimized, [], Bool)
_IsWindowMaximized = _wrap(rlapi.IsWindowMaximized, [], Bool)
_IsWindowFocused = _wrap(rlapi.IsWindowFocused, [], Bool)
_IsWindowResized = _wrap(rlapi.IsWindowResized, [], Bool)
_IsWindowState = _wrap(rlapi.IsWindowState, [UInt], Bool)
_SetWindowState = _wrap(rlapi.SetWindowState, [UInt], None)
_ClearWindowState = _wrap(rlapi.ClearWindowState, [UInt], None)
_ToggleFullscreen = _wrap(rlapi.ToggleFullscreen, [], None)
_MaximizeWindow = _wrap(rlapi.MaximizeWindow, [], None)
_MinimizeWindow = _wrap(rlapi.MinimizeWindow, [], None)
_RestoreWindow = _wrap(rlapi.RestoreWindow, [], None)
_SetWindowIcon = _wrap(rlapi.SetWindowIcon, [Image], None)
_SetWindowTitle = _wrap(rlapi.SetWindowTitle, [CharPtr], None)
_SetWindowPosition = _wrap(rlapi.SetWindowPosition, [Int, Int], None)
_SetWindowMonitor = _wrap(rlapi.SetWindowMonitor, [Int], None)
_SetWindowMinSize = _wrap(rlapi.SetWindowMinSize, [Int, Int], None)
_SetWindowSize = _wrap(rlapi.SetWindowSize, [Int, Int], None)
_SetWindowOpacity = _wrap(rlapi.SetWindowOpacity, [Float], None)
_GetWindowHandle = _wrap(rlapi.GetWindowHandle, [], VoidPtr)
_GetScreenWidth = _wrap(rlapi.GetScreenWidth, [], Int)
_GetScreenHeight = _wrap(rlapi.GetScreenHeight, [], Int)
_GetRenderWidth = _wrap(rlapi.GetRenderWidth, [], Int)
_GetRenderHeight = _wrap(rlapi.GetRenderHeight, [], Int)
_GetMonitorCount = _wrap(rlapi.GetMonitorCount, [], Int)
_GetCurrentMonitor = _wrap(rlapi.GetCurrentMonitor, [], Int)
_GetMonitorPosition = _wrap(rlapi.GetMonitorPosition, [Int], Vector2)
_GetMonitorWidth = _wrap(rlapi.GetMonitorWidth, [Int], Int)
_GetMonitorHeight = _wrap(rlapi.GetMonitorHeight, [Int], Int)
_GetMonitorPhysicalWidth = _wrap(rlapi.GetMonitorPhysicalWidth, [Int], Int)
_GetMonitorPhysicalHeight = _wrap(rlapi.GetMonitorPhysicalHeight, [Int], Int)
_GetMonitorRefreshRate = _wrap(rlapi.GetMonitorRefreshRate, [Int], Int)
_GetWindowPosition = _wrap(rlapi.GetWindowPosition, [], Vector2)
_GetWindowScaleDPI = _wrap(rlapi.GetWindowScaleDPI, [], Vector2)
_GetMonitorName = _wrap(rlapi.GetMonitorName, [Int], CharPtr)
_SetClipboardText = _wrap(rlapi.SetClipboardText, [CharPtr], None)
_GetClipboardText = _wrap(rlapi.GetClipboardText, [], CharPtr)
_EnableEventWaiting = _wrap(rlapi.EnableEventWaiting, [], None)
_DisableEventWaiting = _wrap(rlapi.DisableEventWaiting, [], None)
_SwapScreenBuffer = _wrap(rlapi.SwapScreenBuffer, [], None)
_PollInputEvents = _wrap(rlapi.PollInputEvents, [], None)
_WaitTime = _wrap(rlapi.WaitTime, [Double], None)
_ShowCursor = _wrap(rlapi.ShowCursor, [], None)
_HideCursor = _wrap(rlapi.HideCursor, [], None)
_IsCursorHidden = _wrap(rlapi.IsCursorHidden, [], Bool)
_EnableCursor = _wrap(rlapi.EnableCursor, [], None)
_DisableCursor = _wrap(rlapi.DisableCursor, [], None)
_IsCursorOnScreen = _wrap(rlapi.IsCursorOnScreen, [], Bool)
_ClearBackground = _wrap(rlapi.ClearBackground, [Color], None)
_BeginDrawing = _wrap(rlapi.BeginDrawing, [], None)
_EndDrawing = _wrap(rlapi.EndDrawing, [], None)
_BeginMode2D = _wrap(rlapi.BeginMode2D, [Camera2D], None)
_EndMode2D = _wrap(rlapi.EndMode2D, [], None)
_BeginMode3D = _wrap(rlapi.BeginMode3D, [Camera3D], None)
_EndMode3D = _wrap(rlapi.EndMode3D, [], None)
_BeginTextureMode = _wrap(rlapi.BeginTextureMode, [RenderTexture2D], None)
_EndTextureMode = _wrap(rlapi.EndTextureMode, [], None)
_BeginShaderMode = _wrap(rlapi.BeginShaderMode, [Shader], None)
_EndShaderMode = _wrap(rlapi.EndShaderMode, [], None)
_BeginBlendMode = _wrap(rlapi.BeginBlendMode, [Int], None)
_EndBlendMode = _wrap(rlapi.EndBlendMode, [], None)
_BeginScissorMode = _wrap(rlapi.BeginScissorMode, [Int, Int, Int, Int], None)
_EndScissorMode = _wrap(rlapi.EndScissorMode, [], None)
_BeginVrStereoMode = _wrap(rlapi.BeginVrStereoMode, [VrStereoConfig], None)
_EndVrStereoMode = _wrap(rlapi.EndVrStereoMode, [], None)
_LoadVrStereoConfig = _wrap(rlapi.LoadVrStereoConfig, [VrDeviceInfo], VrStereoConfig)
_UnloadVrStereoConfig = _wrap(rlapi.UnloadVrStereoConfig, [VrStereoConfig], None)
_LoadShader = _wrap(rlapi.LoadShader, [CharPtr, CharPtr], Shader)
_LoadShaderFromMemory = _wrap(rlapi.LoadShaderFromMemory, [CharPtr, CharPtr], Shader)
_GetShaderLocation = _wrap(rlapi.GetShaderLocation, [Shader, CharPtr], Int)
_GetShaderLocationAttrib = _wrap(rlapi.GetShaderLocationAttrib, [Shader, CharPtr], Int)
_SetShaderValue = _wrap(rlapi.SetShaderValue, [Shader, Int, VoidPtr, Int], None)
_SetShaderValueV = _wrap(rlapi.SetShaderValueV, [Shader, Int, VoidPtr, Int, Int], None)
_SetShaderValueMatrix = _wrap(rlapi.SetShaderValueMatrix, [Shader, Int, Matrix], None)
_SetShaderValueTexture = _wrap(rlapi.SetShaderValueTexture, [Shader, Int, Texture2D], None)
_UnloadShader = _wrap(rlapi.UnloadShader, [Shader], None)
_GetMouseRay = _wrap(rlapi.GetMouseRay, [Vector2, Camera], Ray)
_GetCameraMatrix = _wrap(rlapi.GetCameraMatrix, [Camera], Matrix)
_GetCameraMatrix2D = _wrap(rlapi.GetCameraMatrix2D, [Camera2D], Matrix)
_GetWorldToScreen = _wrap(rlapi.GetWorldToScreen, [Vector3, Camera], Vector2)
_GetScreenToWorld2D = _wrap(rlapi.GetScreenToWorld2D, [Vector2, Camera2D], Vector2)
_GetWorldToScreenEx = _wrap(rlapi.GetWorldToScreenEx, [Vector3, Camera, Int, Int], Vector2)
_GetWorldToScreen2D = _wrap(rlapi.GetWorldToScreen2D, [Vector2, Camera2D], Vector2)
_SetTargetFPS = _wrap(rlapi.SetTargetFPS, [Int], None)
_GetFPS = _wrap(rlapi.GetFPS, [], Int)
_GetFrameTime = _wrap(rlapi.GetFrameTime, [], Float)
_GetTime = _wrap(rlapi.GetTime, [], Double)
_GetRandomValue = _wrap(rlapi.GetRandomValue, [Int, Int], Int)
_SetRandomSeed = _wrap(rlapi.SetRandomSeed, [UInt], None)
_TakeScreenshot = _wrap(rlapi.TakeScreenshot, [CharPtr], None)
_SetConfigFlags = _wrap(rlapi.SetConfigFlags, [UInt], None)
_TraceLog = _wrap(rlapi.TraceLog, [Int, CharPtr, VoidPtr], None)
_SetTraceLogLevel = _wrap(rlapi.SetTraceLogLevel, [Int], None)
_MemAlloc = _wrap(rlapi.MemAlloc, [Int], VoidPtr)
_MemRealloc = _wrap(rlapi.MemRealloc, [VoidPtr, Int], VoidPtr)
_MemFree = _wrap(rlapi.MemFree, [VoidPtr], None)
_OpenURL = _wrap(rlapi.OpenURL, [CharPtr], None)
_SetTraceLogCallback = _wrap(rlapi.SetTraceLogCallback, [TraceLogCallback], None)
_SetLoadFileDataCallback = _wrap(rlapi.SetLoadFileDataCallback, [LoadFileDataCallback], None)
_SetSaveFileDataCallback = _wrap(rlapi.SetSaveFileDataCallback, [SaveFileDataCallback], None)
_SetLoadFileTextCallback = _wrap(rlapi.SetLoadFileTextCallback, [LoadFileTextCallback], None)
_SetSaveFileTextCallback = _wrap(rlapi.SetSaveFileTextCallback, [SaveFileTextCallback], None)
_LoadFileData = _wrap(rlapi.LoadFileData, [CharPtr, UIntPtr], UCharPtr)
_UnloadFileData = _wrap(rlapi.UnloadFileData, [UCharPtr], None)
_SaveFileData = _wrap(rlapi.SaveFileData, [CharPtr, VoidPtr, UInt], Bool)
_ExportDataAsCode = _wrap(rlapi.ExportDataAsCode, [CharPtr, UInt, CharPtr], Bool)
_LoadFileText = _wrap(rlapi.LoadFileText, [CharPtr], CharPtr)
_UnloadFileText = _wrap(rlapi.UnloadFileText, [CharPtr], None)
_SaveFileText = _wrap(rlapi.SaveFileText, [CharPtr, CharPtr], Bool)
_FileExists = _wrap(rlapi.FileExists, [CharPtr], Bool)
_DirectoryExists = _wrap(rlapi.DirectoryExists, [CharPtr], Bool)
_IsFileExtension = _wrap(rlapi.IsFileExtension, [CharPtr, CharPtr], Bool)
_GetFileLength = _wrap(rlapi.GetFileLength, [CharPtr], Int)
_GetFileExtension = _wrap(rlapi.GetFileExtension, [CharPtr], CharPtr)
_GetFileName = _wrap(rlapi.GetFileName, [CharPtr], CharPtr)
_GetFileNameWithoutExt = _wrap(rlapi.GetFileNameWithoutExt, [CharPtr], CharPtr)
_GetDirectoryPath = _wrap(rlapi.GetDirectoryPath, [CharPtr], CharPtr)
_GetPrevDirectoryPath = _wrap(rlapi.GetPrevDirectoryPath, [CharPtr], CharPtr)
_GetWorkingDirectory = _wrap(rlapi.GetWorkingDirectory, [], CharPtr)
_GetApplicationDirectory = _wrap(rlapi.GetApplicationDirectory, [], CharPtr)
_ChangeDirectory = _wrap(rlapi.ChangeDirectory, [CharPtr], Bool)
_IsPathFile = _wrap(rlapi.IsPathFile, [CharPtr], Bool)
_LoadDirectoryFiles = _wrap(rlapi.LoadDirectoryFiles, [CharPtr], FilePathList)
_LoadDirectoryFilesEx = _wrap(rlapi.LoadDirectoryFilesEx, [CharPtr, CharPtr, Bool], FilePathList)
_UnloadDirectoryFiles = _wrap(rlapi.UnloadDirectoryFiles, [FilePathList], None)
_IsFileDropped = _wrap(rlapi.IsFileDropped, [], Bool)
_LoadDroppedFiles = _wrap(rlapi.LoadDroppedFiles, [], FilePathList)
_UnloadDroppedFiles = _wrap(rlapi.UnloadDroppedFiles, [FilePathList], None)
_GetFileModTime = _wrap(rlapi.GetFileModTime, [CharPtr], Long)
_CompressData = _wrap(rlapi.CompressData, [UCharPtr, Int, IntPtr], UCharPtr)
_DecompressData = _wrap(rlapi.DecompressData, [UCharPtr, Int, IntPtr], UCharPtr)
_EncodeDataBase64 = _wrap(rlapi.EncodeDataBase64, [UCharPtr, Int, IntPtr], CharPtr)
_DecodeDataBase64 = _wrap(rlapi.DecodeDataBase64, [UCharPtr, IntPtr], UCharPtr)
_IsKeyPressed = _wrap(rlapi.IsKeyPressed, [Int], Bool)
_IsKeyDown = _wrap(rlapi.IsKeyDown, [Int], Bool)
_IsKeyReleased = _wrap(rlapi.IsKeyReleased, [Int], Bool)
_IsKeyUp = _wrap(rlapi.IsKeyUp, [Int], Bool)
_SetExitKey = _wrap(rlapi.SetExitKey, [Int], None)
_GetKeyPressed = _wrap(rlapi.GetKeyPressed, [], Int)
_GetCharPressed = _wrap(rlapi.GetCharPressed, [], Int)
_IsGamepadAvailable = _wrap(rlapi.IsGamepadAvailable, [Int], Bool)
_GetGamepadName = _wrap(rlapi.GetGamepadName, [Int], CharPtr)
_IsGamepadButtonPressed = _wrap(rlapi.IsGamepadButtonPressed, [Int, Int], Bool)
_IsGamepadButtonDown = _wrap(rlapi.IsGamepadButtonDown, [Int, Int], Bool)
_IsGamepadButtonReleased = _wrap(rlapi.IsGamepadButtonReleased, [Int, Int], Bool)
_IsGamepadButtonUp = _wrap(rlapi.IsGamepadButtonUp, [Int, Int], Bool)
_GetGamepadButtonPressed = _wrap(rlapi.GetGamepadButtonPressed, [], Int)
_GetGamepadAxisCount = _wrap(rlapi.GetGamepadAxisCount, [Int], Int)
_GetGamepadAxisMovement = _wrap(rlapi.GetGamepadAxisMovement, [Int, Int], Float)
_SetGamepadMappings = _wrap(rlapi.SetGamepadMappings, [CharPtr], Int)
_IsMouseButtonPressed = _wrap(rlapi.IsMouseButtonPressed, [Int], Bool)
_IsMouseButtonDown = _wrap(rlapi.IsMouseButtonDown, [Int], Bool)
_IsMouseButtonReleased = _wrap(rlapi.IsMouseButtonReleased, [Int], Bool)
_IsMouseButtonUp = _wrap(rlapi.IsMouseButtonUp, [Int], Bool)
_GetMouseX = _wrap(rlapi.GetMouseX, [], Int)
_GetMouseY = _wrap(rlapi.GetMouseY, [], Int)
_GetMousePosition = _wrap(rlapi.GetMousePosition, [], Vector2)
_GetMouseDelta = _wrap(rlapi.GetMouseDelta, [], Vector2)
_SetMousePosition = _wrap(rlapi.SetMousePosition, [Int, Int], None)
_SetMouseOffset = _wrap(rlapi.SetMouseOffset, [Int, Int], None)
_SetMouseScale = _wrap(rlapi.SetMouseScale, [Float, Float], None)
_GetMouseWheelMove = _wrap(rlapi.GetMouseWheelMove, [], Float)
_GetMouseWheelMoveV = _wrap(rlapi.GetMouseWheelMoveV, [], Vector2)
_SetMouseCursor = _wrap(rlapi.SetMouseCursor, [Int], None)
_GetTouchX = _wrap(rlapi.GetTouchX, [], Int)
_GetTouchY = _wrap(rlapi.GetTouchY, [], Int)
_GetTouchPosition = _wrap(rlapi.GetTouchPosition, [Int], Vector2)
_GetTouchPointId = _wrap(rlapi.GetTouchPointId, [Int], Int)
_GetTouchPointCount = _wrap(rlapi.GetTouchPointCount, [], Int)
_SetGesturesEnabled = _wrap(rlapi.SetGesturesEnabled, [UInt], None)
_IsGestureDetected = _wrap(rlapi.IsGestureDetected, [Int], Bool)
_GetGestureDetected = _wrap(rlapi.GetGestureDetected, [], Int)
_GetGestureHoldDuration = _wrap(rlapi.GetGestureHoldDuration, [], Float)
_GetGestureDragVector = _wrap(rlapi.GetGestureDragVector, [], Vector2)
_GetGestureDragAngle = _wrap(rlapi.GetGestureDragAngle, [], Float)
_GetGesturePinchVector = _wrap(rlapi.GetGesturePinchVector, [], Vector2)
_GetGesturePinchAngle = _wrap(rlapi.GetGesturePinchAngle, [], Float)
_SetCameraMode = _wrap(rlapi.SetCameraMode, [Camera, Int], None)
_UpdateCamera = _wrap(rlapi.UpdateCamera, [CameraPtr], None)
_SetCameraPanControl = _wrap(rlapi.SetCameraPanControl, [Int], None)
_SetCameraAltControl = _wrap(rlapi.SetCameraAltControl, [Int], None)
_SetCameraSmoothZoomControl = _wrap(rlapi.SetCameraSmoothZoomControl, [Int], None)
_SetCameraMoveControls = _wrap(rlapi.SetCameraMoveControls, [Int, Int, Int, Int, Int, Int], None)
_SetShapesTexture = _wrap(rlapi.SetShapesTexture, [Texture2D, Rectangle], None)
_DrawPixel = _wrap(rlapi.DrawPixel, [Int, Int, Color], None)
_DrawPixelV = _wrap(rlapi.DrawPixelV, [Vector2, Color], None)
_DrawLine = _wrap(rlapi.DrawLine, [Int, Int, Int, Int, Color], None)
_DrawLineV = _wrap(rlapi.DrawLineV, [Vector2, Vector2, Color], None)
_DrawLineEx = _wrap(rlapi.DrawLineEx, [Vector2, Vector2, Float, Color], None)
_DrawLineBezier = _wrap(rlapi.DrawLineBezier, [Vector2, Vector2, Float, Color], None)
_DrawLineBezierQuad = _wrap(rlapi.DrawLineBezierQuad, [Vector2, Vector2, Vector2, Float, Color], None)
_DrawLineBezierCubic = _wrap(rlapi.DrawLineBezierCubic, [Vector2, Vector2, Vector2, Vector2, Float, Color], None)
_DrawLineStrip = _wrap(rlapi.DrawLineStrip, [Vector2Ptr, Int, Color], None)
_DrawCircle = _wrap(rlapi.DrawCircle, [Int, Int, Float, Color], None)
_DrawCircleSector = _wrap(rlapi.DrawCircleSector, [Vector2, Float, Float, Float, Int, Color], None)
_DrawCircleSectorLines = _wrap(rlapi.DrawCircleSectorLines, [Vector2, Float, Float, Float, Int, Color], None)
_DrawCircleGradient = _wrap(rlapi.DrawCircleGradient, [Int, Int, Float, Color, Color], None)
_DrawCircleV = _wrap(rlapi.DrawCircleV, [Vector2, Float, Color], None)
_DrawCircleLines = _wrap(rlapi.DrawCircleLines, [Int, Int, Float, Color], None)
_DrawEllipse = _wrap(rlapi.DrawEllipse, [Int, Int, Float, Float, Color], None)
_DrawEllipseLines = _wrap(rlapi.DrawEllipseLines, [Int, Int, Float, Float, Color], None)
_DrawRing = _wrap(rlapi.DrawRing, [Vector2, Float, Float, Float, Float, Int, Color], None)
_DrawRingLines = _wrap(rlapi.DrawRingLines, [Vector2, Float, Float, Float, Float, Int, Color], None)
_DrawRectangle = _wrap(rlapi.DrawRectangle, [Int, Int, Int, Int, Color], None)
_DrawRectangleV = _wrap(rlapi.DrawRectangleV, [Vector2, Vector2, Color], None)
_DrawRectangleRec = _wrap(rlapi.DrawRectangleRec, [Rectangle, Color], None)
_DrawRectanglePro = _wrap(rlapi.DrawRectanglePro, [Rectangle, Vector2, Float, Color], None)
_DrawRectangleGradientV = _wrap(rlapi.DrawRectangleGradientV, [Int, Int, Int, Int, Color, Color], None)
_DrawRectangleGradientH = _wrap(rlapi.DrawRectangleGradientH, [Int, Int, Int, Int, Color, Color], None)
_DrawRectangleGradientEx = _wrap(rlapi.DrawRectangleGradientEx, [Rectangle, Color, Color, Color, Color], None)
_DrawRectangleLines = _wrap(rlapi.DrawRectangleLines, [Int, Int, Int, Int, Color], None)
_DrawRectangleLinesEx = _wrap(rlapi.DrawRectangleLinesEx, [Rectangle, Float, Color], None)
_DrawRectangleRounded = _wrap(rlapi.DrawRectangleRounded, [Rectangle, Float, Int, Color], None)
_DrawRectangleRoundedLines = _wrap(rlapi.DrawRectangleRoundedLines, [Rectangle, Float, Int, Float, Color], None)
_DrawTriangle = _wrap(rlapi.DrawTriangle, [Vector2, Vector2, Vector2, Color], None)
_DrawTriangleLines = _wrap(rlapi.DrawTriangleLines, [Vector2, Vector2, Vector2, Color], None)
_DrawTriangleFan = _wrap(rlapi.DrawTriangleFan, [Vector2Ptr, Int, Color], None)
_DrawTriangleStrip = _wrap(rlapi.DrawTriangleStrip, [Vector2Ptr, Int, Color], None)
_DrawPoly = _wrap(rlapi.DrawPoly, [Vector2, Int, Float, Float, Color], None)
_DrawPolyLines = _wrap(rlapi.DrawPolyLines, [Vector2, Int, Float, Float, Color], None)
_DrawPolyLinesEx = _wrap(rlapi.DrawPolyLinesEx, [Vector2, Int, Float, Float, Float, Color], None)
_CheckCollisionRecs = _wrap(rlapi.CheckCollisionRecs, [Rectangle, Rectangle], Bool)
_CheckCollisionCircles = _wrap(rlapi.CheckCollisionCircles, [Vector2, Float, Vector2, Float], Bool)
_CheckCollisionCircleRec = _wrap(rlapi.CheckCollisionCircleRec, [Vector2, Float, Rectangle], Bool)
_CheckCollisionPointRec = _wrap(rlapi.CheckCollisionPointRec, [Vector2, Rectangle], Bool)
_CheckCollisionPointCircle = _wrap(rlapi.CheckCollisionPointCircle, [Vector2, Vector2, Float], Bool)
_CheckCollisionPointTriangle = _wrap(rlapi.CheckCollisionPointTriangle, [Vector2, Vector2, Vector2, Vector2], Bool)
_CheckCollisionLines = _wrap(rlapi.CheckCollisionLines, [Vector2, Vector2, Vector2, Vector2, Vector2Ptr], Bool)
_CheckCollisionPointLine = _wrap(rlapi.CheckCollisionPointLine, [Vector2, Vector2, Vector2, Int], Bool)
_GetCollisionRec = _wrap(rlapi.GetCollisionRec, [Rectangle, Rectangle], Rectangle)
_LoadImage = _wrap(rlapi.LoadImage, [CharPtr], Image)
_LoadImageRaw = _wrap(rlapi.LoadImageRaw, [CharPtr, Int, Int, Int, Int], Image)
_LoadImageAnim = _wrap(rlapi.LoadImageAnim, [CharPtr, IntPtr], Image)
_LoadImageFromMemory = _wrap(rlapi.LoadImageFromMemory, [CharPtr, UCharPtr, Int], Image)
_LoadImageFromTexture = _wrap(rlapi.LoadImageFromTexture, [Texture2D], Image)
_LoadImageFromScreen = _wrap(rlapi.LoadImageFromScreen, [], Image)
_UnloadImage = _wrap(rlapi.UnloadImage, [Image], None)
_ExportImage = _wrap(rlapi.ExportImage, [Image, CharPtr], Bool)
_ExportImageAsCode = _wrap(rlapi.ExportImageAsCode, [Image, CharPtr], Bool)
_GenImageColor = _wrap(rlapi.GenImageColor, [Int, Int, Color], Image)
_GenImageGradientV = _wrap(rlapi.GenImageGradientV, [Int, Int, Color, Color], Image)
_GenImageGradientH = _wrap(rlapi.GenImageGradientH, [Int, Int, Color, Color], Image)
_GenImageGradientRadial = _wrap(rlapi.GenImageGradientRadial, [Int, Int, Float, Color, Color], Image)
_GenImageChecked = _wrap(rlapi.GenImageChecked, [Int, Int, Int, Int, Color, Color], Image)
_GenImageWhiteNoise = _wrap(rlapi.GenImageWhiteNoise, [Int, Int, Float], Image)
_GenImageCellular = _wrap(rlapi.GenImageCellular, [Int, Int, Int], Image)
_ImageCopy = _wrap(rlapi.ImageCopy, [Image], Image)
_ImageFromImage = _wrap(rlapi.ImageFromImage, [Image, Rectangle], Image)
_ImageText = _wrap(rlapi.ImageText, [CharPtr, Int, Color], Image)
_ImageTextEx = _wrap(rlapi.ImageTextEx, [Font, CharPtr, Float, Float, Color], Image)
_ImageFormat = _wrap(rlapi.ImageFormat, [ImagePtr, Int], None)
_ImageToPOT = _wrap(rlapi.ImageToPOT, [ImagePtr, Color], None)
_ImageCrop = _wrap(rlapi.ImageCrop, [ImagePtr, Rectangle], None)
_ImageAlphaCrop = _wrap(rlapi.ImageAlphaCrop, [ImagePtr, Float], None)
_ImageAlphaClear = _wrap(rlapi.ImageAlphaClear, [ImagePtr, Color, Float], None)
_ImageAlphaMask = _wrap(rlapi.ImageAlphaMask, [ImagePtr, Image], None)
_ImageAlphaPremultiply = _wrap(rlapi.ImageAlphaPremultiply, [ImagePtr], None)
_ImageResize = _wrap(rlapi.ImageResize, [ImagePtr, Int, Int], None)
_ImageResizeNN = _wrap(rlapi.ImageResizeNN, [ImagePtr, Int, Int], None)
_ImageResizeCanvas = _wrap(rlapi.ImageResizeCanvas, [ImagePtr, Int, Int, Int, Int, Color], None)
_ImageMipmaps = _wrap(rlapi.ImageMipmaps, [ImagePtr], None)
_ImageDither = _wrap(rlapi.ImageDither, [ImagePtr, Int, Int, Int, Int], None)
_ImageFlipVertical = _wrap(rlapi.ImageFlipVertical, [ImagePtr], None)
_ImageFlipHorizontal = _wrap(rlapi.ImageFlipHorizontal, [ImagePtr], None)
_ImageRotateCW = _wrap(rlapi.ImageRotateCW, [ImagePtr], None)
_ImageRotateCCW = _wrap(rlapi.ImageRotateCCW, [ImagePtr], None)
_ImageColorTint = _wrap(rlapi.ImageColorTint, [ImagePtr, Color], None)
_ImageColorInvert = _wrap(rlapi.ImageColorInvert, [ImagePtr], None)
_ImageColorGrayscale = _wrap(rlapi.ImageColorGrayscale, [ImagePtr], None)
_ImageColorContrast = _wrap(rlapi.ImageColorContrast, [ImagePtr, Float], None)
_ImageColorBrightness = _wrap(rlapi.ImageColorBrightness, [ImagePtr, Int], None)
_ImageColorReplace = _wrap(rlapi.ImageColorReplace, [ImagePtr, Color, Color], None)
_LoadImageColors = _wrap(rlapi.LoadImageColors, [Image], ColorPtr)
_LoadImagePalette = _wrap(rlapi.LoadImagePalette, [Image, Int, IntPtr], ColorPtr)
_UnloadImageColors = _wrap(rlapi.UnloadImageColors, [ColorPtr], None)
_UnloadImagePalette = _wrap(rlapi.UnloadImagePalette, [ColorPtr], None)
_GetImageAlphaBorder = _wrap(rlapi.GetImageAlphaBorder, [Image, Float], Rectangle)
_GetImageColor = _wrap(rlapi.GetImageColor, [Image, Int, Int], Color)
_ImageClearBackground = _wrap(rlapi.ImageClearBackground, [ImagePtr, Color], None)
_ImageDrawPixel = _wrap(rlapi.ImageDrawPixel, [ImagePtr, Int, Int, Color], None)
_ImageDrawPixelV = _wrap(rlapi.ImageDrawPixelV, [ImagePtr, Vector2, Color], None)
_ImageDrawLine = _wrap(rlapi.ImageDrawLine, [ImagePtr, Int, Int, Int, Int, Color], None)
_ImageDrawLineV = _wrap(rlapi.ImageDrawLineV, [ImagePtr, Vector2, Vector2, Color], None)
_ImageDrawCircle = _wrap(rlapi.ImageDrawCircle, [ImagePtr, Int, Int, Int, Color], None)
_ImageDrawCircleV = _wrap(rlapi.ImageDrawCircleV, [ImagePtr, Vector2, Int, Color], None)
_ImageDrawRectangle = _wrap(rlapi.ImageDrawRectangle, [ImagePtr, Int, Int, Int, Int, Color], None)
_ImageDrawRectangleV = _wrap(rlapi.ImageDrawRectangleV, [ImagePtr, Vector2, Vector2, Color], None)
_ImageDrawRectangleRec = _wrap(rlapi.ImageDrawRectangleRec, [ImagePtr, Rectangle, Color], None)
_ImageDrawRectangleLines = _wrap(rlapi.ImageDrawRectangleLines, [ImagePtr, Rectangle, Int, Color], None)
_ImageDraw = _wrap(rlapi.ImageDraw, [ImagePtr, Image, Rectangle, Rectangle, Color], None)
_ImageDrawText = _wrap(rlapi.ImageDrawText, [ImagePtr, CharPtr, Int, Int, Int, Color], None)
_ImageDrawTextEx = _wrap(rlapi.ImageDrawTextEx, [ImagePtr, Font, CharPtr, Vector2, Float, Float, Color], None)
_LoadTexture = _wrap(rlapi.LoadTexture, [CharPtr], Texture2D)
_LoadTextureFromImage = _wrap(rlapi.LoadTextureFromImage, [Image], Texture2D)
_LoadTextureCubemap = _wrap(rlapi.LoadTextureCubemap, [Image, Int], TextureCubemap)
_LoadRenderTexture = _wrap(rlapi.LoadRenderTexture, [Int, Int], RenderTexture2D)
_UnloadTexture = _wrap(rlapi.UnloadTexture, [Texture2D], None)
_UnloadRenderTexture = _wrap(rlapi.UnloadRenderTexture, [RenderTexture2D], None)
_UpdateTexture = _wrap(rlapi.UpdateTexture, [Texture2D, VoidPtr], None)
_UpdateTextureRec = _wrap(rlapi.UpdateTextureRec, [Texture2D, Rectangle, VoidPtr], None)
_GenTextureMipmaps = _wrap(rlapi.GenTextureMipmaps, [Texture2DPtr], None)
_SetTextureFilter = _wrap(rlapi.SetTextureFilter, [Texture2D, Int], None)
_SetTextureWrap = _wrap(rlapi.SetTextureWrap, [Texture2D, Int], None)
_DrawTexture = _wrap(rlapi.DrawTexture, [Texture2D, Int, Int, Color], None)
_DrawTextureV = _wrap(rlapi.DrawTextureV, [Texture2D, Vector2, Color], None)
_DrawTextureEx = _wrap(rlapi.DrawTextureEx, [Texture2D, Vector2, Float, Float, Color], None)
_DrawTextureRec = _wrap(rlapi.DrawTextureRec, [Texture2D, Rectangle, Vector2, Color], None)
_DrawTextureQuad = _wrap(rlapi.DrawTextureQuad, [Texture2D, Vector2, Vector2, Rectangle, Color], None)
_DrawTextureTiled = _wrap(rlapi.DrawTextureTiled, [Texture2D, Rectangle, Rectangle, Vector2, Float, Float, Color], None)
_DrawTexturePro = _wrap(rlapi.DrawTexturePro, [Texture2D, Rectangle, Rectangle, Vector2, Float, Color], None)
_DrawTextureNPatch = _wrap(rlapi.DrawTextureNPatch, [Texture2D, NPatchInfo, Rectangle, Vector2, Float, Color], None)
_DrawTexturePoly = _wrap(rlapi.DrawTexturePoly, [Texture2D, Vector2, Vector2Ptr, Vector2Ptr, Int, Color], None)
_Fade = _wrap(rlapi.Fade, [Color, Float], Color)
_ColorToInt = _wrap(rlapi.ColorToInt, [Color], Int)
_ColorNormalize = _wrap(rlapi.ColorNormalize, [Color], Vector4)
_ColorFromNormalized = _wrap(rlapi.ColorFromNormalized, [Vector4], Color)
_ColorToHSV = _wrap(rlapi.ColorToHSV, [Color], Vector3)
_ColorFromHSV = _wrap(rlapi.ColorFromHSV, [Float, Float, Float], Color)
_ColorAlpha = _wrap(rlapi.ColorAlpha, [Color, Float], Color)
_ColorAlphaBlend = _wrap(rlapi.ColorAlphaBlend, [Color, Color, Color], Color)
_GetColor = _wrap(rlapi.GetColor, [UInt], Color)
_GetPixelColor = _wrap(rlapi.GetPixelColor, [VoidPtr, Int], Color)
_SetPixelColor = _wrap(rlapi.SetPixelColor, [VoidPtr, Color, Int], None)
_GetPixelDataSize = _wrap(rlapi.GetPixelDataSize, [Int, Int, Int], Int)
_GetFontDefault = _wrap(rlapi.GetFontDefault, [], Font)
_LoadFont = _wrap(rlapi.LoadFont, [CharPtr], Font)
_LoadFontEx = _wrap(rlapi.LoadFontEx, [CharPtr, Int, IntPtr, Int], Font)
_LoadFontFromImage = _wrap(rlapi.LoadFontFromImage, [Image, Color, Int], Font)
_LoadFontFromMemory = _wrap(rlapi.LoadFontFromMemory, [CharPtr, UCharPtr, Int, Int, IntPtr, Int], Font)
_LoadFontData = _wrap(rlapi.LoadFontData, [UCharPtr, Int, Int, IntPtr, Int, Int], GlyphInfoPtr)
_GenImageFontAtlas = _wrap(rlapi.GenImageFontAtlas, [GlyphInfoPtr, RectanglePtr, Int, Int, Int, Int], Image)
_UnloadFontData = _wrap(rlapi.UnloadFontData, [GlyphInfoPtr, Int], None)
_UnloadFont = _wrap(rlapi.UnloadFont, [Font], None)
_ExportFontAsCode = _wrap(rlapi.ExportFontAsCode, [Font, CharPtr], Bool)
_DrawFPS = _wrap(rlapi.DrawFPS, [Int, Int], None)
_DrawText = _wrap(rlapi.DrawText, [CharPtr, Int, Int, Int, Color], None)
_DrawTextEx = _wrap(rlapi.DrawTextEx, [Font, CharPtr, Vector2, Float, Float, Color], None)
_DrawTextPro = _wrap(rlapi.DrawTextPro, [Font, CharPtr, Vector2, Vector2, Float, Float, Float, Color], None)
_DrawTextCodepoint = _wrap(rlapi.DrawTextCodepoint, [Font, Int, Vector2, Float, Color], None)
_DrawTextCodepoints = _wrap(rlapi.DrawTextCodepoints, [Font, IntPtr, Int, Vector2, Float, Float, Color], None)
_MeasureText = _wrap(rlapi.MeasureText, [CharPtr, Int], Int)
_MeasureTextEx = _wrap(rlapi.MeasureTextEx, [Font, CharPtr, Float, Float], Vector2)
_GetGlyphIndex = _wrap(rlapi.GetGlyphIndex, [Font, Int], Int)
_GetGlyphInfo = _wrap(rlapi.GetGlyphInfo, [Font, Int], GlyphInfo)
_GetGlyphAtlasRec = _wrap(rlapi.GetGlyphAtlasRec, [Font, Int], Rectangle)
_LoadCodepoints = _wrap(rlapi.LoadCodepoints, [CharPtr, IntPtr], IntPtr)
_UnloadCodepoints = _wrap(rlapi.UnloadCodepoints, [IntPtr], None)
_GetCodepointCount = _wrap(rlapi.GetCodepointCount, [CharPtr], Int)
_GetCodepoint = _wrap(rlapi.GetCodepoint, [CharPtr, IntPtr], Int)
_CodepointToUTF8 = _wrap(rlapi.CodepointToUTF8, [Int, IntPtr], CharPtr)
_TextCodepointsToUTF8 = _wrap(rlapi.TextCodepointsToUTF8, [IntPtr, Int], CharPtr)
_TextCopy = _wrap(rlapi.TextCopy, [CharPtr, CharPtr], Int)
_TextIsEqual = _wrap(rlapi.TextIsEqual, [CharPtr, CharPtr], Bool)
_TextLength = _wrap(rlapi.TextLength, [CharPtr], UInt)
_TextFormat = _wrap(rlapi.TextFormat, [CharPtr, VoidPtr], CharPtr)
_TextSubtext = _wrap(rlapi.TextSubtext, [CharPtr, Int, Int], CharPtr)
_TextReplace = _wrap(rlapi.TextReplace, [CharPtr, CharPtr, CharPtr], CharPtr)
_TextInsert = _wrap(rlapi.TextInsert, [CharPtr, CharPtr, Int], CharPtr)
_TextJoin = _wrap(rlapi.TextJoin, [CharPtrPtr, Int, CharPtr], CharPtr)
_TextSplit = _wrap(rlapi.TextSplit, [CharPtr, Char, IntPtr], CharPtrPtr)
_TextAppend = _wrap(rlapi.TextAppend, [CharPtr, CharPtr, IntPtr], None)
_TextFindIndex = _wrap(rlapi.TextFindIndex, [CharPtr, CharPtr], Int)
_TextToUpper = _wrap(rlapi.TextToUpper, [CharPtr], CharPtr)
_TextToLower = _wrap(rlapi.TextToLower, [CharPtr], CharPtr)
_TextToPascal = _wrap(rlapi.TextToPascal, [CharPtr], CharPtr)
_TextToInteger = _wrap(rlapi.TextToInteger, [CharPtr], Int)
_DrawLine3D = _wrap(rlapi.DrawLine3D, [Vector3, Vector3, Color], None)
_DrawPoint3D = _wrap(rlapi.DrawPoint3D, [Vector3, Color], None)
_DrawCircle3D = _wrap(rlapi.DrawCircle3D, [Vector3, Float, Vector3, Float, Color], None)
_DrawTriangle3D = _wrap(rlapi.DrawTriangle3D, [Vector3, Vector3, Vector3, Color], None)
_DrawTriangleStrip3D = _wrap(rlapi.DrawTriangleStrip3D, [Vector3Ptr, Int, Color], None)
_DrawCube = _wrap(rlapi.DrawCube, [Vector3, Float, Float, Float, Color], None)
_DrawCubeV = _wrap(rlapi.DrawCubeV, [Vector3, Vector3, Color], None)
_DrawCubeWires = _wrap(rlapi.DrawCubeWires, [Vector3, Float, Float, Float, Color], None)
_DrawCubeWiresV = _wrap(rlapi.DrawCubeWiresV, [Vector3, Vector3, Color], None)
_DrawCubeTexture = _wrap(rlapi.DrawCubeTexture, [Texture2D, Vector3, Float, Float, Float, Color], None)
_DrawCubeTextureRec = _wrap(rlapi.DrawCubeTextureRec, [Texture2D, Rectangle, Vector3, Float, Float, Float, Color], None)
_DrawSphere = _wrap(rlapi.DrawSphere, [Vector3, Float, Color], None)
_DrawSphereEx = _wrap(rlapi.DrawSphereEx, [Vector3, Float, Int, Int, Color], None)
_DrawSphereWires = _wrap(rlapi.DrawSphereWires, [Vector3, Float, Int, Int, Color], None)
_DrawCylinder = _wrap(rlapi.DrawCylinder, [Vector3, Float, Float, Float, Int, Color], None)
_DrawCylinderEx = _wrap(rlapi.DrawCylinderEx, [Vector3, Vector3, Float, Float, Int, Color], None)
_DrawCylinderWires = _wrap(rlapi.DrawCylinderWires, [Vector3, Float, Float, Float, Int, Color], None)
_DrawCylinderWiresEx = _wrap(rlapi.DrawCylinderWiresEx, [Vector3, Vector3, Float, Float, Int, Color], None)
_DrawPlane = _wrap(rlapi.DrawPlane, [Vector3, Vector2, Color], None)
_DrawRay = _wrap(rlapi.DrawRay, [Ray, Color], None)
_DrawGrid = _wrap(rlapi.DrawGrid, [Int, Float], None)
_LoadModel = _wrap(rlapi.LoadModel, [CharPtr], Model)
_LoadModelFromMesh = _wrap(rlapi.LoadModelFromMesh, [Mesh], Model)
_UnloadModel = _wrap(rlapi.UnloadModel, [Model], None)
_UnloadModelKeepMeshes = _wrap(rlapi.UnloadModelKeepMeshes, [Model], None)
_GetModelBoundingBox = _wrap(rlapi.GetModelBoundingBox, [Model], BoundingBox)
_DrawModel = _wrap(rlapi.DrawModel, [Model, Vector3, Float, Color], None)
_DrawModelEx = _wrap(rlapi.DrawModelEx, [Model, Vector3, Vector3, Float, Vector3, Color], None)
_DrawModelWires = _wrap(rlapi.DrawModelWires, [Model, Vector3, Float, Color], None)
_DrawModelWiresEx = _wrap(rlapi.DrawModelWiresEx, [Model, Vector3, Vector3, Float, Vector3, Color], None)
_DrawBoundingBox = _wrap(rlapi.DrawBoundingBox, [BoundingBox, Color], None)
_DrawBillboard = _wrap(rlapi.DrawBillboard, [Camera, Texture2D, Vector3, Float, Color], None)
_DrawBillboardRec = _wrap(rlapi.DrawBillboardRec, [Camera, Texture2D, Rectangle, Vector3, Vector2, Color], None)
_DrawBillboardPro = _wrap(rlapi.DrawBillboardPro, [Camera, Texture2D, Rectangle, Vector3, Vector3, Vector2, Vector2, Float, Color], None)
_UploadMesh = _wrap(rlapi.UploadMesh, [MeshPtr, Bool], None)
_UpdateMeshBuffer = _wrap(rlapi.UpdateMeshBuffer, [Mesh, Int, VoidPtr, Int, Int], None)
_UnloadMesh = _wrap(rlapi.UnloadMesh, [Mesh], None)
_DrawMesh = _wrap(rlapi.DrawMesh, [Mesh, Material, Matrix], None)
_DrawMeshInstanced = _wrap(rlapi.DrawMeshInstanced, [Mesh, Material, MatrixPtr, Int], None)
_ExportMesh = _wrap(rlapi.ExportMesh, [Mesh, CharPtr], Bool)
_GetMeshBoundingBox = _wrap(rlapi.GetMeshBoundingBox, [Mesh], BoundingBox)
_GenMeshTangents = _wrap(rlapi.GenMeshTangents, [MeshPtr], None)
_GenMeshPoly = _wrap(rlapi.GenMeshPoly, [Int, Float], Mesh)
_GenMeshPlane = _wrap(rlapi.GenMeshPlane, [Float, Float, Int, Int], Mesh)
_GenMeshCube = _wrap(rlapi.GenMeshCube, [Float, Float, Float], Mesh)
_GenMeshSphere = _wrap(rlapi.GenMeshSphere, [Float, Int, Int], Mesh)
_GenMeshHemiSphere = _wrap(rlapi.GenMeshHemiSphere, [Float, Int, Int], Mesh)
_GenMeshCylinder = _wrap(rlapi.GenMeshCylinder, [Float, Float, Int], Mesh)
_GenMeshCone = _wrap(rlapi.GenMeshCone, [Float, Float, Int], Mesh)
_GenMeshTorus = _wrap(rlapi.GenMeshTorus, [Float, Float, Int, Int], Mesh)
_GenMeshKnot = _wrap(rlapi.GenMeshKnot, [Float, Float, Int, Int], Mesh)
_GenMeshHeightmap = _wrap(rlapi.GenMeshHeightmap, [Image, Vector3], Mesh)
_GenMeshCubicmap = _wrap(rlapi.GenMeshCubicmap, [Image, Vector3], Mesh)
_LoadMaterials = _wrap(rlapi.LoadMaterials, [CharPtr, IntPtr], MaterialPtr)
_LoadMaterialDefault = _wrap(rlapi.LoadMaterialDefault, [], Material)
_UnloadMaterial = _wrap(rlapi.UnloadMaterial, [Material], None)
_SetMaterialTexture = _wrap(rlapi.SetMaterialTexture, [MaterialPtr, Int, Texture2D], None)
_SetModelMeshMaterial = _wrap(rlapi.SetModelMeshMaterial, [ModelPtr, Int, Int], None)
_LoadModelAnimations = _wrap(rlapi.LoadModelAnimations, [CharPtr, UIntPtr], ModelAnimationPtr)
_UpdateModelAnimation = _wrap(rlapi.UpdateModelAnimation, [Model, ModelAnimation, Int], None)
_UnloadModelAnimation = _wrap(rlapi.UnloadModelAnimation, [ModelAnimation], None)
_UnloadModelAnimations = _wrap(rlapi.UnloadModelAnimations, [ModelAnimationPtr, UInt], None)
_IsModelAnimationValid = _wrap(rlapi.IsModelAnimationValid, [Model, ModelAnimation], Bool)
_CheckCollisionSpheres = _wrap(rlapi.CheckCollisionSpheres, [Vector3, Float, Vector3, Float], Bool)
_CheckCollisionBoxes = _wrap(rlapi.CheckCollisionBoxes, [BoundingBox, BoundingBox], Bool)
_CheckCollisionBoxSphere = _wrap(rlapi.CheckCollisionBoxSphere, [BoundingBox, Vector3, Float], Bool)
_GetRayCollisionSphere = _wrap(rlapi.GetRayCollisionSphere, [Ray, Vector3, Float], RayCollision)
_GetRayCollisionBox = _wrap(rlapi.GetRayCollisionBox, [Ray, BoundingBox], RayCollision)
_GetRayCollisionMesh = _wrap(rlapi.GetRayCollisionMesh, [Ray, Mesh, Matrix], RayCollision)
_GetRayCollisionTriangle = _wrap(rlapi.GetRayCollisionTriangle, [Ray, Vector3, Vector3, Vector3], RayCollision)
_GetRayCollisionQuad = _wrap(rlapi.GetRayCollisionQuad, [Ray, Vector3, Vector3, Vector3, Vector3], RayCollision)
_InitAudioDevice = _wrap(rlapi.InitAudioDevice, [], None)
_CloseAudioDevice = _wrap(rlapi.CloseAudioDevice, [], None)
_IsAudioDeviceReady = _wrap(rlapi.IsAudioDeviceReady, [], Bool)
_SetMasterVolume = _wrap(rlapi.SetMasterVolume, [Float], None)
_LoadWave = _wrap(rlapi.LoadWave, [CharPtr], Wave)
_LoadWaveFromMemory = _wrap(rlapi.LoadWaveFromMemory, [CharPtr, UCharPtr, Int], Wave)
_LoadSound = _wrap(rlapi.LoadSound, [CharPtr], Sound)
_LoadSoundFromWave = _wrap(rlapi.LoadSoundFromWave, [Wave], Sound)
_UpdateSound = _wrap(rlapi.UpdateSound, [Sound, VoidPtr, Int], None)
_UnloadWave = _wrap(rlapi.UnloadWave, [Wave], None)
_UnloadSound = _wrap(rlapi.UnloadSound, [Sound], None)
_ExportWave = _wrap(rlapi.ExportWave, [Wave, CharPtr], Bool)
_ExportWaveAsCode = _wrap(rlapi.ExportWaveAsCode, [Wave, CharPtr], Bool)
_PlaySound = _wrap(rlapi.PlaySound, [Sound], None)
_StopSound = _wrap(rlapi.StopSound, [Sound], None)
_PauseSound = _wrap(rlapi.PauseSound, [Sound], None)
_ResumeSound = _wrap(rlapi.ResumeSound, [Sound], None)
_PlaySoundMulti = _wrap(rlapi.PlaySoundMulti, [Sound], None)
_StopSoundMulti = _wrap(rlapi.StopSoundMulti, [], None)
_GetSoundsPlaying = _wrap(rlapi.GetSoundsPlaying, [], Int)
_IsSoundPlaying = _wrap(rlapi.IsSoundPlaying, [Sound], Bool)
_SetSoundVolume = _wrap(rlapi.SetSoundVolume, [Sound, Float], None)
_SetSoundPitch = _wrap(rlapi.SetSoundPitch, [Sound, Float], None)
_SetSoundPan = _wrap(rlapi.SetSoundPan, [Sound, Float], None)
_WaveCopy = _wrap(rlapi.WaveCopy, [Wave], Wave)
_WaveCrop = _wrap(rlapi.WaveCrop, [WavePtr, Int, Int], None)
_WaveFormat = _wrap(rlapi.WaveFormat, [WavePtr, Int, Int, Int], None)
_LoadWaveSamples = _wrap(rlapi.LoadWaveSamples, [Wave], FloatPtr)
_UnloadWaveSamples = _wrap(rlapi.UnloadWaveSamples, [FloatPtr], None)
_LoadMusicStream = _wrap(rlapi.LoadMusicStream, [CharPtr], Music)
_LoadMusicStreamFromMemory = _wrap(rlapi.LoadMusicStreamFromMemory, [CharPtr, UCharPtr, Int], Music)
_UnloadMusicStream = _wrap(rlapi.UnloadMusicStream, [Music], None)
_PlayMusicStream = _wrap(rlapi.PlayMusicStream, [Music], None)
_IsMusicStreamPlaying = _wrap(rlapi.IsMusicStreamPlaying, [Music], Bool)
_UpdateMusicStream = _wrap(rlapi.UpdateMusicStream, [Music], None)
_StopMusicStream = _wrap(rlapi.StopMusicStream, [Music], None)
_PauseMusicStream = _wrap(rlapi.PauseMusicStream, [Music], None)
_ResumeMusicStream = _wrap(rlapi.ResumeMusicStream, [Music], None)
_SeekMusicStream = _wrap(rlapi.SeekMusicStream, [Music, Float], None)
_SetMusicVolume = _wrap(rlapi.SetMusicVolume, [Music, Float], None)
_SetMusicPitch = _wrap(rlapi.SetMusicPitch, [Music, Float], None)
_SetMusicPan = _wrap(rlapi.SetMusicPan, [Music, Float], None)
_GetMusicTimeLength = _wrap(rlapi.GetMusicTimeLength, [Music], Float)
_GetMusicTimePlayed = _wrap(rlapi.GetMusicTimePlayed, [Music], Float)
_LoadAudioStream = _wrap(rlapi.LoadAudioStream, [UInt, UInt, UInt], AudioStream)
_UnloadAudioStream = _wrap(rlapi.UnloadAudioStream, [AudioStream], None)
_UpdateAudioStream = _wrap(rlapi.UpdateAudioStream, [AudioStream, VoidPtr, Int], None)
_IsAudioStreamProcessed = _wrap(rlapi.IsAudioStreamProcessed, [AudioStream], Bool)
_PlayAudioStream = _wrap(rlapi.PlayAudioStream, [AudioStream], None)
_PauseAudioStream = _wrap(rlapi.PauseAudioStream, [AudioStream], None)
_ResumeAudioStream = _wrap(rlapi.ResumeAudioStream, [AudioStream], None)
_IsAudioStreamPlaying = _wrap(rlapi.IsAudioStreamPlaying, [AudioStream], Bool)
_StopAudioStream = _wrap(rlapi.StopAudioStream, [AudioStream], None)
_SetAudioStreamVolume = _wrap(rlapi.SetAudioStreamVolume, [AudioStream, Float], None)
_SetAudioStreamPitch = _wrap(rlapi.SetAudioStreamPitch, [AudioStream, Float], None)
_SetAudioStreamPan = _wrap(rlapi.SetAudioStreamPan, [AudioStream, Float], None)
_SetAudioStreamBufferSizeDefault = _wrap(rlapi.SetAudioStreamBufferSizeDefault, [Int], None)
_SetAudioStreamCallback = _wrap(rlapi.SetAudioStreamCallback, [AudioStream, AudioCallback], None)
_AttachAudioStreamProcessor = _wrap(rlapi.AttachAudioStreamProcessor, [AudioStream, AudioCallback], None)
_DetachAudioStreamProcessor = _wrap(rlapi.DetachAudioStreamProcessor, [AudioStream, AudioCallback], None)
_Clamp = _wrap(rlapi.Clamp, [Float, Float, Float], Float)
_Lerp = _wrap(rlapi.Lerp, [Float, Float, Float], Float)
_Normalize = _wrap(rlapi.Normalize, [Float, Float, Float], Float)
_Remap = _wrap(rlapi.Remap, [Float, Float, Float, Float, Float], Float)
_Wrap = _wrap(rlapi.Wrap, [Float, Float, Float], Float)
_FloatEquals = _wrap(rlapi.FloatEquals, [Float, Float], Int)
_Vector2Zero = _wrap(rlapi.Vector2Zero, [], Vector2)
_Vector2One = _wrap(rlapi.Vector2One, [], Vector2)
_Vector2Add = _wrap(rlapi.Vector2Add, [Vector2, Vector2], Vector2)
_Vector2AddValue = _wrap(rlapi.Vector2AddValue, [Vector2, Float], Vector2)
_Vector2Subtract = _wrap(rlapi.Vector2Subtract, [Vector2, Vector2], Vector2)
_Vector2SubtractValue = _wrap(rlapi.Vector2SubtractValue, [Vector2, Float], Vector2)
_Vector2Length = _wrap(rlapi.Vector2Length, [Vector2], Float)
_Vector2LengthSqr = _wrap(rlapi.Vector2LengthSqr, [Vector2], Float)
_Vector2DotProduct = _wrap(rlapi.Vector2DotProduct, [Vector2, Vector2], Float)
_Vector2Distance = _wrap(rlapi.Vector2Distance, [Vector2, Vector2], Float)
_Vector2DistanceSqr = _wrap(rlapi.Vector2DistanceSqr, [Vector2, Vector2], Float)
_Vector2Angle = _wrap(rlapi.Vector2Angle, [Vector2, Vector2], Float)
_Vector2Scale = _wrap(rlapi.Vector2Scale, [Vector2, Float], Vector2)
_Vector2Multiply = _wrap(rlapi.Vector2Multiply, [Vector2, Vector2], Vector2)
_Vector2Negate = _wrap(rlapi.Vector2Negate, [Vector2], Vector2)
_Vector2Divide = _wrap(rlapi.Vector2Divide, [Vector2, Vector2], Vector2)
_Vector2Normalize = _wrap(rlapi.Vector2Normalize, [Vector2], Vector2)
_Vector2Transform = _wrap(rlapi.Vector2Transform, [Vector2, Matrix], Vector2)
_Vector2Lerp = _wrap(rlapi.Vector2Lerp, [Vector2, Vector2, Float], Vector2)
_Vector2Reflect = _wrap(rlapi.Vector2Reflect, [Vector2, Vector2], Vector2)
_Vector2Rotate = _wrap(rlapi.Vector2Rotate, [Vector2, Float], Vector2)
_Vector2MoveTowards = _wrap(rlapi.Vector2MoveTowards, [Vector2, Vector2, Float], Vector2)
_Vector2Invert = _wrap(rlapi.Vector2Invert, [Vector2], Vector2)
_Vector2Clamp = _wrap(rlapi.Vector2Clamp, [Vector2, Vector2, Vector2], Vector2)
_Vector2ClampValue = _wrap(rlapi.Vector2ClampValue, [Vector2, Float, Float], Vector2)
_Vector2Equals = _wrap(rlapi.Vector2Equals, [Vector2, Vector2], Int)
_Vector3Zero = _wrap(rlapi.Vector3Zero, [], Vector3)
_Vector3One = _wrap(rlapi.Vector3One, [], Vector3)
_Vector3Add = _wrap(rlapi.Vector3Add, [Vector3, Vector3], Vector3)
_Vector3AddValue = _wrap(rlapi.Vector3AddValue, [Vector3, Float], Vector3)
_Vector3Subtract = _wrap(rlapi.Vector3Subtract, [Vector3, Vector3], Vector3)
_Vector3SubtractValue = _wrap(rlapi.Vector3SubtractValue, [Vector3, Float], Vector3)
_Vector3Scale = _wrap(rlapi.Vector3Scale, [Vector3, Float], Vector3)
_Vector3Multiply = _wrap(rlapi.Vector3Multiply, [Vector3, Vector3], Vector3)
_Vector3CrossProduct = _wrap(rlapi.Vector3CrossProduct, [Vector3, Vector3], Float)
_Vector3Perpendicular = _wrap(rlapi.Vector3Perpendicular, [Vector3], Vector3)
_Vector3Length = _wrap(rlapi.Vector3Length, [Vector3], Float)
_Vector3LengthSqr = _wrap(rlapi.Vector3LengthSqr, [Vector3], Float)
_Vector3DotProduct = _wrap(rlapi.Vector3DotProduct, [Vector3, Vector3], Float)
_Vector3Distance = _wrap(rlapi.Vector3Distance, [Vector3, Vector3], Float)
_Vector3DistanceSqr = _wrap(rlapi.Vector3DistanceSqr, [Vector3, Vector3], Float)
_Vector3Angle = _wrap(rlapi.Vector3Angle, [Vector3, Vector3], Float)
_Vector3Negate = _wrap(rlapi.Vector3Negate, [Vector3], Vector3)
_Vector3Divide = _wrap(rlapi.Vector3Divide, [Vector3, Vector3], Float)
_Vector3Normalize = _wrap(rlapi.Vector3Normalize, [Vector3], Vector3)
_Vector3OrthoNormalize = _wrap(rlapi.Vector3OrthoNormalize, [Vector3Ptr, Vector3Ptr], Vector3)
_Vector3Transform = _wrap(rlapi.Vector3Transform, [Vector3, Matrix], Vector3)
_Vector3RotateByQuaternion = _wrap(rlapi.Vector3RotateByQuaternion, [Vector3, Quaternion], Vector3)
_Vector3RotateByAxisAngle = _wrap(rlapi.Vector3RotateByAxisAngle, [Vector3, Vector3, Float], Vector3)
_Vector3Lerp = _wrap(rlapi.Vector3Lerp, [Vector3, Vector3, Float], Vector3)
_Vector3Reflect = _wrap(rlapi.Vector3Reflect, [Vector3, Vector3], Vector3)
_Vector3Min = _wrap(rlapi.Vector3Min, [Vector3, Vector3], Vector3)
_Vector3Max = _wrap(rlapi.Vector3Max, [Vector3, Vector3], Vector3)
_Vector3Barycenter = _wrap(rlapi.Vector3Barycenter, [Vector3, Vector3, Vector3, Vector3], Vector3)
_Vector3Unproject = _wrap(rlapi.Vector3Unproject, [Vector3, Matrix, Matrix], Vector3)
_Vector3ToFloatV = _wrap(rlapi.Vector3ToFloatV, [Vector3], Float * 3)
_Vector3Invert = _wrap(rlapi.Vector3Invert, [Vector3], Vector3)
_Vector3Clamp = _wrap(rlapi.Vector3Clamp, [Vector3, Vector3, Vector3], Vector3)
_Vector3ClampValue = _wrap(rlapi.Vector3ClampValue, [Vector3, Float, Float], Vector3)
_Vector3Equals = _wrap(rlapi.Vector3Equals, [Vector3, Float, Float], Int)
_Vector3Refract = _wrap(rlapi.Vector3Refract, [Vector3, Vector3, Float], Int)
_MatrixDeterminant = _wrap(rlapi.MatrixDeterminant, [Matrix], Float)
_MatrixTrace = _wrap(rlapi.MatrixTrace, [Matrix], Float)
_MatrixTranspose = _wrap(rlapi.MatrixTranspose, [Matrix], Matrix)
_MatrixInvert = _wrap(rlapi.MatrixInvert, [Matrix], Matrix)
_MatrixIdentity = _wrap(rlapi.MatrixIdentity, [], Matrix)
_MatrixAdd = _wrap(rlapi.MatrixAdd, [Matrix, Matrix], Matrix)
_MatrixSubtract = _wrap(rlapi.MatrixSubtract, [Matrix, Matrix], Matrix)
_MatrixMultiply = _wrap(rlapi.MatrixMultiply, [Matrix, Matrix], Matrix)
_MatrixTranslate = _wrap(rlapi.MatrixTranslate, [Float, Float, Float], Matrix)
_MatrixRotate = _wrap(rlapi.MatrixRotate, [Vector3, Float], Matrix)
_MatrixRotateX = _wrap(rlapi.MatrixRotateX, [Float], Matrix)
_MatrixRotateY = _wrap(rlapi.MatrixRotateY, [Float], Matrix)
_MatrixRotateZ = _wrap(rlapi.MatrixRotateZ, [Float], Matrix)
_MatrixRotateXYZ = _wrap(rlapi.MatrixRotateXYZ, [Vector3], Matrix)
_MatrixRotateZYX = _wrap(rlapi.MatrixRotateZYX, [Vector3], Matrix)
_MatrixScale = _wrap(rlapi.MatrixScale, [Float, Float, Float], Matrix)
_MatrixFrustum = _wrap(rlapi.MatrixFrustum, [Float, Float, Float, Float, Float, Float], Matrix)
_MatrixPerspective = _wrap(rlapi.MatrixPerspective, [Float, Float, Float, Float], Matrix)
_MatrixOrtho = _wrap(rlapi.MatrixOrtho, [Float, Float, Float, Float, Float, Float], Matrix)
_MatrixLookAt = _wrap(rlapi.MatrixLookAt, [Vector3, Vector3, Vector3], Matrix)
_MatrixToFloatV = _wrap(rlapi.MatrixToFloatV, [Matrix], Float * 16)
_QuaternionAdd = _wrap(rlapi.QuaternionAdd, [Quaternion, Quaternion], Quaternion)
_QuaternionAddValue = _wrap(rlapi.QuaternionAddValue, [Quaternion, Float], Quaternion)
_QuaternionSubtract = _wrap(rlapi.QuaternionSubtract, [Quaternion, Quaternion], Quaternion)
_QuaternionSubtractValue = _wrap(rlapi.QuaternionSubtractValue, [Quaternion, Float], Quaternion)
_QuaternionIdentity = _wrap(rlapi.QuaternionIdentity, [], Quaternion)
_QuaternionLength = _wrap(rlapi.QuaternionLength, [Quaternion], Quaternion)
_QuaternionNormalize = _wrap(rlapi.QuaternionNormalize, [Quaternion], Quaternion)
_QuaternionInvert = _wrap(rlapi.QuaternionInvert, [Quaternion], Quaternion)
_QuaternionMultiply = _wrap(rlapi.QuaternionMultiply, [Quaternion, Quaternion], Quaternion)
_QuaternionScale = _wrap(rlapi.QuaternionScale, [Quaternion, Float], Quaternion)
_QuaternionDivide = _wrap(rlapi.QuaternionDivide, [Quaternion, Quaternion], Quaternion)
_QuaternionNlerp = _wrap(rlapi.QuaternionNlerp, [Quaternion, Quaternion, Float], Quaternion)
_QuaternionSlerp = _wrap(rlapi.QuaternionSlerp, [Quaternion, Quaternion, Float], Quaternion)
_QuaternionFromVector3ToVector3 = _wrap(rlapi.QuaternionFromVector3ToVector3, [Vector3, Vector3], Quaternion)
_QuaternionToMatrix = _wrap(rlapi.QuaternionToMatrix, [Quaternion], Matrix)
_QuaternionFromMatrix = _wrap(rlapi.QuaternionFromMatrix, [Matrix], Quaternion)
_QuaternionFromAxisAngle = _wrap(rlapi.QuaternionFromAxisAngle, [Vector3, Float], Quaternion)
_QuaternionToAxisAngle = _wrap(rlapi.QuaternionToAxisAngle, [Quaternion, Vector3Ptr, FloatPtr], None)
_QuaternionFromEuler = _wrap(rlapi.QuaternionFromEuler, [Float, Float, Float], Quaternion)
_QuaternionToEuler = _wrap(rlapi.QuaternionToEuler, [Quaternion], Vector3)
_QuaternionTransform = _wrap(rlapi.QuaternionTransform, [Quaternion, Matrix], Quaternion)
_QuaternionEquals = _wrap(rlapi.QuaternionEquals, [Quaternion, Quaternion], Int)
_rlMatrixMode = _wrap(rlapi.rlMatrixMode, [Int], None)
_rlPushMatrix = _wrap(rlapi.rlPushMatrix, [], None)
_rlPopMatrix = _wrap(rlapi.rlPopMatrix, [], None)
_rlLoadIdentity = _wrap(rlapi.rlLoadIdentity, [], None)
_rlTranslatef = _wrap(rlapi.rlTranslatef, [Float, Float, Float], None)
_rlRotatef = _wrap(rlapi.rlRotatef, [Float, Float, Float, Float], None)
_rlScalef = _wrap(rlapi.rlScalef, [Float, Float, Float], None)
_rlMultMatrixf = _wrap(rlapi.rlMultMatrixf, [FloatPtr], None)
_rlFrustum = _wrap(rlapi.rlFrustum, [Double, Double, Double, Double, Double, Double], None)
_rlOrtho = _wrap(rlapi.rlOrtho, [Double, Double, Double, Double, Double, Double], None)
_rlViewport = _wrap(rlapi.rlViewport, [Int, Int, Int, Int], None)
_rlBegin = _wrap(rlapi.rlBegin, [Int], None)
_rlEnd = _wrap(rlapi.rlEnd, [], None)
_rlVertex2i = _wrap(rlapi.rlVertex2i, [Int, Int], None)
_rlVertex2f = _wrap(rlapi.rlVertex2f, [Float, Float], None)
_rlVertex3f = _wrap(rlapi.rlVertex3f, [Float, Float, Float], None)
_rlTexCoord2f = _wrap(rlapi.rlTexCoord2f, [Float, Float], None)
_rlNormal3f = _wrap(rlapi.rlNormal3f, [Float, Float, Float], None)
_rlColor4ub = _wrap(rlapi.rlColor4ub, [UChar, UChar, UChar, UChar], None)
_rlColor3f = _wrap(rlapi.rlColor3f, [Float, Float, Float], None)
_rlColor4f = _wrap(rlapi.rlColor4f, [Float, Float, Float, Float], None)
_rlEnableVertexArray = _wrap(rlapi.rlEnableVertexArray, [UInt], Bool)
_rlDisableVertexArray = _wrap(rlapi.rlDisableVertexArray, [], None)
_rlEnableVertexBuffer = _wrap(rlapi.rlEnableVertexBuffer, [UInt], None)
_rlDisableVertexBuffer = _wrap(rlapi.rlDisableVertexBuffer, [], None)
_rlEnableVertexBufferElement = _wrap(rlapi.rlEnableVertexBufferElement, [UInt], None)
_rlDisableVertexBufferElement = _wrap(rlapi.rlDisableVertexBufferElement, [], None)
_rlEnableVertexAttribute = _wrap(rlapi.rlEnableVertexAttribute, [UInt], None)
_rlDisableVertexAttribute = _wrap(rlapi.rlDisableVertexAttribute, [UInt], None)
_rlActiveTextureSlot = _wrap(rlapi.rlActiveTextureSlot, [Int], None)
_rlEnableTexture = _wrap(rlapi.rlEnableTexture, [UInt], None)
_rlDisableTexture = _wrap(rlapi.rlDisableTexture, [], None)
_rlEnableTextureCubemap = _wrap(rlapi.rlEnableTextureCubemap, [UInt], None)
_rlDisableTextureCubemap = _wrap(rlapi.rlDisableTextureCubemap, [], None)
_rlTextureParameters = _wrap(rlapi.rlTextureParameters, [UInt, Int, Int], None)
_rlEnableShader = _wrap(rlapi.rlEnableShader, [UInt], None)
_rlDisableShader = _wrap(rlapi.rlDisableShader, [], None)
_rlEnableFramebuffer = _wrap(rlapi.rlEnableFramebuffer, [UInt], None)
_rlDisableFramebuffer = _wrap(rlapi.rlDisableFramebuffer, [], None)
_rlActiveDrawBuffers = _wrap(rlapi.rlActiveDrawBuffers, [Int], None)
_rlEnableColorBlend = _wrap(rlapi.rlEnableColorBlend, [], None)
_rlDisableColorBlend = _wrap(rlapi.rlDisableColorBlend, [], None)
_rlEnableDepthTest = _wrap(rlapi.rlEnableDepthTest, [], None)
_rlDisableDepthTest = _wrap(rlapi.rlDisableDepthTest, [], None)
_rlEnableDepthMask = _wrap(rlapi.rlEnableDepthMask, [], None)
_rlDisableDepthMask = _wrap(rlapi.rlDisableDepthMask, [], None)
_rlEnableBackfaceCulling = _wrap(rlapi.rlEnableBackfaceCulling, [], None)
_rlDisableBackfaceCulling = _wrap(rlapi.rlDisableBackfaceCulling, [], None)
_rlEnableScissorTest = _wrap(rlapi.rlEnableScissorTest, [], None)
_rlDisableScissorTest = _wrap(rlapi.rlDisableScissorTest, [], None)
_rlScissor = _wrap(rlapi.rlScissor, [Int, Int, Int, Int], None)
_rlEnableWireMode = _wrap(rlapi.rlEnableWireMode, [], None)
_rlDisableWireMode = _wrap(rlapi.rlDisableWireMode, [], None)
_rlSetLineWidth = _wrap(rlapi.rlSetLineWidth, [Float], None)
_rlGetLineWidth = _wrap(rlapi.rlGetLineWidth, [], Float)
_rlEnableSmoothLines = _wrap(rlapi.rlEnableSmoothLines, [], None)
_rlDisableSmoothLines = _wrap(rlapi.rlDisableSmoothLines, [], None)
_rlEnableStereoRender = _wrap(rlapi.rlEnableStereoRender, [], None)
_rlDisableStereoRender = _wrap(rlapi.rlDisableStereoRender, [], None)
_rlIsStereoRenderEnabled = _wrap(rlapi.rlIsStereoRenderEnabled, [], Bool)
_rlClearColor = _wrap(rlapi.rlClearColor, [UChar, UChar, UChar, UChar], None)
_rlClearScreenBuffers = _wrap(rlapi.rlClearScreenBuffers, [], None)
_rlCheckErrors = _wrap(rlapi.rlCheckErrors, [], None)
_rlSetBlendMode = _wrap(rlapi.rlSetBlendMode, [Int], None)
_rlSetBlendFactors = _wrap(rlapi.rlSetBlendFactors, [Int, Int, Int], None)
_rlglInit = _wrap(rlapi.rlglInit, [Int, Int], None)
_rlglClose = _wrap(rlapi.rlglClose, [], None)
_rlLoadExtensions = _wrap(rlapi.rlLoadExtensions, [VoidPtr], None)
_rlGetVersion = _wrap(rlapi.rlGetVersion, [], Int)
_rlSetFramebufferWidth = _wrap(rlapi.rlSetFramebufferWidth, [Int], None)
_rlGetFramebufferWidth = _wrap(rlapi.rlGetFramebufferWidth, [], Int)
_rlSetFramebufferHeight = _wrap(rlapi.rlSetFramebufferHeight, [Int], None)
_rlGetFramebufferHeight = _wrap(rlapi.rlGetFramebufferHeight, [], Int)
_rlGetTextureIdDefault = _wrap(rlapi.rlGetTextureIdDefault, [], UInt)
_rlGetShaderIdDefault = _wrap(rlapi.rlGetShaderIdDefault, [], UInt)
_rlGetShaderLocsDefault = _wrap(rlapi.rlGetShaderLocsDefault, [], IntPtr)
_rlLoadRenderBatch = _wrap(rlapi.rlLoadRenderBatch, [Int, Int], rlRenderBatch)
_rlUnloadRenderBatch = _wrap(rlapi.rlUnloadRenderBatch, [rlRenderBatch], None)
_rlDrawRenderBatch = _wrap(rlapi.rlDrawRenderBatch, [rlRenderBatchPtr], None)
_rlSetRenderBatchActive = _wrap(rlapi.rlSetRenderBatchActive, [rlRenderBatchPtr], None)
_rlDrawRenderBatchActive = _wrap(rlapi.rlDrawRenderBatchActive, [], None)
_rlCheckRenderBatchLimit = _wrap(rlapi.rlCheckRenderBatchLimit, [Int], Bool)
_rlSetTexture = _wrap(rlapi.rlSetTexture, [UInt], None)
_rlLoadVertexArray = _wrap(rlapi.rlLoadVertexArray, [], UInt)
_rlLoadVertexBuffer = _wrap(rlapi.rlLoadVertexBuffer, [VoidPtr, Int, Bool], UInt)
_rlLoadVertexBufferElement = _wrap(rlapi.rlLoadVertexBufferElement, [VoidPtr, Int, Bool], UInt)
_rlUpdateVertexBuffer = _wrap(rlapi.rlUpdateVertexBuffer, [UInt, VoidPtr, Int, Int], None)
_rlUpdateVertexBufferElements = _wrap(rlapi.rlUpdateVertexBufferElements, [UInt, VoidPtr, Int, Int], None)
_rlUnloadVertexArray = _wrap(rlapi.rlUnloadVertexArray, [UInt], None)
_rlUnloadVertexBuffer = _wrap(rlapi.rlUnloadVertexBuffer, [UInt], None)
_rlSetVertexAttribute = _wrap(rlapi.rlSetVertexAttribute, [UInt, Int, Int, Bool, Int, VoidPtr], None)
_rlSetVertexAttributeDivisor = _wrap(rlapi.rlSetVertexAttributeDivisor, [UInt, Int], None)
_rlSetVertexAttributeDefault = _wrap(rlapi.rlSetVertexAttributeDefault, [Int, VoidPtr, Int, Int], None)
_rlDrawVertexArray = _wrap(rlapi.rlDrawVertexArray, [Int, Int], None)
_rlDrawVertexArrayElements = _wrap(rlapi.rlDrawVertexArrayElements, [Int, Int, VoidPtr], None)
_rlDrawVertexArrayInstanced = _wrap(rlapi.rlDrawVertexArrayInstanced, [Int, Int, Int], None)
_rlDrawVertexArrayElementsInstanced = _wrap(rlapi.rlDrawVertexArrayElementsInstanced, [Int, Int, VoidPtr, Int], None)
_rlLoadTexture = _wrap(rlapi.rlLoadTexture, [VoidPtr, Int, Int, Int, Int], UInt)
_rlLoadTextureDepth = _wrap(rlapi.rlLoadTextureDepth, [Int, Int, Bool], UInt)
_rlLoadTextureCubemap = _wrap(rlapi.rlLoadTextureCubemap, [VoidPtr, Int, Int], UInt)
_rlUpdateTexture = _wrap(rlapi.rlUpdateTexture, [UInt, Int, Int, Int, Int, Int, VoidPtr], None)
_rlGetGlTextureFormats = _wrap(rlapi.rlGetGlTextureFormats, [Int, UIntPtr, UIntPtr, UIntPtr], None)
_rlGetPixelFormatName = _wrap(rlapi.rlGetPixelFormatName, [UInt], CharPtr)
_rlUnloadTexture = _wrap(rlapi.rlUnloadTexture, [UInt], None)
_rlGenTextureMipmaps = _wrap(rlapi.rlGenTextureMipmaps, [UInt, Int, Int, Int, IntPtr], None)
_rlReadTexturePixels = _wrap(rlapi.rlReadTexturePixels, [UInt, Int, Int, Int], VoidPtr)
_rlReadScreenPixels = _wrap(rlapi.rlReadScreenPixels, [Int, Int], UCharPtr)
_rlLoadFramebuffer = _wrap(rlapi.rlLoadFramebuffer, [Int, Int], UInt)
_rlFramebufferAttach = _wrap(rlapi.rlFramebufferAttach, [UInt, UInt, Int, Int, Int], None)
_rlFramebufferComplete = _wrap(rlapi.rlFramebufferComplete, [UInt], Bool)
_rlUnloadFramebuffer = _wrap(rlapi.rlUnloadFramebuffer, [UInt], None)
_rlLoadShaderCode = _wrap(rlapi.rlLoadShaderCode, [CharPtr, CharPtr], UInt)
_rlCompileShader = _wrap(rlapi.rlCompileShader, [CharPtr, Int], UInt)
_rlLoadShaderProgram = _wrap(rlapi.rlLoadShaderProgram, [UInt, UInt], UInt)
_rlUnloadShaderProgram = _wrap(rlapi.rlUnloadShaderProgram, [UInt], None)
_rlGetLocationUniform = _wrap(rlapi.rlGetLocationUniform, [UInt, CharPtr], Int)
_rlGetLocationAttrib = _wrap(rlapi.rlGetLocationAttrib, [UInt, CharPtr], Int)
_rlSetUniform = _wrap(rlapi.rlSetUniform, [Int, VoidPtr, Int, Int], None)
_rlSetUniformMatrix = _wrap(rlapi.rlSetUniformMatrix, [Int, Matrix], None)
_rlSetUniformSampler = _wrap(rlapi.rlSetUniformSampler, [Int, UInt], None)
_rlSetShader = _wrap(rlapi.rlSetShader, [UInt, IntPtr], None)
_rlLoadComputeShaderProgram = _wrap(rlapi.rlLoadComputeShaderProgram, [UInt], UInt)
_rlComputeShaderDispatch = _wrap(rlapi.rlComputeShaderDispatch, [UInt, UInt, UInt], None)
_rlLoadShaderBuffer = _wrap(rlapi.rlLoadShaderBuffer, [ULongLongPtr, VoidPtr, Int], UInt)
_rlUnloadShaderBuffer = _wrap(rlapi.rlUnloadShaderBuffer, [UInt], None)
_rlUpdateShaderBufferElements = _wrap(rlapi.rlUpdateShaderBufferElements, [UInt, VoidPtr, ULongLongPtr, ULongLongPtr], None)
_rlGetShaderBufferSize = _wrap(rlapi.rlGetShaderBufferSize, [UInt], ULongLongPtr)
_rlReadShaderBufferElements = _wrap(rlapi.rlReadShaderBufferElements, [UInt, VoidPtr, ULongLongPtr, ULongLongPtr], None)
_rlBindShaderBuffer = _wrap(rlapi.rlBindShaderBuffer, [UInt, UInt], None)
_rlCopyBuffersElements = _wrap(rlapi.rlCopyBuffersElements, [UInt, UInt, ULongLongPtr, ULongLongPtr, ULongLongPtr], None)
_rlBindImageTexture = _wrap(rlapi.rlBindImageTexture, [UInt, UInt, UInt, Int], None)
_rlGetMatrixModelview = _wrap(rlapi.rlGetMatrixModelview, [], Matrix)
_rlGetMatrixProjection = _wrap(rlapi.rlGetMatrixProjection, [], Matrix)
_rlGetMatrixTransform = _wrap(rlapi.rlGetMatrixTransform, [], Matrix)
_rlGetMatrixProjectionStereo = _wrap(rlapi.rlGetMatrixProjectionStereo, [Int], Matrix)
_rlGetMatrixViewOffsetStereo = _wrap(rlapi.rlGetMatrixViewOffsetStereo, [Int], Matrix)
_rlSetMatrixProjection = _wrap(rlapi.rlSetMatrixProjection, [Matrix], None)
_rlSetMatrixModelview = _wrap(rlapi.rlSetMatrixModelview, [Matrix], None)
_rlSetMatrixProjectionStereo = _wrap(rlapi.rlSetMatrixProjectionStereo, [Matrix, Matrix], None)
_rlSetMatrixViewOffsetStereo = _wrap(rlapi.rlSetMatrixViewOffsetStereo, [Matrix, Matrix], None)
_rlLoadDrawCube = _wrap(rlapi.rlLoadDrawCube, [], None)
_rlLoadDrawQuad = _wrap(rlapi.rlLoadDrawQuad, [], None)


def init_window(width, height, title):
    # type: (int, int, Union[str, CharPtr]) -> None
    """Initialize window and OpenGL context"""
    _InitWindow(int(width), int(height), _str_in(title))


def window_should_close():
    # type: () -> bool
    """Check if KEY_ESCAPE pressed or Close icon pressed"""
    result = _WindowShouldClose()
    return result


def close_window():
    # type: () -> None
    """Close window and unload OpenGL context"""
    _CloseWindow()


def is_window_ready():
    # type: () -> bool
    """Check if window has been initialized successfully"""
    result = _IsWindowReady()
    return result


def is_window_fullscreen():
    # type: () -> bool
    """Check if window is currently fullscreen"""
    result = _IsWindowFullscreen()
    return result


def is_window_hidden():
    # type: () -> bool
    """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
    result = _IsWindowHidden()
    return result


def is_window_minimized():
    # type: () -> bool
    """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
    result = _IsWindowMinimized()
    return result


def is_window_maximized():
    # type: () -> bool
    """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
    result = _IsWindowMaximized()
    return result


def is_window_focused():
    # type: () -> bool
    """Check if window is currently focused (only PLATFORM_DESKTOP)"""
    result = _IsWindowFocused()
    return result


def is_window_resized():
    # type: () -> bool
    """Check if window has been resized last frame"""
    result = _IsWindowResized()
    return result


def is_window_state(flag):
    # type: (int) -> bool
    """Check if one specific window flag is enabled"""
    result = _IsWindowState(flag)
    return result


def set_window_state(flags):
    # type: (int) -> None
    """Set window configuration state using flags (only PLATFORM_DESKTOP)"""
    _SetWindowState(flags)


def clear_window_state(flags):
    # type: (int) -> None
    """Clear window configuration state flags"""
    _ClearWindowState(flags)


def toggle_fullscreen():
    # type: () -> None
    """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
    _ToggleFullscreen()


def maximize_window():
    # type: () -> None
    """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
    _MaximizeWindow()


def minimize_window():
    # type: () -> None
    """Set window state: minimized, if resizable (only PLATFORM_DESKTOP)"""
    _MinimizeWindow()


def restore_window():
    # type: () -> None
    """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
    _RestoreWindow()


def set_window_icon(image):
    # type: (Image) -> None
    """Set icon for window (only PLATFORM_DESKTOP)"""
    _SetWindowIcon(image)


def set_window_title(title):
    # type: (Union[str, CharPtr]) -> None
    """Set title for window (only PLATFORM_DESKTOP)"""
    _SetWindowTitle(_str_in(title))


def set_window_position(x, y):
    # type: (int, int) -> None
    """Set window position on screen (only PLATFORM_DESKTOP)"""
    _SetWindowPosition(int(x), int(y))


def set_window_monitor(monitor):
    # type: (int) -> None
    """Set monitor for the current window (fullscreen mode)"""
    _SetWindowMonitor(int(monitor))


def set_window_min_size(width, height):
    # type: (int, int) -> None
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
    _SetWindowMinSize(int(width), int(height))


def set_window_size(width, height):
    # type: (int, int) -> None
    """Set window dimensions"""
    _SetWindowSize(int(width), int(height))


def set_window_opacity(opacity):
    # type: (float) -> None
    """Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)"""
    _SetWindowOpacity(float(opacity))


def get_window_handle():
    # type: () -> bytes
    """Get native window handle"""
    _GetWindowHandle()


def get_screen_width():
    # type: () -> int
    """Get current screen width"""
    result = _GetScreenWidth()
    return result


def get_screen_height():
    # type: () -> int
    """Get current screen height"""
    result = _GetScreenHeight()
    return result


def get_render_width():
    # type: () -> int
    """Get current render width (it considers HiDPI)"""
    result = _GetRenderWidth()
    return result


def get_render_height():
    # type: () -> int
    """Get current render height (it considers HiDPI)"""
    result = _GetRenderHeight()
    return result


def get_monitor_count():
    # type: () -> int
    """Get number of connected monitors"""
    result = _GetMonitorCount()
    return result


def get_current_monitor():
    # type: () -> int
    """Get current connected monitor"""
    result = _GetCurrentMonitor()
    return result


def get_monitor_position(monitor):
    # type: (int) -> Vector2
    """Get specified monitor position"""
    result = _GetMonitorPosition(int(monitor))
    return result


def get_monitor_width(monitor):
    # type: (int) -> int
    """Get specified monitor width (current video mode used by monitor)"""
    result = _GetMonitorWidth(int(monitor))
    return result


def get_monitor_height(monitor):
    # type: (int) -> int
    """Get specified monitor height (current video mode used by monitor)"""
    result = _GetMonitorHeight(int(monitor))
    return result


def get_monitor_physical_width(monitor):
    # type: (int) -> int
    """Get specified monitor physical width in millimetres"""
    result = _GetMonitorPhysicalWidth(int(monitor))
    return result


def get_monitor_physical_height(monitor):
    # type: (int) -> int
    """Get specified monitor physical height in millimetres"""
    result = _GetMonitorPhysicalHeight(int(monitor))
    return result


def get_monitor_refresh_rate(monitor):
    # type: (int) -> int
    """Get specified monitor refresh rate"""
    result = _GetMonitorRefreshRate(int(monitor))
    return result


def get_window_position():
    # type: () -> Vector2
    """Get window position XY on monitor"""
    result = _GetWindowPosition()
    return result


def get_window_scale_dpi():
    # type: () -> Vector2
    """Get window scale DPI factor"""
    result = _GetWindowScaleDPI()
    return result


def get_monitor_name(monitor):
    # type: (int) -> Union[str, CharPtr]
    """Get the human-readable, UTF-8 encoded name of the primary monitor"""
    result = _ptr_out(_GetMonitorName(int(monitor)))
    return result


def set_clipboard_text(text):
    # type: (Union[str, CharPtr]) -> None
    """Set clipboard text content"""
    _SetClipboardText(_str_in(text))


def get_clipboard_text():
    # type: () -> Union[str, CharPtr]
    """Get clipboard text content"""
    result = _ptr_out(_GetClipboardText())
    return result


def enable_event_waiting():
    # type: () -> None
    """Enable waiting for events on EndDrawing(), no automatic event polling"""
    _EnableEventWaiting()


def disable_event_waiting():
    # type: () -> None
    """Disable waiting for events on EndDrawing(), automatic events polling"""
    _DisableEventWaiting()


def swap_screen_buffer():
    # type: () -> None
    """Swap back buffer with front buffer (screen drawing)"""
    _SwapScreenBuffer()


def poll_input_events():
    # type: () -> None
    """Register all input events"""
    _PollInputEvents()


def wait_time(seconds):
    # type: (float) -> None
    """Wait for some time (halt program execution)"""
    _WaitTime(float(seconds))


def show_cursor():
    # type: () -> None
    """Shows cursor"""
    _ShowCursor()


def hide_cursor():
    # type: () -> None
    """Hides cursor"""
    _HideCursor()


def is_cursor_hidden():
    # type: () -> bool
    """Check if cursor is not visible"""
    result = _IsCursorHidden()
    return result


def enable_cursor():
    # type: () -> None
    """Enables cursor (unlock cursor)"""
    _EnableCursor()


def disable_cursor():
    # type: () -> None
    """Disables cursor (lock cursor)"""
    _DisableCursor()


def is_cursor_on_screen():
    # type: () -> bool
    """Check if cursor is on the screen"""
    result = _IsCursorOnScreen()
    return result


def clear_background(color):
    # type: (Color) -> None
    """Set background color (framebuffer clear color)"""
    _ClearBackground(_color(color))


def begin_drawing():
    # type: () -> None
    """Setup canvas (framebuffer) to start drawing"""
    _BeginDrawing()


def end_drawing():
    # type: () -> None
    """End canvas drawing and swap buffers (double buffering)"""
    _EndDrawing()


def begin_mode2d(camera):
    # type: (Camera2D) -> None
    """Begin 2D mode with custom camera (2D)"""
    _BeginMode2D(camera)


def end_mode2d():
    # type: () -> None
    """Ends 2D mode with custom camera"""
    _EndMode2D()


def begin_mode3d(camera):
    # type: (Camera3D) -> None
    """Begin 3D mode with custom camera (3D)"""
    _BeginMode3D(camera)


def end_mode3d():
    # type: () -> None
    """Ends 3D mode and returns to default 2D orthographic mode"""
    _EndMode3D()


def begin_texture_mode(target):
    # type: (RenderTexture2D) -> None
    """Begin drawing to render texture"""
    _BeginTextureMode(target)


def end_texture_mode():
    # type: () -> None
    """Ends drawing to render texture"""
    _EndTextureMode()


def begin_shader_mode(shader):
    # type: (Shader) -> None
    """Begin custom shader drawing"""
    _BeginShaderMode(shader)


def end_shader_mode():
    # type: () -> None
    """End custom shader drawing (use default shader)"""
    _EndShaderMode()


def begin_blend_mode(mode):
    # type: (int) -> None
    """Begin blending mode (alpha, additive, multiplied, subtract, custom)"""
    _BeginBlendMode(int(mode))


def end_blend_mode():
    # type: () -> None
    """End blending mode (reset to default: alpha blending)"""
    _EndBlendMode()


def begin_scissor_mode(x, y, width, height):
    # type: (int, int, int, int) -> None
    """Begin scissor mode (define screen area for following drawing)"""
    _BeginScissorMode(int(x), int(y), int(width), int(height))


def end_scissor_mode():
    # type: () -> None
    """End scissor mode"""
    _EndScissorMode()


def begin_vr_stereo_mode(config):
    # type: (VrStereoConfig) -> None
    """Begin stereo rendering (requires VR simulator)"""
    _BeginVrStereoMode(config)


def end_vr_stereo_mode():
    # type: () -> None
    """End stereo rendering (requires VR simulator)"""
    _EndVrStereoMode()


def load_vr_stereo_config(device):
    # type: (VrDeviceInfo) -> VrStereoConfig
    """Load VR stereo config for VR simulator device parameters"""
    result = _LoadVrStereoConfig(device)
    return result


def unload_vr_stereo_config(config):
    # type: (VrStereoConfig) -> None
    """Unload VR stereo config"""
    _UnloadVrStereoConfig(config)


def load_shader(vs_file_name, fs_file_name):
    # type: (Union[str, CharPtr], Union[str, CharPtr]) -> Shader
    """Load shader from files and bind default locations"""
    result = _LoadShader(_str_in(vs_file_name), _str_in(fs_file_name))
    return result


def load_shader_from_memory(vs_code, fs_code):
    # type: (Union[str, CharPtr], Union[str, CharPtr]) -> Shader
    """Load shader from code strings and bind default locations"""
    result = _LoadShaderFromMemory(_str_in(vs_code), _str_in(fs_code))
    return result


def get_shader_location(shader, uniform_name):
    # type: (Shader, Union[str, CharPtr]) -> int
    """Get shader uniform location"""
    result = _GetShaderLocation(shader, _str_in(uniform_name))
    return result


def get_shader_location_attrib(shader, attrib_name):
    # type: (Shader, Union[str, CharPtr]) -> int
    """Get shader attribute location"""
    result = _GetShaderLocationAttrib(shader, _str_in(attrib_name))
    return result


def set_shader_value(shader, loc_index, value, uniform_type):
    # type: (Shader, int, bytes, int) -> None
    """Set shader uniform value"""
    _SetShaderValue(shader, int(loc_index), value, int(uniform_type))


def set_shader_value_v(shader, loc_index, value, uniform_type, count):
    # type: (Shader, int, bytes, int, int) -> None
    """Set shader uniform value vector"""
    _SetShaderValueV(shader, int(loc_index), value, int(uniform_type), int(count))


def set_shader_value_matrix(shader, loc_index, mat):
    # type: (Shader, int, Matrix) -> None
    """Set shader uniform value (matrix 4x4)"""
    _SetShaderValueMatrix(shader, int(loc_index), mat)


def set_shader_value_texture(shader, loc_index, texture):
    # type: (Shader, int, Texture2D) -> None
    """Set shader uniform value for texture (sampler2d)"""
    _SetShaderValueTexture(shader, int(loc_index), texture)


def unload_shader(shader):
    # type: (Shader) -> None
    """Unload shader from GPU memory (VRAM)"""
    _UnloadShader(shader)


def get_mouse_ray(mouse_position, camera):
    # type: (Vector2, Camera) -> Ray
    """Get a ray trace from mouse position"""
    result = _GetMouseRay(_vec2(mouse_position), camera)
    return result


def get_camera_matrix(camera):
    # type: (Camera) -> Matrix
    """Get camera transform matrix (view matrix)"""
    result = _GetCameraMatrix(camera)
    return result


def get_camera_matrix2d(camera):
    # type: (Camera2D) -> Matrix
    """Get camera 2d transform matrix"""
    result = _GetCameraMatrix2D(camera)
    return result


def get_world_to_screen(position, camera):
    # type: (Vector3, Camera) -> Vector2
    """Get the screen space position for a 3d world space position"""
    result = _GetWorldToScreen(_vec3(position), camera)
    return result


def get_screen_to_world2d(position, camera):
    # type: (Vector2, Camera2D) -> Vector2
    """Get the world space position for a 2d camera screen space position"""
    result = _GetScreenToWorld2D(_vec2(position), camera)
    return result


def get_world_to_screen_ex(position, camera, width, height):
    # type: (Vector3, Camera, int, int) -> Vector2
    """Get size position for a 3d world space position"""
    result = _GetWorldToScreenEx(_vec3(position), camera, int(width), int(height))
    return result


def get_world_to_screen2d(position, camera):
    # type: (Vector2, Camera2D) -> Vector2
    """Get the screen space position for a 2d camera world space position"""
    result = _GetWorldToScreen2D(_vec2(position), camera)
    return result


def set_target_fps(fps):
    # type: (int) -> None
    """Set target FPS (maximum)"""
    _SetTargetFPS(int(fps))


def get_fps():
    # type: () -> int
    """Get current FPS"""
    result = _GetFPS()
    return result


def get_frame_time():
    # type: () -> float
    """Get time in seconds for last frame drawn (delta time)"""
    result = _GetFrameTime()
    return result


def get_time():
    # type: () -> float
    """Get elapsed time in seconds since InitWindow()"""
    result = _GetTime()
    return result


def get_random_value(min, max):
    # type: (int, int) -> int
    """Get a random value between min and max (both included)"""
    result = _GetRandomValue(int(min), int(max))
    return result


def set_random_seed(seed):
    # type: (int) -> None
    """Set the seed for the random number generator"""
    _SetRandomSeed(seed)


def take_screenshot(file_name):
    # type: (Union[str, CharPtr]) -> None
    """Takes a screenshot of current screen (filename extension defines format)"""
    _TakeScreenshot(_str_in(file_name))


def set_config_flags(flags):
    # type: (int) -> None
    """Setup init configuration flags (view FLAGS)"""
    _SetConfigFlags(flags)


def trace_log(log_level, text, args):
    # type: (int, Union[str, CharPtr], bytes) -> None
    """Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)"""
    _TraceLog(int(log_level), _str_in(text), args)


def set_trace_log_level(log_level):
    # type: (int) -> None
    """Set the current threshold (minimum) log level"""
    _SetTraceLogLevel(int(log_level))


def mem_alloc(size):
    # type: (int) -> bytes
    """Internal memory allocator"""
    _MemAlloc(int(size))


def mem_realloc(ptr, size):
    # type: (bytes, int) -> bytes
    """Internal memory reallocator"""
    _MemRealloc(ptr, int(size))


def mem_free(ptr):
    # type: (bytes) -> None
    """Internal memory free"""
    _MemFree(ptr)


def open_url(url):
    # type: (Union[str, CharPtr]) -> None
    """Open URL with default system browser (if available)"""
    _OpenURL(_str_in(url))


def set_trace_log_callback(callback):
    # type: (TraceLogCallback) -> None
    """Set custom trace log"""
    _SetTraceLogCallback(callback)


def set_load_file_data_callback(callback):
    # type: (LoadFileDataCallback) -> None
    """Set custom file binary data loader"""
    _SetLoadFileDataCallback(callback)


def set_save_file_data_callback(callback):
    # type: (SaveFileDataCallback) -> None
    """Set custom file binary data saver"""
    _SetSaveFileDataCallback(callback)


def set_load_file_text_callback(callback):
    # type: (LoadFileTextCallback) -> None
    """Set custom file text data loader"""
    _SetLoadFileTextCallback(callback)


def set_save_file_text_callback(callback):
    # type: (SaveFileTextCallback) -> None
    """Set custom file text data saver"""
    _SetSaveFileTextCallback(callback)


def load_file_data(file_name, bytes_read):
    # type: (Union[str, CharPtr], Union[Seq[int], UIntPtr]) -> Union[Seq[int], UCharPtr]
    """Load file data as byte array (read)"""
    result = _ptr_out(_LoadFileData(_str_in(file_name), bytes_read))
    return result


def unload_file_data(data):
    # type: (Union[Seq[int], UCharPtr]) -> None
    """Unload file data allocated by LoadFileData()"""
    _UnloadFileData(_str_in(data))


def save_file_data(file_name, data, bytes_to_write):
    # type: (Union[str, CharPtr], bytes, int) -> bool
    """Save data to file from byte array (write), returns true on success"""
    result = _SaveFileData(_str_in(file_name), data, bytes_to_write)
    return result


def export_data_as_code(data, size, file_name):
    # type: (Union[str, CharPtr], int, Union[str, CharPtr]) -> bool
    """Export data to code (.h), returns true on success"""
    result = _ExportDataAsCode(_str_in(data), size, _str_in(file_name))
    return result


def load_file_text(file_name):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Load text data from file (read), returns a '\0' terminated string"""
    result = _ptr_out(_LoadFileText(_str_in(file_name)))
    return result


def unload_file_text(text):
    # type: (Union[str, CharPtr]) -> None
    """Unload file text data allocated by LoadFileText()"""
    _UnloadFileText(_str_in(text))


def save_file_text(file_name, text):
    # type: (Union[str, CharPtr], Union[str, CharPtr]) -> bool
    """Save text data to file (write), string must be '\0' terminated, returns true on success"""
    result = _SaveFileText(_str_in(file_name), _str_in(text))
    return result


def file_exists(file_name):
    # type: (Union[str, CharPtr]) -> bool
    """Check if file exists"""
    result = _FileExists(_str_in(file_name))
    return result


def directory_exists(dir_path):
    # type: (Union[str, CharPtr]) -> bool
    """Check if a directory path exists"""
    result = _DirectoryExists(_str_in(dir_path))
    return result


def is_file_extension(file_name, ext):
    # type: (Union[str, CharPtr], Union[str, CharPtr]) -> bool
    """Check file extension (including point: .png, .wav)"""
    result = _IsFileExtension(_str_in(file_name), _str_in(ext))
    return result


def get_file_length(file_name):
    # type: (Union[str, CharPtr]) -> int
    """Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)"""
    result = _GetFileLength(_str_in(file_name))
    return result


def get_file_extension(file_name):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Get pointer to extension for a filename string (includes dot: '.png')"""
    result = _ptr_out(_GetFileExtension(_str_in(file_name)))
    return result


def get_file_name(file_path):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Get pointer to filename for a path string"""
    result = _ptr_out(_GetFileName(_str_in(file_path)))
    return result


def get_file_name_without_ext(file_path):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Get filename string without extension (uses static string)"""
    result = _ptr_out(_GetFileNameWithoutExt(_str_in(file_path)))
    return result


def get_directory_path(file_path):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Get full path for a given fileName with path (uses static string)"""
    result = _ptr_out(_GetDirectoryPath(_str_in(file_path)))
    return result


def get_prev_directory_path(dir_path):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Get previous directory path for a given path (uses static string)"""
    result = _ptr_out(_GetPrevDirectoryPath(_str_in(dir_path)))
    return result


def get_working_directory():
    # type: () -> Union[str, CharPtr]
    """Get current working directory (uses static string)"""
    result = _ptr_out(_GetWorkingDirectory())
    return result


def get_application_directory():
    # type: () -> Union[str, CharPtr]
    """Get the directory if the running application (uses static string)"""
    result = _ptr_out(_GetApplicationDirectory())
    return result


def change_directory(dir):
    # type: (Union[str, CharPtr]) -> bool
    """Change working directory, return true on success"""
    result = _ChangeDirectory(_str_in(dir))
    return result


def is_path_file(path):
    # type: (Union[str, CharPtr]) -> bool
    """Check if a given path is a file or a directory"""
    result = _IsPathFile(_str_in(path))
    return result


def load_directory_files(dir_path):
    # type: (Union[str, CharPtr]) -> FilePathList
    """Load directory filepaths"""
    result = _LoadDirectoryFiles(_str_in(dir_path))
    return result


def load_directory_files_ex(base_path, filter, scan_subdirs):
    # type: (Union[str, CharPtr], Union[str, CharPtr], bool) -> FilePathList
    """Load directory filepaths with extension filtering and recursive directory scan"""
    result = _LoadDirectoryFilesEx(_str_in(base_path), _str_in(filter), bool(scan_subdirs))
    return result


def unload_directory_files(files):
    # type: (FilePathList) -> None
    """Unload filepaths"""
    _UnloadDirectoryFiles(files)


def is_file_dropped():
    # type: () -> bool
    """Check if a file has been dropped into window"""
    result = _IsFileDropped()
    return result


def load_dropped_files():
    # type: () -> FilePathList
    """Load dropped filepaths"""
    result = _LoadDroppedFiles()
    return result


def unload_dropped_files(files):
    # type: (FilePathList) -> None
    """Unload dropped filepaths"""
    _UnloadDroppedFiles(files)


def get_file_mod_time(file_name):
    # type: (Union[str, CharPtr]) -> int
    """Get file modification time (last write time)"""
    result = _GetFileModTime(_str_in(file_name))
    return result


def compress_data(data, data_size, comp_data_size):
    # type: (Union[Seq[int], UCharPtr], int, Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
    """Compress data (DEFLATE algorithm), memory must be MemFree()"""
    result = _ptr_out(_CompressData(_str_in(data), int(data_size), comp_data_size))
    return result


def decompress_data(comp_data, comp_data_size, data_size):
    # type: (Union[Seq[int], UCharPtr], int, Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
    """Decompress data (DEFLATE algorithm), memory must be MemFree()"""
    result = _ptr_out(_DecompressData(_str_in(comp_data), int(comp_data_size), data_size))
    return result


def encode_data_base64(data, data_size, output_size):
    # type: (Union[Seq[int], UCharPtr], int, Union[Seq[int], IntPtr]) -> Union[str, CharPtr]
    """Encode data to Base64 string, memory must be MemFree()"""
    result = _ptr_out(_EncodeDataBase64(_str_in(data), int(data_size), output_size))
    return result


def decode_data_base64(data, output_size):
    # type: (Union[Seq[int], UCharPtr], Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
    """Decode Base64 string data, memory must be MemFree()"""
    result = _ptr_out(_DecodeDataBase64(_str_in(data), output_size))
    return result


def is_key_pressed(key):
    # type: (int) -> bool
    """Check if a key has been pressed once"""
    result = _IsKeyPressed(int(key))
    return result


def is_key_down(key):
    # type: (int) -> bool
    """Check if a key is being pressed"""
    result = _IsKeyDown(int(key))
    return result


def is_key_released(key):
    # type: (int) -> bool
    """Check if a key has been released once"""
    result = _IsKeyReleased(int(key))
    return result


def is_key_up(key):
    # type: (int) -> bool
    """Check if a key is NOT being pressed"""
    result = _IsKeyUp(int(key))
    return result


def set_exit_key(key):
    # type: (int) -> None
    """Set a custom key to exit program (default is ESC)"""
    _SetExitKey(int(key))


def get_key_pressed():
    # type: () -> int
    """Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty"""
    result = _GetKeyPressed()
    return result


def get_char_pressed():
    # type: () -> int
    """Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty"""
    result = _GetCharPressed()
    return result


def is_gamepad_available(gamepad):
    # type: (int) -> bool
    """Check if a gamepad is available"""
    result = _IsGamepadAvailable(int(gamepad))
    return result


def get_gamepad_name(gamepad):
    # type: (int) -> Union[str, CharPtr]
    """Get gamepad internal name id"""
    result = _ptr_out(_GetGamepadName(int(gamepad)))
    return result


def is_gamepad_button_pressed(gamepad, button):
    # type: (int, int) -> bool
    """Check if a gamepad button has been pressed once"""
    result = _IsGamepadButtonPressed(int(gamepad), int(button))
    return result


def is_gamepad_button_down(gamepad, button):
    # type: (int, int) -> bool
    """Check if a gamepad button is being pressed"""
    result = _IsGamepadButtonDown(int(gamepad), int(button))
    return result


def is_gamepad_button_released(gamepad, button):
    # type: (int, int) -> bool
    """Check if a gamepad button has been released once"""
    result = _IsGamepadButtonReleased(int(gamepad), int(button))
    return result


def is_gamepad_button_up(gamepad, button):
    # type: (int, int) -> bool
    """Check if a gamepad button is NOT being pressed"""
    result = _IsGamepadButtonUp(int(gamepad), int(button))
    return result


def get_gamepad_button_pressed():
    # type: () -> int
    """Get the last gamepad button pressed"""
    result = _GetGamepadButtonPressed()
    return result


def get_gamepad_axis_count(gamepad):
    # type: (int) -> int
    """Get gamepad axis count for a gamepad"""
    result = _GetGamepadAxisCount(int(gamepad))
    return result


def get_gamepad_axis_movement(gamepad, axis):
    # type: (int, int) -> float
    """Get axis movement value for a gamepad axis"""
    result = _GetGamepadAxisMovement(int(gamepad), int(axis))
    return result


def set_gamepad_mappings(mappings):
    # type: (Union[str, CharPtr]) -> int
    """Set internal gamepad mappings (SDL_GameControllerDB)"""
    result = _SetGamepadMappings(_str_in(mappings))
    return result


def is_mouse_button_pressed(button):
    # type: (int) -> bool
    """Check if a mouse button has been pressed once"""
    result = _IsMouseButtonPressed(int(button))
    return result


def is_mouse_button_down(button):
    # type: (int) -> bool
    """Check if a mouse button is being pressed"""
    result = _IsMouseButtonDown(int(button))
    return result


def is_mouse_button_released(button):
    # type: (int) -> bool
    """Check if a mouse button has been released once"""
    result = _IsMouseButtonReleased(int(button))
    return result


def is_mouse_button_up(button):
    # type: (int) -> bool
    """Check if a mouse button is NOT being pressed"""
    result = _IsMouseButtonUp(int(button))
    return result


def get_mouse_x():
    # type: () -> int
    """Get mouse position X"""
    result = _GetMouseX()
    return result


def get_mouse_y():
    # type: () -> int
    """Get mouse position Y"""
    result = _GetMouseY()
    return result


def get_mouse_position():
    # type: () -> Vector2
    """Get mouse position XY"""
    result = _GetMousePosition()
    return result


def get_mouse_delta():
    # type: () -> Vector2
    """Get mouse delta between frames"""
    result = _GetMouseDelta()
    return result


def set_mouse_position(x, y):
    # type: (int, int) -> None
    """Set mouse position XY"""
    _SetMousePosition(int(x), int(y))


def set_mouse_offset(offset_x, offset_y):
    # type: (int, int) -> None
    """Set mouse offset"""
    _SetMouseOffset(int(offset_x), int(offset_y))


def set_mouse_scale(scale_x, scale_y):
    # type: (float, float) -> None
    """Set mouse scaling"""
    _SetMouseScale(float(scale_x), float(scale_y))


def get_mouse_wheel_move():
    # type: () -> float
    """Get mouse wheel movement for X or Y, whichever is larger"""
    result = _GetMouseWheelMove()
    return result


def get_mouse_wheel_move_v():
    # type: () -> Vector2
    """Get mouse wheel movement for both X and Y"""
    result = _GetMouseWheelMoveV()
    return result


def set_mouse_cursor(cursor):
    # type: (int) -> None
    """Set mouse cursor"""
    _SetMouseCursor(int(cursor))


def get_touch_x():
    # type: () -> int
    """Get touch position X for touch point 0 (relative to screen size)"""
    result = _GetTouchX()
    return result


def get_touch_y():
    # type: () -> int
    """Get touch position Y for touch point 0 (relative to screen size)"""
    result = _GetTouchY()
    return result


def get_touch_position(index):
    # type: (int) -> Vector2
    """Get touch position XY for a touch point index (relative to screen size)"""
    result = _GetTouchPosition(int(index))
    return result


def get_touch_point_id(index):
    # type: (int) -> int
    """Get touch point identifier for given index"""
    result = _GetTouchPointId(int(index))
    return result


def get_touch_point_count():
    # type: () -> int
    """Get number of touch points"""
    result = _GetTouchPointCount()
    return result


def set_gestures_enabled(flags):
    # type: (int) -> None
    """Enable a set of gestures using flags"""
    _SetGesturesEnabled(flags)


def is_gesture_detected(gesture):
    # type: (int) -> bool
    """Check if a gesture have been detected"""
    result = _IsGestureDetected(int(gesture))
    return result


def get_gesture_detected():
    # type: () -> int
    """Get latest detected gesture"""
    result = _GetGestureDetected()
    return result


def get_gesture_hold_duration():
    # type: () -> float
    """Get gesture hold time in milliseconds"""
    result = _GetGestureHoldDuration()
    return result


def get_gesture_drag_vector():
    # type: () -> Vector2
    """Get gesture drag vector"""
    result = _GetGestureDragVector()
    return result


def get_gesture_drag_angle():
    # type: () -> float
    """Get gesture drag angle"""
    result = _GetGestureDragAngle()
    return result


def get_gesture_pinch_vector():
    # type: () -> Vector2
    """Get gesture pinch delta"""
    result = _GetGesturePinchVector()
    return result


def get_gesture_pinch_angle():
    # type: () -> float
    """Get gesture pinch angle"""
    result = _GetGesturePinchAngle()
    return result


def set_camera_mode(camera, mode):
    # type: (Camera, int) -> None
    """Set camera mode (multiple camera modes available)"""
    _SetCameraMode(camera, int(mode))


def update_camera(camera):
    # type: (CameraPtr) -> None
    """Update camera position for selected mode"""
    _UpdateCamera(camera)


def set_camera_pan_control(key_pan):
    # type: (int) -> None
    """Set camera pan key to combine with mouse movement (free camera)"""
    _SetCameraPanControl(int(key_pan))


def set_camera_alt_control(key_alt):
    # type: (int) -> None
    """Set camera alt key to combine with mouse movement (free camera)"""
    _SetCameraAltControl(int(key_alt))


def set_camera_smooth_zoom_control(key_smooth_zoom):
    # type: (int) -> None
    """Set camera smooth zoom key to combine with mouse (free camera)"""
    _SetCameraSmoothZoomControl(int(key_smooth_zoom))


def set_camera_move_controls(key_front, key_back, key_right, key_left, key_up, key_down):
    # type: (int, int, int, int, int, int) -> None
    """Set camera move controls (1st person and 3rd person cameras)"""
    _SetCameraMoveControls(int(key_front), int(key_back), int(key_right), int(key_left), int(key_up), int(key_down))


def set_shapes_texture(texture, source):
    # type: (Texture2D, Rectangle) -> None
    """Set texture and rectangle to be used on shapes drawing"""
    _SetShapesTexture(texture, _rect(source))


def draw_pixel(pos_x, pos_y, color):
    # type: (int, int, Color) -> None
    """Draw a pixel"""
    _DrawPixel(int(pos_x), int(pos_y), _color(color))


def draw_pixel_v(position, color):
    # type: (Vector2, Color) -> None
    """Draw a pixel (Vector version)"""
    _DrawPixelV(_vec2(position), _color(color))


def draw_line(start_pos_x, start_pos_y, end_pos_x, end_pos_y, color):
    # type: (int, int, int, int, Color) -> None
    """Draw a line"""
    _DrawLine(int(start_pos_x), int(start_pos_y), int(end_pos_x), int(end_pos_y), _color(color))


def draw_line_v(start_pos, end_pos, color):
    # type: (Vector2, Vector2, Color) -> None
    """Draw a line (Vector version)"""
    _DrawLineV(_vec2(start_pos), _vec2(end_pos), _color(color))


def draw_line_ex(start_pos, end_pos, thick, color):
    # type: (Vector2, Vector2, float, Color) -> None
    """Draw a line defining thickness"""
    _DrawLineEx(_vec2(start_pos), _vec2(end_pos), float(thick), _color(color))


def draw_line_bezier(start_pos, end_pos, thick, color):
    # type: (Vector2, Vector2, float, Color) -> None
    """Draw a line using cubic-bezier curves in-out"""
    _DrawLineBezier(_vec2(start_pos), _vec2(end_pos), float(thick), _color(color))


def draw_line_bezier_quad(start_pos, end_pos, control_pos, thick, color):
    # type: (Vector2, Vector2, Vector2, float, Color) -> None
    """Draw line using quadratic bezier curves with a control point"""
    _DrawLineBezierQuad(_vec2(start_pos), _vec2(end_pos), _vec2(control_pos), float(thick), _color(color))


def draw_line_bezier_cubic(start_pos, end_pos, start_control_pos, end_control_pos, thick, color):
    # type: (Vector2, Vector2, Vector2, Vector2, float, Color) -> None
    """Draw line using cubic bezier curves with 2 control points"""
    _DrawLineBezierCubic(_vec2(start_pos), _vec2(end_pos), _vec2(start_control_pos), _vec2(end_control_pos), float(thick), _color(color))


def draw_line_strip(points, color):
    # type: (Vector2Ptr, Color) -> None
    """Draw lines sequence"""
    _DrawLineStrip(_arr_in(Vector2, points), len(points), _color(color))


def draw_circle(center_x, center_y, radius, color):
    # type: (int, int, float, Color) -> None
    """Draw a color-filled circle"""
    _DrawCircle(int(center_x), int(center_y), float(radius), _color(color))


def draw_circle_sector(center, radius, start_angle, end_angle, segments, color):
    # type: (Vector2, float, float, float, int, Color) -> None
    """Draw a piece of a circle"""
    _DrawCircleSector(_vec2(center), float(radius), float(start_angle), float(end_angle), int(segments), _color(color))


def draw_circle_sector_lines(center, radius, start_angle, end_angle, segments, color):
    # type: (Vector2, float, float, float, int, Color) -> None
    """Draw circle sector outline"""
    _DrawCircleSectorLines(_vec2(center), float(radius), float(start_angle), float(end_angle), int(segments), _color(color))


def draw_circle_gradient(center_x, center_y, radius, color1, color2):
    # type: (int, int, float, Color, Color) -> None
    """Draw a gradient-filled circle"""
    _DrawCircleGradient(int(center_x), int(center_y), float(radius), _color(color1), _color(color2))


def draw_circle_v(center, radius, color):
    # type: (Vector2, float, Color) -> None
    """Draw a color-filled circle (Vector version)"""
    _DrawCircleV(_vec2(center), float(radius), _color(color))


def draw_circle_lines(center_x, center_y, radius, color):
    # type: (int, int, float, Color) -> None
    """Draw circle outline"""
    _DrawCircleLines(int(center_x), int(center_y), float(radius), _color(color))


def draw_ellipse(center_x, center_y, radius_h, radius_v, color):
    # type: (int, int, float, float, Color) -> None
    """Draw ellipse"""
    _DrawEllipse(int(center_x), int(center_y), float(radius_h), float(radius_v), _color(color))


def draw_ellipse_lines(center_x, center_y, radius_h, radius_v, color):
    # type: (int, int, float, float, Color) -> None
    """Draw ellipse outline"""
    _DrawEllipseLines(int(center_x), int(center_y), float(radius_h), float(radius_v), _color(color))


def draw_ring(center, inner_radius, outer_radius, start_angle, end_angle, segments, color):
    # type: (Vector2, float, float, float, float, int, Color) -> None
    """Draw ring"""
    _DrawRing(_vec2(center), float(inner_radius), float(outer_radius), float(start_angle), float(end_angle), int(segments), _color(color))


def draw_ring_lines(center, inner_radius, outer_radius, start_angle, end_angle, segments, color):
    # type: (Vector2, float, float, float, float, int, Color) -> None
    """Draw ring outline"""
    _DrawRingLines(_vec2(center), float(inner_radius), float(outer_radius), float(start_angle), float(end_angle), int(segments), _color(color))


def draw_rectangle(pos_x, pos_y, width, height, color):
    # type: (int, int, int, int, Color) -> None
    """Draw a color-filled rectangle"""
    _DrawRectangle(int(pos_x), int(pos_y), int(width), int(height), _color(color))


def draw_rectangle_v(position, size, color):
    # type: (Vector2, Vector2, Color) -> None
    """Draw a color-filled rectangle (Vector version)"""
    _DrawRectangleV(_vec2(position), _vec2(size), _color(color))


def draw_rectangle_rec(rec, color):
    # type: (Rectangle, Color) -> None
    """Draw a color-filled rectangle"""
    _DrawRectangleRec(_rect(rec), _color(color))


def draw_rectangle_pro(rec, origin, rotation, color):
    # type: (Rectangle, Vector2, float, Color) -> None
    """Draw a color-filled rectangle with pro parameters"""
    _DrawRectanglePro(_rect(rec), _vec2(origin), float(rotation), _color(color))


def draw_rectangle_gradient_v(pos_x, pos_y, width, height, color1, color2):
    # type: (int, int, int, int, Color, Color) -> None
    """Draw a vertical-gradient-filled rectangle"""
    _DrawRectangleGradientV(int(pos_x), int(pos_y), int(width), int(height), _color(color1), _color(color2))


def draw_rectangle_gradient_h(pos_x, pos_y, width, height, color1, color2):
    # type: (int, int, int, int, Color, Color) -> None
    """Draw a horizontal-gradient-filled rectangle"""
    _DrawRectangleGradientH(int(pos_x), int(pos_y), int(width), int(height), _color(color1), _color(color2))


def draw_rectangle_gradient_ex(rec, col1, col2, col3, col4):
    # type: (Rectangle, Color, Color, Color, Color) -> None
    """Draw a gradient-filled rectangle with custom vertex colors"""
    _DrawRectangleGradientEx(_rect(rec), _color(col1), _color(col2), _color(col3), _color(col4))


def draw_rectangle_lines(pos_x, pos_y, width, height, color):
    # type: (int, int, int, int, Color) -> None
    """Draw rectangle outline"""
    _DrawRectangleLines(int(pos_x), int(pos_y), int(width), int(height), _color(color))


def draw_rectangle_lines_ex(rec, line_thick, color):
    # type: (Rectangle, float, Color) -> None
    """Draw rectangle outline with extended parameters"""
    _DrawRectangleLinesEx(_rect(rec), float(line_thick), _color(color))


def draw_rectangle_rounded(rec, roundness, segments, color):
    # type: (Rectangle, float, int, Color) -> None
    """Draw rectangle with rounded edges"""
    _DrawRectangleRounded(_rect(rec), float(roundness), int(segments), _color(color))


def draw_rectangle_rounded_lines(rec, roundness, segments, line_thick, color):
    # type: (Rectangle, float, int, float, Color) -> None
    """Draw rectangle with rounded edges outline"""
    _DrawRectangleRoundedLines(_rect(rec), float(roundness), int(segments), float(line_thick), _color(color))


def draw_triangle(v1, v2, v3, color):
    # type: (Vector2, Vector2, Vector2, Color) -> None
    """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
    _DrawTriangle(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


def draw_triangle_lines(v1, v2, v3, color):
    # type: (Vector2, Vector2, Vector2, Color) -> None
    """Draw triangle outline (vertex in counter-clockwise order!)"""
    _DrawTriangleLines(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


def draw_triangle_fan(points, color):
    # type: (Vector2Ptr, Color) -> None
    """Draw a triangle fan defined by points (first vertex is the center)"""
    _DrawTriangleFan(_arr_in(Vector2, points), len(points), _color(color))


def draw_triangle_strip(points, color):
    # type: (Vector2Ptr, Color) -> None
    """Draw a triangle strip defined by points"""
    _DrawTriangleStrip(_arr_in(Vector2, points), len(points), _color(color))


def draw_poly(center, sides, radius, rotation, color):
    # type: (Vector2, int, float, float, Color) -> None
    """Draw a regular polygon (Vector version)"""
    _DrawPoly(_vec2(center), int(sides), float(radius), float(rotation), _color(color))


def draw_poly_lines(center, sides, radius, rotation, color):
    # type: (Vector2, int, float, float, Color) -> None
    """Draw a polygon outline of n sides"""
    _DrawPolyLines(_vec2(center), int(sides), float(radius), float(rotation), _color(color))


def draw_poly_lines_ex(center, sides, radius, rotation, line_thick, color):
    # type: (Vector2, int, float, float, float, Color) -> None
    """Draw a polygon outline of n sides with extended parameters"""
    _DrawPolyLinesEx(_vec2(center), int(sides), float(radius), float(rotation), float(line_thick), _color(color))


def check_collision_recs(rec1, rec2):
    # type: (Rectangle, Rectangle) -> bool
    """Check collision between two rectangles"""
    result = _CheckCollisionRecs(_rect(rec1), _rect(rec2))
    return result


def check_collision_circles(center1, radius1, center2, radius2):
    # type: (Vector2, float, Vector2, float) -> bool
    """Check collision between two circles"""
    result = _CheckCollisionCircles(_vec2(center1), float(radius1), _vec2(center2), float(radius2))
    return result


def check_collision_circle_rec(center, radius, rec):
    # type: (Vector2, float, Rectangle) -> bool
    """Check collision between circle and rectangle"""
    result = _CheckCollisionCircleRec(_vec2(center), float(radius), _rect(rec))
    return result


def check_collision_point_rec(point, rec):
    # type: (Vector2, Rectangle) -> bool
    """Check if point is inside rectangle"""
    result = _CheckCollisionPointRec(_vec2(point), _rect(rec))
    return result


def check_collision_point_circle(point, center, radius):
    # type: (Vector2, Vector2, float) -> bool
    """Check if point is inside circle"""
    result = _CheckCollisionPointCircle(_vec2(point), _vec2(center), float(radius))
    return result


def check_collision_point_triangle(point, p1, p2, p3):
    # type: (Vector2, Vector2, Vector2, Vector2) -> bool
    """Check if point is inside a triangle"""
    result = _CheckCollisionPointTriangle(_vec2(point), _vec2(p1), _vec2(p2), _vec2(p3))
    return result


def check_collision_lines(start_pos1, end_pos1, start_pos2, end_pos2, collision_point):
    # type: (Vector2, Vector2, Vector2, Vector2, Vector2Ptr) -> bool
    """Check the collision between two lines defined by two points each, returns collision point by reference"""
    result = _CheckCollisionLines(_vec2(start_pos1), _vec2(end_pos1), _vec2(start_pos2), _vec2(end_pos2), _vec2(collision_point))
    return result


def check_collision_point_line(point, p1, p2, threshold):
    # type: (Vector2, Vector2, Vector2, int) -> bool
    """Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]"""
    result = _CheckCollisionPointLine(_vec2(point), _vec2(p1), _vec2(p2), int(threshold))
    return result


def get_collision_rec(rec1, rec2):
    # type: (Rectangle, Rectangle) -> Rectangle
    """Get collision rectangle for two rectangles collision"""
    result = _GetCollisionRec(_rect(rec1), _rect(rec2))
    return result


def load_image(file_name):
    # type: (Union[str, CharPtr]) -> Image
    """Load image from file into CPU memory (RAM)"""
    result = _LoadImage(_str_in(file_name))
    return result


def load_image_raw(file_name, width, height, format, header_size):
    # type: (Union[str, CharPtr], int, int, int, int) -> Image
    """Load image from RAW file data"""
    result = _LoadImageRaw(_str_in(file_name), int(width), int(height), int(format), int(header_size))
    return result


def load_image_anim(file_name, frames):
    # type: (Union[str, CharPtr], Union[Seq[int], IntPtr]) -> Image
    """Load image sequence from file (frames appended to image.data)"""
    result = _LoadImageAnim(_str_in(file_name), frames)
    return result


def load_image_from_memory(file_type, file_data, data_size):
    # type: (Union[str, CharPtr], Union[Seq[int], UCharPtr], int) -> Image
    """Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
    result = _LoadImageFromMemory(_str_in(file_type), _str_in(file_data), int(data_size))
    return result


def load_image_from_texture(texture):
    # type: (Texture2D) -> Image
    """Load image from GPU texture data"""
    result = _LoadImageFromTexture(texture)
    return result


def load_image_from_screen():
    # type: () -> Image
    """Load image from screen buffer and (screenshot)"""
    result = _LoadImageFromScreen()
    return result


def unload_image(image):
    # type: (Image) -> None
    """Unload image from CPU memory (RAM)"""
    _UnloadImage(image)


def export_image(image, file_name):
    # type: (Image, Union[str, CharPtr]) -> bool
    """Export image data to file, returns true on success"""
    result = _ExportImage(image, _str_in(file_name))
    return result


def export_image_as_code(image, file_name):
    # type: (Image, Union[str, CharPtr]) -> bool
    """Export image as code file defining an array of bytes, returns true on success"""
    result = _ExportImageAsCode(image, _str_in(file_name))
    return result


def gen_image_color(width, height, color):
    # type: (int, int, Color) -> Image
    """Generate image: plain color"""
    result = _GenImageColor(int(width), int(height), _color(color))
    return result


def gen_image_gradient_v(width, height, top, bottom):
    # type: (int, int, Color, Color) -> Image
    """Generate image: vertical gradient"""
    result = _GenImageGradientV(int(width), int(height), _color(top), _color(bottom))
    return result


def gen_image_gradient_h(width, height, left, right):
    # type: (int, int, Color, Color) -> Image
    """Generate image: horizontal gradient"""
    result = _GenImageGradientH(int(width), int(height), _color(left), _color(right))
    return result


def gen_image_gradient_radial(width, height, density, inner, outer):
    # type: (int, int, float, Color, Color) -> Image
    """Generate image: radial gradient"""
    result = _GenImageGradientRadial(int(width), int(height), float(density), _color(inner), _color(outer))
    return result


def gen_image_checked(width, height, checks_x, checks_y, col1, col2):
    # type: (int, int, int, int, Color, Color) -> Image
    """Generate image: checked"""
    result = _GenImageChecked(int(width), int(height), int(checks_x), int(checks_y), _color(col1), _color(col2))
    return result


def gen_image_white_noise(width, height, factor):
    # type: (int, int, float) -> Image
    """Generate image: white noise"""
    result = _GenImageWhiteNoise(int(width), int(height), float(factor))
    return result


def gen_image_cellular(width, height, tile_size):
    # type: (int, int, int) -> Image
    """Generate image: cellular algorithm, bigger tileSize means bigger cells"""
    result = _GenImageCellular(int(width), int(height), int(tile_size))
    return result


def image_copy(image):
    # type: (Image) -> Image
    """Create an image duplicate (useful for transformations)"""
    result = _ImageCopy(image)
    return result


def image_from_image(image, rec):
    # type: (Image, Rectangle) -> Image
    """Create an image from another image piece"""
    result = _ImageFromImage(image, _rect(rec))
    return result


def image_text(text, font_size, color):
    # type: (Union[str, CharPtr], int, Color) -> Image
    """Create an image from text (default font)"""
    result = _ImageText(_str_in(text), int(font_size), _color(color))
    return result


def image_text_ex(font, text, font_size, spacing, tint):
    # type: (Font, Union[str, CharPtr], float, float, Color) -> Image
    """Create an image from text (custom sprite font)"""
    result = _ImageTextEx(font, _str_in(text), float(font_size), float(spacing), _color(tint))
    return result


def image_format(image, new_format):
    # type: (ImagePtr, int) -> None
    """Convert image data to desired format"""
    _ImageFormat(image, int(new_format))


def image_to_pot(image, fill):
    # type: (ImagePtr, Color) -> None
    """Convert image to POT (power-of-two)"""
    _ImageToPOT(image, _color(fill))


def image_crop(image, crop):
    # type: (ImagePtr, Rectangle) -> None
    """Crop an image to a defined rectangle"""
    _ImageCrop(image, _rect(crop))


def image_alpha_crop(image, threshold):
    # type: (ImagePtr, float) -> None
    """Crop image depending on alpha value"""
    _ImageAlphaCrop(image, float(threshold))


def image_alpha_clear(image, color, threshold):
    # type: (ImagePtr, Color, float) -> None
    """Clear alpha channel to desired color"""
    _ImageAlphaClear(image, _color(color), float(threshold))


def image_alpha_mask(image, alpha_mask):
    # type: (ImagePtr, Image) -> None
    """Apply alpha mask to image"""
    _ImageAlphaMask(image, alpha_mask)


def image_alpha_premultiply(image):
    # type: (ImagePtr) -> None
    """Premultiply alpha channel"""
    _ImageAlphaPremultiply(image)


def image_resize(image, new_width, new_height):
    # type: (ImagePtr, int, int) -> None
    """Resize image (Bicubic scaling algorithm)"""
    _ImageResize(image, int(new_width), int(new_height))


def image_resize_nn(image, new_width, new_height):
    # type: (ImagePtr, int, int) -> None
    """Resize image (Nearest-Neighbor scaling algorithm)"""
    _ImageResizeNN(image, int(new_width), int(new_height))


def image_resize_canvas(image, new_width, new_height, offset_x, offset_y, fill):
    # type: (ImagePtr, int, int, int, int, Color) -> None
    """Resize canvas and fill with color"""
    _ImageResizeCanvas(image, int(new_width), int(new_height), int(offset_x), int(offset_y), _color(fill))


def image_mipmaps(image):
    # type: (ImagePtr) -> None
    """Compute all mipmap levels for a provided image"""
    _ImageMipmaps(image)


def image_dither(image, r_bpp, g_bpp, b_bpp, a_bpp):
    # type: (ImagePtr, int, int, int, int) -> None
    """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
    _ImageDither(image, int(r_bpp), int(g_bpp), int(b_bpp), int(a_bpp))


def image_flip_vertical(image):
    # type: (ImagePtr) -> None
    """Flip image vertically"""
    _ImageFlipVertical(image)


def image_flip_horizontal(image):
    # type: (ImagePtr) -> None
    """Flip image horizontally"""
    _ImageFlipHorizontal(image)


def image_rotate_cw(image):
    # type: (ImagePtr) -> None
    """Rotate image clockwise 90deg"""
    _ImageRotateCW(image)


def image_rotate_ccw(image):
    # type: (ImagePtr) -> None
    """Rotate image counter-clockwise 90deg"""
    _ImageRotateCCW(image)


def image_color_tint(image, color):
    # type: (ImagePtr, Color) -> None
    """Modify image color: tint"""
    _ImageColorTint(image, _color(color))


def image_color_invert(image):
    # type: (ImagePtr) -> None
    """Modify image color: invert"""
    _ImageColorInvert(image)


def image_color_grayscale(image):
    # type: (ImagePtr) -> None
    """Modify image color: grayscale"""
    _ImageColorGrayscale(image)


def image_color_contrast(image, contrast):
    # type: (ImagePtr, float) -> None
    """Modify image color: contrast (-100 to 100)"""
    _ImageColorContrast(image, float(contrast))


def image_color_brightness(image, brightness):
    # type: (ImagePtr, int) -> None
    """Modify image color: brightness (-255 to 255)"""
    _ImageColorBrightness(image, int(brightness))


def image_color_replace(image, color, replace):
    # type: (ImagePtr, Color, Color) -> None
    """Modify image color: replace color"""
    _ImageColorReplace(image, _color(color), _color(replace))


def load_image_colors(image):
    # type: (Image) -> ColorPtr
    """Load color data from image as a Color array (RGBA - 32bit)"""
    result = _ptr_out(_LoadImageColors(image))
    return result


def load_image_palette(image, max_palette_size):
    # type: (Image, int) -> ColorPtr
    """Load colors palette from image as a Color array (RGBA - 32bit)"""
    color_count = Int(0)
    result = _ptr_out(_LoadImagePalette(image, int(max_palette_size), byref(color_count)), color_count.value)
    return result


def unload_image_colors(colors):
    # type: (ColorPtr) -> None
    """Unload color data loaded with LoadImageColors()"""
    _UnloadImageColors(_color(colors))


def unload_image_palette(colors):
    # type: (ColorPtr) -> None
    """Unload colors palette loaded with LoadImagePalette()"""
    _UnloadImagePalette(_color(colors))


def get_image_alpha_border(image, threshold):
    # type: (Image, float) -> Rectangle
    """Get image alpha border rectangle"""
    result = _GetImageAlphaBorder(image, float(threshold))
    return result


def get_image_color(image, x, y):
    # type: (Image, int, int) -> Color
    """Get image pixel color at (x, y) position"""
    result = _GetImageColor(image, int(x), int(y))
    return result


def image_clear_background(dst, color):
    # type: (ImagePtr, Color) -> None
    """Clear image background with given color"""
    _ImageClearBackground(dst, _color(color))


def image_draw_pixel(dst, pos_x, pos_y, color):
    # type: (ImagePtr, int, int, Color) -> None
    """Draw pixel within an image"""
    _ImageDrawPixel(dst, int(pos_x), int(pos_y), _color(color))


def image_draw_pixel_v(dst, position, color):
    # type: (ImagePtr, Vector2, Color) -> None
    """Draw pixel within an image (Vector version)"""
    _ImageDrawPixelV(dst, _vec2(position), _color(color))


def image_draw_line(dst, start_pos_x, start_pos_y, end_pos_x, end_pos_y, color):
    # type: (ImagePtr, int, int, int, int, Color) -> None
    """Draw line within an image"""
    _ImageDrawLine(dst, int(start_pos_x), int(start_pos_y), int(end_pos_x), int(end_pos_y), _color(color))


def image_draw_line_v(dst, start, end, color):
    # type: (ImagePtr, Vector2, Vector2, Color) -> None
    """Draw line within an image (Vector version)"""
    _ImageDrawLineV(dst, _vec2(start), _vec2(end), _color(color))


def image_draw_circle(dst, center_x, center_y, radius, color):
    # type: (ImagePtr, int, int, int, Color) -> None
    """Draw circle within an image"""
    _ImageDrawCircle(dst, int(center_x), int(center_y), int(radius), _color(color))


def image_draw_circle_v(dst, center, radius, color):
    # type: (ImagePtr, Vector2, int, Color) -> None
    """Draw circle within an image (Vector version)"""
    _ImageDrawCircleV(dst, _vec2(center), int(radius), _color(color))


def image_draw_rectangle(dst, pos_x, pos_y, width, height, color):
    # type: (ImagePtr, int, int, int, int, Color) -> None
    """Draw rectangle within an image"""
    _ImageDrawRectangle(dst, int(pos_x), int(pos_y), int(width), int(height), _color(color))


def image_draw_rectangle_v(dst, position, size, color):
    # type: (ImagePtr, Vector2, Vector2, Color) -> None
    """Draw rectangle within an image (Vector version)"""
    _ImageDrawRectangleV(dst, _vec2(position), _vec2(size), _color(color))


def image_draw_rectangle_rec(dst, rec, color):
    # type: (ImagePtr, Rectangle, Color) -> None
    """Draw rectangle within an image"""
    _ImageDrawRectangleRec(dst, _rect(rec), _color(color))


def image_draw_rectangle_lines(dst, rec, thick, color):
    # type: (ImagePtr, Rectangle, int, Color) -> None
    """Draw rectangle lines within an image"""
    _ImageDrawRectangleLines(dst, _rect(rec), int(thick), _color(color))


def image_draw(dst, src, src_rec, dst_rec, tint):
    # type: (ImagePtr, Image, Rectangle, Rectangle, Color) -> None
    """Draw a source image within a destination image (tint applied to source)"""
    _ImageDraw(dst, src, _rect(src_rec), _rect(dst_rec), _color(tint))


def image_draw_text(dst, text, pos_x, pos_y, font_size, color):
    # type: (ImagePtr, Union[str, CharPtr], int, int, int, Color) -> None
    """Draw text (using default font) within an image (destination)"""
    _ImageDrawText(dst, _str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))


def image_draw_text_ex(dst, font, text, position, font_size, spacing, tint):
    # type: (ImagePtr, Font, Union[str, CharPtr], Vector2, float, float, Color) -> None
    """Draw text (custom sprite font) within an image (destination)"""
    _ImageDrawTextEx(dst, font, _str_in(text), _vec2(position), float(font_size), float(spacing), _color(tint))


def load_texture(file_name):
    # type: (Union[str, CharPtr]) -> Texture2D
    """Load texture from file into GPU memory (VRAM)"""
    result = _LoadTexture(_str_in(file_name))
    return result


def load_texture_from_image(image):
    # type: (Image) -> Texture2D
    """Load texture from image data"""
    result = _LoadTextureFromImage(image)
    return result


def load_texture_cubemap(image, layout):
    # type: (Image, int) -> TextureCubemap
    """Load cubemap from image, multiple image cubemap layouts supported"""
    result = _LoadTextureCubemap(image, int(layout))
    return result


def load_render_texture(width, height):
    # type: (int, int) -> RenderTexture2D
    """Load texture for rendering (framebuffer)"""
    result = _LoadRenderTexture(int(width), int(height))
    return result


def unload_texture(texture):
    # type: (Texture2D) -> None
    """Unload texture from GPU memory (VRAM)"""
    _UnloadTexture(texture)


def unload_render_texture(target):
    # type: (RenderTexture2D) -> None
    """Unload render texture from GPU memory (VRAM)"""
    _UnloadRenderTexture(target)


def update_texture(texture, pixels):
    # type: (Texture2D, bytes) -> None
    """Update GPU texture with new data"""
    _UpdateTexture(texture, pixels)


def update_texture_rec(texture, rec, pixels):
    # type: (Texture2D, Rectangle, bytes) -> None
    """Update GPU texture rectangle with new data"""
    _UpdateTextureRec(texture, _rect(rec), pixels)


def gen_texture_mipmaps(texture):
    # type: (Texture2DPtr) -> None
    """Generate GPU mipmaps for a texture"""
    _GenTextureMipmaps(texture)


def set_texture_filter(texture, filter):
    # type: (Texture2D, int) -> None
    """Set texture scaling filter mode"""
    _SetTextureFilter(texture, int(filter))


def set_texture_wrap(texture, wrap):
    # type: (Texture2D, int) -> None
    """Set texture wrapping mode"""
    _SetTextureWrap(texture, int(wrap))


def draw_texture(texture, pos_x, pos_y, tint):
    # type: (Texture2D, int, int, Color) -> None
    """Draw a Texture2D"""
    _DrawTexture(texture, int(pos_x), int(pos_y), _color(tint))


def draw_texture_v(texture, position, tint):
    # type: (Texture2D, Vector2, Color) -> None
    """Draw a Texture2D with position defined as Vector2"""
    _DrawTextureV(texture, _vec2(position), _color(tint))


def draw_texture_ex(texture, position, rotation, scale, tint):
    # type: (Texture2D, Vector2, float, float, Color) -> None
    """Draw a Texture2D with extended parameters"""
    _DrawTextureEx(texture, _vec2(position), float(rotation), float(scale), _color(tint))


def draw_texture_rec(texture, source, position, tint):
    # type: (Texture2D, Rectangle, Vector2, Color) -> None
    """Draw a part of a texture defined by a rectangle"""
    _DrawTextureRec(texture, _rect(source), _vec2(position), _color(tint))


def draw_texture_quad(texture, tiling, offset, quad, tint):
    # type: (Texture2D, Vector2, Vector2, Rectangle, Color) -> None
    """Draw texture quad with tiling and offset parameters"""
    _DrawTextureQuad(texture, _vec2(tiling), _vec2(offset), _rect(quad), _color(tint))


def draw_texture_tiled(texture, source, dest, origin, rotation, scale, tint):
    # type: (Texture2D, Rectangle, Rectangle, Vector2, float, float, Color) -> None
    """Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest."""
    _DrawTextureTiled(texture, _rect(source), _rect(dest), _vec2(origin), float(rotation), float(scale), _color(tint))


def draw_texture_pro(texture, source, dest, origin, rotation, tint):
    # type: (Texture2D, Rectangle, Rectangle, Vector2, float, Color) -> None
    """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
    _DrawTexturePro(texture, _rect(source), _rect(dest), _vec2(origin), float(rotation), _color(tint))


def draw_texture_npatch(texture, n_patch_info, dest, origin, rotation, tint):
    # type: (Texture2D, NPatchInfo, Rectangle, Vector2, float, Color) -> None
    """Draws a texture (or part of it) that stretches or shrinks nicely"""
    _DrawTextureNPatch(texture, n_patch_info, _rect(dest), _vec2(origin), float(rotation), _color(tint))


def draw_texture_poly(texture, center, points, texcoords, tint):
    # type: (Texture2D, Vector2, Vector2Ptr, Vector2Ptr, Color) -> None
    """Draw a textured polygon"""
    _DrawTexturePoly(texture, _vec2(center), _arr_in(Vector2, points), _vec2(texcoords), len(points), _color(tint))


def fade(color, alpha):
    # type: (Color, float) -> Color
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
    result = _Fade(_color(color), float(alpha))
    return result


def color_to_int(color):
    # type: (Color) -> int
    """Get hexadecimal value for a Color"""
    result = _ColorToInt(_color(color))
    return result


def color_normalize(color):
    # type: (Color) -> Vector4
    """Get Color normalized as float [0..1]"""
    result = _ColorNormalize(_color(color))
    return result


def color_from_normalized(normalized):
    # type: (Vector4) -> Color
    """Get Color from normalized values [0..1]"""
    result = _ColorFromNormalized(_vec4(normalized))
    return result


def color_to_hsv(color):
    # type: (Color) -> Vector3
    """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
    result = _ColorToHSV(_color(color))
    return result


def color_from_hsv(hue, saturation, value):
    # type: (float, float, float) -> Color
    """Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
    result = _ColorFromHSV(float(hue), float(saturation), float(value))
    return result


def color_alpha(color, alpha):
    # type: (Color, float) -> Color
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
    result = _ColorAlpha(_color(color), float(alpha))
    return result


def color_alpha_blend(dst, src, tint):
    # type: (Color, Color, Color) -> Color
    """Get src alpha-blended into dst color with tint"""
    result = _ColorAlphaBlend(_color(dst), _color(src), _color(tint))
    return result


def get_color(hex_value):
    # type: (int) -> Color
    """Get Color structure from hexadecimal value"""
    result = _GetColor(hex_value)
    return result


def get_pixel_color(src_ptr, format):
    # type: (bytes, int) -> Color
    """Get Color from a source pixel pointer of certain format"""
    result = _GetPixelColor(src_ptr, int(format))
    return result


def set_pixel_color(dst_ptr, color, format):
    # type: (bytes, Color, int) -> None
    """Set color formatted into destination pixel pointer"""
    _SetPixelColor(dst_ptr, _color(color), int(format))


def get_pixel_data_size(width, height, format):
    # type: (int, int, int) -> int
    """Get pixel data size in bytes for certain format"""
    result = _GetPixelDataSize(int(width), int(height), int(format))
    return result


def get_font_default():
    # type: () -> Font
    """Get the default Font"""
    result = _GetFontDefault()
    return result


def load_font(file_name):
    # type: (Union[str, CharPtr]) -> Font
    """Load font from file into GPU memory (VRAM)"""
    result = _LoadFont(_str_in(file_name))
    return result


def load_font_ex(file_name, font_size, font_chars, glyph_count):
    # type: (Union[str, CharPtr], int, Union[Seq[int], IntPtr], int) -> Font
    """Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set"""
    result = _LoadFontEx(_str_in(file_name), int(font_size), font_chars, int(glyph_count))
    return result


def load_font_from_image(image, key, first_char):
    # type: (Image, Color, int) -> Font
    """Load font from Image (XNA style)"""
    result = _LoadFontFromImage(image, _color(key), int(first_char))
    return result


def load_font_from_memory(file_type, file_data, data_size, font_size, font_chars, glyph_count):
    # type: (Union[str, CharPtr], Union[Seq[int], UCharPtr], int, int, Union[Seq[int], IntPtr], int) -> Font
    """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
    result = _LoadFontFromMemory(_str_in(file_type), _str_in(file_data), int(data_size), int(font_size), font_chars, int(glyph_count))
    return result


def load_font_data(file_data, data_size, font_size, font_chars, glyph_count, type):
    # type: (Union[Seq[int], UCharPtr], int, int, Union[Seq[int], IntPtr], int, int) -> GlyphInfoPtr
    """Load font data for further use"""
    result = _ptr_out(_LoadFontData(_str_in(file_data), int(data_size), int(font_size), font_chars, int(glyph_count), int(type)))
    return result


def gen_image_font_atlas(chars, recs, glyph_count, font_size, padding, pack_method):
    # type: (GlyphInfoPtr, RectanglePtr, int, int, int, int) -> Image
    """Generate image font atlas using chars info"""
    result = _GenImageFontAtlas(chars, recs, int(glyph_count), int(font_size), int(padding), int(pack_method))
    return result


def unload_font_data(chars, glyph_count):
    # type: (GlyphInfoPtr, int) -> None
    """Unload font chars info data (RAM)"""
    _UnloadFontData(chars, int(glyph_count))


def unload_font(font):
    # type: (Font) -> None
    """Unload font from GPU memory (VRAM)"""
    _UnloadFont(font)


def export_font_as_code(font, file_name):
    # type: (Font, Union[str, CharPtr]) -> bool
    """Export font as code file, returns true on success"""
    result = _ExportFontAsCode(font, _str_in(file_name))
    return result


def draw_fps(pos_x, pos_y):
    # type: (int, int) -> None
    """Draw current FPS"""
    _DrawFPS(int(pos_x), int(pos_y))


def draw_text(text, pos_x, pos_y, font_size, color):
    # type: (Union[str, CharPtr], int, int, int, Color) -> None
    """Draw text (using default font)"""
    _DrawText(_str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))


def draw_text_ex(font, text, position, font_size, spacing, tint):
    # type: (Font, Union[str, CharPtr], Vector2, float, float, Color) -> None
    """Draw text using font and additional parameters"""
    _DrawTextEx(font, _str_in(text), _vec2(position), float(font_size), float(spacing), _color(tint))


def draw_text_pro(font, text, position, origin, rotation, font_size, spacing, tint):
    # type: (Font, Union[str, CharPtr], Vector2, Vector2, float, float, float, Color) -> None
    """Draw text using Font and pro parameters (rotation)"""
    _DrawTextPro(font, _str_in(text), _vec2(position), _vec2(origin), float(rotation), float(font_size), float(spacing), _color(tint))


def draw_text_codepoint(font, codepoint, position, font_size, tint):
    # type: (Font, int, Vector2, float, Color) -> None
    """Draw one character (codepoint)"""
    _DrawTextCodepoint(font, int(codepoint), _vec2(position), float(font_size), _color(tint))


def draw_text_codepoints(font, codepoints, position, font_size, spacing, tint):
    # type: (Font, Union[Seq[int], IntPtr], Vector2, float, float, Color) -> None
    """Draw multiple character (codepoint)"""
    _DrawTextCodepoints(font, _str_in(codepoints), len(codepoints), _vec2(position), float(font_size), float(spacing), _color(tint))


def measure_text(text, font_size):
    # type: (Union[str, CharPtr], int) -> int
    """Measure string width for default font"""
    result = _MeasureText(_str_in(text), int(font_size))
    return result


def measure_text_ex(font, text, font_size, spacing):
    # type: (Font, Union[str, CharPtr], float, float) -> Vector2
    """Measure string size for Font"""
    result = _MeasureTextEx(font, _str_in(text), float(font_size), float(spacing))
    return result


def get_glyph_index(font, codepoint):
    # type: (Font, int) -> int
    """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
    result = _GetGlyphIndex(font, int(codepoint))
    return result


def get_glyph_info(font, codepoint):
    # type: (Font, int) -> GlyphInfo
    """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
    result = _GetGlyphInfo(font, int(codepoint))
    return result


def get_glyph_atlas_rec(font, codepoint):
    # type: (Font, int) -> Rectangle
    """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
    result = _GetGlyphAtlasRec(font, int(codepoint))
    return result


def load_codepoints(text, count):
    # type: (Union[str, CharPtr], Union[Seq[int], IntPtr]) -> Union[Seq[int], IntPtr]
    """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
    result = _ptr_out(_LoadCodepoints(_str_in(text), count))
    return result


def unload_codepoints(codepoints):
    # type: (Union[Seq[int], IntPtr]) -> None
    """Unload codepoints data from memory"""
    _UnloadCodepoints(codepoints)


def get_codepoint_count(text):
    # type: (Union[str, CharPtr]) -> int
    """Get total number of codepoints in a UTF-8 encoded string"""
    result = _GetCodepointCount(_str_in(text))
    return result


def get_codepoint(text, bytes_processed):
    # type: (Union[str, CharPtr], Union[Seq[int], IntPtr]) -> int
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
    result = _GetCodepoint(_str_in(text), bytes_processed)
    return result


def codepoint_to_utf8(codepoint, byte_size):
    # type: (int, Union[Seq[int], IntPtr]) -> Union[str, CharPtr]
    """Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
    result = _ptr_out(_CodepointToUTF8(int(codepoint), byte_size))
    return result


def text_codepoints_to_utf8(codepoints, length):
    # type: (Union[Seq[int], IntPtr], int) -> Union[str, CharPtr]
    """Encode text as codepoints array into UTF-8 text string (WARNING: memory must be freed!)"""
    result = _ptr_out(_TextCodepointsToUTF8(codepoints, int(length)))
    return result


def text_copy(dst, src):
    # type: (Union[str, CharPtr], Union[str, CharPtr]) -> int
    """Copy one string to another, returns bytes copied"""
    result = _TextCopy(_str_in(dst), _str_in(src))
    return result


def text_is_equal(text1, text2):
    # type: (Union[str, CharPtr], Union[str, CharPtr]) -> bool
    """Check if two text string are equal"""
    result = _TextIsEqual(_str_in(text1), _str_in(text2))
    return result


def text_length(text):
    # type: (Union[str, CharPtr]) -> int
    """Get text length, checks for '\0' ending"""
    result = _TextLength(_str_in(text))
    return result


def text_format(text, args):
    # type: (Union[str, CharPtr], bytes) -> Union[str, CharPtr]
    """Text formatting with variables (sprintf() style)"""
    result = _ptr_out(_TextFormat(_str_in(text), args))
    return result


def text_subtext(text, position, length):
    # type: (Union[str, CharPtr], int, int) -> Union[str, CharPtr]
    """Get a piece of a text string"""
    result = _ptr_out(_TextSubtext(_str_in(text), int(position), int(length)))
    return result


def text_replace(text, replace, by):
    # type: (Union[str, CharPtr], Union[str, CharPtr], Union[str, CharPtr]) -> Union[str, CharPtr]
    """Replace text string (WARNING: memory must be freed!)"""
    result = _ptr_out(_TextReplace(_str_in(text), _str_in(replace), _str_in(by)))
    return result


def text_insert(text, insert, position):
    # type: (Union[str, CharPtr], Union[str, CharPtr], int) -> Union[str, CharPtr]
    """Insert text in a position (WARNING: memory must be freed!)"""
    result = _ptr_out(_TextInsert(_str_in(text), _str_in(insert), int(position)))
    return result


def text_join(text_list, count, delimiter):
    # type: (Seq[Union[str, CharPtr]], int, Union[str, CharPtr]) -> Union[str, CharPtr]
    """Join text strings with delimiter"""
    result = _ptr_out(_TextJoin(str_in2(text_list), int(count), _str_in(delimiter)))
    return result


def text_split(text, delimiter, count):
    # type: (Union[str, CharPtr], int, Union[Seq[int], IntPtr]) -> Seq[Union[str, CharPtr]]
    """Split text into multiple strings"""
    result = _ptr_out(_TextSplit(_str_in(text), int(delimiter), count))
    return result


def text_append(text, append, position):
    # type: (Union[str, CharPtr], Union[str, CharPtr], Union[Seq[int], IntPtr]) -> None
    """Append text at specific position and move cursor!"""
    _TextAppend(_str_in(text), _str_in(append), position)


def text_find_index(text, find):
    # type: (Union[str, CharPtr], Union[str, CharPtr]) -> int
    """Find first text occurrence within a string"""
    result = _TextFindIndex(_str_in(text), _str_in(find))
    return result


def text_to_upper(text):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Get upper case version of provided string"""
    result = _ptr_out(_TextToUpper(_str_in(text)))
    return result


def text_to_lower(text):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Get lower case version of provided string"""
    result = _ptr_out(_TextToLower(_str_in(text)))
    return result


def text_to_pascal(text):
    # type: (Union[str, CharPtr]) -> Union[str, CharPtr]
    """Get Pascal case notation version of provided string"""
    result = _ptr_out(_TextToPascal(_str_in(text)))
    return result


def text_to_integer(text):
    # type: (Union[str, CharPtr]) -> int
    """Get integer value from text (negative values not supported)"""
    result = _TextToInteger(_str_in(text))
    return result


def draw_line3d(start_pos, end_pos, color):
    # type: (Vector3, Vector3, Color) -> None
    """Draw a line in 3D world space"""
    _DrawLine3D(_vec3(start_pos), _vec3(end_pos), _color(color))


def draw_point3d(position, color):
    # type: (Vector3, Color) -> None
    """Draw a point in 3D space, actually a small line"""
    _DrawPoint3D(_vec3(position), _color(color))


def draw_circle3d(center, radius, rotation_axis, rotation_angle, color):
    # type: (Vector3, float, Vector3, float, Color) -> None
    """Draw a circle in 3D world space"""
    _DrawCircle3D(_vec3(center), float(radius), _vec3(rotation_axis), float(rotation_angle), _color(color))


def draw_triangle3d(v1, v2, v3, color):
    # type: (Vector3, Vector3, Vector3, Color) -> None
    """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
    _DrawTriangle3D(_vec3(v1), _vec3(v2), _vec3(v3), _color(color))


def draw_triangle_strip3d(points, color):
    # type: (Vector3Ptr, Color) -> None
    """Draw a triangle strip defined by points"""
    _DrawTriangleStrip3D(_arr_in(Vector3, points), len(points), _color(color))


def draw_cube(position, width, height, length, color):
    # type: (Vector3, float, float, float, Color) -> None
    """Draw cube"""
    _DrawCube(_vec3(position), float(width), float(height), float(length), _color(color))


def draw_cube_v(position, size, color):
    # type: (Vector3, Vector3, Color) -> None
    """Draw cube (Vector version)"""
    _DrawCubeV(_vec3(position), _vec3(size), _color(color))


def draw_cube_wires(position, width, height, length, color):
    # type: (Vector3, float, float, float, Color) -> None
    """Draw cube wires"""
    _DrawCubeWires(_vec3(position), float(width), float(height), float(length), _color(color))


def draw_cube_wires_v(position, size, color):
    # type: (Vector3, Vector3, Color) -> None
    """Draw cube wires (Vector version)"""
    _DrawCubeWiresV(_vec3(position), _vec3(size), _color(color))


def draw_cube_texture(texture, position, width, height, length, color):
    # type: (Texture2D, Vector3, float, float, float, Color) -> None
    """Draw cube textured"""
    _DrawCubeTexture(texture, _vec3(position), float(width), float(height), float(length), _color(color))


def draw_cube_texture_rec(texture, source, position, width, height, length, color):
    # type: (Texture2D, Rectangle, Vector3, float, float, float, Color) -> None
    """Draw cube with a region of a texture"""
    _DrawCubeTextureRec(texture, _rect(source), _vec3(position), float(width), float(height), float(length), _color(color))


def draw_sphere(center_pos, radius, color):
    # type: (Vector3, float, Color) -> None
    """Draw sphere"""
    _DrawSphere(_vec3(center_pos), float(radius), _color(color))


def draw_sphere_ex(center_pos, radius, rings, slices, color):
    # type: (Vector3, float, int, int, Color) -> None
    """Draw sphere with extended parameters"""
    _DrawSphereEx(_vec3(center_pos), float(radius), int(rings), int(slices), _color(color))


def draw_sphere_wires(center_pos, radius, rings, slices, color):
    # type: (Vector3, float, int, int, Color) -> None
    """Draw sphere wires"""
    _DrawSphereWires(_vec3(center_pos), float(radius), int(rings), int(slices), _color(color))


def draw_cylinder(position, radius_top, radius_bottom, height, slices, color):
    # type: (Vector3, float, float, float, int, Color) -> None
    """Draw a cylinder/cone"""
    _DrawCylinder(_vec3(position), float(radius_top), float(radius_bottom), float(height), int(slices), _color(color))


def draw_cylinder_ex(start_pos, end_pos, start_radius, end_radius, sides, color):
    # type: (Vector3, Vector3, float, float, int, Color) -> None
    """Draw a cylinder with base at startPos and top at endPos"""
    _DrawCylinderEx(_vec3(start_pos), _vec3(end_pos), float(start_radius), float(end_radius), int(sides), _color(color))


def draw_cylinder_wires(position, radius_top, radius_bottom, height, slices, color):
    # type: (Vector3, float, float, float, int, Color) -> None
    """Draw a cylinder/cone wires"""
    _DrawCylinderWires(_vec3(position), float(radius_top), float(radius_bottom), float(height), int(slices), _color(color))


def draw_cylinder_wires_ex(start_pos, end_pos, start_radius, end_radius, sides, color):
    # type: (Vector3, Vector3, float, float, int, Color) -> None
    """Draw a cylinder wires with base at startPos and top at endPos"""
    _DrawCylinderWiresEx(_vec3(start_pos), _vec3(end_pos), float(start_radius), float(end_radius), int(sides), _color(color))


def draw_plane(center_pos, size, color):
    # type: (Vector3, Vector2, Color) -> None
    """Draw a plane XZ"""
    _DrawPlane(_vec3(center_pos), _vec2(size), _color(color))


def draw_ray(ray, color):
    # type: (Ray, Color) -> None
    """Draw a ray line"""
    _DrawRay(ray, _color(color))


def draw_grid(slices, spacing):
    # type: (int, float) -> None
    """Draw a grid (centered at (0, 0, 0))"""
    _DrawGrid(int(slices), float(spacing))


def load_model(file_name):
    # type: (Union[str, CharPtr]) -> Model
    """Load model from files (meshes and materials)"""
    result = _LoadModel(_str_in(file_name))
    return result


def load_model_from_mesh(mesh):
    # type: (Mesh) -> Model
    """Load model from generated mesh (default material)"""
    result = _LoadModelFromMesh(mesh)
    return result


def unload_model(model):
    # type: (Model) -> None
    """Unload model (including meshes) from memory (RAM and/or VRAM)"""
    _UnloadModel(model)


def unload_model_keep_meshes(model):
    # type: (Model) -> None
    """Unload model (but not meshes) from memory (RAM and/or VRAM)"""
    _UnloadModelKeepMeshes(model)


def get_model_bounding_box(model):
    # type: (Model) -> BoundingBox
    """Compute model bounding box limits (considers all meshes)"""
    result = _GetModelBoundingBox(model)
    return result


def draw_model(model, position, scale, tint):
    # type: (Model, Vector3, float, Color) -> None
    """Draw a model (with texture if set)"""
    _DrawModel(model, _vec3(position), float(scale), _color(tint))


def draw_model_ex(model, position, rotation_axis, rotation_angle, scale, tint):
    # type: (Model, Vector3, Vector3, float, Vector3, Color) -> None
    """Draw a model with extended parameters"""
    _DrawModelEx(model, _vec3(position), _vec3(rotation_axis), float(rotation_angle), _vec3(scale), _color(tint))


def draw_model_wires(model, position, scale, tint):
    # type: (Model, Vector3, float, Color) -> None
    """Draw a model wires (with texture if set)"""
    _DrawModelWires(model, _vec3(position), float(scale), _color(tint))


def draw_model_wires_ex(model, position, rotation_axis, rotation_angle, scale, tint):
    # type: (Model, Vector3, Vector3, float, Vector3, Color) -> None
    """Draw a model wires (with texture if set) with extended parameters"""
    _DrawModelWiresEx(model, _vec3(position), _vec3(rotation_axis), float(rotation_angle), _vec3(scale), _color(tint))


def draw_bounding_box(box, color):
    # type: (BoundingBox, Color) -> None
    """Draw bounding box (wires)"""
    _DrawBoundingBox(box, _color(color))


def draw_billboard(camera, texture, position, size, tint):
    # type: (Camera, Texture2D, Vector3, float, Color) -> None
    """Draw a billboard texture"""
    _DrawBillboard(camera, texture, _vec3(position), float(size), _color(tint))


def draw_billboard_rec(camera, texture, source, position, size, tint):
    # type: (Camera, Texture2D, Rectangle, Vector3, Vector2, Color) -> None
    """Draw a billboard texture defined by source"""
    _DrawBillboardRec(camera, texture, _rect(source), _vec3(position), _vec2(size), _color(tint))


def draw_billboard_pro(camera, texture, source, position, up, size, origin, rotation, tint):
    # type: (Camera, Texture2D, Rectangle, Vector3, Vector3, Vector2, Vector2, float, Color) -> None
    """Draw a billboard texture defined by source and rotation"""
    _DrawBillboardPro(camera, texture, _rect(source), _vec3(position), _vec3(up), _vec2(size), _vec2(origin), float(rotation), _color(tint))


def upload_mesh(mesh, dynamic):
    # type: (MeshPtr, bool) -> None
    """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
    _UploadMesh(mesh, bool(dynamic))


def update_mesh_buffer(mesh, index, data, data_size, offset):
    # type: (Mesh, int, bytes, int, int) -> None
    """Update mesh vertex data in GPU for a specific buffer index"""
    _UpdateMeshBuffer(mesh, int(index), data, int(data_size), int(offset))


def unload_mesh(mesh):
    # type: (Mesh) -> None
    """Unload mesh data from CPU and GPU"""
    _UnloadMesh(mesh)


def draw_mesh(mesh, material, transform):
    # type: (Mesh, Material, Matrix) -> None
    """Draw a 3d mesh with material and transform"""
    _DrawMesh(mesh, material, transform)


def draw_mesh_instanced(mesh, material, transforms, instances):
    # type: (Mesh, Material, MatrixPtr, int) -> None
    """Draw multiple mesh instances with material and different transforms"""
    _DrawMeshInstanced(mesh, material, transforms, int(instances))


def export_mesh(mesh, file_name):
    # type: (Mesh, Union[str, CharPtr]) -> bool
    """Export mesh data to file, returns true on success"""
    result = _ExportMesh(mesh, _str_in(file_name))
    return result


def get_mesh_bounding_box(mesh):
    # type: (Mesh) -> BoundingBox
    """Compute mesh bounding box limits"""
    result = _GetMeshBoundingBox(mesh)
    return result


def gen_mesh_tangents(mesh):
    # type: (MeshPtr) -> None
    """Compute mesh tangents"""
    _GenMeshTangents(mesh)


def gen_mesh_poly(sides, radius):
    # type: (int, float) -> Mesh
    """Generate polygonal mesh"""
    result = _GenMeshPoly(int(sides), float(radius))
    return result


def gen_mesh_plane(width, length, res_x, res_z):
    # type: (float, float, int, int) -> Mesh
    """Generate plane mesh (with subdivisions)"""
    result = _GenMeshPlane(float(width), float(length), int(res_x), int(res_z))
    return result


def gen_mesh_cube(width, height, length):
    # type: (float, float, float) -> Mesh
    """Generate cuboid mesh"""
    result = _GenMeshCube(float(width), float(height), float(length))
    return result


def gen_mesh_sphere(radius, rings, slices):
    # type: (float, int, int) -> Mesh
    """Generate sphere mesh (standard sphere)"""
    result = _GenMeshSphere(float(radius), int(rings), int(slices))
    return result


def gen_mesh_hemi_sphere(radius, rings, slices):
    # type: (float, int, int) -> Mesh
    """Generate half-sphere mesh (no bottom cap)"""
    result = _GenMeshHemiSphere(float(radius), int(rings), int(slices))
    return result


def gen_mesh_cylinder(radius, height, slices):
    # type: (float, float, int) -> Mesh
    """Generate cylinder mesh"""
    result = _GenMeshCylinder(float(radius), float(height), int(slices))
    return result


def gen_mesh_cone(radius, height, slices):
    # type: (float, float, int) -> Mesh
    """Generate cone/pyramid mesh"""
    result = _GenMeshCone(float(radius), float(height), int(slices))
    return result


def gen_mesh_torus(radius, size, rad_seg, sides):
    # type: (float, float, int, int) -> Mesh
    """Generate torus mesh"""
    result = _GenMeshTorus(float(radius), float(size), int(rad_seg), int(sides))
    return result


def gen_mesh_knot(radius, size, rad_seg, sides):
    # type: (float, float, int, int) -> Mesh
    """Generate trefoil knot mesh"""
    result = _GenMeshKnot(float(radius), float(size), int(rad_seg), int(sides))
    return result


def gen_mesh_heightmap(heightmap, size):
    # type: (Image, Vector3) -> Mesh
    """Generate heightmap mesh from image data"""
    result = _GenMeshHeightmap(heightmap, _vec3(size))
    return result


def gen_mesh_cubicmap(cubicmap, cube_size):
    # type: (Image, Vector3) -> Mesh
    """Generate cubes-based map mesh from image data"""
    result = _GenMeshCubicmap(cubicmap, _vec3(cube_size))
    return result


def load_materials(file_name):
    # type: (Union[str, CharPtr]) -> MaterialPtr
    """Load materials from model file"""
    material_count = Int(0)
    result = _ptr_out(_LoadMaterials(_str_in(file_name), byref(material_count)), material_count.value)
    return result


def load_material_default():
    # type: () -> Material
    """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
    result = _LoadMaterialDefault()
    return result


def unload_material(material):
    # type: (Material) -> None
    """Unload material from GPU memory (VRAM)"""
    _UnloadMaterial(material)


def set_material_texture(material, map_type, texture):
    # type: (MaterialPtr, int, Texture2D) -> None
    """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
    _SetMaterialTexture(material, int(map_type), texture)


def set_model_mesh_material(model, mesh_id, material_id):
    # type: (ModelPtr, int, int) -> None
    """Set material for a mesh"""
    _SetModelMeshMaterial(model, int(mesh_id), int(material_id))


def load_model_animations(file_name):
    # type: (Union[str, CharPtr]) -> ModelAnimationPtr
    """Load model animations from file"""
    anim_count = UInt(0)
    result = _ptr_out(_LoadModelAnimations(_str_in(file_name), byref(anim_count)), anim_count.value)
    return result


def update_model_animation(model, anim, frame):
    # type: (Model, ModelAnimation, int) -> None
    """Update model animation pose"""
    _UpdateModelAnimation(model, anim, int(frame))


def unload_model_animation(anim):
    # type: (ModelAnimation) -> None
    """Unload animation data"""
    _UnloadModelAnimation(anim)


def unload_model_animations(animations, count):
    # type: (ModelAnimationPtr, int) -> None
    """Unload animation array data"""
    _UnloadModelAnimations(animations, count)


def is_model_animation_valid(model, anim):
    # type: (Model, ModelAnimation) -> bool
    """Check model animation skeleton match"""
    result = _IsModelAnimationValid(model, anim)
    return result


def check_collision_spheres(center1, radius1, center2, radius2):
    # type: (Vector3, float, Vector3, float) -> bool
    """Check collision between two spheres"""
    result = _CheckCollisionSpheres(_vec3(center1), float(radius1), _vec3(center2), float(radius2))
    return result


def check_collision_boxes(box1, box2):
    # type: (BoundingBox, BoundingBox) -> bool
    """Check collision between two bounding boxes"""
    result = _CheckCollisionBoxes(box1, box2)
    return result


def check_collision_box_sphere(box, center, radius):
    # type: (BoundingBox, Vector3, float) -> bool
    """Check collision between box and sphere"""
    result = _CheckCollisionBoxSphere(box, _vec3(center), float(radius))
    return result


def get_ray_collision_sphere(ray, center, radius):
    # type: (Ray, Vector3, float) -> RayCollision
    """Get collision info between ray and sphere"""
    result = _GetRayCollisionSphere(ray, _vec3(center), float(radius))
    return result


def get_ray_collision_box(ray, box):
    # type: (Ray, BoundingBox) -> RayCollision
    """Get collision info between ray and box"""
    result = _GetRayCollisionBox(ray, box)
    return result


def get_ray_collision_mesh(ray, mesh, transform):
    # type: (Ray, Mesh, Matrix) -> RayCollision
    """Get collision info between ray and mesh"""
    result = _GetRayCollisionMesh(ray, mesh, transform)
    return result


def get_ray_collision_triangle(ray, p1, p2, p3):
    # type: (Ray, Vector3, Vector3, Vector3) -> RayCollision
    """Get collision info between ray and triangle"""
    result = _GetRayCollisionTriangle(ray, _vec3(p1), _vec3(p2), _vec3(p3))
    return result


def get_ray_collision_quad(ray, p1, p2, p3, p4):
    # type: (Ray, Vector3, Vector3, Vector3, Vector3) -> RayCollision
    """Get collision info between ray and quad"""
    result = _GetRayCollisionQuad(ray, _vec3(p1), _vec3(p2), _vec3(p3), _vec3(p4))
    return result


def init_audio_device():
    # type: () -> None
    """Initialize audio device and context"""
    _InitAudioDevice()


def close_audio_device():
    # type: () -> None
    """Close the audio device and context"""
    _CloseAudioDevice()


def is_audio_device_ready():
    # type: () -> bool
    """Check if audio device has been initialized successfully"""
    result = _IsAudioDeviceReady()
    return result


def set_master_volume(volume):
    # type: (float) -> None
    """Set master volume (listener)"""
    _SetMasterVolume(float(volume))


def load_wave(file_name):
    # type: (Union[str, CharPtr]) -> Wave
    """Load wave data from file"""
    result = _LoadWave(_str_in(file_name))
    return result


def load_wave_from_memory(file_type, file_data, data_size):
    # type: (Union[str, CharPtr], Union[Seq[int], UCharPtr], int) -> Wave
    """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
    result = _LoadWaveFromMemory(_str_in(file_type), _str_in(file_data), int(data_size))
    return result


def load_sound(file_name):
    # type: (Union[str, CharPtr]) -> Sound
    """Load sound from file"""
    result = _LoadSound(_str_in(file_name))
    return result


def load_sound_from_wave(wave):
    # type: (Wave) -> Sound
    """Load sound from wave data"""
    result = _LoadSoundFromWave(wave)
    return result


def update_sound(sound, data, sample_count):
    # type: (Sound, bytes, int) -> None
    """Update sound buffer with new data"""
    _UpdateSound(sound, data, int(sample_count))


def unload_wave(wave):
    # type: (Wave) -> None
    """Unload wave data"""
    _UnloadWave(wave)


def unload_sound(sound):
    # type: (Sound) -> None
    """Unload sound"""
    _UnloadSound(sound)


def export_wave(wave, file_name):
    # type: (Wave, Union[str, CharPtr]) -> bool
    """Export wave data to file, returns true on success"""
    result = _ExportWave(wave, _str_in(file_name))
    return result


def export_wave_as_code(wave, file_name):
    # type: (Wave, Union[str, CharPtr]) -> bool
    """Export wave sample data to code (.h), returns true on success"""
    result = _ExportWaveAsCode(wave, _str_in(file_name))
    return result


def play_sound(sound):
    # type: (Sound) -> None
    """Play a sound"""
    _PlaySound(sound)


def stop_sound(sound):
    # type: (Sound) -> None
    """Stop playing a sound"""
    _StopSound(sound)


def pause_sound(sound):
    # type: (Sound) -> None
    """Pause a sound"""
    _PauseSound(sound)


def resume_sound(sound):
    # type: (Sound) -> None
    """Resume a paused sound"""
    _ResumeSound(sound)


def play_sound_multi(sound):
    # type: (Sound) -> None
    """Play a sound (using multichannel buffer pool)"""
    _PlaySoundMulti(sound)


def stop_sound_multi():
    # type: () -> None
    """Stop any sound playing (using multichannel buffer pool)"""
    _StopSoundMulti()


def get_sounds_playing():
    # type: () -> int
    """Get number of sounds playing in the multichannel"""
    result = _GetSoundsPlaying()
    return result


def is_sound_playing(sound):
    # type: (Sound) -> bool
    """Check if a sound is currently playing"""
    result = _IsSoundPlaying(sound)
    return result


def set_sound_volume(sound, volume):
    # type: (Sound, float) -> None
    """Set volume for a sound (1.0 is max level)"""
    _SetSoundVolume(sound, float(volume))


def set_sound_pitch(sound, pitch):
    # type: (Sound, float) -> None
    """Set pitch for a sound (1.0 is base level)"""
    _SetSoundPitch(sound, float(pitch))


def set_sound_pan(sound, pan):
    # type: (Sound, float) -> None
    """Set pan for a sound (0.5 is center)"""
    _SetSoundPan(sound, float(pan))


def wave_copy(wave):
    # type: (Wave) -> Wave
    """Copy a wave to a new wave"""
    result = _WaveCopy(wave)
    return result


def wave_crop(wave, init_sample, final_sample):
    # type: (WavePtr, int, int) -> None
    """Crop a wave to defined samples range"""
    _WaveCrop(wave, int(init_sample), int(final_sample))


def wave_format(wave, sample_rate, sample_size, channels):
    # type: (WavePtr, int, int, int) -> None
    """Convert wave data to desired format"""
    _WaveFormat(wave, int(sample_rate), int(sample_size), int(channels))


def load_wave_samples(wave):
    # type: (Wave) -> Union[Seq[float], FloatPtr]
    """Load samples data from wave as a 32bit float data array"""
    result = _ptr_out(_LoadWaveSamples(wave))
    return result


def unload_wave_samples(samples):
    # type: (Union[Seq[float], FloatPtr]) -> None
    """Unload samples data loaded with LoadWaveSamples()"""
    _UnloadWaveSamples(samples)


def load_music_stream(file_name):
    # type: (Union[str, CharPtr]) -> Music
    """Load music stream from file"""
    result = _LoadMusicStream(_str_in(file_name))
    return result


def load_music_stream_from_memory(file_type, data, data_size):
    # type: (Union[str, CharPtr], Union[Seq[int], UCharPtr], int) -> Music
    """Load music stream from data"""
    result = _LoadMusicStreamFromMemory(_str_in(file_type), _str_in(data), int(data_size))
    return result


def unload_music_stream(music):
    # type: (Music) -> None
    """Unload music stream"""
    _UnloadMusicStream(music)


def play_music_stream(music):
    # type: (Music) -> None
    """Start music playing"""
    _PlayMusicStream(music)


def is_music_stream_playing(music):
    # type: (Music) -> bool
    """Check if music is playing"""
    result = _IsMusicStreamPlaying(music)
    return result


def update_music_stream(music):
    # type: (Music) -> None
    """Updates buffers for music streaming"""
    _UpdateMusicStream(music)


def stop_music_stream(music):
    # type: (Music) -> None
    """Stop music playing"""
    _StopMusicStream(music)


def pause_music_stream(music):
    # type: (Music) -> None
    """Pause music playing"""
    _PauseMusicStream(music)


def resume_music_stream(music):
    # type: (Music) -> None
    """Resume playing paused music"""
    _ResumeMusicStream(music)


def seek_music_stream(music, position):
    # type: (Music, float) -> None
    """Seek music to a position (in seconds)"""
    _SeekMusicStream(music, float(position))


def set_music_volume(music, volume):
    # type: (Music, float) -> None
    """Set volume for music (1.0 is max level)"""
    _SetMusicVolume(music, float(volume))


def set_music_pitch(music, pitch):
    # type: (Music, float) -> None
    """Set pitch for a music (1.0 is base level)"""
    _SetMusicPitch(music, float(pitch))


def set_music_pan(music, pan):
    # type: (Music, float) -> None
    """Set pan for a music (0.5 is center)"""
    _SetMusicPan(music, float(pan))


def get_music_time_length(music):
    # type: (Music) -> float
    """Get music time length (in seconds)"""
    result = _GetMusicTimeLength(music)
    return result


def get_music_time_played(music):
    # type: (Music) -> float
    """Get current music time played (in seconds)"""
    result = _GetMusicTimePlayed(music)
    return result


def load_audio_stream(sample_rate, sample_size, channels):
    # type: (int, int, int) -> AudioStream
    """Load audio stream (to stream raw audio pcm data)"""
    result = _LoadAudioStream(sample_rate, sample_size, channels)
    return result


def unload_audio_stream(stream):
    # type: (AudioStream) -> None
    """Unload audio stream and free memory"""
    _UnloadAudioStream(stream)


def update_audio_stream(stream, data, frame_count):
    # type: (AudioStream, bytes, int) -> None
    """Update audio stream buffers with data"""
    _UpdateAudioStream(stream, data, int(frame_count))


def is_audio_stream_processed(stream):
    # type: (AudioStream) -> bool
    """Check if any audio stream buffers requires refill"""
    result = _IsAudioStreamProcessed(stream)
    return result


def play_audio_stream(stream):
    # type: (AudioStream) -> None
    """Play audio stream"""
    _PlayAudioStream(stream)


def pause_audio_stream(stream):
    # type: (AudioStream) -> None
    """Pause audio stream"""
    _PauseAudioStream(stream)


def resume_audio_stream(stream):
    # type: (AudioStream) -> None
    """Resume audio stream"""
    _ResumeAudioStream(stream)


def is_audio_stream_playing(stream):
    # type: (AudioStream) -> bool
    """Check if audio stream is playing"""
    result = _IsAudioStreamPlaying(stream)
    return result


def stop_audio_stream(stream):
    # type: (AudioStream) -> None
    """Stop audio stream"""
    _StopAudioStream(stream)


def set_audio_stream_volume(stream, volume):
    # type: (AudioStream, float) -> None
    """Set volume for audio stream (1.0 is max level)"""
    _SetAudioStreamVolume(stream, float(volume))


def set_audio_stream_pitch(stream, pitch):
    # type: (AudioStream, float) -> None
    """Set pitch for audio stream (1.0 is base level)"""
    _SetAudioStreamPitch(stream, float(pitch))


def set_audio_stream_pan(stream, pan):
    # type: (AudioStream, float) -> None
    """Set pan for audio stream (0.5 is centered)"""
    _SetAudioStreamPan(stream, float(pan))


def set_audio_stream_buffer_size_default(size):
    # type: (int) -> None
    """Default size for new audio streams"""
    _SetAudioStreamBufferSizeDefault(int(size))


def set_audio_stream_callback(stream, callback):
    # type: (AudioStream, AudioCallback) -> None
    """Audio thread callback to request new data"""
    _SetAudioStreamCallback(stream, callback)


def attach_audio_stream_processor(stream, processor):
    # type: (AudioStream, AudioCallback) -> None
    """"""
    _AttachAudioStreamProcessor(stream, processor)


def detach_audio_stream_processor(stream, processor):
    # type: (AudioStream, AudioCallback) -> None
    """"""
    _DetachAudioStreamProcessor(stream, processor)


def clamp(value, min_, max_):
    # type: (float, float, float) -> float
    """Clamp float value"""
    result = _Clamp(float(value), float(min_), float(max_))
    return result


def lerp(start, end, amount):
    # type: (float, float, float) -> float
    """Calculate linear interpolation between two floats"""
    result = _Lerp(float(start), float(end), float(amount))
    return result


def normalize(value, start, end):
    # type: (float, float, float) -> float
    """Calculate linear interpolation between two floats"""
    result = _Normalize(float(value), float(start), float(end))
    return result


def remap(value, input_start, input_end, output_start, output_end):
    # type: (float, float, float, float, float) -> float
    """Remap input value within input range to output range"""
    result = _Remap(float(value), float(input_start), float(input_end), float(output_start), float(output_end))
    return result


def wrap(value, min_, max_):
    # type: (float, float, float) -> float
    """Wrap input value from min to max"""
    result = _Wrap(float(value), float(min_), float(max_))
    return result


def float_equals(x, y):
    # type: (float, float) -> int
    """Check whether two given floats are almost equal"""
    result = _FloatEquals(float(x), float(y))
    return result


def vector2zero():
    # type: () -> Vector2
    """Vector with components value 0.0f"""
    result = _Vector2Zero()
    return result


def vector2one():
    # type: () -> Vector2
    """Vector with components value 1.0f"""
    result = _Vector2One()
    return result


def vector2add(v1, v2):
    # type: (Vector2, Vector2) -> Vector2
    """Add two vectors (v1 + v2)"""
    result = _Vector2Add(_vec2(v1), _vec2(v2))
    return result


def vector2add_value(v, add):
    # type: (Vector2, float) -> Vector2
    """Add vector and float value"""
    result = _Vector2AddValue(_vec2(v), float(add))
    return result


def vector2subtract(v1, v2):
    # type: (Vector2, Vector2) -> Vector2
    """Subtract two vectors (v1 - v2)"""
    result = _Vector2Subtract(_vec2(v1), _vec2(v2))
    return result


def vector2subtract_value(v, sub):
    # type: (Vector2, float) -> Vector2
    """Subtract vector by float value"""
    result = _Vector2SubtractValue(_vec2(v), float(sub))
    return result


def vector2length(v):
    # type: (Vector2) -> float
    """Calculate vector length"""
    result = _Vector2Length(_vec2(v))
    return result


def vector2length_sqr(v):
    # type: (Vector2) -> float
    """Calculate vector square length"""
    result = _Vector2LengthSqr(_vec2(v))
    return result


def vector2dot_product(v1, v2):
    # type: (Vector2, Vector2) -> float
    """Calculate two vectors dot product"""
    result = _Vector2DotProduct(_vec2(v1), _vec2(v2))
    return result


def vector2distance(v1, v2):
    # type: (Vector2, Vector2) -> float
    """Calculate distance between two vectors"""
    result = _Vector2Distance(_vec2(v1), _vec2(v2))
    return result


def vector2distance_sqr(v1, v2):
    # type: (Vector2, Vector2) -> float
    """Calculate square distance between two vectors"""
    result = _Vector2DistanceSqr(_vec2(v1), _vec2(v2))
    return result


def vector2angle(v1, v2):
    # type: (Vector2, Vector2) -> float
    """Calculate angle from two vectors"""
    result = _Vector2Angle(_vec2(v1), _vec2(v2))
    return result


def vector2scale(v, scale):
    # type: (Vector2, float) -> Vector2
    """Scale vector (multiply by value)"""
    result = _Vector2Scale(_vec2(v), float(scale))
    return result


def vector2multiply(v1, v2):
    # type: (Vector2, Vector2) -> Vector2
    """Multiply vector by vector"""
    result = _Vector2Multiply(_vec2(v1), _vec2(v2))
    return result


def vector2negate(v):
    # type: (Vector2) -> Vector2
    """Negate vector"""
    result = _Vector2Negate(_vec2(v))
    return result


def vector2divide(v1, v2):
    # type: (Vector2, Vector2) -> Vector2
    """Divide vector by vector"""
    result = _Vector2Divide(_vec2(v1), _vec2(v2))
    return result


def vector2normalize(v):
    # type: (Vector2) -> Vector2
    """Normalize provided vector"""
    result = _Vector2Normalize(_vec2(v))
    return result


def vector2transform(v, mat):
    # type: (Vector2, Matrix) -> Vector2
    """Transforms a Vector2 by a given Matrix"""
    result = _Vector2Transform(_vec2(v), mat)
    return result


def vector2lerp(v1, v2, amount):
    # type: (Vector2, Vector2, float) -> Vector2
    """Calculate linear interpolation between two vectors"""
    result = _Vector2Lerp(_vec2(v1), _vec2(v2), float(amount))
    return result


def vector2reflect(v1, normal):
    # type: (Vector2, Vector2) -> Vector2
    """Calculate reflected vector to normal"""
    result = _Vector2Reflect(_vec2(v1), _vec2(normal))
    return result


def vector2rotate(v1, angle):
    # type: (Vector2, float) -> Vector2
    """Rotate vector by angle"""
    result = _Vector2Rotate(_vec2(v1), float(angle))
    return result


def vector2move_towards(v1, target, max_distance):
    # type: (Vector2, Vector2, float) -> Vector2
    """Move Vector towards target"""
    result = _Vector2MoveTowards(_vec2(v1), _vec2(target), float(max_distance))
    return result


def vector2invert(v):
    # type: (Vector2) -> Vector2
    """Invert the given vector"""
    result = _Vector2Invert(_vec2(v))
    return result


def vector2clamp(v, min_, max_):
    # type: (Vector2, Vector2, Vector2) -> Vector2
    """Clamp the components of the vector between min and max values specified by the given vectors"""
    result = _Vector2Clamp(_vec2(v), _vec2(min_), _vec2(max_))
    return result


def vector2clamp_value(v, min_, max_):
    # type: (Vector2, float, float) -> Vector2
    """Clamp the magnitude of the vector between two min and max values"""
    result = _Vector2ClampValue(_vec2(v), float(min_), float(max_))
    return result


def vector2equals(p, q):
    # type: (Vector2, Vector2) -> int
    """Check whether two given vectors are almost equal"""
    result = _Vector2Equals(_vec2(p), _vec2(q))
    return result


def vector3zero():
    # type: () -> Vector3
    """Vector with components value 0.0f"""
    result = _Vector3Zero()
    return result


def vector3one():
    # type: () -> Vector3
    """Vector with components value 1.0f"""
    result = _Vector3One()
    return result


def vector3add(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    """Add two vectors"""
    result = _Vector3Add(_vec3(v1), _vec3(v2))
    return result


def vector3add_value(v, add):
    # type: (Vector3, float) -> Vector3
    """Add vector and float value"""
    result = _Vector3AddValue(_vec3(v), float(add))
    return result


def vector3subtract(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    """Subtract two vectors"""
    result = _Vector3Subtract(_vec3(v1), _vec3(v2))
    return result


def vector3subtract_value(v, sub):
    # type: (Vector3, float) -> Vector3
    """Subtract vector and float value"""
    result = _Vector3SubtractValue(_vec3(v), float(sub))
    return result


def vector3scale(v, scalar):
    # type: (Vector3, float) -> Vector3
    """Multiply vector by scalar"""
    result = _Vector3Scale(_vec3(v), float(scalar))
    return result


def vector3multiply(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    """Multiply vector by vector"""
    result = _Vector3Multiply(_vec3(v1), _vec3(v2))
    return result


def vector3cross_product(v1, v2):
    # type: (Vector3, Vector3) -> float
    """Calculate two vectors cross product"""
    result = _Vector3CrossProduct(_vec3(v1), _vec3(v2))
    return result


def vector3perpendicular(v1):
    # type: (Vector3) -> Vector3
    """Calculate one vector perpendicular vector"""
    result = _Vector3Perpendicular(_vec3(v1))
    return result


def vector3length(v1):
    # type: (Vector3) -> float
    """Calculate vector length"""
    result = _Vector3Length(_vec3(v1))
    return result


def vector3length_sqr(v1):
    # type: (Vector3) -> float
    """Calculate vector square length"""
    result = _Vector3LengthSqr(_vec3(v1))
    return result


def vector3dot_product(v1, v2):
    # type: (Vector3, Vector3) -> float
    """Calculate two vectors dot product"""
    result = _Vector3DotProduct(_vec3(v1), _vec3(v2))
    return result


def vector3distance(v1, v2):
    # type: (Vector3, Vector3) -> float
    """Calculate distance between two vectors"""
    result = _Vector3Distance(_vec3(v1), _vec3(v2))
    return result


def vector3distance_sqr(v1, v2):
    # type: (Vector3, Vector3) -> float
    """Calculate square distance between two vectors"""
    result = _Vector3DistanceSqr(_vec3(v1), _vec3(v2))
    return result


def vector3angle(v1, v2):
    # type: (Vector3, Vector3) -> float
    """Calculate angle between two vectors"""
    result = _Vector3Angle(_vec3(v1), _vec3(v2))
    return result


def vector3negate(v):
    # type: (Vector3) -> Vector3
    """Negate provided vector (invert direction)"""
    result = _Vector3Negate(_vec3(v))
    return result


def vector3divide(v1, v2):
    # type: (Vector3, Vector3) -> float
    """Divide vector by vector"""
    result = _Vector3Divide(_vec3(v1), _vec3(v2))
    return result


def vector3normalize(v):
    # type: (Vector3) -> Vector3
    """Normalize provided vector"""
    result = _Vector3Normalize(_vec3(v))
    return result


def vector3ortho_normalize(v1, v2):
    # type: (Vector3Ptr, Vector3Ptr) -> Vector3
    """Makes vectors normalized and orthogonal to each other"""
    result = _Vector3OrthoNormalize(_vec3(v1), _vec3(v2))
    return result


def vector3transform(v, mat):
    # type: (Vector3, Matrix) -> Vector3
    """Transforms a Vector3 by a given Matrix"""
    result = _Vector3Transform(_vec3(v), mat)
    return result


def vector3rotate_by_quaternion(v, q):
    # type: (Vector3, Quaternion) -> Vector3
    """Transform a vector by quaternion rotation"""
    result = _Vector3RotateByQuaternion(_vec3(v), q)
    return result


def vector3rotate_by_axis_angle(v, axis, angle):
    # type: (Vector3, Vector3, float) -> Vector3
    """Rotates a vector around an axis"""
    result = _Vector3RotateByAxisAngle(_vec3(v), _vec3(axis), float(angle))
    return result


def vector3lerp(v1, v2, amount):
    # type: (Vector3, Vector3, float) -> Vector3
    """Calculate linear interpolation between two vectors"""
    result = _Vector3Lerp(_vec3(v1), _vec3(v2), float(amount))
    return result


def vector3reflect(v, normal):
    # type: (Vector3, Vector3) -> Vector3
    """Calculate reflected vector to normal"""
    result = _Vector3Reflect(_vec3(v), _vec3(normal))
    return result


def vector3min(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    """Get min value for each pair of components"""
    result = _Vector3Min(_vec3(v1), _vec3(v2))
    return result


def vector3max(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    """Get max value for each pair of components"""
    result = _Vector3Max(_vec3(v1), _vec3(v2))
    return result


def vector3barycenter(p, a, b, c):
    # type: (Vector3, Vector3, Vector3, Vector3) -> Vector3
    """Compute barycenter coordinates (u, v, w) for point p with respect to triangle (a, b, c). Assumes P is on the plane of the triangle"""
    result = _Vector3Barycenter(_vec3(p), _vec3(a), _vec3(b), _vec3(c))
    return result


def vector3unproject(source, projection, view):
    # type: (Vector3, Matrix, Matrix) -> Vector3
    """Projects a Vector3 from screen space into object space"""
    result = _Vector3Unproject(_vec3(source), projection, view)
    return result


def vector3to_float_v(v):
    # type: (Vector3) -> Seq[float]
    """Get Vector3 as float array"""
    result = _Vector3ToFloatV(_vec3(v))
    return result


def vector3invert(v):
    # type: (Vector3) -> Vector3
    """Invert the given vector"""
    result = _Vector3Invert(_vec3(v))
    return result


def vector3clamp(v, min_, max_):
    # type: (Vector3, Vector3, Vector3) -> Vector3
    """Clamp the components of the vector between min and max values specified by the given vectors"""
    result = _Vector3Clamp(_vec3(v), _vec3(min_), _vec3(max_))
    return result


def vector3clamp_value(v, min_, max_):
    # type: (Vector3, float, float) -> Vector3
    """Clamp the magnitude of the vector between two values"""
    result = _Vector3ClampValue(_vec3(v), float(min_), float(max_))
    return result


def vector3equals(v, min_, max_):
    # type: (Vector3, float, float) -> int
    """Check whether two given vectors are almost equal"""
    result = _Vector3Equals(_vec3(v), float(min_), float(max_))
    return result


def vector3refract(v, n, r):
    # type: (Vector3, Vector3, float) -> int
    """Compute the direction of a refracted ray where v specifies the normalized direction of the incoming ray, n specifies the normalized normal vector of the interface of two optical media, and r specifies the ratio of the refractive index of the medium from where the ray comes to the refractive index of the medium on the other side of the surface"""
    result = _Vector3Refract(_vec3(v), _vec3(n), float(r))
    return result


def matrix_determinant(mat):
    # type: (Matrix) -> float
    """Compute matrix determinant"""
    result = _MatrixDeterminant(mat)
    return result


def matrix_trace(mat):
    # type: (Matrix) -> float
    """Get the trace of the matrix (sum of the values along the diagonal)"""
    result = _MatrixTrace(mat)
    return result


def matrix_transpose(mat):
    # type: (Matrix) -> Matrix
    """Get the trace of the matrix (sum of the values along the diagonal)"""
    result = _MatrixTranspose(mat)
    return result


def matrix_invert(mat):
    # type: (Matrix) -> Matrix
    """Invert provided matrix"""
    result = _MatrixInvert(mat)
    return result


def matrix_identity():
    # type: () -> Matrix
    """Get identity matrix"""
    result = _MatrixIdentity()
    return result


def matrix_add(left, right):
    # type: (Matrix, Matrix) -> Matrix
    """Add two matrices"""
    result = _MatrixAdd(left, right)
    return result


def matrix_subtract(left, right):
    # type: (Matrix, Matrix) -> Matrix
    """Subtract two matrices (left - right)"""
    result = _MatrixSubtract(left, right)
    return result


def matrix_multiply(left, right):
    # type: (Matrix, Matrix) -> Matrix
    """Get two matrix multiplication. When multiplying matrices... the order matters!"""
    result = _MatrixMultiply(left, right)
    return result


def matrix_translate(x, y, z):
    # type: (float, float, float) -> Matrix
    """Get translation matrix"""
    result = _MatrixTranslate(float(x), float(y), float(z))
    return result


def matrix_rotate(axis, angle):
    # type: (Vector3, float) -> Matrix
    """Create rotation matrix from axis and angle. Angle should be provided in radians"""
    result = _MatrixRotate(_vec3(axis), float(angle))
    return result


def matrix_rotate_x(angle):
    # type: (float) -> Matrix
    """Get x-rotation matrix. Angle must be provided in radians"""
    result = _MatrixRotateX(float(angle))
    return result


def matrix_rotate_y(angle):
    # type: (float) -> Matrix
    """Get y-rotation matrix. Angle must be provided in radians"""
    result = _MatrixRotateY(float(angle))
    return result


def matrix_rotate_z(angle):
    # type: (float) -> Matrix
    """Get z-rotation matrix. Angle must be provided in radians"""
    result = _MatrixRotateZ(float(angle))
    return result


def matrix_rotate_xyz(angle):
    # type: (Vector3) -> Matrix
    """Get xyz-rotation matrix. Angle must be provided in radians"""
    result = _MatrixRotateXYZ(_vec3(angle))
    return result


def matrix_rotate_zyx(angle):
    # type: (Vector3) -> Matrix
    """Get zyx-rotation matrix. Angle must be provided in radians"""
    result = _MatrixRotateZYX(_vec3(angle))
    return result


def matrix_scale(x, y, z):
    # type: (float, float, float) -> Matrix
    """Get scaling matrix"""
    result = _MatrixScale(float(x), float(y), float(z))
    return result


def matrix_frustum(left, right, bottom, top, near, far):
    # type: (float, float, float, float, float, float) -> Matrix
    """Get perspective projection matrix"""
    result = _MatrixFrustum(float(left), float(right), float(bottom), float(top), float(near), float(far))
    return result


def matrix_perspective(fovy, aspect, near, far):
    # type: (float, float, float, float) -> Matrix
    """Get perspective projection matrix. Fovy angle must be provided in radians"""
    result = _MatrixPerspective(float(fovy), float(aspect), float(near), float(far))
    return result


def matrix_ortho(left, right, bottom, top, near, far):
    # type: (float, float, float, float, float, float) -> Matrix
    """Get orthographic projection matrix"""
    result = _MatrixOrtho(float(left), float(right), float(bottom), float(top), float(near), float(far))
    return result


def matrix_look_at(eye, target, up):
    # type: (Vector3, Vector3, Vector3) -> Matrix
    """Get camera look-at matrix (view matrix)"""
    result = _MatrixLookAt(_vec3(eye), _vec3(target), _vec3(up))
    return result


def matrix_to_float_v(mat):
    # type: (Matrix) -> Seq[float]
    """Get float array of matrix data"""
    result = _MatrixToFloatV(mat)
    return result


def quaternion_add(q1, q2):
    # type: (Quaternion, Quaternion) -> Quaternion
    """Add two quaternions"""
    result = _QuaternionAdd(q1, q2)
    return result


def quaternion_add_value(q, add):
    # type: (Quaternion, float) -> Quaternion
    """Add quaternion and float value"""
    result = _QuaternionAddValue(q, float(add))
    return result


def quaternion_subtract(q1, q2):
    # type: (Quaternion, Quaternion) -> Quaternion
    """Subtract two quaternions"""
    result = _QuaternionSubtract(q1, q2)
    return result


def quaternion_subtract_value(q, sub):
    # type: (Quaternion, float) -> Quaternion
    """Subtract quaternion and float value"""
    result = _QuaternionSubtractValue(q, float(sub))
    return result


def quaternion_identity():
    # type: () -> Quaternion
    """Get identity quaternion"""
    result = _QuaternionIdentity()
    return result


def quaternion_length(q):
    # type: (Quaternion) -> Quaternion
    """Computes the length of a quaternion"""
    result = _QuaternionLength(q)
    return result


def quaternion_normalize(q):
    # type: (Quaternion) -> Quaternion
    """Normalize provided quaternion"""
    result = _QuaternionNormalize(q)
    return result


def quaternion_invert(q):
    # type: (Quaternion) -> Quaternion
    """Invert provided quaternion"""
    result = _QuaternionInvert(q)
    return result


def quaternion_multiply(q1, q2):
    # type: (Quaternion, Quaternion) -> Quaternion
    """Calculate two quaternion multiplication"""
    result = _QuaternionMultiply(q1, q2)
    return result


def quaternion_scale(q1, mul):
    # type: (Quaternion, float) -> Quaternion
    """Scale quaternion by float value"""
    result = _QuaternionScale(q1, float(mul))
    return result


def quaternion_divide(q1, q2):
    # type: (Quaternion, Quaternion) -> Quaternion
    """Divide two quaternions"""
    result = _QuaternionDivide(q1, q2)
    return result


def quaternion_nlerp(q1, q2, amount):
    # type: (Quaternion, Quaternion, float) -> Quaternion
    """Calculate slerp-optimized interpolation between two quaternions"""
    result = _QuaternionNlerp(q1, q2, float(amount))
    return result


def quaternion_slerp(q1, q2, amount):
    # type: (Quaternion, Quaternion, float) -> Quaternion
    """Calculates spherical linear interpolation between two quaternions"""
    result = _QuaternionSlerp(q1, q2, float(amount))
    return result


def quaternion_from_vector3to_vector3(from_, to):
    # type: (Vector3, Vector3) -> Quaternion
    """Calculate quaternion based on the rotation from one vector to another"""
    result = _QuaternionFromVector3ToVector3(_vec3(from_), _vec3(to))
    return result


def quaternion_to_matrix(q):
    # type: (Quaternion) -> Matrix
    """Get a quaternion for a given rotation matrix"""
    result = _QuaternionToMatrix(q)
    return result


def quaternion_from_matrix(mat):
    # type: (Matrix) -> Quaternion
    """Get a quaternion for a given rotation matrix"""
    result = _QuaternionFromMatrix(mat)
    return result


def quaternion_from_axis_angle(mat, angle):
    # type: (Vector3, float) -> Quaternion
    """Get rotation quaternion for an angle and axis. Angle must be provided in radians"""
    result = _QuaternionFromAxisAngle(_vec3(mat), float(angle))
    return result


def quaternion_to_axis_angle(q, out_axis, out_angle):
    # type: (Quaternion, Vector3Ptr, Union[Seq[float], FloatPtr]) -> None
    """Get the rotation angle and axis for a given quaternion"""
    _QuaternionToAxisAngle(q, _vec3(out_axis), out_angle)


def quaternion_from_euler(pitch, yaw, roll):
    # type: (float, float, float) -> Quaternion
    """Get the quaternion equivalent to Euler angles. Rotation order is ZYX"""
    result = _QuaternionFromEuler(float(pitch), float(yaw), float(roll))
    return result


def quaternion_to_euler(q):
    # type: (Quaternion) -> Vector3
    """Get the quaternion equivalent to Euler angles. Rotation order is ZYX"""
    result = _QuaternionToEuler(q)
    return result


def quaternion_transform(q, mat):
    # type: (Quaternion, Matrix) -> Quaternion
    """Transform a quaternion given a transformation matrix"""
    result = _QuaternionTransform(q, mat)
    return result


def quaternion_equals(p, q):
    # type: (Quaternion, Quaternion) -> int
    """Check whether two given quaternions are almost equal"""
    result = _QuaternionEquals(p, q)
    return result


def rl_matrix_mode(mode):
    # type: (int) -> None
    """Choose the current matrix to be transformed"""
    _rlMatrixMode(int(mode))


def rl_push_matrix():
    # type: () -> None
    """Push the current matrix to stack"""
    _rlPushMatrix()


def rl_pop_matrix():
    # type: () -> None
    """Pop lattest inserted matrix from stack"""
    _rlPopMatrix()


def rl_load_identity():
    # type: () -> None
    """Reset current matrix to identity matrix"""
    _rlLoadIdentity()


def rl_translatef(x, y, z):
    # type: (float, float, float) -> None
    """Multiply the current matrix by a translation matrix"""
    _rlTranslatef(float(x), float(y), float(z))


def rl_rotatef(angle, x, y, z):
    # type: (float, float, float, float) -> None
    """Multiply the current matrix by a rotation matrix"""
    _rlRotatef(float(angle), float(x), float(y), float(z))


def rl_scalef(x, y, z):
    # type: (float, float, float) -> None
    """Multiply the current matrix by a scaling matrix"""
    _rlScalef(float(x), float(y), float(z))


def rl_mult_matrixf(matf):
    # type: (Union[Seq[float], FloatPtr]) -> None
    """Multiply the current matrix by another matrix"""
    _rlMultMatrixf(matf)


def rl_frustum(left, right, bottom, top, znear, zfar):
    # type: (float, float, float, float, float, float) -> None
    """"""
    _rlFrustum(float(left), float(right), float(bottom), float(top), float(znear), float(zfar))


def rl_ortho(left, right, bottom, top, znear, zfar):
    # type: (float, float, float, float, float, float) -> None
    """"""
    _rlOrtho(float(left), float(right), float(bottom), float(top), float(znear), float(zfar))


def rl_viewport(x, y, width, height):
    # type: (int, int, int, int) -> None
    """Set the viewport area"""
    _rlViewport(int(x), int(y), int(width), int(height))


def rl_begin(mode):
    # type: (int) -> None
    """Initialize drawing mode (how to organize vertex)"""
    _rlBegin(int(mode))


def rl_end():
    # type: () -> None
    """Finish vertex providing"""
    _rlEnd()


def rl_vertex2i(x, y):
    # type: (int, int) -> None
    """Define one vertex (position) - 2 int"""
    _rlVertex2i(int(x), int(y))


def rl_vertex2f(x, y):
    # type: (float, float) -> None
    """Define one vertex (position) - 2 float"""
    _rlVertex2f(float(x), float(y))


def rl_vertex3f(x, y, z):
    # type: (float, float, float) -> None
    """Define one vertex (position) - 3 float"""
    _rlVertex3f(float(x), float(y), float(z))


def rl_tex_coord2f(x, y):
    # type: (float, float) -> None
    """Define one vertex (texture coordinate) - 2 float"""
    _rlTexCoord2f(float(x), float(y))


def rl_normal3f(x, y, z):
    # type: (float, float, float) -> None
    """Define one vertex (normal) - 3 float"""
    _rlNormal3f(float(x), float(y), float(z))


def rl_color4ub(r, g, b, a):
    # type: (int, int, int, int) -> None
    """Define one vertex (color) - 4 byte"""
    _rlColor4ub(r, g, b, a)


def rl_color3f(x, y, z):
    # type: (float, float, float) -> None
    """Define one vertex (color) - 3 float"""
    _rlColor3f(float(x), float(y), float(z))


def rl_color4f(x, y, z, w):
    # type: (float, float, float, float) -> None
    """Define one vertex (color) - 4 float"""
    _rlColor4f(float(x), float(y), float(z), float(w))


def rl_enable_vertex_array(vao_id):
    # type: (int) -> bool
    """Enable vertex array (VAO, if supported)"""
    result = _rlEnableVertexArray(vao_id)
    return result


def rl_disable_vertex_array():
    # type: () -> None
    """Disable vertex array (VAO, if supported)"""
    _rlDisableVertexArray()


def rl_enable_vertex_buffer(id):
    # type: (int) -> None
    """Enable vertex buffer (VBO)"""
    _rlEnableVertexBuffer(id)


def rl_disable_vertex_buffer():
    # type: () -> None
    """Disable vertex buffer (VBO)"""
    _rlDisableVertexBuffer()


def rl_enable_vertex_buffer_element(id):
    # type: (int) -> None
    """Enable vertex buffer element (VBO element)"""
    _rlEnableVertexBufferElement(id)


def rl_disable_vertex_buffer_element():
    # type: () -> None
    """Disable vertex buffer element (VBO element)"""
    _rlDisableVertexBufferElement()


def rl_enable_vertex_attribute(index):
    # type: (int) -> None
    """Enable vertex attribute index"""
    _rlEnableVertexAttribute(index)


def rl_disable_vertex_attribute(index):
    # type: (int) -> None
    """Disable vertex attribute index"""
    _rlDisableVertexAttribute(index)


def rl_active_texture_slot(slot):
    # type: (int) -> None
    """Select and active a texture slot"""
    _rlActiveTextureSlot(int(slot))


def rl_enable_texture(id):
    # type: (int) -> None
    """Enable texture"""
    _rlEnableTexture(id)


def rl_disable_texture():
    # type: () -> None
    """Disable texture"""
    _rlDisableTexture()


def rl_enable_texture_cubemap(id):
    # type: (int) -> None
    """Enable texture cubemap"""
    _rlEnableTextureCubemap(id)


def rl_disable_texture_cubemap():
    # type: () -> None
    """Disable texture cubemap"""
    _rlDisableTextureCubemap()


def rl_texture_parameters(id, param, value):
    # type: (int, int, int) -> None
    """Set texture parameters (filter, wrap)"""
    _rlTextureParameters(id, int(param), int(value))


def rl_enable_shader(id):
    # type: (int) -> None
    """Enable shader program"""
    _rlEnableShader(id)


def rl_disable_shader():
    # type: () -> None
    """Disable shader program"""
    _rlDisableShader()


def rl_enable_framebuffer(id):
    # type: (int) -> None
    """Enable render texture (fbo)"""
    _rlEnableFramebuffer(id)


def rl_disable_framebuffer():
    # type: () -> None
    """Disable render texture (fbo), return to default framebuffer"""
    _rlDisableFramebuffer()


def rl_active_draw_buffers(count):
    # type: (int) -> None
    """Activate multiple draw color buffers"""
    _rlActiveDrawBuffers(int(count))


def rl_enable_color_blend():
    # type: () -> None
    """Enable color blending"""
    _rlEnableColorBlend()


def rl_disable_color_blend():
    # type: () -> None
    """Disable color blending"""
    _rlDisableColorBlend()


def rl_enable_depth_test():
    # type: () -> None
    """Enable depth test"""
    _rlEnableDepthTest()


def rl_disable_depth_test():
    # type: () -> None
    """Disable depth test"""
    _rlDisableDepthTest()


def rl_enable_depth_mask():
    # type: () -> None
    """Enable depth write"""
    _rlEnableDepthMask()


def rl_disable_depth_mask():
    # type: () -> None
    """Disable depth write"""
    _rlDisableDepthMask()


def rl_enable_backface_culling():
    # type: () -> None
    """Enable backface culling"""
    _rlEnableBackfaceCulling()


def rl_disable_backface_culling():
    # type: () -> None
    """Disable backface culling"""
    _rlDisableBackfaceCulling()


def rl_enable_scissor_test():
    # type: () -> None
    """Enable scissor test"""
    _rlEnableScissorTest()


def rl_disable_scissor_test():
    # type: () -> None
    """Disable scissor test"""
    _rlDisableScissorTest()


def rl_scissor(x, y, width, height):
    # type: (int, int, int, int) -> None
    """Scissor test"""
    _rlScissor(int(x), int(y), int(width), int(height))


def rl_enable_wire_mode():
    # type: () -> None
    """Enable wire mode"""
    _rlEnableWireMode()


def rl_disable_wire_mode():
    # type: () -> None
    """Disable wire mode"""
    _rlDisableWireMode()


def rl_set_line_width(width):
    # type: (float) -> None
    """Set the line drawing width"""
    _rlSetLineWidth(float(width))


def rl_get_line_width():
    # type: () -> float
    """Get the line drawing width"""
    result = _rlGetLineWidth()
    return result


def rl_enable_smooth_lines():
    # type: () -> None
    """Enable line aliasing"""
    _rlEnableSmoothLines()


def rl_disable_smooth_lines():
    # type: () -> None
    """Disable line aliasing"""
    _rlDisableSmoothLines()


def rl_enable_stereo_render():
    # type: () -> None
    """Enable stereo rendering"""
    _rlEnableStereoRender()


def rl_disable_stereo_render():
    # type: () -> None
    """Disable stereo rendering"""
    _rlDisableStereoRender()


def rl_is_stereo_render_enabled():
    # type: () -> bool
    """Check if stereo render is enabled"""
    result = _rlIsStereoRenderEnabled()
    return result


def rl_clear_color(r, g, b, a):
    # type: (int, int, int, int) -> None
    """Clear color buffer with color"""
    _rlClearColor(r, g, b, a)


def rl_clear_screen_buffers():
    # type: () -> None
    """Clear used screen buffers (color and depth)"""
    _rlClearScreenBuffers()


def rl_check_errors():
    # type: () -> None
    """Check and log OpenGL error codes"""
    _rlCheckErrors()


def rl_set_blend_mode(mode):
    # type: (int) -> None
    """Set blending mode"""
    _rlSetBlendMode(int(mode))


def rl_set_blend_factors(gl_src_factor, gl_dst_factor, gl_equation):
    # type: (int, int, int) -> None
    """Set blending mode factor and equation (using OpenGL factors)"""
    _rlSetBlendFactors(int(gl_src_factor), int(gl_dst_factor), int(gl_equation))


def rlgl_init(width, height):
    # type: (int, int) -> None
    """Initialize rlgl (buffers, shaders, textures, states)"""
    _rlglInit(int(width), int(height))


def rlgl_close():
    # type: () -> None
    """De-inititialize rlgl (buffers, shaders, textures)"""
    _rlglClose()


def rl_load_extensions(loader):
    # type: (bytes) -> None
    """Load OpenGL extensions (loader function required)"""
    _rlLoadExtensions(loader)


def rl_get_version():
    # type: () -> int
    """Get current OpenGL version"""
    result = _rlGetVersion()
    return result


def rl_set_framebuffer_width(width):
    # type: (int) -> None
    """Set current framebuffer width"""
    _rlSetFramebufferWidth(int(width))


def rl_get_framebuffer_width():
    # type: () -> int
    """Get default framebuffer width"""
    result = _rlGetFramebufferWidth()
    return result


def rl_set_framebuffer_height(height):
    # type: (int) -> None
    """Set current framebuffer height"""
    _rlSetFramebufferHeight(int(height))


def rl_get_framebuffer_height():
    # type: () -> int
    """Get default framebuffer height"""
    result = _rlGetFramebufferHeight()
    return result


def rl_get_texture_id_default():
    # type: () -> int
    """Get default texture id"""
    result = _rlGetTextureIdDefault()
    return result


def rl_get_shader_id_default():
    # type: () -> int
    """Get default shader id"""
    result = _rlGetShaderIdDefault()
    return result


def rl_get_shader_locs_default():
    # type: () -> Union[Seq[int], IntPtr]
    """Get default shader locations"""
    result = _ptr_out(_rlGetShaderLocsDefault())
    return result


def rl_load_render_batch(num_buffers, buffer_elements):
    # type: (int, int) -> rlRenderBatch
    """Load a render batch system"""
    result = _rlLoadRenderBatch(int(num_buffers), int(buffer_elements))
    return result


def rl_unload_render_batch(batch):
    # type: (rlRenderBatch) -> None
    """Unload render batch system"""
    _rlUnloadRenderBatch(batch)


def rl_draw_render_batch(batch):
    # type: (rlRenderBatchPtr) -> None
    """Draw render batch data (Update->Draw->Reset)"""
    _rlDrawRenderBatch(batch)


def rl_set_render_batch_active(batch):
    # type: (rlRenderBatchPtr) -> None
    """Set the active render batch for rlgl (NULL for default internal)"""
    _rlSetRenderBatchActive(batch)


def rl_draw_render_batch_active():
    # type: () -> None
    """Update and draw internal render batch"""
    _rlDrawRenderBatchActive()


def rl_check_render_batch_limit(v_count):
    # type: (int) -> bool
    """Check internal buffer overflow for a given number of vertex"""
    result = _rlCheckRenderBatchLimit(int(v_count))
    return result


def rl_set_texture(id):
    # type: (int) -> None
    """Set current texture for render batch and check buffers limits"""
    _rlSetTexture(id)


def rl_load_vertex_array():
    # type: () -> int
    """Load vertex array (vao) if supported"""
    result = _rlLoadVertexArray()
    return result


def rl_load_vertex_buffer(buffer, size, dynamic):
    # type: (bytes, int, bool) -> int
    """Load a vertex buffer attribute"""
    result = _rlLoadVertexBuffer(buffer, int(size), bool(dynamic))
    return result


def rl_load_vertex_buffer_element(buffer, size, dynamic):
    # type: (bytes, int, bool) -> int
    """Load a new attributes element buffer"""
    result = _rlLoadVertexBufferElement(buffer, int(size), bool(dynamic))
    return result


def rl_update_vertex_buffer(buffer_id, data, data_size, offset):
    # type: (int, bytes, int, int) -> None
    """Update GPU buffer with new data"""
    _rlUpdateVertexBuffer(buffer_id, data, int(data_size), int(offset))


def rl_update_vertex_buffer_elements(id, data, data_size, offset):
    # type: (int, bytes, int, int) -> None
    """Update vertex buffer elements with new data"""
    _rlUpdateVertexBufferElements(id, data, int(data_size), int(offset))


def rl_unload_vertex_array(vao_id):
    # type: (int) -> None
    """"""
    _rlUnloadVertexArray(vao_id)


def rl_unload_vertex_buffer(vbo_id):
    # type: (int) -> None
    """"""
    _rlUnloadVertexBuffer(vbo_id)


def rl_set_vertex_attribute(index, comp_size, type, normalized, stride, pointer):
    # type: (int, int, int, bool, int, bytes) -> None
    """"""
    _rlSetVertexAttribute(index, int(comp_size), int(type), bool(normalized), int(stride), pointer)


def rl_set_vertex_attribute_divisor(index, divisor):
    # type: (int, int) -> None
    """"""
    _rlSetVertexAttributeDivisor(index, int(divisor))


def rl_set_vertex_attribute_default(loc_index, value, attrib_type, count):
    # type: (int, bytes, int, int) -> None
    """Set vertex attribute default value"""
    _rlSetVertexAttributeDefault(int(loc_index), value, int(attrib_type), int(count))


def rl_draw_vertex_array(offset, count):
    # type: (int, int) -> None
    """"""
    _rlDrawVertexArray(int(offset), int(count))


def rl_draw_vertex_array_elements(offset, count, buffer):
    # type: (int, int, bytes) -> None
    """"""
    _rlDrawVertexArrayElements(int(offset), int(count), buffer)


def rl_draw_vertex_array_instanced(offset, count, instances):
    # type: (int, int, int) -> None
    """"""
    _rlDrawVertexArrayInstanced(int(offset), int(count), int(instances))


def rl_draw_vertex_array_elements_instanced(offset, count, buffer, instances):
    # type: (int, int, bytes, int) -> None
    """"""
    _rlDrawVertexArrayElementsInstanced(int(offset), int(count), buffer, int(instances))


def rl_load_texture(data, width, height, format, mipmap_count):
    # type: (bytes, int, int, int, int) -> int
    """Load texture in GPU"""
    result = _rlLoadTexture(data, int(width), int(height), int(format), int(mipmap_count))
    return result


def rl_load_texture_depth(width, height, use_render_buffer):
    # type: (int, int, bool) -> int
    """Load depth texture/renderbuffer (to be attached to fbo)"""
    result = _rlLoadTextureDepth(int(width), int(height), bool(use_render_buffer))
    return result


def rl_load_texture_cubemap(data, size, format):
    # type: (bytes, int, int) -> int
    """Load texture cubemap"""
    result = _rlLoadTextureCubemap(data, int(size), int(format))
    return result


def rl_update_texture(id, offset_x, offset_y, width, height, format, data):
    # type: (int, int, int, int, int, int, bytes) -> None
    """Update GPU texture with new data"""
    _rlUpdateTexture(id, int(offset_x), int(offset_y), int(width), int(height), int(format), data)


def rl_get_gl_texture_formats(format, gl_internal_format, gl_format, gl_type):
    # type: (int, Union[Seq[int], UIntPtr], Union[Seq[int], UIntPtr], Union[Seq[int], UIntPtr]) -> None
    """Get OpenGL internal formats"""
    _rlGetGlTextureFormats(int(format), gl_internal_format, gl_format, gl_type)


def rl_get_pixel_format_name(format):
    # type: (int) -> Union[str, CharPtr]
    """Get name string for pixel format"""
    result = _ptr_out(_rlGetPixelFormatName(format))
    return result


def rl_unload_texture(id):
    # type: (int) -> None
    """Unload texture from GPU memory"""
    _rlUnloadTexture(id)


def rl_gen_texture_mipmaps(id, width, height, format, mipmaps):
    # type: (int, int, int, int, Union[Seq[int], IntPtr]) -> None
    """Generate mipmap data for selected texture"""
    _rlGenTextureMipmaps(id, int(width), int(height), int(format), mipmaps)


def rl_read_texture_pixels(id, width, height, format):
    # type: (int, int, int, int) -> bytes
    """Read texture pixel data"""
    _rlReadTexturePixels(id, int(width), int(height), int(format))


def rl_read_screen_pixels(width, height):
    # type: (int, int) -> Union[Seq[int], UCharPtr]
    """Read screen pixel data (color buffer)"""
    result = _ptr_out(_rlReadScreenPixels(int(width), int(height)))
    return result


def rl_load_framebuffer(width, height):
    # type: (int, int) -> int
    """Load an empty framebuffer"""
    result = _rlLoadFramebuffer(int(width), int(height))
    return result


def rl_framebuffer_attach(fbo_id, tex_id, attach_type, tex_type, mip_level):
    # type: (int, int, int, int, int) -> None
    """Attach texture/renderbuffer to a framebuffer"""
    _rlFramebufferAttach(fbo_id, tex_id, int(attach_type), int(tex_type), int(mip_level))


def rl_framebuffer_complete(id):
    # type: (int) -> bool
    """Verify framebuffer is complete"""
    result = _rlFramebufferComplete(id)
    return result


def rl_unload_framebuffer(id):
    # type: (int) -> None
    """Delete framebuffer from GPU"""
    _rlUnloadFramebuffer(id)


def rl_load_shader_code(vs_code, fs_code):
    # type: (Union[str, CharPtr], Union[str, CharPtr]) -> int
    """Load shader from code strings"""
    result = _rlLoadShaderCode(_str_in(vs_code), _str_in(fs_code))
    return result


def rl_compile_shader(shader_code, type):
    # type: (Union[str, CharPtr], int) -> int
    """Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)"""
    result = _rlCompileShader(_str_in(shader_code), int(type))
    return result


def rl_load_shader_program(v_shader_id, f_shader_id):
    # type: (int, int) -> int
    """Load custom shader program"""
    result = _rlLoadShaderProgram(v_shader_id, f_shader_id)
    return result


def rl_unload_shader_program(id):
    # type: (int) -> None
    """Unload shader program"""
    _rlUnloadShaderProgram(id)


def rl_get_location_uniform(shader_id, uniform_name):
    # type: (int, Union[str, CharPtr]) -> int
    """Get shader location uniform"""
    result = _rlGetLocationUniform(shader_id, _str_in(uniform_name))
    return result


def rl_get_location_attrib(shader_id, attrib_name):
    # type: (int, Union[str, CharPtr]) -> int
    """Get shader location attribute"""
    result = _rlGetLocationAttrib(shader_id, _str_in(attrib_name))
    return result


def rl_set_uniform(loc_index, value, uniform_type, count):
    # type: (int, bytes, int, int) -> None
    """Set shader value uniform"""
    _rlSetUniform(int(loc_index), value, int(uniform_type), int(count))


def rl_set_uniform_matrix(loc_index, mat):
    # type: (int, Matrix) -> None
    """Set shader value matrix"""
    _rlSetUniformMatrix(int(loc_index), mat)


def rl_set_uniform_sampler(loc_index, texture_id):
    # type: (int, int) -> None
    """Set shader value sampler"""
    _rlSetUniformSampler(int(loc_index), texture_id)


def rl_set_shader(id, locs):
    # type: (int, Union[Seq[int], IntPtr]) -> None
    """Set shader currently active (id and locations)"""
    _rlSetShader(id, locs)


def rl_load_compute_shader_program(shader_id):
    # type: (int) -> int
    """Load compute shader program"""
    result = _rlLoadComputeShaderProgram(shader_id)
    return result


def rl_compute_shader_dispatch(group_x, group_y, group_z):
    # type: (int, int, int) -> None
    """Dispatch compute shader (equivalent to *draw* for graphics pilepine)"""
    _rlComputeShaderDispatch(group_x, group_y, group_z)


def rl_load_shader_buffer(size, data, usage_hint):
    # type: (int, bytes, int) -> int
    """Load shader storage buffer object (SSBO)"""
    result = _rlLoadShaderBuffer(int(size), data, int(usage_hint))
    return result


def rl_unload_shader_buffer(ssbo_id):
    # type: (int) -> None
    """Unload shader storage buffer object (SSBO)"""
    _rlUnloadShaderBuffer(ssbo_id)


def rl_update_shader_buffer_elements(id, data, data_size, offset):
    # type: (int, bytes, int, int) -> None
    """Update SSBO buffer data"""
    _rlUpdateShaderBufferElements(id, data, int(data_size), int(offset))


def rl_get_shader_buffer_size(id):
    # type: (int) -> int
    """Get SSBO buffer size"""
    result = _rlGetShaderBufferSize(id)
    return result


def rl_read_shader_buffer_elements(id, dest, count, offset):
    # type: (int, bytes, int, int) -> None
    """Bind SSBO buffer"""
    _rlReadShaderBufferElements(id, dest, int(count), int(offset))


def rl_bind_shader_buffer(id, index):
    # type: (int, int) -> None
    """Copy SSBO buffer data"""
    _rlBindShaderBuffer(id, index)


def rl_copy_buffers_elements(dest_id, src_id, dest_offset, src_offset, count):
    # type: (int, int, int, int, int) -> None
    """Copy SSBO buffer data"""
    _rlCopyBuffersElements(dest_id, src_id, int(dest_offset), int(src_offset), int(count))


def rl_bind_image_texture(id, index, format, readonly):
    # type: (int, int, int, int) -> None
    """Bind image texture"""
    _rlBindImageTexture(id, index, format, int(readonly))


def rl_get_matrix_modelview():
    # type: () -> Matrix
    """Get internal modelview matrix"""
    result = _rlGetMatrixModelview()
    return result


def rl_get_matrix_projection():
    # type: () -> Matrix
    """Get internal projection matrix"""
    result = _rlGetMatrixProjection()
    return result


def rl_get_matrix_transform():
    # type: () -> Matrix
    """Get internal accumulated transform matrix"""
    result = _rlGetMatrixTransform()
    return result


def rl_get_matrix_projection_stereo(eye):
    # type: (int) -> Matrix
    """Get internal projection matrix for stereo render (selected eye)"""
    result = _rlGetMatrixProjectionStereo(int(eye))
    return result


def rl_get_matrix_view_offset_stereo(eye):
    # type: (int) -> Matrix
    """Get internal view offset matrix for stereo render (selected eye)"""
    result = _rlGetMatrixViewOffsetStereo(int(eye))
    return result


def rl_set_matrix_projection(proj):
    # type: (Matrix) -> None
    """Set a custom projection matrix (replaces internal projection matrix)"""
    _rlSetMatrixProjection(proj)


def rl_set_matrix_modelview(view):
    # type: (Matrix) -> None
    """Set a custom modelview matrix (replaces internal modelview matrix)"""
    _rlSetMatrixModelview(view)


def rl_set_matrix_projection_stereo(right, left):
    # type: (Matrix, Matrix) -> None
    """Set eyes projection matrices for stereo rendering"""
    _rlSetMatrixProjectionStereo(right, left)


def rl_set_matrix_view_offset_stereo(right, left):
    # type: (Matrix, Matrix) -> None
    """Set eyes view offsets matrices for stereo rendering"""
    _rlSetMatrixViewOffsetStereo(right, left)


def rl_load_draw_cube():
    # type: () -> None
    """Load and draw a cube"""
    _rlLoadDrawCube()


def rl_load_draw_quad():
    # type: () -> None
    """Load and draw a quad"""
    _rlLoadDrawQuad()

@contextmanager
def drawing():# type: () -> None
    """Context manager for drawing"""
    _BeginDrawing()
    yield
    _EndDrawing()

@contextmanager
def scissor_mode(x, y, width, height):# type: (int, int, int, int) -> None
    """Context manager for scissor mode"""
    _BeginScissorMode(int(x), int(y), int(width), int(height))
    yield
    _EndScissorMode()

@contextmanager
def blend_mode(mode):# type: (int) -> None
    """Context manager for blend mode"""
    _BeginBlendMode(int(mode))
    yield
    _EndBlendMode()

@contextmanager
def mode2d(camera):# type: (Camera2D) -> None
    """Context manager for mode2d"""
    _BeginMode2D(camera)
    yield
    _EndMode2D()

@contextmanager
def mode3d(camera):# type: (Camera3D) -> None
    """Context manager for mode3d"""
    _BeginMode3D(camera)
    yield
    _EndMode3D()

@contextmanager
def shader_mode(shader):# type: (Shader) -> None
    """Context manager for shader mode"""
    _BeginShaderMode(shader)
    yield
    _EndShaderMode()

@contextmanager
def texture_mode(target):# type: (RenderTexture2D) -> None
    """Context manager for texture mode"""
    _BeginTextureMode(target)
    yield
    _EndTextureMode()

@contextmanager
def vr_stereo_mode(config):# type: (VrStereoConfig) -> None
    """Context manager for vr stereo mode"""
    _BeginVrStereoMode(config)
    yield
    _EndVrStereoMode()

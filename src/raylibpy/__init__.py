# #!/usr/bin/python3
# -*- encoding: utf8 -*-

# region LICENSE INFORMATION

# C raylib license

# ------------------------------------------------------------------------------
# zlib/libpng
#
# raylib is licensed under an unmodified zlib/libpng license, which is an OSI-certified,
# BSD-like license that allows static linking with closed source software:
#
# Copyright (c) 2013-2023 Ramon Santamaria (@raysan5)
#
# This software is provided "as-is", without any express or implied warranty. In no event
# will the authors be held liable for any damages arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose, including commercial
# applications, and to alter it and redistribute it freely, subject to the following restrictions:
#
#    1. The origin of this software must not be misrepresented; you must not claim that you
#    wrote the original software. If you use this software in a product, an acknowledgment
#    in the product documentation would be appreciated but is not required.
#
#    2. Altered source versions must be plainly marked as such, and must not be misrepresented
#    as being the original software.
#
#    3. This notice may not be removed or altered from any source distribution.
#
# ------------------------------------------------------------------------------

# raylib-py license

# ------------------------------------------------------------------------------
# The MIT License
#
#
# Copyright (c) 2023 Jorge A. Gomes
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ------------------------------------------------------------------------------

# endregion (license information)

# region IMPORTS

import sys
import re
import os
import platform
import ctypes
import json
import struct

from typing import Generic, TypeVar
from enum import IntEnum
from contextlib import contextmanager
from ctypes import (
    CDLL, wintypes,
    c_bool,
    c_char, c_wchar, c_char_p, c_wchar_p,
    c_byte, c_short, c_int, c_long, c_longlong,
    c_ubyte, c_ushort, c_uint, c_ulong, c_ulonglong,
    c_float, c_double, c_longdouble,
    c_void_p, c_size_t,
    Array, Structure, POINTER, CFUNCTYPE, byref, cast, pointer, POINTER
)

from . import easings


# endregion (imports)

# region EXPORTS

__all__ = [

    # utilities
    'byte_array',
    'clear_format_string_cache',
    'double_array',
    'float_array',
    'int_array',
    'pop_out_param',
    'short_array',
    'string_array',
    'ubyte_array',
    'uint_array',
    'ushort_array',

    # types
    'AutomationEventListPtr',
    'AutomationEventPtr',
    'BoneInfoPtr',
    'Bool',
    'CameraPtr',
    'Char',
    'Char32',
    'CharPtr',
    'CharPtrPtr',
    'ColorPtr',
    'Double',
    'Float',
    'Float16',
    'Float2',
    'Float3',
    'Float4',
    'FloatPtr',
    'GlyphInfoPtr',
    'ImagePtr',
    'Int',
    'Int4',
    'IntPtr',
    'Long',
    'MaterialMapPtr',
    'MaterialPtr',
    'MatrixPtr',
    'MeshPtr',
    'ModelAnimationPtr',
    'ModelPtr',
    'RectanglePtr',
    'RectanglePtrPtr',
    'Texture2DPtr',
    'TransformPtr',
    'TransformPtrPtr',
    'UChar',
    'UCharPtr',
    'UInt',
    'UInt4',
    'UIntPtr',
    'UShortPtr',
    'Vector2Ptr',
    'Vector3Ptr',
    'VoidPtr',
    'WavePtr',
    'rAudioBufferPtr',
    'rAudioProcessorPtr',
    'rlDrawCallPtr',
    'rlRenderBatchPtr',
    'rlVertexBufferPtr',

    # structs
    'AudioStream',
    'AutomationEvent',
    'AutomationEventList',
    'BoneInfo',
    'BoundingBox',
    'Camera2D',
    'Camera3D',
    'Color',
    'FilePathList',
    'Font',
    'GlyphInfo',
    'Image',
    'Material',
    'MaterialMap',
    'Matrix',
    'Mesh',
    'Model',
    'ModelAnimation',
    'Music',
    'NPatchInfo',
    'Ray',
    'RayCollision',
    'Rectangle',
    'RenderTexture',
    'Shader',
    'Sound',
    'Texture',
    'Transform',
    'Vector2',
    'Vector3',
    'Vector4',
    'VrDeviceInfo',
    'VrStereoConfig',
    'Wave',
    'float16',
    'float3',
    'rlDrawCall',
    'rlRenderBatch',
    'rlVertexBuffer',

    # enums
    'BlendMode',
    'CameraMode',
    'CameraProjection',
    'ConfigFlags',
    'CubemapLayout',
    'FontType',
    'GamepadAxis',
    'GamepadButton',
    'Gesture',
    'KeyboardKey',
    'MaterialMapIndex',
    'MouseButton',
    'MouseCursor',
    'NPatchLayout',
    'PixelFormat',
    'ShaderAttributeDataType',
    'ShaderLocationIndex',
    'ShaderUniformDataType',
    'TextureFilter',
    'TextureWrap',
    'TraceLogLevel',
    'rlBlendMode',
    'rlCullMode',
    'rlFramebufferAttachTextureType',
    'rlFramebufferAttachType',
    'rlGlVersion',
    'rlPixelFormat',
    'rlShaderAttributeDataType',
    'rlShaderLocationIndex',
    'rlShaderUniformDataType',
    'rlTextureFilter',
    'rlTraceLogLevel',

    # aliases
    'Camera',
    'CameraPtr',
    'Quaternion',
    'QuaternionPtr',
    'RenderTexture2D',
    'RenderTexture2DPtr',
    'Texture2D',
    'Texture2DPtr',
    'TextureCubemap',
    'TextureCubemapPtr',

    # enumerands
    'BLEND_ADDITIVE',
    'BLEND_ADD_COLORS',
    'BLEND_ALPHA',
    'BLEND_ALPHA_PREMULTIPLY',
    'BLEND_CUSTOM',
    'BLEND_CUSTOM_SEPARATE',
    'BLEND_MULTIPLIED',
    'BLEND_SUBTRACT_COLORS',
    'CAMERA_CUSTOM',
    'CAMERA_FIRST_PERSON',
    'CAMERA_FREE',
    'CAMERA_ORBITAL',
    'CAMERA_ORTHOGRAPHIC',
    'CAMERA_PERSPECTIVE',
    'CAMERA_THIRD_PERSON',
    'CUBEMAP_LAYOUT_AUTO_DETECT',
    'CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE',
    'CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR',
    'CUBEMAP_LAYOUT_LINE_HORIZONTAL',
    'CUBEMAP_LAYOUT_LINE_VERTICAL',
    'CUBEMAP_LAYOUT_PANORAMA',
    'FLAG_BORDERLESS_WINDOWED_MODE',
    'FLAG_FULLSCREEN_MODE',
    'FLAG_INTERLACED_HINT',
    'FLAG_MSAA_4X_HINT',
    'FLAG_VSYNC_HINT',
    'FLAG_WINDOW_ALWAYS_RUN',
    'FLAG_WINDOW_HIDDEN',
    'FLAG_WINDOW_HIGHDPI',
    'FLAG_WINDOW_MAXIMIZED',
    'FLAG_WINDOW_MINIMIZED',
    'FLAG_WINDOW_MOUSE_PASSTHROUGH',
    'FLAG_WINDOW_RESIZABLE',
    'FLAG_WINDOW_TOPMOST',
    'FLAG_WINDOW_TRANSPARENT',
    'FLAG_WINDOW_UNDECORATED',
    'FLAG_WINDOW_UNFOCUSED',
    'FONT_BITMAP',
    'FONT_DEFAULT',
    'FONT_SDF',
    'GAMEPAD_AXIS_LEFT_TRIGGER',
    'GAMEPAD_AXIS_LEFT_X',
    'GAMEPAD_AXIS_LEFT_Y',
    'GAMEPAD_AXIS_RIGHT_TRIGGER',
    'GAMEPAD_AXIS_RIGHT_X',
    'GAMEPAD_AXIS_RIGHT_Y',
    'GAMEPAD_BUTTON_LEFT_FACE_DOWN',
    'GAMEPAD_BUTTON_LEFT_FACE_LEFT',
    'GAMEPAD_BUTTON_LEFT_FACE_RIGHT',
    'GAMEPAD_BUTTON_LEFT_FACE_UP',
    'GAMEPAD_BUTTON_LEFT_THUMB',
    'GAMEPAD_BUTTON_LEFT_TRIGGER_1',
    'GAMEPAD_BUTTON_LEFT_TRIGGER_2',
    'GAMEPAD_BUTTON_MIDDLE',
    'GAMEPAD_BUTTON_MIDDLE_LEFT',
    'GAMEPAD_BUTTON_MIDDLE_RIGHT',
    'GAMEPAD_BUTTON_RIGHT_FACE_DOWN',
    'GAMEPAD_BUTTON_RIGHT_FACE_LEFT',
    'GAMEPAD_BUTTON_RIGHT_FACE_RIGHT',
    'GAMEPAD_BUTTON_RIGHT_FACE_UP',
    'GAMEPAD_BUTTON_RIGHT_THUMB',
    'GAMEPAD_BUTTON_RIGHT_TRIGGER_1',
    'GAMEPAD_BUTTON_RIGHT_TRIGGER_2',
    'GAMEPAD_BUTTON_UNKNOWN',
    'GESTURE_DOUBLETAP',
    'GESTURE_DRAG',
    'GESTURE_HOLD',
    'GESTURE_NONE',
    'GESTURE_PINCH_IN',
    'GESTURE_PINCH_OUT',
    'GESTURE_SWIPE_DOWN',
    'GESTURE_SWIPE_LEFT',
    'GESTURE_SWIPE_RIGHT',
    'GESTURE_SWIPE_UP',
    'GESTURE_TAP',
    'KEY_A',
    'KEY_APOSTROPHE',
    'KEY_B',
    'KEY_BACK',
    'KEY_BACKSLASH',
    'KEY_BACKSPACE',
    'KEY_C',
    'KEY_CAPS_LOCK',
    'KEY_COMMA',
    'KEY_D',
    'KEY_DELETE',
    'KEY_DOWN',
    'KEY_E',
    'KEY_EIGHT',
    'KEY_END',
    'KEY_ENTER',
    'KEY_EQUAL',
    'KEY_ESCAPE',
    'KEY_F',
    'KEY_F1',
    'KEY_F10',
    'KEY_F11',
    'KEY_F12',
    'KEY_F2',
    'KEY_F3',
    'KEY_F4',
    'KEY_F5',
    'KEY_F6',
    'KEY_F7',
    'KEY_F8',
    'KEY_F9',
    'KEY_FIVE',
    'KEY_FOUR',
    'KEY_G',
    'KEY_GRAVE',
    'KEY_H',
    'KEY_HOME',
    'KEY_I',
    'KEY_INSERT',
    'KEY_J',
    'KEY_K',
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
    'KEY_KP_ADD',
    'KEY_KP_DECIMAL',
    'KEY_KP_DIVIDE',
    'KEY_KP_ENTER',
    'KEY_KP_EQUAL',
    'KEY_KP_MULTIPLY',
    'KEY_KP_SUBTRACT',
    'KEY_L',
    'KEY_LEFT',
    'KEY_LEFT_ALT',
    'KEY_LEFT_BRACKET',
    'KEY_LEFT_CONTROL',
    'KEY_LEFT_SHIFT',
    'KEY_LEFT_SUPER',
    'KEY_M',
    'KEY_MENU',
    'KEY_MINUS',
    'KEY_N',
    'KEY_NINE',
    'KEY_NULL',
    'KEY_NUM_LOCK',
    'KEY_O',
    'KEY_ONE',
    'KEY_P',
    'KEY_PAGE_DOWN',
    'KEY_PAGE_UP',
    'KEY_PAUSE',
    'KEY_PERIOD',
    'KEY_PRINT_SCREEN',
    'KEY_Q',
    'KEY_R',
    'KEY_RIGHT',
    'KEY_RIGHT_ALT',
    'KEY_RIGHT_BRACKET',
    'KEY_RIGHT_CONTROL',
    'KEY_RIGHT_SHIFT',
    'KEY_RIGHT_SUPER',
    'KEY_S',
    'KEY_SCROLL_LOCK',
    'KEY_SEMICOLON',
    'KEY_SEVEN',
    'KEY_SIX',
    'KEY_SLASH',
    'KEY_SPACE',
    'KEY_T',
    'KEY_TAB',
    'KEY_THREE',
    'KEY_TWO',
    'KEY_U',
    'KEY_UP',
    'KEY_V',
    'KEY_VOLUME_DOWN',
    'KEY_VOLUME_UP',
    'KEY_W',
    'KEY_X',
    'KEY_Y',
    'KEY_Z',
    'KEY_ZERO',
    'LOG_ALL',
    'LOG_DEBUG',
    'LOG_ERROR',
    'LOG_FATAL',
    'LOG_INFO',
    'LOG_NONE',
    'LOG_TRACE',
    'LOG_WARNING',
    'MATERIAL_MAP_ALBEDO',
    'MATERIAL_MAP_BRDF',
    'MATERIAL_MAP_CUBEMAP',
    'MATERIAL_MAP_EMISSION',
    'MATERIAL_MAP_HEIGHT',
    'MATERIAL_MAP_IRRADIANCE',
    'MATERIAL_MAP_METALNESS',
    'MATERIAL_MAP_NORMAL',
    'MATERIAL_MAP_OCCLUSION',
    'MATERIAL_MAP_PREFILTER',
    'MATERIAL_MAP_ROUGHNESS',
    'MOUSE_BUTTON_BACK',
    'MOUSE_BUTTON_EXTRA',
    'MOUSE_BUTTON_FORWARD',
    'MOUSE_BUTTON_LEFT',
    'MOUSE_BUTTON_MIDDLE',
    'MOUSE_BUTTON_RIGHT',
    'MOUSE_BUTTON_SIDE',
    'MOUSE_CURSOR_ARROW',
    'MOUSE_CURSOR_CROSSHAIR',
    'MOUSE_CURSOR_DEFAULT',
    'MOUSE_CURSOR_IBEAM',
    'MOUSE_CURSOR_NOT_ALLOWED',
    'MOUSE_CURSOR_POINTING_HAND',
    'MOUSE_CURSOR_RESIZE_ALL',
    'MOUSE_CURSOR_RESIZE_EW',
    'MOUSE_CURSOR_RESIZE_NESW',
    'MOUSE_CURSOR_RESIZE_NS',
    'MOUSE_CURSOR_RESIZE_NWSE',
    'NPATCH_NINE_PATCH',
    'NPATCH_THREE_PATCH_HORIZONTAL',
    'NPATCH_THREE_PATCH_VERTICAL',
    'PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA',
    'PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT1_RGB',
    'PIXELFORMAT_COMPRESSED_DXT1_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT3_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT5_RGBA',
    'PIXELFORMAT_COMPRESSED_ETC1_RGB',
    'PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA',
    'PIXELFORMAT_COMPRESSED_ETC2_RGB',
    'PIXELFORMAT_COMPRESSED_PVRT_RGB',
    'PIXELFORMAT_COMPRESSED_PVRT_RGBA',
    'PIXELFORMAT_UNCOMPRESSED_GRAYSCALE',
    'PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA',
    'PIXELFORMAT_UNCOMPRESSED_R16',
    'PIXELFORMAT_UNCOMPRESSED_R16G16B16',
    'PIXELFORMAT_UNCOMPRESSED_R16G16B16A16',
    'PIXELFORMAT_UNCOMPRESSED_R32',
    'PIXELFORMAT_UNCOMPRESSED_R32G32B32',
    'PIXELFORMAT_UNCOMPRESSED_R32G32B32A32',
    'PIXELFORMAT_UNCOMPRESSED_R4G4B4A4',
    'PIXELFORMAT_UNCOMPRESSED_R5G5B5A1',
    'PIXELFORMAT_UNCOMPRESSED_R5G6B5',
    'PIXELFORMAT_UNCOMPRESSED_R8G8B8',
    'PIXELFORMAT_UNCOMPRESSED_R8G8B8A8',
    'RL_ATTACHMENT_COLOR_CHANNEL0',
    'RL_ATTACHMENT_COLOR_CHANNEL1',
    'RL_ATTACHMENT_COLOR_CHANNEL2',
    'RL_ATTACHMENT_COLOR_CHANNEL3',
    'RL_ATTACHMENT_COLOR_CHANNEL4',
    'RL_ATTACHMENT_COLOR_CHANNEL5',
    'RL_ATTACHMENT_COLOR_CHANNEL6',
    'RL_ATTACHMENT_COLOR_CHANNEL7',
    'RL_ATTACHMENT_CUBEMAP_NEGATIVE_X',
    'RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y',
    'RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z',
    'RL_ATTACHMENT_CUBEMAP_POSITIVE_X',
    'RL_ATTACHMENT_CUBEMAP_POSITIVE_Y',
    'RL_ATTACHMENT_CUBEMAP_POSITIVE_Z',
    'RL_ATTACHMENT_DEPTH',
    'RL_ATTACHMENT_RENDERBUFFER',
    'RL_ATTACHMENT_STENCIL',
    'RL_ATTACHMENT_TEXTURE2D',
    'RL_BLEND_ADDITIVE',
    'RL_BLEND_ADD_COLORS',
    'RL_BLEND_ALPHA',
    'RL_BLEND_ALPHA_PREMULTIPLY',
    'RL_BLEND_CUSTOM',
    'RL_BLEND_CUSTOM_SEPARATE',
    'RL_BLEND_MULTIPLIED',
    'RL_BLEND_SUBTRACT_COLORS',
    'RL_CULL_FACE_BACK',
    'RL_CULL_FACE_FRONT',
    'RL_LOG_ALL',
    'RL_LOG_DEBUG',
    'RL_LOG_ERROR',
    'RL_LOG_FATAL',
    'RL_LOG_INFO',
    'RL_LOG_NONE',
    'RL_LOG_TRACE',
    'RL_LOG_WARNING',
    'RL_OPENGL_11',
    'RL_OPENGL_21',
    'RL_OPENGL_33',
    'RL_OPENGL_43',
    'RL_OPENGL_ES_20',
    'RL_OPENGL_ES_30',
    'RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_DXT1_RGB',
    'RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_ETC1_RGB',
    'RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA',
    'RL_PIXELFORMAT_COMPRESSED_ETC2_RGB',
    'RL_PIXELFORMAT_COMPRESSED_PVRT_RGB',
    'RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA',
    'RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE',
    'RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA',
    'RL_PIXELFORMAT_UNCOMPRESSED_R16',
    'RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16',
    'RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16A16',
    'RL_PIXELFORMAT_UNCOMPRESSED_R32',
    'RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32',
    'RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32',
    'RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4',
    'RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1',
    'RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5',
    'RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8',
    'RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8',
    'RL_SHADER_ATTRIB_FLOAT',
    'RL_SHADER_ATTRIB_VEC2',
    'RL_SHADER_ATTRIB_VEC3',
    'RL_SHADER_ATTRIB_VEC4',
    'RL_SHADER_LOC_COLOR_AMBIENT',
    'RL_SHADER_LOC_COLOR_DIFFUSE',
    'RL_SHADER_LOC_COLOR_SPECULAR',
    'RL_SHADER_LOC_MAP_ALBEDO',
    'RL_SHADER_LOC_MAP_BRDF',
    'RL_SHADER_LOC_MAP_CUBEMAP',
    'RL_SHADER_LOC_MAP_EMISSION',
    'RL_SHADER_LOC_MAP_HEIGHT',
    'RL_SHADER_LOC_MAP_IRRADIANCE',
    'RL_SHADER_LOC_MAP_METALNESS',
    'RL_SHADER_LOC_MAP_NORMAL',
    'RL_SHADER_LOC_MAP_OCCLUSION',
    'RL_SHADER_LOC_MAP_PREFILTER',
    'RL_SHADER_LOC_MAP_ROUGHNESS',
    'RL_SHADER_LOC_MATRIX_MODEL',
    'RL_SHADER_LOC_MATRIX_MVP',
    'RL_SHADER_LOC_MATRIX_NORMAL',
    'RL_SHADER_LOC_MATRIX_PROJECTION',
    'RL_SHADER_LOC_MATRIX_VIEW',
    'RL_SHADER_LOC_VECTOR_VIEW',
    'RL_SHADER_LOC_VERTEX_COLOR',
    'RL_SHADER_LOC_VERTEX_NORMAL',
    'RL_SHADER_LOC_VERTEX_POSITION',
    'RL_SHADER_LOC_VERTEX_TANGENT',
    'RL_SHADER_LOC_VERTEX_TEXCOORD01',
    'RL_SHADER_LOC_VERTEX_TEXCOORD02',
    'RL_SHADER_UNIFORM_FLOAT',
    'RL_SHADER_UNIFORM_INT',
    'RL_SHADER_UNIFORM_IVEC2',
    'RL_SHADER_UNIFORM_IVEC3',
    'RL_SHADER_UNIFORM_IVEC4',
    'RL_SHADER_UNIFORM_SAMPLER2D',
    'RL_SHADER_UNIFORM_VEC2',
    'RL_SHADER_UNIFORM_VEC3',
    'RL_SHADER_UNIFORM_VEC4',
    'RL_TEXTURE_FILTER_ANISOTROPIC_16X',
    'RL_TEXTURE_FILTER_ANISOTROPIC_4X',
    'RL_TEXTURE_FILTER_ANISOTROPIC_8X',
    'RL_TEXTURE_FILTER_BILINEAR',
    'RL_TEXTURE_FILTER_POINT',
    'RL_TEXTURE_FILTER_TRILINEAR',
    'SHADER_ATTRIB_FLOAT',
    'SHADER_ATTRIB_VEC2',
    'SHADER_ATTRIB_VEC3',
    'SHADER_ATTRIB_VEC4',
    'SHADER_LOC_COLOR_AMBIENT',
    'SHADER_LOC_COLOR_DIFFUSE',
    'SHADER_LOC_COLOR_SPECULAR',
    'SHADER_LOC_MAP_ALBEDO',
    'SHADER_LOC_MAP_BRDF',
    'SHADER_LOC_MAP_CUBEMAP',
    'SHADER_LOC_MAP_EMISSION',
    'SHADER_LOC_MAP_HEIGHT',
    'SHADER_LOC_MAP_IRRADIANCE',
    'SHADER_LOC_MAP_METALNESS',
    'SHADER_LOC_MAP_NORMAL',
    'SHADER_LOC_MAP_OCCLUSION',
    'SHADER_LOC_MAP_PREFILTER',
    'SHADER_LOC_MAP_ROUGHNESS',
    'SHADER_LOC_MATRIX_MODEL',
    'SHADER_LOC_MATRIX_MVP',
    'SHADER_LOC_MATRIX_NORMAL',
    'SHADER_LOC_MATRIX_PROJECTION',
    'SHADER_LOC_MATRIX_VIEW',
    'SHADER_LOC_VECTOR_VIEW',
    'SHADER_LOC_VERTEX_COLOR',
    'SHADER_LOC_VERTEX_NORMAL',
    'SHADER_LOC_VERTEX_POSITION',
    'SHADER_LOC_VERTEX_TANGENT',
    'SHADER_LOC_VERTEX_TEXCOORD01',
    'SHADER_LOC_VERTEX_TEXCOORD02',
    'SHADER_UNIFORM_FLOAT',
    'SHADER_UNIFORM_INT',
    'SHADER_UNIFORM_IVEC2',
    'SHADER_UNIFORM_IVEC3',
    'SHADER_UNIFORM_IVEC4',
    'SHADER_UNIFORM_SAMPLER2D',
    'SHADER_UNIFORM_VEC2',
    'SHADER_UNIFORM_VEC3',
    'SHADER_UNIFORM_VEC4',
    'TEXTURE_FILTER_ANISOTROPIC_16X',
    'TEXTURE_FILTER_ANISOTROPIC_4X',
    'TEXTURE_FILTER_ANISOTROPIC_8X',
    'TEXTURE_FILTER_BILINEAR',
    'TEXTURE_FILTER_POINT',
    'TEXTURE_FILTER_TRILINEAR',
    'TEXTURE_WRAP_CLAMP',
    'TEXTURE_WRAP_MIRROR_CLAMP',
    'TEXTURE_WRAP_MIRROR_REPEAT',
    'TEXTURE_WRAP_REPEAT',

    # defines
    'BEIGE',
    'BLACK',
    'BLANK',
    'BLUE',
    'BROWN',
    'DARKBLUE',
    'DARKBROWN',
    'DARKGRAY',
    'DARKGREEN',
    'DARKPURPLE',
    'DEG2RAD',
    'EPSILON',
    'GOLD',
    'GRAY',
    'GREEN',
    'LIGHTGRAY',
    'LIME',
    'MAGENTA',
    'MAROON',
    'MATERIAL_MAP_DIFFUSE',
    'MATERIAL_MAP_SPECULAR',
    'MOUSE_LEFT_BUTTON',
    'MOUSE_MIDDLE_BUTTON',
    'MOUSE_RIGHT_BUTTON',
    'ORANGE',
    'PI',
    'PINK',
    'PURPLE',
    'RAD2DEG',
    'RAYLIB_VERSION',
    'RAYLIB_VERSION_MAJOR',
    'RAYLIB_VERSION_MINOR',
    'RAYLIB_VERSION_PATCH',
    'RAYWHITE',
    'RED',
    'RLGL_VERSION',
    'RL_BLEND_COLOR',
    'RL_BLEND_DST_ALPHA',
    'RL_BLEND_DST_RGB',
    'RL_BLEND_EQUATION',
    'RL_BLEND_EQUATION_ALPHA',
    'RL_BLEND_EQUATION_RGB',
    'RL_BLEND_SRC_ALPHA',
    'RL_BLEND_SRC_RGB',
    'RL_COMPUTE_SHADER',
    'RL_CONSTANT_ALPHA',
    'RL_CONSTANT_COLOR',
    'RL_CULL_DISTANCE_FAR',
    'RL_CULL_DISTANCE_NEAR',
    'RL_DEFAULT_BATCH_BUFFERS',
    'RL_DEFAULT_BATCH_BUFFER_ELEMENTS',
    'RL_DEFAULT_BATCH_DRAWCALLS',
    'RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS',
    'RL_DST_ALPHA',
    'RL_DST_COLOR',
    'RL_DYNAMIC_COPY',
    'RL_DYNAMIC_DRAW',
    'RL_DYNAMIC_READ',
    'RL_FLOAT',
    'RL_FRAGMENT_SHADER',
    'RL_FUNC_ADD',
    'RL_FUNC_REVERSE_SUBTRACT',
    'RL_FUNC_SUBTRACT',
    'RL_LINES',
    'RL_MAX',
    'RL_MAX_MATRIX_STACK_SIZE',
    'RL_MAX_SHADER_LOCATIONS',
    'RL_MIN',
    'RL_MODELVIEW',
    'RL_ONE',
    'RL_ONE_MINUS_CONSTANT_ALPHA',
    'RL_ONE_MINUS_CONSTANT_COLOR',
    'RL_ONE_MINUS_DST_ALPHA',
    'RL_ONE_MINUS_DST_COLOR',
    'RL_ONE_MINUS_SRC_ALPHA',
    'RL_ONE_MINUS_SRC_COLOR',
    'RL_PROJECTION',
    'RL_QUADS',
    'RL_SHADER_LOC_MAP_DIFFUSE',
    'RL_SHADER_LOC_MAP_SPECULAR',
    'RL_SRC_ALPHA',
    'RL_SRC_ALPHA_SATURATE',
    'RL_SRC_COLOR',
    'RL_STATIC_COPY',
    'RL_STATIC_DRAW',
    'RL_STATIC_READ',
    'RL_STREAM_COPY',
    'RL_STREAM_DRAW',
    'RL_STREAM_READ',
    'RL_TEXTURE',
    'RL_TEXTURE_FILTER_ANISOTROPIC',
    'RL_TEXTURE_FILTER_LINEAR',
    'RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST',
    'RL_TEXTURE_FILTER_MIP_LINEAR',
    'RL_TEXTURE_FILTER_MIP_NEAREST',
    'RL_TEXTURE_FILTER_NEAREST',
    'RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR',
    'RL_TEXTURE_MAG_FILTER',
    'RL_TEXTURE_MIN_FILTER',
    'RL_TEXTURE_MIPMAP_BIAS_RATIO',
    'RL_TEXTURE_WRAP_CLAMP',
    'RL_TEXTURE_WRAP_MIRROR_CLAMP',
    'RL_TEXTURE_WRAP_MIRROR_REPEAT',
    'RL_TEXTURE_WRAP_REPEAT',
    'RL_TEXTURE_WRAP_S',
    'RL_TEXTURE_WRAP_T',
    'RL_TRIANGLES',
    'RL_UNSIGNED_BYTE',
    'RL_VERTEX_SHADER',
    'RL_ZERO',
    'SHADER_LOC_MAP_DIFFUSE',
    'SHADER_LOC_MAP_SPECULAR',
    'SKYBLUE',
    'VIOLET',
    'WHITE',
    'YELLOW',

    # callbacks
    'AudioCallback',
    'LoadFileDataCallback',
    'LoadFileTextCallback',
    'SaveFileDataCallback',
    'SaveFileTextCallback',
    'TraceLogCallback',

    # functions
    'attach_audio_mixed_processor',
    'attach_audio_stream_processor',
    'begin_blend_mode',
    'begin_drawing',
    'begin_mode2d',
    'begin_mode3d',
    'begin_scissor_mode',
    'begin_shader_mode',
    'begin_texture_mode',
    'begin_vr_stereo_mode',
    'change_directory',
    'check_collision_box_sphere',
    'check_collision_boxes',
    'check_collision_circle_rec',
    'check_collision_circles',
    'check_collision_lines',
    'check_collision_point_circle',
    'check_collision_point_line',
    'check_collision_point_poly',
    'check_collision_point_rec',
    'check_collision_point_triangle',
    'check_collision_recs',
    'check_collision_spheres',
    'clamp',
    'clear_background',
    'clear_window_state',
    'close_audio_device',
    'close_window',
    'codepoint_to_utf8',
    'color_alpha',
    'color_alpha_blend',
    'color_brightness',
    'color_contrast',
    'color_from_hsv',
    'color_from_normalized',
    'color_normalize',
    'color_tint',
    'color_to_hsv',
    'color_to_int',
    'compress_data',
    'decode_data_base64',
    'decompress_data',
    'detach_audio_mixed_processor',
    'detach_audio_stream_processor',
    'directory_exists',
    'disable_cursor',
    'disable_event_waiting',
    'draw_billboard',
    'draw_billboard_pro',
    'draw_billboard_rec',
    'draw_bounding_box',
    'draw_capsule',
    'draw_capsule_wires',
    'draw_circle',
    'draw_circle3d',
    'draw_circle_gradient',
    'draw_circle_lines',
    'draw_circle_lines_v',
    'draw_circle_sector',
    'draw_circle_sector_lines',
    'draw_circle_v',
    'draw_cube',
    'draw_cube_v',
    'draw_cube_wires',
    'draw_cube_wires_v',
    'draw_cylinder',
    'draw_cylinder_ex',
    'draw_cylinder_wires',
    'draw_cylinder_wires_ex',
    'draw_ellipse',
    'draw_ellipse_lines',
    'draw_fps',
    'draw_grid',
    'draw_line',
    'draw_line3d',
    'draw_line_bezier',
    'draw_line_ex',
    'draw_line_strip',
    'draw_line_v',
    'draw_mesh',
    'draw_mesh_instanced',
    'draw_model',
    'draw_model_ex',
    'draw_model_wires',
    'draw_model_wires_ex',
    'draw_pixel',
    'draw_pixel_v',
    'draw_plane',
    'draw_point3d',
    'draw_poly',
    'draw_poly_lines',
    'draw_poly_lines_ex',
    'draw_ray',
    'draw_rectangle',
    'draw_rectangle_gradient_ex',
    'draw_rectangle_gradient_h',
    'draw_rectangle_gradient_v',
    'draw_rectangle_lines',
    'draw_rectangle_lines_ex',
    'draw_rectangle_pro',
    'draw_rectangle_rec',
    'draw_rectangle_rounded',
    'draw_rectangle_rounded_lines',
    'draw_rectangle_v',
    'draw_ring',
    'draw_ring_lines',
    'draw_sphere',
    'draw_sphere_ex',
    'draw_sphere_wires',
    'draw_spline_basis',
    'draw_spline_bezier_cubic',
    'draw_spline_bezier_quadratic',
    'draw_spline_catmull_rom',
    'draw_spline_linear',
    'draw_spline_segment_basis',
    'draw_spline_segment_bezier_cubic',
    'draw_spline_segment_bezier_quadratic',
    'draw_spline_segment_catmull_rom',
    'draw_spline_segment_linear',
    'draw_text',
    'draw_text_codepoint',
    'draw_text_codepoints',
    'draw_text_ex',
    'draw_text_pro',
    'draw_texture',
    'draw_texture_ex',
    'draw_texture_npatch',
    'draw_texture_pro',
    'draw_texture_rec',
    'draw_texture_v',
    'draw_triangle',
    'draw_triangle3d',
    'draw_triangle_fan',
    'draw_triangle_lines',
    'draw_triangle_strip',
    'draw_triangle_strip3d',
    'enable_cursor',
    'enable_event_waiting',
    'encode_data_base64',
    'end_blend_mode',
    'end_drawing',
    'end_mode2d',
    'end_mode3d',
    'end_scissor_mode',
    'end_shader_mode',
    'end_texture_mode',
    'end_vr_stereo_mode',
    'export_automation_event_list',
    'export_data_as_code',
    'export_font_as_code',
    'export_image',
    'export_image_as_code',
    'export_image_to_memory',
    'export_mesh',
    'export_wave',
    'export_wave_as_code',
    'fade',
    'file_exists',
    'float_equals',
    'gen_image_cellular',
    'gen_image_checked',
    'gen_image_color',
    'gen_image_font_atlas',
    'gen_image_gradient_linear',
    'gen_image_gradient_radial',
    'gen_image_gradient_square',
    'gen_image_perlin_noise',
    'gen_image_text',
    'gen_image_white_noise',
    'gen_mesh_cone',
    'gen_mesh_cube',
    'gen_mesh_cubicmap',
    'gen_mesh_cylinder',
    'gen_mesh_heightmap',
    'gen_mesh_hemi_sphere',
    'gen_mesh_knot',
    'gen_mesh_plane',
    'gen_mesh_poly',
    'gen_mesh_sphere',
    'gen_mesh_tangents',
    'gen_mesh_torus',
    'gen_texture_mipmaps',
    'get_application_directory',
    'get_camera_matrix',
    'get_camera_matrix2d',
    'get_char_pressed',
    'get_clipboard_text',
    'get_codepoint',
    'get_codepoint_count',
    'get_codepoint_next',
    'get_codepoint_previous',
    'get_collision_rec',
    'get_color',
    'get_current_monitor',
    'get_directory_path',
    'get_file_extension',
    'get_file_length',
    'get_file_mod_time',
    'get_file_name',
    'get_file_name_without_ext',
    'get_font_default',
    'get_fps',
    'get_frame_time',
    'get_gamepad_axis_count',
    'get_gamepad_axis_movement',
    'get_gamepad_button_pressed',
    'get_gamepad_name',
    'get_gesture_detected',
    'get_gesture_drag_angle',
    'get_gesture_drag_vector',
    'get_gesture_hold_duration',
    'get_gesture_pinch_angle',
    'get_gesture_pinch_vector',
    'get_glyph_atlas_rec',
    'get_glyph_index',
    'get_glyph_info',
    'get_image_alpha_border',
    'get_image_color',
    'get_key_pressed',
    'get_master_volume',
    'get_mesh_bounding_box',
    'get_model_bounding_box',
    'get_monitor_count',
    'get_monitor_height',
    'get_monitor_name',
    'get_monitor_physical_height',
    'get_monitor_physical_width',
    'get_monitor_position',
    'get_monitor_refresh_rate',
    'get_monitor_width',
    'get_mouse_delta',
    'get_mouse_position',
    'get_mouse_ray',
    'get_mouse_wheel_move',
    'get_mouse_wheel_move_v',
    'get_mouse_x',
    'get_mouse_y',
    'get_music_time_length',
    'get_music_time_played',
    'get_pixel_color',
    'get_pixel_data_size',
    'get_prev_directory_path',
    'get_random_value',
    'get_ray_collision_box',
    'get_ray_collision_mesh',
    'get_ray_collision_quad',
    'get_ray_collision_sphere',
    'get_ray_collision_triangle',
    'get_render_height',
    'get_render_width',
    'get_screen_height',
    'get_screen_to_world2d',
    'get_screen_width',
    'get_shader_location',
    'get_shader_location_attrib',
    'get_spline_point_basis',
    'get_spline_point_bezier_cubic',
    'get_spline_point_bezier_quad',
    'get_spline_point_catmull_rom',
    'get_spline_point_linear',
    'get_time',
    'get_touch_point_count',
    'get_touch_point_id',
    'get_touch_position',
    'get_touch_x',
    'get_touch_y',
    'get_window_handle',
    'get_window_position',
    'get_window_scale_dpi',
    'get_working_directory',
    'get_world_to_screen',
    'get_world_to_screen2d',
    'get_world_to_screen_ex',
    'hide_cursor',
    'image_alpha_clear',
    'image_alpha_crop',
    'image_alpha_mask',
    'image_alpha_premultiply',
    'image_blur_gaussian',
    'image_clear_background',
    'image_color_brightness',
    'image_color_contrast',
    'image_color_grayscale',
    'image_color_invert',
    'image_color_replace',
    'image_color_tint',
    'image_copy',
    'image_crop',
    'image_dither',
    'image_draw',
    'image_draw_circle',
    'image_draw_circle_lines',
    'image_draw_circle_lines_v',
    'image_draw_circle_v',
    'image_draw_line',
    'image_draw_line_v',
    'image_draw_pixel',
    'image_draw_pixel_v',
    'image_draw_rectangle',
    'image_draw_rectangle_lines',
    'image_draw_rectangle_rec',
    'image_draw_rectangle_v',
    'image_draw_text',
    'image_draw_text_ex',
    'image_flip_horizontal',
    'image_flip_vertical',
    'image_format',
    'image_from_image',
    'image_mipmaps',
    'image_resize',
    'image_resize_canvas',
    'image_resize_nn',
    'image_rotate',
    'image_rotate_ccw',
    'image_rotate_cw',
    'image_text',
    'image_text_ex',
    'image_to_pot',
    'init_audio_device',
    'init_window',
    'is_audio_device_ready',
    'is_audio_stream_playing',
    'is_audio_stream_processed',
    'is_audio_stream_ready',
    'is_cursor_hidden',
    'is_cursor_on_screen',
    'is_file_dropped',
    'is_file_extension',
    'is_font_ready',
    'is_gamepad_available',
    'is_gamepad_button_down',
    'is_gamepad_button_pressed',
    'is_gamepad_button_released',
    'is_gamepad_button_up',
    'is_gesture_detected',
    'is_image_ready',
    'is_key_down',
    'is_key_pressed',
    'is_key_pressed_repeat',
    'is_key_released',
    'is_key_up',
    'is_material_ready',
    'is_model_animation_valid',
    'is_model_ready',
    'is_mouse_button_down',
    'is_mouse_button_pressed',
    'is_mouse_button_released',
    'is_mouse_button_up',
    'is_music_ready',
    'is_music_stream_playing',
    'is_path_file',
    'is_render_texture_ready',
    'is_shader_ready',
    'is_sound_playing',
    'is_sound_ready',
    'is_texture_ready',
    'is_wave_ready',
    'is_window_focused',
    'is_window_fullscreen',
    'is_window_hidden',
    'is_window_maximized',
    'is_window_minimized',
    'is_window_ready',
    'is_window_resized',
    'is_window_state',
    'lerp',
    'load_audio_stream',
    'load_automation_event_list',
    'load_codepoints',
    'load_directory_files',
    'load_directory_files_ex',
    'load_dropped_files',
    'load_file_data',
    'load_file_text',
    'load_font',
    'load_font_data',
    'load_font_ex',
    'load_font_from_image',
    'load_font_from_memory',
    'load_image',
    'load_image_anim',
    'load_image_colors',
    'load_image_from_memory',
    'load_image_from_screen',
    'load_image_from_texture',
    'load_image_palette',
    'load_image_raw',
    'load_image_svg',
    'load_material_default',
    'load_materials',
    'load_model',
    'load_model_animations',
    'load_model_from_mesh',
    'load_music_stream',
    'load_music_stream_from_memory',
    'load_random_sequence',
    'load_render_texture',
    'load_shader',
    'load_shader_from_memory',
    'load_sound',
    'load_sound_alias',
    'load_sound_from_wave',
    'load_texture',
    'load_texture_cubemap',
    'load_texture_from_image',
    'load_utf8',
    'load_vr_stereo_config',
    'load_wave',
    'load_wave_from_memory',
    'load_wave_samples',
    'matrix_add',
    'matrix_determinant',
    'matrix_frustum',
    'matrix_identity',
    'matrix_invert',
    'matrix_look_at',
    'matrix_multiply',
    'matrix_ortho',
    'matrix_perspective',
    'matrix_rotate',
    'matrix_rotate_x',
    'matrix_rotate_xyz',
    'matrix_rotate_y',
    'matrix_rotate_z',
    'matrix_rotate_zyx',
    'matrix_scale',
    'matrix_subtract',
    'matrix_to_float_v',
    'matrix_trace',
    'matrix_translate',
    'matrix_transpose',
    'maximize_window',
    'measure_text',
    'measure_text_ex',
    'mem_alloc',
    'mem_free',
    'mem_realloc',
    'minimize_window',
    'normalize',
    'open_url',
    'pause_audio_stream',
    'pause_music_stream',
    'pause_sound',
    'play_audio_stream',
    'play_automation_event',
    'play_music_stream',
    'play_sound',
    'poll_input_events',
    'quaternion_add',
    'quaternion_add_value',
    'quaternion_divide',
    'quaternion_equals',
    'quaternion_from_axis_angle',
    'quaternion_from_euler',
    'quaternion_from_matrix',
    'quaternion_from_vector3_to_vector3',
    'quaternion_identity',
    'quaternion_invert',
    'quaternion_length',
    'quaternion_lerp',
    'quaternion_multiply',
    'quaternion_nlerp',
    'quaternion_normalize',
    'quaternion_scale',
    'quaternion_slerp',
    'quaternion_subtract',
    'quaternion_subtract_value',
    'quaternion_to_axis_angle',
    'quaternion_to_euler',
    'quaternion_to_matrix',
    'quaternion_transform',
    'remap',
    'restore_window',
    'resume_audio_stream',
    'resume_music_stream',
    'resume_sound',
    'rl_active_draw_buffers',
    'rl_active_texture_slot',
    'rl_begin',
    'rl_bind_image_texture',
    'rl_bind_shader_buffer',
    'rl_blit_framebuffer',
    'rl_check_errors',
    'rl_check_render_batch_limit',
    'rl_clear_color',
    'rl_clear_screen_buffers',
    'rl_color_3ff',
    'rl_color_4_uub',
    'rl_color_4ff',
    'rl_compile_shader',
    'rl_compute_shader_dispatch',
    'rl_copy_shader_buffer',
    'rl_cubemap_parameters',
    'rl_disable_backface_culling',
    'rl_disable_color_blend',
    'rl_disable_depth_mask',
    'rl_disable_depth_test',
    'rl_disable_framebuffer',
    'rl_disable_scissor_test',
    'rl_disable_shader',
    'rl_disable_smooth_lines',
    'rl_disable_stereo_render',
    'rl_disable_texture',
    'rl_disable_texture_cubemap',
    'rl_disable_vertex_array',
    'rl_disable_vertex_attribute',
    'rl_disable_vertex_buffer',
    'rl_disable_vertex_buffer_element',
    'rl_disable_wire_mode',
    'rl_draw_render_batch',
    'rl_draw_render_batch_active',
    'rl_draw_vertex_array',
    'rl_draw_vertex_array_elements',
    'rl_draw_vertex_array_elements_instanced',
    'rl_draw_vertex_array_instanced',
    'rl_enable_backface_culling',
    'rl_enable_color_blend',
    'rl_enable_depth_mask',
    'rl_enable_depth_test',
    'rl_enable_framebuffer',
    'rl_enable_point_mode',
    'rl_enable_scissor_test',
    'rl_enable_shader',
    'rl_enable_smooth_lines',
    'rl_enable_stereo_render',
    'rl_enable_texture',
    'rl_enable_texture_cubemap',
    'rl_enable_vertex_array',
    'rl_enable_vertex_attribute',
    'rl_enable_vertex_buffer',
    'rl_enable_vertex_buffer_element',
    'rl_enable_wire_mode',
    'rl_end',
    'rl_framebuffer_attach',
    'rl_framebuffer_complete',
    'rl_frustum',
    'rl_gen_texture_mipmaps',
    'rl_get_framebuffer_height',
    'rl_get_framebuffer_width',
    'rl_get_gl_texture_formats',
    'rl_get_line_width',
    'rl_get_location_attrib',
    'rl_get_location_uniform',
    'rl_get_matrix_modelview',
    'rl_get_matrix_projection',
    'rl_get_matrix_projection_stereo',
    'rl_get_matrix_transform',
    'rl_get_matrix_view_offset_stereo',
    'rl_get_pixel_format_name',
    'rl_get_shader_buffer_size',
    'rl_get_shader_id_default',
    'rl_get_shader_locs_default',
    'rl_get_texture_id_default',
    'rl_get_version',
    'rl_is_stereo_render_enabled',
    'rl_load_compute_shader_program',
    'rl_load_draw_cube',
    'rl_load_draw_quad',
    'rl_load_extensions',
    'rl_load_framebuffer',
    'rl_load_identity',
    'rl_load_render_batch',
    'rl_load_shader_buffer',
    'rl_load_shader_code',
    'rl_load_shader_program',
    'rl_load_texture',
    'rl_load_texture_cubemap',
    'rl_load_texture_depth',
    'rl_load_vertex_array',
    'rl_load_vertex_buffer',
    'rl_load_vertex_buffer_element',
    'rl_matrix_mode',
    'rl_mult_matrixf',
    'rl_normal_3ff',
    'rl_ortho',
    'rl_pop_matrix',
    'rl_push_matrix',
    'rl_read_screen_pixels',
    'rl_read_shader_buffer',
    'rl_read_texture_pixels',
    'rl_rotatef',
    'rl_scalef',
    'rl_scissor',
    'rl_set_blend_factors',
    'rl_set_blend_factors_separate',
    'rl_set_blend_mode',
    'rl_set_cull_face',
    'rl_set_framebuffer_height',
    'rl_set_framebuffer_width',
    'rl_set_line_width',
    'rl_set_matrix_modelview',
    'rl_set_matrix_projection',
    'rl_set_matrix_projection_stereo',
    'rl_set_matrix_view_offset_stereo',
    'rl_set_render_batch_active',
    'rl_set_shader',
    'rl_set_texture',
    'rl_set_uniform',
    'rl_set_uniform_matrix',
    'rl_set_uniform_sampler',
    'rl_set_vertex_attribute',
    'rl_set_vertex_attribute_default',
    'rl_set_vertex_attribute_divisor',
    'rl_tex_coord_2ff',
    'rl_texture_parameters',
    'rl_translatef',
    'rl_unload_framebuffer',
    'rl_unload_render_batch',
    'rl_unload_shader_buffer',
    'rl_unload_shader_program',
    'rl_unload_texture',
    'rl_unload_vertex_array',
    'rl_unload_vertex_buffer',
    'rl_update_shader_buffer',
    'rl_update_texture',
    'rl_update_vertex_buffer',
    'rl_update_vertex_buffer_elements',
    'rl_vertex_2ff',
    'rl_vertex_2ii',
    'rl_vertex_3ff',
    'rl_viewport',
    'rlgl_close',
    'rlgl_init',
    'save_file_data',
    'save_file_text',
    'seek_music_stream',
    'set_audio_stream_buffer_size_default',
    'set_audio_stream_callback',
    'set_audio_stream_pan',
    'set_audio_stream_pitch',
    'set_audio_stream_volume',
    'set_automation_event_base_frame',
    'set_automation_event_list',
    'set_clipboard_text',
    'set_config_flags',
    'set_exit_key',
    'set_gamepad_mappings',
    'set_gestures_enabled',
    'set_load_file_data_callback',
    'set_load_file_text_callback',
    'set_master_volume',
    'set_material_texture',
    'set_model_mesh_material',
    'set_mouse_cursor',
    'set_mouse_offset',
    'set_mouse_position',
    'set_mouse_scale',
    'set_music_pan',
    'set_music_pitch',
    'set_music_volume',
    'set_pixel_color',
    'set_random_seed',
    'set_save_file_data_callback',
    'set_save_file_text_callback',
    'set_shader_value',
    'set_shader_value_matrix',
    'set_shader_value_texture',
    'set_shader_value_v',
    'set_shapes_texture',
    'set_sound_pan',
    'set_sound_pitch',
    'set_sound_volume',
    'set_target_fps',
    'set_text_line_spacing',
    'set_texture_filter',
    'set_texture_wrap',
    'set_trace_log_callback',
    'set_trace_log_level',
    'set_window_focused',
    'set_window_icon',
    'set_window_icons',
    'set_window_max_size',
    'set_window_min_size',
    'set_window_monitor',
    'set_window_opacity',
    'set_window_position',
    'set_window_size',
    'set_window_state',
    'set_window_title',
    'show_cursor',
    'start_automation_event_recording',
    'stop_audio_stream',
    'stop_automation_event_recording',
    'stop_music_stream',
    'stop_sound',
    'swap_screen_buffer',
    'take_screenshot',
    'text_append',
    'text_copy',
    'text_find_index',
    'text_format',
    'text_insert',
    'text_is_equal',
    'text_join',
    'text_length',
    'text_replace',
    'text_split',
    'text_subtext',
    'text_to_integer',
    'text_to_lower',
    'text_to_pascal',
    'text_to_upper',
    'toggle_borderless_windowed',
    'toggle_fullscreen',
    'trace_log',
    'unload_audio_stream',
    'unload_automation_event_list',
    'unload_codepoints',
    'unload_directory_files',
    'unload_dropped_files',
    'unload_file_data',
    'unload_file_text',
    'unload_font',
    'unload_font_data',
    'unload_image',
    'unload_image_colors',
    'unload_image_palette',
    'unload_material',
    'unload_mesh',
    'unload_model',
    'unload_model_animation',
    'unload_model_animations',
    'unload_music_stream',
    'unload_random_sequence',
    'unload_render_texture',
    'unload_shader',
    'unload_sound',
    'unload_sound_alias',
    'unload_texture',
    'unload_utf8',
    'unload_vr_stereo_config',
    'unload_wave',
    'unload_wave_samples',
    'update_audio_stream',
    'update_camera',
    'update_camera_pro',
    'update_mesh_buffer',
    'update_model_animation',
    'update_music_stream',
    'update_sound',
    'update_texture',
    'update_texture_rec',
    'upload_mesh',
    'vector2_add',
    'vector2_add_value',
    'vector2_angle',
    'vector2_clamp',
    'vector2_clamp_value',
    'vector2_distance',
    'vector2_distance_sqr',
    'vector2_divide',
    'vector2_dot_product',
    'vector2_equals',
    'vector2_invert',
    'vector2_length',
    'vector2_length_sqr',
    'vector2_lerp',
    'vector2_line_angle',
    'vector2_move_towards',
    'vector2_multiply',
    'vector2_negate',
    'vector2_normalize',
    'vector2_one',
    'vector2_reflect',
    'vector2_rotate',
    'vector2_scale',
    'vector2_subtract',
    'vector2_subtract_value',
    'vector2_transform',
    'vector2_zero',
    'vector3_add',
    'vector3_add_value',
    'vector3_angle',
    'vector3_barycenter',
    'vector3_clamp',
    'vector3_clamp_value',
    'vector3_cross_product',
    'vector3_distance',
    'vector3_distance_sqr',
    'vector3_divide',
    'vector3_dot_product',
    'vector3_equals',
    'vector3_invert',
    'vector3_length',
    'vector3_length_sqr',
    'vector3_lerp',
    'vector3_max',
    'vector3_min',
    'vector3_multiply',
    'vector3_negate',
    'vector3_normalize',
    'vector3_one',
    'vector3_ortho_normalize',
    'vector3_perpendicular',
    'vector3_project',
    'vector3_reflect',
    'vector3_refract',
    'vector3_reject',
    'vector3_rotate_by_axis_angle',
    'vector3_rotate_by_quaternion',
    'vector3_scale',
    'vector3_subtract',
    'vector3_subtract_value',
    'vector3_to_float_v',
    'vector3_transform',
    'vector3_unproject',
    'vector3_zero',
    'wait_time',
    'wave_copy',
    'wave_crop',
    'wave_format',
    'window_should_close',
    'wrap',

    # contexts
    'blend_mode',
    'drawing',
    'mode2d',
    'mode3d',
    'rl_backface_culling',
    'rl_color_blend',
    'rl_depth_mask',
    'rl_depth_test',
    'rl_framebuffer',
    'rl_gl',
    'rl_scissor_test',
    'rl_shader',
    'rl_smooth_lines',
    'rl_stereo_render',
    'rl_texture',
    'rl_texture_cubemap',
    'rl_vertex_array',
    'rl_vertex_attribute',
    'rl_vertex_buffer',
    'rl_vertex_buffer_element',
    'rl_wire_mode',
    'scissor_mode',
    'shader_mode',
    'texture_mode',
    'vr_stereo_mode',
]

# endregion (exports)

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

_dotraylib_used = False
_dotraylib_loadinfo = []

def _check_dotraylib(lib, platform, bitness, default=None):
    """Checks for the .raylib file in the current working directory

    The presence of this file allows the loading of binaries other than those
    provided by raylib. Example of .raylib file contents:

    ```json
    {
        "raylib": {
            "win32": {
                "32bit": "path/to/raylib/filename.dll",
                "64bit": "path/to/raylib/filename.dll"
            },
            "linux": {
                "32bit": "path/to/raylib/filename.so",
                "64bit": "path/to/raylib/filename.so"
            },
            "darwin": {
                "64bit": "path/to/raylib/filename.dylib"
            }
        }
    }
    ```
    """

    global _dotraylib_loadinfo, _dotraylib_used
    _dotraylib = os.path.join(os.getcwd(), '.raylib')

    if os.path.exists(_dotraylib) and os.path.isfile(_dotraylib):
        _dotraylib_used = True

        with open(_dotraylib, 'r', encoding='utf8') as fp:
            try:
                _dotraylib_config = json.load(fp)
                _libpath = _dotraylib_config.get(lib, {}).get(platform, {}).get(bitness, default)
                _dotraylib_loadinfo.append("INFO: .raylib loaded successfully")
                return _libpath

            except json.JSONDecodeError:
                _dotraylib_loadinfo.append("ERROR: Could not decode .raylib file")
    else:
        _dotraylib_loadinfo.append("INFO: .raylib file not available")
    return default


def _load_library(lib_name, is_extension, basedir, **bin_fnames):
    global _dotraylib_loadinfo, _dotraylib_used

    _lib_fname = {
        'win32': bin_fnames.get('win32', 'no_file_specified.dll'),
        'linux': bin_fnames.get('linux', 'no_file_specified.so'),
        'darwin': bin_fnames.get('darwin', 'no_file_specified.dylib')
    }

    _dotraylib_used = False
    _lib_platform = sys.platform

    if _lib_platform == 'win32':
        _bitness = platform.architecture()[0]
    elif _lib_platform == 'darwin':
        _bitness = '64bit'
    else:
        _bitness = '64bit' if sys.maxsize > 2 ** 32 else '32bit'

    if is_extension:
        _lib_default = None
    else:
        _lib_default = os.path.join(*(d.format(os.path.dirname(__file__)) for d in basedir), _bitness, _lib_fname[_lib_platform])

    _lib_default = _check_dotraylib(lib_name, _lib_platform, _bitness, _lib_default)

    if not _lib_default:
        if is_extension:
            _dotraylib_loadinfo.append("ERROR: Platform ({}), bitness ({}) or valid filename not specified in .raylib file for {} extension".format(lib_name, _lib_platform, _bitness))
        else:
            _dotraylib_loadinfo.append("ERROR: Platform ({}), bitness ({}) or valid filename not specified in .raylib file for {}".format(lib_name, _lib_platform, _bitness))

        _lib_fname_abspath = ''
        _ok = False
    else:
        _lib_fname_abspath = os.path.normcase(os.path.normpath(_lib_default))
        _ok = True

    _cwd_info = os.getcwd()
    _load_info = "\n            ".join(_dotraylib_loadinfo) if _dotraylib_loadinfo else "does not apply"

    print(
        """Library loading info:
        platform: {}
        bitness: {}
        current working dir: {}
        .raylib used: {}
        .raylib status: {}
        absolute path: {}
        is extension: {}
        path exists: {}
        path leads to a file: {}
        """.format(
            _lib_platform,
            _bitness,
            _cwd_info,
            'yes' if _dotraylib_used else 'no',
            _load_info,
            _lib_fname_abspath,
            'yes' if is_extension else 'no',
            'yes' if os.path.exists(_lib_fname_abspath) else 'no',
            'yes' if os.path.isfile(_lib_fname_abspath) else 'no'
        )
    )

    if not _ok:
        print("Failed to load Shared library", lib_name)
        sys.exit(1)

    lib_ = None
    if _lib_platform == 'win32':

        try:
            lib_ = CDLLEx(_lib_fname_abspath, LOAD_WITH_ALTERED_SEARCH_PATH)
        except OSError as e:
            print("Unable to load {}: {}".format(_lib_fname[_lib_platform], e.args))
            lib_ = None
    else:
        lib_ = CDLL(_lib_fname_abspath)

    if lib_ is None:
        print("Failed to load Shared library", lib_name)
        sys.exit(1)
    else:
        print("Shared library loaded succesfully", lib_)

    return lib_


rlapi = _load_library('raylib', False, ['{}/bin'], win32='raylib.dll', linux='libraylib.so.5.0.0', darwin='libraylib.5.0.0.dylib')

# endregion (library loading)

print('\nraylib-py v{RAYLIB_VERSION} is initializing.\n')

# region GLOBALS

# Used to store temporarily out param argument passed to functions
# so that the values can be retrieved following the call
_in_out = []

# TypeVar for generic Array class
_T = TypeVar('_T')

RE_C_FMT_STRING = re.compile(r"%(?P<flags>[ \-+#0])?(?P<width>\d+|\*)?(?P<precision>\.[*\d])?(?P<length>hh|h|ll|l|j|z|t|L)?(?P<spec>[diuoxXfFeEgGaAcspn])")

FMT_SPEC_TABLE = {
    'd': {'*': c_int,          'hh': c_byte,   'h': c_short,          'l': c_long,          'll': c_longlong,          'j': None, 'z': c_size_t,          't': None, 'L': None},
    'i': {'*': c_int,          'hh': c_byte,   'h': c_short,          'l': c_long,          'll': c_longlong,          'j': None, 'z': c_size_t,          't': None, 'L': None},
    'u': {'*': c_uint,         'hh': c_ubyte,  'h': c_ushort,         'l': c_ulong,         'll': c_ulonglong,         'j': None, 'z': c_size_t,          't': None, 'L': None},
    'o': {'*': c_uint,         'hh': c_ubyte,  'h': c_ushort,         'l': c_ulong,         'll': c_ulonglong,         'j': None, 'z': c_size_t,          't': None, 'L': None},
    'x': {'*': c_uint,         'hh': c_ubyte,  'h': c_ushort,         'l': c_ulong,         'll': c_ulonglong,         'j': None, 'z': c_size_t,          't': None, 'L': None},
    'X': {'*': c_uint,         'hh': c_ubyte,  'h': c_ushort,         'l': c_ulong,         'll': c_ulonglong,         'j': None, 'z': c_size_t,          't': None, 'L': None},
    'f': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'F': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'e': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'E': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'g': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'G': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'a': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'A': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'c': {'*': c_int,          'hh': None,     'h': None,             'l': c_wchar,         'll': None,                'j': None, 'z': None,              't': None, 'L': None},
    's': {'*': c_char_p,       'hh': None,     'h': None,             'l': c_wchar_p,       'll': None,                'j': None, 'z': None,              't': None, 'L': None},
    'p': {'*': c_void_p,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': None},
    'n': {'*': POINTER(c_int), 'hh': c_char_p, 'h': POINTER(c_short), 'l': POINTER(c_long), 'll': POINTER(c_longlong), 'j': None, 'z': POINTER(c_size_t), 't': None, 'L': None},
}

_fmt_cache = {}

# Vector component swizzling helppers
RE_VEC2_GET_SWZL = re.compile(r'[xy]{,4}')
RE_VEC3_GET_SWZL = re.compile(r'[xyz]{,4}')
RE_VEC4_GET_SWZL = re.compile(r'[xyzw]{,4}')
RE_RGBA_GET_SWZL = re.compile(r'[rgba]{1,4}')
RE_RECT_GET_SWZL = re.compile(r'(width|height|[xywhcmrb]{,4})')

RE_VEC2_SET_SWZL = re.compile(r'[xy]{,2}')
RE_VEC3_SET_SWZL = re.compile(r'[xyz]{,3}')
RE_VEC4_SET_SWZL = re.compile(r'[xyzw]{,4}')
RE_RGBA_SET_SWZL = re.compile(r'[rgba]{1,4}')
RE_RECT_SET_SWZL = re.compile(r'(width|height|[xywhcmrb]{,4})')
# endregion (globals)

# region UTILS

# region INTERNAL


def _extract_argtypes(format_string):
    """Generator function to extract all specifiers as ctypes types from the format string
    
    (yielded items are tuples of slice, str and a ctypes type or None)
    """
    # type: (str) -> Iterator[tuple[slice, str, Any]]
    for m in RE_C_FMT_STRING.finditer(format_string):
        spec = m.group('spec')
        length = m.group('length') or '*'
        ctypes_type = FMT_SPEC_TABLE.get(spec, {}).get(length)
        yield slice(*m.span()), m[0], ctypes_type


def _transform_fmt(format_string, *args):
    n = len(args)
    vals = []
    sentinel = object()

    for i, (slc, str_, ctype) in enumerate(_extract_argtypes(format_string[:])):
        try:
            val = ctype(args[i])
        except Exception:
            val = sentinel

        if i >= n or ctype is None or val is sentinel:
            left = format_string[:slc.start]
            right = format_string[slc.stop:]
            middle = '<?fmt?>'
            format_string = left + middle + right
            continue

        vals.append(val)

    return [format_string, *vals]


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
    return Color(_int(r, rng), _int(g, rng), _int(b, rng), _int(q, rng))


def _array_in(sequence, type_ctype=None):
    if isinstance(sequence, BaseArray):
        return sequence
    else:
        return (type_ctype * len(sequence))(*sequence)


def _clear_in_out():
    global _in_out

    _in_out.clear()


def _push_in_out(ctype_pointer_type):
    global _in_out

    _in_out.append(ctype_pointer_type)


def _wrap(api, res_type, *arg_types):
    """Configure the paramters and return types for the wrapped C function and returns it"""
    api.argtypes = arg_types
    api.restype = res_type
    return api

# endregion (internal)


BaseArray = Array

class Array(Generic[_T]):
    """Generic class defined only for type hinting/annotation purposes (e.g. Array[Color])."""
    pass


def clear_format_string_cache():
    global _fmt_cache

    _fmt_cache.clear()


def pop_out_param(default=None):
    """Pops and returns the out param argument passed to the last call, or the default value otherwise"""
    global _in_out

    if len(_in_out):
        return _in_out.pop()
    return default


def float_array(sequence):
    """Factory function to create and return an array of floats"""
    if isinstance(sequence, Array):
        return sequence

    return (Float * len(sequence))(*sequence)


def double_array(sequence):
    """Factory function to create and return an array of doubles"""
    if isinstance(sequence, Array):
        return sequence

    return (Double * len(sequence))(*sequence)


def int_array(sequence):
    """Factory function to create and return an array of signed int numbers"""
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (Int * len(sequence))(*sequence)


def uint_array(sequence):
    """Factory function to create and return an array of unsigned int numbers"""
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (UInt * len(sequence))(*sequence)


def short_array(sequence):
    """Factory function to create and return an array of signed short numbers"""
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (Short * len(sequence))(*sequence)


def ushort_array(sequence):
    """Factory function to create and return an array of unsigned short numbers"""
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (UShort * len(sequence))(*sequence)


def byte_array(sequence):
    """Factory function to create and return an array of signed byte numbers"""
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (Byte * len(sequence))(*sequence)


def ubyte_array(sequence):
    """Factory function to create and return an array of unsigned byte numbers"""
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (UByte * len(sequence))(*sequence)


def string_array(sequence, encoding='utf8', errors='ignore'):
    """Factory function to create and return an array of char * (a char **)"""
    if isinstance(sequence, Array):
        return sequence
    elsequence = [s.encode(encoding, ignore) for s in sequence]

    return (CharPtr * len(sequence))(*sequence)


# endregion (utils)

# region C TYPES


# Type wrapper for `bool`
Bool = c_bool

# Type wrapper for `char`
Char = c_char

# Type wrapper for `char *`
CharPtr = c_char_p

# Type wrapper for `char **`
CharPtrPtr = POINTER(c_char_p)

# Type wrapper for `char[32]`
Char32 = c_char * 32

# Type wrapper for `double`
Double = c_double

# Type wrapper for `float`
Float = c_float

# Type wrapper for `float *`
FloatPtr = POINTER(c_float)

# Type wrapper for `float[16]`
Float16 = c_float * 16

# Type wrapper for `float[2]`
Float2 = c_float * 2

# Type wrapper for `float[3]`
Float3 = c_float * 3

# Type wrapper for `float[4]`
Float4 = c_float * 4

# Type wrapper for `int`
Int = c_int

# Type wrapper for `int *`
IntPtr = POINTER(c_int)

# Type wrapper for `int[4]`
Int4 = c_int * 4

# Type wrapper for `long`
Long = c_long

# Type wrapper for `unsigned char`
UChar = c_ubyte

# Type wrapper for `unsigned char *`
UCharPtr = c_ubyte

# Type wrapper for `unsigned int`
UInt = c_uint

# Type wrapper for `unsigned int *`
UIntPtr = POINTER(c_uint)

# Type wrapper for `unsigned int[4]`
UInt4 = c_uint * 4

# Type wrapper for `unsigned short *`
UShortPtr = POINTER(c_ushort)

# Type wrapper for `void *`
VoidPtr = c_void_p

# endregion (c types)

# region ENUMERATIONS

# rlapi::raylib
# ------------------------------------------------------------------------------

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

    FLAG_BORDERLESS_WINDOWED_MODE = 32768
    """Set to run program in borderless windowed mode"""

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
FLAG_BORDERLESS_WINDOWED_MODE = ConfigFlags.FLAG_BORDERLESS_WINDOWED_MODE
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
    """Mouse button forward (advanced mouse device)"""

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
    """The omnidirectional resize/move cursor shape"""

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

    PIXELFORMAT_UNCOMPRESSED_R16 = 11
    """16 bpp (1 channel - half float)"""

    PIXELFORMAT_UNCOMPRESSED_R16G16B16 = 12
    """16*3 bpp (3 channels - half float)"""

    PIXELFORMAT_UNCOMPRESSED_R16G16B16A16 = 13
    """16*4 bpp (4 channels - half float)"""

    PIXELFORMAT_COMPRESSED_DXT1_RGB = 14
    """4 bpp (no alpha)"""

    PIXELFORMAT_COMPRESSED_DXT1_RGBA = 15
    """4 bpp (1 bit alpha)"""

    PIXELFORMAT_COMPRESSED_DXT3_RGBA = 16
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_DXT5_RGBA = 17
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_ETC1_RGB = 18
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ETC2_RGB = 19
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 20
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_PVRT_RGB = 21
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_PVRT_RGBA = 22
    """4 bpp"""

    PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 23
    """8 bpp"""

    PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 24
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
PIXELFORMAT_UNCOMPRESSED_R16 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R16
PIXELFORMAT_UNCOMPRESSED_R16G16B16 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R16G16B16
PIXELFORMAT_UNCOMPRESSED_R16G16B16A16 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R16G16B16A16
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
    """Layout is defined by a horizontal line with faces"""

    CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = 3
    """Layout is defined by a 3x4 cross with cubemap faces"""

    CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = 4
    """Layout is defined by a 4x3 cross with cubemap faces"""

    CUBEMAP_LAYOUT_PANORAMA = 5
    """Layout is defined by a panorama image (equirrectangular map)"""


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
    """Blend textures using custom src/dst factors (use rlSetBlendFactors())"""

    BLEND_CUSTOM_SEPARATE = 7
    """Blend textures using custom rgb/alpha separate src/dst factors (use rlSetBlendFactorsSeparate())"""


BLEND_ALPHA = BlendMode.BLEND_ALPHA
BLEND_ADDITIVE = BlendMode.BLEND_ADDITIVE
BLEND_MULTIPLIED = BlendMode.BLEND_MULTIPLIED
BLEND_ADD_COLORS = BlendMode.BLEND_ADD_COLORS
BLEND_SUBTRACT_COLORS = BlendMode.BLEND_SUBTRACT_COLORS
BLEND_ALPHA_PREMULTIPLY = BlendMode.BLEND_ALPHA_PREMULTIPLY
BLEND_CUSTOM = BlendMode.BLEND_CUSTOM
BLEND_CUSTOM_SEPARATE = BlendMode.BLEND_CUSTOM_SEPARATE


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


# rlapi::rlgl
# ------------------------------------------------------------------------------

class rlGlVersion(IntEnum):
    """OpenGL version"""

    RL_OPENGL_11 = 1
    """OpenGL 1.1"""

    RL_OPENGL_21 = 2
    """OpenGL 2.1 (GLSL 120)"""

    RL_OPENGL_33 = 3
    """OpenGL 3.3 (GLSL 330)"""

    RL_OPENGL_43 = 4
    """OpenGL 4.3 (using GLSL 330)"""

    RL_OPENGL_ES_20 = 5
    """OpenGL ES 2.0 (GLSL 100)"""

    RL_OPENGL_ES_30 = 6
    """OpenGL ES 3.0 (GLSL 300 es)"""


RL_OPENGL_11 = rlGlVersion.RL_OPENGL_11
RL_OPENGL_21 = rlGlVersion.RL_OPENGL_21
RL_OPENGL_33 = rlGlVersion.RL_OPENGL_33
RL_OPENGL_43 = rlGlVersion.RL_OPENGL_43
RL_OPENGL_ES_20 = rlGlVersion.RL_OPENGL_ES_20
RL_OPENGL_ES_30 = rlGlVersion.RL_OPENGL_ES_30


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
    """Texture pixel formats"""

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

    RL_PIXELFORMAT_UNCOMPRESSED_R16 = 11
    """16 bpp (1 channel - half float)"""

    RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16 = 12
    """16*3 bpp (3 channels - half float)"""

    RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16A16 = 13
    """16*4 bpp (4 channels - half float)"""

    RL_PIXELFORMAT_COMPRESSED_DXT1_RGB = 14
    """4 bpp (no alpha)"""

    RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA = 15
    """4 bpp (1 bit alpha)"""

    RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA = 16
    """8 bpp"""

    RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA = 17
    """8 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ETC1_RGB = 18
    """4 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ETC2_RGB = 19
    """4 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = 20
    """8 bpp"""

    RL_PIXELFORMAT_COMPRESSED_PVRT_RGB = 21
    """4 bpp"""

    RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA = 22
    """4 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = 23
    """8 bpp"""

    RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = 24
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
RL_PIXELFORMAT_UNCOMPRESSED_R16 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R16
RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16
RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16A16 = rlPixelFormat.RL_PIXELFORMAT_UNCOMPRESSED_R16G16B16A16
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

    RL_BLEND_CUSTOM_SEPARATE = 7
    """Blend textures using custom src/dst factors (use rlSetBlendFactorsSeparate())"""


RL_BLEND_ALPHA = rlBlendMode.RL_BLEND_ALPHA
RL_BLEND_ADDITIVE = rlBlendMode.RL_BLEND_ADDITIVE
RL_BLEND_MULTIPLIED = rlBlendMode.RL_BLEND_MULTIPLIED
RL_BLEND_ADD_COLORS = rlBlendMode.RL_BLEND_ADD_COLORS
RL_BLEND_SUBTRACT_COLORS = rlBlendMode.RL_BLEND_SUBTRACT_COLORS
RL_BLEND_ALPHA_PREMULTIPLY = rlBlendMode.RL_BLEND_ALPHA_PREMULTIPLY
RL_BLEND_CUSTOM = rlBlendMode.RL_BLEND_CUSTOM
RL_BLEND_CUSTOM_SEPARATE = rlBlendMode.RL_BLEND_CUSTOM_SEPARATE


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


class rlFramebufferAttachType(IntEnum):
    """Framebuffer attachment type"""

    RL_ATTACHMENT_COLOR_CHANNEL0 = 0
    """Framebuffer attachment type: color 0"""

    RL_ATTACHMENT_COLOR_CHANNEL1 = 1
    """Framebuffer attachment type: color 1"""

    RL_ATTACHMENT_COLOR_CHANNEL2 = 2
    """Framebuffer attachment type: color 2"""

    RL_ATTACHMENT_COLOR_CHANNEL3 = 3
    """Framebuffer attachment type: color 3"""

    RL_ATTACHMENT_COLOR_CHANNEL4 = 4
    """Framebuffer attachment type: color 4"""

    RL_ATTACHMENT_COLOR_CHANNEL5 = 5
    """Framebuffer attachment type: color 5"""

    RL_ATTACHMENT_COLOR_CHANNEL6 = 6
    """Framebuffer attachment type: color 6"""

    RL_ATTACHMENT_COLOR_CHANNEL7 = 7
    """Framebuffer attachment type: color 7"""

    RL_ATTACHMENT_DEPTH = 100
    """Framebuffer attachment type: depth"""

    RL_ATTACHMENT_STENCIL = 200
    """Framebuffer attachment type: stencil"""


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
    """Framebuffer texture attachment type"""

    RL_ATTACHMENT_CUBEMAP_POSITIVE_X = 0
    """Framebuffer texture attachment type: cubemap, +X side"""

    RL_ATTACHMENT_CUBEMAP_NEGATIVE_X = 1
    """Framebuffer texture attachment type: cubemap, -X side"""

    RL_ATTACHMENT_CUBEMAP_POSITIVE_Y = 2
    """Framebuffer texture attachment type: cubemap, +Y side"""

    RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y = 3
    """Framebuffer texture attachment type: cubemap, -Y side"""

    RL_ATTACHMENT_CUBEMAP_POSITIVE_Z = 4
    """Framebuffer texture attachment type: cubemap, +Z side"""

    RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z = 5
    """Framebuffer texture attachment type: cubemap, -Z side"""

    RL_ATTACHMENT_TEXTURE2D = 100
    """Framebuffer texture attachment type: texture2d"""

    RL_ATTACHMENT_RENDERBUFFER = 200
    """Framebuffer texture attachment type: renderbuffer"""


RL_ATTACHMENT_CUBEMAP_POSITIVE_X = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_POSITIVE_X
RL_ATTACHMENT_CUBEMAP_NEGATIVE_X = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_NEGATIVE_X
RL_ATTACHMENT_CUBEMAP_POSITIVE_Y = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_POSITIVE_Y
RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y
RL_ATTACHMENT_CUBEMAP_POSITIVE_Z = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_POSITIVE_Z
RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z = rlFramebufferAttachTextureType.RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z
RL_ATTACHMENT_TEXTURE2D = rlFramebufferAttachTextureType.RL_ATTACHMENT_TEXTURE2D
RL_ATTACHMENT_RENDERBUFFER = rlFramebufferAttachTextureType.RL_ATTACHMENT_RENDERBUFFER


class rlCullMode(IntEnum):
    """Face culling mode"""

    RL_CULL_FACE_FRONT = 0

    RL_CULL_FACE_BACK = 1


RL_CULL_FACE_FRONT = rlCullMode.RL_CULL_FACE_FRONT
RL_CULL_FACE_BACK = rlCullMode.RL_CULL_FACE_BACK

# endregion (enumerations)

# region STRUCTURES

# rlapi::raylib
# ------------------------------------------------------------------------------

class Vector2(Structure):
    """Vector2, 2 components"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Vector2 elements"""
        return (Vector2 * len(sequence))(*sequence)

    @classmethod
    def one(cls):
        # type: (Vector2) -> Vector2
        return _Vector2One()

    def __init__(self, x=None, y=None):
        # type: (Vector2, float, float) -> None
        """Initializes this Vector2"""
        super(Vector2, self).__init__(
            x or 0.0,
            y or 0.0
        )

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Vector2{}".format(self.__str__())

    def __eq__(self, other):
        return _Vector2Equals(self, other)
    
    def __ne__(self, other):
        return not _Vector2Equals(self, other)
    
    def __pos__(self):
        return Vector2(+self.x, +self.y)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return _Vector2AddValue(self, float(other))
        return _Vector2Add(self, Vector2(other[0], other[1]))
    
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return _Vector2AddValue(self, float(other))
        return _Vector2Add(self, Vector2(other[0], other[1]))
    
    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.xy = _Vector2AddValue(self, float(other))
        else:
            self.xy = _Vector2Add(self, Vector2(other[0], other[1]))
        return self
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return _Vector2SubtractValue(self, float(other))
        return _Vector2Subtract(self, Vector2(other[0], other[1]))
    
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(other - self.x, other - self.y)
        return _Vector2Subtract(Vector2(other[0], other[1]), self)
    
    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.xy = _Vector2SubtractValue(self, float(other))
        else:
            self.xy = _Vector2Subtract(self, Vector2(other[0], other[1]))
        return self
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return _Vector2Scale(self, float(other))
        elif isinstance(other, Matrix):
            return _Vector2Transform(self, other)
        return _Vector2Multiply(self, Vector2(other[0], other[1]))
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return _Vector2Scale(self, float(other))
        return _Vector2Multiply(self, Vector2(other[0], other[1]))
    
    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.xy = _Vector2Scale(self, float(other))
        elif isinstance(other, Matrix):
            self.xy = _Vector2Transform(self, other)
        else:
            self.xy = _Vector2Multiply(self, Vector2(other[0], other[1]))
        return self
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return _Vector2Divide(self, Vector2(other, other))
        return _Vector2Divide(self, Vector2(other[0], other[1]))
    
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(other / self.x, other / self.y)
        return _Vector2Divide(Vector2(other[0], other[1]), self)
    
    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self.xy = _Vector2Divide(self, Vector2(other, other))
        else:
            self.xy = _Vector2Divide(self, Vector2(other[0], other[1]))
        return self

    def __len__(self):
        return 2
    
    def __getitem__(self, key):
        return (self.x, self.y).__getitem__(key)
    
    def __getattr__(self, attr):
        m = RE_VEC2_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector2 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))
    
    def __setattr__(self, attr, value):
        m = RE_VEC2_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector2 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector2, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector2, self).__setattr__(ch, float(value[i]))

    @property
    def byref(self):
        """Gets a pointer to this Vector2"""
        return byref(self)

    @property
    def length(self):
        return _Vector2Length(self)

    @property
    def length_sqr(self):
        return _Vector2LengthSqr(self)

    def dot_product(self, v2):
        # type: (Vector2, Vector2) -> float
        return _Vector2DotProduct(self, v2)

    def distance(self, v2):
        # type: (Vector2, Vector2) -> float
        return _Vector2Distance(self, v2)

    def distance_sqr(self, v2):
        # type: (Vector2, Vector2) -> float
        return _Vector2DistanceSqr(self, v2)

    def angle(self, v2):
        # type: (Vector2, Vector2) -> float
        return _Vector2Angle(self, v2)

    def normalize(self):
        # type: (Vector2) -> Vector2
        self.xy = _Vector2Normalize(self)
        return self

    def transform(self, mat):
        # type: (Vector2, Matrix) -> Vector2
        self.xy = _Vector2Transform(self, mat)
        return self

    def lerp(self, v2, amount):
        # type: (Vector2, Vector2, float) -> Vector2
        self.xy = _Vector2Lerp(self, v2, _float(amount))
        return self

    def reflect(self, normal):
        # type: (Vector2, Vector2) -> Vector2
        self.xy = _Vector2Reflect(self, normal)
        return self

    def rotate(self, angle):
        # type: (Vector2, float) -> Vector2
        self.xy = _Vector2Rotate(self, _float(angle))
        return self

    def move_towards(self, target, max_distance):
        # type: (Vector2, Vector2, float) -> Vector2
        self.xy = _Vector2MoveTowards(self, target, _float(max_distance))
        return self

    def clamp(self, min_, max_):
        # type: (Vector2, Vector2, Vector2) -> Vector2
        self.xy = _Vector2Clamp(self, min_, max_)
        return self

    def clamp_value(self, min_, max_):
        # type: (Vector2, float, float) -> Vector2
        self.xy = _Vector2ClampValue(self, _float(min_), _float(max_))
        return self

    def todict(self):
        '''Returns a dict mapping this Vector2's components'''
        return {'x': self.x, 'y': self.y}
    
    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector2's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))

# Pointer types for Vector2
Vector2Ptr = POINTER(Vector2)


class Vector3(Structure):
    """Vector3, 3 components"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Vector3 elements"""
        return (Vector3 * len(sequence))(*sequence)

    @classmethod
    def one(cls):
        # type: (Vector3) -> Vector3
        return _Vector3One()

    def __init__(self, x=None, y=None, z=None):
        # type: (Vector3, float, float, float) -> None
        """Initializes this Vector3"""
        super(Vector3, self).__init__(
            x or 0.0,
            y or 0.0,
            z or 0.0
        )

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Vector3{}".format(self.__str__())

    def __eq__(self, other):
        return _Vector3Equals(self, other)
    
    def __ne__(self, other):
        return not _Vector3Equals(self, other)
    
    def __pos__(self):
        return Vector3(+self.x, +self.y, +self.z)
    
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    def __abs__(self):
        return Vector3(abs(self.x), abs(self.y), abs(self.z))
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return _Vector3AddValue(self, float(other))
        return _Vector3Add(self, Vector3(other[0], other[1], other[2]))
    
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return _Vector3AddValue(self, float(other))
        return _Vector3Add(self, Vector3(other[0], other[1], other[2]))
    
    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.xy = _Vector3AddValue(self, float(other))
        else:
            self.xy = _Vector3Add(self, Vector3(other[0], other[1], other[2]))
        return self
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return _Vector3SubtractValue(self, float(other))
        return _Vector3Subtract(self, Vector3(other[0], other[1], other[2]))
    
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(other - self.x, other - self.y, other - self.z)
        return _Vector3Subtract(Vector3(other[0], other[1], other[2]), self)
    
    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.xy = _Vector3SubtractValue(self, float(other))
        else:
            self.xy = _Vector3Subtract(self, Vector3(other[0], other[1], other[2]))
        return self
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return _Vector3Scale(self, float(other))
        elif isinstance(other, Matrix):
            return _Vector3Transform(self, other)
        return _Vector3Multiply(self, Vector3(other[0], other[1], other[2]))
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return _Vector3Scale(self, float(other))
        return _Vector3Multiply(self, Vector3(other[0], other[1], other[2]))
    
    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.xy = _Vector3Scale(self, float(other))
        elif isinstance(other, Matrix):
            self.xy = _Vector3Transform(self, other)
        else:
            self.xy = _Vector3Multiply(self, Vector3(other[0], other[1], other[2]))
        return self
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return _Vector3Divide(self, Vector3(other, other))
        return _Vector3Divide(self, Vector3(other[0], other[1]))
    
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(other / self.x, other / self.y, other / self.z)
        return _Vector3Divide(Vector3(other[0], other[1], other[2]), self)
    
    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self.xy = _Vector3Divide(self, Vector3(other, other))
        else:
            self.xy = _Vector3Divide(self, Vector3(other[0], other[1], other[2]))
        return self

    def __len__(self):
        return 3
    
    def __getitem__(self, key):
        return (self.x, self.y, self.z).__getitem__(key)
    
    def __getattr__(self, attr):
        m = RE_VEC3_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector3 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))
    
    def __setattr__(self, attr, value):
        m = RE_VEC3_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector3 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector3, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector3, self).__setattr__(ch, float(value[i]))

    @property
    def byref(self):
        """Gets a pointer to this Vector3"""
        return byref(self)

    @property
    def length(self):
        return _Vector3Length(self)

    @property
    def length_sqr(self):
        return _Vector3LengthSqr(self)

    def cross_product(self, v2):
        # type: (Vector3, Vector3) -> Vector3
        return _Vector3CrossProduct(self, v2)

    def perpendicular(self):
        # type: (Vector3) -> Vector3
        self.xyz = _Vector3Perpendicular(self)
        return self

    def dot_product(self, v2):
        # type: (Vector3, Vector3) -> float
        return _Vector3DotProduct(self, v2)

    def distance(self, v2):
        # type: (Vector3, Vector3) -> float
        return _Vector3Distance(self, v2)

    def distance_sqr(self, v2):
        # type: (Vector3, Vector3) -> float
        return _Vector3DistanceSqr(self, v2)

    def angle(self, v2):
        # type: (Vector3, Vector3) -> float
        return _Vector3Angle(self, v2)

    def normalize(self):
        # type: (Vector3) -> Vector3
        self.xyz = _Vector3Normalize(self)
        return self

    def ortho_normalize(self, v2):
        # type: (Vector3Ptr, Vector3Ptr) -> None
        _Vector3OrthoNormalize(self, v2)

    def transform(self, mat):
        # type: (Vector3, Matrix) -> Vector3
        self.xyz = _Vector3Transform(self, mat)
        return self

    def rotate_by_quaternion(self, q):
        # type: (Vector3, Quaternion) -> Vector3
        self.xyz = _Vector3RotateByQuaternion(self, q)
        return self

    def rotate_by_axis_angle(self, axis, angle):
        # type: (Vector3, Vector3, float) -> Vector3
        self.xyz = _Vector3RotateByAxisAngle(self, axis, _float(angle))
        return self

    def lerp(self, v2, amount):
        # type: (Vector3, Vector3, float) -> Vector3
        self.xyz = _Vector3Lerp(self, v2, _float(amount))
        return self

    def reflect(self, normal):
        # type: (Vector3, Vector3) -> Vector3
        self.xyz = _Vector3Reflect(self, normal)
        return self

    def min(self, v2):
        # type: (Vector3, Vector3) -> Vector3
        self.xyz = _Vector3Min(self, v2)
        return self

    def max(self, v2):
        # type: (Vector3, Vector3) -> Vector3
        self.xyz = _Vector3Max(self, v2)
        return self

    def barycenter(self, a, b, c):
        # type: (Vector3, Vector3, Vector3, Vector3) -> Vector3
        self.xyz = _Vector3Barycenter(self, a, b, c)
        return self

    def unproject(self, projection, view):
        # type: (Vector3, Matrix, Matrix) -> Vector3
        self.xyz = _Vector3Unproject(self, projection, view)
        return self

    def to_float_v(self):
        # type: (Vector3) -> float3
        return _Vector3ToFloatV(self)

    def clamp(self, min_, max_):
        # type: (Vector3, Vector3, Vector3) -> Vector3
        self.xyz = _Vector3Clamp(self, min_, max_)
        return self

    def clamp_value(self, min_, max_):
        # type: (Vector3, float, float) -> Vector3
        self.xyz = _Vector3ClampValue(self, _float(min_), _float(max_))
        return self

    def refract(self, n, r):
        # type: (Vector3, Vector3, float) -> Vector3
        return _Vector3Refract(self, n, _float(r))

    def todict(self):
        '''Returns a dict mapping this Vector3's components'''
        return {'x': self.x, 'y': self.y, 'z': self.z}
    
    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector3's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.z = float(d.get('z', self.z))

# Pointer types for Vector3
Vector3Ptr = POINTER(Vector3)


class Vector4(Structure):
    """Vector4, 4 components"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Vector4 elements"""
        return (Vector4 * len(sequence))(*sequence)

    def __init__(self, x=None, y=None, z=None, w=None):
        # type: (Vector4, float, float, float, float) -> None
        """Initializes this Vector4"""
        super(Vector4, self).__init__(
            x or 0.0,
            y or 0.0,
            z or 0.0,
            w or 0.0
        )

    def __str__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)

    def __repr__(self):
        return "Vector4{}".format(self.__str__())

    def __eq__(self, other):
        return _Vector3Equals(self.xyz, other[:3])
    
    def __ne__(self, other):
        return not _Vector3Equals(self.xyz, other[:3])
    
    def __pos__(self):
        return Vector4(+self.x, +self.y, +self.z, +self.w)
    
    def __neg__(self):
        return Vector4(-self.x, -self.y, -self.z, -self.w)
    
    def __abs__(self):
        return Vector4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

    def __len__(self):
        return 4
    
    def __getitem__(self, key):
        return (self.x, self.y, self.z, self.w).__getitem__(key)
    
    def __getattr__(self, attr):
        m = RE_VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector4 object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))
    
    def __setattr__(self, attr, value):
        m = RE_VEC4_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Vector4 object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Vector4, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector4, self).__setattr__(ch, float(value[i]))

    @property
    def byref(self):
        """Gets a pointer to this Vector4"""
        return byref(self)

    def todict(self):
        '''Returns a dict mapping this Vector4's components'''
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}
    
    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector4's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.z = float(d.get('z', self.z))
        self.w = float(d.get('w', self.w))


# Quaternion, 4 components (Vector4 alias)
Quaternion = Vector4
QuaternionPtr = POINTER(Vector4)


class Matrix(Structure):
    """Matrix, 4x4 components, column major, OpenGL style, right-handed"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Matrix elements"""
        return (Matrix * len(sequence))(*sequence)

    @classmethod
    def identity(cls):
        # type: (Matrix) -> Matrix
        return _MatrixIdentity()

    @classmethod
    def translate(cls, x, y, z):
        # type: (Matrix, float, float, float) -> Matrix
        return _MatrixTranslate(_float(x), _float(y), _float(z))

    @classmethod
    def rotate(cls, axis, angle):
        # type: (Matrix, Vector3, float) -> Matrix
        return _MatrixRotate(axis, _float(angle))

    @classmethod
    def rotate_x(cls, angle):
        # type: (Matrix, float) -> Matrix
        return _MatrixRotateX(_float(angle))

    @classmethod
    def rotate_y(cls, angle):
        # type: (Matrix, float) -> Matrix
        return _MatrixRotateY(_float(angle))

    @classmethod
    def rotate_z(cls, angle):
        # type: (Matrix, float) -> Matrix
        return _MatrixRotateZ(_float(angle))

    @classmethod
    def rotate_xyz(cls, angle):
        # type: (Matrix, Vector3) -> Matrix
        return _MatrixRotateXYZ(angle)

    @classmethod
    def rotate_zyx(cls, angle):
        # type: (Matrix, Vector3) -> Matrix
        return _MatrixRotateZYX(angle)

    @classmethod
    def scale(cls, x, y, z):
        # type: (Matrix, float, float, float) -> Matrix
        return _MatrixScale(_float(x), _float(y), _float(z))

    @classmethod
    def frustum(cls, left, right, bottom, top, near, far):
        # type: (Matrix, float, float, float, float, float, float) -> Matrix
        return _MatrixFrustum(_float(left), _float(right), _float(bottom), _float(top), _float(near), _float(far))

    @classmethod
    def perspective(cls, fov_y, aspect, near_plane, far_plane):
        # type: (Matrix, float, float, float, float) -> Matrix
        return _MatrixPerspective(_float(fov_y), _float(aspect), _float(near_plane), _float(far_plane))

    @classmethod
    def ortho(cls, left, right, bottom, top, near_plane, far_plane):
        # type: (Matrix, float, float, float, float, float, float) -> Matrix
        return _MatrixOrtho(_float(left), _float(right), _float(bottom), _float(top), _float(near_plane), _float(far_plane))

    @classmethod
    def look_at(cls, eye, target, up):
        # type: (Matrix, Vector3, Vector3, Vector3) -> Matrix
        return _MatrixLookAt(eye, target, up)

    def __init__(self, m0=None, m4=None, m8=None, m12=None, m1=None, m5=None, m9=None, m13=None, m2=None, m6=None, m10=None, m14=None, m3=None, m7=None, m11=None, m15=None):
        # type: (Matrix, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float) -> None
        """Initializes this Matrix"""
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

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Matrix"""
        return byref(self)

    def determinant(self):
        # type: (Matrix) -> float
        return _MatrixDeterminant(self)

    def trace(self):
        # type: (Matrix) -> float
        return _MatrixTrace(self)

    def transpose(self):
        # type: (Matrix) -> Matrix
        return _MatrixTranspose(self)

    def invert(self):
        # type: (Matrix) -> Matrix
        return _MatrixInvert(self)

# Pointer types for Matrix
MatrixPtr = POINTER(Matrix)


class Color(Structure):
    """Color, 4 components, R8G8B8A8 (32bit)"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Color elements"""
        return (Color * len(sequence))(*sequence)

    @classmethod
    def from_normalized(cls, normalized):
        # type: (Color, Vector4) -> Color
        """Get Color from normalized values [0..1]"""
        return _ColorFromNormalized(_vec4(normalized))

    @classmethod
    def from_hsv(cls, hue, saturation, value):
        # type: (Color, float, float, float) -> Color
        """Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
        return _ColorFromHSV(_float(hue), _float(saturation), _float(value))

    @classmethod
    def get(cls, hex_value):
        # type: (Color, int) -> Color
        """Get Color structure from hexadecimal value"""
        return _GetColor(_int(hex_value))

    def __init__(self, r=None, g=None, b=None, a=None):
        # type: (Color, int, int, int, int) -> None
        """Initializes this Color"""
        super(Color, self).__init__(
            r or 0,
            g or 0,
            b or 0,
            a or 0
        )

    def __str__(self):
        return "({: 3}, {: 3}, {: 3}, {: 3})".format(self.r, self.g, self.b, self.a)

    def __repr__(self):
        return "Color{}".format(self.__str__())

    def __len__(self):
        return 4
    
    def __getitem__(self, key):
        return (self.r, self.g, self.b, self.a).__getitem__(key)
    
    def __getattr__(self, attr):
        m = RE_RGBA_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Color object does not have attribute '{}'.".format(attr))
        cls = {1: int, 4: Color}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))
    
    def __setattr__(self, attr, value):
        m = RE_RGBA_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Color object does not have attribute '{}'.".format(attr))
        if len(attr) == 1:
            super(Color, self).__setattr__(attr, int(value))
        else:
            for i, ch in enumerate(attr):
                super(Color, self).__setattr__(ch, int(value[i]))

    @property
    def byref(self):
        """Gets a pointer to this Color"""
        return byref(self)

    def fade(self, alpha):
        # type: (Color, float) -> Color
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        return _Fade(_color(self), _float(alpha))

    def normalize(self):
        # type: (Color) -> Vector4
        """Get Color normalized as float [0..1]"""
        return _ColorNormalize(_color(self))

    def to_int(self):
        # type: (Color) -> int
        """Get hexadecimal value for a Color"""
        return _ColorToInt(_color(self))

    def to_hsv(self):
        # type: (Color) -> Vector3
        """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
        return _ColorToHSV(_color(self))

    def tint(self, tint):
        # type: (Color, Color) -> Color
        """Get color multiplied with another color"""
        return _ColorTint(_color(self), _color(tint))

    def brightness(self, factor):
        # type: (Color, float) -> Color
        """Get color with brightness correction, brightness factor goes from -1.0f to 1.0f"""
        return _ColorBrightness(_color(self), _float(factor))

    def contrast(self, contrast):
        # type: (Color, float) -> Color
        """Get color with contrast correction, contrast values between -1.0f and 1.0f"""
        return _ColorContrast(_color(self), _float(contrast))

    def alpha(self, alpha):
        # type: (Color, float) -> Color
        """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
        return _ColorAlpha(_color(self), _float(alpha))

    def alpha_blend(self, src, tint):
        # type: (Color, Color, Color) -> Color
        """Get src alpha-blended into dst color with tint"""
        return _ColorAlphaBlend(_color(self), _color(src), _color(tint))

    def todict(self):
        '''Returns a dict mapping this Color's components'''
        return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}
    
    def fromdict(self, d):
        '''Apply the mapping `d` to this Color's components'''
        self.r = int(d.get('r', self.r))
        self.g = int(d.get('g', self.g))
        self.b = int(d.get('b', self.b))
        self.a = int(d.get('a', self.a))

# Pointer types for Color
ColorPtr = POINTER(Color)


class Rectangle(Structure):
    """Rectangle, 4 components"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Rectangle elements"""
        return (Rectangle * len(sequence))(*sequence)

    def __init__(self, x=None, y=None, width=None, height=None):
        # type: (Rectangle, float, float, float, float) -> None
        """Initializes this Rectangle"""
        super(Rectangle, self).__init__(
            x or 0.0,
            y or 0.0,
            width or 0.0,
            height or 0.0
        )

    def __str__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.width, self.height)

    def __repr__(self):
        return "Rectangle{}".format(self.__str__())

    def __len__(self):
        return 4
    
    def __getitem__(self, key):
        return (self.x, self.y, self.width, self.height).__getitem__(key)
    
    def __getattr__(self, attr):
        m = RE_RECT_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Rectangle object does not have attribute '{}'.".format(attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Rectangle}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))
    
    def __setattr__(self, attr, value):
        m = RE_RECT_SET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError("Rectangle object does not have attribute '{}'.".format(attr))
        w = self.width
        h = self.height
        if attr in ('width', 'height') or len(attr) == 1:
            if attr == 'c':
                super(Rectangle, self).__setattr__('x', float(value - w * 0.5))
            elif attr == 'r':
                super(Rectangle, self).__setattr__('x', float(value - w))
            elif attr == 'm':
                super(Rectangle, self).__setattr__('y', float(value - h * 0.5))
            elif attr == 'b':
                super(Rectangle, self).__setattr__('y', float(value - h))
            elif attr == 'w':
                super(Rectangle, self).__setattr__('width', value)
            elif attr == 'h':
                super(Rectangle, self).__setattr__('height', value)
            else:
                super(Rectangle, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                if ch in ('x', 'y'):
                    super(Rectangle, self).__setattr__(ch, float(value[i]))
                elif ch == 'c':
                    super(Rectangle, self).__setattr__('x', float(value[i] - w * 0.5))
                elif ch == 'r':
                    super(Rectangle, self).__setattr__('x', float(value[i] - w))
                elif ch == 'm':
                    super(Rectangle, self).__setattr__('y', float(value[i] - h * 0.5))
                elif ch == 'b':
                    super(Rectangle, self).__setattr__('y', float(value[i] - h))
                elif ch == 'w':
                    super(Rectangle, self).__setattr__('width', value[i])
                elif ch == 'h':
                    super(Rectangle, self).__setattr__('height', value[i])

    @property
    def byref(self):
        """Gets a pointer to this Rectangle"""
        return byref(self)

    def todict(self):
        '''Returns a dict mapping this Rectangle's components'''
        return {'x': self.x, 'y': self.y, 'w': self.width, 'h': self.height,
                'c': self.x + self.width * 0.5, 'm': self.y + self.height * 0.5,
                'r': self.x + self.width, 'b': self.y + self.height}
    
    def fromdict(self, d):
        '''Apply the mapping `d` to this Rectangle's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.width = float(d.get('w', self.width))
        self.height = float(d.get('h', self.height))

# Pointer types for Rectangle
RectanglePtr = POINTER(Rectangle)

# Pointer types for Rectangle
RectanglePtrPtr = POINTER(RectanglePtr)


class Image(Structure):
    """Image, pixel data stored in CPU memory (RAM)"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Image elements"""
        return (Image * len(sequence))(*sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Image, bytes | str | None) -> Image
        """Load image from file into CPU memory (RAM)"""
        return _LoadImage(_str_in(file_name))

    @classmethod
    def load_raw(cls, file_name, width, height, format_, header_size):
        # type: (Image, bytes | str | None, int, int, int, int) -> Image
        """Load image from RAW file data"""
        return _LoadImageRaw(_str_in(file_name), _int(width), _int(height), _int(format_), _int(header_size))

    @classmethod
    def load_svg(cls, file_name_or_string, width, height):
        # type: (Image, bytes | str | None, int, int) -> Image
        """Load image from SVG file data or string with specified size"""
        return _LoadImageSvg(_str_in(file_name_or_string), _int(width), _int(height))

    @classmethod
    def load_anim(cls, file_name, frames):
        # type: (Image, bytes | str | None, IntPtr) -> Image
        """Load image sequence from file (frames appended to image.data)"""
        return _LoadImageAnim(_str_in(file_name), frames)

    @classmethod
    def load_from_memory(cls, file_type, file_data, data_size):
        # type: (Image, bytes | str | None, int, int) -> Image
        """Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
        return _LoadImageFromMemory(_str_in(file_type), _int(file_data, (0, 255)), _int(data_size))

    @classmethod
    def load_from_texture(cls, texture):
        # type: (Image, Texture2D) -> Image
        """Load image from GPU texture data"""
        return _LoadImageFromTexture(texture)

    @classmethod
    def load_from_screen(cls):
        # type: (Image) -> Image
        """Load image from screen buffer and (screenshot)"""
        return _LoadImageFromScreen()

    @classmethod
    def gen_color(cls, width, height, color):
        # type: (Image, int, int, Color) -> Image
        """Generate image: plain color"""
        return _GenImageColor(_int(width), _int(height), _color(color))

    @classmethod
    def gen_gradient_linear(cls, width, height, direction, start, end):
        # type: (Image, int, int, int, Color, Color) -> Image
        """Generate image: linear gradient, direction in degrees [0..360], 0=Vertical gradient"""
        return _GenImageGradientLinear(_int(width), _int(height), _int(direction), _color(start), _color(end))

    @classmethod
    def gen_gradient_radial(cls, width, height, density, inner, outer):
        # type: (Image, int, int, float, Color, Color) -> Image
        """Generate image: radial gradient"""
        return _GenImageGradientRadial(_int(width), _int(height), _float(density), _color(inner), _color(outer))

    @classmethod
    def gen_gradient_square(cls, width, height, density, inner, outer):
        # type: (Image, int, int, float, Color, Color) -> Image
        """Generate image: square gradient"""
        return _GenImageGradientSquare(_int(width), _int(height), _float(density), _color(inner), _color(outer))

    @classmethod
    def gen_checked(cls, width, height, checks_x, checks_y, col1, col2):
        # type: (Image, int, int, int, int, Color, Color) -> Image
        """Generate image: checked"""
        return _GenImageChecked(_int(width), _int(height), _int(checks_x), _int(checks_y), _color(col1), _color(col2))

    @classmethod
    def gen_white_noise(cls, width, height, factor):
        # type: (Image, int, int, float) -> Image
        """Generate image: white noise"""
        return _GenImageWhiteNoise(_int(width), _int(height), _float(factor))

    @classmethod
    def gen_perlin_noise(cls, width, height, offset_x, offset_y, scale):
        # type: (Image, int, int, int, int, float) -> Image
        """Generate image: perlin noise"""
        return _GenImagePerlinNoise(_int(width), _int(height), _int(offset_x), _int(offset_y), _float(scale))

    @classmethod
    def gen_cellular(cls, width, height, tile_size):
        # type: (Image, int, int, int) -> Image
        """Generate image: cellular algorithm, bigger tileSize means bigger cells"""
        return _GenImageCellular(_int(width), _int(height), _int(tile_size))

    @classmethod
    def gen_text(cls, width, height, text):
        # type: (Image, int, int, bytes | str | None) -> Image
        """Generate image: grayscale image from text data"""
        return _GenImageText(_int(width), _int(height), _str_in(text))

    @classmethod
    def from_image(cls, image, rec):
        # type: (Image, Image, Rectangle) -> Image
        """Create an image from another image piece"""
        return _ImageFromImage(image, _rect(rec))

    @classmethod
    def text(cls, text, font_size, color):
        # type: (Image, bytes | str | None, int, Color) -> Image
        """Create an image from text (default font)"""
        return _ImageText(_str_in(text), _int(font_size), _color(color))

    @classmethod
    def text_ex(cls, font, text, font_size, spacing, tint):
        # type: (Image, Font, bytes | str | None, float, float, Color) -> Image
        """Create an image from text (custom sprite font)"""
        return _ImageTextEx(font, _str_in(text), _float(font_size), _float(spacing), _color(tint))

    def __init__(self, data=None, width=None, height=None, mipmaps=None, format_=None):
        # type: (Image, bytes | str | None, int, int, int, int) -> None
        """Initializes this Image"""
        super(Image, self).__init__(
            data,
            width or 0,
            height or 0,
            mipmaps or 1,
            format_ or PIXELFORMAT_UNCOMPRESSED_GRAYSCALE
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this Image"""
        return byref(self)

    @property
    def is_ready(self):
        """Check if an image is ready"""
        return _IsImageReady(self)

    def unload(self):
        # type: (Image) -> None
        """Unload image from CPU memory (RAM)"""
        _UnloadImage(self)

    def export(self, file_name):
        # type: (Image, bytes | str | None) -> bool
        """Export image data to file, returns true on success"""
        return _ExportImage(self, _str_in(file_name))

    def export_as_code(self, file_name):
        # type: (Image, bytes | str | None) -> bool
        """Export image as code file defining an array of bytes, returns true on success"""
        return _ExportImageAsCode(self, _str_in(file_name))

    def copy(self):
        # type: (Image) -> Image
        """Create an image duplicate (useful for transformations)"""
        return _ImageCopy(self)

    def format(self, new_format):
        # type: (ImagePtr, int) -> None
        """Convert image data to desired format"""
        _ImageFormat(self, _int(new_format))

    def to_pot(self, fill):
        # type: (ImagePtr, Color) -> None
        """Convert image to POT (power-of-two)"""
        _ImageToPOT(self, _color(fill))

    def crop(self, crop):
        # type: (ImagePtr, Rectangle) -> None
        """Crop an image to a defined rectangle"""
        _ImageCrop(self, _rect(crop))

    def alpha_crop(self, threshold):
        # type: (ImagePtr, float) -> None
        """Crop image depending on alpha value"""
        _ImageAlphaCrop(self, _float(threshold))

    def alpha_clear(self, color, threshold):
        # type: (ImagePtr, Color, float) -> None
        """Clear alpha channel to desired color"""
        _ImageAlphaClear(self, _color(color), _float(threshold))

    def alpha_mask(self, alpha_mask):
        # type: (ImagePtr, Image) -> None
        """Apply alpha mask to image"""
        _ImageAlphaMask(self, alpha_mask)

    def alpha_premultiply(self):
        # type: (ImagePtr) -> None
        """Premultiply alpha channel"""
        _ImageAlphaPremultiply(self)

    def blur_gaussian(self, blur_size):
        # type: (ImagePtr, int) -> None
        """Apply Gaussian blur using a box blur approximation"""
        _ImageBlurGaussian(self, _int(blur_size))

    def resize(self, new_width, new_height):
        # type: (ImagePtr, int, int) -> None
        """Resize image (Bicubic scaling algorithm)"""
        _ImageResize(self, _int(new_width), _int(new_height))

    def resize_nn(self, new_width, new_height):
        # type: (ImagePtr, int, int) -> None
        """Resize image (Nearest-Neighbor scaling algorithm)"""
        _ImageResizeNN(self, _int(new_width), _int(new_height))

    def resize_canvas(self, new_width, new_height, offset_x, offset_y, fill):
        # type: (ImagePtr, int, int, int, int, Color) -> None
        """Resize canvas and fill with color"""
        _ImageResizeCanvas(self, _int(new_width), _int(new_height), _int(offset_x), _int(offset_y), _color(fill))

    def mipmaps(self):
        # type: (ImagePtr) -> None
        """Compute all mipmap levels for a provided image"""
        _ImageMipmaps(self)

    def dither(self, r_bpp, g_bpp, b_bpp, a_bpp):
        # type: (ImagePtr, int, int, int, int) -> None
        """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
        _ImageDither(self, _int(r_bpp), _int(g_bpp), _int(b_bpp), _int(a_bpp))

    def flip_vertical(self):
        # type: (ImagePtr) -> None
        """Flip image vertically"""
        _ImageFlipVertical(self)

    def flip_horizontal(self):
        # type: (ImagePtr) -> None
        """Flip image horizontally"""
        _ImageFlipHorizontal(self)

    def rotate(self, degrees):
        # type: (ImagePtr, int) -> None
        """Rotate image by input angle in degrees (-359 to 359)"""
        _ImageRotate(self, _int(degrees))

    def rotate_cw(self):
        # type: (ImagePtr) -> None
        """Rotate image clockwise 90deg"""
        _ImageRotateCW(self)

    def rotate_ccw(self):
        # type: (ImagePtr) -> None
        """Rotate image counter-clockwise 90deg"""
        _ImageRotateCCW(self)

    def color_tint(self, color):
        # type: (ImagePtr, Color) -> None
        """Modify image color: tint"""
        _ImageColorTint(self, _color(color))

    def color_invert(self):
        # type: (ImagePtr) -> None
        """Modify image color: invert"""
        _ImageColorInvert(self)

    def color_grayscale(self):
        # type: (ImagePtr) -> None
        """Modify image color: grayscale"""
        _ImageColorGrayscale(self)

    def color_contrast(self, contrast):
        # type: (ImagePtr, float) -> None
        """Modify image color: contrast (-100 to 100)"""
        _ImageColorContrast(self, _float(contrast))

    def color_brightness(self, brightness):
        # type: (ImagePtr, int) -> None
        """Modify image color: brightness (-255 to 255)"""
        _ImageColorBrightness(self, _int(brightness))

    def color_replace(self, color, replace):
        # type: (ImagePtr, Color, Color) -> None
        """Modify image color: replace color"""
        _ImageColorReplace(self, _color(color), _color(replace))

    def clear_background(self, color):
        # type: (ImagePtr, Color) -> None
        """Clear image background with given color"""
        _ImageClearBackground(self, _color(color))

    def draw_pixel(self, pos_x, pos_y, color):
        # type: (ImagePtr, int, int, Color) -> None
        """Draw pixel within an image"""
        _ImageDrawPixel(self, _int(pos_x), _int(pos_y), _color(color))

    def draw_pixel_v(self, position, color):
        # type: (ImagePtr, Vector2, Color) -> None
        """Draw pixel within an image (Vector version)"""
        _ImageDrawPixelV(self, _vec2(position), _color(color))

    def draw_line(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y, color):
        # type: (ImagePtr, int, int, int, int, Color) -> None
        """Draw line within an image"""
        _ImageDrawLine(self, _int(start_pos_x), _int(start_pos_y), _int(end_pos_x), _int(end_pos_y), _color(color))

    def draw_line_v(self, start, end, color):
        # type: (ImagePtr, Vector2, Vector2, Color) -> None
        """Draw line within an image (Vector version)"""
        _ImageDrawLineV(self, _vec2(start), _vec2(end), _color(color))

    def draw_circle(self, center_x, center_y, radius, color):
        # type: (ImagePtr, int, int, int, Color) -> None
        """Draw a filled circle within an image"""
        _ImageDrawCircle(self, _int(center_x), _int(center_y), _int(radius), _color(color))

    def draw_circle_v(self, center, radius, color):
        # type: (ImagePtr, Vector2, int, Color) -> None
        """Draw a filled circle within an image (Vector version)"""
        _ImageDrawCircleV(self, _vec2(center), _int(radius), _color(color))

    def draw_circle_lines(self, center_x, center_y, radius, color):
        # type: (ImagePtr, int, int, int, Color) -> None
        """Draw circle outline within an image"""
        _ImageDrawCircleLines(self, _int(center_x), _int(center_y), _int(radius), _color(color))

    def draw_circle_lines_v(self, center, radius, color):
        # type: (ImagePtr, Vector2, int, Color) -> None
        """Draw circle outline within an image (Vector version)"""
        _ImageDrawCircleLinesV(self, _vec2(center), _int(radius), _color(color))

    def draw_rectangle(self, pos_x, pos_y, width, height, color):
        # type: (ImagePtr, int, int, int, int, Color) -> None
        """Draw rectangle within an image"""
        _ImageDrawRectangle(self, _int(pos_x), _int(pos_y), _int(width), _int(height), _color(color))

    def draw_rectangle_v(self, position, size, color):
        # type: (ImagePtr, Vector2, Vector2, Color) -> None
        """Draw rectangle within an image (Vector version)"""
        _ImageDrawRectangleV(self, _vec2(position), _vec2(size), _color(color))

    def draw_rectangle_rec(self, rec, color):
        # type: (ImagePtr, Rectangle, Color) -> None
        """Draw rectangle within an image"""
        _ImageDrawRectangleRec(self, _rect(rec), _color(color))

    def draw_rectangle_lines(self, rec, thick, color):
        # type: (ImagePtr, Rectangle, int, Color) -> None
        """Draw rectangle lines within an image"""
        _ImageDrawRectangleLines(self, _rect(rec), _int(thick), _color(color))

    def draw(self, src, src_rec, dst_rec, tint):
        # type: (ImagePtr, Image, Rectangle, Rectangle, Color) -> None
        """Draw a source image within a destination image (tint applied to source)"""
        _ImageDraw(self, src, _rect(src_rec), _rect(dst_rec), _color(tint))

    def draw_text(self, text, pos_x, pos_y, font_size, color):
        # type: (ImagePtr, bytes | str | None, int, int, int, Color) -> None
        """Draw text (using default font) within an image (destination)"""
        _ImageDrawText(self, _str_in(text), _int(pos_x), _int(pos_y), _int(font_size), _color(color))

    def draw_text_ex(self, font, text, position, font_size, spacing, tint):
        # type: (ImagePtr, Font, bytes | str | None, Vector2, float, float, Color) -> None
        """Draw text (custom sprite font) within an image (destination)"""
        _ImageDrawTextEx(self, font, _str_in(text), _vec2(position), _float(font_size), _float(spacing), _color(tint))

    def load_colors(self):
        # type: (Image) -> ColorPtr
        """Load color data from image as a Color array (RGBA - 32bit)"""
        return _LoadImageColors(self)

    def load_palette(self, max_palette_size, color_count):
        # type: (Image, int, int) -> Array[Color]
        """Load colors palette from image as a Color array (RGBA - 32bit)"""
        color_count = Int(color_count)
        result = _LoadImagePalette(self, _int(max_palette_size), byref(color_count))
        result = cast(result, POINTER(Color * color_count.value))[0]
        _clear_in_out()
        _push_in_out(color_count.value)
        return result

    def get_alpha_border(self, threshold):
        # type: (Image, float) -> Rectangle
        """Get image alpha border rectangle"""
        return _GetImageAlphaBorder(self, _float(threshold))

    def get_color(self, x, y):
        # type: (Image, int, int) -> Color
        """Get image pixel color at (x, y) position"""
        return _GetImageColor(self, _int(x), _int(y))

    @staticmethod
    def unload_colors(colors):
        # type: (ColorPtr) -> None
        """Unload color data loaded with LoadImageColors()"""
        _UnloadImageColors(colors)

    @staticmethod
    def unload_palette(colors):
        # type: (ColorPtr) -> None
        """Unload colors palette loaded with LoadImagePalette()"""
        _UnloadImagePalette(colors)

# Pointer types for Image
ImagePtr = POINTER(Image)


class Texture(Structure):
    """Texture, tex data stored in GPU memory (VRAM)"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Texture elements"""
        return (Texture * len(sequence))(*sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Texture, bytes | str | None) -> Texture2D
        """Load texture from file into GPU memory (VRAM)"""
        return _LoadTexture(_str_in(file_name))

    @classmethod
    def load_from_image(cls, image):
        # type: (Texture, Image) -> Texture2D
        """Load texture from image data"""
        return _LoadTextureFromImage(image)

    @classmethod
    def load_cubemap(cls, image, layout):
        # type: (Texture, Image, int) -> TextureCubemap
        """Load cubemap from image, multiple image cubemap layouts supported"""
        return _LoadTextureCubemap(image, _int(layout))

    def __init__(self, id_=None, width=None, height=None, mipmaps=None, format_=None):
        # type: (Texture, int, int, int, int, int) -> None
        """Initializes this Texture"""
        super(Texture, self).__init__(
            id_ or 0,
            width or 0,
            height or 0,
            mipmaps or 0,
            format_ or PIXELFORMAT_UNCOMPRESSED_GRAYSCALE
        )

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Texture"""
        return byref(self)

    @property
    def is_ready(self):
        """Check if a texture is ready"""
        return _IsTextureReady(self)

    def unload(self):
        # type: (Texture2D) -> None
        """Unload texture from GPU memory (VRAM)"""
        _UnloadTexture(self)

    def gen_mip_maps(self):
        # type: (Texture2DPtr) -> None
        """Generate GPU mipmaps for a texture"""
        _GenTextureMipmaps(self)

    def set_filter(self, filter_):
        # type: (Texture2D, int) -> None
        """Set texture scaling filter mode"""
        _SetTextureFilter(self, _int(filter_))

    def set_wrap(self, wrap):
        # type: (Texture2D, int) -> None
        """Set texture wrapping mode"""
        _SetTextureWrap(self, _int(wrap))

    def draw(self, pos_x, pos_y, tint):
        # type: (Texture2D, int, int, Color) -> None
        """Draw a Texture2D"""
        _DrawTexture(self, _int(pos_x), _int(pos_y), _color(tint))

    def draw_v(self, position, tint):
        # type: (Texture2D, Vector2, Color) -> None
        """Draw a Texture2D with position defined as Vector2"""
        _DrawTextureV(self, _vec2(position), _color(tint))

    def draw_ex(self, position, rotation, scale, tint):
        # type: (Texture2D, Vector2, float, float, Color) -> None
        """Draw a Texture2D with extended parameters"""
        _DrawTextureEx(self, _vec2(position), _float(rotation), _float(scale), _color(tint))

    def draw_rec(self, source, position, tint):
        # type: (Texture2D, Rectangle, Vector2, Color) -> None
        """Draw a part of a texture defined by a rectangle"""
        _DrawTextureRec(self, _rect(source), _vec2(position), _color(tint))

    def draw_pro(self, source, dest, origin, rotation, tint):
        # type: (Texture2D, Rectangle, Rectangle, Vector2, float, Color) -> None
        """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
        _DrawTexturePro(self, _rect(source), _rect(dest), _vec2(origin), _float(rotation), _color(tint))

    def draw_npatch(self, n_patch_info, dest, origin, rotation, tint):
        # type: (Texture2D, NPatchInfo, Rectangle, Vector2, float, Color) -> None
        """Draws a texture (or part of it) that stretches or shrinks nicely"""
        _DrawTextureNPatch(self, n_patch_info, _rect(dest), _vec2(origin), _float(rotation), _color(tint))

    def update(self, pixels):
        # type: (Texture2D, bytes | str | None) -> None
        """Update GPU texture with new data"""
        _UpdateTexture(self, pixels)

    def update_rec(self, rec, pixels):
        # type: (Texture2D, Rectangle, bytes | str | None) -> None
        """Update GPU texture rectangle with new data"""
        _UpdateTextureRec(self, _rect(rec), pixels)


# Texture2D, same as Texture
Texture2D = Texture
Texture2DPtr = POINTER(Texture)

# TextureCubemap, same as Texture
TextureCubemap = Texture
TextureCubemapPtr = POINTER(Texture)


class RenderTexture(Structure):
    """RenderTexture, fbo for texture rendering"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of RenderTexture elements"""
        return (RenderTexture * len(sequence))(*sequence)

    def __init__(self, id_=None, texture=None, depth=None):
        # type: (RenderTexture, int, Texture, Texture) -> None
        """Initializes this RenderTexture"""
        super(RenderTexture, self).__init__(
            id_,
            texture,
            depth
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this RenderTexture"""
        return byref(self)


# RenderTexture2D, same as RenderTexture
RenderTexture2D = RenderTexture
RenderTexture2DPtr = POINTER(RenderTexture)


class NPatchInfo(Structure):
    """NPatchInfo, n-patch layout info"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of NPatchInfo elements"""
        return (NPatchInfo * len(sequence))(*sequence)

    def __init__(self, source=None, left=None, top=None, right=None, bottom=None, layout=None):
        # type: (NPatchInfo, Rectangle, int, int, int, int, int) -> None
        """Initializes this NPatchInfo"""
        super(NPatchInfo, self).__init__(
            source or Rectangle(),
            left or 1,
            top or 1,
            right or 1,
            bottom or 1,
            layout or NPATCH_NINE_PATCH
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this NPatchInfo"""
        return byref(self)


class GlyphInfo(Structure):
    """GlyphInfo, font characters glyphs info"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of GlyphInfo elements"""
        return (GlyphInfo * len(sequence))(*sequence)

    def __init__(self, value=None, offset_x=None, offset_y=None, advance_x=None, image=None):
        # type: (GlyphInfo, int, int, int, int, Image) -> None
        """Initializes this GlyphInfo"""
        super(GlyphInfo, self).__init__(
            value or 0,
            offset_x or 0,
            offset_y or 0,
            advance_x or 0,
            image or Image()
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this GlyphInfo"""
        return byref(self)

# Pointer types for GlyphInfo
GlyphInfoPtr = POINTER(GlyphInfo)


class Font(Structure):
    """Font, font texture and GlyphInfo array data"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Font elements"""
        return (Font * len(sequence))(*sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Font, bytes | str | None) -> Font
        """Load font from file into GPU memory (VRAM)"""
        return _LoadFont(_str_in(file_name))

    @classmethod
    def load_ex(cls, file_name, font_size, codepoints, codepoint_count):
        # type: (Font, bytes | str | None, int, list[int] | str, int) -> Font
        """Load font from file with extended parameters, use NULL for codepoints and 0 for codepointCount to load the default character setFont"""
        codepoints = int_array(codepoints)
        result = _LoadFontEx(_str_in(file_name), _int(font_size), byref(codepoints), _int(codepoint_count))
        result = result.contents[:codepoints]
        return result

    @classmethod
    def load_from_image(cls, image, key, first_char):
        # type: (Font, Image, Color, int) -> Font
        """Load font from Image (XNA style)"""
        return _LoadFontFromImage(image, _color(key), _int(first_char))

    @classmethod
    def load_from_memory(cls, file_type, file_data, data_size, font_size, codepoints, codepoint_count):
        # type: (Font, bytes | str | None, int, int, int, list[int] | str, int) -> Font
        """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
        codepoints = int_array(codepoints)
        return _LoadFontFromMemory(_str_in(file_type), _int(file_data, (0, 255)), _int(data_size), _int(font_size), codepoints, _int(codepoint_count))

    @classmethod
    def get_default(cls):
        # type: (Font) -> Font
        """Get the default Font"""
        return _GetFontDefault()

    def __init__(self, base_size=None, glyph_count=None, glyph_padding=None, texture=None, recs=None, glyphs=None):
        # type: (Font, int, int, int, Texture2D, RectanglePtr, GlyphInfoPtr) -> None
        """Initializes this Font"""
        super(Font, self).__init__(
            base_size or 1,
            glyph_count or 0,
            glyph_padding or 1,
            texture or Texture2D(),
            recs,
            glyphs
        )

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Font"""
        return byref(self)

    @property
    def is_ready(self):
        """Check if a font is ready"""
        return _IsFontReady(self)

    def unload(self):
        # type: (Font) -> None
        """Unload font from GPU memory (VRAM)"""
        _UnloadFont(self)

    def draw_text_ex(self, text, position, font_size, spacing, tint):
        # type: (Font, bytes | str | None, Vector2, float, float, Color) -> None
        """Draw text using font and additional parameters"""
        _DrawTextEx(self, _str_in(text), _vec2(position), _float(font_size), _float(spacing), _color(tint))

    def draw_text_pro(self, text, position, origin, rotation, font_size, spacing, tint):
        # type: (Font, bytes | str | None, Vector2, Vector2, float, float, float, Color) -> None
        """Draw text using Font and pro parameters (rotation)"""
        _DrawTextPro(self, _str_in(text), _vec2(position), _vec2(origin), _float(rotation), _float(font_size), _float(spacing), _color(tint))

    def draw_text_codepoint(self, codepoint, position, font_size, tint):
        # type: (Font, int, Vector2, float, Color) -> None
        """Draw one character (codepoint)"""
        _DrawTextCodepoint(self, _int(codepoint), _vec2(position), _float(font_size), _color(tint))

    def draw_text_codepoints(self, codepoints, codepoint_count, position, font_size, spacing, tint):
        # type: (Font, IntPtr, int, Vector2, float, float, Color) -> None
        """Draw multiple character (codepoint)"""
        _DrawTextCodepoints(self, codepoints, _int(codepoint_count), _vec2(position), _float(font_size), _float(spacing), _color(tint))

    def measure_text_ex(self, text, font_size, spacing):
        # type: (Font, bytes | str | None, float, float) -> Vector2
        """Measure string size for Font"""
        return _MeasureTextEx(self, _str_in(text), _float(font_size), _float(spacing))

    def get_glyph_index(self, codepoint):
        # type: (Font, int) -> int
        """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
        return _GetGlyphIndex(self, _int(codepoint))

    def get_glyph_info(self, codepoint):
        # type: (Font, int) -> GlyphInfo
        """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
        return _GetGlyphInfo(self, _int(codepoint))

    def get_glyph_atlas_rec(self, codepoint):
        # type: (Font, int) -> Rectangle
        """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
        return _GetGlyphAtlasRec(self, _int(codepoint))

    @staticmethod
    def load_data(file_data, data_size, font_size, codepoints, codepoint_count, type_):
        # type: (int, int, int, list[int] | str, int, int) -> Array[GlyphInfo]
        """Load font data for further use"""
        codepoints = int_array(codepoints)
        result = _LoadFontData(_int(file_data, (0, 255)), _int(data_size), _int(font_size), byref(codepoints), _int(codepoint_count), _int(type_))
        result = cast(result, POINTER(GlyphInfo * codepoints.value))[0]
        _clear_in_out()
        _push_in_out(codepoints.value)
        return result

    @staticmethod
    def unload_data(glyphs, glyph_count):
        # type: (GlyphInfoPtr, int) -> None
        """Unload font chars info data (RAM)"""
        _UnloadFontData(glyphs, _int(glyph_count))


class Camera3D(Structure):
    """Camera, defines position/orientation in 3d space"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Camera3D elements"""
        return (Camera3D * len(sequence))(*sequence)

    def __init__(self, position=None, target=None, up=None, fovy=None, projection=None):
        # type: (Camera3D, Vector3, Vector3, Vector3, float, int) -> None
        """Initializes this Camera3D"""
        super(Camera3D, self).__init__(
            position or Vector3(),
            target or Vector3(),
            up or Vector3(0.0, 1.0, 0.0),
            fovy or 45.0,
            projection or CAMERA_PERSPECTIVE
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    def __enter__(self):
        # type: (Camera3D) -> None
        """Begin 3D mode with custom camera (3D)"""
        _BeginMode3D(self)

    def __exit__():
        # type: () -> None
        """Ends 3D mode and returns to default 2D orthographic mode"""
        _EndMode3D()

    @property
    def byref(self):
        """Gets a pointer to this Camera3D"""
        return byref(self)

    def get_matrix(self):
        # type: (Camera) -> Matrix
        """Get camera transform matrix (view matrix)"""
        return _GetCameraMatrix(self)


# Camera type fallback, defaults to Camera3D
Camera = Camera3D
CameraPtr = POINTER(Camera3D)


class Camera2D(Structure):
    """Camera2D, defines position/orientation in 2d space"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Camera2D elements"""
        return (Camera2D * len(sequence))(*sequence)

    def __init__(self, offset=None, target=None, rotation=None, zoom=None):
        # type: (Camera2D, Vector2, Vector2, float, float) -> None
        """Initializes this Camera2D"""
        super(Camera2D, self).__init__(
            offset or Vector2(),
            target or Vector2(),
            rotation or 0.0,
            zoom or 1.0
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    def __enter__(self):
        # type: (Camera2D) -> None
        """Begin 2D mode with custom camera (2D)"""
        _BeginMode2D(self)

    def __exit__():
        # type: () -> None
        """Ends 2D mode with custom camera"""
        _EndMode2D()

    @property
    def byref(self):
        """Gets a pointer to this Camera2D"""
        return byref(self)

    def get_matrix2d(self):
        # type: (Camera2D) -> Matrix
        """Get camera 2d transform matrix"""
        return _GetCameraMatrix2D(self)


class Mesh(Structure):
    """Mesh, vertex data and vao/vbo"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Mesh elements"""
        return (Mesh * len(sequence))(*sequence)

    @classmethod
    def gen_poly(cls, sides, radius):
        # type: (Mesh, int, float) -> Mesh
        """Generate polygonal mesh"""
        return _GenMeshPoly(_int(sides), _float(radius))

    @classmethod
    def gen_plane(cls, width, length, res_x, res_z):
        # type: (Mesh, float, float, int, int) -> Mesh
        """Generate plane mesh (with subdivisions)"""
        return _GenMeshPlane(_float(width), _float(length), _int(res_x), _int(res_z))

    @classmethod
    def gen_cube(cls, width, height, length):
        # type: (Mesh, float, float, float) -> Mesh
        """Generate cuboid mesh"""
        return _GenMeshCube(_float(width), _float(height), _float(length))

    @classmethod
    def gen_sphere(cls, radius, rings, slices):
        # type: (Mesh, float, int, int) -> Mesh
        """Generate sphere mesh (standard sphere)"""
        return _GenMeshSphere(_float(radius), _int(rings), _int(slices))

    @classmethod
    def gen_hemi_sphere(cls, radius, rings, slices):
        # type: (Mesh, float, int, int) -> Mesh
        """Generate half-sphere mesh (no bottom cap)"""
        return _GenMeshHemiSphere(_float(radius), _int(rings), _int(slices))

    @classmethod
    def gen_cylinder(cls, radius, height, slices):
        # type: (Mesh, float, float, int) -> Mesh
        """Generate cylinder mesh"""
        return _GenMeshCylinder(_float(radius), _float(height), _int(slices))

    @classmethod
    def gen_cone(cls, radius, height, slices):
        # type: (Mesh, float, float, int) -> Mesh
        """Generate cone/pyramid mesh"""
        return _GenMeshCone(_float(radius), _float(height), _int(slices))

    @classmethod
    def gen_torus(cls, radius, size, rad_seg, sides):
        # type: (Mesh, float, float, int, int) -> Mesh
        """Generate torus mesh"""
        return _GenMeshTorus(_float(radius), _float(size), _int(rad_seg), _int(sides))

    @classmethod
    def gen_knot(cls, radius, size, rad_seg, sides):
        # type: (Mesh, float, float, int, int) -> Mesh
        """Generate trefoil knot mesh"""
        return _GenMeshKnot(_float(radius), _float(size), _int(rad_seg), _int(sides))

    @classmethod
    def gen_heightmap(cls, heightmap, size):
        # type: (Mesh, Image, Vector3) -> Mesh
        """Generate heightmap mesh from image data"""
        return _GenMeshHeightmap(heightmap, _vec3(size))

    @classmethod
    def gen_cubicmap(cls, cubicmap, cube_size):
        # type: (Mesh, Image, Vector3) -> Mesh
        """Generate cubes-based map mesh from image data"""
        return _GenMeshCubicmap(cubicmap, _vec3(cube_size))

    def __init__(self, vertex_count=None, triangle_count=None, vertices=None, texcoords=None, texcoords2=None, normals=None, tangents=None, colors=None, indices=None, anim_vertices=None, anim_normals=None, bone_ids=None, bone_weights=None, vao_id=None, vbo_id=None):
        # type: (Mesh, int, int, FloatPtr, FloatPtr, FloatPtr, FloatPtr, FloatPtr, int, UShortPtr, FloatPtr, FloatPtr, int, FloatPtr, int, UIntPtr) -> None
        """Initializes this Mesh"""
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

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Mesh"""
        return byref(self)

    def upload(self, dynamic):
        # type: (MeshPtr, bool) -> None
        """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
        _UploadMesh(self, _bool(dynamic))

    def update_buffer(self, index, data, data_size, offset):
        # type: (Mesh, int, bytes | str | None, int, int) -> None
        """Update mesh vertex data in GPU for a specific buffer index"""
        _UpdateMeshBuffer(self, _int(index), data, _int(data_size), _int(offset))

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
        _DrawMeshInstanced(self, material, transforms, _int(instances))

    def export(self, file_name):
        # type: (Mesh, bytes | str | None) -> bool
        """Export mesh data to file, returns true on success"""
        return _ExportMesh(self, _str_in(file_name))

    def get_bounding_box(self):
        # type: (Mesh) -> BoundingBox
        """Compute mesh bounding box limits"""
        return _GetMeshBoundingBox(self)

    def gen_tangents(self):
        # type: (MeshPtr) -> None
        """Compute mesh tangents"""
        _GenMeshTangents(self)

# Pointer types for Mesh
MeshPtr = POINTER(Mesh)


class Shader(Structure):
    """Shader"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Shader elements"""
        return (Shader * len(sequence))(*sequence)

    @classmethod
    def load(cls, vs_file_name, fs_file_name):
        # type: (Shader, bytes | str | None, bytes | str | None) -> Shader
        """Load shader from files and bind default locations"""
        return _LoadShader(_str_in(vs_file_name), _str_in(fs_file_name))

    @classmethod
    def load_from_memory(cls, vs_code, fs_code):
        # type: (Shader, bytes | str | None, bytes | str | None) -> Shader
        """Load shader from code strings and bind default locations"""
        return _LoadShaderFromMemory(_str_in(vs_code), _str_in(fs_code))

    def __init__(self, id_=None, locs=None):
        # type: (Shader, int, IntPtr) -> None
        """Initializes this Shader"""
        super(Shader, self).__init__(
            id_ or 0,
            locs
        )

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    def __enter__(self):
        # type: (Shader) -> None
        """Begin custom shader drawing"""
        _BeginShaderMode(self)

    def __exit__():
        # type: () -> None
        """End custom shader drawing (use default shader)"""
        _EndShaderMode()

    @property
    def byref(self):
        """Gets a pointer to this Shader"""
        return byref(self)

    @property
    def is_ready(self):
        """Check if a shader is ready"""
        return _IsShaderReady(self)

    def get_location(self, uniform_name):
        # type: (Shader, bytes | str | None) -> int
        """Get shader uniform location"""
        return _GetShaderLocation(self, _str_in(uniform_name))

    def get_location_attrib(self, attrib_name):
        # type: (Shader, bytes | str | None) -> int
        """Get shader attribute location"""
        return _GetShaderLocationAttrib(self, _str_in(attrib_name))

    def set_value(self, loc_index, value, uniform_type):
        # type: (Shader, int, bytes | str | None, int) -> None
        """Set shader uniform value"""
        _SetShaderValue(self, _int(loc_index), value, _int(uniform_type))

    def set_value_v(self, loc_index, value, uniform_type, count):
        # type: (Shader, int, bytes | str | None, int, int) -> None
        """Set shader uniform value vector"""
        _SetShaderValueV(self, _int(loc_index), value, _int(uniform_type), _int(count))

    def set_value_matrix(self, loc_index, mat):
        # type: (Shader, int, Matrix) -> None
        """Set shader uniform value (matrix 4x4)"""
        _SetShaderValueMatrix(self, _int(loc_index), mat)

    def set_value_texture(self, loc_index, texture):
        # type: (Shader, int, Texture2D) -> None
        """Set shader uniform value for texture (sampler2d)"""
        _SetShaderValueTexture(self, _int(loc_index), texture)

    def unload(self):
        # type: (Shader) -> None
        """Unload shader from GPU memory (VRAM)"""
        _UnloadShader(self)


class MaterialMap(Structure):
    """MaterialMap"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of MaterialMap elements"""
        return (MaterialMap * len(sequence))(*sequence)

    def __init__(self, texture=None, color=None, value=None):
        # type: (MaterialMap, Texture2D, Color, float) -> None
        """Initializes this MaterialMap"""
        super(MaterialMap, self).__init__(
            texture or Texture2D(),
            color or Color(),
            value or 0.0
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this MaterialMap"""
        return byref(self)

# Pointer types for MaterialMap
MaterialMapPtr = POINTER(MaterialMap)


class Material(Structure):
    """Material, includes shader and maps"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Material elements"""
        return (Material * len(sequence))(*sequence)

    @classmethod
    def load_materials(cls, file_name, material_count):
        # type: (Material, bytes | str | None, int) -> Array[Material]
        """Load materials from model file"""
        material_count = Int(material_count)
        result = _LoadMaterials(_str_in(file_name), byref(material_count))
        result = cast(result, POINTER(Material * material_count.value))[0]
        _clear_in_out()
        _push_in_out(material_count.value)
        return result

    @classmethod
    def load_default(cls):
        # type: (Material) -> Material
        """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
        return _LoadMaterialDefault()

    def __init__(self, shader=None, maps=None, params=None):
        # type: (Material, Shader, MaterialMapPtr, Float4 | list[float]) -> None
        """Initializes this Material"""
        super(Material, self).__init__(
            shader or Shader(),
            maps,
            params
        )

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Material"""
        return byref(self)

    @property
    def is_ready(self):
        """Check if a material is ready"""
        return _IsMaterialReady(self)

    def unload(self):
        # type: (Material) -> None
        """Unload material from GPU memory (VRAM)"""
        _UnloadMaterial(self)

    def set_texture(self, map_type, texture):
        # type: (MaterialPtr, int, Texture2D) -> None
        """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
        _SetMaterialTexture(self, _int(map_type), texture)

# Pointer types for Material
MaterialPtr = POINTER(Material)


class Transform(Structure):
    """Transform, vertex transformation data"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Transform elements"""
        return (Transform * len(sequence))(*sequence)

    def __init__(self, translation=None, rotation=None, scale=None):
        # type: (Transform, Vector3, Quaternion, Vector3) -> None
        """Initializes this Transform"""
        super(Transform, self).__init__(
            translation or Vector3(),
            rotation or Quaternion(),
            scale or Vector3(1.0, 1.0, 1.0)
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this Transform"""
        return byref(self)

# Pointer types for Transform
TransformPtr = POINTER(Transform)

# Pointer types for Transform
TransformPtrPtr = POINTER(TransformPtr)


class BoneInfo(Structure):
    """Bone, skeletal animation bone"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of BoneInfo elements"""
        return (BoneInfo * len(sequence))(*sequence)

    def __init__(self, name=None, parent=None):
        # type: (BoneInfo, Char32 | list[int | str] | str, int) -> None
        """Initializes this BoneInfo"""
        super(BoneInfo, self).__init__(
            name,
            parent or 0
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this BoneInfo"""
        return byref(self)

# Pointer types for BoneInfo
BoneInfoPtr = POINTER(BoneInfo)


class Model(Structure):
    """Model, meshes, materials and animation data"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Model elements"""
        return (Model * len(sequence))(*sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Model, bytes | str | None) -> Model
        """Load model from files (meshes and materials)"""
        return _LoadModel(_str_in(file_name))

    @classmethod
    def load_from_mesh(cls, mesh):
        # type: (Model, Mesh) -> Model
        """Load model from generated mesh (default material)"""
        return _LoadModelFromMesh(mesh)

    def __init__(self, transform=None, mesh_count=None, material_count=None, meshes=None, materials=None, mesh_material=None, bone_count=None, bones=None, bind_pose=None):
        # type: (Model, Matrix, int, int, MeshPtr, MaterialPtr, IntPtr, int, BoneInfoPtr, TransformPtr) -> None
        """Initializes this Model"""
        super(Model, self).__init__(
            transform,
            mesh_count or 0,
            material_count or 0,
            meshes,
            materials,
            mesh_material,
            bone_count or 0,
            bones,
            bind_pose
        )

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Model"""
        return byref(self)

    def is_animation_valid(self, anim):
        # type: (Model, ModelAnimation) -> bool
        """Check model animation skeleton match"""
        return _IsModelAnimationValid(self, anim)

    def update_animation(self, anim, frame):
        # type: (Model, ModelAnimation, int) -> None
        """Update model animation pose"""
        _UpdateModelAnimation(self, anim, _int(frame))

    def set_mesh_material(self, mesh_id, material_id):
        # type: (ModelPtr, int, int) -> None
        """Set material for a mesh"""
        _SetModelMeshMaterial(self, _int(mesh_id), _int(material_id))

    def unload(self):
        # type: (Model) -> None
        """Unload model (including meshes) from memory (RAM and/or VRAM)"""
        _UnloadModel(self)

    def get_bounding_box(self):
        # type: (Model) -> BoundingBox
        """Compute model bounding box limits (considers all meshes)"""
        return _GetModelBoundingBox(self)

    def draw(self, position, scale, tint):
        # type: (Model, Vector3, float, Color) -> None
        """Draw a model (with texture if set)"""
        _DrawModel(self, _vec3(position), _float(scale), _color(tint))

    def draw_ex(self, position, rotation_axis, rotation_angle, scale, tint):
        # type: (Model, Vector3, Vector3, float, Vector3, Color) -> None
        """Draw a model with extended parameters"""
        _DrawModelEx(self, _vec3(position), _vec3(rotation_axis), _float(rotation_angle), _vec3(scale), _color(tint))

    def draw_wires(self, position, scale, tint):
        # type: (Model, Vector3, float, Color) -> None
        """Draw a model wires (with texture if set)"""
        _DrawModelWires(self, _vec3(position), _float(scale), _color(tint))

    def draw_wires_ex(self, position, rotation_axis, rotation_angle, scale, tint):
        # type: (Model, Vector3, Vector3, float, Vector3, Color) -> None
        """Draw a model wires (with texture if set) with extended parameters"""
        _DrawModelWiresEx(self, _vec3(position), _vec3(rotation_axis), _float(rotation_angle), _vec3(scale), _color(tint))

# Pointer types for Model
ModelPtr = POINTER(Model)


class ModelAnimation(Structure):
    """ModelAnimation"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of ModelAnimation elements"""
        return (ModelAnimation * len(sequence))(*sequence)

    def __init__(self, bone_count=None, frame_count=None, bones=None, frame_poses=None, name=None):
        # type: (ModelAnimation, int, int, BoneInfoPtr, TransformPtrPtr, Char32 | list[int | str] | str) -> None
        """Initializes this ModelAnimation"""
        super(ModelAnimation, self).__init__(
            bone_count or 0,
            frame_count or 0,
            bones,
            frame_poses,
            name
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this ModelAnimation"""
        return byref(self)

# Pointer types for ModelAnimation
ModelAnimationPtr = POINTER(ModelAnimation)


class Ray(Structure):
    """Ray, ray for raycasting"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Ray elements"""
        return (Ray * len(sequence))(*sequence)

    def __init__(self, position=None, direction=None):
        # type: (Ray, Vector3, Vector3) -> None
        """Initializes this Ray"""
        super(Ray, self).__init__(
            position or Vector3(),
            direction or Vector3()
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this Ray"""
        return byref(self)


class RayCollision(Structure):
    """RayCollision, ray hit information"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of RayCollision elements"""
        return (RayCollision * len(sequence))(*sequence)

    def __init__(self, hit=None, distance=None, point=None, normal=None):
        # type: (RayCollision, bool, float, Vector3, Vector3) -> None
        """Initializes this RayCollision"""
        super(RayCollision, self).__init__(
            hit or False,
            distance or 0.0,
            point or Vector3(),
            normal or Vector3()
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this RayCollision"""
        return byref(self)


class BoundingBox(Structure):
    """BoundingBox"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of BoundingBox elements"""
        return (BoundingBox * len(sequence))(*sequence)

    def __init__(self, min_=None, max_=None):
        # type: (BoundingBox, Vector3, Vector3) -> None
        """Initializes this BoundingBox"""
        super(BoundingBox, self).__init__(
            min_ or Vector3(),
            max_ or Vector3()
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this BoundingBox"""
        return byref(self)


class Wave(Structure):
    """Wave, audio wave data"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Wave elements"""
        return (Wave * len(sequence))(*sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Wave, bytes | str | None) -> Wave
        """Load wave data from file"""
        return _LoadWave(_str_in(file_name))

    @classmethod
    def load_from_memory(cls, file_type, file_data, data_size):
        # type: (Wave, bytes | str | None, int, int) -> Wave
        """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
        return _LoadWaveFromMemory(_str_in(file_type), _int(file_data, (0, 255)), _int(data_size))

    def __init__(self, frame_count=None, sample_rate=None, sample_size=None, channels=None, data=None):
        # type: (Wave, int, int, int, int, bytes | str | None) -> None
        """Initializes this Wave"""
        super(Wave, self).__init__(
            frame_count or 0,
            sample_rate or 0,
            sample_size or 0,
            channels or 0,
            data
        )

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Wave"""
        return byref(self)

    @property
    def is_ready(self):
        """Checks if wave data is ready"""
        return _IsWaveReady(self)

    def copy(self):
        # type: (Wave) -> Wave
        """Copy a wave to a new wave"""
        return _WaveCopy(self)

    def crop(self, init_sample, final_sample):
        # type: (WavePtr, int, int) -> None
        """Crop a wave to defined samples range"""
        _WaveCrop(self, _int(init_sample), _int(final_sample))

    def format(self, sample_rate, sample_size, channels):
        # type: (WavePtr, int, int, int) -> None
        """Convert wave data to desired format"""
        _WaveFormat(self, _int(sample_rate), _int(sample_size), _int(channels))

    def format(self):
        # type: (Wave) -> FloatPtr
        """Load samples data from wave as a 32bit float data array"""
        return _LoadWaveSamples(self)

    def export(self, file_name):
        # type: (Wave, bytes | str | None) -> bool
        """Export wave data to file, returns true on success"""
        return _ExportWave(self, _str_in(file_name))

    def export_as_code(self, file_name):
        # type: (Wave, bytes | str | None) -> bool
        """Export wave sample data to code (.h), returns true on success"""
        return _ExportWaveAsCode(self, _str_in(file_name))

    def unload(self):
        # type: (Wave) -> None
        """Unload wave data"""
        _UnloadWave(self)

    def unload_samples(self):
        # type: (FloatPtr) -> None
        """Unload samples data loaded with LoadWaveSamples()"""
        _UnloadWaveSamples(self)

# Pointer types for Wave
WavePtr = POINTER(Wave)


class AudioStream(Structure):
    """AudioStream, custom audio stream"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of AudioStream elements"""
        return (AudioStream * len(sequence))(*sequence)

    @classmethod
    def load(cls, sample_rate, sample_size, channels):
        # type: (AudioStream, int, int, int) -> AudioStream
        """Load audio stream (to stream raw audio pcm data)"""
        return _LoadAudioStream(_int(sample_rate), _int(sample_size), _int(channels))

    def __init__(self, buffer=None, processor=None, sample_rate=None, sample_size=None, channels=None):
        # type: (AudioStream, rAudioBufferPtr, rAudioProcessorPtr, int, int, int) -> None
        """Initializes this AudioStream"""
        super(AudioStream, self).__init__(
            buffer,
            processor,
            sample_rate or 0,
            sample_size or 0,
            channels or 0
        )

    def __str__(self):
        return "[{} Playing: {}]".format(self.__class__.__name__, _IsAudioStreamPlaying(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this AudioStream"""
        return byref(self)

    @property
    def is_ready(self):
        """Checks if an audio stream is ready"""
        return _IsAudioStreamReady(self)

    def unload(self):
        # type: (AudioStream) -> None
        """Unload audio stream and free memory"""
        _UnloadAudioStream(self)

    def update(self, data, frame_count):
        # type: (AudioStream, bytes | str | None, int) -> None
        """Update audio stream buffers with data"""
        _UpdateAudioStream(self, data, _int(frame_count))

    def is_processed(self):
        # type: (AudioStream) -> bool
        """Check if any audio stream buffers requires refill"""
        return _IsAudioStreamProcessed(self)

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
        return _IsAudioStreamPlaying(self)

    def stop(self):
        # type: (AudioStream) -> None
        """Stop audio stream"""
        _StopAudioStream(self)

    def set_volume(self, volume):
        # type: (AudioStream, float) -> None
        """Set volume for audio stream (1.0 is max level)"""
        _SetAudioStreamVolume(self, _float(volume))

    def set_pitch(self, pitch):
        # type: (AudioStream, float) -> None
        """Set pitch for audio stream (1.0 is base level)"""
        _SetAudioStreamPitch(self, _float(pitch))

    def set_pan(self, pan):
        # type: (AudioStream, float) -> None
        """Set pan for audio stream (0.5 is centered)"""
        _SetAudioStreamPan(self, _float(pan))

    def set_buffer_size_default(self):
        # type: (int) -> None
        """Default size for new audio streams"""
        _SetAudioStreamBufferSizeDefault(_int(self))

    def set_callback(self, callback):
        # type: (AudioStream, AudioCallback) -> None
        """Audio thread callback to request new data"""
        _SetAudioStreamCallback(self, callback)

    def attach_processor(self, processor):
        # type: (AudioStream, AudioCallback) -> None
        """Attach audio stream processor to stream, receives the samples as <float>s"""
        _AttachAudioStreamProcessor(self, processor)

    def detach_processor(self, processor):
        # type: (AudioStream, AudioCallback) -> None
        """Detach audio stream processor from stream"""
        _DetachAudioStreamProcessor(self, processor)


class Sound(Structure):
    """Sound"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Sound elements"""
        return (Sound * len(sequence))(*sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Sound, bytes | str | None) -> Sound
        """Load sound from file"""
        return _LoadSound(_str_in(file_name))

    @classmethod
    def load_from_wave(cls, wave):
        # type: (Sound, Wave) -> Sound
        """Load sound from wave data"""
        return _LoadSoundFromWave(wave)

    @classmethod
    def load_alias(cls, source):
        # type: (Sound, Sound) -> Sound
        """Create a new sound that shares the same sample data as the source sound, does not own the sound data"""
        return _LoadSoundAlias(source)

    def __init__(self, stream=None, frame_count=None):
        # type: (Sound, AudioStream, int) -> None
        """Initializes this Sound"""
        super(Sound, self).__init__(
            stream or AudioStream(),
            frame_count or 0
        )

    def __str__(self):
        return "[{} Playing: {}]".format(self.__class__.__name__, _IsSoundPlaying(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Sound"""
        return byref(self)

    @property
    def is_ready(self):
        """Checks if a sound is ready"""
        return _IsSoundReady(self)

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

    def is_playing(self):
        # type: (Sound) -> bool
        """Check if a sound is currently playing"""
        return _IsSoundPlaying(self)

    def set_volume(self, volume):
        # type: (Sound, float) -> None
        """Set volume for a sound (1.0 is max level)"""
        _SetSoundVolume(self, _float(volume))

    def set_pitch(self, pitch):
        # type: (Sound, float) -> None
        """Set pitch for a sound (1.0 is base level)"""
        _SetSoundPitch(self, _float(pitch))

    def set_pan(self, pan):
        # type: (Sound, float) -> None
        """Set pan for a sound (0.5 is center)"""
        _SetSoundPan(self, _float(pan))

    def unload(self):
        # type: (Sound) -> None
        """Unload sound"""
        _UnloadSound(self)

    def unload_alias(self):
        # type: (Sound) -> None
        """Unload a sound alias (does not deallocate sample data)"""
        _UnloadSoundAlias(self)

    def update(self, data, sample_count):
        # type: (Sound, bytes | str | None, int) -> None
        """Update sound buffer with new data"""
        _UpdateSound(self, data, _int(sample_count))


class Music(Structure):
    """Music, audio stream, anything longer than ~10 seconds should be streamed"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of Music elements"""
        return (Music * len(sequence))(*sequence)

    @classmethod
    def load(cls, file_name):
        # type: (Music, bytes | str | None) -> Music
        """Load music stream from file"""
        return _LoadMusicStream(_str_in(file_name))

    @classmethod
    def load_from_memory(cls, file_type, data, data_size):
        # type: (Music, bytes | str | None, int, int) -> Music
        """Load music stream from data"""
        return _LoadMusicStreamFromMemory(_str_in(file_type), _int(data, (0, 255)), _int(data_size))

    def __init__(self, stream=None, frame_count=None, looping=None, ctx_type=None, ctx_data=None):
        # type: (Music, AudioStream, int, bool, int, bytes | str | None) -> None
        """Initializes this Music"""
        super(Music, self).__init__(
            stream or AudioStream(),
            frame_count or 0,
            looping or False,
            ctx_type or 0,
            ctx_data
        )

    def __str__(self):
        return "[{} at {}]".format(self.__class__.__name__, id(self))

    def __repr__(self):
        return self.__str__()

    @property
    def byref(self):
        """Gets a pointer to this Music"""
        return byref(self)

    @property
    def is_ready(self):
        """Checks if a music stream is ready"""
        return _IsMusicReady(self)

    @property
    def time_length(self):
        """Get music time length (in seconds)"""
        return _GetMusicTimeLength(self)

    @property
    def time_played(self):
        """Get current music time played (in seconds)"""
        return _GetMusicTimePlayed(self)

    def play(self):
        # type: (Music) -> None
        """Start music playing"""
        _PlayMusicStream(self)

    def is_playing(self):
        # type: (Music) -> bool
        """Check if music is playing"""
        return _IsMusicStreamPlaying(self)

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
        _SeekMusicStream(self, _float(position))

    def set_volume(self, volume):
        # type: (Music, float) -> None
        """Set volume for music (1.0 is max level)"""
        _SetMusicVolume(self, _float(volume))

    def set_pitch(self, pitch):
        # type: (Music, float) -> None
        """Set pitch for a music (1.0 is base level)"""
        _SetMusicPitch(self, _float(pitch))

    def set_pan(self, pan):
        # type: (Music, float) -> None
        """Set pan for a music (0.5 is center)"""
        _SetMusicPan(self, _float(pan))

    def unload(self):
        # type: (Music) -> None
        """Unload music stream"""
        _UnloadMusicStream(self)


class VrDeviceInfo(Structure):
    """VrDeviceInfo, Head-Mounted-Display device parameters"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of VrDeviceInfo elements"""
        return (VrDeviceInfo * len(sequence))(*sequence)

    def __init__(self, h_resolution=None, v_resolution=None, h_screen_size=None, v_screen_size=None, v_screen_center=None, eye_to_screen_distance=None, lens_separation_distance=None, interpupillary_distance=None, lens_distortion_values=None, chroma_ab_correction=None):
        # type: (VrDeviceInfo, int, int, float, float, float, float, float, float, Float4 | list[float], Float4 | list[float]) -> None
        """Initializes this VrDeviceInfo"""
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

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this VrDeviceInfo"""
        return byref(self)


class VrStereoConfig(Structure):
    """VrStereoConfig, VR stereo rendering configuration for simulator"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of VrStereoConfig elements"""
        return (VrStereoConfig * len(sequence))(*sequence)

    @classmethod
    def load(cls, device):
        # type: (VrStereoConfig, VrDeviceInfo) -> VrStereoConfig
        """Load VR stereo config for VR simulator device parameters"""
        return _LoadVrStereoConfig(device)

    def __init__(self, projection=None, view_offset=None, left_lens_center=None, right_lens_center=None, left_screen_center=None, right_screen_center=None, scale=None, scale_in=None):
        # type: (VrStereoConfig, Matrix2 | list[Matrix], Matrix2 | list[Matrix], Float2 | list[float], Float2 | list[float], Float2 | list[float], Float2 | list[float], Float2 | list[float], Float2 | list[float]) -> None
        """Initializes this VrStereoConfig"""
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

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    def __enter__(self):
        # type: (VrStereoConfig) -> None
        """Begin stereo rendering (requires VR simulator)"""
        _BeginVrStereoMode(self)

    def __exit__():
        # type: () -> None
        """End stereo rendering (requires VR simulator)"""
        _EndVrStereoMode()

    @property
    def byref(self):
        """Gets a pointer to this VrStereoConfig"""
        return byref(self)

    def unload(self):
        # type: (VrStereoConfig) -> None
        """Unload VR stereo config"""
        _UnloadVrStereoConfig(self)


class FilePathList(Structure):
    """File path list"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of FilePathList elements"""
        return (FilePathList * len(sequence))(*sequence)

    def __init__(self, capacity=None, count=None, paths=None):
        # type: (FilePathList, int, int, CharPtrPtr | list[CharPtr | str] | None) -> None
        """Initializes this FilePathList"""
        super(FilePathList, self).__init__(
            capacity or 0,
            count or 0,
            paths
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this FilePathList"""
        return byref(self)


class AutomationEvent(Structure):
    """Automation event"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of AutomationEvent elements"""
        return (AutomationEvent * len(sequence))(*sequence)

    def __init__(self, frame=None, type_=None, params=None):
        # type: (AutomationEvent, int, int, Int4 | list[int]) -> None
        """Initializes this AutomationEvent"""
        super(AutomationEvent, self).__init__(
            frame or 0,
            type_ or 0,
            params
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this AutomationEvent"""
        return byref(self)

# Pointer types for AutomationEvent
AutomationEventPtr = POINTER(AutomationEvent)


class AutomationEventList(Structure):
    """Automation event list"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of AutomationEventList elements"""
        return (AutomationEventList * len(sequence))(*sequence)

    def __init__(self, capacity=None, count=None, events=None):
        # type: (AutomationEventList, int, int, AutomationEventPtr) -> None
        """Initializes this AutomationEventList"""
        super(AutomationEventList, self).__init__(
            capacity or 0,
            count or 0,
            events
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this AutomationEventList"""
        return byref(self)

# Pointer types for AutomationEventList
AutomationEventListPtr = POINTER(AutomationEventList)

class rAudioBuffer(Structure):
    """Opaque structure type"""

    pass

rAudioBufferPtr = POINTER(rAudioBuffer)
class rAudioProcessor(Structure):
    """Opaque structure type"""

    pass

rAudioProcessorPtr = POINTER(rAudioProcessor)

# rlapi::raymath
# ------------------------------------------------------------------------------

class float3(Structure):
    """NOTE: Helper types to be used instead of array return types for *ToFloat functions"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of float3 elements"""
        return (float3 * len(sequence))(*sequence)

    def __init__(self, v=None):
        # type: (float3, Float3 | list[float]) -> None
        """Initializes this float3"""
        super(float3, self).__init__(
            v
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this float3"""
        return byref(self)


class float16(Structure):
    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of float16 elements"""
        return (float16 * len(sequence))(*sequence)

    def __init__(self, v=None):
        # type: (float16, Float16 | list[float]) -> None
        """Initializes this float16"""
        super(float16, self).__init__(
            v
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this float16"""
        return byref(self)


# rlapi::rlgl
# ------------------------------------------------------------------------------

class rlVertexBuffer(Structure):
    """Dynamic vertex buffers (position + texcoords + colors + indices arrays)"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of rlVertexBuffer elements"""
        return (rlVertexBuffer * len(sequence))(*sequence)

    def __init__(self, element_count=None, vertices=None, texcoords=None, colors=None, indices=None, vao_id=None, vbo_id=None):
        # type: (rlVertexBuffer, int, FloatPtr, FloatPtr, int, UShortPtr, int, UInt4 | list[int]) -> None
        """Initializes this rlVertexBuffer"""
        super(rlVertexBuffer, self).__init__(
            element_count,
            vertices,
            texcoords,
            colors,
            indices,
            vao_id,
            vbo_id
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this rlVertexBuffer"""
        return byref(self)

# Pointer types for rlVertexBuffer
rlVertexBufferPtr = POINTER(rlVertexBuffer)


class rlDrawCall(Structure):
    """of those state-change happens (this is done in core module)"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of rlDrawCall elements"""
        return (rlDrawCall * len(sequence))(*sequence)

    def __init__(self, mode=None, vertex_count=None, vertex_alignment=None, texture_id=None):
        # type: (rlDrawCall, int, int, int, int) -> None
        """Initializes this rlDrawCall"""
        super(rlDrawCall, self).__init__(
            mode,
            vertex_count,
            vertex_alignment,
            texture_id
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this rlDrawCall"""
        return byref(self)

# Pointer types for rlDrawCall
rlDrawCallPtr = POINTER(rlDrawCall)


class rlRenderBatch(Structure):
    """rlRenderBatch type"""

    @classmethod
    def array_of(cls, sequence):
        """Creates and returns an array of rlRenderBatch elements"""
        return (rlRenderBatch * len(sequence))(*sequence)

    def __init__(self, buffer_count=None, current_buffer=None, vertex_buffer=None, draws=None, draw_counter=None, current_depth=None):
        # type: (rlRenderBatch, int, int, rlVertexBufferPtr, rlDrawCallPtr, int, float) -> None
        """Initializes this rlRenderBatch"""
        super(rlRenderBatch, self).__init__(
            buffer_count,
            current_buffer,
            vertex_buffer,
            draws,
            draw_counter,
            current_depth
        )

    def __str__(self):
        return "[{} at {}]".format(_clsname(self), id(self))

    def __repr__(self):
        return "{}()".format(_clsname(self))

    @property
    def byref(self):
        """Gets a pointer to this rlRenderBatch"""
        return byref(self)

# Pointer types for rlRenderBatch
rlRenderBatchPtr = POINTER(rlRenderBatch)


# endregion (structures)

# region CALLBACKS

# rlapi::raylib
# ------------------------------------------------------------------------------


# Logging: Redirect trace log messages
TraceLogCallback = CFUNCTYPE(Int, CharPtr)


# FileIO: Load binary data
LoadFileDataCallback = CFUNCTYPE(CharPtr, IntPtr)


# FileIO: Save binary data
SaveFileDataCallback = CFUNCTYPE(CharPtr, VoidPtr, Int)


# FileIO: Load text data
LoadFileTextCallback = CFUNCTYPE(CharPtr)


# FileIO: Save text data
SaveFileTextCallback = CFUNCTYPE(CharPtr, CharPtr)


AudioCallback = CFUNCTYPE(VoidPtr, UInt)

# endregion (callbacks)

# region INTERNALS

# rlapi::raylib
# ------------------------------------------------------------------------------

Vector2._fields_ = [
    ('x', c_float),
    ('y', c_float),
]


Vector3._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
]


Vector4._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('w', c_float),
]


Matrix._fields_ = [
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


Color._fields_ = [
    ('r', c_ubyte),
    ('g', c_ubyte),
    ('b', c_ubyte),
    ('a', c_ubyte),
]


Rectangle._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('width', c_float),
    ('height', c_float),
]


Image._fields_ = [
    ('data', c_void_p),
    ('width', c_int),
    ('height', c_int),
    ('mipmaps', c_int),
    ('format', c_int),
]


Texture._fields_ = [
    ('id', c_uint),
    ('width', c_int),
    ('height', c_int),
    ('mipmaps', c_int),
    ('format', c_int),
]


RenderTexture._fields_ = [
    ('id', c_uint),
    ('texture', Texture),
    ('depth', Texture),
]


NPatchInfo._fields_ = [
    ('source', Rectangle),
    ('left', c_int),
    ('top', c_int),
    ('right', c_int),
    ('bottom', c_int),
    ('layout', c_int),
]


GlyphInfo._fields_ = [
    ('value', c_int),
    ('offset_x', c_int),
    ('offset_y', c_int),
    ('advance_x', c_int),
    ('image', Image),
]


Font._fields_ = [
    ('base_size', c_int),
    ('glyph_count', c_int),
    ('glyph_padding', c_int),
    ('texture', Texture2D),
    ('recs', RectanglePtr),
    ('glyphs', GlyphInfoPtr),
]


Camera3D._fields_ = [
    ('position', Vector3),
    ('target', Vector3),
    ('up', Vector3),
    ('fovy', c_float),
    ('projection', c_int),
]


Camera2D._fields_ = [
    ('offset', Vector2),
    ('target', Vector2),
    ('rotation', c_float),
    ('zoom', c_float),
]


Mesh._fields_ = [
    ('vertex_count', c_int),
    ('triangle_count', c_int),
    ('vertices', POINTER(c_float)),
    ('texcoords', POINTER(c_float)),
    ('texcoords2', POINTER(c_float)),
    ('normals', POINTER(c_float)),
    ('tangents', POINTER(c_float)),
    ('colors', c_ubyte),
    ('indices', POINTER(c_ushort)),
    ('anim_vertices', POINTER(c_float)),
    ('anim_normals', POINTER(c_float)),
    ('bone_ids', c_ubyte),
    ('bone_weights', POINTER(c_float)),
    ('vao_id', c_uint),
    ('vbo_id', POINTER(c_uint)),
]


Shader._fields_ = [
    ('id', c_uint),
    ('locs', POINTER(c_int)),
]


MaterialMap._fields_ = [
    ('texture', Texture2D),
    ('color', Color),
    ('value', c_float),
]


Material._fields_ = [
    ('shader', Shader),
    ('maps', MaterialMapPtr),
    ('params', c_float * 4),
]


Transform._fields_ = [
    ('translation', Vector3),
    ('rotation', Quaternion),
    ('scale', Vector3),
]


BoneInfo._fields_ = [
    ('name', c_char * 32),
    ('parent', c_int),
]


Model._fields_ = [
    ('transform', Matrix),
    ('mesh_count', c_int),
    ('material_count', c_int),
    ('meshes', MeshPtr),
    ('materials', MaterialPtr),
    ('mesh_material', POINTER(c_int)),
    ('bone_count', c_int),
    ('bones', BoneInfoPtr),
    ('bind_pose', TransformPtr),
]


ModelAnimation._fields_ = [
    ('bone_count', c_int),
    ('frame_count', c_int),
    ('bones', BoneInfoPtr),
    ('frame_poses', TransformPtrPtr),
    ('name', c_char * 32),
]


Ray._fields_ = [
    ('position', Vector3),
    ('direction', Vector3),
]


RayCollision._fields_ = [
    ('hit', c_bool),
    ('distance', c_float),
    ('point', Vector3),
    ('normal', Vector3),
]


BoundingBox._fields_ = [
    ('min', Vector3),
    ('max', Vector3),
]


Wave._fields_ = [
    ('frame_count', c_uint),
    ('sample_rate', c_uint),
    ('sample_size', c_uint),
    ('channels', c_uint),
    ('data', c_void_p),
]


AudioStream._fields_ = [
    ('buffer', rAudioBufferPtr),
    ('processor', rAudioProcessorPtr),
    ('sample_rate', c_uint),
    ('sample_size', c_uint),
    ('channels', c_uint),
]


Sound._fields_ = [
    ('stream', AudioStream),
    ('frame_count', c_uint),
]


Music._fields_ = [
    ('stream', AudioStream),
    ('frame_count', c_uint),
    ('looping', c_bool),
    ('ctx_type', c_int),
    ('ctx_data', c_void_p),
]


VrDeviceInfo._fields_ = [
    ('h_resolution', c_int),
    ('v_resolution', c_int),
    ('h_screen_size', c_float),
    ('v_screen_size', c_float),
    ('v_screen_center', c_float),
    ('eye_to_screen_distance', c_float),
    ('lens_separation_distance', c_float),
    ('interpupillary_distance', c_float),
    ('lens_distortion_values', c_float * 4),
    ('chroma_ab_correction', c_float * 4),
]


VrStereoConfig._fields_ = [
    ('projection', Matrix * 2),
    ('view_offset', Matrix * 2),
    ('left_lens_center', c_float * 2),
    ('right_lens_center', c_float * 2),
    ('left_screen_center', c_float * 2),
    ('right_screen_center', c_float * 2),
    ('scale', c_float * 2),
    ('scale_in', c_float * 2),
]


FilePathList._fields_ = [
    ('capacity', c_uint),
    ('count', c_uint),
    ('paths', POINTER(c_char_p)),
]


AutomationEvent._fields_ = [
    ('frame', c_uint),
    ('type', c_uint),
    ('params', c_int * 4),
]


AutomationEventList._fields_ = [
    ('capacity', c_uint),
    ('count', c_uint),
    ('events', AutomationEventPtr),
]


_InitWindow = _wrap(rlapi.InitWindow, None, Int, Int, CharPtr)
_CloseWindow = _wrap(rlapi.CloseWindow, None)
_WindowShouldClose = _wrap(rlapi.WindowShouldClose, Bool)
_IsWindowReady = _wrap(rlapi.IsWindowReady, Bool)
_IsWindowFullscreen = _wrap(rlapi.IsWindowFullscreen, Bool)
_IsWindowHidden = _wrap(rlapi.IsWindowHidden, Bool)
_IsWindowMinimized = _wrap(rlapi.IsWindowMinimized, Bool)
_IsWindowMaximized = _wrap(rlapi.IsWindowMaximized, Bool)
_IsWindowFocused = _wrap(rlapi.IsWindowFocused, Bool)
_IsWindowResized = _wrap(rlapi.IsWindowResized, Bool)
_IsWindowState = _wrap(rlapi.IsWindowState, Bool, UInt)
_SetWindowState = _wrap(rlapi.SetWindowState, None, UInt)
_ClearWindowState = _wrap(rlapi.ClearWindowState, None, UInt)
_ToggleFullscreen = _wrap(rlapi.ToggleFullscreen, None)
_ToggleBorderlessWindowed = _wrap(rlapi.ToggleBorderlessWindowed, None)
_MaximizeWindow = _wrap(rlapi.MaximizeWindow, None)
_MinimizeWindow = _wrap(rlapi.MinimizeWindow, None)
_RestoreWindow = _wrap(rlapi.RestoreWindow, None)
_SetWindowIcon = _wrap(rlapi.SetWindowIcon, None, Image)
_SetWindowIcons = _wrap(rlapi.SetWindowIcons, None, ImagePtr, Int)
_SetWindowTitle = _wrap(rlapi.SetWindowTitle, None, CharPtr)
_SetWindowPosition = _wrap(rlapi.SetWindowPosition, None, Int, Int)
_SetWindowMonitor = _wrap(rlapi.SetWindowMonitor, None, Int)
_SetWindowMinSize = _wrap(rlapi.SetWindowMinSize, None, Int, Int)
_SetWindowMaxSize = _wrap(rlapi.SetWindowMaxSize, None, Int, Int)
_SetWindowSize = _wrap(rlapi.SetWindowSize, None, Int, Int)
_SetWindowOpacity = _wrap(rlapi.SetWindowOpacity, None, Float)
_SetWindowFocused = _wrap(rlapi.SetWindowFocused, None)
_GetWindowHandle = _wrap(rlapi.GetWindowHandle, VoidPtr)
_GetScreenWidth = _wrap(rlapi.GetScreenWidth, Int)
_GetScreenHeight = _wrap(rlapi.GetScreenHeight, Int)
_GetRenderWidth = _wrap(rlapi.GetRenderWidth, Int)
_GetRenderHeight = _wrap(rlapi.GetRenderHeight, Int)
_GetMonitorCount = _wrap(rlapi.GetMonitorCount, Int)
_GetCurrentMonitor = _wrap(rlapi.GetCurrentMonitor, Int)
_GetMonitorPosition = _wrap(rlapi.GetMonitorPosition, Vector2, Int)
_GetMonitorWidth = _wrap(rlapi.GetMonitorWidth, Int, Int)
_GetMonitorHeight = _wrap(rlapi.GetMonitorHeight, Int, Int)
_GetMonitorPhysicalWidth = _wrap(rlapi.GetMonitorPhysicalWidth, Int, Int)
_GetMonitorPhysicalHeight = _wrap(rlapi.GetMonitorPhysicalHeight, Int, Int)
_GetMonitorRefreshRate = _wrap(rlapi.GetMonitorRefreshRate, Int, Int)
_GetWindowPosition = _wrap(rlapi.GetWindowPosition, Vector2)
_GetWindowScaleDPI = _wrap(rlapi.GetWindowScaleDPI, Vector2)
_GetMonitorName = _wrap(rlapi.GetMonitorName, CharPtr, Int)
_SetClipboardText = _wrap(rlapi.SetClipboardText, None, CharPtr)
_GetClipboardText = _wrap(rlapi.GetClipboardText, CharPtr)
_EnableEventWaiting = _wrap(rlapi.EnableEventWaiting, None)
_DisableEventWaiting = _wrap(rlapi.DisableEventWaiting, None)
_ShowCursor = _wrap(rlapi.ShowCursor, None)
_HideCursor = _wrap(rlapi.HideCursor, None)
_IsCursorHidden = _wrap(rlapi.IsCursorHidden, Bool)
_EnableCursor = _wrap(rlapi.EnableCursor, None)
_DisableCursor = _wrap(rlapi.DisableCursor, None)
_IsCursorOnScreen = _wrap(rlapi.IsCursorOnScreen, Bool)
_ClearBackground = _wrap(rlapi.ClearBackground, None, Color)
_BeginDrawing = _wrap(rlapi.BeginDrawing, None)
_EndDrawing = _wrap(rlapi.EndDrawing, None)
_BeginMode2D = _wrap(rlapi.BeginMode2D, None, Camera2D)
_EndMode2D = _wrap(rlapi.EndMode2D, None)
_BeginMode3D = _wrap(rlapi.BeginMode3D, None, Camera3D)
_EndMode3D = _wrap(rlapi.EndMode3D, None)
_BeginTextureMode = _wrap(rlapi.BeginTextureMode, None, RenderTexture2D)
_EndTextureMode = _wrap(rlapi.EndTextureMode, None)
_BeginShaderMode = _wrap(rlapi.BeginShaderMode, None, Shader)
_EndShaderMode = _wrap(rlapi.EndShaderMode, None)
_BeginBlendMode = _wrap(rlapi.BeginBlendMode, None, Int)
_EndBlendMode = _wrap(rlapi.EndBlendMode, None)
_BeginScissorMode = _wrap(rlapi.BeginScissorMode, None, Int, Int, Int, Int)
_EndScissorMode = _wrap(rlapi.EndScissorMode, None)
_BeginVrStereoMode = _wrap(rlapi.BeginVrStereoMode, None, VrStereoConfig)
_EndVrStereoMode = _wrap(rlapi.EndVrStereoMode, None)
_LoadVrStereoConfig = _wrap(rlapi.LoadVrStereoConfig, VrStereoConfig, VrDeviceInfo)
_UnloadVrStereoConfig = _wrap(rlapi.UnloadVrStereoConfig, None, VrStereoConfig)
_LoadShader = _wrap(rlapi.LoadShader, Shader, CharPtr, CharPtr)
_LoadShaderFromMemory = _wrap(rlapi.LoadShaderFromMemory, Shader, CharPtr, CharPtr)
_IsShaderReady = _wrap(rlapi.IsShaderReady, Bool, Shader)
_GetShaderLocation = _wrap(rlapi.GetShaderLocation, Int, Shader, CharPtr)
_GetShaderLocationAttrib = _wrap(rlapi.GetShaderLocationAttrib, Int, Shader, CharPtr)
_SetShaderValue = _wrap(rlapi.SetShaderValue, None, Shader, Int, VoidPtr, Int)
_SetShaderValueV = _wrap(rlapi.SetShaderValueV, None, Shader, Int, VoidPtr, Int, Int)
_SetShaderValueMatrix = _wrap(rlapi.SetShaderValueMatrix, None, Shader, Int, Matrix)
_SetShaderValueTexture = _wrap(rlapi.SetShaderValueTexture, None, Shader, Int, Texture2D)
_UnloadShader = _wrap(rlapi.UnloadShader, None, Shader)
_GetMouseRay = _wrap(rlapi.GetMouseRay, Ray, Vector2, Camera)
_GetCameraMatrix = _wrap(rlapi.GetCameraMatrix, Matrix, Camera)
_GetCameraMatrix2D = _wrap(rlapi.GetCameraMatrix2D, Matrix, Camera2D)
_GetWorldToScreen = _wrap(rlapi.GetWorldToScreen, Vector2, Vector3, Camera)
_GetScreenToWorld2D = _wrap(rlapi.GetScreenToWorld2D, Vector2, Vector2, Camera2D)
_GetWorldToScreenEx = _wrap(rlapi.GetWorldToScreenEx, Vector2, Vector3, Camera, Int, Int)
_GetWorldToScreen2D = _wrap(rlapi.GetWorldToScreen2D, Vector2, Vector2, Camera2D)
_SetTargetFPS = _wrap(rlapi.SetTargetFPS, None, Int)
_GetFrameTime = _wrap(rlapi.GetFrameTime, Float)
_GetTime = _wrap(rlapi.GetTime, Double)
_GetFPS = _wrap(rlapi.GetFPS, Int)
_SwapScreenBuffer = _wrap(rlapi.SwapScreenBuffer, None)
_PollInputEvents = _wrap(rlapi.PollInputEvents, None)
_WaitTime = _wrap(rlapi.WaitTime, None, Double)
_SetRandomSeed = _wrap(rlapi.SetRandomSeed, None, UInt)
_GetRandomValue = _wrap(rlapi.GetRandomValue, Int, Int, Int)
_LoadRandomSequence = _wrap(rlapi.LoadRandomSequence, IntPtr, UInt, Int, Int)
_UnloadRandomSequence = _wrap(rlapi.UnloadRandomSequence, None, IntPtr)
_TakeScreenshot = _wrap(rlapi.TakeScreenshot, None, CharPtr)
_SetConfigFlags = _wrap(rlapi.SetConfigFlags, None, UInt)
_OpenURL = _wrap(rlapi.OpenURL, None, CharPtr)
_TraceLog = _wrap(rlapi.TraceLog, None, Int, CharPtr)
_SetTraceLogLevel = _wrap(rlapi.SetTraceLogLevel, None, Int)
_MemAlloc = _wrap(rlapi.MemAlloc, VoidPtr, UInt)
_MemRealloc = _wrap(rlapi.MemRealloc, VoidPtr, VoidPtr, UInt)
_MemFree = _wrap(rlapi.MemFree, None, VoidPtr)
_SetTraceLogCallback = _wrap(rlapi.SetTraceLogCallback, None, TraceLogCallback)
_SetLoadFileDataCallback = _wrap(rlapi.SetLoadFileDataCallback, None, LoadFileDataCallback)
_SetSaveFileDataCallback = _wrap(rlapi.SetSaveFileDataCallback, None, SaveFileDataCallback)
_SetLoadFileTextCallback = _wrap(rlapi.SetLoadFileTextCallback, None, LoadFileTextCallback)
_SetSaveFileTextCallback = _wrap(rlapi.SetSaveFileTextCallback, None, SaveFileTextCallback)
_LoadFileData = _wrap(rlapi.LoadFileData, UCharPtr, CharPtr, IntPtr)
_UnloadFileData = _wrap(rlapi.UnloadFileData, None, UCharPtr)
_SaveFileData = _wrap(rlapi.SaveFileData, Bool, CharPtr, VoidPtr, Int)
_ExportDataAsCode = _wrap(rlapi.ExportDataAsCode, Bool, UCharPtr, Int, CharPtr)
_LoadFileText = _wrap(rlapi.LoadFileText, CharPtr, CharPtr)
_UnloadFileText = _wrap(rlapi.UnloadFileText, None, CharPtr)
_SaveFileText = _wrap(rlapi.SaveFileText, Bool, CharPtr, CharPtr)
_FileExists = _wrap(rlapi.FileExists, Bool, CharPtr)
_DirectoryExists = _wrap(rlapi.DirectoryExists, Bool, CharPtr)
_IsFileExtension = _wrap(rlapi.IsFileExtension, Bool, CharPtr, CharPtr)
_GetFileLength = _wrap(rlapi.GetFileLength, Int, CharPtr)
_GetFileExtension = _wrap(rlapi.GetFileExtension, CharPtr, CharPtr)
_GetFileName = _wrap(rlapi.GetFileName, CharPtr, CharPtr)
_GetFileNameWithoutExt = _wrap(rlapi.GetFileNameWithoutExt, CharPtr, CharPtr)
_GetDirectoryPath = _wrap(rlapi.GetDirectoryPath, CharPtr, CharPtr)
_GetPrevDirectoryPath = _wrap(rlapi.GetPrevDirectoryPath, CharPtr, CharPtr)
_GetWorkingDirectory = _wrap(rlapi.GetWorkingDirectory, CharPtr)
_GetApplicationDirectory = _wrap(rlapi.GetApplicationDirectory, CharPtr)
_ChangeDirectory = _wrap(rlapi.ChangeDirectory, Bool, CharPtr)
_IsPathFile = _wrap(rlapi.IsPathFile, Bool, CharPtr)
_LoadDirectoryFiles = _wrap(rlapi.LoadDirectoryFiles, FilePathList, CharPtr)
_LoadDirectoryFilesEx = _wrap(rlapi.LoadDirectoryFilesEx, FilePathList, CharPtr, CharPtr, Bool)
_UnloadDirectoryFiles = _wrap(rlapi.UnloadDirectoryFiles, None, FilePathList)
_IsFileDropped = _wrap(rlapi.IsFileDropped, Bool)
_LoadDroppedFiles = _wrap(rlapi.LoadDroppedFiles, FilePathList)
_UnloadDroppedFiles = _wrap(rlapi.UnloadDroppedFiles, None, FilePathList)
_GetFileModTime = _wrap(rlapi.GetFileModTime, Long, CharPtr)
_CompressData = _wrap(rlapi.CompressData, UCharPtr, UCharPtr, Int, IntPtr)
_DecompressData = _wrap(rlapi.DecompressData, UCharPtr, UCharPtr, Int, IntPtr)
_EncodeDataBase64 = _wrap(rlapi.EncodeDataBase64, CharPtr, UCharPtr, Int, IntPtr)
_DecodeDataBase64 = _wrap(rlapi.DecodeDataBase64, UCharPtr, UCharPtr, IntPtr)
_LoadAutomationEventList = _wrap(rlapi.LoadAutomationEventList, AutomationEventList, CharPtr)
_UnloadAutomationEventList = _wrap(rlapi.UnloadAutomationEventList, None, AutomationEventListPtr)
_ExportAutomationEventList = _wrap(rlapi.ExportAutomationEventList, Bool, AutomationEventList, CharPtr)
_SetAutomationEventList = _wrap(rlapi.SetAutomationEventList, None, AutomationEventListPtr)
_SetAutomationEventBaseFrame = _wrap(rlapi.SetAutomationEventBaseFrame, None, Int)
_StartAutomationEventRecording = _wrap(rlapi.StartAutomationEventRecording, None)
_StopAutomationEventRecording = _wrap(rlapi.StopAutomationEventRecording, None)
_PlayAutomationEvent = _wrap(rlapi.PlayAutomationEvent, None, AutomationEvent)
_IsKeyPressed = _wrap(rlapi.IsKeyPressed, Bool, Int)
_IsKeyPressedRepeat = _wrap(rlapi.IsKeyPressedRepeat, Bool, Int)
_IsKeyDown = _wrap(rlapi.IsKeyDown, Bool, Int)
_IsKeyReleased = _wrap(rlapi.IsKeyReleased, Bool, Int)
_IsKeyUp = _wrap(rlapi.IsKeyUp, Bool, Int)
_GetKeyPressed = _wrap(rlapi.GetKeyPressed, Int)
_GetCharPressed = _wrap(rlapi.GetCharPressed, Int)
_SetExitKey = _wrap(rlapi.SetExitKey, None, Int)
_IsGamepadAvailable = _wrap(rlapi.IsGamepadAvailable, Bool, Int)
_GetGamepadName = _wrap(rlapi.GetGamepadName, CharPtr, Int)
_IsGamepadButtonPressed = _wrap(rlapi.IsGamepadButtonPressed, Bool, Int, Int)
_IsGamepadButtonDown = _wrap(rlapi.IsGamepadButtonDown, Bool, Int, Int)
_IsGamepadButtonReleased = _wrap(rlapi.IsGamepadButtonReleased, Bool, Int, Int)
_IsGamepadButtonUp = _wrap(rlapi.IsGamepadButtonUp, Bool, Int, Int)
_GetGamepadButtonPressed = _wrap(rlapi.GetGamepadButtonPressed, Int)
_GetGamepadAxisCount = _wrap(rlapi.GetGamepadAxisCount, Int, Int)
_GetGamepadAxisMovement = _wrap(rlapi.GetGamepadAxisMovement, Float, Int, Int)
_SetGamepadMappings = _wrap(rlapi.SetGamepadMappings, Int, CharPtr)
_IsMouseButtonPressed = _wrap(rlapi.IsMouseButtonPressed, Bool, Int)
_IsMouseButtonDown = _wrap(rlapi.IsMouseButtonDown, Bool, Int)
_IsMouseButtonReleased = _wrap(rlapi.IsMouseButtonReleased, Bool, Int)
_IsMouseButtonUp = _wrap(rlapi.IsMouseButtonUp, Bool, Int)
_GetMouseX = _wrap(rlapi.GetMouseX, Int)
_GetMouseY = _wrap(rlapi.GetMouseY, Int)
_GetMousePosition = _wrap(rlapi.GetMousePosition, Vector2)
_GetMouseDelta = _wrap(rlapi.GetMouseDelta, Vector2)
_SetMousePosition = _wrap(rlapi.SetMousePosition, None, Int, Int)
_SetMouseOffset = _wrap(rlapi.SetMouseOffset, None, Int, Int)
_SetMouseScale = _wrap(rlapi.SetMouseScale, None, Float, Float)
_GetMouseWheelMove = _wrap(rlapi.GetMouseWheelMove, Float)
_GetMouseWheelMoveV = _wrap(rlapi.GetMouseWheelMoveV, Vector2)
_SetMouseCursor = _wrap(rlapi.SetMouseCursor, None, Int)
_GetTouchX = _wrap(rlapi.GetTouchX, Int)
_GetTouchY = _wrap(rlapi.GetTouchY, Int)
_GetTouchPosition = _wrap(rlapi.GetTouchPosition, Vector2, Int)
_GetTouchPointId = _wrap(rlapi.GetTouchPointId, Int, Int)
_GetTouchPointCount = _wrap(rlapi.GetTouchPointCount, Int)
_SetGesturesEnabled = _wrap(rlapi.SetGesturesEnabled, None, UInt)
_IsGestureDetected = _wrap(rlapi.IsGestureDetected, Bool, UInt)
_GetGestureDetected = _wrap(rlapi.GetGestureDetected, Int)
_GetGestureHoldDuration = _wrap(rlapi.GetGestureHoldDuration, Float)
_GetGestureDragVector = _wrap(rlapi.GetGestureDragVector, Vector2)
_GetGestureDragAngle = _wrap(rlapi.GetGestureDragAngle, Float)
_GetGesturePinchVector = _wrap(rlapi.GetGesturePinchVector, Vector2)
_GetGesturePinchAngle = _wrap(rlapi.GetGesturePinchAngle, Float)
_UpdateCamera = _wrap(rlapi.UpdateCamera, None, CameraPtr, Int)
_UpdateCameraPro = _wrap(rlapi.UpdateCameraPro, None, CameraPtr, Vector3, Vector3, Float)
_SetShapesTexture = _wrap(rlapi.SetShapesTexture, None, Texture2D, Rectangle)
_DrawPixel = _wrap(rlapi.DrawPixel, None, Int, Int, Color)
_DrawPixelV = _wrap(rlapi.DrawPixelV, None, Vector2, Color)
_DrawLine = _wrap(rlapi.DrawLine, None, Int, Int, Int, Int, Color)
_DrawLineV = _wrap(rlapi.DrawLineV, None, Vector2, Vector2, Color)
_DrawLineEx = _wrap(rlapi.DrawLineEx, None, Vector2, Vector2, Float, Color)
_DrawLineStrip = _wrap(rlapi.DrawLineStrip, None, Vector2Ptr, Int, Color)
_DrawLineBezier = _wrap(rlapi.DrawLineBezier, None, Vector2, Vector2, Float, Color)
_DrawCircle = _wrap(rlapi.DrawCircle, None, Int, Int, Float, Color)
_DrawCircleSector = _wrap(rlapi.DrawCircleSector, None, Vector2, Float, Float, Float, Int, Color)
_DrawCircleSectorLines = _wrap(rlapi.DrawCircleSectorLines, None, Vector2, Float, Float, Float, Int, Color)
_DrawCircleGradient = _wrap(rlapi.DrawCircleGradient, None, Int, Int, Float, Color, Color)
_DrawCircleV = _wrap(rlapi.DrawCircleV, None, Vector2, Float, Color)
_DrawCircleLines = _wrap(rlapi.DrawCircleLines, None, Int, Int, Float, Color)
_DrawCircleLinesV = _wrap(rlapi.DrawCircleLinesV, None, Vector2, Float, Color)
_DrawEllipse = _wrap(rlapi.DrawEllipse, None, Int, Int, Float, Float, Color)
_DrawEllipseLines = _wrap(rlapi.DrawEllipseLines, None, Int, Int, Float, Float, Color)
_DrawRing = _wrap(rlapi.DrawRing, None, Vector2, Float, Float, Float, Float, Int, Color)
_DrawRingLines = _wrap(rlapi.DrawRingLines, None, Vector2, Float, Float, Float, Float, Int, Color)
_DrawRectangle = _wrap(rlapi.DrawRectangle, None, Int, Int, Int, Int, Color)
_DrawRectangleV = _wrap(rlapi.DrawRectangleV, None, Vector2, Vector2, Color)
_DrawRectangleRec = _wrap(rlapi.DrawRectangleRec, None, Rectangle, Color)
_DrawRectanglePro = _wrap(rlapi.DrawRectanglePro, None, Rectangle, Vector2, Float, Color)
_DrawRectangleGradientV = _wrap(rlapi.DrawRectangleGradientV, None, Int, Int, Int, Int, Color, Color)
_DrawRectangleGradientH = _wrap(rlapi.DrawRectangleGradientH, None, Int, Int, Int, Int, Color, Color)
_DrawRectangleGradientEx = _wrap(rlapi.DrawRectangleGradientEx, None, Rectangle, Color, Color, Color, Color)
_DrawRectangleLines = _wrap(rlapi.DrawRectangleLines, None, Int, Int, Int, Int, Color)
_DrawRectangleLinesEx = _wrap(rlapi.DrawRectangleLinesEx, None, Rectangle, Float, Color)
_DrawRectangleRounded = _wrap(rlapi.DrawRectangleRounded, None, Rectangle, Float, Int, Color)
_DrawRectangleRoundedLines = _wrap(rlapi.DrawRectangleRoundedLines, None, Rectangle, Float, Int, Float, Color)
_DrawTriangle = _wrap(rlapi.DrawTriangle, None, Vector2, Vector2, Vector2, Color)
_DrawTriangleLines = _wrap(rlapi.DrawTriangleLines, None, Vector2, Vector2, Vector2, Color)
_DrawTriangleFan = _wrap(rlapi.DrawTriangleFan, None, Vector2Ptr, Int, Color)
_DrawTriangleStrip = _wrap(rlapi.DrawTriangleStrip, None, Vector2Ptr, Int, Color)
_DrawPoly = _wrap(rlapi.DrawPoly, None, Vector2, Int, Float, Float, Color)
_DrawPolyLines = _wrap(rlapi.DrawPolyLines, None, Vector2, Int, Float, Float, Color)
_DrawPolyLinesEx = _wrap(rlapi.DrawPolyLinesEx, None, Vector2, Int, Float, Float, Float, Color)
_DrawSplineLinear = _wrap(rlapi.DrawSplineLinear, None, Vector2Ptr, Int, Float, Color)
_DrawSplineBasis = _wrap(rlapi.DrawSplineBasis, None, Vector2Ptr, Int, Float, Color)
_DrawSplineCatmullRom = _wrap(rlapi.DrawSplineCatmullRom, None, Vector2Ptr, Int, Float, Color)
_DrawSplineBezierQuadratic = _wrap(rlapi.DrawSplineBezierQuadratic, None, Vector2Ptr, Int, Float, Color)
_DrawSplineBezierCubic = _wrap(rlapi.DrawSplineBezierCubic, None, Vector2Ptr, Int, Float, Color)
_DrawSplineSegmentLinear = _wrap(rlapi.DrawSplineSegmentLinear, None, Vector2, Vector2, Float, Color)
_DrawSplineSegmentBasis = _wrap(rlapi.DrawSplineSegmentBasis, None, Vector2, Vector2, Vector2, Vector2, Float, Color)
_DrawSplineSegmentCatmullRom = _wrap(rlapi.DrawSplineSegmentCatmullRom, None, Vector2, Vector2, Vector2, Vector2, Float, Color)
_DrawSplineSegmentBezierQuadratic = _wrap(rlapi.DrawSplineSegmentBezierQuadratic, None, Vector2, Vector2, Vector2, Float, Color)
_DrawSplineSegmentBezierCubic = _wrap(rlapi.DrawSplineSegmentBezierCubic, None, Vector2, Vector2, Vector2, Vector2, Float, Color)
_GetSplinePointLinear = _wrap(rlapi.GetSplinePointLinear, Vector2, Vector2, Vector2, Float)
_GetSplinePointBasis = _wrap(rlapi.GetSplinePointBasis, Vector2, Vector2, Vector2, Vector2, Vector2, Float)
_GetSplinePointCatmullRom = _wrap(rlapi.GetSplinePointCatmullRom, Vector2, Vector2, Vector2, Vector2, Vector2, Float)
_GetSplinePointBezierQuad = _wrap(rlapi.GetSplinePointBezierQuad, Vector2, Vector2, Vector2, Vector2, Float)
_GetSplinePointBezierCubic = _wrap(rlapi.GetSplinePointBezierCubic, Vector2, Vector2, Vector2, Vector2, Vector2, Float)
_CheckCollisionRecs = _wrap(rlapi.CheckCollisionRecs, Bool, Rectangle, Rectangle)
_CheckCollisionCircles = _wrap(rlapi.CheckCollisionCircles, Bool, Vector2, Float, Vector2, Float)
_CheckCollisionCircleRec = _wrap(rlapi.CheckCollisionCircleRec, Bool, Vector2, Float, Rectangle)
_CheckCollisionPointRec = _wrap(rlapi.CheckCollisionPointRec, Bool, Vector2, Rectangle)
_CheckCollisionPointCircle = _wrap(rlapi.CheckCollisionPointCircle, Bool, Vector2, Vector2, Float)
_CheckCollisionPointTriangle = _wrap(rlapi.CheckCollisionPointTriangle, Bool, Vector2, Vector2, Vector2, Vector2)
_CheckCollisionPointPoly = _wrap(rlapi.CheckCollisionPointPoly, Bool, Vector2, Vector2Ptr, Int)
_CheckCollisionLines = _wrap(rlapi.CheckCollisionLines, Bool, Vector2, Vector2, Vector2, Vector2, Vector2Ptr)
_CheckCollisionPointLine = _wrap(rlapi.CheckCollisionPointLine, Bool, Vector2, Vector2, Vector2, Int)
_GetCollisionRec = _wrap(rlapi.GetCollisionRec, Rectangle, Rectangle, Rectangle)
_LoadImage = _wrap(rlapi.LoadImage, Image, CharPtr)
_LoadImageRaw = _wrap(rlapi.LoadImageRaw, Image, CharPtr, Int, Int, Int, Int)
_LoadImageSvg = _wrap(rlapi.LoadImageSvg, Image, CharPtr, Int, Int)
_LoadImageAnim = _wrap(rlapi.LoadImageAnim, Image, CharPtr, IntPtr)
_LoadImageFromMemory = _wrap(rlapi.LoadImageFromMemory, Image, CharPtr, UCharPtr, Int)
_LoadImageFromTexture = _wrap(rlapi.LoadImageFromTexture, Image, Texture2D)
_LoadImageFromScreen = _wrap(rlapi.LoadImageFromScreen, Image)
_IsImageReady = _wrap(rlapi.IsImageReady, Bool, Image)
_UnloadImage = _wrap(rlapi.UnloadImage, None, Image)
_ExportImage = _wrap(rlapi.ExportImage, Bool, Image, CharPtr)
_ExportImageToMemory = _wrap(rlapi.ExportImageToMemory, UCharPtr, Image, CharPtr, IntPtr)
_ExportImageAsCode = _wrap(rlapi.ExportImageAsCode, Bool, Image, CharPtr)
_GenImageColor = _wrap(rlapi.GenImageColor, Image, Int, Int, Color)
_GenImageGradientLinear = _wrap(rlapi.GenImageGradientLinear, Image, Int, Int, Int, Color, Color)
_GenImageGradientRadial = _wrap(rlapi.GenImageGradientRadial, Image, Int, Int, Float, Color, Color)
_GenImageGradientSquare = _wrap(rlapi.GenImageGradientSquare, Image, Int, Int, Float, Color, Color)
_GenImageChecked = _wrap(rlapi.GenImageChecked, Image, Int, Int, Int, Int, Color, Color)
_GenImageWhiteNoise = _wrap(rlapi.GenImageWhiteNoise, Image, Int, Int, Float)
_GenImagePerlinNoise = _wrap(rlapi.GenImagePerlinNoise, Image, Int, Int, Int, Int, Float)
_GenImageCellular = _wrap(rlapi.GenImageCellular, Image, Int, Int, Int)
_GenImageText = _wrap(rlapi.GenImageText, Image, Int, Int, CharPtr)
_ImageCopy = _wrap(rlapi.ImageCopy, Image, Image)
_ImageFromImage = _wrap(rlapi.ImageFromImage, Image, Image, Rectangle)
_ImageText = _wrap(rlapi.ImageText, Image, CharPtr, Int, Color)
_ImageTextEx = _wrap(rlapi.ImageTextEx, Image, Font, CharPtr, Float, Float, Color)
_ImageFormat = _wrap(rlapi.ImageFormat, None, ImagePtr, Int)
_ImageToPOT = _wrap(rlapi.ImageToPOT, None, ImagePtr, Color)
_ImageCrop = _wrap(rlapi.ImageCrop, None, ImagePtr, Rectangle)
_ImageAlphaCrop = _wrap(rlapi.ImageAlphaCrop, None, ImagePtr, Float)
_ImageAlphaClear = _wrap(rlapi.ImageAlphaClear, None, ImagePtr, Color, Float)
_ImageAlphaMask = _wrap(rlapi.ImageAlphaMask, None, ImagePtr, Image)
_ImageAlphaPremultiply = _wrap(rlapi.ImageAlphaPremultiply, None, ImagePtr)
_ImageBlurGaussian = _wrap(rlapi.ImageBlurGaussian, None, ImagePtr, Int)
_ImageResize = _wrap(rlapi.ImageResize, None, ImagePtr, Int, Int)
_ImageResizeNN = _wrap(rlapi.ImageResizeNN, None, ImagePtr, Int, Int)
_ImageResizeCanvas = _wrap(rlapi.ImageResizeCanvas, None, ImagePtr, Int, Int, Int, Int, Color)
_ImageMipmaps = _wrap(rlapi.ImageMipmaps, None, ImagePtr)
_ImageDither = _wrap(rlapi.ImageDither, None, ImagePtr, Int, Int, Int, Int)
_ImageFlipVertical = _wrap(rlapi.ImageFlipVertical, None, ImagePtr)
_ImageFlipHorizontal = _wrap(rlapi.ImageFlipHorizontal, None, ImagePtr)
_ImageRotate = _wrap(rlapi.ImageRotate, None, ImagePtr, Int)
_ImageRotateCW = _wrap(rlapi.ImageRotateCW, None, ImagePtr)
_ImageRotateCCW = _wrap(rlapi.ImageRotateCCW, None, ImagePtr)
_ImageColorTint = _wrap(rlapi.ImageColorTint, None, ImagePtr, Color)
_ImageColorInvert = _wrap(rlapi.ImageColorInvert, None, ImagePtr)
_ImageColorGrayscale = _wrap(rlapi.ImageColorGrayscale, None, ImagePtr)
_ImageColorContrast = _wrap(rlapi.ImageColorContrast, None, ImagePtr, Float)
_ImageColorBrightness = _wrap(rlapi.ImageColorBrightness, None, ImagePtr, Int)
_ImageColorReplace = _wrap(rlapi.ImageColorReplace, None, ImagePtr, Color, Color)
_LoadImageColors = _wrap(rlapi.LoadImageColors, ColorPtr, Image)
_LoadImagePalette = _wrap(rlapi.LoadImagePalette, ColorPtr, Image, Int, IntPtr)
_UnloadImageColors = _wrap(rlapi.UnloadImageColors, None, ColorPtr)
_UnloadImagePalette = _wrap(rlapi.UnloadImagePalette, None, ColorPtr)
_GetImageAlphaBorder = _wrap(rlapi.GetImageAlphaBorder, Rectangle, Image, Float)
_GetImageColor = _wrap(rlapi.GetImageColor, Color, Image, Int, Int)
_ImageClearBackground = _wrap(rlapi.ImageClearBackground, None, ImagePtr, Color)
_ImageDrawPixel = _wrap(rlapi.ImageDrawPixel, None, ImagePtr, Int, Int, Color)
_ImageDrawPixelV = _wrap(rlapi.ImageDrawPixelV, None, ImagePtr, Vector2, Color)
_ImageDrawLine = _wrap(rlapi.ImageDrawLine, None, ImagePtr, Int, Int, Int, Int, Color)
_ImageDrawLineV = _wrap(rlapi.ImageDrawLineV, None, ImagePtr, Vector2, Vector2, Color)
_ImageDrawCircle = _wrap(rlapi.ImageDrawCircle, None, ImagePtr, Int, Int, Int, Color)
_ImageDrawCircleV = _wrap(rlapi.ImageDrawCircleV, None, ImagePtr, Vector2, Int, Color)
_ImageDrawCircleLines = _wrap(rlapi.ImageDrawCircleLines, None, ImagePtr, Int, Int, Int, Color)
_ImageDrawCircleLinesV = _wrap(rlapi.ImageDrawCircleLinesV, None, ImagePtr, Vector2, Int, Color)
_ImageDrawRectangle = _wrap(rlapi.ImageDrawRectangle, None, ImagePtr, Int, Int, Int, Int, Color)
_ImageDrawRectangleV = _wrap(rlapi.ImageDrawRectangleV, None, ImagePtr, Vector2, Vector2, Color)
_ImageDrawRectangleRec = _wrap(rlapi.ImageDrawRectangleRec, None, ImagePtr, Rectangle, Color)
_ImageDrawRectangleLines = _wrap(rlapi.ImageDrawRectangleLines, None, ImagePtr, Rectangle, Int, Color)
_ImageDraw = _wrap(rlapi.ImageDraw, None, ImagePtr, Image, Rectangle, Rectangle, Color)
_ImageDrawText = _wrap(rlapi.ImageDrawText, None, ImagePtr, CharPtr, Int, Int, Int, Color)
_ImageDrawTextEx = _wrap(rlapi.ImageDrawTextEx, None, ImagePtr, Font, CharPtr, Vector2, Float, Float, Color)
_LoadTexture = _wrap(rlapi.LoadTexture, Texture2D, CharPtr)
_LoadTextureFromImage = _wrap(rlapi.LoadTextureFromImage, Texture2D, Image)
_LoadTextureCubemap = _wrap(rlapi.LoadTextureCubemap, TextureCubemap, Image, Int)
_LoadRenderTexture = _wrap(rlapi.LoadRenderTexture, RenderTexture2D, Int, Int)
_IsTextureReady = _wrap(rlapi.IsTextureReady, Bool, Texture2D)
_UnloadTexture = _wrap(rlapi.UnloadTexture, None, Texture2D)
_IsRenderTextureReady = _wrap(rlapi.IsRenderTextureReady, Bool, RenderTexture2D)
_UnloadRenderTexture = _wrap(rlapi.UnloadRenderTexture, None, RenderTexture2D)
_UpdateTexture = _wrap(rlapi.UpdateTexture, None, Texture2D, VoidPtr)
_UpdateTextureRec = _wrap(rlapi.UpdateTextureRec, None, Texture2D, Rectangle, VoidPtr)
_GenTextureMipmaps = _wrap(rlapi.GenTextureMipmaps, None, Texture2DPtr)
_SetTextureFilter = _wrap(rlapi.SetTextureFilter, None, Texture2D, Int)
_SetTextureWrap = _wrap(rlapi.SetTextureWrap, None, Texture2D, Int)
_DrawTexture = _wrap(rlapi.DrawTexture, None, Texture2D, Int, Int, Color)
_DrawTextureV = _wrap(rlapi.DrawTextureV, None, Texture2D, Vector2, Color)
_DrawTextureEx = _wrap(rlapi.DrawTextureEx, None, Texture2D, Vector2, Float, Float, Color)
_DrawTextureRec = _wrap(rlapi.DrawTextureRec, None, Texture2D, Rectangle, Vector2, Color)
_DrawTexturePro = _wrap(rlapi.DrawTexturePro, None, Texture2D, Rectangle, Rectangle, Vector2, Float, Color)
_DrawTextureNPatch = _wrap(rlapi.DrawTextureNPatch, None, Texture2D, NPatchInfo, Rectangle, Vector2, Float, Color)
_Fade = _wrap(rlapi.Fade, Color, Color, Float)
_ColorToInt = _wrap(rlapi.ColorToInt, Int, Color)
_ColorNormalize = _wrap(rlapi.ColorNormalize, Vector4, Color)
_ColorFromNormalized = _wrap(rlapi.ColorFromNormalized, Color, Vector4)
_ColorToHSV = _wrap(rlapi.ColorToHSV, Vector3, Color)
_ColorFromHSV = _wrap(rlapi.ColorFromHSV, Color, Float, Float, Float)
_ColorTint = _wrap(rlapi.ColorTint, Color, Color, Color)
_ColorBrightness = _wrap(rlapi.ColorBrightness, Color, Color, Float)
_ColorContrast = _wrap(rlapi.ColorContrast, Color, Color, Float)
_ColorAlpha = _wrap(rlapi.ColorAlpha, Color, Color, Float)
_ColorAlphaBlend = _wrap(rlapi.ColorAlphaBlend, Color, Color, Color, Color)
_GetColor = _wrap(rlapi.GetColor, Color, UInt)
_GetPixelColor = _wrap(rlapi.GetPixelColor, Color, VoidPtr, Int)
_SetPixelColor = _wrap(rlapi.SetPixelColor, None, VoidPtr, Color, Int)
_GetPixelDataSize = _wrap(rlapi.GetPixelDataSize, Int, Int, Int, Int)
_GetFontDefault = _wrap(rlapi.GetFontDefault, Font)
_LoadFont = _wrap(rlapi.LoadFont, Font, CharPtr)
_LoadFontEx = _wrap(rlapi.LoadFontEx, Font, CharPtr, Int, IntPtr, Int)
_LoadFontFromImage = _wrap(rlapi.LoadFontFromImage, Font, Image, Color, Int)
_LoadFontFromMemory = _wrap(rlapi.LoadFontFromMemory, Font, CharPtr, UCharPtr, Int, Int, IntPtr, Int)
_IsFontReady = _wrap(rlapi.IsFontReady, Bool, Font)
_LoadFontData = _wrap(rlapi.LoadFontData, GlyphInfoPtr, UCharPtr, Int, Int, IntPtr, Int, Int)
_GenImageFontAtlas = _wrap(rlapi.GenImageFontAtlas, Image, GlyphInfoPtr, RectanglePtrPtr, Int, Int, Int, Int)
_UnloadFontData = _wrap(rlapi.UnloadFontData, None, GlyphInfoPtr, Int)
_UnloadFont = _wrap(rlapi.UnloadFont, None, Font)
_ExportFontAsCode = _wrap(rlapi.ExportFontAsCode, Bool, Font, CharPtr)
_DrawFPS = _wrap(rlapi.DrawFPS, None, Int, Int)
_DrawText = _wrap(rlapi.DrawText, None, CharPtr, Int, Int, Int, Color)
_DrawTextEx = _wrap(rlapi.DrawTextEx, None, Font, CharPtr, Vector2, Float, Float, Color)
_DrawTextPro = _wrap(rlapi.DrawTextPro, None, Font, CharPtr, Vector2, Vector2, Float, Float, Float, Color)
_DrawTextCodepoint = _wrap(rlapi.DrawTextCodepoint, None, Font, Int, Vector2, Float, Color)
_DrawTextCodepoints = _wrap(rlapi.DrawTextCodepoints, None, Font, IntPtr, Int, Vector2, Float, Float, Color)
_SetTextLineSpacing = _wrap(rlapi.SetTextLineSpacing, None, Int)
_MeasureText = _wrap(rlapi.MeasureText, Int, CharPtr, Int)
_MeasureTextEx = _wrap(rlapi.MeasureTextEx, Vector2, Font, CharPtr, Float, Float)
_GetGlyphIndex = _wrap(rlapi.GetGlyphIndex, Int, Font, Int)
_GetGlyphInfo = _wrap(rlapi.GetGlyphInfo, GlyphInfo, Font, Int)
_GetGlyphAtlasRec = _wrap(rlapi.GetGlyphAtlasRec, Rectangle, Font, Int)
_LoadUTF8 = _wrap(rlapi.LoadUTF8, CharPtr, IntPtr, Int)
_UnloadUTF8 = _wrap(rlapi.UnloadUTF8, None, CharPtr)
_LoadCodepoints = _wrap(rlapi.LoadCodepoints, IntPtr, CharPtr, IntPtr)
_UnloadCodepoints = _wrap(rlapi.UnloadCodepoints, None, IntPtr)
_GetCodepointCount = _wrap(rlapi.GetCodepointCount, Int, CharPtr)
_GetCodepoint = _wrap(rlapi.GetCodepoint, Int, CharPtr, IntPtr)
_GetCodepointNext = _wrap(rlapi.GetCodepointNext, Int, CharPtr, IntPtr)
_GetCodepointPrevious = _wrap(rlapi.GetCodepointPrevious, Int, CharPtr, IntPtr)
_CodepointToUTF8 = _wrap(rlapi.CodepointToUTF8, CharPtr, Int, IntPtr)
_TextCopy = _wrap(rlapi.TextCopy, Int, CharPtr, CharPtr)
_TextIsEqual = _wrap(rlapi.TextIsEqual, Bool, CharPtr, CharPtr)
_TextLength = _wrap(rlapi.TextLength, UInt, CharPtr)
_TextFormat = _wrap(rlapi.TextFormat, CharPtr, CharPtr)
_TextSubtext = _wrap(rlapi.TextSubtext, CharPtr, CharPtr, Int, Int)
_TextReplace = _wrap(rlapi.TextReplace, CharPtr, CharPtr, CharPtr, CharPtr)
_TextInsert = _wrap(rlapi.TextInsert, CharPtr, CharPtr, CharPtr, Int)
_TextJoin = _wrap(rlapi.TextJoin, CharPtr, CharPtrPtr, Int, CharPtr)
_TextSplit = _wrap(rlapi.TextSplit, CharPtrPtr, CharPtr, Char, IntPtr)
_TextAppend = _wrap(rlapi.TextAppend, None, CharPtr, CharPtr, IntPtr)
_TextFindIndex = _wrap(rlapi.TextFindIndex, Int, CharPtr, CharPtr)
_TextToUpper = _wrap(rlapi.TextToUpper, CharPtr, CharPtr)
_TextToLower = _wrap(rlapi.TextToLower, CharPtr, CharPtr)
_TextToPascal = _wrap(rlapi.TextToPascal, CharPtr, CharPtr)
_TextToInteger = _wrap(rlapi.TextToInteger, Int, CharPtr)
_DrawLine3D = _wrap(rlapi.DrawLine3D, None, Vector3, Vector3, Color)
_DrawPoint3D = _wrap(rlapi.DrawPoint3D, None, Vector3, Color)
_DrawCircle3D = _wrap(rlapi.DrawCircle3D, None, Vector3, Float, Vector3, Float, Color)
_DrawTriangle3D = _wrap(rlapi.DrawTriangle3D, None, Vector3, Vector3, Vector3, Color)
_DrawTriangleStrip3D = _wrap(rlapi.DrawTriangleStrip3D, None, Vector3Ptr, Int, Color)
_DrawCube = _wrap(rlapi.DrawCube, None, Vector3, Float, Float, Float, Color)
_DrawCubeV = _wrap(rlapi.DrawCubeV, None, Vector3, Vector3, Color)
_DrawCubeWires = _wrap(rlapi.DrawCubeWires, None, Vector3, Float, Float, Float, Color)
_DrawCubeWiresV = _wrap(rlapi.DrawCubeWiresV, None, Vector3, Vector3, Color)
_DrawSphere = _wrap(rlapi.DrawSphere, None, Vector3, Float, Color)
_DrawSphereEx = _wrap(rlapi.DrawSphereEx, None, Vector3, Float, Int, Int, Color)
_DrawSphereWires = _wrap(rlapi.DrawSphereWires, None, Vector3, Float, Int, Int, Color)
_DrawCylinder = _wrap(rlapi.DrawCylinder, None, Vector3, Float, Float, Float, Int, Color)
_DrawCylinderEx = _wrap(rlapi.DrawCylinderEx, None, Vector3, Vector3, Float, Float, Int, Color)
_DrawCylinderWires = _wrap(rlapi.DrawCylinderWires, None, Vector3, Float, Float, Float, Int, Color)
_DrawCylinderWiresEx = _wrap(rlapi.DrawCylinderWiresEx, None, Vector3, Vector3, Float, Float, Int, Color)
_DrawCapsule = _wrap(rlapi.DrawCapsule, None, Vector3, Vector3, Float, Int, Int, Color)
_DrawCapsuleWires = _wrap(rlapi.DrawCapsuleWires, None, Vector3, Vector3, Float, Int, Int, Color)
_DrawPlane = _wrap(rlapi.DrawPlane, None, Vector3, Vector2, Color)
_DrawRay = _wrap(rlapi.DrawRay, None, Ray, Color)
_DrawGrid = _wrap(rlapi.DrawGrid, None, Int, Float)
_LoadModel = _wrap(rlapi.LoadModel, Model, CharPtr)
_LoadModelFromMesh = _wrap(rlapi.LoadModelFromMesh, Model, Mesh)
_IsModelReady = _wrap(rlapi.IsModelReady, Bool, Model)
_UnloadModel = _wrap(rlapi.UnloadModel, None, Model)
_GetModelBoundingBox = _wrap(rlapi.GetModelBoundingBox, BoundingBox, Model)
_DrawModel = _wrap(rlapi.DrawModel, None, Model, Vector3, Float, Color)
_DrawModelEx = _wrap(rlapi.DrawModelEx, None, Model, Vector3, Vector3, Float, Vector3, Color)
_DrawModelWires = _wrap(rlapi.DrawModelWires, None, Model, Vector3, Float, Color)
_DrawModelWiresEx = _wrap(rlapi.DrawModelWiresEx, None, Model, Vector3, Vector3, Float, Vector3, Color)
_DrawBoundingBox = _wrap(rlapi.DrawBoundingBox, None, BoundingBox, Color)
_DrawBillboard = _wrap(rlapi.DrawBillboard, None, Camera, Texture2D, Vector3, Float, Color)
_DrawBillboardRec = _wrap(rlapi.DrawBillboardRec, None, Camera, Texture2D, Rectangle, Vector3, Vector2, Color)
_DrawBillboardPro = _wrap(rlapi.DrawBillboardPro, None, Camera, Texture2D, Rectangle, Vector3, Vector3, Vector2, Vector2, Float, Color)
_UploadMesh = _wrap(rlapi.UploadMesh, None, MeshPtr, Bool)
_UpdateMeshBuffer = _wrap(rlapi.UpdateMeshBuffer, None, Mesh, Int, VoidPtr, Int, Int)
_UnloadMesh = _wrap(rlapi.UnloadMesh, None, Mesh)
_DrawMesh = _wrap(rlapi.DrawMesh, None, Mesh, Material, Matrix)
_DrawMeshInstanced = _wrap(rlapi.DrawMeshInstanced, None, Mesh, Material, MatrixPtr, Int)
_ExportMesh = _wrap(rlapi.ExportMesh, Bool, Mesh, CharPtr)
_GetMeshBoundingBox = _wrap(rlapi.GetMeshBoundingBox, BoundingBox, Mesh)
_GenMeshTangents = _wrap(rlapi.GenMeshTangents, None, MeshPtr)
_GenMeshPoly = _wrap(rlapi.GenMeshPoly, Mesh, Int, Float)
_GenMeshPlane = _wrap(rlapi.GenMeshPlane, Mesh, Float, Float, Int, Int)
_GenMeshCube = _wrap(rlapi.GenMeshCube, Mesh, Float, Float, Float)
_GenMeshSphere = _wrap(rlapi.GenMeshSphere, Mesh, Float, Int, Int)
_GenMeshHemiSphere = _wrap(rlapi.GenMeshHemiSphere, Mesh, Float, Int, Int)
_GenMeshCylinder = _wrap(rlapi.GenMeshCylinder, Mesh, Float, Float, Int)
_GenMeshCone = _wrap(rlapi.GenMeshCone, Mesh, Float, Float, Int)
_GenMeshTorus = _wrap(rlapi.GenMeshTorus, Mesh, Float, Float, Int, Int)
_GenMeshKnot = _wrap(rlapi.GenMeshKnot, Mesh, Float, Float, Int, Int)
_GenMeshHeightmap = _wrap(rlapi.GenMeshHeightmap, Mesh, Image, Vector3)
_GenMeshCubicmap = _wrap(rlapi.GenMeshCubicmap, Mesh, Image, Vector3)
_LoadMaterials = _wrap(rlapi.LoadMaterials, MaterialPtr, CharPtr, IntPtr)
_LoadMaterialDefault = _wrap(rlapi.LoadMaterialDefault, Material)
_IsMaterialReady = _wrap(rlapi.IsMaterialReady, Bool, Material)
_UnloadMaterial = _wrap(rlapi.UnloadMaterial, None, Material)
_SetMaterialTexture = _wrap(rlapi.SetMaterialTexture, None, MaterialPtr, Int, Texture2D)
_SetModelMeshMaterial = _wrap(rlapi.SetModelMeshMaterial, None, ModelPtr, Int, Int)
_LoadModelAnimations = _wrap(rlapi.LoadModelAnimations, ModelAnimationPtr, CharPtr, IntPtr)
_UpdateModelAnimation = _wrap(rlapi.UpdateModelAnimation, None, Model, ModelAnimation, Int)
_UnloadModelAnimation = _wrap(rlapi.UnloadModelAnimation, None, ModelAnimation)
_UnloadModelAnimations = _wrap(rlapi.UnloadModelAnimations, None, ModelAnimationPtr, Int)
_IsModelAnimationValid = _wrap(rlapi.IsModelAnimationValid, Bool, Model, ModelAnimation)
_CheckCollisionSpheres = _wrap(rlapi.CheckCollisionSpheres, Bool, Vector3, Float, Vector3, Float)
_CheckCollisionBoxes = _wrap(rlapi.CheckCollisionBoxes, Bool, BoundingBox, BoundingBox)
_CheckCollisionBoxSphere = _wrap(rlapi.CheckCollisionBoxSphere, Bool, BoundingBox, Vector3, Float)
_GetRayCollisionSphere = _wrap(rlapi.GetRayCollisionSphere, RayCollision, Ray, Vector3, Float)
_GetRayCollisionBox = _wrap(rlapi.GetRayCollisionBox, RayCollision, Ray, BoundingBox)
_GetRayCollisionMesh = _wrap(rlapi.GetRayCollisionMesh, RayCollision, Ray, Mesh, Matrix)
_GetRayCollisionTriangle = _wrap(rlapi.GetRayCollisionTriangle, RayCollision, Ray, Vector3, Vector3, Vector3)
_GetRayCollisionQuad = _wrap(rlapi.GetRayCollisionQuad, RayCollision, Ray, Vector3, Vector3, Vector3, Vector3)
_InitAudioDevice = _wrap(rlapi.InitAudioDevice, None)
_CloseAudioDevice = _wrap(rlapi.CloseAudioDevice, None)
_IsAudioDeviceReady = _wrap(rlapi.IsAudioDeviceReady, Bool)
_SetMasterVolume = _wrap(rlapi.SetMasterVolume, None, Float)
_GetMasterVolume = _wrap(rlapi.GetMasterVolume, Float)
_LoadWave = _wrap(rlapi.LoadWave, Wave, CharPtr)
_LoadWaveFromMemory = _wrap(rlapi.LoadWaveFromMemory, Wave, CharPtr, UCharPtr, Int)
_IsWaveReady = _wrap(rlapi.IsWaveReady, Bool, Wave)
_LoadSound = _wrap(rlapi.LoadSound, Sound, CharPtr)
_LoadSoundFromWave = _wrap(rlapi.LoadSoundFromWave, Sound, Wave)
_LoadSoundAlias = _wrap(rlapi.LoadSoundAlias, Sound, Sound)
_IsSoundReady = _wrap(rlapi.IsSoundReady, Bool, Sound)
_UpdateSound = _wrap(rlapi.UpdateSound, None, Sound, VoidPtr, Int)
_UnloadWave = _wrap(rlapi.UnloadWave, None, Wave)
_UnloadSound = _wrap(rlapi.UnloadSound, None, Sound)
_UnloadSoundAlias = _wrap(rlapi.UnloadSoundAlias, None, Sound)
_ExportWave = _wrap(rlapi.ExportWave, Bool, Wave, CharPtr)
_ExportWaveAsCode = _wrap(rlapi.ExportWaveAsCode, Bool, Wave, CharPtr)
_PlaySound = _wrap(rlapi.PlaySound, None, Sound)
_StopSound = _wrap(rlapi.StopSound, None, Sound)
_PauseSound = _wrap(rlapi.PauseSound, None, Sound)
_ResumeSound = _wrap(rlapi.ResumeSound, None, Sound)
_IsSoundPlaying = _wrap(rlapi.IsSoundPlaying, Bool, Sound)
_SetSoundVolume = _wrap(rlapi.SetSoundVolume, None, Sound, Float)
_SetSoundPitch = _wrap(rlapi.SetSoundPitch, None, Sound, Float)
_SetSoundPan = _wrap(rlapi.SetSoundPan, None, Sound, Float)
_WaveCopy = _wrap(rlapi.WaveCopy, Wave, Wave)
_WaveCrop = _wrap(rlapi.WaveCrop, None, WavePtr, Int, Int)
_WaveFormat = _wrap(rlapi.WaveFormat, None, WavePtr, Int, Int, Int)
_LoadWaveSamples = _wrap(rlapi.LoadWaveSamples, FloatPtr, Wave)
_UnloadWaveSamples = _wrap(rlapi.UnloadWaveSamples, None, FloatPtr)
_LoadMusicStream = _wrap(rlapi.LoadMusicStream, Music, CharPtr)
_LoadMusicStreamFromMemory = _wrap(rlapi.LoadMusicStreamFromMemory, Music, CharPtr, UCharPtr, Int)
_IsMusicReady = _wrap(rlapi.IsMusicReady, Bool, Music)
_UnloadMusicStream = _wrap(rlapi.UnloadMusicStream, None, Music)
_PlayMusicStream = _wrap(rlapi.PlayMusicStream, None, Music)
_IsMusicStreamPlaying = _wrap(rlapi.IsMusicStreamPlaying, Bool, Music)
_UpdateMusicStream = _wrap(rlapi.UpdateMusicStream, None, Music)
_StopMusicStream = _wrap(rlapi.StopMusicStream, None, Music)
_PauseMusicStream = _wrap(rlapi.PauseMusicStream, None, Music)
_ResumeMusicStream = _wrap(rlapi.ResumeMusicStream, None, Music)
_SeekMusicStream = _wrap(rlapi.SeekMusicStream, None, Music, Float)
_SetMusicVolume = _wrap(rlapi.SetMusicVolume, None, Music, Float)
_SetMusicPitch = _wrap(rlapi.SetMusicPitch, None, Music, Float)
_SetMusicPan = _wrap(rlapi.SetMusicPan, None, Music, Float)
_GetMusicTimeLength = _wrap(rlapi.GetMusicTimeLength, Float, Music)
_GetMusicTimePlayed = _wrap(rlapi.GetMusicTimePlayed, Float, Music)
_LoadAudioStream = _wrap(rlapi.LoadAudioStream, AudioStream, UInt, UInt, UInt)
_IsAudioStreamReady = _wrap(rlapi.IsAudioStreamReady, Bool, AudioStream)
_UnloadAudioStream = _wrap(rlapi.UnloadAudioStream, None, AudioStream)
_UpdateAudioStream = _wrap(rlapi.UpdateAudioStream, None, AudioStream, VoidPtr, Int)
_IsAudioStreamProcessed = _wrap(rlapi.IsAudioStreamProcessed, Bool, AudioStream)
_PlayAudioStream = _wrap(rlapi.PlayAudioStream, None, AudioStream)
_PauseAudioStream = _wrap(rlapi.PauseAudioStream, None, AudioStream)
_ResumeAudioStream = _wrap(rlapi.ResumeAudioStream, None, AudioStream)
_IsAudioStreamPlaying = _wrap(rlapi.IsAudioStreamPlaying, Bool, AudioStream)
_StopAudioStream = _wrap(rlapi.StopAudioStream, None, AudioStream)
_SetAudioStreamVolume = _wrap(rlapi.SetAudioStreamVolume, None, AudioStream, Float)
_SetAudioStreamPitch = _wrap(rlapi.SetAudioStreamPitch, None, AudioStream, Float)
_SetAudioStreamPan = _wrap(rlapi.SetAudioStreamPan, None, AudioStream, Float)
_SetAudioStreamBufferSizeDefault = _wrap(rlapi.SetAudioStreamBufferSizeDefault, None, Int)
_SetAudioStreamCallback = _wrap(rlapi.SetAudioStreamCallback, None, AudioStream, AudioCallback)
_AttachAudioStreamProcessor = _wrap(rlapi.AttachAudioStreamProcessor, None, AudioStream, AudioCallback)
_DetachAudioStreamProcessor = _wrap(rlapi.DetachAudioStreamProcessor, None, AudioStream, AudioCallback)
_AttachAudioMixedProcessor = _wrap(rlapi.AttachAudioMixedProcessor, None, AudioCallback)
_DetachAudioMixedProcessor = _wrap(rlapi.DetachAudioMixedProcessor, None, AudioCallback)


# rlapi::raymath
# ------------------------------------------------------------------------------

float3._fields_ = [
    ('v', c_float * 3),
]


float16._fields_ = [
    ('v', c_float * 16),
]


_Clamp = _wrap(rlapi.Clamp, Float, Float, Float, Float)
_Lerp = _wrap(rlapi.Lerp, Float, Float, Float, Float)
_Normalize = _wrap(rlapi.Normalize, Float, Float, Float, Float)
_Remap = _wrap(rlapi.Remap, Float, Float, Float, Float, Float, Float)
_Wrap = _wrap(rlapi.Wrap, Float, Float, Float, Float)
_FloatEquals = _wrap(rlapi.FloatEquals, Int, Float, Float)
_Vector2Zero = _wrap(rlapi.Vector2Zero, Vector2)
_Vector2One = _wrap(rlapi.Vector2One, Vector2)
_Vector2Add = _wrap(rlapi.Vector2Add, Vector2, Vector2, Vector2)
_Vector2AddValue = _wrap(rlapi.Vector2AddValue, Vector2, Vector2, Float)
_Vector2Subtract = _wrap(rlapi.Vector2Subtract, Vector2, Vector2, Vector2)
_Vector2SubtractValue = _wrap(rlapi.Vector2SubtractValue, Vector2, Vector2, Float)
_Vector2Length = _wrap(rlapi.Vector2Length, Float, Vector2)
_Vector2LengthSqr = _wrap(rlapi.Vector2LengthSqr, Float, Vector2)
_Vector2DotProduct = _wrap(rlapi.Vector2DotProduct, Float, Vector2, Vector2)
_Vector2Distance = _wrap(rlapi.Vector2Distance, Float, Vector2, Vector2)
_Vector2DistanceSqr = _wrap(rlapi.Vector2DistanceSqr, Float, Vector2, Vector2)
_Vector2Angle = _wrap(rlapi.Vector2Angle, Float, Vector2, Vector2)
_Vector2LineAngle = _wrap(rlapi.Vector2LineAngle, Float, Vector2, Vector2)
_Vector2Scale = _wrap(rlapi.Vector2Scale, Vector2, Vector2, Float)
_Vector2Multiply = _wrap(rlapi.Vector2Multiply, Vector2, Vector2, Vector2)
_Vector2Negate = _wrap(rlapi.Vector2Negate, Vector2, Vector2)
_Vector2Divide = _wrap(rlapi.Vector2Divide, Vector2, Vector2, Vector2)
_Vector2Normalize = _wrap(rlapi.Vector2Normalize, Vector2, Vector2)
_Vector2Transform = _wrap(rlapi.Vector2Transform, Vector2, Vector2, Matrix)
_Vector2Lerp = _wrap(rlapi.Vector2Lerp, Vector2, Vector2, Vector2, Float)
_Vector2Reflect = _wrap(rlapi.Vector2Reflect, Vector2, Vector2, Vector2)
_Vector2Rotate = _wrap(rlapi.Vector2Rotate, Vector2, Vector2, Float)
_Vector2MoveTowards = _wrap(rlapi.Vector2MoveTowards, Vector2, Vector2, Vector2, Float)
_Vector2Invert = _wrap(rlapi.Vector2Invert, Vector2, Vector2)
_Vector2Clamp = _wrap(rlapi.Vector2Clamp, Vector2, Vector2, Vector2, Vector2)
_Vector2ClampValue = _wrap(rlapi.Vector2ClampValue, Vector2, Vector2, Float, Float)
_Vector2Equals = _wrap(rlapi.Vector2Equals, Int, Vector2, Vector2)
_Vector3Zero = _wrap(rlapi.Vector3Zero, Vector3)
_Vector3One = _wrap(rlapi.Vector3One, Vector3)
_Vector3Add = _wrap(rlapi.Vector3Add, Vector3, Vector3, Vector3)
_Vector3AddValue = _wrap(rlapi.Vector3AddValue, Vector3, Vector3, Float)
_Vector3Subtract = _wrap(rlapi.Vector3Subtract, Vector3, Vector3, Vector3)
_Vector3SubtractValue = _wrap(rlapi.Vector3SubtractValue, Vector3, Vector3, Float)
_Vector3Scale = _wrap(rlapi.Vector3Scale, Vector3, Vector3, Float)
_Vector3Multiply = _wrap(rlapi.Vector3Multiply, Vector3, Vector3, Vector3)
_Vector3CrossProduct = _wrap(rlapi.Vector3CrossProduct, Vector3, Vector3, Vector3)
_Vector3Perpendicular = _wrap(rlapi.Vector3Perpendicular, Vector3, Vector3)
_Vector3Length = _wrap(rlapi.Vector3Length, Float, Vector3)
_Vector3LengthSqr = _wrap(rlapi.Vector3LengthSqr, Float, Vector3)
_Vector3DotProduct = _wrap(rlapi.Vector3DotProduct, Float, Vector3, Vector3)
_Vector3Distance = _wrap(rlapi.Vector3Distance, Float, Vector3, Vector3)
_Vector3DistanceSqr = _wrap(rlapi.Vector3DistanceSqr, Float, Vector3, Vector3)
_Vector3Angle = _wrap(rlapi.Vector3Angle, Float, Vector3, Vector3)
_Vector3Negate = _wrap(rlapi.Vector3Negate, Vector3, Vector3)
_Vector3Divide = _wrap(rlapi.Vector3Divide, Vector3, Vector3, Vector3)
_Vector3Normalize = _wrap(rlapi.Vector3Normalize, Vector3, Vector3)
_Vector3Project = _wrap(rlapi.Vector3Project, Vector3, Vector3, Vector3)
_Vector3Reject = _wrap(rlapi.Vector3Reject, Vector3, Vector3, Vector3)
_Vector3OrthoNormalize = _wrap(rlapi.Vector3OrthoNormalize, None, Vector3Ptr, Vector3Ptr)
_Vector3Transform = _wrap(rlapi.Vector3Transform, Vector3, Vector3, Matrix)
_Vector3RotateByQuaternion = _wrap(rlapi.Vector3RotateByQuaternion, Vector3, Vector3, Quaternion)
_Vector3RotateByAxisAngle = _wrap(rlapi.Vector3RotateByAxisAngle, Vector3, Vector3, Vector3, Float)
_Vector3Lerp = _wrap(rlapi.Vector3Lerp, Vector3, Vector3, Vector3, Float)
_Vector3Reflect = _wrap(rlapi.Vector3Reflect, Vector3, Vector3, Vector3)
_Vector3Min = _wrap(rlapi.Vector3Min, Vector3, Vector3, Vector3)
_Vector3Max = _wrap(rlapi.Vector3Max, Vector3, Vector3, Vector3)
_Vector3Barycenter = _wrap(rlapi.Vector3Barycenter, Vector3, Vector3, Vector3, Vector3, Vector3)
_Vector3Unproject = _wrap(rlapi.Vector3Unproject, Vector3, Vector3, Matrix, Matrix)
_Vector3ToFloatV = _wrap(rlapi.Vector3ToFloatV, float3, Vector3)
_Vector3Invert = _wrap(rlapi.Vector3Invert, Vector3, Vector3)
_Vector3Clamp = _wrap(rlapi.Vector3Clamp, Vector3, Vector3, Vector3, Vector3)
_Vector3ClampValue = _wrap(rlapi.Vector3ClampValue, Vector3, Vector3, Float, Float)
_Vector3Equals = _wrap(rlapi.Vector3Equals, Int, Vector3, Vector3)
_Vector3Refract = _wrap(rlapi.Vector3Refract, Vector3, Vector3, Vector3, Float)
_MatrixDeterminant = _wrap(rlapi.MatrixDeterminant, Float, Matrix)
_MatrixTrace = _wrap(rlapi.MatrixTrace, Float, Matrix)
_MatrixTranspose = _wrap(rlapi.MatrixTranspose, Matrix, Matrix)
_MatrixInvert = _wrap(rlapi.MatrixInvert, Matrix, Matrix)
_MatrixIdentity = _wrap(rlapi.MatrixIdentity, Matrix)
_MatrixAdd = _wrap(rlapi.MatrixAdd, Matrix, Matrix, Matrix)
_MatrixSubtract = _wrap(rlapi.MatrixSubtract, Matrix, Matrix, Matrix)
_MatrixMultiply = _wrap(rlapi.MatrixMultiply, Matrix, Matrix, Matrix)
_MatrixTranslate = _wrap(rlapi.MatrixTranslate, Matrix, Float, Float, Float)
_MatrixRotate = _wrap(rlapi.MatrixRotate, Matrix, Vector3, Float)
_MatrixRotateX = _wrap(rlapi.MatrixRotateX, Matrix, Float)
_MatrixRotateY = _wrap(rlapi.MatrixRotateY, Matrix, Float)
_MatrixRotateZ = _wrap(rlapi.MatrixRotateZ, Matrix, Float)
_MatrixRotateXYZ = _wrap(rlapi.MatrixRotateXYZ, Matrix, Vector3)
_MatrixRotateZYX = _wrap(rlapi.MatrixRotateZYX, Matrix, Vector3)
_MatrixScale = _wrap(rlapi.MatrixScale, Matrix, Float, Float, Float)
_MatrixFrustum = _wrap(rlapi.MatrixFrustum, Matrix, Double, Double, Double, Double, Double, Double)
_MatrixPerspective = _wrap(rlapi.MatrixPerspective, Matrix, Double, Double, Double, Double)
_MatrixOrtho = _wrap(rlapi.MatrixOrtho, Matrix, Double, Double, Double, Double, Double, Double)
_MatrixLookAt = _wrap(rlapi.MatrixLookAt, Matrix, Vector3, Vector3, Vector3)
_MatrixToFloatV = _wrap(rlapi.MatrixToFloatV, float16, Matrix)
_QuaternionAdd = _wrap(rlapi.QuaternionAdd, Quaternion, Quaternion, Quaternion)
_QuaternionAddValue = _wrap(rlapi.QuaternionAddValue, Quaternion, Quaternion, Float)
_QuaternionSubtract = _wrap(rlapi.QuaternionSubtract, Quaternion, Quaternion, Quaternion)
_QuaternionSubtractValue = _wrap(rlapi.QuaternionSubtractValue, Quaternion, Quaternion, Float)
_QuaternionIdentity = _wrap(rlapi.QuaternionIdentity, Quaternion)
_QuaternionLength = _wrap(rlapi.QuaternionLength, Float, Quaternion)
_QuaternionNormalize = _wrap(rlapi.QuaternionNormalize, Quaternion, Quaternion)
_QuaternionInvert = _wrap(rlapi.QuaternionInvert, Quaternion, Quaternion)
_QuaternionMultiply = _wrap(rlapi.QuaternionMultiply, Quaternion, Quaternion, Quaternion)
_QuaternionScale = _wrap(rlapi.QuaternionScale, Quaternion, Quaternion, Float)
_QuaternionDivide = _wrap(rlapi.QuaternionDivide, Quaternion, Quaternion, Quaternion)
_QuaternionLerp = _wrap(rlapi.QuaternionLerp, Quaternion, Quaternion, Quaternion, Float)
_QuaternionNlerp = _wrap(rlapi.QuaternionNlerp, Quaternion, Quaternion, Quaternion, Float)
_QuaternionSlerp = _wrap(rlapi.QuaternionSlerp, Quaternion, Quaternion, Quaternion, Float)
_QuaternionFromVector3ToVector3 = _wrap(rlapi.QuaternionFromVector3ToVector3, Quaternion, Vector3, Vector3)
_QuaternionFromMatrix = _wrap(rlapi.QuaternionFromMatrix, Quaternion, Matrix)
_QuaternionToMatrix = _wrap(rlapi.QuaternionToMatrix, Matrix, Quaternion)
_QuaternionFromAxisAngle = _wrap(rlapi.QuaternionFromAxisAngle, Quaternion, Vector3, Float)
_QuaternionToAxisAngle = _wrap(rlapi.QuaternionToAxisAngle, None, Quaternion, Vector3Ptr, FloatPtr)
_QuaternionFromEuler = _wrap(rlapi.QuaternionFromEuler, Quaternion, Float, Float, Float)
_QuaternionToEuler = _wrap(rlapi.QuaternionToEuler, Vector3, Quaternion)
_QuaternionTransform = _wrap(rlapi.QuaternionTransform, Quaternion, Quaternion, Matrix)
_QuaternionEquals = _wrap(rlapi.QuaternionEquals, Int, Quaternion, Quaternion)


# rlapi::rlgl
# ------------------------------------------------------------------------------

rlVertexBuffer._fields_ = [
    ('element_count', c_int),
    ('vertices', POINTER(c_float)),
    ('texcoords', POINTER(c_float)),
    ('colors', c_ubyte),
    ('indices', POINTER(c_uint)),
    ('indices', POINTER(c_ushort)),
    ('vao_id', c_uint),
    ('vbo_id', c_uint * 4),
]


rlDrawCall._fields_ = [
    ('mode', c_int),
    ('vertex_count', c_int),
    ('vertex_alignment', c_int),
    ('texture_id', c_uint),
]


rlRenderBatch._fields_ = [
    ('buffer_count', c_int),
    ('current_buffer', c_int),
    ('vertex_buffer', rlVertexBufferPtr),
    ('draws', rlDrawCallPtr),
    ('draw_counter', c_int),
    ('current_depth', c_float),
]


_rlMatrixMode = _wrap(rlapi.rlMatrixMode, None, Int)
_rlPushMatrix = _wrap(rlapi.rlPushMatrix, None)
_rlPopMatrix = _wrap(rlapi.rlPopMatrix, None)
_rlLoadIdentity = _wrap(rlapi.rlLoadIdentity, None)
_rlTranslatef = _wrap(rlapi.rlTranslatef, None, Float, Float, Float)
_rlRotatef = _wrap(rlapi.rlRotatef, None, Float, Float, Float, Float)
_rlScalef = _wrap(rlapi.rlScalef, None, Float, Float, Float)
_rlMultMatrixf = _wrap(rlapi.rlMultMatrixf, None, FloatPtr)
_rlFrustum = _wrap(rlapi.rlFrustum, None, Double, Double, Double, Double, Double, Double)
_rlOrtho = _wrap(rlapi.rlOrtho, None, Double, Double, Double, Double, Double, Double)
_rlViewport = _wrap(rlapi.rlViewport, None, Int, Int, Int, Int)
_rlBegin = _wrap(rlapi.rlBegin, None, Int)
_rlEnd = _wrap(rlapi.rlEnd, None)
_rlVertex2i = _wrap(rlapi.rlVertex2i, None, Int, Int)
_rlVertex2f = _wrap(rlapi.rlVertex2f, None, Float, Float)
_rlVertex3f = _wrap(rlapi.rlVertex3f, None, Float, Float, Float)
_rlTexCoord2f = _wrap(rlapi.rlTexCoord2f, None, Float, Float)
_rlNormal3f = _wrap(rlapi.rlNormal3f, None, Float, Float, Float)
_rlColor4ub = _wrap(rlapi.rlColor4ub, None, UChar, UChar, UChar, UChar)
_rlColor3f = _wrap(rlapi.rlColor3f, None, Float, Float, Float)
_rlColor4f = _wrap(rlapi.rlColor4f, None, Float, Float, Float, Float)
_rlEnableVertexArray = _wrap(rlapi.rlEnableVertexArray, Bool, UInt)
_rlDisableVertexArray = _wrap(rlapi.rlDisableVertexArray, None)
_rlEnableVertexBuffer = _wrap(rlapi.rlEnableVertexBuffer, None, UInt)
_rlDisableVertexBuffer = _wrap(rlapi.rlDisableVertexBuffer, None)
_rlEnableVertexBufferElement = _wrap(rlapi.rlEnableVertexBufferElement, None, UInt)
_rlDisableVertexBufferElement = _wrap(rlapi.rlDisableVertexBufferElement, None)
_rlEnableVertexAttribute = _wrap(rlapi.rlEnableVertexAttribute, None, UInt)
_rlDisableVertexAttribute = _wrap(rlapi.rlDisableVertexAttribute, None, UInt)
_rlActiveTextureSlot = _wrap(rlapi.rlActiveTextureSlot, None, Int)
_rlEnableTexture = _wrap(rlapi.rlEnableTexture, None, UInt)
_rlDisableTexture = _wrap(rlapi.rlDisableTexture, None)
_rlEnableTextureCubemap = _wrap(rlapi.rlEnableTextureCubemap, None, UInt)
_rlDisableTextureCubemap = _wrap(rlapi.rlDisableTextureCubemap, None)
_rlTextureParameters = _wrap(rlapi.rlTextureParameters, None, UInt, Int, Int)
_rlCubemapParameters = _wrap(rlapi.rlCubemapParameters, None, UInt, Int, Int)
_rlEnableShader = _wrap(rlapi.rlEnableShader, None, UInt)
_rlDisableShader = _wrap(rlapi.rlDisableShader, None)
_rlEnableFramebuffer = _wrap(rlapi.rlEnableFramebuffer, None, UInt)
_rlDisableFramebuffer = _wrap(rlapi.rlDisableFramebuffer, None)
_rlActiveDrawBuffers = _wrap(rlapi.rlActiveDrawBuffers, None, Int)
_rlBlitFramebuffer = _wrap(rlapi.rlBlitFramebuffer, None, Int, Int, Int, Int, Int, Int, Int, Int, Int)
_rlEnableColorBlend = _wrap(rlapi.rlEnableColorBlend, None)
_rlDisableColorBlend = _wrap(rlapi.rlDisableColorBlend, None)
_rlEnableDepthTest = _wrap(rlapi.rlEnableDepthTest, None)
_rlDisableDepthTest = _wrap(rlapi.rlDisableDepthTest, None)
_rlEnableDepthMask = _wrap(rlapi.rlEnableDepthMask, None)
_rlDisableDepthMask = _wrap(rlapi.rlDisableDepthMask, None)
_rlEnableBackfaceCulling = _wrap(rlapi.rlEnableBackfaceCulling, None)
_rlDisableBackfaceCulling = _wrap(rlapi.rlDisableBackfaceCulling, None)
_rlSetCullFace = _wrap(rlapi.rlSetCullFace, None, Int)
_rlEnableScissorTest = _wrap(rlapi.rlEnableScissorTest, None)
_rlDisableScissorTest = _wrap(rlapi.rlDisableScissorTest, None)
_rlScissor = _wrap(rlapi.rlScissor, None, Int, Int, Int, Int)
_rlEnableWireMode = _wrap(rlapi.rlEnableWireMode, None)
_rlEnablePointMode = _wrap(rlapi.rlEnablePointMode, None)
_rlDisableWireMode = _wrap(rlapi.rlDisableWireMode, None)
_rlSetLineWidth = _wrap(rlapi.rlSetLineWidth, None, Float)
_rlGetLineWidth = _wrap(rlapi.rlGetLineWidth, Float)
_rlEnableSmoothLines = _wrap(rlapi.rlEnableSmoothLines, None)
_rlDisableSmoothLines = _wrap(rlapi.rlDisableSmoothLines, None)
_rlEnableStereoRender = _wrap(rlapi.rlEnableStereoRender, None)
_rlDisableStereoRender = _wrap(rlapi.rlDisableStereoRender, None)
_rlIsStereoRenderEnabled = _wrap(rlapi.rlIsStereoRenderEnabled, Bool)
_rlClearColor = _wrap(rlapi.rlClearColor, None, UChar, UChar, UChar, UChar)
_rlClearScreenBuffers = _wrap(rlapi.rlClearScreenBuffers, None)
_rlCheckErrors = _wrap(rlapi.rlCheckErrors, None)
_rlSetBlendMode = _wrap(rlapi.rlSetBlendMode, None, Int)
_rlSetBlendFactors = _wrap(rlapi.rlSetBlendFactors, None, Int, Int, Int)
_rlSetBlendFactorsSeparate = _wrap(rlapi.rlSetBlendFactorsSeparate, None, Int, Int, Int, Int, Int, Int)
_rlglInit = _wrap(rlapi.rlglInit, None, Int, Int)
_rlglClose = _wrap(rlapi.rlglClose, None)
_rlLoadExtensions = _wrap(rlapi.rlLoadExtensions, None, VoidPtr)
_rlGetVersion = _wrap(rlapi.rlGetVersion, Int)
_rlSetFramebufferWidth = _wrap(rlapi.rlSetFramebufferWidth, None, Int)
_rlGetFramebufferWidth = _wrap(rlapi.rlGetFramebufferWidth, Int)
_rlSetFramebufferHeight = _wrap(rlapi.rlSetFramebufferHeight, None, Int)
_rlGetFramebufferHeight = _wrap(rlapi.rlGetFramebufferHeight, Int)
_rlGetTextureIdDefault = _wrap(rlapi.rlGetTextureIdDefault, UInt)
_rlGetShaderIdDefault = _wrap(rlapi.rlGetShaderIdDefault, UInt)
_rlGetShaderLocsDefault = _wrap(rlapi.rlGetShaderLocsDefault, IntPtr)
_rlLoadRenderBatch = _wrap(rlapi.rlLoadRenderBatch, rlRenderBatch, Int, Int)
_rlUnloadRenderBatch = _wrap(rlapi.rlUnloadRenderBatch, None, rlRenderBatch)
_rlDrawRenderBatch = _wrap(rlapi.rlDrawRenderBatch, None, rlRenderBatchPtr)
_rlSetRenderBatchActive = _wrap(rlapi.rlSetRenderBatchActive, None, rlRenderBatchPtr)
_rlDrawRenderBatchActive = _wrap(rlapi.rlDrawRenderBatchActive, None)
_rlCheckRenderBatchLimit = _wrap(rlapi.rlCheckRenderBatchLimit, Bool, Int)
_rlSetTexture = _wrap(rlapi.rlSetTexture, None, UInt)
_rlLoadVertexArray = _wrap(rlapi.rlLoadVertexArray, UInt)
_rlLoadVertexBuffer = _wrap(rlapi.rlLoadVertexBuffer, UInt, VoidPtr, Int, Bool)
_rlLoadVertexBufferElement = _wrap(rlapi.rlLoadVertexBufferElement, UInt, VoidPtr, Int, Bool)
_rlUpdateVertexBuffer = _wrap(rlapi.rlUpdateVertexBuffer, None, UInt, VoidPtr, Int, Int)
_rlUpdateVertexBufferElements = _wrap(rlapi.rlUpdateVertexBufferElements, None, UInt, VoidPtr, Int, Int)
_rlUnloadVertexArray = _wrap(rlapi.rlUnloadVertexArray, None, UInt)
_rlUnloadVertexBuffer = _wrap(rlapi.rlUnloadVertexBuffer, None, UInt)
_rlSetVertexAttribute = _wrap(rlapi.rlSetVertexAttribute, None, UInt, Int, Int, Bool, Int, VoidPtr)
_rlSetVertexAttributeDivisor = _wrap(rlapi.rlSetVertexAttributeDivisor, None, UInt, Int)
_rlSetVertexAttributeDefault = _wrap(rlapi.rlSetVertexAttributeDefault, None, Int, VoidPtr, Int, Int)
_rlDrawVertexArray = _wrap(rlapi.rlDrawVertexArray, None, Int, Int)
_rlDrawVertexArrayElements = _wrap(rlapi.rlDrawVertexArrayElements, None, Int, Int, VoidPtr)
_rlDrawVertexArrayInstanced = _wrap(rlapi.rlDrawVertexArrayInstanced, None, Int, Int, Int)
_rlDrawVertexArrayElementsInstanced = _wrap(rlapi.rlDrawVertexArrayElementsInstanced, None, Int, Int, VoidPtr, Int)
_rlLoadTexture = _wrap(rlapi.rlLoadTexture, UInt, VoidPtr, Int, Int, Int, Int)
_rlLoadTextureDepth = _wrap(rlapi.rlLoadTextureDepth, UInt, Int, Int, Bool)
_rlLoadTextureCubemap = _wrap(rlapi.rlLoadTextureCubemap, UInt, VoidPtr, Int, Int)
_rlUpdateTexture = _wrap(rlapi.rlUpdateTexture, None, UInt, Int, Int, Int, Int, Int, VoidPtr)
_rlGetGlTextureFormats = _wrap(rlapi.rlGetGlTextureFormats, None, Int, UIntPtr, UIntPtr, UIntPtr)
_rlGetPixelFormatName = _wrap(rlapi.rlGetPixelFormatName, CharPtr, UInt)
_rlUnloadTexture = _wrap(rlapi.rlUnloadTexture, None, UInt)
_rlGenTextureMipmaps = _wrap(rlapi.rlGenTextureMipmaps, None, UInt, Int, Int, Int, IntPtr)
_rlReadTexturePixels = _wrap(rlapi.rlReadTexturePixels, VoidPtr, UInt, Int, Int, Int)
_rlReadScreenPixels = _wrap(rlapi.rlReadScreenPixels, UCharPtr, Int, Int)
_rlLoadFramebuffer = _wrap(rlapi.rlLoadFramebuffer, UInt, Int, Int)
_rlFramebufferAttach = _wrap(rlapi.rlFramebufferAttach, None, UInt, UInt, Int, Int, Int)
_rlFramebufferComplete = _wrap(rlapi.rlFramebufferComplete, Bool, UInt)
_rlUnloadFramebuffer = _wrap(rlapi.rlUnloadFramebuffer, None, UInt)
_rlLoadShaderCode = _wrap(rlapi.rlLoadShaderCode, UInt, CharPtr, CharPtr)
_rlCompileShader = _wrap(rlapi.rlCompileShader, UInt, CharPtr, Int)
_rlLoadShaderProgram = _wrap(rlapi.rlLoadShaderProgram, UInt, UInt, UInt)
_rlUnloadShaderProgram = _wrap(rlapi.rlUnloadShaderProgram, None, UInt)
_rlGetLocationUniform = _wrap(rlapi.rlGetLocationUniform, Int, UInt, CharPtr)
_rlGetLocationAttrib = _wrap(rlapi.rlGetLocationAttrib, Int, UInt, CharPtr)
_rlSetUniform = _wrap(rlapi.rlSetUniform, None, Int, VoidPtr, Int, Int)
_rlSetUniformMatrix = _wrap(rlapi.rlSetUniformMatrix, None, Int, Matrix)
_rlSetUniformSampler = _wrap(rlapi.rlSetUniformSampler, None, Int, UInt)
_rlSetShader = _wrap(rlapi.rlSetShader, None, UInt, IntPtr)
_rlLoadComputeShaderProgram = _wrap(rlapi.rlLoadComputeShaderProgram, UInt, UInt)
_rlComputeShaderDispatch = _wrap(rlapi.rlComputeShaderDispatch, None, UInt, UInt, UInt)
_rlLoadShaderBuffer = _wrap(rlapi.rlLoadShaderBuffer, UInt, UInt, VoidPtr, Int)
_rlUnloadShaderBuffer = _wrap(rlapi.rlUnloadShaderBuffer, None, UInt)
_rlUpdateShaderBuffer = _wrap(rlapi.rlUpdateShaderBuffer, None, UInt, VoidPtr, UInt, UInt)
_rlBindShaderBuffer = _wrap(rlapi.rlBindShaderBuffer, None, UInt, UInt)
_rlReadShaderBuffer = _wrap(rlapi.rlReadShaderBuffer, None, UInt, VoidPtr, UInt, UInt)
_rlCopyShaderBuffer = _wrap(rlapi.rlCopyShaderBuffer, None, UInt, UInt, UInt, UInt, UInt)
_rlGetShaderBufferSize = _wrap(rlapi.rlGetShaderBufferSize, UInt, UInt)
_rlBindImageTexture = _wrap(rlapi.rlBindImageTexture, None, UInt, UInt, Int, Bool)
_rlGetMatrixModelview = _wrap(rlapi.rlGetMatrixModelview, Matrix)
_rlGetMatrixProjection = _wrap(rlapi.rlGetMatrixProjection, Matrix)
_rlGetMatrixTransform = _wrap(rlapi.rlGetMatrixTransform, Matrix)
_rlGetMatrixProjectionStereo = _wrap(rlapi.rlGetMatrixProjectionStereo, Matrix, Int)
_rlGetMatrixViewOffsetStereo = _wrap(rlapi.rlGetMatrixViewOffsetStereo, Matrix, Int)
_rlSetMatrixProjection = _wrap(rlapi.rlSetMatrixProjection, None, Matrix)
_rlSetMatrixModelview = _wrap(rlapi.rlSetMatrixModelview, None, Matrix)
_rlSetMatrixProjectionStereo = _wrap(rlapi.rlSetMatrixProjectionStereo, None, Matrix, Matrix)
_rlSetMatrixViewOffsetStereo = _wrap(rlapi.rlSetMatrixViewOffsetStereo, None, Matrix, Matrix)
_rlLoadDrawCube = _wrap(rlapi.rlLoadDrawCube, None)
_rlLoadDrawQuad = _wrap(rlapi.rlLoadDrawQuad, None)

# endregion (internals)

# region DEFINES

# rlapi::raylib
# ------------------------------------------------------------------------------
RAYLIB_VERSION_MAJOR = 5

RAYLIB_VERSION_MINOR = 0

RAYLIB_VERSION_PATCH = 0

RAYLIB_VERSION = 5.0

PI = 3.141592653589793

DEG2RAD = PI / 180.0

RAD2DEG = 180.0 / PI

# Light Gray
LIGHTGRAY = Color(200, 200, 200, 255)

# Gray
GRAY = Color(130, 130, 130, 255)

# Dark Gray
DARKGRAY = Color(80, 80, 80, 255)

# Yellow
YELLOW = Color(253, 249, 0, 255)

# Gold
GOLD = Color(255, 203, 0, 255)

# Orange
ORANGE = Color(255, 161, 0, 255)

# Pink
PINK = Color(255, 109, 194, 255)

# Red
RED = Color(230, 41, 55, 255)

# Maroon
MAROON = Color(190, 33, 55, 255)

# Green
GREEN = Color(0, 228, 48, 255)

# Lime
LIME = Color(0, 158, 47, 255)

# Dark Green
DARKGREEN = Color(0, 117, 44, 255)

# Sky Blue
SKYBLUE = Color(102, 191, 255, 255)

# Blue
BLUE = Color(0, 121, 241, 255)

# Dark Blue
DARKBLUE = Color(0, 82, 172, 255)

# Purple
PURPLE = Color(200, 122, 255, 255)

# Violet
VIOLET = Color(135, 60, 190, 255)

# Dark Purple
DARKPURPLE = Color(112, 31, 126, 255)

# Beige
BEIGE = Color(211, 176, 131, 255)

# Brown
BROWN = Color(127, 106, 79, 255)

# Dark Brown
DARKBROWN = Color(76, 63, 47, 255)

# White
WHITE = Color(255, 255, 255, 255)

# Black
BLACK = Color(0, 0, 0, 255)

# Blank (Transparent)
BLANK = Color(0, 0, 0, 0)

# Magenta
MAGENTA = Color(255, 0, 255, 255)

# My own White (raylib logo)
RAYWHITE = Color(245, 245, 245, 255)

MOUSE_LEFT_BUTTON = MOUSE_BUTTON_LEFT

MOUSE_RIGHT_BUTTON = MOUSE_BUTTON_RIGHT

MOUSE_MIDDLE_BUTTON = MOUSE_BUTTON_MIDDLE

MATERIAL_MAP_DIFFUSE = MATERIAL_MAP_ALBEDO

MATERIAL_MAP_SPECULAR = MATERIAL_MAP_METALNESS

SHADER_LOC_MAP_DIFFUSE = SHADER_LOC_MAP_ALBEDO

SHADER_LOC_MAP_SPECULAR = SHADER_LOC_MAP_METALNESS


# rlapi::raymath
# ------------------------------------------------------------------------------
EPSILON = 1e-06


# rlapi::rlgl
# ------------------------------------------------------------------------------
RLGL_VERSION = 4.5

RL_DEFAULT_BATCH_BUFFER_ELEMENTS = 8192

# Default number of batch buffers (multi-buffering)
RL_DEFAULT_BATCH_BUFFERS = 1

# Default number of batch draw calls (by state changes: mode, texture)
RL_DEFAULT_BATCH_DRAWCALLS = 256

# Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS = 4

# Maximum size of Matrix stack
RL_MAX_MATRIX_STACK_SIZE = 32

# Maximum number of shader locations supported
RL_MAX_SHADER_LOCATIONS = 32

# Default near cull distance
RL_CULL_DISTANCE_NEAR = 0.01

# Default far cull distance
RL_CULL_DISTANCE_FAR = 1000.0

# GL_TEXTURE_WRAP_S
RL_TEXTURE_WRAP_S = 10242

# GL_TEXTURE_WRAP_T
RL_TEXTURE_WRAP_T = 10243

# GL_TEXTURE_MAG_FILTER
RL_TEXTURE_MAG_FILTER = 10240

# GL_TEXTURE_MIN_FILTER
RL_TEXTURE_MIN_FILTER = 10241

# GL_NEAREST
RL_TEXTURE_FILTER_NEAREST = 9728

# GL_LINEAR
RL_TEXTURE_FILTER_LINEAR = 9729

# GL_NEAREST_MIPMAP_NEAREST
RL_TEXTURE_FILTER_MIP_NEAREST = 9984

# GL_NEAREST_MIPMAP_LINEAR
RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR = 9986

# GL_LINEAR_MIPMAP_NEAREST
RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST = 9985

# GL_LINEAR_MIPMAP_LINEAR
RL_TEXTURE_FILTER_MIP_LINEAR = 9987

# Anisotropic filter (custom identifier)
RL_TEXTURE_FILTER_ANISOTROPIC = 12288

# Texture mipmap bias, percentage ratio (custom identifier)
RL_TEXTURE_MIPMAP_BIAS_RATIO = 16384

# GL_REPEAT
RL_TEXTURE_WRAP_REPEAT = 10497

# GL_CLAMP_TO_EDGE
RL_TEXTURE_WRAP_CLAMP = 33071

# GL_MIRRORED_REPEAT
RL_TEXTURE_WRAP_MIRROR_REPEAT = 33648

# GL_MIRROR_CLAMP_EXT
RL_TEXTURE_WRAP_MIRROR_CLAMP = 34626

# GL_MODELVIEW
RL_MODELVIEW = 5888

# GL_PROJECTION
RL_PROJECTION = 5889

# GL_TEXTURE
RL_TEXTURE = 5890

# GL_LINES
RL_LINES = 1

# GL_TRIANGLES
RL_TRIANGLES = 4

# GL_QUADS
RL_QUADS = 7

# GL_UNSIGNED_BYTE
RL_UNSIGNED_BYTE = 5121

# GL_FLOAT
RL_FLOAT = 5126

# GL_STREAM_DRAW
RL_STREAM_DRAW = 35040

# GL_STREAM_READ
RL_STREAM_READ = 35041

# GL_STREAM_COPY
RL_STREAM_COPY = 35042

# GL_STATIC_DRAW
RL_STATIC_DRAW = 35044

# GL_STATIC_READ
RL_STATIC_READ = 35045

# GL_STATIC_COPY
RL_STATIC_COPY = 35046

# GL_DYNAMIC_DRAW
RL_DYNAMIC_DRAW = 35048

# GL_DYNAMIC_READ
RL_DYNAMIC_READ = 35049

# GL_DYNAMIC_COPY
RL_DYNAMIC_COPY = 35050

# GL_FRAGMENT_SHADER
RL_FRAGMENT_SHADER = 35632

# GL_VERTEX_SHADER
RL_VERTEX_SHADER = 35633

# GL_COMPUTE_SHADER
RL_COMPUTE_SHADER = 37305

# GL_ZERO
RL_ZERO = 0

# GL_ONE
RL_ONE = 1

# GL_SRC_COLOR
RL_SRC_COLOR = 768

# GL_ONE_MINUS_SRC_COLOR
RL_ONE_MINUS_SRC_COLOR = 769

# GL_SRC_ALPHA
RL_SRC_ALPHA = 770

# GL_ONE_MINUS_SRC_ALPHA
RL_ONE_MINUS_SRC_ALPHA = 771

# GL_DST_ALPHA
RL_DST_ALPHA = 772

# GL_ONE_MINUS_DST_ALPHA
RL_ONE_MINUS_DST_ALPHA = 773

# GL_DST_COLOR
RL_DST_COLOR = 774

# GL_ONE_MINUS_DST_COLOR
RL_ONE_MINUS_DST_COLOR = 775

# GL_SRC_ALPHA_SATURATE
RL_SRC_ALPHA_SATURATE = 776

# GL_CONSTANT_COLOR
RL_CONSTANT_COLOR = 32769

# GL_ONE_MINUS_CONSTANT_COLOR
RL_ONE_MINUS_CONSTANT_COLOR = 32770

# GL_CONSTANT_ALPHA
RL_CONSTANT_ALPHA = 32771

# GL_ONE_MINUS_CONSTANT_ALPHA
RL_ONE_MINUS_CONSTANT_ALPHA = 32772

# GL_FUNC_ADD
RL_FUNC_ADD = 32774

# GL_MIN
RL_MIN = 32775

# GL_MAX
RL_MAX = 32776

# GL_FUNC_SUBTRACT
RL_FUNC_SUBTRACT = 32778

# GL_FUNC_REVERSE_SUBTRACT
RL_FUNC_REVERSE_SUBTRACT = 32779

# GL_BLEND_EQUATION
RL_BLEND_EQUATION = 32777

# GL_BLEND_EQUATION_RGB   // (Same as BLEND_EQUATION)
RL_BLEND_EQUATION_RGB = 32777

# GL_BLEND_EQUATION_ALPHA
RL_BLEND_EQUATION_ALPHA = 34877

# GL_BLEND_DST_RGB
RL_BLEND_DST_RGB = 32968

# GL_BLEND_SRC_RGB
RL_BLEND_SRC_RGB = 32969

# GL_BLEND_DST_ALPHA
RL_BLEND_DST_ALPHA = 32970

# GL_BLEND_SRC_ALPHA
RL_BLEND_SRC_ALPHA = 32971

# GL_BLEND_COLOR
RL_BLEND_COLOR = 32773

RL_SHADER_LOC_MAP_DIFFUSE = RL_SHADER_LOC_MAP_ALBEDO

RL_SHADER_LOC_MAP_SPECULAR = RL_SHADER_LOC_MAP_METALNESS

# endregion (defines)

# region FUNCTIONS

# rlapi::raylib
# ------------------------------------------------------------------------------

def init_window(width, height, title):
    # type: (int, int, bytes | str | None) -> None
    """Initialize window and OpenGL context"""
    _InitWindow(_int(width), _int(height), _str_in(title))


def close_window():
    # type: () -> None
    """Close window and unload OpenGL context"""
    _CloseWindow()


def window_should_close():
    # type: () -> bool
    """Check if application should close (KEY_ESCAPE pressed or windows close icon clicked)"""
    return _WindowShouldClose()


def is_window_ready():
    # type: () -> bool
    """Check if window has been initialized successfully"""
    return _IsWindowReady()


def is_window_fullscreen():
    # type: () -> bool
    """Check if window is currently fullscreen"""
    return _IsWindowFullscreen()


def is_window_hidden():
    # type: () -> bool
    """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
    return _IsWindowHidden()


def is_window_minimized():
    # type: () -> bool
    """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
    return _IsWindowMinimized()


def is_window_maximized():
    # type: () -> bool
    """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
    return _IsWindowMaximized()


def is_window_focused():
    # type: () -> bool
    """Check if window is currently focused (only PLATFORM_DESKTOP)"""
    return _IsWindowFocused()


def is_window_resized():
    # type: () -> bool
    """Check if window has been resized last frame"""
    return _IsWindowResized()


def is_window_state(flag):
    # type: (int) -> bool
    """Check if one specific window flag is enabled"""
    return _IsWindowState(_int(flag))


def set_window_state(flags):
    # type: (int) -> None
    """Set window configuration state using flags (only PLATFORM_DESKTOP)"""
    _SetWindowState(_int(flags))


def clear_window_state(flags):
    # type: (int) -> None
    """Clear window configuration state flags"""
    _ClearWindowState(_int(flags))


def toggle_fullscreen():
    # type: () -> None
    """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
    _ToggleFullscreen()


def toggle_borderless_windowed():
    # type: () -> None
    """Toggle window state: borderless windowed (only PLATFORM_DESKTOP)"""
    _ToggleBorderlessWindowed()


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
    """Set icon for window (single image, RGBA 32bit, only PLATFORM_DESKTOP)"""
    _SetWindowIcon(image)


def set_window_icons(images, count):
    # type: (ImagePtr, int) -> None
    """Set icon for window (multiple images, RGBA 32bit, only PLATFORM_DESKTOP)"""
    _SetWindowIcons(images, _int(count))


def set_window_title(title):
    # type: (bytes | str | None) -> None
    """Set title for window (only PLATFORM_DESKTOP and PLATFORM_WEB)"""
    _SetWindowTitle(_str_in(title))


def set_window_position(x, y):
    # type: (int, int) -> None
    """Set window position on screen (only PLATFORM_DESKTOP)"""
    _SetWindowPosition(_int(x), _int(y))


def set_window_monitor(monitor):
    # type: (int) -> None
    """Set monitor for the current window"""
    _SetWindowMonitor(_int(monitor))


def set_window_min_size(width, height):
    # type: (int, int) -> None
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
    _SetWindowMinSize(_int(width), _int(height))


def set_window_max_size(width, height):
    # type: (int, int) -> None
    """Set window maximum dimensions (for FLAG_WINDOW_RESIZABLE)"""
    _SetWindowMaxSize(_int(width), _int(height))


def set_window_size(width, height):
    # type: (int, int) -> None
    """Set window dimensions"""
    _SetWindowSize(_int(width), _int(height))


def set_window_opacity(opacity):
    # type: (float) -> None
    """Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)"""
    _SetWindowOpacity(_float(opacity))


def set_window_focused():
    # type: () -> None
    """Set window focused (only PLATFORM_DESKTOP)"""
    _SetWindowFocused()


def get_window_handle():
    # type: () -> bytes | str | None
    """Get native window handle"""
    return _GetWindowHandle()


def get_screen_width():
    # type: () -> int
    """Get current screen width"""
    return _GetScreenWidth()


def get_screen_height():
    # type: () -> int
    """Get current screen height"""
    return _GetScreenHeight()


def get_render_width():
    # type: () -> int
    """Get current render width (it considers HiDPI)"""
    return _GetRenderWidth()


def get_render_height():
    # type: () -> int
    """Get current render height (it considers HiDPI)"""
    return _GetRenderHeight()


def get_monitor_count():
    # type: () -> int
    """Get number of connected monitors"""
    return _GetMonitorCount()


def get_current_monitor():
    # type: () -> int
    """Get current connected monitor"""
    return _GetCurrentMonitor()


def get_monitor_position(monitor):
    # type: (int) -> Vector2
    """Get specified monitor position"""
    return _GetMonitorPosition(_int(monitor))


def get_monitor_width(monitor):
    # type: (int) -> int
    """Get specified monitor width (current video mode used by monitor)"""
    return _GetMonitorWidth(_int(monitor))


def get_monitor_height(monitor):
    # type: (int) -> int
    """Get specified monitor height (current video mode used by monitor)"""
    return _GetMonitorHeight(_int(monitor))


def get_monitor_physical_width(monitor):
    # type: (int) -> int
    """Get specified monitor physical width in millimetres"""
    return _GetMonitorPhysicalWidth(_int(monitor))


def get_monitor_physical_height(monitor):
    # type: (int) -> int
    """Get specified monitor physical height in millimetres"""
    return _GetMonitorPhysicalHeight(_int(monitor))


def get_monitor_refresh_rate(monitor):
    # type: (int) -> int
    """Get specified monitor refresh rate"""
    return _GetMonitorRefreshRate(_int(monitor))


def get_window_position():
    # type: () -> Vector2
    """Get window position XY on monitor"""
    return _GetWindowPosition()


def get_window_scale_dpi():
    # type: () -> Vector2
    """Get window scale DPI factor"""
    return _GetWindowScaleDPI()


def get_monitor_name(monitor):
    # type: (int) -> bytes | str | None
    """Get the human-readable, UTF-8 encoded name of the specified monitor"""
    return _str_out(_GetMonitorName(_int(monitor)))


def set_clipboard_text(text):
    # type: (bytes | str | None) -> None
    """Set clipboard text content"""
    _SetClipboardText(_str_in(text))


def get_clipboard_text():
    # type: () -> bytes | str | None
    """Get clipboard text content"""
    return _str_out(_GetClipboardText())


def enable_event_waiting():
    # type: () -> None
    """Enable waiting for events on EndDrawing(), no automatic event polling"""
    _EnableEventWaiting()


def disable_event_waiting():
    # type: () -> None
    """Disable waiting for events on EndDrawing(), automatic events polling"""
    _DisableEventWaiting()


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
    return _IsCursorHidden()


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
    return _IsCursorOnScreen()


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
    _BeginBlendMode(_int(mode))


def end_blend_mode():
    # type: () -> None
    """End blending mode (reset to default: alpha blending)"""
    _EndBlendMode()


def begin_scissor_mode(x, y, width, height):
    # type: (int, int, int, int) -> None
    """Begin scissor mode (define screen area for following drawing)"""
    _BeginScissorMode(_int(x), _int(y), _int(width), _int(height))


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
    return _LoadVrStereoConfig(device)


def unload_vr_stereo_config(config):
    # type: (VrStereoConfig) -> None
    """Unload VR stereo config"""
    _UnloadVrStereoConfig(config)


def load_shader(vs_file_name, fs_file_name):
    # type: (bytes | str | None, bytes | str | None) -> Shader
    """Load shader from files and bind default locations"""
    return _LoadShader(_str_in(vs_file_name), _str_in(fs_file_name))


def load_shader_from_memory(vs_code, fs_code):
    # type: (bytes | str | None, bytes | str | None) -> Shader
    """Load shader from code strings and bind default locations"""
    return _LoadShaderFromMemory(_str_in(vs_code), _str_in(fs_code))


def is_shader_ready(shader):
    # type: (Shader) -> bool
    """Check if a shader is ready"""
    return _IsShaderReady(shader)


def get_shader_location(shader, uniform_name):
    # type: (Shader, bytes | str | None) -> int
    """Get shader uniform location"""
    return _GetShaderLocation(shader, _str_in(uniform_name))


def get_shader_location_attrib(shader, attrib_name):
    # type: (Shader, bytes | str | None) -> int
    """Get shader attribute location"""
    return _GetShaderLocationAttrib(shader, _str_in(attrib_name))


def set_shader_value(shader, loc_index, value, uniform_type):
    # type: (Shader, int, bytes | str | None, int) -> None
    """Set shader uniform value"""
    _SetShaderValue(shader, _int(loc_index), value, _int(uniform_type))


def set_shader_value_v(shader, loc_index, value, uniform_type, count):
    # type: (Shader, int, bytes | str | None, int, int) -> None
    """Set shader uniform value vector"""
    _SetShaderValueV(shader, _int(loc_index), value, _int(uniform_type), _int(count))


def set_shader_value_matrix(shader, loc_index, mat):
    # type: (Shader, int, Matrix) -> None
    """Set shader uniform value (matrix 4x4)"""
    _SetShaderValueMatrix(shader, _int(loc_index), mat)


def set_shader_value_texture(shader, loc_index, texture):
    # type: (Shader, int, Texture2D) -> None
    """Set shader uniform value for texture (sampler2d)"""
    _SetShaderValueTexture(shader, _int(loc_index), texture)


def unload_shader(shader):
    # type: (Shader) -> None
    """Unload shader from GPU memory (VRAM)"""
    _UnloadShader(shader)


def get_mouse_ray(mouse_position, camera):
    # type: (Vector2, Camera) -> Ray
    """Get a ray trace from mouse position"""
    return _GetMouseRay(_vec2(mouse_position), camera)


def get_camera_matrix(camera):
    # type: (Camera) -> Matrix
    """Get camera transform matrix (view matrix)"""
    return _GetCameraMatrix(camera)


def get_camera_matrix2d(camera):
    # type: (Camera2D) -> Matrix
    """Get camera 2d transform matrix"""
    return _GetCameraMatrix2D(camera)


def get_world_to_screen(position, camera):
    # type: (Vector3, Camera) -> Vector2
    """Get the screen space position for a 3d world space position"""
    return _GetWorldToScreen(_vec3(position), camera)


def get_screen_to_world2d(position, camera):
    # type: (Vector2, Camera2D) -> Vector2
    """Get the world space position for a 2d camera screen space position"""
    return _GetScreenToWorld2D(_vec2(position), camera)


def get_world_to_screen_ex(position, camera, width, height):
    # type: (Vector3, Camera, int, int) -> Vector2
    """Get size position for a 3d world space position"""
    return _GetWorldToScreenEx(_vec3(position), camera, _int(width), _int(height))


def get_world_to_screen2d(position, camera):
    # type: (Vector2, Camera2D) -> Vector2
    """Get the screen space position for a 2d camera world space position"""
    return _GetWorldToScreen2D(_vec2(position), camera)


def set_target_fps(fps):
    # type: (int) -> None
    """Set target FPS (maximum)"""
    _SetTargetFPS(_int(fps))


def get_frame_time():
    # type: () -> float
    """Get time in seconds for last frame drawn (delta time)"""
    return _GetFrameTime()


def get_time():
    # type: () -> float
    """Get elapsed time in seconds since InitWindow()"""
    return _GetTime()


def get_fps():
    # type: () -> int
    """Get current FPS"""
    return _GetFPS()


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
    _WaitTime(_float(seconds))


def set_random_seed(seed):
    # type: (int) -> None
    """Set the seed for the random number generator"""
    _SetRandomSeed(_int(seed))


def get_random_value(min_, max_):
    # type: (int, int) -> int
    """Get a random value between min and max (both included)"""
    return _GetRandomValue(_int(min_), _int(max_))


def load_random_sequence(count, min_, max_):
    # type: (int, int, int) -> IntPtr
    """Load random values sequence, no values repeated"""
    return _LoadRandomSequence(_int(count), _int(min_), _int(max_))


def unload_random_sequence(sequence):
    # type: (IntPtr) -> None
    """Unload random values sequence"""
    _UnloadRandomSequence(sequence)


def take_screenshot(file_name):
    # type: (bytes | str | None) -> None
    """Takes a screenshot of current screen (filename extension defines format)"""
    _TakeScreenshot(_str_in(file_name))


def set_config_flags(flags):
    # type: (int) -> None
    """Setup init configuration flags (view FLAGS)"""
    _SetConfigFlags(_int(flags))


def open_url(url):
    # type: (bytes | str | None) -> None
    """Open URL with default system browser (if available)"""
    _OpenURL(_str_in(url))


def trace_log(log_level, text, *args):
    # type: (int, bytes | str | None, ...) -> None
    """Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)"""
    _TraceLog(_int(log_level), _str_in(text), *args)


def set_trace_log_level(log_level):
    # type: (int) -> None
    """Set the current threshold (minimum) log level"""
    _SetTraceLogLevel(_int(log_level))


def mem_alloc(size):
    # type: (int) -> bytes | str | None
    """Internal memory allocator"""
    return _MemAlloc(_int(size))


def mem_realloc(ptr, size):
    # type: (bytes | str | None, int) -> bytes | str | None
    """Internal memory reallocator"""
    return _MemRealloc(ptr, _int(size))


def mem_free(ptr):
    # type: (bytes | str | None) -> None
    """Internal memory free"""
    _MemFree(ptr)


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


def load_file_data(file_name, data_size):
    # type: (bytes | str | None, IntPtr) -> int
    """Load file data as byte array (read)"""
    return _LoadFileData(_str_in(file_name), data_size)


def unload_file_data(data):
    # type: (int) -> None
    """Unload file data allocated by LoadFileData()"""
    _UnloadFileData(_int(data, (0, 255)))


def save_file_data(file_name, data, data_size):
    # type: (bytes | str | None, bytes | str | None, int) -> bool
    """Save data to file from byte array (write), returns true on success"""
    return _SaveFileData(_str_in(file_name), data, _int(data_size))


def export_data_as_code(data, data_size, file_name):
    # type: (int, int, bytes | str | None) -> bool
    """Export data to code (.h), returns true on success"""
    return _ExportDataAsCode(_int(data, (0, 255)), _int(data_size), _str_in(file_name))


def load_file_text(file_name):
    # type: (bytes | str | None) -> bytes | str | None
    """Load text data from file (read), returns a '\0' terminated string"""
    return _str_out(_LoadFileText(_str_in(file_name)))


def unload_file_text(text):
    # type: (bytes | str | None) -> None
    """Unload file text data allocated by LoadFileText()"""
    _UnloadFileText(_str_in(text))


def save_file_text(file_name, text):
    # type: (bytes | str | None, bytes | str | None) -> bool
    """Save text data to file (write), string must be '\0' terminated, returns true on success"""
    return _SaveFileText(_str_in(file_name), _str_in(text))


def file_exists(file_name):
    # type: (bytes | str | None) -> bool
    """Check if file exists"""
    return _FileExists(_str_in(file_name))


def directory_exists(dir_path):
    # type: (bytes | str | None) -> bool
    """Check if a directory path exists"""
    return _DirectoryExists(_str_in(dir_path))


def is_file_extension(file_name, ext):
    # type: (bytes | str | None, bytes | str | None) -> bool
    """Check file extension (including point: .png, .wav)"""
    return _IsFileExtension(_str_in(file_name), _str_in(ext))


def get_file_length(file_name):
    # type: (bytes | str | None) -> int
    """Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)"""
    return _GetFileLength(_str_in(file_name))


def get_file_extension(file_name):
    # type: (bytes | str | None) -> bytes | str | None
    """Get pointer to extension for a filename string (includes dot: '.png')"""
    return _str_out(_GetFileExtension(_str_in(file_name)))


def get_file_name(file_path):
    # type: (bytes | str | None) -> bytes | str | None
    """Get pointer to filename for a path string"""
    return _str_out(_GetFileName(_str_in(file_path)))


def get_file_name_without_ext(file_path):
    # type: (bytes | str | None) -> bytes | str | None
    """Get filename string without extension (uses static string)"""
    return _str_out(_GetFileNameWithoutExt(_str_in(file_path)))


def get_directory_path(file_path):
    # type: (bytes | str | None) -> bytes | str | None
    """Get full path for a given fileName with path (uses static string)"""
    return _str_out(_GetDirectoryPath(_str_in(file_path)))


def get_prev_directory_path(dir_path):
    # type: (bytes | str | None) -> bytes | str | None
    """Get previous directory path for a given path (uses static string)"""
    return _str_out(_GetPrevDirectoryPath(_str_in(dir_path)))


def get_working_directory():
    # type: () -> bytes | str | None
    """Get current working directory (uses static string)"""
    return _str_out(_GetWorkingDirectory())


def get_application_directory():
    # type: () -> bytes | str | None
    """Get the directory of the running application (uses static string)"""
    return _str_out(_GetApplicationDirectory())


def change_directory(dir_):
    # type: (bytes | str | None) -> bool
    """Change working directory, return true on success"""
    return _ChangeDirectory(_str_in(dir_))


def is_path_file(path):
    # type: (bytes | str | None) -> bool
    """Check if a given path is a file or a directory"""
    return _IsPathFile(_str_in(path))


def load_directory_files(dir_path):
    # type: (bytes | str | None) -> FilePathList
    """Load directory filepaths"""
    return _LoadDirectoryFiles(_str_in(dir_path))


def load_directory_files_ex(base_path, filter_, scan_subdirs):
    # type: (bytes | str | None, bytes | str | None, bool) -> FilePathList
    """Load directory filepaths with extension filtering and recursive directory scan"""
    return _LoadDirectoryFilesEx(_str_in(base_path), _str_in(filter_), _bool(scan_subdirs))


def unload_directory_files(files):
    # type: (FilePathList) -> None
    """Unload filepaths"""
    _UnloadDirectoryFiles(files)


def is_file_dropped():
    # type: () -> bool
    """Check if a file has been dropped into window"""
    return _IsFileDropped()


def load_dropped_files():
    # type: () -> FilePathList
    """Load dropped filepaths"""
    return _LoadDroppedFiles()


def unload_dropped_files(files):
    # type: (FilePathList) -> None
    """Unload dropped filepaths"""
    _UnloadDroppedFiles(files)


def get_file_mod_time(file_name):
    # type: (bytes | str | None) -> int
    """Get file modification time (last write time)"""
    return _GetFileModTime(_str_in(file_name))


def compress_data(data, data_size, comp_data_size):
    # type: (int, int, IntPtr) -> int
    """Compress data (DEFLATE algorithm), memory must be MemFree()"""
    return _CompressData(_int(data, (0, 255)), _int(data_size), comp_data_size)


def decompress_data(comp_data, comp_data_size, data_size):
    # type: (int, int, IntPtr) -> int
    """Decompress data (DEFLATE algorithm), memory must be MemFree()"""
    return _DecompressData(_int(comp_data, (0, 255)), _int(comp_data_size), data_size)


def encode_data_base64(data, data_size, output_size):
    # type: (int, int, IntPtr) -> bytes | str | None
    """Encode data to Base64 string, memory must be MemFree()"""
    return _EncodeDataBase64(_int(data, (0, 255)), _int(data_size), output_size)


def decode_data_base64(data, output_size):
    # type: (int, IntPtr) -> int
    """Decode Base64 string data, memory must be MemFree()"""
    return _DecodeDataBase64(_int(data, (0, 255)), output_size)


def load_automation_event_list(file_name):
    # type: (bytes | str | None) -> AutomationEventList
    """Load automation events list from file, NULL for empty list, capacity = MAX_AUTOMATION_EVENTS"""
    return _LoadAutomationEventList(_str_in(file_name))


def unload_automation_event_list(list_):
    # type: (AutomationEventListPtr) -> None
    """Unload automation events list from file"""
    _UnloadAutomationEventList(list_)


def export_automation_event_list(list_, file_name):
    # type: (AutomationEventList, bytes | str | None) -> bool
    """Export automation events list as text file"""
    return _ExportAutomationEventList(list_, _str_in(file_name))


def set_automation_event_list(list_):
    # type: (AutomationEventListPtr) -> None
    """Set automation event list to record to"""
    _SetAutomationEventList(list_)


def set_automation_event_base_frame(frame):
    # type: (int) -> None
    """Set automation event internal base frame to start recording"""
    _SetAutomationEventBaseFrame(_int(frame))


def start_automation_event_recording():
    # type: () -> None
    """Start recording automation events (AutomationEventList must be set)"""
    _StartAutomationEventRecording()


def stop_automation_event_recording():
    # type: () -> None
    """Stop recording automation events"""
    _StopAutomationEventRecording()


def play_automation_event(event):
    # type: (AutomationEvent) -> None
    """Play a recorded automation event"""
    _PlayAutomationEvent(event)


def is_key_pressed(key):
    # type: (int) -> bool
    """Check if a key has been pressed once"""
    return _IsKeyPressed(_int(key))


def is_key_pressed_repeat(key):
    # type: (int) -> bool
    """Check if a key has been pressed again (Only PLATFORM_DESKTOP)"""
    return _IsKeyPressedRepeat(_int(key))


def is_key_down(key):
    # type: (int) -> bool
    """Check if a key is being pressed"""
    return _IsKeyDown(_int(key))


def is_key_released(key):
    # type: (int) -> bool
    """Check if a key has been released once"""
    return _IsKeyReleased(_int(key))


def is_key_up(key):
    # type: (int) -> bool
    """Check if a key is NOT being pressed"""
    return _IsKeyUp(_int(key))


def get_key_pressed():
    # type: () -> int
    """Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty"""
    return _GetKeyPressed()


def get_char_pressed():
    # type: () -> int
    """Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty"""
    return _GetCharPressed()


def set_exit_key(key):
    # type: (int) -> None
    """Set a custom key to exit program (default is ESC)"""
    _SetExitKey(_int(key))


def is_gamepad_available(gamepad):
    # type: (int) -> bool
    """Check if a gamepad is available"""
    return _IsGamepadAvailable(_int(gamepad))


def get_gamepad_name(gamepad):
    # type: (int) -> bytes | str | None
    """Get gamepad internal name id"""
    return _str_out(_GetGamepadName(_int(gamepad)))


def is_gamepad_button_pressed(gamepad, button):
    # type: (int, int) -> bool
    """Check if a gamepad button has been pressed once"""
    return _IsGamepadButtonPressed(_int(gamepad), _int(button))


def is_gamepad_button_down(gamepad, button):
    # type: (int, int) -> bool
    """Check if a gamepad button is being pressed"""
    return _IsGamepadButtonDown(_int(gamepad), _int(button))


def is_gamepad_button_released(gamepad, button):
    # type: (int, int) -> bool
    """Check if a gamepad button has been released once"""
    return _IsGamepadButtonReleased(_int(gamepad), _int(button))


def is_gamepad_button_up(gamepad, button):
    # type: (int, int) -> bool
    """Check if a gamepad button is NOT being pressed"""
    return _IsGamepadButtonUp(_int(gamepad), _int(button))


def get_gamepad_button_pressed():
    # type: () -> int
    """Get the last gamepad button pressed"""
    return _GetGamepadButtonPressed()


def get_gamepad_axis_count(gamepad):
    # type: (int) -> int
    """Get gamepad axis count for a gamepad"""
    return _GetGamepadAxisCount(_int(gamepad))


def get_gamepad_axis_movement(gamepad, axis):
    # type: (int, int) -> float
    """Get axis movement value for a gamepad axis"""
    return _GetGamepadAxisMovement(_int(gamepad), _int(axis))


def set_gamepad_mappings(mappings):
    # type: (bytes | str | None) -> int
    """Set internal gamepad mappings (SDL_GameControllerDB)"""
    return _SetGamepadMappings(_str_in(mappings))


def is_mouse_button_pressed(button):
    # type: (int) -> bool
    """Check if a mouse button has been pressed once"""
    return _IsMouseButtonPressed(_int(button))


def is_mouse_button_down(button):
    # type: (int) -> bool
    """Check if a mouse button is being pressed"""
    return _IsMouseButtonDown(_int(button))


def is_mouse_button_released(button):
    # type: (int) -> bool
    """Check if a mouse button has been released once"""
    return _IsMouseButtonReleased(_int(button))


def is_mouse_button_up(button):
    # type: (int) -> bool
    """Check if a mouse button is NOT being pressed"""
    return _IsMouseButtonUp(_int(button))


def get_mouse_x():
    # type: () -> int
    """Get mouse position X"""
    return _GetMouseX()


def get_mouse_y():
    # type: () -> int
    """Get mouse position Y"""
    return _GetMouseY()


def get_mouse_position():
    # type: () -> Vector2
    """Get mouse position XY"""
    return _GetMousePosition()


def get_mouse_delta():
    # type: () -> Vector2
    """Get mouse delta between frames"""
    return _GetMouseDelta()


def set_mouse_position(x, y):
    # type: (int, int) -> None
    """Set mouse position XY"""
    _SetMousePosition(_int(x), _int(y))


def set_mouse_offset(offset_x, offset_y):
    # type: (int, int) -> None
    """Set mouse offset"""
    _SetMouseOffset(_int(offset_x), _int(offset_y))


def set_mouse_scale(scale_x, scale_y):
    # type: (float, float) -> None
    """Set mouse scaling"""
    _SetMouseScale(_float(scale_x), _float(scale_y))


def get_mouse_wheel_move():
    # type: () -> float
    """Get mouse wheel movement for X or Y, whichever is larger"""
    return _GetMouseWheelMove()


def get_mouse_wheel_move_v():
    # type: () -> Vector2
    """Get mouse wheel movement for both X and Y"""
    return _GetMouseWheelMoveV()


def set_mouse_cursor(cursor):
    # type: (int) -> None
    """Set mouse cursor"""
    _SetMouseCursor(_int(cursor))


def get_touch_x():
    # type: () -> int
    """Get touch position X for touch point 0 (relative to screen size)"""
    return _GetTouchX()


def get_touch_y():
    # type: () -> int
    """Get touch position Y for touch point 0 (relative to screen size)"""
    return _GetTouchY()


def get_touch_position(index):
    # type: (int) -> Vector2
    """Get touch position XY for a touch point index (relative to screen size)"""
    return _GetTouchPosition(_int(index))


def get_touch_point_id(index):
    # type: (int) -> int
    """Get touch point identifier for given index"""
    return _GetTouchPointId(_int(index))


def get_touch_point_count():
    # type: () -> int
    """Get number of touch points"""
    return _GetTouchPointCount()


def set_gestures_enabled(flags):
    # type: (int) -> None
    """Enable a set of gestures using flags"""
    _SetGesturesEnabled(_int(flags))


def is_gesture_detected(gesture):
    # type: (int) -> bool
    """Check if a gesture have been detected"""
    return _IsGestureDetected(_int(gesture))


def get_gesture_detected():
    # type: () -> int
    """Get latest detected gesture"""
    return _GetGestureDetected()


def get_gesture_hold_duration():
    # type: () -> float
    """Get gesture hold time in milliseconds"""
    return _GetGestureHoldDuration()


def get_gesture_drag_vector():
    # type: () -> Vector2
    """Get gesture drag vector"""
    return _GetGestureDragVector()


def get_gesture_drag_angle():
    # type: () -> float
    """Get gesture drag angle"""
    return _GetGestureDragAngle()


def get_gesture_pinch_vector():
    # type: () -> Vector2
    """Get gesture pinch delta"""
    return _GetGesturePinchVector()


def get_gesture_pinch_angle():
    # type: () -> float
    """Get gesture pinch angle"""
    return _GetGesturePinchAngle()


def update_camera(camera, mode):
    # type: (CameraPtr, int) -> None
    """Update camera position for selected mode"""
    _UpdateCamera(camera, _int(mode))


def update_camera_pro(camera, movement, rotation, zoom):
    # type: (CameraPtr, Vector3, Vector3, float) -> None
    """Update camera movement/rotation"""
    _UpdateCameraPro(camera, _vec3(movement), _vec3(rotation), _float(zoom))


def set_shapes_texture(texture, source):
    # type: (Texture2D, Rectangle) -> None
    """Set texture and rectangle to be used on shapes drawing"""
    _SetShapesTexture(texture, _rect(source))


def draw_pixel(pos_x, pos_y, color):
    # type: (int, int, Color) -> None
    """Draw a pixel"""
    _DrawPixel(_int(pos_x), _int(pos_y), _color(color))


def draw_pixel_v(position, color):
    # type: (Vector2, Color) -> None
    """Draw a pixel (Vector version)"""
    _DrawPixelV(_vec2(position), _color(color))


def draw_line(start_pos_x, start_pos_y, end_pos_x, end_pos_y, color):
    # type: (int, int, int, int, Color) -> None
    """Draw a line"""
    _DrawLine(_int(start_pos_x), _int(start_pos_y), _int(end_pos_x), _int(end_pos_y), _color(color))


def draw_line_v(start_pos, end_pos, color):
    # type: (Vector2, Vector2, Color) -> None
    """Draw a line (using gl lines)"""
    _DrawLineV(_vec2(start_pos), _vec2(end_pos), _color(color))


def draw_line_ex(start_pos, end_pos, thick, color):
    # type: (Vector2, Vector2, float, Color) -> None
    """Draw a line (using triangles/quads)"""
    _DrawLineEx(_vec2(start_pos), _vec2(end_pos), _float(thick), _color(color))


def draw_line_strip(points, point_count, color):
    # type: (Vector2Ptr, int, Color) -> None
    """Draw lines sequence (using gl lines)"""
    _DrawLineStrip(points, _int(point_count), _color(color))


def draw_line_bezier(start_pos, end_pos, thick, color):
    # type: (Vector2, Vector2, float, Color) -> None
    """Draw line segment cubic-bezier in-out interpolation"""
    _DrawLineBezier(_vec2(start_pos), _vec2(end_pos), _float(thick), _color(color))


def draw_circle(center_x, center_y, radius, color):
    # type: (int, int, float, Color) -> None
    """Draw a color-filled circle"""
    _DrawCircle(_int(center_x), _int(center_y), _float(radius), _color(color))


def draw_circle_sector(center, radius, start_angle, end_angle, segments, color):
    # type: (Vector2, float, float, float, int, Color) -> None
    """Draw a piece of a circle"""
    _DrawCircleSector(_vec2(center), _float(radius), _float(start_angle), _float(end_angle), _int(segments), _color(color))


def draw_circle_sector_lines(center, radius, start_angle, end_angle, segments, color):
    # type: (Vector2, float, float, float, int, Color) -> None
    """Draw circle sector outline"""
    _DrawCircleSectorLines(_vec2(center), _float(radius), _float(start_angle), _float(end_angle), _int(segments), _color(color))


def draw_circle_gradient(center_x, center_y, radius, color1, color2):
    # type: (int, int, float, Color, Color) -> None
    """Draw a gradient-filled circle"""
    _DrawCircleGradient(_int(center_x), _int(center_y), _float(radius), _color(color1), _color(color2))


def draw_circle_v(center, radius, color):
    # type: (Vector2, float, Color) -> None
    """Draw a color-filled circle (Vector version)"""
    _DrawCircleV(_vec2(center), _float(radius), _color(color))


def draw_circle_lines(center_x, center_y, radius, color):
    # type: (int, int, float, Color) -> None
    """Draw circle outline"""
    _DrawCircleLines(_int(center_x), _int(center_y), _float(radius), _color(color))


def draw_circle_lines_v(center, radius, color):
    # type: (Vector2, float, Color) -> None
    """Draw circle outline (Vector version)"""
    _DrawCircleLinesV(_vec2(center), _float(radius), _color(color))


def draw_ellipse(center_x, center_y, radius_h, radius_v, color):
    # type: (int, int, float, float, Color) -> None
    """Draw ellipse"""
    _DrawEllipse(_int(center_x), _int(center_y), _float(radius_h), _float(radius_v), _color(color))


def draw_ellipse_lines(center_x, center_y, radius_h, radius_v, color):
    # type: (int, int, float, float, Color) -> None
    """Draw ellipse outline"""
    _DrawEllipseLines(_int(center_x), _int(center_y), _float(radius_h), _float(radius_v), _color(color))


def draw_ring(center, inner_radius, outer_radius, start_angle, end_angle, segments, color):
    # type: (Vector2, float, float, float, float, int, Color) -> None
    """Draw ring"""
    _DrawRing(_vec2(center), _float(inner_radius), _float(outer_radius), _float(start_angle), _float(end_angle), _int(segments), _color(color))


def draw_ring_lines(center, inner_radius, outer_radius, start_angle, end_angle, segments, color):
    # type: (Vector2, float, float, float, float, int, Color) -> None
    """Draw ring outline"""
    _DrawRingLines(_vec2(center), _float(inner_radius), _float(outer_radius), _float(start_angle), _float(end_angle), _int(segments), _color(color))


def draw_rectangle(pos_x, pos_y, width, height, color):
    # type: (int, int, int, int, Color) -> None
    """Draw a color-filled rectangle"""
    _DrawRectangle(_int(pos_x), _int(pos_y), _int(width), _int(height), _color(color))


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
    _DrawRectanglePro(_rect(rec), _vec2(origin), _float(rotation), _color(color))


def draw_rectangle_gradient_v(pos_x, pos_y, width, height, color1, color2):
    # type: (int, int, int, int, Color, Color) -> None
    """Draw a vertical-gradient-filled rectangle"""
    _DrawRectangleGradientV(_int(pos_x), _int(pos_y), _int(width), _int(height), _color(color1), _color(color2))


def draw_rectangle_gradient_h(pos_x, pos_y, width, height, color1, color2):
    # type: (int, int, int, int, Color, Color) -> None
    """Draw a horizontal-gradient-filled rectangle"""
    _DrawRectangleGradientH(_int(pos_x), _int(pos_y), _int(width), _int(height), _color(color1), _color(color2))


def draw_rectangle_gradient_ex(rec, col1, col2, col3, col4):
    # type: (Rectangle, Color, Color, Color, Color) -> None
    """Draw a gradient-filled rectangle with custom vertex colors"""
    _DrawRectangleGradientEx(_rect(rec), _color(col1), _color(col2), _color(col3), _color(col4))


def draw_rectangle_lines(pos_x, pos_y, width, height, color):
    # type: (int, int, int, int, Color) -> None
    """Draw rectangle outline"""
    _DrawRectangleLines(_int(pos_x), _int(pos_y), _int(width), _int(height), _color(color))


def draw_rectangle_lines_ex(rec, line_thick, color):
    # type: (Rectangle, float, Color) -> None
    """Draw rectangle outline with extended parameters"""
    _DrawRectangleLinesEx(_rect(rec), _float(line_thick), _color(color))


def draw_rectangle_rounded(rec, roundness, segments, color):
    # type: (Rectangle, float, int, Color) -> None
    """Draw rectangle with rounded edges"""
    _DrawRectangleRounded(_rect(rec), _float(roundness), _int(segments), _color(color))


def draw_rectangle_rounded_lines(rec, roundness, segments, line_thick, color):
    # type: (Rectangle, float, int, float, Color) -> None
    """Draw rectangle with rounded edges outline"""
    _DrawRectangleRoundedLines(_rect(rec), _float(roundness), _int(segments), _float(line_thick), _color(color))


def draw_triangle(v1, v2, v3, color):
    # type: (Vector2, Vector2, Vector2, Color) -> None
    """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
    _DrawTriangle(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


def draw_triangle_lines(v1, v2, v3, color):
    # type: (Vector2, Vector2, Vector2, Color) -> None
    """Draw triangle outline (vertex in counter-clockwise order!)"""
    _DrawTriangleLines(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


def draw_triangle_fan(points, point_count, color):
    # type: (Vector2Ptr | Array[Vector2], int, Color) -> None
    """Draw a triangle fan defined by points (first vertex is the center)"""
    _DrawTriangleFan(points, _int(point_count), _color(color))


def draw_triangle_strip(points, point_count, color):
    # type: (Vector2Ptr | Array[Vector2], int, Color) -> None
    """Draw a triangle strip defined by points"""
    point_count = len(points) if point_count <= 0 else point_count
    _DrawTriangleStrip(points, _int(point_count), _color(color))


def draw_poly(center, sides, radius, rotation, color):
    # type: (Vector2, int, float, float, Color) -> None
    """Draw a regular polygon (Vector version)"""
    _DrawPoly(_vec2(center), _int(sides), _float(radius), _float(rotation), _color(color))


def draw_poly_lines(center, sides, radius, rotation, color):
    # type: (Vector2, int, float, float, Color) -> None
    """Draw a polygon outline of n sides"""
    _DrawPolyLines(_vec2(center), _int(sides), _float(radius), _float(rotation), _color(color))


def draw_poly_lines_ex(center, sides, radius, rotation, line_thick, color):
    # type: (Vector2, int, float, float, float, Color) -> None
    """Draw a polygon outline of n sides with extended parameters"""
    _DrawPolyLinesEx(_vec2(center), _int(sides), _float(radius), _float(rotation), _float(line_thick), _color(color))


def draw_spline_linear(points, point_count, thick, color):
    # type: (Vector2Ptr | Array[Vector2], int, float, Color) -> None
    """Draw spline: Linear, minimum 2 points"""
    _DrawSplineLinear(points, _int(point_count), _float(thick), _color(color))


def draw_spline_basis(points, point_count, thick, color):
    # type: (Vector2Ptr | Array[Vector2], int, float, Color) -> None
    """Draw spline: B-Spline, minimum 4 points"""
    _DrawSplineBasis(points, _int(point_count), _float(thick), _color(color))


def draw_spline_catmull_rom(points, point_count, thick, color):
    # type: (Vector2Ptr | Array[Vector2], int, float, Color) -> None
    """Draw spline: Catmull-Rom, minimum 4 points"""
    _DrawSplineCatmullRom(points, _int(point_count), _float(thick), _color(color))


def draw_spline_bezier_quadratic(points, point_count, thick, color):
    # type: (Vector2Ptr | Array[Vector2], int, float, Color) -> None
    """Draw spline: Quadratic Bezier, minimum 3 points (1 control point): [p1, c2, p3, c4...]"""
    _DrawSplineBezierQuadratic(points, _int(point_count), _float(thick), _color(color))


def draw_spline_bezier_cubic(points, point_count, thick, color):
    # type: (Vector2Ptr | Array[Vector2], int, float, Color) -> None
    """Draw spline: Cubic Bezier, minimum 4 points (2 control points): [p1, c2, c3, p4, c5, c6...]"""
    _DrawSplineBezierCubic(points, _int(point_count), _float(thick), _color(color))


def draw_spline_segment_linear(p1, p2, thick, color):
    # type: (Vector2, Vector2, float, Color) -> None
    """Draw spline segment: Linear, 2 points"""
    _DrawSplineSegmentLinear(_vec2(p1), _vec2(p2), _float(thick), _color(color))


def draw_spline_segment_basis(p1, p2, p3, p4, thick, color):
    # type: (Vector2, Vector2, Vector2, Vector2, float, Color) -> None
    """Draw spline segment: B-Spline, 4 points"""
    _DrawSplineSegmentBasis(_vec2(p1), _vec2(p2), _vec2(p3), _vec2(p4), _float(thick), _color(color))


def draw_spline_segment_catmull_rom(p1, p2, p3, p4, thick, color):
    # type: (Vector2, Vector2, Vector2, Vector2, float, Color) -> None
    """Draw spline segment: Catmull-Rom, 4 points"""
    _DrawSplineSegmentCatmullRom(_vec2(p1), _vec2(p2), _vec2(p3), _vec2(p4), _float(thick), _color(color))


def draw_spline_segment_bezier_quadratic(p1, c2, p3, thick, color):
    # type: (Vector2, Vector2, Vector2, float, Color) -> None
    """Draw spline segment: Quadratic Bezier, 2 points, 1 control point"""
    _DrawSplineSegmentBezierQuadratic(_vec2(p1), _vec2(c2), _vec2(p3), _float(thick), _color(color))


def draw_spline_segment_bezier_cubic(p1, c2, c3, p4, thick, color):
    # type: (Vector2, Vector2, Vector2, Vector2, float, Color) -> None
    """Draw spline segment: Cubic Bezier, 2 points, 2 control points"""
    _DrawSplineSegmentBezierCubic(_vec2(p1), _vec2(c2), _vec2(c3), _vec2(p4), _float(thick), _color(color))


def get_spline_point_linear(start_pos, end_pos, t):
    # type: (Vector2, Vector2, float) -> Vector2
    """Get (evaluate) spline point: Linear"""
    return _GetSplinePointLinear(_vec2(start_pos), _vec2(end_pos), _float(t))


def get_spline_point_basis(p1, p2, p3, p4, t):
    # type: (Vector2, Vector2, Vector2, Vector2, float) -> Vector2
    """Get (evaluate) spline point: B-Spline"""
    return _GetSplinePointBasis(_vec2(p1), _vec2(p2), _vec2(p3), _vec2(p4), _float(t))


def get_spline_point_catmull_rom(p1, p2, p3, p4, t):
    # type: (Vector2, Vector2, Vector2, Vector2, float) -> Vector2
    """Get (evaluate) spline point: Catmull-Rom"""
    return _GetSplinePointCatmullRom(_vec2(p1), _vec2(p2), _vec2(p3), _vec2(p4), _float(t))


def get_spline_point_bezier_quad(p1, c2, p3, t):
    # type: (Vector2, Vector2, Vector2, float) -> Vector2
    """Get (evaluate) spline point: Quadratic Bezier"""
    return _GetSplinePointBezierQuad(_vec2(p1), _vec2(c2), _vec2(p3), _float(t))


def get_spline_point_bezier_cubic(p1, c2, c3, p4, t):
    # type: (Vector2, Vector2, Vector2, Vector2, float) -> Vector2
    """Get (evaluate) spline point: Cubic Bezier"""
    return _GetSplinePointBezierCubic(_vec2(p1), _vec2(c2), _vec2(c3), _vec2(p4), _float(t))


def check_collision_recs(rec1, rec2):
    # type: (Rectangle, Rectangle) -> bool
    """Check collision between two rectangles"""
    return _CheckCollisionRecs(_rect(rec1), _rect(rec2))


def check_collision_circles(center1, radius1, center2, radius2):
    # type: (Vector2, float, Vector2, float) -> bool
    """Check collision between two circles"""
    return _CheckCollisionCircles(_vec2(center1), _float(radius1), _vec2(center2), _float(radius2))


def check_collision_circle_rec(center, radius, rec):
    # type: (Vector2, float, Rectangle) -> bool
    """Check collision between circle and rectangle"""
    return _CheckCollisionCircleRec(_vec2(center), _float(radius), _rect(rec))


def check_collision_point_rec(point, rec):
    # type: (Vector2, Rectangle) -> bool
    """Check if point is inside rectangle"""
    return _CheckCollisionPointRec(_vec2(point), _rect(rec))


def check_collision_point_circle(point, center, radius):
    # type: (Vector2, Vector2, float) -> bool
    """Check if point is inside circle"""
    return _CheckCollisionPointCircle(_vec2(point), _vec2(center), _float(radius))


def check_collision_point_triangle(point, p1, p2, p3):
    # type: (Vector2, Vector2, Vector2, Vector2) -> bool
    """Check if point is inside a triangle"""
    return _CheckCollisionPointTriangle(_vec2(point), _vec2(p1), _vec2(p2), _vec2(p3))


def check_collision_point_poly(point, points, point_count):
    # type: (Vector2, Vector2Ptr, int) -> bool
    """Check if point is within a polygon described by array of vertices"""
    return _CheckCollisionPointPoly(_vec2(point), points, _int(point_count))


def check_collision_lines(start_pos1, end_pos1, start_pos2, end_pos2, collision_point):
    # type: (Vector2, Vector2, Vector2, Vector2, Vector2Ptr) -> bool
    """Check the collision between two lines defined by two points each, returns collision point by reference"""
    return _CheckCollisionLines(_vec2(start_pos1), _vec2(end_pos1), _vec2(start_pos2), _vec2(end_pos2), collision_point)


def check_collision_point_line(point, p1, p2, threshold):
    # type: (Vector2, Vector2, Vector2, int) -> bool
    """Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]"""
    return _CheckCollisionPointLine(_vec2(point), _vec2(p1), _vec2(p2), _int(threshold))


def get_collision_rec(rec1, rec2):
    # type: (Rectangle, Rectangle) -> Rectangle
    """Get collision rectangle for two rectangles collision"""
    return _GetCollisionRec(_rect(rec1), _rect(rec2))


def load_image(file_name):
    # type: (bytes | str | None) -> Image
    """Load image from file into CPU memory (RAM)"""
    return _LoadImage(_str_in(file_name))


def load_image_raw(file_name, width, height, format_, header_size):
    # type: (bytes | str | None, int, int, int, int) -> Image
    """Load image from RAW file data"""
    return _LoadImageRaw(_str_in(file_name), _int(width), _int(height), _int(format_), _int(header_size))


def load_image_svg(file_name_or_string, width, height):
    # type: (bytes | str | None, int, int) -> Image
    """Load image from SVG file data or string with specified size"""
    return _LoadImageSvg(_str_in(file_name_or_string), _int(width), _int(height))


def load_image_anim(file_name, frames):
    # type: (bytes | str | None, IntPtr) -> Image
    """Load image sequence from file (frames appended to image.data)"""
    return _LoadImageAnim(_str_in(file_name), frames)


def load_image_from_memory(file_type, file_data, data_size):
    # type: (bytes | str | None, int, int) -> Image
    """Load image from memory buffer, fileType refers to extension: i.e. '.png'"""
    return _LoadImageFromMemory(_str_in(file_type), _int(file_data, (0, 255)), _int(data_size))


def load_image_from_texture(texture):
    # type: (Texture2D) -> Image
    """Load image from GPU texture data"""
    return _LoadImageFromTexture(texture)


def load_image_from_screen():
    # type: () -> Image
    """Load image from screen buffer and (screenshot)"""
    return _LoadImageFromScreen()


def is_image_ready(image):
    # type: (Image) -> bool
    """Check if an image is ready"""
    return _IsImageReady(image)


def unload_image(image):
    # type: (Image) -> None
    """Unload image from CPU memory (RAM)"""
    _UnloadImage(image)


def export_image(image, file_name):
    # type: (Image, bytes | str | None) -> bool
    """Export image data to file, returns true on success"""
    return _ExportImage(image, _str_in(file_name))


def export_image_to_memory(image, file_type, file_size):
    # type: (Image, bytes | str | None, IntPtr) -> int
    """Export image to memory buffer"""
    return _ExportImageToMemory(image, _str_in(file_type), file_size)


def export_image_as_code(image, file_name):
    # type: (Image, bytes | str | None) -> bool
    """Export image as code file defining an array of bytes, returns true on success"""
    return _ExportImageAsCode(image, _str_in(file_name))


def gen_image_color(width, height, color):
    # type: (int, int, Color) -> Image
    """Generate image: plain color"""
    return _GenImageColor(_int(width), _int(height), _color(color))


def gen_image_gradient_linear(width, height, direction, start, end):
    # type: (int, int, int, Color, Color) -> Image
    """Generate image: linear gradient, direction in degrees [0..360], 0=Vertical gradient"""
    return _GenImageGradientLinear(_int(width), _int(height), _int(direction), _color(start), _color(end))


def gen_image_gradient_radial(width, height, density, inner, outer):
    # type: (int, int, float, Color, Color) -> Image
    """Generate image: radial gradient"""
    return _GenImageGradientRadial(_int(width), _int(height), _float(density), _color(inner), _color(outer))


def gen_image_gradient_square(width, height, density, inner, outer):
    # type: (int, int, float, Color, Color) -> Image
    """Generate image: square gradient"""
    return _GenImageGradientSquare(_int(width), _int(height), _float(density), _color(inner), _color(outer))


def gen_image_checked(width, height, checks_x, checks_y, col1, col2):
    # type: (int, int, int, int, Color, Color) -> Image
    """Generate image: checked"""
    return _GenImageChecked(_int(width), _int(height), _int(checks_x), _int(checks_y), _color(col1), _color(col2))


def gen_image_white_noise(width, height, factor):
    # type: (int, int, float) -> Image
    """Generate image: white noise"""
    return _GenImageWhiteNoise(_int(width), _int(height), _float(factor))


def gen_image_perlin_noise(width, height, offset_x, offset_y, scale):
    # type: (int, int, int, int, float) -> Image
    """Generate image: perlin noise"""
    return _GenImagePerlinNoise(_int(width), _int(height), _int(offset_x), _int(offset_y), _float(scale))


def gen_image_cellular(width, height, tile_size):
    # type: (int, int, int) -> Image
    """Generate image: cellular algorithm, bigger tileSize means bigger cells"""
    return _GenImageCellular(_int(width), _int(height), _int(tile_size))


def gen_image_text(width, height, text):
    # type: (int, int, bytes | str | None) -> Image
    """Generate image: grayscale image from text data"""
    return _GenImageText(_int(width), _int(height), _str_in(text))


def image_copy(image):
    # type: (Image) -> Image
    """Create an image duplicate (useful for transformations)"""
    return _ImageCopy(image)


def image_from_image(image, rec):
    # type: (Image, Rectangle) -> Image
    """Create an image from another image piece"""
    return _ImageFromImage(image, _rect(rec))


def image_text(text, font_size, color):
    # type: (bytes | str | None, int, Color) -> Image
    """Create an image from text (default font)"""
    return _ImageText(_str_in(text), _int(font_size), _color(color))


def image_text_ex(font, text, font_size, spacing, tint):
    # type: (Font, bytes | str | None, float, float, Color) -> Image
    """Create an image from text (custom sprite font)"""
    return _ImageTextEx(font, _str_in(text), _float(font_size), _float(spacing), _color(tint))


def image_format(image, new_format):
    # type: (ImagePtr, int) -> None
    """Convert image data to desired format"""
    _ImageFormat(image, _int(new_format))


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
    _ImageAlphaCrop(image, _float(threshold))


def image_alpha_clear(image, color, threshold):
    # type: (ImagePtr, Color, float) -> None
    """Clear alpha channel to desired color"""
    _ImageAlphaClear(image, _color(color), _float(threshold))


def image_alpha_mask(image, alpha_mask):
    # type: (ImagePtr, Image) -> None
    """Apply alpha mask to image"""
    _ImageAlphaMask(image, alpha_mask)


def image_alpha_premultiply(image):
    # type: (ImagePtr) -> None
    """Premultiply alpha channel"""
    _ImageAlphaPremultiply(image)


def image_blur_gaussian(image, blur_size):
    # type: (ImagePtr, int) -> None
    """Apply Gaussian blur using a box blur approximation"""
    _ImageBlurGaussian(image, _int(blur_size))


def image_resize(image, new_width, new_height):
    # type: (ImagePtr, int, int) -> None
    """Resize image (Bicubic scaling algorithm)"""
    _ImageResize(image, _int(new_width), _int(new_height))


def image_resize_nn(image, new_width, new_height):
    # type: (ImagePtr, int, int) -> None
    """Resize image (Nearest-Neighbor scaling algorithm)"""
    _ImageResizeNN(image, _int(new_width), _int(new_height))


def image_resize_canvas(image, new_width, new_height, offset_x, offset_y, fill):
    # type: (ImagePtr, int, int, int, int, Color) -> None
    """Resize canvas and fill with color"""
    _ImageResizeCanvas(image, _int(new_width), _int(new_height), _int(offset_x), _int(offset_y), _color(fill))


def image_mipmaps(image):
    # type: (ImagePtr) -> None
    """Compute all mipmap levels for a provided image"""
    _ImageMipmaps(image)


def image_dither(image, r_bpp, g_bpp, b_bpp, a_bpp):
    # type: (ImagePtr, int, int, int, int) -> None
    """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
    _ImageDither(image, _int(r_bpp), _int(g_bpp), _int(b_bpp), _int(a_bpp))


def image_flip_vertical(image):
    # type: (ImagePtr) -> None
    """Flip image vertically"""
    _ImageFlipVertical(image)


def image_flip_horizontal(image):
    # type: (ImagePtr) -> None
    """Flip image horizontally"""
    _ImageFlipHorizontal(image)


def image_rotate(image, degrees):
    # type: (ImagePtr, int) -> None
    """Rotate image by input angle in degrees (-359 to 359)"""
    _ImageRotate(image, _int(degrees))


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
    _ImageColorContrast(image, _float(contrast))


def image_color_brightness(image, brightness):
    # type: (ImagePtr, int) -> None
    """Modify image color: brightness (-255 to 255)"""
    _ImageColorBrightness(image, _int(brightness))


def image_color_replace(image, color, replace):
    # type: (ImagePtr, Color, Color) -> None
    """Modify image color: replace color"""
    _ImageColorReplace(image, _color(color), _color(replace))


def load_image_colors(image):
    # type: (Image) -> ColorPtr
    """Load color data from image as a Color array (RGBA - 32bit)"""
    return _LoadImageColors(image)


def load_image_palette(image, max_palette_size, color_count):
    # type: (Image, int, int) -> Array[Color]
    """Load colors palette from image as a Color array (RGBA - 32bit)"""
    color_count = Int(color_count)
    result = _LoadImagePalette(image, _int(max_palette_size), byref(color_count))
    result = cast(result, POINTER(Color * color_count.value))[0]
    _clear_in_out()
    _push_in_out(color_count.value)
    return result


def unload_image_colors(colors):
    # type: (ColorPtr) -> None
    """Unload color data loaded with LoadImageColors()"""
    _UnloadImageColors(colors)


def unload_image_palette(colors):
    # type: (ColorPtr) -> None
    """Unload colors palette loaded with LoadImagePalette()"""
    _UnloadImagePalette(colors)


def get_image_alpha_border(image, threshold):
    # type: (Image, float) -> Rectangle
    """Get image alpha border rectangle"""
    return _GetImageAlphaBorder(image, _float(threshold))


def get_image_color(image, x, y):
    # type: (Image, int, int) -> Color
    """Get image pixel color at (x, y) position"""
    return _GetImageColor(image, _int(x), _int(y))


def image_clear_background(dst, color):
    # type: (ImagePtr, Color) -> None
    """Clear image background with given color"""
    _ImageClearBackground(dst, _color(color))


def image_draw_pixel(dst, pos_x, pos_y, color):
    # type: (ImagePtr, int, int, Color) -> None
    """Draw pixel within an image"""
    _ImageDrawPixel(dst, _int(pos_x), _int(pos_y), _color(color))


def image_draw_pixel_v(dst, position, color):
    # type: (ImagePtr, Vector2, Color) -> None
    """Draw pixel within an image (Vector version)"""
    _ImageDrawPixelV(dst, _vec2(position), _color(color))


def image_draw_line(dst, start_pos_x, start_pos_y, end_pos_x, end_pos_y, color):
    # type: (ImagePtr, int, int, int, int, Color) -> None
    """Draw line within an image"""
    _ImageDrawLine(dst, _int(start_pos_x), _int(start_pos_y), _int(end_pos_x), _int(end_pos_y), _color(color))


def image_draw_line_v(dst, start, end, color):
    # type: (ImagePtr, Vector2, Vector2, Color) -> None
    """Draw line within an image (Vector version)"""
    _ImageDrawLineV(dst, _vec2(start), _vec2(end), _color(color))


def image_draw_circle(dst, center_x, center_y, radius, color):
    # type: (ImagePtr, int, int, int, Color) -> None
    """Draw a filled circle within an image"""
    _ImageDrawCircle(dst, _int(center_x), _int(center_y), _int(radius), _color(color))


def image_draw_circle_v(dst, center, radius, color):
    # type: (ImagePtr, Vector2, int, Color) -> None
    """Draw a filled circle within an image (Vector version)"""
    _ImageDrawCircleV(dst, _vec2(center), _int(radius), _color(color))


def image_draw_circle_lines(dst, center_x, center_y, radius, color):
    # type: (ImagePtr, int, int, int, Color) -> None
    """Draw circle outline within an image"""
    _ImageDrawCircleLines(dst, _int(center_x), _int(center_y), _int(radius), _color(color))


def image_draw_circle_lines_v(dst, center, radius, color):
    # type: (ImagePtr, Vector2, int, Color) -> None
    """Draw circle outline within an image (Vector version)"""
    _ImageDrawCircleLinesV(dst, _vec2(center), _int(radius), _color(color))


def image_draw_rectangle(dst, pos_x, pos_y, width, height, color):
    # type: (ImagePtr, int, int, int, int, Color) -> None
    """Draw rectangle within an image"""
    _ImageDrawRectangle(dst, _int(pos_x), _int(pos_y), _int(width), _int(height), _color(color))


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
    _ImageDrawRectangleLines(dst, _rect(rec), _int(thick), _color(color))


def image_draw(dst, src, src_rec, dst_rec, tint):
    # type: (ImagePtr, Image, Rectangle, Rectangle, Color) -> None
    """Draw a source image within a destination image (tint applied to source)"""
    _ImageDraw(dst, src, _rect(src_rec), _rect(dst_rec), _color(tint))


def image_draw_text(dst, text, pos_x, pos_y, font_size, color):
    # type: (ImagePtr, bytes | str | None, int, int, int, Color) -> None
    """Draw text (using default font) within an image (destination)"""
    _ImageDrawText(dst, _str_in(text), _int(pos_x), _int(pos_y), _int(font_size), _color(color))


def image_draw_text_ex(dst, font, text, position, font_size, spacing, tint):
    # type: (ImagePtr, Font, bytes | str | None, Vector2, float, float, Color) -> None
    """Draw text (custom sprite font) within an image (destination)"""
    _ImageDrawTextEx(dst, font, _str_in(text), _vec2(position), _float(font_size), _float(spacing), _color(tint))


def load_texture(file_name):
    # type: (bytes | str | None) -> Texture2D
    """Load texture from file into GPU memory (VRAM)"""
    return _LoadTexture(_str_in(file_name))


def load_texture_from_image(image):
    # type: (Image) -> Texture2D
    """Load texture from image data"""
    return _LoadTextureFromImage(image)


def load_texture_cubemap(image, layout):
    # type: (Image, int) -> TextureCubemap
    """Load cubemap from image, multiple image cubemap layouts supported"""
    return _LoadTextureCubemap(image, _int(layout))


def load_render_texture(width, height):
    # type: (int, int) -> RenderTexture2D
    """Load texture for rendering (framebuffer)"""
    return _LoadRenderTexture(_int(width), _int(height))


def is_texture_ready(texture):
    # type: (Texture2D) -> bool
    """Check if a texture is ready"""
    return _IsTextureReady(texture)


def unload_texture(texture):
    # type: (Texture2D) -> None
    """Unload texture from GPU memory (VRAM)"""
    _UnloadTexture(texture)


def is_render_texture_ready(target):
    # type: (RenderTexture2D) -> bool
    """Check if a render texture is ready"""
    return _IsRenderTextureReady(target)


def unload_render_texture(target):
    # type: (RenderTexture2D) -> None
    """Unload render texture from GPU memory (VRAM)"""
    _UnloadRenderTexture(target)


def update_texture(texture, pixels):
    # type: (Texture2D, bytes | str | None) -> None
    """Update GPU texture with new data"""
    _UpdateTexture(texture, pixels)


def update_texture_rec(texture, rec, pixels):
    # type: (Texture2D, Rectangle, bytes | str | None) -> None
    """Update GPU texture rectangle with new data"""
    _UpdateTextureRec(texture, _rect(rec), pixels)


def gen_texture_mipmaps(texture):
    # type: (Texture2DPtr) -> None
    """Generate GPU mipmaps for a texture"""
    _GenTextureMipmaps(texture)


def set_texture_filter(texture, filter_):
    # type: (Texture2D, int) -> None
    """Set texture scaling filter mode"""
    _SetTextureFilter(texture, _int(filter_))


def set_texture_wrap(texture, wrap):
    # type: (Texture2D, int) -> None
    """Set texture wrapping mode"""
    _SetTextureWrap(texture, _int(wrap))


def draw_texture(texture, pos_x, pos_y, tint):
    # type: (Texture2D, int, int, Color) -> None
    """Draw a Texture2D"""
    _DrawTexture(texture, _int(pos_x), _int(pos_y), _color(tint))


def draw_texture_v(texture, position, tint):
    # type: (Texture2D, Vector2, Color) -> None
    """Draw a Texture2D with position defined as Vector2"""
    _DrawTextureV(texture, _vec2(position), _color(tint))


def draw_texture_ex(texture, position, rotation, scale, tint):
    # type: (Texture2D, Vector2, float, float, Color) -> None
    """Draw a Texture2D with extended parameters"""
    _DrawTextureEx(texture, _vec2(position), _float(rotation), _float(scale), _color(tint))


def draw_texture_rec(texture, source, position, tint):
    # type: (Texture2D, Rectangle, Vector2, Color) -> None
    """Draw a part of a texture defined by a rectangle"""
    _DrawTextureRec(texture, _rect(source), _vec2(position), _color(tint))


def draw_texture_pro(texture, source, dest, origin, rotation, tint):
    # type: (Texture2D, Rectangle, Rectangle, Vector2, float, Color) -> None
    """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
    _DrawTexturePro(texture, _rect(source), _rect(dest), _vec2(origin), _float(rotation), _color(tint))


def draw_texture_npatch(texture, n_patch_info, dest, origin, rotation, tint):
    # type: (Texture2D, NPatchInfo, Rectangle, Vector2, float, Color) -> None
    """Draws a texture (or part of it) that stretches or shrinks nicely"""
    _DrawTextureNPatch(texture, n_patch_info, _rect(dest), _vec2(origin), _float(rotation), _color(tint))


def fade(color, alpha):
    # type: (Color, float) -> Color
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
    return _Fade(_color(color), _float(alpha))


def color_to_int(color):
    # type: (Color) -> int
    """Get hexadecimal value for a Color"""
    return _ColorToInt(_color(color))


def color_normalize(color):
    # type: (Color) -> Vector4
    """Get Color normalized as float [0..1]"""
    return _ColorNormalize(_color(color))


def color_from_normalized(normalized):
    # type: (Vector4) -> Color
    """Get Color from normalized values [0..1]"""
    return _ColorFromNormalized(_vec4(normalized))


def color_to_hsv(color):
    # type: (Color) -> Vector3
    """Get HSV values for a Color, hue [0..360], saturation/value [0..1]"""
    return _ColorToHSV(_color(color))


def color_from_hsv(hue, saturation, value):
    # type: (float, float, float) -> Color
    """Get a Color from HSV values, hue [0..360], saturation/value [0..1]"""
    return _ColorFromHSV(_float(hue), _float(saturation), _float(value))


def color_tint(color, tint):
    # type: (Color, Color) -> Color
    """Get color multiplied with another color"""
    return _ColorTint(_color(color), _color(tint))


def color_brightness(color, factor):
    # type: (Color, float) -> Color
    """Get color with brightness correction, brightness factor goes from -1.0f to 1.0f"""
    return _ColorBrightness(_color(color), _float(factor))


def color_contrast(color, contrast):
    # type: (Color, float) -> Color
    """Get color with contrast correction, contrast values between -1.0f and 1.0f"""
    return _ColorContrast(_color(color), _float(contrast))


def color_alpha(color, alpha):
    # type: (Color, float) -> Color
    """Get color with alpha applied, alpha goes from 0.0f to 1.0f"""
    return _ColorAlpha(_color(color), _float(alpha))


def color_alpha_blend(dst, src, tint):
    # type: (Color, Color, Color) -> Color
    """Get src alpha-blended into dst color with tint"""
    return _ColorAlphaBlend(_color(dst), _color(src), _color(tint))


def get_color(hex_value):
    # type: (int) -> Color
    """Get Color structure from hexadecimal value"""
    return _GetColor(_int(hex_value))


def get_pixel_color(src_ptr, format_):
    # type: (bytes | str | None, int) -> Color
    """Get Color from a source pixel pointer of certain format"""
    return _GetPixelColor(src_ptr, _int(format_))


def set_pixel_color(dst_ptr, color, format_):
    # type: (bytes | str | None, Color, int) -> None
    """Set color formatted into destination pixel pointer"""
    _SetPixelColor(dst_ptr, _color(color), _int(format_))


def get_pixel_data_size(width, height, format_):
    # type: (int, int, int) -> int
    """Get pixel data size in bytes for certain format"""
    return _GetPixelDataSize(_int(width), _int(height), _int(format_))


def get_font_default():
    # type: () -> Font
    """Get the default Font"""
    return _GetFontDefault()


def load_font(file_name):
    # type: (bytes | str | None) -> Font
    """Load font from file into GPU memory (VRAM)"""
    return _LoadFont(_str_in(file_name))


def load_font_ex(file_name, font_size, codepoints, codepoint_count):
    # type: (bytes | str | None, int, list[int] | str, int) -> Font
    """Load font from file with extended parameters, use NULL for codepoints and 0 for codepointCount to load the default character setFont"""
    codepoints = int_array(codepoints)
    result = _LoadFontEx(_str_in(file_name), _int(font_size), byref(codepoints), _int(codepoint_count))
    result = result.contents[:codepoints]
    return result


def load_font_from_image(image, key, first_char):
    # type: (Image, Color, int) -> Font
    """Load font from Image (XNA style)"""
    return _LoadFontFromImage(image, _color(key), _int(first_char))


def load_font_from_memory(file_type, file_data, data_size, font_size, codepoints, codepoint_count):
    # type: (bytes | str | None, int, int, int, list[int] | str, int) -> Font
    """Load font from memory buffer, fileType refers to extension: i.e. '.ttf'"""
    codepoints = int_array(codepoints)
    return _LoadFontFromMemory(_str_in(file_type), _int(file_data, (0, 255)), _int(data_size), _int(font_size), codepoints, _int(codepoint_count))


def is_font_ready(font):
    # type: (Font) -> bool
    """Check if a font is ready"""
    return _IsFontReady(font)


def load_font_data(file_data, data_size, font_size, codepoints, codepoint_count, type_):
    # type: (int, int, int, list[int] | str, int, int) -> Array[GlyphInfo]
    """Load font data for further use"""
    codepoints = int_array(codepoints)
    result = _LoadFontData(_int(file_data, (0, 255)), _int(data_size), _int(font_size), byref(codepoints), _int(codepoint_count), _int(type_))
    result = cast(result, POINTER(GlyphInfo * codepoints.value))[0]
    _clear_in_out()
    _push_in_out(codepoints.value)
    return result


def gen_image_font_atlas(glyphs, glyph_recs, glyph_count, font_size, padding, pack_method):
    # type: (GlyphInfoPtr, RectanglePtrPtr, int, int, int, int) -> Image
    """Generate image font atlas using chars info"""
    return _GenImageFontAtlas(glyphs, glyph_recs, _int(glyph_count), _int(font_size), _int(padding), _int(pack_method))


def unload_font_data(glyphs, glyph_count):
    # type: (GlyphInfoPtr, int) -> None
    """Unload font chars info data (RAM)"""
    _UnloadFontData(glyphs, _int(glyph_count))


def unload_font(font):
    # type: (Font) -> None
    """Unload font from GPU memory (VRAM)"""
    _UnloadFont(font)


def export_font_as_code(font, file_name):
    # type: (Font, bytes | str | None) -> bool
    """Export font as code file, returns true on success"""
    return _ExportFontAsCode(font, _str_in(file_name))


def draw_fps(pos_x, pos_y):
    # type: (int, int) -> None
    """Draw current FPS"""
    _DrawFPS(_int(pos_x), _int(pos_y))


def draw_text(text, pos_x, pos_y, font_size, color):
    # type: (bytes | str | None, int, int, int, Color) -> None
    """Draw text (using default font)"""
    _DrawText(_str_in(text), _int(pos_x), _int(pos_y), _int(font_size), _color(color))


def draw_text_ex(font, text, position, font_size, spacing, tint):
    # type: (Font, bytes | str | None, Vector2, float, float, Color) -> None
    """Draw text using font and additional parameters"""
    _DrawTextEx(font, _str_in(text), _vec2(position), _float(font_size), _float(spacing), _color(tint))


def draw_text_pro(font, text, position, origin, rotation, font_size, spacing, tint):
    # type: (Font, bytes | str | None, Vector2, Vector2, float, float, float, Color) -> None
    """Draw text using Font and pro parameters (rotation)"""
    _DrawTextPro(font, _str_in(text), _vec2(position), _vec2(origin), _float(rotation), _float(font_size), _float(spacing), _color(tint))


def draw_text_codepoint(font, codepoint, position, font_size, tint):
    # type: (Font, int, Vector2, float, Color) -> None
    """Draw one character (codepoint)"""
    _DrawTextCodepoint(font, _int(codepoint), _vec2(position), _float(font_size), _color(tint))


def draw_text_codepoints(font, codepoints, codepoint_count, position, font_size, spacing, tint):
    # type: (Font, IntPtr, int, Vector2, float, float, Color) -> None
    """Draw multiple character (codepoint)"""
    _DrawTextCodepoints(font, codepoints, _int(codepoint_count), _vec2(position), _float(font_size), _float(spacing), _color(tint))


def set_text_line_spacing(spacing):
    # type: (int) -> None
    """Set vertical line spacing when drawing with line-breaks"""
    _SetTextLineSpacing(_int(spacing))


def measure_text(text, font_size):
    # type: (bytes | str | None, int) -> int
    """Measure string width for default font"""
    return _MeasureText(_str_in(text), _int(font_size))


def measure_text_ex(font, text, font_size, spacing):
    # type: (Font, bytes | str | None, float, float) -> Vector2
    """Measure string size for Font"""
    return _MeasureTextEx(font, _str_in(text), _float(font_size), _float(spacing))


def get_glyph_index(font, codepoint):
    # type: (Font, int) -> int
    """Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found"""
    return _GetGlyphIndex(font, _int(codepoint))


def get_glyph_info(font, codepoint):
    # type: (Font, int) -> GlyphInfo
    """Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found"""
    return _GetGlyphInfo(font, _int(codepoint))


def get_glyph_atlas_rec(font, codepoint):
    # type: (Font, int) -> Rectangle
    """Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found"""
    return _GetGlyphAtlasRec(font, _int(codepoint))


def load_utf8(codepoints, length):
    # type: (IntPtr, int) -> bytes | str | None
    """Load UTF-8 text encoded from codepoints array"""
    return _LoadUTF8(codepoints, _int(length))


def unload_utf8(text):
    # type: (bytes | str | None) -> None
    """Unload UTF-8 text encoded from codepoints array"""
    _UnloadUTF8(_str_in(text))


def load_codepoints(text, count):
    # type: (bytes | str | None, IntPtr) -> IntPtr
    """Load all codepoints from a UTF-8 text string, codepoints count returned by parameter"""
    return _LoadCodepoints(_str_in(text), count)


def unload_codepoints(codepoints):
    # type: (IntPtr) -> None
    """Unload codepoints data from memory"""
    _UnloadCodepoints(codepoints)


def get_codepoint_count(text):
    # type: (bytes | str | None) -> int
    """Get total number of codepoints in a UTF-8 encoded string"""
    return _GetCodepointCount(_str_in(text))


def get_codepoint(text, codepoint_size):
    # type: (bytes | str | None, IntPtr) -> int
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
    return _GetCodepoint(_str_in(text), codepoint_size)


def get_codepoint_next(text, codepoint_size):
    # type: (bytes | str | None, IntPtr) -> int
    """Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
    return _GetCodepointNext(_str_in(text), codepoint_size)


def get_codepoint_previous(text, codepoint_size):
    # type: (bytes | str | None, IntPtr) -> int
    """Get previous codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure"""
    return _GetCodepointPrevious(_str_in(text), codepoint_size)


def codepoint_to_utf8(codepoint, utf8_size):
    # type: (int, IntPtr) -> bytes | str | None
    """Encode one codepoint into UTF-8 byte array (array length returned as parameter)"""
    return _CodepointToUTF8(_int(codepoint), utf8_size)


def text_copy(dst, src):
    # type: (bytes | str | None, bytes | str | None) -> int
    """Copy one string to another, returns bytes copied"""
    return _TextCopy(_str_in(dst), _str_in(src))


def text_is_equal(text1, text2):
    # type: (bytes | str | None, bytes | str | None) -> bool
    """Check if two text string are equal"""
    return _TextIsEqual(_str_in(text1), _str_in(text2))


def text_length(text):
    # type: (bytes | str | None) -> int
    """Get text length, checks for '\0' ending"""
    return _TextLength(_str_in(text))


def text_format(text, *args):
    # type: (bytes | str | None, ...) -> bytes | str | None
    """Text formatting with variables (sprintf() style)"""
    return _str_out(_TextFormat(_str_in(text), *args))


def text_subtext(text, position, length):
    # type: (bytes | str | None, int, int) -> bytes | str | None
    """Get a piece of a text string"""
    return _str_out(_TextSubtext(_str_in(text), _int(position), _int(length)))


def text_replace(text, replace, by):
    # type: (bytes | str | None, bytes | str | None, bytes | str | None) -> bytes | str | None
    """Replace text string (WARNING: memory must be freed!)"""
    return _str_out(_TextReplace(_str_in(text), _str_in(replace), _str_in(by)))


def text_insert(text, insert, position):
    # type: (bytes | str | None, bytes | str | None, int) -> bytes | str | None
    """Insert text in a position (WARNING: memory must be freed!)"""
    return _str_out(_TextInsert(_str_in(text), _str_in(insert), _int(position)))


def text_join(text_list, count, delimiter):
    # type: (CharPtrPtr | list[CharPtr | str] | None, int, bytes | str | None) -> bytes | str | None
    """Join text strings with delimiter"""
    return _str_out(_TextJoin(text_list, _int(count), _str_in(delimiter)))


def text_split(text, delimiter, count):
    # type: (bytes | str | None, int | str, IntPtr) -> CharPtrPtr | list[CharPtr | str] | None
    """Split text into multiple strings"""
    return _TextSplit(_str_in(text), _int(delimiter, (-128, 127)), count)


def text_append(text, append, position):
    # type: (bytes | str | None, bytes | str | None, IntPtr) -> None
    """Append text at specific position and move cursor!"""
    _TextAppend(_str_in(text), _str_in(append), position)


def text_find_index(text, find):
    # type: (bytes | str | None, bytes | str | None) -> int
    """Find first text occurrence within a string"""
    return _TextFindIndex(_str_in(text), _str_in(find))


def text_to_upper(text):
    # type: (bytes | str | None) -> bytes | str | None
    """Get upper case version of provided string"""
    return _str_out(_TextToUpper(_str_in(text)))


def text_to_lower(text):
    # type: (bytes | str | None) -> bytes | str | None
    """Get lower case version of provided string"""
    return _str_out(_TextToLower(_str_in(text)))


def text_to_pascal(text):
    # type: (bytes | str | None) -> bytes | str | None
    """Get Pascal case notation version of provided string"""
    return _str_out(_TextToPascal(_str_in(text)))


def text_to_integer(text):
    # type: (bytes | str | None) -> int
    """Get integer value from text (negative values not supported)"""
    return _TextToInteger(_str_in(text))


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
    _DrawCircle3D(_vec3(center), _float(radius), _vec3(rotation_axis), _float(rotation_angle), _color(color))


def draw_triangle3d(v1, v2, v3, color):
    # type: (Vector3, Vector3, Vector3, Color) -> None
    """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
    _DrawTriangle3D(_vec3(v1), _vec3(v2), _vec3(v3), _color(color))


def draw_triangle_strip3d(points, point_count, color):
    # type: (Vector3Ptr | Array[Vector3], int, Color) -> None
    """Draw a triangle strip defined by points"""
    _DrawTriangleStrip3D(points, len(points) if point_count <= 0 else point_count, _color(color))


def draw_cube(position, width, height, length, color):
    # type: (Vector3, float, float, float, Color) -> None
    """Draw cube"""
    _DrawCube(_vec3(position), _float(width), _float(height), _float(length), _color(color))


def draw_cube_v(position, size, color):
    # type: (Vector3, Vector3, Color) -> None
    """Draw cube (Vector version)"""
    _DrawCubeV(_vec3(position), _vec3(size), _color(color))


def draw_cube_wires(position, width, height, length, color):
    # type: (Vector3, float, float, float, Color) -> None
    """Draw cube wires"""
    _DrawCubeWires(_vec3(position), _float(width), _float(height), _float(length), _color(color))


def draw_cube_wires_v(position, size, color):
    # type: (Vector3, Vector3, Color) -> None
    """Draw cube wires (Vector version)"""
    _DrawCubeWiresV(_vec3(position), _vec3(size), _color(color))


def draw_sphere(center_pos, radius, color):
    # type: (Vector3, float, Color) -> None
    """Draw sphere"""
    _DrawSphere(_vec3(center_pos), _float(radius), _color(color))


def draw_sphere_ex(center_pos, radius, rings, slices, color):
    # type: (Vector3, float, int, int, Color) -> None
    """Draw sphere with extended parameters"""
    _DrawSphereEx(_vec3(center_pos), _float(radius), _int(rings), _int(slices), _color(color))


def draw_sphere_wires(center_pos, radius, rings, slices, color):
    # type: (Vector3, float, int, int, Color) -> None
    """Draw sphere wires"""
    _DrawSphereWires(_vec3(center_pos), _float(radius), _int(rings), _int(slices), _color(color))


def draw_cylinder(position, radius_top, radius_bottom, height, slices, color):
    # type: (Vector3, float, float, float, int, Color) -> None
    """Draw a cylinder/cone"""
    _DrawCylinder(_vec3(position), _float(radius_top), _float(radius_bottom), _float(height), _int(slices), _color(color))


def draw_cylinder_ex(start_pos, end_pos, start_radius, end_radius, sides, color):
    # type: (Vector3, Vector3, float, float, int, Color) -> None
    """Draw a cylinder with base at startPos and top at endPos"""
    _DrawCylinderEx(_vec3(start_pos), _vec3(end_pos), _float(start_radius), _float(end_radius), _int(sides), _color(color))


def draw_cylinder_wires(position, radius_top, radius_bottom, height, slices, color):
    # type: (Vector3, float, float, float, int, Color) -> None
    """Draw a cylinder/cone wires"""
    _DrawCylinderWires(_vec3(position), _float(radius_top), _float(radius_bottom), _float(height), _int(slices), _color(color))


def draw_cylinder_wires_ex(start_pos, end_pos, start_radius, end_radius, sides, color):
    # type: (Vector3, Vector3, float, float, int, Color) -> None
    """Draw a cylinder wires with base at startPos and top at endPos"""
    _DrawCylinderWiresEx(_vec3(start_pos), _vec3(end_pos), _float(start_radius), _float(end_radius), _int(sides), _color(color))


def draw_capsule(start_pos, end_pos, radius, slices, rings, color):
    # type: (Vector3, Vector3, float, int, int, Color) -> None
    """Draw a capsule with the center of its sphere caps at startPos and endPos"""
    _DrawCapsule(_vec3(start_pos), _vec3(end_pos), _float(radius), _int(slices), _int(rings), _color(color))


def draw_capsule_wires(start_pos, end_pos, radius, slices, rings, color):
    # type: (Vector3, Vector3, float, int, int, Color) -> None
    """Draw capsule wireframe with the center of its sphere caps at startPos and endPos"""
    _DrawCapsuleWires(_vec3(start_pos), _vec3(end_pos), _float(radius), _int(slices), _int(rings), _color(color))


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
    _DrawGrid(_int(slices), _float(spacing))


def load_model(file_name):
    # type: (bytes | str | None) -> Model
    """Load model from files (meshes and materials)"""
    return _LoadModel(_str_in(file_name))


def load_model_from_mesh(mesh):
    # type: (Mesh) -> Model
    """Load model from generated mesh (default material)"""
    return _LoadModelFromMesh(mesh)


def is_model_ready(model):
    # type: (Model) -> bool
    """Check if a model is ready"""
    return _IsModelReady(model)


def unload_model(model):
    # type: (Model) -> None
    """Unload model (including meshes) from memory (RAM and/or VRAM)"""
    _UnloadModel(model)


def get_model_bounding_box(model):
    # type: (Model) -> BoundingBox
    """Compute model bounding box limits (considers all meshes)"""
    return _GetModelBoundingBox(model)


def draw_model(model, position, scale, tint):
    # type: (Model, Vector3, float, Color) -> None
    """Draw a model (with texture if set)"""
    _DrawModel(model, _vec3(position), _float(scale), _color(tint))


def draw_model_ex(model, position, rotation_axis, rotation_angle, scale, tint):
    # type: (Model, Vector3, Vector3, float, Vector3, Color) -> None
    """Draw a model with extended parameters"""
    _DrawModelEx(model, _vec3(position), _vec3(rotation_axis), _float(rotation_angle), _vec3(scale), _color(tint))


def draw_model_wires(model, position, scale, tint):
    # type: (Model, Vector3, float, Color) -> None
    """Draw a model wires (with texture if set)"""
    _DrawModelWires(model, _vec3(position), _float(scale), _color(tint))


def draw_model_wires_ex(model, position, rotation_axis, rotation_angle, scale, tint):
    # type: (Model, Vector3, Vector3, float, Vector3, Color) -> None
    """Draw a model wires (with texture if set) with extended parameters"""
    _DrawModelWiresEx(model, _vec3(position), _vec3(rotation_axis), _float(rotation_angle), _vec3(scale), _color(tint))


def draw_bounding_box(box, color):
    # type: (BoundingBox, Color) -> None
    """Draw bounding box (wires)"""
    _DrawBoundingBox(box, _color(color))


def draw_billboard(camera, texture, position, size, tint):
    # type: (Camera, Texture2D, Vector3, float, Color) -> None
    """Draw a billboard texture"""
    _DrawBillboard(camera, texture, _vec3(position), _float(size), _color(tint))


def draw_billboard_rec(camera, texture, source, position, size, tint):
    # type: (Camera, Texture2D, Rectangle, Vector3, Vector2, Color) -> None
    """Draw a billboard texture defined by source"""
    _DrawBillboardRec(camera, texture, _rect(source), _vec3(position), _vec2(size), _color(tint))


def draw_billboard_pro(camera, texture, source, position, up, size, origin, rotation, tint):
    # type: (Camera, Texture2D, Rectangle, Vector3, Vector3, Vector2, Vector2, float, Color) -> None
    """Draw a billboard texture defined by source and rotation"""
    _DrawBillboardPro(camera, texture, _rect(source), _vec3(position), _vec3(up), _vec2(size), _vec2(origin), _float(rotation), _color(tint))


def upload_mesh(mesh, dynamic):
    # type: (MeshPtr, bool) -> None
    """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
    _UploadMesh(mesh, _bool(dynamic))


def update_mesh_buffer(mesh, index, data, data_size, offset):
    # type: (Mesh, int, bytes | str | None, int, int) -> None
    """Update mesh vertex data in GPU for a specific buffer index"""
    _UpdateMeshBuffer(mesh, _int(index), data, _int(data_size), _int(offset))


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
    _DrawMeshInstanced(mesh, material, transforms, _int(instances))


def export_mesh(mesh, file_name):
    # type: (Mesh, bytes | str | None) -> bool
    """Export mesh data to file, returns true on success"""
    return _ExportMesh(mesh, _str_in(file_name))


def get_mesh_bounding_box(mesh):
    # type: (Mesh) -> BoundingBox
    """Compute mesh bounding box limits"""
    return _GetMeshBoundingBox(mesh)


def gen_mesh_tangents(mesh):
    # type: (MeshPtr) -> None
    """Compute mesh tangents"""
    _GenMeshTangents(mesh)


def gen_mesh_poly(sides, radius):
    # type: (int, float) -> Mesh
    """Generate polygonal mesh"""
    return _GenMeshPoly(_int(sides), _float(radius))


def gen_mesh_plane(width, length, res_x, res_z):
    # type: (float, float, int, int) -> Mesh
    """Generate plane mesh (with subdivisions)"""
    return _GenMeshPlane(_float(width), _float(length), _int(res_x), _int(res_z))


def gen_mesh_cube(width, height, length):
    # type: (float, float, float) -> Mesh
    """Generate cuboid mesh"""
    return _GenMeshCube(_float(width), _float(height), _float(length))


def gen_mesh_sphere(radius, rings, slices):
    # type: (float, int, int) -> Mesh
    """Generate sphere mesh (standard sphere)"""
    return _GenMeshSphere(_float(radius), _int(rings), _int(slices))


def gen_mesh_hemi_sphere(radius, rings, slices):
    # type: (float, int, int) -> Mesh
    """Generate half-sphere mesh (no bottom cap)"""
    return _GenMeshHemiSphere(_float(radius), _int(rings), _int(slices))


def gen_mesh_cylinder(radius, height, slices):
    # type: (float, float, int) -> Mesh
    """Generate cylinder mesh"""
    return _GenMeshCylinder(_float(radius), _float(height), _int(slices))


def gen_mesh_cone(radius, height, slices):
    # type: (float, float, int) -> Mesh
    """Generate cone/pyramid mesh"""
    return _GenMeshCone(_float(radius), _float(height), _int(slices))


def gen_mesh_torus(radius, size, rad_seg, sides):
    # type: (float, float, int, int) -> Mesh
    """Generate torus mesh"""
    return _GenMeshTorus(_float(radius), _float(size), _int(rad_seg), _int(sides))


def gen_mesh_knot(radius, size, rad_seg, sides):
    # type: (float, float, int, int) -> Mesh
    """Generate trefoil knot mesh"""
    return _GenMeshKnot(_float(radius), _float(size), _int(rad_seg), _int(sides))


def gen_mesh_heightmap(heightmap, size):
    # type: (Image, Vector3) -> Mesh
    """Generate heightmap mesh from image data"""
    return _GenMeshHeightmap(heightmap, _vec3(size))


def gen_mesh_cubicmap(cubicmap, cube_size):
    # type: (Image, Vector3) -> Mesh
    """Generate cubes-based map mesh from image data"""
    return _GenMeshCubicmap(cubicmap, _vec3(cube_size))


def load_materials(file_name, material_count):
    # type: (bytes | str | None, int) -> Array[Material]
    """Load materials from model file"""
    material_count = Int(material_count)
    result = _LoadMaterials(_str_in(file_name), byref(material_count))
    result = cast(result, POINTER(Material * material_count.value))[0]
    _clear_in_out()
    _push_in_out(material_count.value)
    return result


def load_material_default():
    # type: () -> Material
    """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
    return _LoadMaterialDefault()


def is_material_ready(material):
    # type: (Material) -> bool
    """Check if a material is ready"""
    return _IsMaterialReady(material)


def unload_material(material):
    # type: (Material) -> None
    """Unload material from GPU memory (VRAM)"""
    _UnloadMaterial(material)


def set_material_texture(material, map_type, texture):
    # type: (MaterialPtr, int, Texture2D) -> None
    """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
    _SetMaterialTexture(material, _int(map_type), texture)


def set_model_mesh_material(model, mesh_id, material_id):
    # type: (ModelPtr, int, int) -> None
    """Set material for a mesh"""
    _SetModelMeshMaterial(model, _int(mesh_id), _int(material_id))


def load_model_animations(file_name, anim_count):
    # type: (bytes | str | None, int) -> Array[ModelAnimation]
    """Load model animations from file"""
    anim_count = Int(anim_count)
    result = _LoadModelAnimations(_str_in(file_name), byref(anim_count))
    result = cast(result, POINTER(ModelAnimation * anim_count.value))[0]
    _clear_in_out()
    _push_in_out(anim_count.value)
    return result


def update_model_animation(model, anim, frame):
    # type: (Model, ModelAnimation, int) -> None
    """Update model animation pose"""
    _UpdateModelAnimation(model, anim, _int(frame))


def unload_model_animation(anim):
    # type: (ModelAnimation) -> None
    """Unload animation data"""
    _UnloadModelAnimation(anim)


def unload_model_animations(animations, anim_count):
    # type: (ModelAnimationPtr, int) -> None
    """Unload animation array data"""
    _UnloadModelAnimations(animations, _int(anim_count))


def is_model_animation_valid(model, anim):
    # type: (Model, ModelAnimation) -> bool
    """Check model animation skeleton match"""
    return _IsModelAnimationValid(model, anim)


def check_collision_spheres(center1, radius1, center2, radius2):
    # type: (Vector3, float, Vector3, float) -> bool
    """Check collision between two spheres"""
    return _CheckCollisionSpheres(_vec3(center1), _float(radius1), _vec3(center2), _float(radius2))


def check_collision_boxes(box1, box2):
    # type: (BoundingBox, BoundingBox) -> bool
    """Check collision between two bounding boxes"""
    return _CheckCollisionBoxes(box1, box2)


def check_collision_box_sphere(box, center, radius):
    # type: (BoundingBox, Vector3, float) -> bool
    """Check collision between box and sphere"""
    return _CheckCollisionBoxSphere(box, _vec3(center), _float(radius))


def get_ray_collision_sphere(ray, center, radius):
    # type: (Ray, Vector3, float) -> RayCollision
    """Get collision info between ray and sphere"""
    return _GetRayCollisionSphere(ray, _vec3(center), _float(radius))


def get_ray_collision_box(ray, box):
    # type: (Ray, BoundingBox) -> RayCollision
    """Get collision info between ray and box"""
    return _GetRayCollisionBox(ray, box)


def get_ray_collision_mesh(ray, mesh, transform):
    # type: (Ray, Mesh, Matrix) -> RayCollision
    """Get collision info between ray and mesh"""
    return _GetRayCollisionMesh(ray, mesh, transform)


def get_ray_collision_triangle(ray, p1, p2, p3):
    # type: (Ray, Vector3, Vector3, Vector3) -> RayCollision
    """Get collision info between ray and triangle"""
    return _GetRayCollisionTriangle(ray, _vec3(p1), _vec3(p2), _vec3(p3))


def get_ray_collision_quad(ray, p1, p2, p3, p4):
    # type: (Ray, Vector3, Vector3, Vector3, Vector3) -> RayCollision
    """Get collision info between ray and quad"""
    return _GetRayCollisionQuad(ray, _vec3(p1), _vec3(p2), _vec3(p3), _vec3(p4))


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
    return _IsAudioDeviceReady()


def set_master_volume(volume):
    # type: (float) -> None
    """Set master volume (listener)"""
    _SetMasterVolume(_float(volume))


def get_master_volume():
    # type: () -> float
    """Get master volume (listener)"""
    return _GetMasterVolume()


def load_wave(file_name):
    # type: (bytes | str | None) -> Wave
    """Load wave data from file"""
    return _LoadWave(_str_in(file_name))


def load_wave_from_memory(file_type, file_data, data_size):
    # type: (bytes | str | None, int, int) -> Wave
    """Load wave from memory buffer, fileType refers to extension: i.e. '.wav'"""
    return _LoadWaveFromMemory(_str_in(file_type), _int(file_data, (0, 255)), _int(data_size))


def is_wave_ready(wave):
    # type: (Wave) -> bool
    """Checks if wave data is ready"""
    return _IsWaveReady(wave)


def load_sound(file_name):
    # type: (bytes | str | None) -> Sound
    """Load sound from file"""
    return _LoadSound(_str_in(file_name))


def load_sound_from_wave(wave):
    # type: (Wave) -> Sound
    """Load sound from wave data"""
    return _LoadSoundFromWave(wave)


def load_sound_alias(source):
    # type: (Sound) -> Sound
    """Create a new sound that shares the same sample data as the source sound, does not own the sound data"""
    return _LoadSoundAlias(source)


def is_sound_ready(sound):
    # type: (Sound) -> bool
    """Checks if a sound is ready"""
    return _IsSoundReady(sound)


def update_sound(sound, data, sample_count):
    # type: (Sound, bytes | str | None, int) -> None
    """Update sound buffer with new data"""
    _UpdateSound(sound, data, _int(sample_count))


def unload_wave(wave):
    # type: (Wave) -> None
    """Unload wave data"""
    _UnloadWave(wave)


def unload_sound(sound):
    # type: (Sound) -> None
    """Unload sound"""
    _UnloadSound(sound)


def unload_sound_alias(alias):
    # type: (Sound) -> None
    """Unload a sound alias (does not deallocate sample data)"""
    _UnloadSoundAlias(alias)


def export_wave(wave, file_name):
    # type: (Wave, bytes | str | None) -> bool
    """Export wave data to file, returns true on success"""
    return _ExportWave(wave, _str_in(file_name))


def export_wave_as_code(wave, file_name):
    # type: (Wave, bytes | str | None) -> bool
    """Export wave sample data to code (.h), returns true on success"""
    return _ExportWaveAsCode(wave, _str_in(file_name))


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


def is_sound_playing(sound):
    # type: (Sound) -> bool
    """Check if a sound is currently playing"""
    return _IsSoundPlaying(sound)


def set_sound_volume(sound, volume):
    # type: (Sound, float) -> None
    """Set volume for a sound (1.0 is max level)"""
    _SetSoundVolume(sound, _float(volume))


def set_sound_pitch(sound, pitch):
    # type: (Sound, float) -> None
    """Set pitch for a sound (1.0 is base level)"""
    _SetSoundPitch(sound, _float(pitch))


def set_sound_pan(sound, pan):
    # type: (Sound, float) -> None
    """Set pan for a sound (0.5 is center)"""
    _SetSoundPan(sound, _float(pan))


def wave_copy(wave):
    # type: (Wave) -> Wave
    """Copy a wave to a new wave"""
    return _WaveCopy(wave)


def wave_crop(wave, init_sample, final_sample):
    # type: (WavePtr, int, int) -> None
    """Crop a wave to defined samples range"""
    _WaveCrop(wave, _int(init_sample), _int(final_sample))


def wave_format(wave, sample_rate, sample_size, channels):
    # type: (WavePtr, int, int, int) -> None
    """Convert wave data to desired format"""
    _WaveFormat(wave, _int(sample_rate), _int(sample_size), _int(channels))


def load_wave_samples(wave):
    # type: (Wave) -> FloatPtr
    """Load samples data from wave as a 32bit float data array"""
    return _LoadWaveSamples(wave)


def unload_wave_samples(samples):
    # type: (FloatPtr) -> None
    """Unload samples data loaded with LoadWaveSamples()"""
    _UnloadWaveSamples(samples)


def load_music_stream(file_name):
    # type: (bytes | str | None) -> Music
    """Load music stream from file"""
    return _LoadMusicStream(_str_in(file_name))


def load_music_stream_from_memory(file_type, data, data_size):
    # type: (bytes | str | None, int, int) -> Music
    """Load music stream from data"""
    return _LoadMusicStreamFromMemory(_str_in(file_type), _int(data, (0, 255)), _int(data_size))


def is_music_ready(music):
    # type: (Music) -> bool
    """Checks if a music stream is ready"""
    return _IsMusicReady(music)


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
    return _IsMusicStreamPlaying(music)


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
    _SeekMusicStream(music, _float(position))


def set_music_volume(music, volume):
    # type: (Music, float) -> None
    """Set volume for music (1.0 is max level)"""
    _SetMusicVolume(music, _float(volume))


def set_music_pitch(music, pitch):
    # type: (Music, float) -> None
    """Set pitch for a music (1.0 is base level)"""
    _SetMusicPitch(music, _float(pitch))


def set_music_pan(music, pan):
    # type: (Music, float) -> None
    """Set pan for a music (0.5 is center)"""
    _SetMusicPan(music, _float(pan))


def get_music_time_length(music):
    # type: (Music) -> float
    """Get music time length (in seconds)"""
    return _GetMusicTimeLength(music)


def get_music_time_played(music):
    # type: (Music) -> float
    """Get current music time played (in seconds)"""
    return _GetMusicTimePlayed(music)


def load_audio_stream(sample_rate, sample_size, channels):
    # type: (int, int, int) -> AudioStream
    """Load audio stream (to stream raw audio pcm data)"""
    return _LoadAudioStream(_int(sample_rate), _int(sample_size), _int(channels))


def is_audio_stream_ready(stream):
    # type: (AudioStream) -> bool
    """Checks if an audio stream is ready"""
    return _IsAudioStreamReady(stream)


def unload_audio_stream(stream):
    # type: (AudioStream) -> None
    """Unload audio stream and free memory"""
    _UnloadAudioStream(stream)


def update_audio_stream(stream, data, frame_count):
    # type: (AudioStream, bytes | str | None, int) -> None
    """Update audio stream buffers with data"""
    _UpdateAudioStream(stream, data, _int(frame_count))


def is_audio_stream_processed(stream):
    # type: (AudioStream) -> bool
    """Check if any audio stream buffers requires refill"""
    return _IsAudioStreamProcessed(stream)


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
    return _IsAudioStreamPlaying(stream)


def stop_audio_stream(stream):
    # type: (AudioStream) -> None
    """Stop audio stream"""
    _StopAudioStream(stream)


def set_audio_stream_volume(stream, volume):
    # type: (AudioStream, float) -> None
    """Set volume for audio stream (1.0 is max level)"""
    _SetAudioStreamVolume(stream, _float(volume))


def set_audio_stream_pitch(stream, pitch):
    # type: (AudioStream, float) -> None
    """Set pitch for audio stream (1.0 is base level)"""
    _SetAudioStreamPitch(stream, _float(pitch))


def set_audio_stream_pan(stream, pan):
    # type: (AudioStream, float) -> None
    """Set pan for audio stream (0.5 is centered)"""
    _SetAudioStreamPan(stream, _float(pan))


def set_audio_stream_buffer_size_default(size):
    # type: (int) -> None
    """Default size for new audio streams"""
    _SetAudioStreamBufferSizeDefault(_int(size))


def set_audio_stream_callback(stream, callback):
    # type: (AudioStream, AudioCallback) -> None
    """Audio thread callback to request new data"""
    _SetAudioStreamCallback(stream, callback)


def attach_audio_stream_processor(stream, processor):
    # type: (AudioStream, AudioCallback) -> None
    """Attach audio stream processor to stream, receives the samples as <float>s"""
    _AttachAudioStreamProcessor(stream, processor)


def detach_audio_stream_processor(stream, processor):
    # type: (AudioStream, AudioCallback) -> None
    """Detach audio stream processor from stream"""
    _DetachAudioStreamProcessor(stream, processor)


def attach_audio_mixed_processor(processor):
    # type: (AudioCallback) -> None
    """Attach audio stream processor to the entire audio pipeline, receives the samples as <float>s"""
    _AttachAudioMixedProcessor(processor)


def detach_audio_mixed_processor(processor):
    # type: (AudioCallback) -> None
    """Detach audio stream processor from the entire audio pipeline"""
    _DetachAudioMixedProcessor(processor)


# rlapi::raymath
# ------------------------------------------------------------------------------

def clamp(value, min_, max_):
    # type: (float, float, float) -> float
    return _Clamp(_float(value), _float(min_), _float(max_))


def lerp(start, end, amount):
    # type: (float, float, float) -> float
    return _Lerp(_float(start), _float(end), _float(amount))


def normalize(value, start, end):
    # type: (float, float, float) -> float
    return _Normalize(_float(value), _float(start), _float(end))


def remap(value, input_start, input_end, output_start, output_end):
    # type: (float, float, float, float, float) -> float
    return _Remap(_float(value), _float(input_start), _float(input_end), _float(output_start), _float(output_end))


def wrap(value, min_, max_):
    # type: (float, float, float) -> float
    return _Wrap(_float(value), _float(min_), _float(max_))


def float_equals(x, y):
    # type: (float, float) -> int
    return _FloatEquals(_float(x), _float(y))


def vector2_zero():
    # type: () -> Vector2
    return _Vector2Zero()


def vector2_one():
    # type: () -> Vector2
    return _Vector2One()


def vector2_add(v1, v2):
    # type: (Vector2, Vector2) -> Vector2
    return _Vector2Add(v1, v2)


def vector2_add_value(v, add):
    # type: (Vector2, float) -> Vector2
    return _Vector2AddValue(v, _float(add))


def vector2_subtract(v1, v2):
    # type: (Vector2, Vector2) -> Vector2
    return _Vector2Subtract(v1, v2)


def vector2_subtract_value(v, sub):
    # type: (Vector2, float) -> Vector2
    return _Vector2SubtractValue(v, _float(sub))


def vector2_length(v):
    # type: (Vector2) -> float
    return _Vector2Length(v)


def vector2_length_sqr(v):
    # type: (Vector2) -> float
    return _Vector2LengthSqr(v)


def vector2_dot_product(v1, v2):
    # type: (Vector2, Vector2) -> float
    return _Vector2DotProduct(v1, v2)


def vector2_distance(v1, v2):
    # type: (Vector2, Vector2) -> float
    return _Vector2Distance(v1, v2)


def vector2_distance_sqr(v1, v2):
    # type: (Vector2, Vector2) -> float
    return _Vector2DistanceSqr(v1, v2)


def vector2_angle(v1, v2):
    # type: (Vector2, Vector2) -> float
    return _Vector2Angle(v1, v2)


def vector2_line_angle(start, end):
    # type: (Vector2, Vector2) -> float
    return _Vector2LineAngle(start, end)


def vector2_scale(v, scale):
    # type: (Vector2, float) -> Vector2
    return _Vector2Scale(v, _float(scale))


def vector2_multiply(v1, v2):
    # type: (Vector2, Vector2) -> Vector2
    return _Vector2Multiply(v1, v2)


def vector2_negate(v):
    # type: (Vector2) -> Vector2
    return _Vector2Negate(v)


def vector2_divide(v1, v2):
    # type: (Vector2, Vector2) -> Vector2
    return _Vector2Divide(v1, v2)


def vector2_normalize(v):
    # type: (Vector2) -> Vector2
    return _Vector2Normalize(v)


def vector2_transform(v, mat):
    # type: (Vector2, Matrix) -> Vector2
    return _Vector2Transform(v, mat)


def vector2_lerp(v1, v2, amount):
    # type: (Vector2, Vector2, float) -> Vector2
    return _Vector2Lerp(v1, v2, _float(amount))


def vector2_reflect(v, normal):
    # type: (Vector2, Vector2) -> Vector2
    return _Vector2Reflect(v, normal)


def vector2_rotate(v, angle):
    # type: (Vector2, float) -> Vector2
    return _Vector2Rotate(v, _float(angle))


def vector2_move_towards(v, target, max_distance):
    # type: (Vector2, Vector2, float) -> Vector2
    return _Vector2MoveTowards(v, target, _float(max_distance))


def vector2_invert(v):
    # type: (Vector2) -> Vector2
    return _Vector2Invert(v)


def vector2_clamp(v, min_, max_):
    # type: (Vector2, Vector2, Vector2) -> Vector2
    return _Vector2Clamp(v, min_, max_)


def vector2_clamp_value(v, min_, max_):
    # type: (Vector2, float, float) -> Vector2
    return _Vector2ClampValue(v, _float(min_), _float(max_))


def vector2_equals(p, q):
    # type: (Vector2, Vector2) -> int
    return _Vector2Equals(p, q)


def vector3_zero():
    # type: () -> Vector3
    return _Vector3Zero()


def vector3_one():
    # type: () -> Vector3
    return _Vector3One()


def vector3_add(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Add(v1, v2)


def vector3_add_value(v, add):
    # type: (Vector3, float) -> Vector3
    return _Vector3AddValue(v, _float(add))


def vector3_subtract(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Subtract(v1, v2)


def vector3_subtract_value(v, sub):
    # type: (Vector3, float) -> Vector3
    return _Vector3SubtractValue(v, _float(sub))


def vector3_scale(v, scalar):
    # type: (Vector3, float) -> Vector3
    return _Vector3Scale(v, _float(scalar))


def vector3_multiply(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Multiply(v1, v2)


def vector3_cross_product(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3CrossProduct(v1, v2)


def vector3_perpendicular(v):
    # type: (Vector3) -> Vector3
    return _Vector3Perpendicular(v)


def vector3_length(v):
    # type: (Vector3) -> float
    return _Vector3Length(v)


def vector3_length_sqr(v):
    # type: (Vector3) -> float
    return _Vector3LengthSqr(v)


def vector3_dot_product(v1, v2):
    # type: (Vector3, Vector3) -> float
    return _Vector3DotProduct(v1, v2)


def vector3_distance(v1, v2):
    # type: (Vector3, Vector3) -> float
    return _Vector3Distance(v1, v2)


def vector3_distance_sqr(v1, v2):
    # type: (Vector3, Vector3) -> float
    return _Vector3DistanceSqr(v1, v2)


def vector3_angle(v1, v2):
    # type: (Vector3, Vector3) -> float
    return _Vector3Angle(v1, v2)


def vector3_negate(v):
    # type: (Vector3) -> Vector3
    return _Vector3Negate(v)


def vector3_divide(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Divide(v1, v2)


def vector3_normalize(v):
    # type: (Vector3) -> Vector3
    return _Vector3Normalize(v)


def vector3_project(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Project(v1, v2)


def vector3_reject(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Reject(v1, v2)


def vector3_ortho_normalize(v1, v2):
    # type: (Vector3Ptr, Vector3Ptr) -> None
    _Vector3OrthoNormalize(v1, v2)


def vector3_transform(v, mat):
    # type: (Vector3, Matrix) -> Vector3
    return _Vector3Transform(v, mat)


def vector3_rotate_by_quaternion(v, q):
    # type: (Vector3, Quaternion) -> Vector3
    return _Vector3RotateByQuaternion(v, q)


def vector3_rotate_by_axis_angle(v, axis, angle):
    # type: (Vector3, Vector3, float) -> Vector3
    return _Vector3RotateByAxisAngle(v, axis, _float(angle))


def vector3_lerp(v1, v2, amount):
    # type: (Vector3, Vector3, float) -> Vector3
    return _Vector3Lerp(v1, v2, _float(amount))


def vector3_reflect(v, normal):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Reflect(v, normal)


def vector3_min(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Min(v1, v2)


def vector3_max(v1, v2):
    # type: (Vector3, Vector3) -> Vector3
    return _Vector3Max(v1, v2)


def vector3_barycenter(p, a, b, c):
    # type: (Vector3, Vector3, Vector3, Vector3) -> Vector3
    return _Vector3Barycenter(p, a, b, c)


def vector3_unproject(source, projection, view):
    # type: (Vector3, Matrix, Matrix) -> Vector3
    return _Vector3Unproject(source, projection, view)


def vector3_to_float_v(v):
    # type: (Vector3) -> float3
    return _Vector3ToFloatV(v)


def vector3_invert(v):
    # type: (Vector3) -> Vector3
    return _Vector3Invert(v)


def vector3_clamp(v, min_, max_):
    # type: (Vector3, Vector3, Vector3) -> Vector3
    return _Vector3Clamp(v, min_, max_)


def vector3_clamp_value(v, min_, max_):
    # type: (Vector3, float, float) -> Vector3
    return _Vector3ClampValue(v, _float(min_), _float(max_))


def vector3_equals(p, q):
    # type: (Vector3, Vector3) -> int
    return _Vector3Equals(p, q)


def vector3_refract(v, n, r):
    # type: (Vector3, Vector3, float) -> Vector3
    return _Vector3Refract(v, n, _float(r))


def matrix_determinant(mat):
    # type: (Matrix) -> float
    return _MatrixDeterminant(mat)


def matrix_trace(mat):
    # type: (Matrix) -> float
    return _MatrixTrace(mat)


def matrix_transpose(mat):
    # type: (Matrix) -> Matrix
    return _MatrixTranspose(mat)


def matrix_invert(mat):
    # type: (Matrix) -> Matrix
    return _MatrixInvert(mat)


def matrix_identity():
    # type: () -> Matrix
    return _MatrixIdentity()


def matrix_add(left, right):
    # type: (Matrix, Matrix) -> Matrix
    return _MatrixAdd(left, right)


def matrix_subtract(left, right):
    # type: (Matrix, Matrix) -> Matrix
    return _MatrixSubtract(left, right)


def matrix_multiply(left, right):
    # type: (Matrix, Matrix) -> Matrix
    return _MatrixMultiply(left, right)


def matrix_translate(x, y, z):
    # type: (float, float, float) -> Matrix
    return _MatrixTranslate(_float(x), _float(y), _float(z))


def matrix_rotate(axis, angle):
    # type: (Vector3, float) -> Matrix
    return _MatrixRotate(axis, _float(angle))


def matrix_rotate_x(angle):
    # type: (float) -> Matrix
    return _MatrixRotateX(_float(angle))


def matrix_rotate_y(angle):
    # type: (float) -> Matrix
    return _MatrixRotateY(_float(angle))


def matrix_rotate_z(angle):
    # type: (float) -> Matrix
    return _MatrixRotateZ(_float(angle))


def matrix_rotate_xyz(angle):
    # type: (Vector3) -> Matrix
    return _MatrixRotateXYZ(angle)


def matrix_rotate_zyx(angle):
    # type: (Vector3) -> Matrix
    return _MatrixRotateZYX(angle)


def matrix_scale(x, y, z):
    # type: (float, float, float) -> Matrix
    return _MatrixScale(_float(x), _float(y), _float(z))


def matrix_frustum(left, right, bottom, top, near, far):
    # type: (float, float, float, float, float, float) -> Matrix
    return _MatrixFrustum(_float(left), _float(right), _float(bottom), _float(top), _float(near), _float(far))


def matrix_perspective(fov_y, aspect, near_plane, far_plane):
    # type: (float, float, float, float) -> Matrix
    return _MatrixPerspective(_float(fov_y), _float(aspect), _float(near_plane), _float(far_plane))


def matrix_ortho(left, right, bottom, top, near_plane, far_plane):
    # type: (float, float, float, float, float, float) -> Matrix
    return _MatrixOrtho(_float(left), _float(right), _float(bottom), _float(top), _float(near_plane), _float(far_plane))


def matrix_look_at(eye, target, up):
    # type: (Vector3, Vector3, Vector3) -> Matrix
    return _MatrixLookAt(eye, target, up)


def matrix_to_float_v(mat):
    # type: (Matrix) -> float16
    return _MatrixToFloatV(mat)


def quaternion_add(q1, q2):
    # type: (Quaternion, Quaternion) -> Quaternion
    return _QuaternionAdd(q1, q2)


def quaternion_add_value(q, add):
    # type: (Quaternion, float) -> Quaternion
    return _QuaternionAddValue(q, _float(add))


def quaternion_subtract(q1, q2):
    # type: (Quaternion, Quaternion) -> Quaternion
    return _QuaternionSubtract(q1, q2)


def quaternion_subtract_value(q, sub):
    # type: (Quaternion, float) -> Quaternion
    return _QuaternionSubtractValue(q, _float(sub))


def quaternion_identity():
    # type: () -> Quaternion
    return _QuaternionIdentity()


def quaternion_length(q):
    # type: (Quaternion) -> float
    return _QuaternionLength(q)


def quaternion_normalize(q):
    # type: (Quaternion) -> Quaternion
    return _QuaternionNormalize(q)


def quaternion_invert(q):
    # type: (Quaternion) -> Quaternion
    return _QuaternionInvert(q)


def quaternion_multiply(q1, q2):
    # type: (Quaternion, Quaternion) -> Quaternion
    return _QuaternionMultiply(q1, q2)


def quaternion_scale(q, mul):
    # type: (Quaternion, float) -> Quaternion
    return _QuaternionScale(q, _float(mul))


def quaternion_divide(q1, q2):
    # type: (Quaternion, Quaternion) -> Quaternion
    return _QuaternionDivide(q1, q2)


def quaternion_lerp(q1, q2, amount):
    # type: (Quaternion, Quaternion, float) -> Quaternion
    return _QuaternionLerp(q1, q2, _float(amount))


def quaternion_nlerp(q1, q2, amount):
    # type: (Quaternion, Quaternion, float) -> Quaternion
    return _QuaternionNlerp(q1, q2, _float(amount))


def quaternion_slerp(q1, q2, amount):
    # type: (Quaternion, Quaternion, float) -> Quaternion
    return _QuaternionSlerp(q1, q2, _float(amount))


def quaternion_from_vector3_to_vector3(from_, to):
    # type: (Vector3, Vector3) -> Quaternion
    return _QuaternionFromVector3ToVector3(from_, to)


def quaternion_from_matrix(mat):
    # type: (Matrix) -> Quaternion
    return _QuaternionFromMatrix(mat)


def quaternion_to_matrix(q):
    # type: (Quaternion) -> Matrix
    return _QuaternionToMatrix(q)


def quaternion_from_axis_angle(axis, angle):
    # type: (Vector3, float) -> Quaternion
    return _QuaternionFromAxisAngle(axis, _float(angle))


def quaternion_to_axis_angle(q, out_axis, out_angle):
    # type: (Quaternion, Vector3Ptr, FloatPtr) -> None
    _QuaternionToAxisAngle(q, out_axis, out_angle)


def quaternion_from_euler(pitch, yaw, roll):
    # type: (float, float, float) -> Quaternion
    return _QuaternionFromEuler(_float(pitch), _float(yaw), _float(roll))


def quaternion_to_euler(q):
    # type: (Quaternion) -> Vector3
    return _QuaternionToEuler(q)


def quaternion_transform(q, mat):
    # type: (Quaternion, Matrix) -> Quaternion
    return _QuaternionTransform(q, mat)


def quaternion_equals(p, q):
    # type: (Quaternion, Quaternion) -> int
    return _QuaternionEquals(p, q)


# rlapi::rlgl
# ------------------------------------------------------------------------------

def rl_matrix_mode(mode):
    # type: (int) -> None
    """Choose the current matrix to be transformed"""
    _rlMatrixMode(_int(mode))


def rl_push_matrix():
    # type: () -> None
    """Push the current matrix to stack"""
    _rlPushMatrix()


def rl_pop_matrix():
    # type: () -> None
    """Pop latest inserted matrix from stack"""
    _rlPopMatrix()


def rl_load_identity():
    # type: () -> None
    """Reset current matrix to identity matrix"""
    _rlLoadIdentity()


def rl_translatef(x, y, z):
    # type: (float, float, float) -> None
    """Multiply the current matrix by a translation matrix"""
    _rlTranslatef(_float(x), _float(y), _float(z))


def rl_rotatef(angle, x, y, z):
    # type: (float, float, float, float) -> None
    """Multiply the current matrix by a rotation matrix"""
    _rlRotatef(_float(angle), _float(x), _float(y), _float(z))


def rl_scalef(x, y, z):
    # type: (float, float, float) -> None
    """Multiply the current matrix by a scaling matrix"""
    _rlScalef(_float(x), _float(y), _float(z))


def rl_mult_matrixf(matf):
    # type: (FloatPtr) -> None
    """Multiply the current matrix by another matrix"""
    _rlMultMatrixf(matf)


def rl_frustum(left, right, bottom, top, znear, zfar):
    # type: (float, float, float, float, float, float) -> None
    _rlFrustum(_float(left), _float(right), _float(bottom), _float(top), _float(znear), _float(zfar))


def rl_ortho(left, right, bottom, top, znear, zfar):
    # type: (float, float, float, float, float, float) -> None
    _rlOrtho(_float(left), _float(right), _float(bottom), _float(top), _float(znear), _float(zfar))


def rl_viewport(x, y, width, height):
    # type: (int, int, int, int) -> None
    """Set the viewport area"""
    _rlViewport(_int(x), _int(y), _int(width), _int(height))


def rl_begin(mode):
    # type: (int) -> None
    """Initialize drawing mode (how to organize vertex)"""
    _rlBegin(_int(mode))


def rl_end():
    # type: () -> None
    """Finish vertex providing"""
    _rlEnd()


def rl_vertex_2ii(x, y):
    # type: (int, int) -> None
    """Define one vertex (position) - 2 int"""
    _rlVertex2i(_int(x), _int(y))


def rl_vertex_2ff(x, y):
    # type: (float, float) -> None
    """Define one vertex (position) - 2 float"""
    _rlVertex2f(_float(x), _float(y))


def rl_vertex_3ff(x, y, z):
    # type: (float, float, float) -> None
    """Define one vertex (position) - 3 float"""
    _rlVertex3f(_float(x), _float(y), _float(z))


def rl_tex_coord_2ff(x, y):
    # type: (float, float) -> None
    """Define one vertex (texture coordinate) - 2 float"""
    _rlTexCoord2f(_float(x), _float(y))


def rl_normal_3ff(x, y, z):
    # type: (float, float, float) -> None
    """Define one vertex (normal) - 3 float"""
    _rlNormal3f(_float(x), _float(y), _float(z))


def rl_color_4_uub(r, g, b, a):
    # type: (int, int, int, int) -> None
    """Define one vertex (color) - 4 byte"""
    _rlColor4ub(_int(r, (0, 255)), _int(g, (0, 255)), _int(b, (0, 255)), _int(a, (0, 255)))


def rl_color_3ff(x, y, z):
    # type: (float, float, float) -> None
    """Define one vertex (color) - 3 float"""
    _rlColor3f(_float(x), _float(y), _float(z))


def rl_color_4ff(x, y, z, w):
    # type: (float, float, float, float) -> None
    """Define one vertex (color) - 4 float"""
    _rlColor4f(_float(x), _float(y), _float(z), _float(w))


def rl_enable_vertex_array(vao_id):
    # type: (int) -> bool
    """Enable vertex array (VAO, if supported)"""
    return _rlEnableVertexArray(_int(vao_id))


def rl_disable_vertex_array():
    # type: () -> None
    """Disable vertex array (VAO, if supported)"""
    _rlDisableVertexArray()


def rl_enable_vertex_buffer(id_):
    # type: (int) -> None
    """Enable vertex buffer (VBO)"""
    _rlEnableVertexBuffer(_int(id_))


def rl_disable_vertex_buffer():
    # type: () -> None
    """Disable vertex buffer (VBO)"""
    _rlDisableVertexBuffer()


def rl_enable_vertex_buffer_element(id_):
    # type: (int) -> None
    """Enable vertex buffer element (VBO element)"""
    _rlEnableVertexBufferElement(_int(id_))


def rl_disable_vertex_buffer_element():
    # type: () -> None
    """Disable vertex buffer element (VBO element)"""
    _rlDisableVertexBufferElement()


def rl_enable_vertex_attribute(index):
    # type: (int) -> None
    """Enable vertex attribute index"""
    _rlEnableVertexAttribute(_int(index))


def rl_disable_vertex_attribute(index):
    # type: (int) -> None
    """Disable vertex attribute index"""
    _rlDisableVertexAttribute(_int(index))


def rl_active_texture_slot(slot):
    # type: (int) -> None
    """Select and active a texture slot"""
    _rlActiveTextureSlot(_int(slot))


def rl_enable_texture(id_):
    # type: (int) -> None
    """Enable texture"""
    _rlEnableTexture(_int(id_))


def rl_disable_texture():
    # type: () -> None
    """Disable texture"""
    _rlDisableTexture()


def rl_enable_texture_cubemap(id_):
    # type: (int) -> None
    """Enable texture cubemap"""
    _rlEnableTextureCubemap(_int(id_))


def rl_disable_texture_cubemap():
    # type: () -> None
    """Disable texture cubemap"""
    _rlDisableTextureCubemap()


def rl_texture_parameters(id_, param, value):
    # type: (int, int, int) -> None
    """Set texture parameters (filter, wrap)"""
    _rlTextureParameters(_int(id_), _int(param), _int(value))


def rl_cubemap_parameters(id_, param, value):
    # type: (int, int, int) -> None
    """Set cubemap parameters (filter, wrap)"""
    _rlCubemapParameters(_int(id_), _int(param), _int(value))


def rl_enable_shader(id_):
    # type: (int) -> None
    """Enable shader program"""
    _rlEnableShader(_int(id_))


def rl_disable_shader():
    # type: () -> None
    """Disable shader program"""
    _rlDisableShader()


def rl_enable_framebuffer(id_):
    # type: (int) -> None
    """Enable render texture (fbo)"""
    _rlEnableFramebuffer(_int(id_))


def rl_disable_framebuffer():
    # type: () -> None
    """Disable render texture (fbo), return to default framebuffer"""
    _rlDisableFramebuffer()


def rl_active_draw_buffers(count):
    # type: (int) -> None
    """Activate multiple draw color buffers"""
    _rlActiveDrawBuffers(_int(count))


def rl_blit_framebuffer(src_x, src_y, src_width, src_height, dst_x, dst_y, dst_width, dst_height, buffer_mask):
    # type: (int, int, int, int, int, int, int, int, int) -> None
    """Blit active framebuffer to main framebuffer"""
    _rlBlitFramebuffer(_int(src_x), _int(src_y), _int(src_width), _int(src_height), _int(dst_x), _int(dst_y), _int(dst_width), _int(dst_height), _int(buffer_mask))


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


def rl_set_cull_face(mode):
    # type: (int) -> None
    """Set face culling mode"""
    _rlSetCullFace(_int(mode))


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
    _rlScissor(_int(x), _int(y), _int(width), _int(height))


def rl_enable_wire_mode():
    # type: () -> None
    """Enable wire mode"""
    _rlEnableWireMode()


def rl_enable_point_mode():
    # type: () -> None
    """Enable point mode"""
    _rlEnablePointMode()


def rl_disable_wire_mode():
    # type: () -> None
    """Disable wire mode ( and point ) maybe rename"""
    _rlDisableWireMode()


def rl_set_line_width(width):
    # type: (float) -> None
    """Set the line drawing width"""
    _rlSetLineWidth(_float(width))


def rl_get_line_width():
    # type: () -> float
    """Get the line drawing width"""
    return _rlGetLineWidth()


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
    return _rlIsStereoRenderEnabled()


def rl_clear_color(r, g, b, a):
    # type: (int, int, int, int) -> None
    """Clear color buffer with color"""
    _rlClearColor(_int(r, (0, 255)), _int(g, (0, 255)), _int(b, (0, 255)), _int(a, (0, 255)))


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
    _rlSetBlendMode(_int(mode))


def rl_set_blend_factors(gl_src_factor, gl_dst_factor, gl_equation):
    # type: (int, int, int) -> None
    """Set blending mode factor and equation (using OpenGL factors)"""
    _rlSetBlendFactors(_int(gl_src_factor), _int(gl_dst_factor), _int(gl_equation))


def rl_set_blend_factors_separate(gl_src_rgb, gl_dst_rgb, gl_src_alpha, gl_dst_alpha, gl_eq_rgb, gl_eq_alpha):
    # type: (int, int, int, int, int, int) -> None
    """Set blending mode factors and equations separately (using OpenGL factors)"""
    _rlSetBlendFactorsSeparate(_int(gl_src_rgb), _int(gl_dst_rgb), _int(gl_src_alpha), _int(gl_dst_alpha), _int(gl_eq_rgb), _int(gl_eq_alpha))


def rlgl_init(width, height):
    # type: (int, int) -> None
    """Initialize rlgl (buffers, shaders, textures, states)"""
    _rlglInit(_int(width), _int(height))


def rlgl_close():
    # type: () -> None
    """De-initialize rlgl (buffers, shaders, textures)"""
    _rlglClose()


def rl_load_extensions(loader):
    # type: (bytes | str | None) -> None
    """Load OpenGL extensions (loader function required)"""
    _rlLoadExtensions(loader)


def rl_get_version():
    # type: () -> int
    """Get current OpenGL version"""
    return _rlGetVersion()


def rl_set_framebuffer_width(width):
    # type: (int) -> None
    """Set current framebuffer width"""
    _rlSetFramebufferWidth(_int(width))


def rl_get_framebuffer_width():
    # type: () -> int
    """Get default framebuffer width"""
    return _rlGetFramebufferWidth()


def rl_set_framebuffer_height(height):
    # type: (int) -> None
    """Set current framebuffer height"""
    _rlSetFramebufferHeight(_int(height))


def rl_get_framebuffer_height():
    # type: () -> int
    """Get default framebuffer height"""
    return _rlGetFramebufferHeight()


def rl_get_texture_id_default():
    # type: () -> int
    """Get default texture id"""
    return _rlGetTextureIdDefault()


def rl_get_shader_id_default():
    # type: () -> int
    """Get default shader id"""
    return _rlGetShaderIdDefault()


def rl_get_shader_locs_default():
    # type: () -> IntPtr
    """Get default shader locations"""
    return _rlGetShaderLocsDefault()


def rl_load_render_batch(num_buffers, buffer_elements):
    # type: (int, int) -> rlRenderBatch
    """Load a render batch system"""
    return _rlLoadRenderBatch(_int(num_buffers), _int(buffer_elements))


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
    return _rlCheckRenderBatchLimit(_int(v_count))


def rl_set_texture(id_):
    # type: (int) -> None
    """Set current texture for render batch and check buffers limits"""
    _rlSetTexture(_int(id_))


def rl_load_vertex_array():
    # type: () -> int
    """Load vertex array (vao) if supported"""
    return _rlLoadVertexArray()


def rl_load_vertex_buffer(buffer, size, dynamic):
    # type: (bytes | str | None, int, bool) -> int
    """Load a vertex buffer attribute"""
    return _rlLoadVertexBuffer(buffer, _int(size), _bool(dynamic))


def rl_load_vertex_buffer_element(buffer, size, dynamic):
    # type: (bytes | str | None, int, bool) -> int
    """Load a new attributes element buffer"""
    return _rlLoadVertexBufferElement(buffer, _int(size), _bool(dynamic))


def rl_update_vertex_buffer(buffer_id, data, data_size, offset):
    # type: (int, bytes | str | None, int, int) -> None
    """Update GPU buffer with new data"""
    _rlUpdateVertexBuffer(_int(buffer_id), data, _int(data_size), _int(offset))


def rl_update_vertex_buffer_elements(id_, data, data_size, offset):
    # type: (int, bytes | str | None, int, int) -> None
    """Update vertex buffer elements with new data"""
    _rlUpdateVertexBufferElements(_int(id_), data, _int(data_size), _int(offset))


def rl_unload_vertex_array(vao_id):
    # type: (int) -> None
    _rlUnloadVertexArray(_int(vao_id))


def rl_unload_vertex_buffer(vbo_id):
    # type: (int) -> None
    _rlUnloadVertexBuffer(_int(vbo_id))


def rl_set_vertex_attribute(index, comp_size, type_, normalized, stride, pointer):
    # type: (int, int, int, bool, int, bytes | str | None) -> None
    _rlSetVertexAttribute(_int(index), _int(comp_size), _int(type_), _bool(normalized), _int(stride), pointer)


def rl_set_vertex_attribute_divisor(index, divisor):
    # type: (int, int) -> None
    _rlSetVertexAttributeDivisor(_int(index), _int(divisor))


def rl_set_vertex_attribute_default(loc_index, value, attrib_type, count):
    # type: (int, bytes | str | None, int, int) -> None
    """Set vertex attribute default value"""
    _rlSetVertexAttributeDefault(_int(loc_index), value, _int(attrib_type), _int(count))


def rl_draw_vertex_array(offset, count):
    # type: (int, int) -> None
    _rlDrawVertexArray(_int(offset), _int(count))


def rl_draw_vertex_array_elements(offset, count, buffer):
    # type: (int, int, bytes | str | None) -> None
    _rlDrawVertexArrayElements(_int(offset), _int(count), buffer)


def rl_draw_vertex_array_instanced(offset, count, instances):
    # type: (int, int, int) -> None
    _rlDrawVertexArrayInstanced(_int(offset), _int(count), _int(instances))


def rl_draw_vertex_array_elements_instanced(offset, count, buffer, instances):
    # type: (int, int, bytes | str | None, int) -> None
    _rlDrawVertexArrayElementsInstanced(_int(offset), _int(count), buffer, _int(instances))


def rl_load_texture(data, width, height, format_, mipmap_count):
    # type: (bytes | str | None, int, int, int, int) -> int
    """Load texture in GPU"""
    return _rlLoadTexture(data, _int(width), _int(height), _int(format_), _int(mipmap_count))


def rl_load_texture_depth(width, height, use_render_buffer):
    # type: (int, int, bool) -> int
    """Load depth texture/renderbuffer (to be attached to fbo)"""
    return _rlLoadTextureDepth(_int(width), _int(height), _bool(use_render_buffer))


def rl_load_texture_cubemap(data, size, format_):
    # type: (bytes | str | None, int, int) -> int
    """Load texture cubemap"""
    return _rlLoadTextureCubemap(data, _int(size), _int(format_))


def rl_update_texture(id_, offset_x, offset_y, width, height, format_, data):
    # type: (int, int, int, int, int, int, bytes | str | None) -> None
    """Update GPU texture with new data"""
    _rlUpdateTexture(_int(id_), _int(offset_x), _int(offset_y), _int(width), _int(height), _int(format_), data)


def rl_get_gl_texture_formats(format_, gl_internal_format, gl_format, gl_type):
    # type: (int, UIntPtr, UIntPtr, UIntPtr) -> None
    """Get OpenGL internal formats"""
    _rlGetGlTextureFormats(_int(format_), gl_internal_format, gl_format, gl_type)


def rl_get_pixel_format_name(format_):
    # type: (int) -> bytes | str | None
    """Get name string for pixel format"""
    return _rlGetPixelFormatName(_int(format_))


def rl_unload_texture(id_):
    # type: (int) -> None
    """Unload texture from GPU memory"""
    _rlUnloadTexture(_int(id_))


def rl_gen_texture_mipmaps(id_, width, height, format_, mipmaps):
    # type: (int, int, int, int, IntPtr) -> None
    """Generate mipmap data for selected texture"""
    _rlGenTextureMipmaps(_int(id_), _int(width), _int(height), _int(format_), mipmaps)


def rl_read_texture_pixels(id_, width, height, format_):
    # type: (int, int, int, int) -> bytes | str | None
    """Read texture pixel data"""
    return _rlReadTexturePixels(_int(id_), _int(width), _int(height), _int(format_))


def rl_read_screen_pixels(width, height):
    # type: (int, int) -> int
    """Read screen pixel data (color buffer)"""
    return _rlReadScreenPixels(_int(width), _int(height))


def rl_load_framebuffer(width, height):
    # type: (int, int) -> int
    """Load an empty framebuffer"""
    return _rlLoadFramebuffer(_int(width), _int(height))


def rl_framebuffer_attach(fbo_id, tex_id, attach_type, tex_type, mip_level):
    # type: (int, int, int, int, int) -> None
    """Attach texture/renderbuffer to a framebuffer"""
    _rlFramebufferAttach(_int(fbo_id), _int(tex_id), _int(attach_type), _int(tex_type), _int(mip_level))


def rl_framebuffer_complete(id_):
    # type: (int) -> bool
    """Verify framebuffer is complete"""
    return _rlFramebufferComplete(_int(id_))


def rl_unload_framebuffer(id_):
    # type: (int) -> None
    """Delete framebuffer from GPU"""
    _rlUnloadFramebuffer(_int(id_))


def rl_load_shader_code(vs_code, fs_code):
    # type: (bytes | str | None, bytes | str | None) -> int
    """Load shader from code strings"""
    return _rlLoadShaderCode(_str_in(vs_code), _str_in(fs_code))


def rl_compile_shader(shader_code, type_):
    # type: (bytes | str | None, int) -> int
    """Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)"""
    return _rlCompileShader(_str_in(shader_code), _int(type_))


def rl_load_shader_program(v_shader_id, f_shader_id):
    # type: (int, int) -> int
    """Load custom shader program"""
    return _rlLoadShaderProgram(_int(v_shader_id), _int(f_shader_id))


def rl_unload_shader_program(id_):
    # type: (int) -> None
    """Unload shader program"""
    _rlUnloadShaderProgram(_int(id_))


def rl_get_location_uniform(shader_id, uniform_name):
    # type: (int, bytes | str | None) -> int
    """Get shader location uniform"""
    return _rlGetLocationUniform(_int(shader_id), _str_in(uniform_name))


def rl_get_location_attrib(shader_id, attrib_name):
    # type: (int, bytes | str | None) -> int
    """Get shader location attribute"""
    return _rlGetLocationAttrib(_int(shader_id), _str_in(attrib_name))


def rl_set_uniform(loc_index, value, uniform_type, count):
    # type: (int, bytes | str | None, int, int) -> None
    """Set shader value uniform"""
    _rlSetUniform(_int(loc_index), value, _int(uniform_type), _int(count))


def rl_set_uniform_matrix(loc_index, mat):
    # type: (int, Matrix) -> None
    """Set shader value matrix"""
    _rlSetUniformMatrix(_int(loc_index), mat)


def rl_set_uniform_sampler(loc_index, texture_id):
    # type: (int, int) -> None
    """Set shader value sampler"""
    _rlSetUniformSampler(_int(loc_index), _int(texture_id))


def rl_set_shader(id_, locs):
    # type: (int, IntPtr) -> None
    """Set shader currently active (id and locations)"""
    _rlSetShader(_int(id_), locs)


def rl_load_compute_shader_program(shader_id):
    # type: (int) -> int
    """Load compute shader program"""
    return _rlLoadComputeShaderProgram(_int(shader_id))


def rl_compute_shader_dispatch(group_x, group_y, group_z):
    # type: (int, int, int) -> None
    """Dispatch compute shader (equivalent to *draw* for graphics pipeline)"""
    _rlComputeShaderDispatch(_int(group_x), _int(group_y), _int(group_z))


def rl_load_shader_buffer(size, data, usage_hint):
    # type: (int, bytes | str | None, int) -> int
    """Load shader storage buffer object (SSBO)"""
    return _rlLoadShaderBuffer(_int(size), data, _int(usage_hint))


def rl_unload_shader_buffer(ssbo_id):
    # type: (int) -> None
    """Unload shader storage buffer object (SSBO)"""
    _rlUnloadShaderBuffer(_int(ssbo_id))


def rl_update_shader_buffer(id_, data, data_size, offset):
    # type: (int, bytes | str | None, int, int) -> None
    """Update SSBO buffer data"""
    _rlUpdateShaderBuffer(_int(id_), data, _int(data_size), _int(offset))


def rl_bind_shader_buffer(id_, index):
    # type: (int, int) -> None
    """Bind SSBO buffer"""
    _rlBindShaderBuffer(_int(id_), _int(index))


def rl_read_shader_buffer(id_, dest, count, offset):
    # type: (int, bytes | str | None, int, int) -> None
    """Read SSBO buffer data (GPU->CPU)"""
    _rlReadShaderBuffer(_int(id_), dest, _int(count), _int(offset))


def rl_copy_shader_buffer(dest_id, src_id, dest_offset, src_offset, count):
    # type: (int, int, int, int, int) -> None
    """Copy SSBO data between buffers"""
    _rlCopyShaderBuffer(_int(dest_id), _int(src_id), _int(dest_offset), _int(src_offset), _int(count))


def rl_get_shader_buffer_size(id_):
    # type: (int) -> int
    """Get SSBO buffer size"""
    return _rlGetShaderBufferSize(_int(id_))


def rl_bind_image_texture(id_, index, format_, readonly):
    # type: (int, int, int, bool) -> None
    """Bind image texture"""
    _rlBindImageTexture(_int(id_), _int(index), _int(format_), _bool(readonly))


def rl_get_matrix_modelview():
    # type: () -> Matrix
    """Get internal modelview matrix"""
    return _rlGetMatrixModelview()


def rl_get_matrix_projection():
    # type: () -> Matrix
    """Get internal projection matrix"""
    return _rlGetMatrixProjection()


def rl_get_matrix_transform():
    # type: () -> Matrix
    """Get internal accumulated transform matrix"""
    return _rlGetMatrixTransform()


def rl_get_matrix_projection_stereo(eye):
    # type: (int) -> Matrix
    """Get internal projection matrix for stereo render (selected eye)"""
    return _rlGetMatrixProjectionStereo(_int(eye))


def rl_get_matrix_view_offset_stereo(eye):
    # type: (int) -> Matrix
    """Get internal view offset matrix for stereo render (selected eye)"""
    return _rlGetMatrixViewOffsetStereo(_int(eye))


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

# endregion (functions)

# region CONTEXT MANAGERS

# rlapi::raylib
# ------------------------------------------------------------------------------

@contextmanager
def drawing():
    """Context manager for BeginDrawing and EndDrawing"""
    _BeginDrawing()
    yield
    _EndDrawing()


@contextmanager
def scissor_mode(x, y, width, height):
    """Context manager for BeginScissorMode and EndScissorMode"""
    _BeginScissorMode(x, y, width, height)
    yield
    _EndScissorMode()


@contextmanager
def blend_mode(mode):
    """Context manager for BeginBlendMode and EndBlendMode"""
    _BeginBlendMode(mode)
    yield
    _EndBlendMode()


@contextmanager
def mode2d(camera):
    """Context manager for BeginMode2D and EndMode2D"""
    _BeginMode2D(camera)
    yield
    _EndMode2D()


@contextmanager
def mode3d(camera):
    """Context manager for BeginMode3D and EndMode3D"""
    _BeginMode3D(camera)
    yield
    _EndMode3D()


@contextmanager
def shader_mode(shader):
    """Context manager for BeginShaderMode and EndShaderMode"""
    _BeginShaderMode(shader)
    yield
    _EndShaderMode()


@contextmanager
def texture_mode(target):
    """Context manager for BeginTextureMode and EndTextureMode"""
    _BeginTextureMode(target)
    yield
    _EndTextureMode()


@contextmanager
def vr_stereo_mode(config):
    """Context manager for BeginVrStereoMode and EndVrStereoMode"""
    _BeginVrStereoMode(config)
    yield
    _EndVrStereoMode()


# rlapi::rlgl
# ------------------------------------------------------------------------------

@contextmanager
def rl_gl(mode):
    """Context manager for rlBegin and rlEnd"""
    _rlBegin(mode)
    yield
    _rlEnd()


@contextmanager
def rl_vertex_array(vao_id):
    """Context manager for rlEnableVertexArray and rlDisableVertexArray"""
    _rlEnableVertexArray(vao_id)
    yield
    _rlDisableVertexArray()


@contextmanager
def rl_vertex_buffer(id_):
    """Context manager for rlEnableVertexBuffer and rlDisableVertexBuffer"""
    _rlEnableVertexBuffer(id_)
    yield
    _rlDisableVertexBuffer()


@contextmanager
def rl_vertex_buffer_element(id_):
    """Context manager for rlEnableVertexBufferElement and rlDisableVertexBufferElement"""
    _rlEnableVertexBufferElement(id_)
    yield
    _rlDisableVertexBufferElement()


@contextmanager
def rl_vertex_attribute(index):
    """Context manager for rlEnableVertexAttribute and rlDisableVertexAttribute"""
    _rlEnableVertexAttribute(index)
    yield
    _rlDisableVertexAttribute()


@contextmanager
def rl_texture(id_):
    """Context manager for rlEnableTexture and rlDisableTexture"""
    _rlEnableTexture(id_)
    yield
    _rlDisableTexture()


@contextmanager
def rl_texture_cubemap(id_):
    """Context manager for rlEnableTextureCubemap and rlDisableTextureCubemap"""
    _rlEnableTextureCubemap(id_)
    yield
    _rlDisableTextureCubemap()


@contextmanager
def rl_shader(id_):
    """Context manager for rlEnableShader and rlDisableShader"""
    _rlEnableShader(id_)
    yield
    _rlDisableShader()


@contextmanager
def rl_framebuffer(id_):
    """Context manager for rlEnableFramebuffer and rlDisableFramebuffer"""
    _rlEnableFramebuffer(id_)
    yield
    _rlDisableFramebuffer()


@contextmanager
def rl_color_blend():
    """Context manager for rlEnableColorBlend and rlDisableColorBlend"""
    _rlEnableColorBlend()
    yield
    _rlDisableColorBlend()


@contextmanager
def rl_depth_test():
    """Context manager for rlEnableDepthTest and rlDisableDepthTest"""
    _rlEnableDepthTest()
    yield
    _rlDisableDepthTest()


@contextmanager
def rl_depth_mask():
    """Context manager for rlEnableDepthMask and rlDisableDepthMask"""
    _rlEnableDepthMask()
    yield
    _rlDisableDepthMask()


@contextmanager
def rl_backface_culling():
    """Context manager for rlEnableBackfaceCulling and rlDisableBackfaceCulling"""
    _rlEnableBackfaceCulling()
    yield
    _rlDisableBackfaceCulling()


@contextmanager
def rl_scissor_test():
    """Context manager for rlEnableScissorTest and rlDisableScissorTest"""
    _rlEnableScissorTest()
    yield
    _rlDisableScissorTest()


@contextmanager
def rl_wire_mode():
    """Context manager for rlEnableWireMode and rlDisableWireMode"""
    _rlEnableWireMode()
    yield
    _rlDisableWireMode()


@contextmanager
def rl_smooth_lines():
    """Context manager for rlEnableSmoothLines and rlDisableSmoothLines"""
    _rlEnableSmoothLines()
    yield
    _rlDisableSmoothLines()


@contextmanager
def rl_stereo_render():
    """Context manager for rlEnableStereoRender and rlDisableStereoRender"""
    _rlEnableStereoRender()
    yield
    _rlDisableStereoRender()

# endregion (context managers)

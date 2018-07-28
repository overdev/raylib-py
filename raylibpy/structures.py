from constants import *
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
    Structure,
    byref
)


__all__ = [
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
]

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

# STRUCTURES DEFINITIONS
# -------------------------------------------------------------------

class Vector2(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float)
    ]


Vector2Ptr = POINTER(Vector2)


class Vector3(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
    ]


Vector3Ptr = POINTER(Vector3)


class Vector4(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
        ('w', c_float),
    ]


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


class Color(Structure):
    _fields_ = [
        ('r', c_ubyte),
        ('g', c_ubyte),
        ('b', c_ubyte),
        ('a', c_ubyte),
    ]


ColorPtr = POINTER(Color)


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

ImagePtr = POINTER(Image)

class Texture2D(Structure):
    _fields_ = [
        ('data', c_void_p),
        ('id', c_uint),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]


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


CharInfoPtr = POINTER(CharInfo)


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


Camera3DPtr = POINTER(Camera3D)
Camera = Camera3D
CameraPtr = Camera3DPtr


"""
typedef struct Camera2D {
    Vector2 offset;         // Camera offset (displacement from target)
    Vector2 target;         // Camera target (rotation and zoom origin)
    float rotation;         // Camera rotation in degrees
    float zoom;             // Camera zoom (scaling), should be 1.0f by default
} Camera2D;
"""

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


MeshPtr = POINTER(Mesh)


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


ModelPtr = POINTER(Model)


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


WavePtr = POINTER(Wave)


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


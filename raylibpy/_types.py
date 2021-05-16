from typing import Union, Sequence, Tuple, List
from ctypes import (
    c_bool,
    c_char_p,
    c_byte,
    c_ubyte,
    c_int,
    c_uint,
    c_short,
    c_ushort,
    c_void_p,
    c_float,
    c_double,
    POINTER, c_long, CFUNCTYPE
)

__all__ = [
    'Bool',
    'VoidPtr',
    'CharPtr',
    'CharPtrPtr',
    'UCharPtr',
    'IntPtr',
    'UIntPtr',
    'FloatPtr',
    'Char',
    'UChar',
    'Byte',
    'Short',
    'UShort',
    'Int',
    'UInt',
    'Long',
    'LongPtr',
    'Float',
    'Double',
    'Number',
    'Seq',
    'VectorN',
    'TVec4',
    'LVector',
    'Vec4',
    'RGBA',
    'AnyRect',
    'AnyRGB',
    'AnyVec2',
    'AnyVec3',
    'AnyVec4',
    'AnyQuat4',
    'TraceLogCallback',
    'LoadFileDataCallback',
    'SaveFileDataCallback',
    'LoadFileTextCallback',
    'SaveFileTextCallback',
]

# ---------------------------------------------------------
# region CONSTANTS & ENUMS

Bool = c_bool
VoidPtr = c_void_p
CharPtr = c_char_p
CharPtrPtr = POINTER(c_char_p)
UCharPtr = POINTER(c_ubyte)
IntPtr = POINTER(c_int)
LongPtr = POINTER(c_long)
UIntPtr = POINTER(c_uint)
FloatPtr = POINTER(c_float)
Char = c_byte
UChar = c_ubyte
Byte = c_byte
Short = c_short
UShort = c_ushort
Int = c_int
UInt = c_uint
Long = c_long
Float = c_float
Double = c_double
Number = Union[int, float]
Seq = Sequence[Number]
ISeq = Sequence[int]
FSeq = Sequence[float]
VectorN = Union[Seq, 'Vector4', 'Vector3', 'Vector2', 'Quaternion']
RGBA = Union[ISeq, 'Color']
TVec4 = Tuple[Number, Number, Number, Number]
LVector = List[Number]
Vec4 = Union['Vector4', TVec4, LVector]

Num2 = Tuple[Number, Number]
Num3 = Tuple[Number, Number, Number]
Num4 = Tuple[Number, Number, Number, Number]

int2 = Tuple[int, int]
int3 = Tuple[int, int, int]
int4 = Tuple[int, int, int, int]

float2 = Tuple[float, float]
float3 = Tuple[float, float, float]
float4 = Tuple[float, float, float, float]

AnyRect = Union[Seq, Num4, 'Rectangle']
AnyRGB = Union[bytes, bytearray, ISeq, int4, 'Color']
AnyVec2 = Union[Seq, Num2, int2, float2, 'Vector2']
AnyVec3 = Union[Seq, Num3, int3, float3, 'Vector3']
AnyVec4 = Union[Seq, Num4, int4, float4, 'Vector4']
AnyQuat4 = Union[Seq, Num4, int4, float4, 'Vector4']

# region CALLBACKS

TraceLogCallback = CFUNCTYPE(None, Int, CharPtr, VoidPtr)
LoadFileDataCallback = CFUNCTYPE(UCharPtr, CharPtr, UIntPtr)
SaveFileDataCallback = CFUNCTYPE(Bool, CharPtr, VoidPtr, UInt)
LoadFileTextCallback = CFUNCTYPE(CharPtr, CharPtr)
SaveFileTextCallback = CFUNCTYPE(Bool, CharPtr, CharPtr)

# endregion (constants)
# ---------------------------------------------------------
# region FUNCTIONS

# endregion (functions)
# ---------------------------------------------------------
# region CLASSES

# endregion (classes)
# ---------------------------------------------------------

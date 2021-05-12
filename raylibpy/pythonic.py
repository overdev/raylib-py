from ctypes import byref
from typing import Sequence, Tuple, Union
from raylibpy import _rl
import re
from typing import Any, Dict, Union, Tuple, List, Sequence, TypeVar, Optional
from ctypes import (
    Structure,
    c_bool,
    c_ubyte,
    c_int,
    c_uint,
    c_ushort,
    c_void_p,
    c_float,
    c_char,
    POINTER,
    Array,
)
from raylibpy._types import *

__all__ = [
    'Vector2',
    'Vector2Ptr',
    'Vector3',
    'Vector3Ptr',
    'Vector4',
    'Vector4Ptr',
    'Quaternion',
    'Matrix',
    'Color',
    'Rectangle',
    'Image',
    'Texture',
    'TextureCubemap',
    'Texture2D',
    'RenderTexture',
    'RenderTexture2D',
    'NPatchInfo',
    'CharInfo',
    'Font',
    'SpriteFont',
    'Camera3D',
    'Camera',
    'Camera2D',
    'Mesh',
    'Shader',
    'MaterialMap',
    'Material',
    'Transform',
    'BoneInfo',
    'Model',
    'ModelAnimation',
    'ModelAnimationPtr',
    'Ray',
    'RayHitInfo',
    'BoundingBox',
    'Wave',
    'rAudioBuffer',
    'AudioStream',
    'Sound',
    'Music',
    '_VrDeviceInfo',
    '_VrStereoConfig',

    # Pointer Types
    'CharInfoPtr',
    'CameraPtr',
    'Camera3DPtr',
    'ModelPtr',
    'MeshPtr',
    'RayHitInfoPtr',
    'WavePtr',
    'Vector2Ptr',
    # 'Vector3Ptr',
    # 'Vector4Ptr',
    # 'QuaternionPtr',
    'MatrixPtr',
    'ColorPtr',
    'RectanglePtr',
    'RectanglePtrPtr',
    'ImagePtr',
    # 'TexturePtr',
    # 'TextureCubemapPtr',
    'Texture2DPtr',
    # 'RenderTexturePtr',
    # 'RenderTexture2DPtr',
    # 'NPatchInfoPtr',
    'CharInfoPtr',
    # 'FontPtr',
    # 'SpriteFontPtr',
    'Camera3DPtr',
    'CameraPtr',
    # 'Camera2DPtr',
    'MeshPtr',
    # 'ShaderPtr',
    # 'MaterialMapPtr',
    'MaterialPtr',
    # 'TransformPtr',
    # 'BoneInfoPtr',
    'ModelPtr',
    # 'ModelAnimationPtr',
    # 'RayPtr',
    # 'BoundingBoxPtr',
    'WavePtr',
    'rAudioBufferPtr',
    # 'AudioStreamPtr',
    # 'SoundPtr',

    # TYPE CASTS
    '_vec2',
    '_vec3',
    '_vec4',
    '_rect',
    '_color',
    '_arr',
    '_arr2',
    '_str_in',
    '_str_in2',
    '_str_out',
]

# ---------------------------------------------------------
# region CONSTANTS & ENUMS

# region HELPER CONSTS

_VEC2_GET_SWZL = re.compile(r'[xy]{,4}')
_VEC3_GET_SWZL = re.compile(r'[xyz]{1,4}|[rgb]{1,4}')
_VEC4_GET_SWZL = re.compile(r'[xyzw]{1,4}|[rgba]{1,4}')
_RGBA_GET_SWZL = re.compile(r'[rgba]{1,4}')

_number = (int, float)

_RGBA_TO_XYZW = {'r': 'x', 'g': 'y', 'b': 'z', 'a': 'w'}

T = TypeVar('T')
U = TypeVar('U')


# endregion (helper consts)

# endregion (constants)
# ---------------------------------------------------------
# region FUNCTIONS


def is_number(obj) -> bool:
    return isinstance(obj, _number)


def is_component(value) -> bool:
    return isinstance(value, int) and 0 <= value <= 255


def _clsname(obj: Any) -> str:
    return obj.__class__.__name__


def _clamp_rgba(*args) -> Union[int, Sequence[int]]:
    return tuple(value & 255 for value in args)


def _str_in(value: Union[str, bytes]) -> bytes:
    return value.encode('utf-8', 'ignore') if isinstance(value, str) else value


def _str_in2(values: Sequence[Union[str, bytes]]) -> Array[bytes]:
    return _arr(CharPtr, tuple(_str_in(value) for value in values))


def _str_out(value: Union[str, bytes]) -> bytes:
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


def _arr(typ: Any, data: Sequence[U]) -> Array[U]:
    return (typ * len(data))(*data)


def _arr2(typ: Any, data: Sequence[U]) -> Array[U]:
    arr = typ * len(data[0])
    return (arr * len(data))(*data)


# region TYPE CAST FUNCS


def _float(value) -> float:
    return float(value)


def _int(value, ranged: Optional[Tuple[int, int]] = None) -> int:
    if ranged:
        return max(ranged[0], min(int(value), ranged[1]))
    return int(value)


def _vec2(seq: AnyVec2) -> 'Vector2':
    if isinstance(seq, Vector2):
        return seq
    x, y = seq
    return Vector2(_float(x), _float(y))


def _vec3(seq: AnyVec3) -> 'Vector3':
    if isinstance(seq, Vector3):
        return seq
    x, y, z = seq
    return Vector3(float(x), float(y), float(z))


def _vec4(seq: AnyVec3) -> 'Vector4':
    if isinstance(seq, Vector4):
        return seq
    x, y, z, w = seq
    return Vector4(float(x), float(y), float(z), float(w))


def _rect(seq: AnyRect) -> 'Rectangle':
    if isinstance(seq, Rectangle):
        return seq
    x, y, w, h = seq
    return Rectangle(float(x), float(y), float(w), float(h))


def _color(seq: AnyRGB) -> 'Color':
    if isinstance(seq, Color):
        return seq
    r, g, b, q = seq
    rng = 0, 255
    return Color(_int(r, rng), _int(r, rng), _int(b, rng), _int(q, rng))


# endregion (type cast funcs)

# endregion (functions)
# ---------------------------------------------------------
# region CLASSES

# region VECTORS


class Vector2(Structure):
    """Wraps raylib's Vector2 struct.

    Extended support for:
    - string representation with str and repr;
    - attribute swizzling of x and y axes;
    - math operations (+, -, *, /, //, %, abs, negation, rounding)
    - subscript access for reading and writing

    """

    _fields_ = [
        ('x', c_float),
        ('y', c_float)
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0):
        super().__init__(x, y)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union['Vector2', 'Vector3', 'Vector4', float]:
        m = _VEC2_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: VectorN):
        m = _VEC2_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                super(Vector2, self).__setattr__(ch, value[i])
        else:
            if not is_number(value):
                raise ValueError(f"int or float expected, got {_clsname(value)}.")
            super(Vector2, self).__setattr__(attr, float(value))

    # endregion (attribute swizzling)

    # region VECTOR MATH

    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __abs__(self) -> 'Vector2':
        return Vector2(abs(self.x), abs(self.y))

    def __round__(self, n=None) -> 'Vector2':
        return Vector2(round(self.x, n), round(self.y, n))

    def __add__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x + (other if is_num else other[0]),
                       self.y + (other if is_num else other[1]))

    def __radd__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) + self.x,
                       (other if is_num else other[1]) + self.y)

    def __iadd__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x += other if is_num else other[0]
        self.y += other if is_num else other[1]
        return self

    def __sub__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x - (other if is_num else other[0]),
                       self.y - (other if is_num else other[1]))

    def __rsub__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) - self.x,
                       (other if is_num else other[1]) - self.y)

    def __isub__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x -= other if is_num else other[0]
        self.y -= other if is_num else other[1]
        return self

    def __mul__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x * (other if is_num else other[0]),
                       self.y * (other if is_num else other[1]))

    def __rmul__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) * self.x,
                       (other if is_num else other[1]) * self.y)

    def __imul__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x *= other if is_num else other[0]
        self.y *= other if is_num else other[1]
        return self

    def __truediv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x / (other if is_num else other[0]),
                       self.y / (other if is_num else other[1]))

    def __rtruediv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) / self.x,
                       (other if is_num else other[1]) / self.y)

    def __itruediv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x /= other if is_num else other[0]
        self.y /= other if is_num else other[1]
        return self

    def __floordiv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x // (other if is_num else other[0]),
                       self.y // (other if is_num else other[1]))

    def __rfloordiv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) // self.x,
                       (other if is_num else other[1]) // self.y)

    def __ifloordiv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x //= other if is_num else other[0]
        self.y //= other if is_num else other[1]
        return self

    def __mod__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x % (other if is_num else other[0]),
                       self.y % (other if is_num else other[1]))

    def __rmod__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) % self.x,
                       (other if is_num else other[1]) % self.y)

    def __imod__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x %= other if is_num else other[0]
        self.y %= other if is_num else other[1]
        return self

    # endregion (vector math)

    # region COMPARISSON

    def __eq__(self, other: VectorN) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.x == other[0] and self.y == other[1]
        return False

    def __ne__(self, other: VectorN) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.x != other[0] or self.y != other[1]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 2

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as index key.")
        return getattr(self, 'xy'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as index key.")
        setattr(self, 'xy'[key], value)

    # endregion (container support)

    # region METHODS

    def todict(self) -> Dict[str, float]:
        return {'x': self.x, 'y': self.y}

    def fromdict(self, d: Dict[str, float]):
        self.x = float(d.get('x', 0.0))
        self.y = float(d.get('y', 0.0))

    def totuple(self) -> Tuple[Number, Number]:
        return (self.x, self.y)

    def tolist(self) -> List[Number]:
        return [self.x, self.y]

    # endregion (methods)


Vector2Ptr = POINTER(Vector2)


class Vector3(Structure):
    """Wraps raylib's Vector3 struct.

    Extended support for:
    - string representation with str and repr;
    - attribute swizzling of x and y axes;
    - math operations (+, -, *, /, //, %, abs, negation, rounding)
    - subscript access for reading and writing
    """
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0, z: Number = 0.0):
        super().__init__(x, y, z)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y}, {self.z})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union['Vector2', 'Vector3', 'Vector4', float]:
        m = _VEC3_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict('r' in attr or 'g' in attr or 'b' in attr or 'a' in attr)
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: VectorN):
        m = _VEC3_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        as_color = 'r' in attr or 'g' in attr or 'b' in attr
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                super(Vector3, self).__setattr__(_RGBA_TO_XYZW[ch] if as_color else ch, value[i])
        else:
            if not is_number(value):
                raise ValueError(f"int or float expected, got {_clsname(value)}.")
            super(Vector3, self).__setattr__(_RGBA_TO_XYZW[attr] if as_color else attr, float(value))

    # endregion (attribute swizzling)

    # region VECTOR MATH

    def __neg__(self) -> 'Vector3':
        return Vector3(-self.x, -self.y, -self.z)

    def __abs__(self) -> 'Vector3':
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def __round__(self, n=None) -> 'Vector3':
        return Vector3(round(self.x, n), round(self.y, n), round(self.z, n))

    def __add__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x + (other if is_num else other[0]),
                       self.y + (other if is_num else other[1]),
                       self.z + (other if is_num else other[2]))

    def __radd__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) + self.x,
                       (other if is_num else other[1]) + self.y,
                       (other if is_num else other[2]) + self.z)

    def __iadd__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x += other if is_num else other[0]
        self.y += other if is_num else other[1]
        self.z += other if is_num else other[2]
        return self

    def __sub__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x - (other if is_num else other[0]),
                       self.y - (other if is_num else other[1]),
                       self.z - (other if is_num else other[2]))

    def __rsub__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) - self.x,
                       (other if is_num else other[1]) - self.y,
                       (other if is_num else other[2]) - self.z)

    def __isub__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x -= other if is_num else other[0]
        self.y -= other if is_num else other[1]
        self.z -= other if is_num else other[2]
        return self

    def __mul__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x * (other if is_num else other[0]),
                       self.y * (other if is_num else other[1]),
                       self.z * (other if is_num else other[2]))

    def __rmul__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) * self.x,
                       (other if is_num else other[1]) * self.y,
                       (other if is_num else other[2]) * self.z)

    def __imul__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x *= other if is_num else other[0]
        self.y *= other if is_num else other[1]
        self.z *= other if is_num else other[2]
        return self

    def __truediv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x / (other if is_num else other[0]),
                       self.y / (other if is_num else other[1]),
                       self.z / (other if is_num else other[2]))

    def __rtruediv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) / self.x,
                       (other if is_num else other[1]) / self.y,
                       (other if is_num else other[2]) / self.z)

    def __itruediv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x /= other if is_num else other[0]
        self.y /= other if is_num else other[1]
        self.z /= other if is_num else other[2]
        return self

    def __floordiv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x // (other if is_num else other[0]),
                       self.y // (other if is_num else other[1]),
                       self.z // (other if is_num else other[2]))

    def __rfloordiv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) // self.x,
                       (other if is_num else other[1]) // self.y,
                       (other if is_num else other[2]) // self.z)

    def __ifloordiv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x //= other if is_num else other[0]
        self.y //= other if is_num else other[1]
        self.z //= other if is_num else other[2]
        return self

    def __mod__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x % (other if is_num else other[0]),
                       self.y % (other if is_num else other[1]),
                       self.z % (other if is_num else other[2]))

    def __rmod__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) % self.x,
                       (other if is_num else other[1]) % self.y,
                       (other if is_num else other[2]) % self.z)

    def __imod__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x %= other if is_num else other[0]
        self.y %= other if is_num else other[1]
        self.z %= other if is_num else other[2]
        return self

    # endregion (vector math)

    # region COMPARISSON

    def __eq__(self, other: VectorN) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.x == other[0] and self.y == other[1] and self.z == other[2]
        return False

    def __ne__(self, other: VectorN) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.x != other[0] or self.y != other[1] or self.z != other[2]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 3

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        return getattr(self, 'xyz'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        setattr(self, 'xyz'[key], value)

    # endregion (container support)

    # region METHODS

    def todict(self, as_color: bool = False) -> Dict[str, float]:
        if as_color:
            return {'r': self.x, 'g': self.y, 'b': self.z}
        return {'x': self.x, 'y': self.y, 'z': self.z}

    def fromdict(self, d: Dict[str, float]):
        self.x = float(d.get('x', 0.0))
        self.y = float(d.get('y', 0.0))
        self.z = float(d.get('z', 0.0))

    def totuple(self) -> Tuple[Number, Number, Number]:
        return self.x, self.y, self.z

    def tolist(self) -> List[Number]:
        return [self.x, self.y, self.z]

    # endregion (methods)


Vector3Ptr = POINTER(Vector3)


class Vector4(Structure):
    """Wraps raylib's Vector4 struct.

    Extended support for:
    - string representation with str and repr;
    - attribute swizzling of x and y axes;
    - math operations (+, -, *, /, //, %, abs, negation, rounding)
    - subscript access for reading and writing
    """
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
        ('w', c_float),
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0, z: Number = 0.0, w: Number = 0.0):
        super().__init__(x, y, z, w)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y}, {self.z}, {self.w})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union['Vector2', 'Vector3', 'Vector4', float]:
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict('r' in attr or 'g' in attr or 'b' in attr or 'a' in attr)
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: VectorN):
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        as_color = 'r' in attr or 'g' in attr or 'b' in attr or 'a' in attr
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                super(Vector4, self).__setattr__(_RGBA_TO_XYZW[ch] if as_color else ch, value[i])
        else:
            if not is_number(value):
                raise ValueError(f"int or float expected, got {_clsname(value)}.")
            super(Vector4, self).__setattr__(_RGBA_TO_XYZW[attr] if as_color else attr, float(value))

    # endregion (attribute swizzling)

    # region VECTOR MATH

    def __neg__(self) -> 'Vector4':
        return Vector4(-self.x, -self.y, -self.z, -self.w)

    def __abs__(self) -> 'Vector4':
        return Vector4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

    def __round__(self, n=None) -> 'Vector4':
        return Vector4(round(self.x, n), round(self.y, n), round(self.z, n), round(self.w, n))

    def __add__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x + (other if is_num else other[0]),
                       self.y + (other if is_num else other[1]),
                       self.z + (other if is_num else other[2]),
                       self.w + (other if is_num else other[3]))

    def __radd__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) + self.x,
                       (other if is_num else other[1]) + self.y,
                       (other if is_num else other[2]) + self.z,
                       (other if is_num else other[3]) + self.w)

    def __iadd__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x += other if is_num else other[0]
        self.y += other if is_num else other[1]
        self.z += other if is_num else other[2]
        self.w += other if is_num else other[3]
        return self

    def __sub__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x - (other if is_num else other[0]),
                       self.y - (other if is_num else other[1]),
                       self.z - (other if is_num else other[2]),
                       self.w - (other if is_num else other[3]))

    def __rsub__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) - self.x,
                       (other if is_num else other[1]) - self.y,
                       (other if is_num else other[2]) - self.z,
                       (other if is_num else other[3]) - self.w)

    def __isub__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x -= other if is_num else other[0]
        self.y -= other if is_num else other[1]
        self.z -= other if is_num else other[2]
        self.w -= other if is_num else other[3]
        return self

    def __mul__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x * (other if is_num else other[0]),
                       self.y * (other if is_num else other[1]),
                       self.z * (other if is_num else other[2]),
                       self.w * (other if is_num else other[3]))

    def __rmul__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) * self.x,
                       (other if is_num else other[1]) * self.y,
                       (other if is_num else other[2]) * self.z,
                       (other if is_num else other[3]) * self.w)

    def __imul__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x *= other if is_num else other[0]
        self.y *= other if is_num else other[1]
        self.z *= other if is_num else other[2]
        self.w *= other if is_num else other[3]
        return self

    def __truediv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x / (other if is_num else other[0]),
                       self.y / (other if is_num else other[1]),
                       self.z / (other if is_num else other[2]),
                       self.w / (other if is_num else other[3]))

    def __rtruediv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) / self.x,
                       (other if is_num else other[1]) / self.y,
                       (other if is_num else other[2]) / self.z,
                       (other if is_num else other[3]) / self.w)

    def __itruediv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x /= other if is_num else other[0]
        self.y /= other if is_num else other[1]
        self.z /= other if is_num else other[2]
        self.w /= other if is_num else other[3]
        return self

    def __floordiv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x // (other if is_num else other[0]),
                       self.y // (other if is_num else other[1]),
                       self.z // (other if is_num else other[2]),
                       self.w // (other if is_num else other[3]))

    def __rfloordiv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) // self.x,
                       (other if is_num else other[1]) // self.y,
                       (other if is_num else other[2]) // self.z,
                       (other if is_num else other[3]) // self.w)

    def __ifloordiv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x //= other if is_num else other[0]
        self.y //= other if is_num else other[1]
        self.z //= other if is_num else other[2]
        self.w //= other if is_num else other[3]
        return self

    def __mod__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x % (other if is_num else other[0]),
                       self.y % (other if is_num else other[1]),
                       self.z % (other if is_num else other[2]),
                       self.w % (other if is_num else other[3]))

    def __rmod__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) % self.x,
                       (other if is_num else other[1]) % self.y,
                       (other if is_num else other[2]) % self.z,
                       (other if is_num else other[3]) % self.w)

    def __imod__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x %= other if is_num else other[0]
        self.y %= other if is_num else other[1]
        self.z %= other if is_num else other[2]
        self.w %= other if is_num else other[3]
        return self

    # endregion (vector math)

    # region COMPARISSON

    def __eq__(self, other: VectorN) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.x == other[0] and self.y == other[1] and self.z == other[2] and self.w == other[3]
        return False

    def __ne__(self, other: VectorN) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.x != other[0] or self.y != other[1] or self.z != other[2] or self.w != other[3]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 4

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        return getattr(self, 'xyzw'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        setattr(self, 'xyzw'[key], value)

    # endregion (container support)

    # region METHODS

    def todict(self, as_color: bool = False) -> Dict[str, float]:
        if as_color:
            return {'r': self.x, 'g': self.y, 'b': self.z, 'a': self.w}
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

    def fromdict(self, d: Dict[str, float]):
        self.x = float(d.get('x', 0.0))
        self.y = float(d.get('y', 0.0))
        self.z = float(d.get('z', 0.0))
        self.w = float(d.get('w', 0.0))

    def totuple(self) -> Tuple[Number, Number, Number, Number]:
        return self.x, self.y, self.z, self.w

    def tolist(self) -> List[Number]:
        return [self.x, self.y, self.z, self.w]

    # endregion (methods)


Vector4Ptr = POINTER(Vector4)


class Quaternion(Structure):
    """Same as Vector4"""
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
        ('w', c_float),
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0, z: Number = 0.0, w: Number = 0.0):
        super().__init__(x, y, z, w)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y}, {self.z}, {self.w})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union['Vector2', 'Vector3', 'Vector4', 'Quaternion', float]:
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: Vector2, 3: Vector3, 4: Quaternion}.get(len(attr))
        v = self.todict('r' in attr or 'g' in attr or 'b' in attr or 'a' in attr)
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: VectorN):
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        as_color = 'r' in attr or 'g' in attr or 'b' in attr or 'a' in attr
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                super(Quaternion, self).__setattr__(_RGBA_TO_XYZW[ch] if as_color else ch, value[i])
        else:
            if not is_number(value):
                raise ValueError(f"int or float expected, got {_clsname(value)}.")
            super(Quaternion, self).__setattr__(_RGBA_TO_XYZW[attr] if as_color else attr, float(value))

    # endregion (attribute swizzling)

    # region VECTOR MATH

    def __neg__(self) -> 'Quaternion':
        return Quaternion(-self.x, -self.y, -self.z, -self.w)

    def __abs__(self) -> 'Quaternion':
        return Quaternion(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

    def __round__(self, n=None) -> 'Quaternion':
        return Quaternion(round(self.x, n), round(self.y, n), round(self.z, n), round(self.w, n))

    def __add__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x + (other if is_num else other[0]),
                          self.y + (other if is_num else other[1]),
                          self.z + (other if is_num else other[2]),
                          self.w + (other if is_num else other[3]))

    def __radd__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) + self.x,
                          (other if is_num else other[1]) + self.y,
                          (other if is_num else other[2]) + self.z,
                          (other if is_num else other[3]) + self.w)

    def __iadd__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x += other if is_num else other[0]
        self.y += other if is_num else other[1]
        self.z += other if is_num else other[2]
        self.w += other if is_num else other[3]
        return self

    def __sub__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x - (other if is_num else other[0]),
                          self.y - (other if is_num else other[1]),
                          self.z - (other if is_num else other[2]),
                          self.w - (other if is_num else other[3]))

    def __rsub__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) - self.x,
                          (other if is_num else other[1]) - self.y,
                          (other if is_num else other[2]) - self.z,
                          (other if is_num else other[3]) - self.w)

    def __isub__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x -= other if is_num else other[0]
        self.y -= other if is_num else other[1]
        self.z -= other if is_num else other[2]
        self.w -= other if is_num else other[3]
        return self

    def __mul__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x * (other if is_num else other[0]),
                          self.y * (other if is_num else other[1]),
                          self.z * (other if is_num else other[2]),
                          self.w * (other if is_num else other[3]))

    def __rmul__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) * self.x,
                          (other if is_num else other[1]) * self.y,
                          (other if is_num else other[2]) * self.z,
                          (other if is_num else other[3]) * self.w)

    def __imul__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x *= other if is_num else other[0]
        self.y *= other if is_num else other[1]
        self.z *= other if is_num else other[2]
        self.w *= other if is_num else other[3]
        return self

    def __truediv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x / (other if is_num else other[0]),
                          self.y / (other if is_num else other[1]),
                          self.z / (other if is_num else other[2]),
                          self.w / (other if is_num else other[3]))

    def __rtruediv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) / self.x,
                          (other if is_num else other[1]) / self.y,
                          (other if is_num else other[2]) / self.z,
                          (other if is_num else other[3]) / self.w)

    def __itruediv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x /= other if is_num else other[0]
        self.y /= other if is_num else other[1]
        self.z /= other if is_num else other[2]
        self.w /= other if is_num else other[3]
        return self

    def __floordiv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x // (other if is_num else other[0]),
                          self.y // (other if is_num else other[1]),
                          self.z // (other if is_num else other[2]),
                          self.w // (other if is_num else other[3]))

    def __rfloordiv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) // self.x,
                          (other if is_num else other[1]) // self.y,
                          (other if is_num else other[2]) // self.z,
                          (other if is_num else other[3]) // self.w)

    def __ifloordiv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x //= other if is_num else other[0]
        self.y //= other if is_num else other[1]
        self.z //= other if is_num else other[2]
        self.w //= other if is_num else other[3]
        return self

    def __mod__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x % (other if is_num else other[0]),
                          self.y % (other if is_num else other[1]),
                          self.z % (other if is_num else other[2]),
                          self.w % (other if is_num else other[3]))

    def __rmod__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) % self.x,
                          (other if is_num else other[1]) % self.y,
                          (other if is_num else other[2]) % self.z,
                          (other if is_num else other[3]) % self.w)

    def __imod__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x %= other if is_num else other[0]
        self.y %= other if is_num else other[1]
        self.z %= other if is_num else other[2]
        self.w %= other if is_num else other[3]
        return self

    # endregion (vector math)

    # region COMPARISSON

    def __eq__(self, other: VectorN) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.x == other[0] and self.y == other[1] and self.z == other[2] and self.w == other[3]
        return False

    def __ne__(self, other: VectorN) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.x != other[0] or self.y != other[1] or self.z != other[2] or self.w != other[3]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 4

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        return getattr(self, 'xyzw'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        setattr(self, 'xyzw'[key], value)

    # endregion (container support)

    # region METHODS

    def todict(self, as_color: bool = False) -> Dict[str, float]:
        if as_color:
            return {'r': self.x, 'g': self.y, 'b': self.z, 'a': self.w}
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

    def fromdict(self, d: Dict[str, float]):
        self.x = float(d.get('x', 0.0))
        self.y = float(d.get('y', 0.0))
        self.z = float(d.get('z', 0.0))
        self.w = float(d.get('w', 0.0))

    def totuple(self) -> Tuple[Number, Number, Number, Number]:
        return self.x, self.y, self.z, self.w

    def tolist(self) -> List[Number]:
        return [self.x, self.y, self.z, self.w]

    # endregion (methods)


# endregion (vectors)


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

    # region CLASSMETHODS

    @classmethod
    def join(cls, col1: Vec4, col2: Vec4, col3: Vec4, col4: Vec4) -> 'Matrix':
        return cls(col1.x, col2.x, col3.x, col4.x,
                   col1.y, col2.y, col3.y, col4.y,
                   col1.z, col2.z, col3.z, col4.z,
                   col1.w, col2.w, col3.w, col4.w)

    @classmethod
    def diag(cls, value: float = 1.0) -> 'Matrix':
        return cls(value, 0.0, 0.0, 0.0,
                   0.0, value, 0.0, 0.0,
                   0.0, 0.0, value, 0.0,
                   0.0, 0.0, 0.0, value)

    # endregion (classmethods)

    def __init__(self,
                 m0: Number, m4: Number, m8: Number, m12: Number,
                 m1: Number, m5: Number, m9: Number, m13: Number,
                 m2: Number, m6: Number, m10: Number, m14: Number,
                 m3: Number, m7: Number, m11: Number, m15: Number):
        super().__init__(m0, m4, m8, m12,
                         m1, m5, m9, m13,
                         m2, m6, m10, m14,
                         m3, m7, m11, m15)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"\n[{self.column1}\n {self.column2}\n {self.column3}\n {self.column4}]"

    def __repr__(self) -> str:
        return (f"{_clsname(self)}("
                f"{self.m0}, {self.m1}, {self.m2}, {self.m3}, "
                f"{self.m4}, {self.m5}, {self.m6}, {self.m7}, "
                f"{self.m8}, {self.m9}, {self.m10}, {self.m11}, "
                f"{self.m12}, {self.m13}, {self.m14}, {self.m15})")

    # endregion (representation)

    # region PROPERTIES

    # region COLUMNS

    @property
    def column1(self) -> 'Quaternion':
        return Quaternion(self.m0, self.m1, self.m2, self.m3)

    @column1.setter
    def column1(self, value: Vec4):
        self.m0, self.m1, self.m2, self.m3 = value

    @property
    def column2(self) -> 'Quaternion':
        return Quaternion(self.m4, self.m5, self.m6, self.m7)

    @column2.setter
    def column2(self, value: Vec4):
        self.m4, self.m5, self.m6, self.m7 = value

    @property
    def column3(self) -> 'Quaternion':
        return Quaternion(self.m8, self.m9, self.m10, self.m11)

    @column3.setter
    def column3(self, value: Vec4):
        self.m8, self.m9, self.m10, self.m11 = value

    @property
    def column4(self) -> 'Quaternion':
        return Quaternion(self.m12, self.m13, self.m14, self.m15)

    @column4.setter
    def column4(self, value: Vec4):
        self.m12, self.m13, self.m14, self.m15 = value

    # endregion (columns)

    # region ROWS

    @property
    def row1(self) -> 'Quaternion':
        return Quaternion(self.m0, self.m4, self.m8, self.m12)

    @row1.setter
    def row1(self, value: Vec4):
        self.m0, self.m4, self.m8, self.m12 = value

    @property
    def row2(self) -> 'Quaternion':
        return Quaternion(self.m1, self.m5, self.m9, self.m13)

    @row2.setter
    def row2(self, value: Vec4):
        self.m1, self.m5, self.m9, self.m13 = value

    @property
    def row3(self) -> 'Quaternion':
        return Quaternion(self.m2, self.m6, self.m10, self.m14)

    @row3.setter
    def row3(self, value: Vec4):
        self.m2, self.m6, self.m10, self.m14 = value

    @property
    def row4(self) -> 'Quaternion':
        return Quaternion(self.m3, self.m7, self.m11, self.m15)

    @row4.setter
    def row4(self, value: Vec4):
        self.m3, self.m7, self.m11, self.m15 = value

    # endregion (rows)

    # endregion (properties)


MatrixPtr = POINTER(Matrix)


class Color(Structure):
    _fields_ = [
        ('r', c_ubyte),
        ('g', c_ubyte),
        ('b', c_ubyte),
        ('a', c_ubyte),
    ]

    def __init__(self, r: int = 0, g: int = 0, b: int = 0, a: int = 0):
        super().__init__(r, g, b, a)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.r}, {self.g}, {self.b}, {self.a})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.r}, {self.g}, {self.b}, {self.a})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union[int, Tuple[int, int], Tuple[int, int, int], 'Color']:
        m = _RGBA_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: tuple, 3: tuple, 4: Color}.get(len(attr))
        v = self.todict('r' in attr or 'g' in attr or 'b' in attr or 'a' in attr)
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: RGBA):
        m = _RGBA_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                if not is_component(value[i]):
                    raise ValueError(f"int expected in 0..255 range, got {_clsname(value[i])} ({value[i]}).")
                super(Color, self).__setattr__(ch, value[i])
        else:
            if not is_component(value):
                raise ValueError(f"int expected in 0..255 range, got {_clsname(value)} ({value}).")
            super(Color, self).__setattr__(attr, value)

    # endregion (attribute swizzling)

    # region COLOR MATH

    def __neg__(self, other: Union[int, RGBA]) -> 'Color':
        return Color(255 - self.r, 255 - self.g, 255 - self.b, self.a)

    def __add__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r + (other if is_num else other[0]),
                                  self.g + (other if is_num else other[1]),
                                  self.b + (other if is_num else other[2]),
                                  self.a))

    def __radd__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) + self.r,
                                  (other if is_num else other[1]) + self.g,
                                  (other if is_num else other[2]) + self.b,
                                  self.a))

    def __iadd__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r + (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g + (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b + (other if is_num else other[2]))
        return self

    def __sub__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r - (other if is_num else other[0]),
                                  self.g - (other if is_num else other[1]),
                                  self.b - (other if is_num else other[2]),
                                  self.a))

    def __rsub__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) - self.r,
                                  (other if is_num else other[1]) - self.g,
                                  (other if is_num else other[2]) - self.b,
                                  self.a))

    def __isub__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r - (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g - (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b - (other if is_num else other[2]))
        return self

    def __and__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r & (other if is_num else other[0]),
                                  self.g & (other if is_num else other[1]),
                                  self.b & (other if is_num else other[2]),
                                  self.a))

    def __rand__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) & self.r,
                                  (other if is_num else other[1]) & self.g,
                                  (other if is_num else other[2]) & self.b,
                                  self.a))

    def __iand__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r & (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g & (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b & (other if is_num else other[2]))
        return self

    def __or__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r | (other if is_num else other[0]),
                                  self.g | (other if is_num else other[1]),
                                  self.b | (other if is_num else other[2]),
                                  self.a))

    def __ror__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) | self.r,
                                  (other if is_num else other[1]) | self.g,
                                  (other if is_num else other[2]) | self.b,
                                  self.a))

    def __ior__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r | (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g | (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b | (other if is_num else other[2]))
        return self

    def __xor__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r ^ (other if is_num else other[0]),
                                  self.g ^ (other if is_num else other[1]),
                                  self.b ^ (other if is_num else other[2]),
                                  self.a))

    def __rxor__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) ^ self.r,
                                  (other if is_num else other[1]) ^ self.g,
                                  (other if is_num else other[2]) ^ self.b,
                                  self.a))

    def __ixor__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r ^ (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g ^ (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b ^ (other if is_num else other[2]))
        return self

    # endregion (color math)

    # region COMPARISSON

    def __eq__(self, other: RGBA) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.r == other[0] and self.g == other[1] and self.b == other[2]
        return False

    def __ne__(self, other: RGBA) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.r != other[0] or self.g != other[1] or self.b != other[2]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 4

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        return getattr(self, 'xyzw'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        setattr(self, 'xyzw'[key], value)

    # endregion (container support)

    # region METHODS

    # region UTILS

    def todict(self) -> Dict[str, int]:
        return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}

    def fromdict(self, d: Dict[str, int]):
        self.r = int(d.get('r', 0))
        self.g = int(d.get('g', 0))
        self.b = int(d.get('b', 0))
        self.a = int(d.get('a', 0))

    def totuple(self) -> Tuple[Number, Number, Number, Number]:
        return self.r, self.g, self.b, self.a

    def tolist(self) -> List[Number]:
        return [self.r, self.g, self.b, self.a]

    # endregion (utils)

    # region COLORSPACE CONVERSION

    def fade(self, alpha: float) -> 'Color':
        """Returns color with alpha applied, alpha goes from 0.0f to 1.0f"""
        return _rl.Fade(self, float(alpha))

    def to_int(self) -> int:
        """Returns hexadecimal value for a Color"""
        return _rl.ColorToInt(self)

    def normalize(self) -> Vector4:
        """Returns Color normalized as float [0..1]"""
        return _rl.ColorNormalize(self)

    @staticmethod
    def from_normalized(normalized: AnyVec4):
        """Returns Color from normalized values [0..1]"""
        return _rl.ColorFromNormalized(_vec4(normalized))

    def to_hsv(self) -> Vector3:
        """Returns HSV values for a Color, hue [0..360], saturation/value [0..1]"""
        return _rl.ColorToHSV(self)

    @staticmethod
    def from_hsv(hue: float, saturation: float, value: float) -> 'Color':
        """Returns a Color from HSV values, hue [0..360], saturation/value [0..1]"""
        return _rl.ColorFromHSV(float(hue), float(saturation), float(value))

    def color_alpha(self, alpha: float) -> 'Color':
        """Returns color with alpha applied, alpha goes from 0.0f to 1.0f"""
        return _rl.ColorAlpha(self, float(alpha))

    @staticmethod
    def color_alpha_blend(dst: AnyRGB, src: AnyRGB, tint: AnyRGB) -> 'Color':
        """Returns src alpha-blended into dst color with tint"""
        return _rl.ColorAlphaBlend(_color(dst), _color(src), _color(tint))

    @staticmethod
    def get_color(hex_value: int) -> 'Color':
        """Get Color structure from hexadecimal value"""
        return _rl.GetColor(int(hex_value))

    # endregion (colorspace conversion)

    # endregion (methods)


ColorPtr = POINTER(Color)


class Rectangle(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('width', c_float),
        ('height', c_float),
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0, width: Number = 0.0, height: Number = 0.0):
        super().__init__(x, y, width, height)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.width}, {self.height})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y}, {self.width}, {self.height})"

    # endregion

    # region PROPERTIES

    @property
    def left(self) -> float:
        return self.x

    @left.setter
    def left(self, value: Number):
        self.x = value

    @property
    def top(self) -> float:
        return self.y

    @top.setter
    def top(self, value: Number):
        self.y = value

    @property
    def right(self) -> float:
        return self.x + self.width

    @right.setter
    def right(self, value: Number):
        self.x = value - self.width

    @property
    def bottom(self) -> float:
        return self.y - self.height

    @bottom.setter
    def bottom(self, value: Number):
        self.y = value + self.height

    # endregion (properties)


RectanglePtr = POINTER(Rectangle)
RectanglePtrPtr = POINTER(RectanglePtr)


class Image(Structure):
    _fields_ = [
        ('data', c_void_p),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(file_name: str) -> 'Image':
        """Load image from file into CPU memory (RAM)"""
        return _rl.LoadImage(_str_in(file_name))

    @staticmethod
    def load_raw(file_name: str, width: int, height: int, format_: int, header_size: int) -> 'Image':
        """Load image from RAW file data"""
        return _rl.LoadImageRaw(_str_in(file_name), int(width), int(height), int(format_), int(header_size))

    @staticmethod
    def load_anim(file_name: str) -> Tuple['Image', int]:
        """Load image sequence from file (frames appended to image.data)"""
        frames = IntPtr(0)
        image = _rl.LoadImageAnim(_str_in(file_name), frames)
        return image, frames.contents

    @staticmethod
    def load_from_memory(file_type: str, file_data: bytes, data_size: int) -> 'Image':
        """Load image from memory buffer, fileType refers to extension: i.e. ".png"."""
        return _rl.LoadImageFromMemory(_str_in(file_type), file_data, int(data_size))

    @staticmethod
    def gen_plain_color(width: int, height: int, color: AnyRGB) -> 'Image':
        """Generate image: plain color"""
        return _rl.GenImageColor(int(width), int(height), _color(color))

    @staticmethod
    def gen_gradient_v(width: int, height: int, top: AnyRGB, bottom: AnyRGB) -> 'Image':
        """Generate image: vertical gradient"""
        return _rl.GenImageGradientV(int(width), int(height), _color(top), _color(bottom))

    @staticmethod
    def gen_gradient_h(width: int, height: int, left: AnyRGB, right: AnyRGB) -> 'Image':
        """Generate image: horizontal gradient"""
        return _rl.GenImageGradientH(int(width), int(height), _color(left), _color(right))

    @staticmethod
    def gen_gradient_radial(width: int, height: int, density: float, inner: AnyRGB, outer: AnyRGB) -> 'Image':
        """Generate image: radial gradient"""
        return _rl.GenImageGradientRadial(int(width), int(height), float(density), _color(inner), _color(outer))

    @staticmethod
    def gen_checked(width: int, height: int, checks_x: int, checks_y: int, col1: AnyRGB, col2: AnyRGB) -> 'Image':
        """Generate image: checked"""
        return _rl.GenImageChecked(int(width), int(height), int(checks_x), int(checks_y), _color(col1), _color(col2))

    @staticmethod
    def gen_white_noise(width: int, height: int, factor: float) -> 'Image':
        """Generate image: white noise"""
        return _rl.GenImageWhiteNoise(int(width), int(height), float(factor))

    @staticmethod
    def gen_perlin_noise(width: int, height: int, offset_x: int, offset_y: int, scale: float) -> 'Image':
        """Generate image: perlin noise"""
        return _rl.GenImagePerlinNoise(int(width), int(height), int(offset_x), int(offset_y), float(scale))

    @staticmethod
    def gen_cellular(width: int, height: int, tile_size: int) -> 'Image':
        """Generate image: cellular algorithm. Bigger tileSize means bigger cells"""
        return _rl.GenImageCellular(int(width), int(height), int(tile_size))

    @staticmethod
    def from_image(image: 'Image', rec: AnyRect) -> 'Image':
        """Create an image from another image piece"""
        return _rl.ImageFromImage(image, _rect(rec))

    @staticmethod
    def text(text: str, font_size: int, color: AnyRGB) -> 'Image':
        """Create an image from text (default font)"""
        return _rl.ImageText(_str_in(text), int(font_size), _color(color))

    @staticmethod
    def text_ex(font: 'Font', text: str, font_size: float, spacing: float, tint: AnyRGB) -> 'Image':
        """Create an image from text (custom sprite font)"""
        return _rl.ImageTextEx(font, _str_in(text), float(font_size), float(spacing), _color(tint))

    # endregion (classmethods)

    def __init__(self, data: VoidPtr, width: int, height: int, mipmaps: int, format_: int):
        super().__init__(data, width, height, mipmaps, format_)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.data}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.data}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"

    # endregion

    # region NO REFS

    def __del__(self) -> None:
        """Unload image from CPU memory (RAM)"""
        return _rl.UnloadImage(self)

    # endregion (no refs)

    # region METHODS

    def copy(self) -> 'Image':
        """Create an image duplicate (useful for transformations)"""
        return _rl.ImageCopy(self)

    def export_image(self, file_name: str) -> bool:
        """Export image data to file, returns true on success"""
        return _rl.ExportImage(self, _str_in(file_name))

    def export_image_as_code(self, file_name: str) -> bool:
        """Export image as code file defining an array of bytes, returns true on success"""
        return _rl.ExportImageAsCode(self, _str_in(file_name))

    # region MANIPULATION

    def format(self, new_format: int) -> None:
        """Convert image data to desired format"""
        return _rl.ImageFormat(byref(self), int(new_format))

    def to_pot(self, fill: AnyRGB) -> None:
        """Convert image to POT (power-of-two)"""
        return _rl.ImageToPOT(byref(self), _color(fill))

    def crop(self, crop: AnyRect) -> None:
        """Crop an image to a defined rectangle"""
        return _rl.ImageCrop(byref(self), _rect(crop))

    def alpha_crop(self, threshold: float) -> None:
        """Crop image depending on alpha value"""
        return _rl.ImageAlphaCrop(byref(self), float(threshold))

    def alpha_clear(self, color: AnyRGB, threshold: float) -> None:
        """Clear alpha channel to desired color"""
        return _rl.ImageAlphaClear(byref(self), _color(color), float(threshold))

    def alpha_mask(self, alpha_mask: 'Image') -> None:
        """Apply alpha mask to image"""
        return _rl.ImageAlphaMask(byref(self), alpha_mask)

    def alpha_premultiply(self) -> None:
        """Premultiply alpha channel"""
        return _rl.ImageAlphaPremultiply(byref(self))

    def resize(self, new_width: int, new_height: int) -> None:
        """Resize image (Bicubic scaling algorithm)"""
        return _rl.ImageResize(byref(self), int(new_width), int(new_height))

    def resize_nn(self, new_width: int, new_height: int) -> None:
        """Resize image (Nearest-Neighbor scaling algorithm)"""
        return _rl.ImageResizeNN(byref(self), int(new_width), int(new_height))

    def resize_canvas(self, new_width: int, new_height: int, offset_x: int, offset_y: int,
                      fill: AnyRGB) -> None:
        """Resize canvas and fill with color"""
        return _rl.ImageResizeCanvas(byref(self), int(new_width), int(new_height), int(offset_x), int(offset_y),
                                     _color(fill))

    def mipmaps(self) -> None:
        """Generate all mipmap levels for a provided image"""
        return _rl.ImageMipmaps(byref(self))

    def dither(self, r_bpp: int, g_bpp: int, b_bpp: int, a_bpp: int) -> None:
        """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
        return _rl.ImageDither(byref(self), int(r_bpp), int(g_bpp), int(b_bpp), int(a_bpp))

    def flip_vertical(self) -> None:
        """Flip image vertically"""
        return _rl.ImageFlipVertical(byref(self))

    def flip_horizontal(self) -> None:
        """Flip image horizontally"""
        return _rl.ImageFlipHorizontal(byref(self))

    def rotate_cw(self) -> None:
        """Rotate image clockwise 90deg"""
        return _rl.ImageRotateCW(byref(self))

    def rotate_ccw(self) -> None:
        """Rotate image counter-clockwise 90deg"""
        return _rl.ImageRotateCCW(byref(self))

    def color_tint(self, color: AnyRGB) -> None:
        """Modify image color: tint"""
        return _rl.ImageColorTint(byref(self), _color(color))

    def color_invert(self) -> None:
        """Modify image color: invert"""
        return _rl.ImageColorInvert(byref(self))

    def color_grayscale(self) -> None:
        """Modify image color: grayscale"""
        return _rl.ImageColorGrayscale(byref(self))

    def color_contrast(self, contrast: float) -> None:
        """Modify image color: contrast (-100 to 100)"""
        return _rl.ImageColorContrast(byref(self), float(contrast))

    def color_brightness(self, brightness: int) -> None:
        """Modify image color: brightness (-255 to 255)"""
        return _rl.ImageColorBrightness(byref(self), int(brightness))

    def color_replace(self, color: AnyRGB, replace: AnyRGB) -> None:
        """Modify image color: replace color"""
        return _rl.ImageColorReplace(byref(self), _color(color), _color(replace))

    def load_colors(self) -> Sequence[Color]:
        """Load color data from image as a Color array (RGBA - 32bit)"""
        result = _rl.LoadImageColors(self)
        colors = []
        i = 0
        while result[i] is not None:
            colors.append(result[i])
        return tuple(colors)

    def load_palette(self, max_palette_size: int) -> Sequence[Color]:
        """Load colors palette from image as a Color array (RGBA - 32bit)"""
        colors_count = IntPtr(0)
        result = _rl.LoadImagePalette(self, int(max_palette_size), colors_count)
        colors = [color for color in result[:colors_count.contents[0]]]
        return tuple(colors)

    @staticmethod
    def unload_colors(colors: Sequence[Color]) -> None:
        """Unload color data loaded with LoadImageColors()"""
        return _rl.UnloadImageColors(_arr(Color, colors))

    @staticmethod
    def unload_palette(colors: Sequence[Color]) -> None:
        """Unload colors palette loaded with LoadImagePalette()"""
        return _rl.UnloadImagePalette(_arr(Color, colors))

    def get_alpha_border(self, threshold: float) -> Rectangle:
        """Get image alpha border rectangle"""
        return _rl.GetImageAlphaBorder(self, float(threshold))

    # endregion (manipulation)

    # region DRAWING

    def clear_background(self, color: AnyRGB) -> None:
        """Clear image background with given color"""
        return _rl.ImageClearBackground(byref(self), _color(color))

    def draw_pixel(self, pos_x: int, pos_y: int, color: AnyRGB) -> None:
        """Draw pixel within an image"""
        return _rl.ImageDrawPixel(byref(self), int(pos_x), int(pos_y), _color(color))

    def draw_pixel_v(self, position: AnyVec2, color: AnyRGB) -> None:
        """Draw pixel within an image (Vector version)"""
        return _rl.ImageDrawPixelV(byref(self), _vec2(position), _color(color))

    def draw_line(self, start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: AnyRGB) -> None:
        """Draw line within an image"""
        return _rl.ImageDrawLine(byref(self), int(start_pos_x), int(start_pos_y), int(end_pos_x), int(end_pos_y),
                                 _color(color))

    def draw_line_v(self, start: AnyVec2, end: AnyVec2, color: AnyRGB) -> None:
        """Draw line within an image (Vector version)"""
        return _rl.ImageDrawLineV(byref(self), _vec2(start), _vec2(end), _color(color))

    def draw_circle(self, center_x: int, center_y: int, radius: int, color: AnyRGB) -> None:
        """Draw circle within an image"""
        return _rl.ImageDrawCircle(byref(self), int(center_x), int(center_y), int(radius), _color(color))

    def draw_circle_v(self, center: AnyVec2, radius: int, color: AnyRGB) -> None:
        """Draw circle within an image (Vector version)"""
        return _rl.ImageDrawCircleV(byref(self), _vec2(center), int(radius), _color(color))

    def draw_rectangle(self, pos_x: int, pos_y: int, width: int, height: int, color: AnyRGB) -> None:
        """Draw rectangle within an image"""
        return _rl.ImageDrawRectangle(byref(self), int(pos_x), int(pos_y), int(width), int(height), _color(color))

    def draw_rectangle_v(self, position: AnyVec2, size: AnyVec2, color: AnyRGB) -> None:
        """Draw rectangle within an image (Vector version)"""
        return _rl.ImageDrawRectangleV(byref(self), _vec2(position), _vec2(size), _color(color))

    def draw_rectangle_rec(self, rec: AnyRect, color: AnyRGB) -> None:
        """Draw rectangle within an image"""
        return _rl.ImageDrawRectangleRec(byref(self), _rect(rec), _color(color))

    def draw_rectangle_lines(self, rec: AnyRect, thick: int, color: AnyRGB) -> None:
        """Draw rectangle lines within an image"""
        return _rl.ImageDrawRectangleLines(byref(self), _rect(rec), int(thick), _color(color))

    def draw_image(self, src: 'Image', src_rec: AnyRect, dst_rec: AnyRect, tint: AnyRGB) -> None:
        """Draw a source image within a destination image (tint applied to source)"""
        return _rl.ImageDraw(byref(self), src, _rect(src_rec), _rect(dst_rec), _color(tint))

    def draw_text(self, text: str, pos_x: int, pos_y: int, font_size: int, color: AnyRGB) -> None:
        """Draw text (using default font) within an image (destination)"""
        return _rl.ImageDrawText(byref(self), _str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))

    def draw_text_ex(self, font: 'Font', text: str, position: AnyVec2, font_size: float, spacing: float,
                     tint: AnyRGB) -> None:
        """Draw text (custom sprite font) within an image (destination)"""
        return _rl.ImageDrawTextEx(byref(self), font, _str_in(text), _vec2(position), float(font_size), float(spacing),
                                   _color(tint))

    # endregion (drawing)

    # endregion (methods)


ImagePtr = POINTER(Image)


class Texture(Structure):
    _fields_ = [
        ('id', c_uint),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]

    def __init__(self, id: int, width: int, height: int, mipmaps: int, format_: int):
        super().__init__(id, width, height, mipmaps, format_)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.id}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.id}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"

    # endregion


TextureCubemap = Texture

# class TextureCubemap(Structure):
#     _fields_ = [
#         ('id', c_uint),
#         ('width', c_int),
#         ('height', c_int),
#         ('mipmaps', c_int),
#         ('format', c_int),
#     ]
#
#     def __init__(self, id: int, width: int, height: int, mipmaps: int, format_: int):
#         super().__init__(id, width, height, mipmaps, format_)
#
#     # region REPRESENTATION
#
#     def __str__(self) -> str:
#         return f"({self.id}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"
#
#     def __repr__(self) -> str:
#         return f"{_clsname(self)}({self.id}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"
#
#     # endregion

#
# class Texture2D(Structure):
#     _fields_ = [
#         ('id', c_uint),
#         ('width', c_int),
#         ('height', c_int),
#         ('mipmaps', c_int),
#         ('format', c_int),
#     ]
#
#     def __init__(self, id: int, width: int, height: int, mipmaps: int, format_: int):
#         super().__init__(id, width, height, mipmaps, format_)
#
#     # region REPRESENTATION
#
#     def __str__(self) -> str:
#         return f"({self.id}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"
#
#     def __repr__(self) -> str:
#         return f"{_clsname(self)}({self.id}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"
#
#     # endregion


Texture2D = Texture
Texture2DPtr = POINTER(Texture2D)


#
# class RenderTexture(Structure):
#     _fields_ = [
#         ('id', c_uint),
#         ('texture', Texture2D),
#         ('depth', Texture2D),
#     ]
#
#     def __init__(self, id: int, texture: Texture2D, depth: Texture2D):
#         super().__init__(id, texture, depth)
#
#     # region REPRESENTATION
#
#     def __str__(self) -> str:
#         return f"({self.id}, {self.texture}, {self.depth})"
#
#     def __repr__(self) -> str:
#         return f"{_clsname(self)}({self.id}, {self.texture}, {self.depth})"
#
#     # endregion


class RenderTexture2D(Structure):
    _fields_ = [
        ('id', c_uint),
        ('texture', Texture2D),
        ('depth', Texture2D),
    ]

    def __init__(self, id: int, texture: Texture2D, depth: Texture2D):
        super().__init__(id, texture, depth)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.id}, {self.texture}, {self.depth})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.id}, {self.texture}, {self.depth})"

    # endregion

    # region CONTEXT

    def __enter__(self):
        _rl.BeginTextureMode(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _rl.EndTextureMode()

    # endregion (context)


RenderTexture = RenderTexture2D


class NPatchInfo(Structure):
    _fields_ = [
        ('source', Rectangle),
        ('left', c_int),
        ('top', c_int),
        ('right', c_int),
        ('bottom', c_int),
        ('layout', c_int),
    ]

    def __init__(self, source: Rectangle, left: int, top: int, right: int, bottom: int, layout: int):
        super().__init__(source, left, top, right, bottom, layout)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.source}, {self.left}, {self.top}, {self.right}, {self.bottom}, {self.layout})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.source}, {self.left}, {self.top}, {self.right}, {self.bottom}, {self.layout})"

    # endregion


class CharInfo(Structure):
    _fields_ = [
        ('value', c_int),
        ('offsetX', c_int),
        ('offsetY', c_int),
        ('advanceX', c_int),
        ('image', Image),
    ]

    def __init__(self, value: int, offset_x: int, offset_y: int, advance_x: int, image: Image):
        super().__init__(value, offset_x, offset_y, advance_x, image)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.value}, {self.offsetX}, {self.offsetY}, {self.advanceX}, {self.image})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.value}, {self.offsetX}, {self.offsetY}, {self.advanceX}, {self.image})"

    # endregion


CharInfoPtr = POINTER(CharInfo)


class Font(Structure):
    _fields_ = [
        ('baseSize', c_int),
        ('charsCount', c_int),
        ('charsPadding', c_int),
        ('texture', Texture2D),
        ('recs', POINTER(Rectangle)),
        ('chars', POINTER(CharInfo)),
    ]

    # region CLASSMETHODS

    @staticmethod
    def get_default() -> 'Font':
        """Get the default Font"""
        return _rl.GetFontDefault()

    @staticmethod
    def load(file_name: str) -> 'Font':
        """Load font from file into GPU memory (VRAM)"""
        return _rl.LoadFont(_str_in(file_name))

    @staticmethod
    def load_ex(file_name: str, font_size: int, font_chars: str) -> 'Font':
        """Load font from file with extended parameters"""
        chars_count = [ord(ch) for ch in font_chars]
        chars = _arr(Int, chars_count)
        return _rl.LoadFontEx(_str_in(file_name), int(font_size), chars, chars_count)

    @staticmethod
    def load_from_image(image: Image, key: AnyRGB, first_char: int) -> 'Font':
        """Load font from Image (XNA style)"""
        return _rl.LoadFontFromImage(image, _color(key), int(first_char))

    @staticmethod
    def load_from_memory(file_type: str, file_data: bytes, font_size: int, font_chars: str) -> 'Font':
        """Load font from memory buffer, fileType refers to extension: i.e. ".ttf"."""
        chars_count = [ord(ch) for ch in font_chars]
        chars = _arr(Int, chars_count)
        return _rl.LoadFontFromMemory(_str_in(file_type), file_data, len(file_data), int(font_size), chars, chars_count)

    # endregion (classmethos)

    def __init__(self, base_size: int, chars_count: int, chars_padding: int, texture: int, image: Image,
                 recs: Sequence[Rectangle], chars: Sequence[CharInfo]):
        super().__init__(base_size, chars_count, chars_padding, texture, image, recs, chars)
        self._font_data: Optional[CharInfoPtr] = None
        self._chars_count: int = -1

    def __del__(self):
        return _rl.UnloadFont(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return (f"({self.baseSize}, {self.charsCount}, {self.charsPadding}, {self.texture}, {self.image}, {self.recs},"
                f" {self.chars})")

    def __repr__(self) -> str:
        return (f"{_clsname(self)}({self.baseSize}, {self.charsCount}, {self.charsPadding}, {self.texture},"
                f" {self.image}, {self.recs}, {self.chars})")

    # endregion

    # region METHODS

    def load_data(self, file_data: bytes, data_size: int, font_size: int, font_chars: str, type_: int) -> None:
        """Load font data for further use"""
        if self._font_data is None:
            chars_count = [ord(ch) for ch in font_chars]
            chars = _arr(Int, chars_count)
            self._chars_count = len(chars_count)
            self._font_data = _rl.LoadFontData(file_data, int(data_size), int(font_size), chars, self._chars_count,
                                               int(type_))

    def unload_data(self) -> None:
        """Unload font chars info data (RAM)"""
        if self._font_data is not None:
            _rl.UnloadFontData(self._font_data, self._chars_count)

    @staticmethod
    def gen_image_font_atlas(chars: Sequence[CharInfo], recs: Sequence[Sequence[Rectangle]], chars_count: int,
                             font_size: int, padding: int, pack_method: int) -> Image:
        """Generate image font atlas using chars info"""
        return _rl.GenImageFontAtlas(_arr(CharInfo, chars), _arr2(Rectangle, recs), int(chars_count), int(font_size),
                                     int(padding), int(pack_method))

    @staticmethod
    def draw_fps(pos_x: int, pos_y: int) -> None:
        """Draw current FPS"""
        return _rl.DrawFPS(int(pos_x), int(pos_y))

    @staticmethod
    def draw_text(text: str, pos_x: int, pos_y: int, font_size: int, color: AnyRGB) -> None:
        """Draw text (using default font)"""
        return _rl.DrawText(_str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))

    def draw_text_ex(self, text: str, position: AnyVec2, font_size: float, spacing: float, tint: AnyRGB) -> None:
        """Draw text using font and additional parameters"""
        return _rl.DrawTextEx(self, _str_in(text), _vec2(position), float(font_size), float(spacing), _color(tint))

    def draw_text_rec(self, text: str, rec: AnyRect, font_size: float, spacing: float, word_wrap: bool,
                      tint: AnyRGB) -> None:
        """Draw text using font inside rectangle limits"""
        return _rl.DrawTextRec(self, _str_in(text), _rect(rec), float(font_size), float(spacing), bool(word_wrap),
                               _color(tint))

    def draw_text_rec_ex(self, text: str, rec: AnyRect, font_size: float, spacing: float, word_wrap: bool,
                         tint: AnyRGB, select_start: int, select_length: int, select_tint: AnyRGB,
                         select_back_tint: AnyRGB) -> None:
        """Draw text using font inside rectangle limits with support for text selection"""
        return _rl.DrawTextRecEx(self, _str_in(text), _rect(rec), float(font_size), float(spacing), bool(word_wrap),
                                 _color(tint), int(select_start), int(select_length), _color(select_tint),
                                 _color(select_back_tint))

    def draw_text_codepoint(self, codepoint: int, position: AnyVec2, font_size: float, tint: AnyRGB) -> None:
        """Draw one character (codepoint)"""
        return _rl.DrawTextCodepoint(self, int(codepoint), _vec2(position), float(font_size), _color(tint))

    @staticmethod
    def measure_text(text: str, font_size: int) -> int:
        """Measure string width for default font"""
        return _rl.MeasureText(_str_in(text), int(font_size))

    def measure_text_ex(self, text: str, font_size: float, spacing: float) -> Vector2:
        """Measure string size for Font"""
        return _rl.MeasureTextEx(self, _str_in(text), float(font_size), float(spacing))

    def get_glyph_index(self, codepoint: int) -> int:
        """Get index position for a unicode character on font"""
        return _rl.GetGlyphIndex(self, int(codepoint))

    # endregion (methods)


SpriteFont = Font


# region CAMERAS


class Camera3D(Structure):
    _fields_ = [
        ('position', Vector3),
        ('target', Vector3),
        ('up', Vector3),
        ('fovy', c_float),
        ('projection', c_int),
    ]

    # region CLASSMETHODS

    @staticmethod
    def set_pan_control(key_pan: int) -> None:
        """Set camera pan key to combine with mouse movement (free camera)"""
        return _rl.SetCameraPanControl(int(key_pan))

    @staticmethod
    def set_alt_control(key_alt: int) -> None:
        """Set camera alt key to combine with mouse movement (free camera)"""
        return _rl.SetCameraAltControl(int(key_alt))

    @staticmethod
    def set_smooth_zoom_control(key_smooth_zoom: int) -> None:
        """Set camera smooth zoom key to combine with mouse (free camera)"""
        return _rl.SetCameraSmoothZoomControl(int(key_smooth_zoom))

    @staticmethod
    def set_move_controls(key_front: int, key_back: int, key_right: int, key_left: int, key_up: int,
                          key_down: int) -> None:
        """Set camera move controls (1st person and 3rd person cameras)"""
        return _rl.SetCameraMoveControls(int(key_front), int(key_back), int(key_right), int(key_left),
                                         int(key_up), int(key_down))

    # endregion (classmethods)

    def __init__(self, position: Optional[Vector3] = None, target: Optional[Vector3] = None,
                 up: Optional[Vector3] = None, fovy: float = 0.0, projection: int = 0):
        super().__init__(position if position else Vector3(), target if target else Vector3(),
                         up if up else Vector3(), fovy, projection)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.position}, {self.target}, {self.up}, {self.fovy}, {self.projection})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.position}, {self.target}, {self.up}, {self.fovy}, {self.projection})"

    # endregion

    # region CONTEXT

    def __enter__(self):
        _rl.BeginMode3D(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _rl.EndMode3D()

    # endregion (context)

    # region METHODS

    def set_mode(self, mode: int) -> None:
        """Set camera mode (multiple camera modes available)"""
        return _rl.SetCameraMode(self, int(mode))

    def update(self) -> None:
        """Update camera position for selected mode"""
        return _rl.UpdateCamera(byref(self))

    def get_matrix(self) -> Matrix:
        """Returns camera transform matrix (view matrix)"""
        return _rl.GetCameraMatrix(self)

    def get_world_to_screen(self, position: AnyVec3) -> Vector2:
        """Returns the screen space position for a 3d world space position"""
        return _rl.GetWorldToScreen(_vec3(position), self)

    def get_world_to_screen_ex(self, position: AnyVec3, width: int, height: int) -> Vector2:
        """Returns size position for a 3d world space position"""
        return _rl.GetWorldToScreenEx(_vec3(position), self, int(width), int(height))

    # endregion (methods)


#
# class Camera(Structure):
#     _fields_ = [
#         ('position', Vector3),
#         ('target', Vector3),
#         ('up', Vector3),
#         ('fovy', c_float),
#         ('projection', c_int),
#     ]
#
#     def __init__(self, position: Optional[Vector3] = None, target: Optional[Vector3] = None,
#                  up: Optional[Vector3] = None, fovy: float = 0.0, projection: int = 0):
#         super().__init__(position if position else Vector3(), target if target else Vector3(),
#                          up if up else Vector3(), fovy, projection)
#
#     # region REPRESENTATION
#
#     def __str__(self) -> str:
#         return f"({self.position}, {self.target}, {self.up}, {self.fovy}, {self.projection})"
#
#     def __repr__(self) -> str:
#         return f"{_clsname(self)}({self.position}, {self.target}, {self.up}, {self.fovy}, {self.projection})"
#
#     # endregion


Camera = Camera3D
Camera3DPtr = POINTER(Camera3D)
CameraPtr = Camera3DPtr


class Camera2D(Structure):
    _fields_ = [
        ('offset', Vector2),
        ('target', Vector2),
        ('rotation', c_float),
        ('zoom', c_float),
    ]

    def __init__(self, offset: Optional[Vector2] = None, target: Optional[Vector2] = None, rotation: float = 0.0,
                 zoom: float = 1.0):
        super().__init__(offset if offset else Vector2(), target if target else Vector2(), rotation, zoom)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.offset}, {self.target}, {self.rotation}, {self.zoom})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.offset}, {self.target}, {self.rotation}, {self.zoom})"

    # endregion

    # region CONTEXT

    def __enter__(self):
        _rl.BeginMode2D(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _rl.EndMode2D()

    # endregion (context)

    # region METHODS

    def get_matrix2d(self) -> Matrix:
        """Returns camera 2d transform matrix"""
        return _rl.GetCameraMatrix2D(self)

    def get_world_to_screen(self, position: AnyVec2) -> Vector2:
        """Returns the screen space position for a 2d camera world space position"""
        return _rl.GetWorldToScreen2D(_vec2(position), self)

    def get_screen_to_world(self, position: AnyVec2) -> Vector2:
        """Returns the world space position for a 2d camera screen space position"""
        return _rl.GetScreenToWorld2D(_vec2(position), self)

    # endregion (methods)


# endregion (cameras)


class Mesh(Structure):
    _fields_ = [
        ('vertexCount', c_int),
        ('triangleCount', c_int),

        # Default vertex data
        ('vertices', POINTER(c_float)),
        ('texcoords', POINTER(c_float)),
        ('texcoords2', POINTER(c_float)),
        ('normals', POINTER(c_float)),
        ('tangents', POINTER(c_float)),
        ('colors', POINTER(c_ubyte)),
        ('indices', POINTER(c_ushort)),

        # Animation vertex data
        ('animVertices', POINTER(c_float)),
        ('animNormals', POINTER(c_float)),
        ('boneIds', POINTER(c_int)),
        ('boneWeights', POINTER(c_float)),

        # OpenGL identifiers
        ('vaoId', c_uint),
        ('vboId', POINTER(c_uint)),
    ]

    def __init__(self, vertex_count: int, triangle_count: int, vertices: Sequence[float], texcoords: Sequence[float],
                 texcoords2: Sequence[float], normals: Sequence[float], tangents: Sequence[float],
                 colors: Sequence[int],
                 indices: Sequence[int], anim_vertices: Sequence[float], anim_normals: Sequence[float],
                 bone_ids: Sequence[int], bone_weights: Sequence[float], vao_id: int, vbo_id: IntPtr):
        super().__init__(vertex_count, triangle_count, _arr(c_float, vertices), _arr(c_float, texcoords),
                         _arr(c_float, texcoords2), _arr(c_float, normals), _arr(c_float, tangents),
                         _arr(c_ubyte, colors), _arr(c_ushort, indices), _arr(c_float, anim_vertices),
                         _arr(c_float, anim_normals), _arr(c_int, bone_ids), _arr(c_float, bone_weights), vao_id,
                         vbo_id)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.vertexCount}, {self.triangleCount}, {self.vaoId}, {self.vboId})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.vertexCount}, {self.triangleCount}, {self.vaoId}, {self.vboId})"

    # endregion


MeshPtr = POINTER(Mesh)


class Shader(Structure):
    _fields_ = [
        ('id', c_uint),
        ('locs', POINTER(c_int)),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(vs_file_name: str, fs_file_name: str) -> 'Shader':
        """Load shader from files and bind default locations"""
        return _rl.LoadShader(_str_in(vs_file_name), _str_in(fs_file_name))

    @staticmethod
    def load_from_memory(vs_code: str, fs_code: str) -> 'Shader':
        """Load shader from code strings and bind default locations"""
        return _rl.LoadShaderFromMemory(_str_in(vs_code), _str_in(fs_code))

    # endregion (classmethods)

    def __init__(self, id: int, locs: Sequence[int]):
        super().__init__(id, (c_int * len(locs))(*locs))

    def __del__(self):
        return _rl.UnloadShader(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.id}, {self.locs})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.id}, {self.locs})"

    # endregion

    # region CONTEXT

    def __enter__(self):
        _rl.BeginShaderMode(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _rl.EndShaderMode()

    # endregion (context)

    # region METHODS

    def get_location(self, uniform_name: str) -> int:
        """Get shader uniform location"""
        return _rl.GetShaderLocation(self, _str_in(uniform_name))

    def get_location_attrib(self, attrib_name: str) -> int:
        """Get shader attribute location"""
        return _rl.GetShaderLocationAttrib(self, _str_in(attrib_name))

    def set_value(self, loc_index: int, value: bytes, uniform_type: int) -> None:
        """Set shader uniform value"""
        return _rl.SetShaderValue(self, int(loc_index), value, int(uniform_type))

    def set_value_v(self, loc_index: int, value: bytes, uniform_type: int, count: int) -> None:
        """Set shader uniform value vector"""
        return _rl.SetShaderValueV(self, int(loc_index), value, int(uniform_type), int(count))

    def set_value_matrix(self, loc_index: int, mat: Matrix) -> None:
        """Set shader uniform value (matrix 4x4)"""
        return _rl.SetShaderValueMatrix(self, int(loc_index), mat)

    def set_value_texture(self, loc_index: int, texture: Texture2D) -> None:
        """Set shader uniform value for texture (sampler2d)"""
        return _rl.SetShaderValueTexture(self, int(loc_index), texture)

    # endregion (methods)


class MaterialMap(Structure):
    _fields_ = [
        ('texture', Texture2D),
        ('color', Color),
        ('value', c_float),
    ]

    def __init__(self, texture: int, color: Color, value: float):
        super().__init__(texture, color, value)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.texture}, {self.color}, {self.value})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.texture}, {self.color}, {self.value})"

    # endregion


class Material(Structure):
    _fields_ = [
        ('shader', Shader),
        ('maps', POINTER(MaterialMap)),
        ('params', c_float * 4),
    ]

    def __init__(self, shader: int, maps: Sequence[MaterialMap], params: Sequence[float]):
        n_params = len(params)
        if n_params > 4:
            raise ValueError(f"Expected up to 4 param values, got {n_params}.")
        super().__init__(shader, maps, (c_float * n_params)(*params))

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.shader}, {self.maps}, {self.params})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.shader}, {self.maps}, {self.params})"

    # endregion


MaterialPtr = POINTER(Material)


class Transform(Structure):
    _fields_ = [
        ('translation', Vector3),
        ('rotation', Quaternion),
        ('scale', Vector3),
    ]

    def __init__(self, translation: Vector3, rotation: Quaternion, scale: Vector3):
        super().__init__(translation, rotation, scale)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.translation}, {self.rotation}, {self.scale})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.translation}, {self.rotation}, {self.scale})"

    # endregion


class BoneInfo(Structure):
    _fields_ = [
        ('name', c_char * 32),
        ('parent', c_int),
    ]

    def __init__(self, name: str, parent: int):
        n = len(name)
        if n > 32:
            raise ValueError(f"name argument is more than 32 characters long ({n}).")
        super().__init__(_str_in(name), parent)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.name}, {self.parent})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.name}, {self.parent})"

    # endregion


class Model(Structure):
    _fields_ = [
        ('transform', Transform),

        ('meshCount', c_int),
        ('materialCount', c_int),
        ('meshes', POINTER(Mesh)),
        ('materials', POINTER(Material)),
        ('meshMaterial', POINTER(c_int)),

        ('boneCount', c_int),
        ('bones', POINTER(BoneInfo)),
        ('bindPose', POINTER(Transform)),
    ]

    def __init__(self, transform: Transform, mesh_count: int, material_count: int, meshes: Sequence[Mesh],
                 materials: Sequence[Material], mesh_material: Sequence[int], bone_count: int,
                 bones: Sequence[BoneInfo], bind_pose: Sequence[Transform]):
        mesh_array = Mesh * len(meshes)
        material_array = Material * len(materials)
        mesh_material_array = c_int * len(mesh_material)
        bone_array = BoneInfo * len(bones)
        transform_array = Transform * len(bind_pose)
        super().__init__(transform, mesh_count, material_count, mesh_array(*meshes), material_array(*materials),
                         mesh_material_array(*mesh_material), bone_count, bone_array(*bones),
                         transform_array(bind_pose))

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.transform}, {self.materialCount}, {self.bones}, {self.framePoses})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.transform}, {self.materialCount}, {self.bones}, {self.framePoses})"

    # endregion


ModelPtr = POINTER(Model)


class ModelAnimation(Structure):
    _fields_ = [
        ('boneCount', c_int),
        ('frameCount', c_int),
        ('bones', POINTER(BoneInfo)),
        ('framePoses', POINTER(POINTER(Transform))),
    ]

    def __init__(self, bone_count: Vector3, frame_count: Vector3, bones: Sequence[BoneInfo],
                 frame_poses: Sequence[Sequence[Transform]]):
        bone_array = BoneInfo * len(bones)
        transform_array = Transform * len(frame_poses[0])
        array_array = transform_array * len(frame_poses)
        super().__init__(bone_count, frame_count, bone_array(*bones), array_array(*frame_poses))

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.boneCount}, {self.frameCount}, {self.bones}, {self.framePoses})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.boneCount}, {self.frameCount}, {self.bones}, {self.framePoses})"

    # endregion


ModelAnimationPtr = POINTER(ModelAnimation)


class Ray(Structure):
    _fields_ = [
        ('position', Vector3),
        ('direction', Vector3),
    ]

    def __init__(self, position: Vector3, direction: Vector3):
        super().__init__(position, direction)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.position}, {self.direction})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.position}, {self.direction})"

    # endregion


class RayHitInfo(Structure):
    _fields_ = [
        ('hit', c_bool),
        ('distance', c_float),
        ('position', Vector3),
        ('normal', Vector3),
    ]


RayHitInfoPtr = POINTER(RayHitInfo)


class BoundingBox(Structure):
    _fields_ = [
        ('min', Vector3),
        ('max', Vector3),
    ]

    def __init__(self, min: Vector3, max: Vector3):
        super().__init__(min, max)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.min}, {self.max})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.min}, {self.max})"

    # endregion


class Wave(Structure):
    _fields_ = [
        ('sampleCount', c_uint),
        ('sampleRate', c_uint),
        ('SampleSize', c_uint),
        ('channels', c_uint),
        ('data', c_void_p),
    ]

    def __init__(self, sample_count: int, sample_rate: int, sample_size: int, channels: int, data: IntPtr):
        super().__init__(sample_count, sample_rate, sample_size, channels, data)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.sampleCount}, {self.sampleRate}, {self.SampleSize}, {self.channels})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.sampleCount}, {self.sampleRate}, {self.SampleSize}, {self.channels})"

    # endregion


WavePtr = POINTER(Wave)


class rAudioBuffer(Structure):
    pass


rAudioBufferPtr = POINTER(rAudioBuffer)


class AudioStream(Structure):
    _fields_ = [
        ('buffer', POINTER(rAudioBuffer)),

        ('sampleRate', c_uint),
        ('SampleSize', c_uint),
        ('channels', c_uint),
    ]

    def __init__(self, buffer: rAudioBufferPtr, sample_rate: int, sample_size: int, channels: int):
        super().__init__(buffer, sample_rate, sample_size, channels)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.sampleRate}, {self.SampleSize}, {self.channels})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.sampleRate}, {self.SampleSize}, {self.channels})"

    # endregion


class Sound(Structure):
    _fields_ = [
        ('stream', AudioStream),
        ('sampleCount', c_uint),
    ]

    def __init__(self, stream: AudioStream, sample_count: int):
        super().__init__(stream, sample_count)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.stream}, {self.sampleCount})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.stream}, {self.sampleCount})"

    # endregion


class Music(Structure):
    _fields_ = [
        ('stream', AudioStream),
        ('sampleCount', c_uint),
        ('looping', c_bool),

        ('ctxType', c_int),
        ('ctxData', c_void_p),
    ]

    def __init__(self, stream: AudioStream, sample_count: int, looping: bool, ctx_type: int, ctx_data: IntPtr):
        super().__init__(stream, sample_count, looping, ctx_type, ctx_data)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.stream}, {self.sampleCount}, {self.looping}, {self.ctxType})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.stream}, {self.sampleCount}, {self.looping}, {self.ctxType})"

    # endregion


MusicData = POINTER(Music)


class _VrDeviceInfo(Structure):
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


class _VrStereoConfig(Structure):
    _fields_ = [
        ('projection', Matrix * 2),
        ('viewOffset', Matrix * 2),
        ('leftLensCenter', c_float * 2),
        ('rightLensCenter', c_float * 2),
        ('leftScreenCenter', c_float * 2),
        ('rightScreenCenter', c_float * 2),
        ('scale', c_float * 2),
        ('scaleIn', c_float * 2),
    ]

# endregion (classes)
# ---------------------------------------------------------

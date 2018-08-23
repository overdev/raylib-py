raylibpy
========

**raylib is a simple and easy-to-use library to learn videogames programming. raylibpy
brings the all the strengths of this great library to Python, via ctypes binding.**

More about raylib can be found at its [repository](https://github.com/raisan5/raylib)
and/or [website](https://www.raylib.com).


## features
* **NO external dependencies**, all required libraries included with raylib.
* Multiple platforms supported: **Window, MacOS, Android... and many more!**
* Hardware accelerated with OpenGL (**1.1, 2.1, 3.3 or ES 2.0**)
* **Unique OpenGL abstraction layer** (usable as standalone module): rlgl
* Multiple Font formats supported (XNA fonts, AngelCode fonts, TTF)
* Outstanding texture formats support, including compressed formats (DXT, ETC, ASTC)
* **Full 3d support** for 3d Shapes, Models, Billboards, Heightmaps and more!
* Flexible Materials system, supports classic maps and **PBR maps**
* Shaders support, including Model shaders and Postprocessing shaders
* Audio loading and playing with streamming support (WAV, OGG, MP3, FLAC, XM, MOD)
* **VR stereo rendering** support with configurable HMD device parameters


## binaries

raylibpy comes by default with 32bit binaries for Windows (`libraylib_shared.dll`, mingw),
Linux (`libraylib.so.2.0.0`, i386) and MacOS (`libraylib.2.0.0.dylib`), but raylib have
other [binary releases](https://github.com/raisan5/raylib/releases) (win64, mingw or
msvc15 and linux amd64).

raylibpy will look for the respective binary in 3 locations:
* In the `RAYLIB_BIN_PATH` environment variable;
* in the directory where the `__main__` module is located, and
* in the raylibpy package directory.

`RAYLIB_LIB_PATH` accepts as value: `__main__`, as the entry point module directory; 
`__file__` as the package directory or another specific directory.

if `RAYLIB_BIN_PATH` is not set, it will look in the package directory first,
then in the `__main__` module location. Note though that `__main__` refers the module selected to
start the Python interpreter, not the `__main__.py` file, although it might be the case.

The binaries made available by raylib are all OpenGL 3.3. For OpenGL 1.1 or 2.1,
you can download the raylib source and build with the necessary changes in the Makefile.
More information on how to build raylib can be found in the [raylib wiki pages](https://github.com/raisan5/raylib/wiki).


## raylib vs raylibpy

Below are the differences in usage between raylib and raylibpy. Note, though that these
differences are being worked to make raylibpy as pythonic as possible, so changes may
occur without notification.

### Constant values

All C `#define`s got translated to Python 'constants'. Enums got translated to
Python [enums](https://docs.python.org/3/library/enum.html).

### Structures

#### In general

All structures inherit from `ctypes.Structure` class. At the moment, constructors
(except for vectors) require the exact argument types, so `int`s can't be passed
where `float`s are expected (although the argument can be omitted).

All structures have `__str__()` implemented, so they have a very basic textual representation:
```python
# Define the camera to look into our 3d world
>>> camera = Camera()
>>> camera.position = Vector3(5., 4., 5.)
>>> camera.target = Vector3(0., 2., 0.)
>>> camera.up = Vector3(0., 1., 0.)
>>> camera.fovy = 45.0
>>> camera.type = CAMERA_PERSPECTIVE
>>> camera
"(CAMERA3D: position: (5.0, 4.0, 5.0), target: (0.0, 2.0, 0.0), up: (0.0, 1.0, 0.0), fovy: 45.0°, type: PERSPECTIVE)"
```
Not all information is exposed, though. Mesh objects, for example, exposes only the
vertex and triangle count attributes.


#### Vectors

Vector2, Vector3 and Vector4 support basic aritmetic operations: addiction, subtraction,
multiplication (incluiding scalar multiplication), division and modulo. Augmented
assignment is also supported; the right hand side operand can be any sequence of same
number of components:

```python
vec_a = Vector3(3., 5., 7.)
vec_b = Vector3(4., 2., 0.)
vec_a * vec_b           # outputs (12.0, 10.0, 0.0)
vec_a + (8, 100, -1)    # outputs (11.0, 105.0, 6.0)
vec_a %= 2              # augmented assignment (modulo)
vec_a                   # outputs (1.0, 1.0, 0.0)
```

Vectors also support GLSL vector swizzling. Also, `x`, `y`, `z` and `w` coordinates maps to
normalized color values (`r`, `g`, `b` and `a`; only for `Vector3` and `Vector4`) and
texture coordinates (`u` and `v`):

```python
# Reading (__getattr__)
vec3 = Vector3(123.0, 467.0, 789.0)
vec2 = vec3.uv      # x and y respectively as u and v
vec3 = vec3.bgr     # x, y and z respectively as r, g and b ( rgb is not available in Vector 2)
vec4 = vec2.rrrg     # for attribute reading, is ok to repeat components


# Writing (__setattr__)
vec3 = Vector3(123.0, 467.0, 789.0)
vec4.yxwz = 10, 0, -1, vec3.z         # sequences of ints and/or floats are accepted as value
vec2.vu = vec3.xy                       # x and y respectively as u and v
vec3.bgr = 12, vec4.x                 # x, y and z respectively as r, g and b ( rgb is not available in Vector 2)

# the following raises an exception:
vec3.rrr = vec4.yxw     # for attribute writing, is _not_ ok to repeat components
vec2.br = vec4.uv       # r, g and b is not available in Vector2
vec4.brxy = (0., 0., vec2.x, vec3.z)       # can't mix component name groups (rgba, xywz and uv)
```

Constructors and swizzled attributes now accept any combination of numbers,
vectors and sequences, as long as the total number of arguments are preserved:
```python
# all these results in the same Vector4
a = Vector4(3, 4, 5, 6)
b = Vector4(a.xy, 5, 6)
c = Vector4(b.x, b.yz, b.w)
d = Vector4(c.x, c.y, c.zw)
e = Vector4(d.xy, d.zw)
f = Vector4(e.xyz, 6)
g = Vector4(f.x, f.yzw)
h = Vector4(g)
```

Setting attributes also works:

```python
a = Vector4(Vector2(10, 0), 100, 20)
b = Vector4.zero()
b.rgba = 0.0, vec4.rg, 1.0
a.xyzw = (10, b.uv), 1.0
```

This became available by dropping a previous feature wich allowed for a very basic
swizzling emulation. A feature more similas to GLSL vectors is implemented on
top of Python container emulation magic functions:

```python
vec = Vector4(0., 1., 2., 3.)

# __len__()
print(len(vec))     # outputs 4

# __iter__()
for comp in v:
    print(comp)     # iterates on Vector4 components

# __getitem__()
x = vec[0]      # key as int
y = vec['y']    # key as str
zw = vec[2:]    # key as slice; returns a List[float]

# __setitem__()
vec[0] = 10
vec['y'] = 20
# vec[2:] = zw      # <--- not supported; will raise TypeError
```

## extras

raylibpy has the extra module [`easings`](https://github.com/overdev/raylibpy/blob/master/raylibpy/easings.py) for animations.

The current plan it to translate [rayGui](https://github.com/raysan5/raygui) and add it too.

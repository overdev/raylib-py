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

### Constant values

All C `#define`s and `enum`s got translated to Python 'constants'. Enums may, in the future,
be converted to Python [enums](https://docs.python.org/3/library/enum.html), if
`ctypes` allows it.

### Structures

#### In general

All structures inherit from `ctypes.Structure` class. Unlike functions, constructors require
the exact argument types, so `int`s can't be passed where `float`s are expected (although the
argument can be omitted):

```python
# ways of creating a Vector3 instance:
vec_a = Vector3()
vec_b = Vector3(0., 1., 0.)
vec_c = Vector3.one()

# the following will raise an exception:
vec_d = Vector3(10, 0, 100)
```

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
>>> vec_a = Vector3(3., 5., 7.)
>>> vec_b = Vector3(4., 2., 0.)
>>> vec_a * vec_b
"(12.0, 10.0, 0.0)"
>>> vec_a + (8, 100, -1)
"(11.0, 105.0, 6.0)"
>>> vec_a %= 2
>>> vec_a
"(1.0, 1.0, 1.0)"
```

Vectors have also a feature that tries to emulate the GLSL vector swizzling, but
its done through subscription:
```python
>>> vec_a = Vector4(10.0, 20.0, 50.0, 1.0)
>>> # create a Vector2 from it:
...
>>> vec_b = vec_a['xy']
>>> vec_b
"(10.0, 20.0)"
>>> # create a Vector3 from it, setting 1.0 to the z axis:
...
>>> vec_c = vec_b['xy1']
>>> vec_c
"(10.0, 20.0, 0.0)"
>>> # another Vector2, perpendicular to vec_b:
...
>>> vec_d = vec_b['Yx']
>>> vec_d
"(-20.0, 10.0)"
>>> # a Vector4 from the y axis:
...
>>> vec_e = vec_b['yyyy']
>>> # vec_d with signs flipped:
...
>>> vec_d['XY']
"(20.0, -10.0)"
>>> # moving vec_a in the y axis by one:
...
>>> vec_a += vec_a['0010']
```
That's not all! Other component-wise operations (or tricks) can be made this way (note,
though that these operators apply in positional fashion):
```python
>>> vec_a = Vector3(-10.0, 20.5, 15.840)
>>> # divide all components by 2:
...
>>> vec_a['///']
"(-5.0, 10.25, 7.920)"
>>>
>>>
>>> # multiply all components by 2:
...
>>> vec_a['***']
"(-20.0, 41.0, 31.680)"
>>>
>>>
>>> # all components raised to the power of 2:
...
>>> vec_a['^^^']
"(-1e-10, 7.779544182561597e+26, 1.0095364584490473e+19)"
>>>
>>>
>>> # inverse of all components (1/x):
...
>>> vec_a['...']
"(-0.1, 0.04878048780487805, 0.06313131313131314)"
>>>
>>>
>>> # sign of components (-1 if < 0, 1 if > 0, 0 otherwise):
...
>>> vec_a['+++']
"(-1.0, 1.0, 1.0)"
>>>
>>>
>>> # nonzero components (1 if != 0, 0 otherwise):
...
>>> vec_a['???']
"(1.0, 1.0, 1.0)"
>>>
>>>
>>> # the component of vec_a with largest value:
...
>>> vec_a['>>>']
"(15.840, 15.840, 15.840)"
>>>
>>>
>>> # the component of vec_a with smallest value:
...
>>> vec_a['<<<']
"(-10.0, -10.0, -10.0)"
>>>
>>>
>>> # component values rounded:
...
>>> vec_a['###']
"(-10.0, 20.0, 15.0)"
>>>
>>>
>>> # fractional part of component values:
...
>>> vec_a['%%%']
"(0.0, 0.5, 0.840)"
```


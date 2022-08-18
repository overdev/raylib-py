# DISCONTINUED: please, refer to <a href="https://github.com/overdev/raylibpyctbg">raylibpyctbgh</a> for a possibly better alternative</h1>

<img align="left" src="https://github.com/overdev/raylib-py/blob/master/logo/raylib-py_256x256.png" width=256>

# raylib-py

[![Downloads](https://pepy.tech/badge/raylib-py)](https://pepy.tech/project/raylib-py)
[![Downloads](https://pepy.tech/badge/raylib-py/month)](https://pepy.tech/project/raylib-py)
A python binding for the great _C_ library **[raylib](https://github.com/raysan5/raylib)**.

## Getting Started
<!--
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
-->
### Prerequisites

_raylib-py_ uses type [annotations](https://www.python.org/dev/peps/pep-3107/#id30) in its source, so a Python version that supports it is required.

Some Python versions may not have [enum](https://pypi.org/project/enum/) and/or [typings](https://pypi.org/project/typing/) modules as part of the standard library, wich are required. These are installed automatically by pip.

### Installing

The easiest way to install _raylib-py_ is by the pip install command:

Depending on you system and python version(s) installed, the command might be:

```
pip install raylib-py
```

or

```
python -m pip install raylib-py
```

or (with Python3.7 launcher with multiple versions installed)

```
py-3.x-32 -m pip install raylib-py
```

> Note that the minimum Python version tested is 3.4. Please, let me know if you're able to run it in Python33.

_raylib-py_ comes with 32bit binaries for Windows, Mac and Linux, but you're not required to use these. If you have a custom _raylib_ _**dll**_, _**dylib**_ or _**so**_ binary, make sure to set a PATH indicating the directory it is located:

```python
import os

# set the path before raylib is imported.
os.environ["RAYLIB_BIN_PATH"] = "path/to/the/binary"

import raylibpy

# let the fun begin.
```

You can set `"__file__"` as value to `"RAYLIB_BIN_PATH"` and _raylib-py_ will search for the binary in the package dir:

```python
# bynary file is wherever the package is located.
os.environ["RAYLIB_BIN_PATH"] = "__file__"
```

`"__main__"` can also be set to look for the binary in the project's directory where the starting script is located:

```python
# binary file is in the same dir as this py file.
os.environ["RAYLIB_BIN_PATH"] = "__main__"

# ...

if __name__ == "__main__":
    # run the game
    # ...
```

> Make sure the bin file name for the respective platform is `libraylib_shared.dll`, `libraylib.2.0.0.dylib` or `libraylib.so.2.0.0`.

## Tests

_raylib-py_ does not have test code, but you can run the examples in the [examples directory](https://github.com/overdev/raylib-py/tree/master/examples).

<!--
### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

-->

## _raylib_ vs _raylib-py_

Below are the differences in usage between _raylib_ and _raylib-py_. Note, though that these differences are being worked to make _raylib-py_ as pythonic as possible, so changes may occur without notification.

### Constant values

All C `#define`s got translated to Python 'constants'. Enums got translated to
Python [enums](https://docs.python.org/3/library/enum.html).

### Structures

In general, all structures inherit from `ctypes.Structure` class. At the moment, constructors
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
vec_a * vec_b                   # outputs (12.0, 10.0, 0.0)
vec_a + (8, 100, -1)            # outputs (11.0, 105.0, 6.0)
vec_a %= 2                      # augmented assignment (modulo)
vec_a                           # outputs (1.0, 1.0, 0.0)
```

Vectors also support GLSL vector swizzling. Also, `x`, `y`, `z` and `w` coordinates maps to
normalized color values (`r`, `g`, `b` and `a`; only for `Vector3` and `Vector4`) and
texture coordinates (`u` and `v`):

```python
# Reading (__getattr__)
vec3 = Vector3(123.0, 467.0, 789.0)
vec2 = vec3.uv       # x and y respectively as u and v
vec3 = vec3.bgr      # x, y and z respectively as r, g and b ( rgb is not available in Vector 2)
vec4 = vec2.rrrg     # for attribute reading, is ok to repeat components

# Writing (__setattr__)
vec3 = Vector3(123.0, 467.0, 789.0)
vec4.yxwz = 10, 0, -1, vec3.z           # sequences of ints and/or floats are accepted as value
vec2.vu = vec3.xy                       # x and y respectively as u and v
vec3.bgr = 12, vec4.x                   # x, y and z respectively as r, g and b ( rgb is not available in Vector 2)

# the following raises an exception:
vec3.rrr = vec4.yxw                         # for attribute writing, is _not_ ok to repeat components
vec2.br = vec4.uv                           # r, g and b is not available in Vector2
vec4.brxy = (0., 0., vec2.x, vec3.z)        # can't mix component name groups (rgba, xywz and uv)
```

Constructors and swizzled attributes now accept any combination of numbers,
vectors and sequences, as long as the total number of arguments are preserved:
```python
# all these results in the same Vector4
a = Vector4(3, 4, 5, 6)
b = Vector4(a.xy, 5, 6)
c = Vector4(b.x, b.yz, 6)
d = Vector4(3, c.y, c.zw)
e = Vector4(d.xy, (5, 6))
f = Vector4(e.xyz, 6)
g = Vector4(3, f.yzw)
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
swizzling emulation. A feature more similar to GLSL vectors is implemented on
top of Python container emulation magic functions:

```python
vec = Vector4(0., 1., 2., 3.)

# __len__()
print(len(vec))     # outputs 4

# __iter__()
for comp in vec:
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

## Additional (feature) draw function: `draw_texture_npatch`

The custom DLL installed by _raylib-py_ includes an not yet official drawing function and
corresponding `NPatchInfo` helper structure:

```python
# draws an 3-patch (vertical, or horizontal) or 9-patch textured that stretches and
# shrinks nicely.
# Seq means any sequence type
def draw_texture_npatch(texture: Texture2D, npatch_info: NPatchInfo,
                        dest_rec: Union[Rectangle, Seq], origin: Union[Vector2, Seq],
                        rotation: float, tint: Union[Color, Seq]) -> None:
```

At the moment (after _raylib_ v2.0.0), only the x86 custom DLL contains this function
and, to enabled it, an specific `os.environ` key must be set:

```python
# set this before importing raylibpy (the value does not matter as long is a str type)
os.environ['ENABLE_V2_0_0_FEATURE_DRAWTEXTURENPATCH'] = '1'
```

## Building _raylib_ from source

_raylib_ wiki pages contains information on how to build it on [Windows](https://github.com/raysan5/raylib/wiki/Working-on-Windows), [Mac](https://github.com/raysan5/raylib/wiki/Working-on-macOS), [Linux](https://github.com/raysan5/raylib/wiki/Working-on-GNU-Linux) and other platforms.

## Contributing

Please, let me know if you find any strange or unexpected behavior while using _raylib-py_. If you want to [request features](https://github.com/raysan5/raylib/pulls) or [report bugs](https://github.com/raysan5/raylib/issues) related to the library (in contrast to this binding), please refer to the [author's project repo](https://github.com/raysan5/raylib).

## Authors

* **Ramon Santamaria** - *raylib's author* - [raysan5](https://github.com/raysan5)
* **Jorge A. Gomes** - *python binding code* - [overdev](https://github.com/overdev)

See also the list of [contributors](https://github.com/raysan5/raylib/graphs/contributors) who participated in this project.

## License

_raylib-py_ (and _raylib_) is licensed under an unmodified zlib/libpng license, which is an OSI-certified, BSD-like license that allows static linking with closed source software.

<!--
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->


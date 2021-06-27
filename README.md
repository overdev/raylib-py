> # WIP: Updating raylib-py to the latest raylib release, version 3.7

<img align="left" src="logo/raylib-py_256x256.png" width=256>

# raylib-py

[![Downloads](https://pepy.tech/badge/raylib-py)](https://pepy.tech/project/raylib-py)
[![Downloads](https://pepy.tech/badge/raylib-py/month)](https://pepy.tech/project/raylib-py)
A python binding for the great _C_ library **[raylib](https://github.com/raysan5/raylib)**.

## Getting Started

<!--
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
-->

### About this version

If you were using the previous version of _raylib-py_, that code might not work with this version before some tweaks are
made. The previous version wraps raylib 2.0; this one wraps version 3.7. There is a lot of new things and changes in the
API.

### Prerequisites

_raylib-py_ uses type [annotations](https://www.python.org/dev/peps/pep-3107/#id30) in its source, so a Python version
that supports it is required.

Some Python versions may not have [enum](https://pypi.org/project/enum/)
and/or [typings](https://pypi.org/project/typing/) modules as part of the standard library, which are required. These are
installed automatically by pip.

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

or (with Python3.7+ launcher with multiple versions installed)

```
py-3.x-32 -m pip install raylib-py
```

> Note that the minimum Python version tested is 3.4. Please, let me know if you're able to run it in Python33.

_raylib-py_ comes with 32bit binaries for Windows, Mac and Linux, but you're not required to use these.
If you have an existing _raylib_ _**dll**_, _**dylib**_ or _**so**_ binary, you can set the environment variable
"USE_EXTERNAL_RAYLIB" to any value (it just has to exist) and _raylib-py_ will fallback to using your operating
sytems mechanism of loading libraries.

```python
import os

# specify that we should load raylib from the system instead
os.environ["USE_EXTERNAL_RAYLIB"] = True

import raylibpy

# let the fun begin.
```

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

### Classes

All classes have `__str__()` implemented, so they have a very basic textual representation:
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

Vector2, Vector3 and Vector4 support the operators `==`, `!=` (both componet-wise length and value comparisson), `+`
, `-` (negation and subtraction), `*`, `/`, `//`, `%` for vectors and scalars. They can also be `abs()`*ed*
and `round()`*ed*. Augmented assignment and inverse order is also supported; the other operand can be any sequence of
length:

```python
vec_a = Vector3(3., 5., 7.)
vec_b = Vector3(4., 2., 0.)
vec_a * vec_b                   # outputs (12.0, 10.0, 0.0)
vec_a + (8, 100, -1)            # outputs (11.0, 105.0, 6.0)
vec_a %= 2                      # augmented assignment (modulo)
vec_a  # outputs (1.0, 1.0, 0.0)
vec_a == (1.0, 1.0, 0.0)  # outputs True
```

Vectors also support GLSL vector swizzling. Also, `Vector3` and `Vector4` coordinates
`x`, `y`, `z` and `w` coordinates maps to normalized color values (`r`, `g`, `b` and `a`):

```python
# Reading (__getattr__)
vec3 = Vector3(123.0, 467.0, 789.0)
vec3 = vec3.bgr      # x, y and z respectively as r, g and b ( rgb is not available in Vector 2)
vec4 = vec2.rrrg     # for attribute reading, is ok to repeat components

# Writing (__setattr__)
vec3 = Vector3(123.0, 467.0, 789.0)
vec4.yxwz = 10, 0, -1, vec3.z           # sequences of ints and/or floats are accepted as value
vec3.bgr = 12, vec4.x                   # x, y and z respectively as r, g and b ( rgb is not available in Vector 2)

# the following raises an exception:
vec3.rrr = vec4.yxw                         # for attribute writing, is _not_ ok to repeat components
vec4.brxy = (0., 0., vec2.x, vec3.z)        # can't mix component name groups (rgba, xywz and uv)
```

Constructors and swizzled attributes now accept any combination of numbers,
vectors and sequences, as long as the total number of arguments are preserved:
> Currently, this feature for constructors is yet to be implemented.
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

Vectors can be used as sequences:

```python
vec = Vector4(0., 1., 2., 3.)

# __len__()
print(len(vec))     # outputs 4

# __iter__()
for comp in vec:
    print(comp)     # iterates on Vector4 components

# __getitem__()
x = vec[0]  # key as int only

# __setitem__()
vec[0] = 10
vec['y'] = 20
# vec[2:] = zw      # <--- not supported; will raise TypeError
```

### _Pythonic_ and _Spartan_ "flavors"

In raylib-py a more OOP wrapper was added, so some classes have methods that wraps functions, like Image, for example.
This is the `raylibpy.pythonic` module.

> It is recommended to import either the spartan or pythonic to avoid unexpected
> behavior between classes of both modules (`spartan.Image is pythonic.Image`
> evaluates to `False`).

```python
from raylibpy.spartan import *
from raylibpy.colors import *
from raylibpy.consts import *
```

The `raylibpy.spartan` module follows the _C_ raylib style (structs, functions, callbacks and constants).

### Context Managers

Some raylib functions are called in pairs to begin and end some specific modes. A context manager version of these
functions are provided for a more practical entering/leaving of these modes:

```python
# Draw
# ---------------------------------------------------------------------------------
with drawing():
    clear_background(RAYWHITE)

    with mode3d(camera):
        if collision:
    # ...
```

Better than:

```python
# Draw
# ---------------------------------------------------------------------------------
begin_drawing()
clear_background(RAYWHITE)

begin_mode3d(camera)
if collision:
# ...

end_mode3d()
end_drawing()
```

In `raylibpy.pythonic`, some classes are also context managers:

```python
# Draw
# ---------------------------------------------------------------------------------
with drawing():
    clear_background(RAYWHITE)

    with camera:
        if collision:
    # ...

```

> `raylib.pythonic` is a work in progress. Currently, only `raylibpy.spartan` is
> fully wrapped.

## Building _raylib_ from source

_raylib_ wiki pages contains information on how to build it
on [Windows](https://github.com/raysan5/raylib/wiki/Working-on-Windows)
, [Mac](https://github.com/raysan5/raylib/wiki/Working-on-macOS)
, [Linux](https://github.com/raysan5/raylib/wiki/Working-on-GNU-Linux) and other platforms.

## Contributing

Please, let me know if you find any strange or unexpected behavior while using _raylib-py_. If you want
to [request features](https://github.com/raysan5/raylib/pulls)
or [report bugs](https://github.com/raysan5/raylib/issues) related to the library (in contrast to this binding), please
refer to the [author's project repo](https://github.com/raysan5/raylib).

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

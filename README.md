raylibpy
========

**raylib is a simple and easy-to-use library to learn videogames programming. raylibpy
brings the all the strengths of this great library to Python, via ctypes binding.**

More about raylib can be found at its [repository](https://github.com/raisan5/raylib)
and/or [website](https://www.raylib.com).


##features
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

Except for the naming conventions and data types (names and convertions), theres no 
significative differences between raylib and raylibpy. At the moment, only bytes
are accepted as string arguments, no implicit convertion is made between integers and
floats. Some of the refinements to be done are exposed below:

| Expects or returns | Accepts/returns only | Will accept/return |
| ------- | ------- | ------- |
| `const char *` | `bytes` (ASCII) | `str` (unicode) |
| `const char **` | `CharPtrPtr` | `List[str]` |
| `int` | `int` | `float` |
| `float` | `float` | `int` |
| `int*` as argument | `IntPtr` as argument | `int` as return, if omitted as argument |
| `Vector3` | `Vector3` | `Tuple[float, float, float]` or `List[float]` |
| `Vector3 *` | `Vector3Ptr` as `byref(instance)` | array, sequence or `bytes` |


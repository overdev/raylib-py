

<img align="left" src="https://github.com/overdev/raylib-py/blob/master/logo/raylib-py_256x256.png" width=256>

# raylib-py

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/raylib-py?style=plastic)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/overdev/raylib-py?style=plastic)
![GitHub Release Date](https://img.shields.io/github/release-date/overdev/raylib-py?style=plastic)

![PyPI - Wheel](https://img.shields.io/pypi/wheel/raylib-py?style=plastic)
![PyPI - License](https://img.shields.io/pypi/l/raylib-py?style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dd/raylib-py?label=PyPI%20Downloads&style=plastic)

![GitHub all releases](https://img.shields.io/github/downloads/overdev/raylib-py/total?style=plastic)
![GitHub release (by tag)](https://img.shields.io/github/downloads/overdev/raylib-py/v6.2.0/total?style=plastic)
![GitHub forks](https://img.shields.io/github/forks/overdev/raylib-py?style=social)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/overdev/raylib-py?style=plastic)
![GitHub commits since tagged version](https://img.shields.io/github/commits-since/overdev/raylib-py/v6.2.0?style=plastic)

A python binding for the great _C_ library **[raylib](https://github.com/raysan5/raylib)**.


## How to install:

From PyPI, in the CLI:

```
$ pip install raylib-py
```

You can also download the wheel from the [releases](https://github.com/overdev/raylib-py/releases) page and install it with pip locally:

```
$ pip install path/to/raylib_py-6.2.0-py3-none-any.whl
```

## How to use:

Try this (after installed raylib-py, create a new python file, save the code below into it, then run it):

```python

from raylibpy import *


def main():

    init_window(800, 450, "raylib [core] example - basic window")

    set_target_fps(60)

    while not window_should_close():

        begin_drawing()
        clear_background(RAYWHITE)
        draw_text("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)
        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
```

## API Documentation

Please refer to [`raylibpy-documentation.html` for v6.2.0](https://github.com/overdev/raylib-py/releases/download/v6.2.0) for documentation on raylib-py 6.2.

## Features:
- PEP8 naming convention only:

    Structure attributes are in `snake_case`, classes and other types in `PascalCase`.

- Type annotation:

    ```python
    def get_ray_collision_mesh(ray: Ray, mesh: Mesh, transform: Matrix) -> RayCollision:
        ...
    ```

- structures with functions as methods and properties:

    ```python
    sound = Sound.load('my/resorces/sound.wav')     # same as load_sound(...)
    position = Vector(4.0, 10.0)

    # later...
    sound.play()                                    # same as play_sound(sound)
    length = position.length                        # same as vector2length(position); uses raymath.h functions

    # creates an array of 3 Vector2 structures
    triangle = Vector2.array(Vector2(10.0, 10.0), Vector2(20.0, 30.0), Vector2(0.0, 30.0))

    # creates an array of 24 Image structures, zero initialized
    frames = Image.array(length=24)
    ```
    
- Vector{2,3,4}, Rectangle and Color have attribute swizzling;

    ```python
    vec3 = Vector3(2.0, 5.0, 3.0)
    vec2 = vec3.zxy                 # vec2 is a Vector2, not a sequence type
    other_vec3 = vec2.xxy           # same thing: other_vec3 is a Vector3
    vec2.xy = vec3.y, other_vec3.z  # sequences can be set as values

    c_red = Color(255, 0, 0)
    c_yellow = c_red.rrb

    # Rectangles have aliases for width and height: w and h respectively:
    rect = Rectangle(10.0, 10.0, 320.0, 240.0)
    other_rect = rect.whxy          # swizzling is only allowed when using four attributes, not 3 nor 2
    ```

- Pretty printing: most structures implement `__str__()` and `__repr__()` in a friendly way;
- Context managers: begin_* and end_* functions can be called as context managers:

    Without context managers:

    ```python
    # this example shows a rendering step

    begin_drawing()

    begin_texture_mode(minimap_texture)
    # render the "minimap"
    draw_line(2, 2, 5, 5, RED)
    end_texture_mode(minimap_texture)

    begin_mode2d(main_camera)
    # 2d drawing logic...
    draw_texture(minimap_texture, 10, 10, WHITE)
    end_mode2d()

    end_drawing()
    ```

    With context managers:

    ```python
    # this example shows a rendering step

    with drawing():

        with texture_mode(minimap_texture):
            # render the minimap
            draw_line(2, 2, 5, 5, RED)

        with mode2d(main_camera):
            # 2d drawing logic...
            draw_texture(minimap_texture, 10, 10, WHITE)
    ```

- Context managers for some structures: Camera{2,3}D, Shader and others;

    Folowing the example above:
    ```python
    # this example shows a rendering step

    with drawing():

        with minimap_texture:
            # render the minimap
            draw_line(2, 2, 5, 5, RED)

        with main_camera:
            # 2d drawing logic...
            draw_texture(minimap_texture, 10, 10, WHITE)
    ```

- RLGL and RayMath functions exposed

    Includes all symbols in raymath.h and rlgl.h

And more.

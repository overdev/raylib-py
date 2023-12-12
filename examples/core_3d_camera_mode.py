#*******************************************************************************************
#
#   raylib [core] example - Initialize 3d camera mode
#
#   Example originally created with raylib 1.0, last time updated with raylib 1.0
#
#   Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software
#
#   Copyright (c) 2014-2023 Ramon Santamaria (@raysan5)
#
#*******************************************************************************************/


import sys
import os
from ctypes import byref
from raylibpy import *


def main():
    """Transpiled function."""
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [core] example - 3d camera mode")

    camera = Camera3D()
    camera.position  = Vector3(0.0, 10.0, 10.0)
    camera.target  = Vector3(0.0, 0.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    cubePosition = Vector3(0.0, 0.0, 0.0)

    set_target_fps(60)
    
    while not window_should_close():
        with drawing():
            clear_background(RAYWHITE)

            with mode3d(camera):
                draw_cube(cubePosition, 2.0, 2.0, 2.0, RED)
                draw_cube_wires(cubePosition, 2.0, 2.0, 2.0, MAROON)
                draw_grid(10, 1.0)

            # end_mode3d()

            draw_text("Welcome to the third dimension!", 10, 40, 20, DARKGRAY)
            draw_fps(10, 10)

        # end_drawing()

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
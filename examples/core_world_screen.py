#*******************************************************************************************
#
#   raylib [core] example - World to screen
#
#   Example originally created with raylib 1.3, last time updated with raylib 1.4
#
#   Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software
#
#   Copyright (c) 2015-2023 Ramon Santamaria (@raysan5)
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

    init_window(screenWidth, screenHeight, "raylib [core] example - core world screen")

    camera = Camera()
    camera.position  = Vector3(10.0, 10.0, 10.0)
    camera.target  = Vector3(0.0, 0.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    cubePosition = Vector3(0.0, 0.0, 0.0)
    cubeScreenPosition = Vector2(0.0, 0.0)

    disable_cursor()
    set_target_fps(60)
    
    while not window_should_close():
        update_camera(byref(camera), CAMERA_THIRD_PERSON)

        cubeScreenPosition = get_world_to_screen(Vector3(cubePosition.x, cubePosition.y + 2.5, cubePosition.z), camera)

        begin_drawing()

        clear_background(RAYWHITE)

        with mode3d(camera):
            draw_cube(cubePosition, 2.0, 2.0, 2.0, RED)
            draw_cube_wires(cubePosition, 2.0, 2.0, 2.0, MAROON)
            draw_grid(10, 1.0)

        # end_mode3d()

        draw_text("Enemy: 100 / 100", cubeScreenPosition.x - measure_text("Enemy: 100/100", 20) / 2, cubeScreenPosition.y, 20, BLACK)
        draw_text(f"Cube position in screen space coordinates: {cubeScreenPosition.x}, {cubeScreenPosition.y})", 10, 10, 20, LIME)
        draw_text("Text 2d should be always on top of the cube", 10, 40, 20, GRAY)

        end_drawing()

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
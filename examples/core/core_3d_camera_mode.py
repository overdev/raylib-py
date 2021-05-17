# core_3d_camera_mode.py
# ******************************************************************************************
# 
#   raylib [core] example - Initialize 3d camera mode
# 
#   This example has been created using raylib 1.0 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2014 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [core] example - 3d camera mode")

    # Define the camera to look into our 3d world
    camera: Camera3D = Camera3D()
    camera.position = Vector3(0.0, 10.0, 10.0)  # Camera position
    camera.target = Vector3(0.0, 0.0, 0.0)  # Camera looking at point
    camera.up = Vector3(0.0, 1.0, 0.0)  # Camera up vector (rotation towards target)
    camera.fovy = 45.0  # Camera field-of-view Y
    camera.projection = CAMERA_PERSPECTIVE  # Camera mode type

    cube_position: Vector3 = Vector3()

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # TODO: Update your variables here
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(RAYWHITE)

            with mode3d(camera):
                draw_cube(cube_position, 2.0, 2.0, 2.0, RED)
                draw_cube_wires(cube_position, 2.0, 2.0, 2.0, MAROON)

                draw_grid(10, 1.0)

            # EndMode3D()

            draw_text("Welcome to the third dimension!", 10, 40, 20, DARKGRAY)

            draw_fps(10, 10)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# ******************************************************************************************
#
#   raylib [core] example - World to screen
#
#   This example has been created using raylib 1.3 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2015 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, "raylib [core] example - 3d camera free")

    # Define the camera to look into our 3d world
    camera: Camera = Camera()
    camera.position = Vector3(10.0, 10.0, 10.0)
    camera.target = Vector3(0.0, 0.0, 0.0)
    camera.up = Vector3(0.0, 1.0, 0.0)
    camera.fovy = 45.0
    camera.projection = CAMERA_PERSPECTIVE

    cube_position: Vector3 = Vector3(0.0, 0.0, 0.0)
    cube_screen_position: Vector2 = Vector2(0.0, 0.0)

    set_camera_mode(camera, CAMERA_FREE)  # Set a free camera mode

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key

        # Update
        # ----------------------------------------------------------------------------------
        update_camera(camera)  # Update camera

        # Calculate cube screen space position (with a little offset to be in top)
        cube_screen_position = get_world_to_screen(Vector3(cube_position.x, cube_position.y + 2.5, cube_position.z),
                                                   camera)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)

        draw_cube(cube_position, 2.0, 2.0, 2.0, RED)
        draw_cube_wires(cube_position, 2.0, 2.0, 2.0, MAROON)

        draw_grid(10, 1.0)

        end_mode3d()

        draw_text("Enemy: 100 / 100", cube_screen_position.x - measure_text("Enemy: 100 / 100", 20) / 2,
                  cube_screen_position.y, 20, BLACK)
        draw_text("Text is always on top of the cube",
                  (screen_width - measure_text("Text is always on top of the cube", 20)) // 2, 25, 20, GRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

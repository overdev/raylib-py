# core_3d_camera_free.py

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_COLUMNS = 20


def main():
    # Initialization
    # ---------------------------------------------------------------
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, "raylib [core] example - 3d camera free")

    # Define the camera to look into our 3d world
    camera = Camera(
        Vector3(4.0, 2.0, 4.0),
        Vector3(0.0, 0.0, 0.0),
        Vector3(0.0, 1.0, 0.0),
        45.0,
        CAMERA_PERSPECTIVE
    )

    cube_position = Vector3(0.0, 0.0, 0.0)

    set_camera_mode(camera, CAMERA_FREE)

    set_target_fps(60)
    # ---------------------------------------------------------------

    # Main game loop
    while not window_should_close():

        # Update
        # -----------------------------------------------------------
        update_camera(camera)
        if is_key_down(KEY_Z):
            camera.target = Vector3(0.0, 0.0, 0.0)
        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)

        draw_cube(cube_position, 2.0, 2.0, 2.0, RED)
        draw_cube_wires(cube_position, 2.0, 2.0, 2.0, MAROON)

        draw_grid(10, 1.0)

        end_mode3d()

        draw_rectangle(10, 10, 320, 133, fade(SKYBLUE, 0.5))
        draw_rectangle_lines(10, 10, 320, 133, BLUE)

        draw_text("Free camera default controls:", 20, 20, 10, BLACK)
        draw_text("- Mouse Wheel to Zoom in-out", 40, 40, 10, DARKGRAY)
        draw_text("- Mouse Wheel Pressed to Pan", 40, 60, 10, DARKGRAY)
        draw_text("- Alt + Mouse Wheel Pressed to Rotate", 40, 80, 10, DARKGRAY)
        draw_text("- Alt + Ctrl + Mouse Wheel Pressed for Smooth Zoom", 40, 100, 10, DARKGRAY)
        draw_text("- Z to Zoom to (0, 0, 0)", 40, 120, 10, DARKGRAY)

        end_drawing()
        # -----------------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ---------------------------------------------------------------


if __name__ == '__main__':
    main()

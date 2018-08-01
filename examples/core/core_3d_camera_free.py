# core_3d_camera_free.py

import raylibpy as rl
from ctypes import byref

MAX_COLUMNS = 20


def main():

    # Initialization
    # ---------------------------------------------------------------
    screen_width = 800
    screen_height = 450

    rl.init_window(screen_width, screen_height, "raylib [core] example - 3d camera free")

    # Define the camera to look into our 3d world
    camera = rl.Camera(
        rl.Vector3(4.0, 2.0, 4.0),
        rl.Vector3(0.0, 0.0, 0.0),
        rl.Vector3(0.0, 1.0, 0.0),
        45.0,
        rl.CAMERA_PERSPECTIVE
    )

    cube_position = rl.Vector3(0.0, 0.0, 0.0)

    rl.set_camera_mode(camera, rl.CAMERA_FREE)

    rl.set_target_fps(60)
    # ---------------------------------------------------------------

    # Main game loop
    while not rl.window_should_close():

        # Update
        # -----------------------------------------------------------
        rl.update_camera(byref(camera))
        if rl.is_key_down(rl.KEY_Z):
            camera.target = rl.Vector3(0.0, 0.0, 0.0)
        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)

        rl.begin_mode3d(camera)

        rl.draw_cube(cube_position, 2.0, 2.0, 2.0, rl.RED)
        rl.draw_cube_wires(cube_position, 2.0, 2.0, 2.0, rl.MAROON)

        rl.draw_grid(10, 1.0)

        rl.end_mode3d()

        rl.draw_rectangle(10, 10, 320, 133, rl.fade(rl.SKYBLUE, 0.5))
        rl.draw_rectangle_lines(10, 10, 320, 133, rl.BLUE)
        
        rl.draw_text("Free camera default controls:", 20, 20, 10, rl.BLACK)
        rl.draw_text("- Mouse Wheel to Zoom in-out", 40, 40, 10, rl.DARKGRAY)
        rl.draw_text("- Mouse Wheel Pressed to Pan", 40, 60, 10, rl.DARKGRAY)
        rl.draw_text("- Alt + Mouse Wheel Pressed to Rotate", 40, 80, 10, rl.DARKGRAY)
        rl.draw_text("- Alt + Ctrl + Mouse Wheel Pressed for Smooth Zoom", 40, 100, 10, rl.DARKGRAY)
        rl.draw_text("- Z to Zoom to (0, 0, 0)", 40, 120, 10, rl.DARKGRAY)

        rl.end_drawing()
        # -----------------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------------
    rl.close_window()       # Close window and OpenGL context
    # ---------------------------------------------------------------


if __name__ == '__main__':
    main()
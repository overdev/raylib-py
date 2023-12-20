
import sys
import os
from ctypes import byref
from raylibpy import *


FOVY_PERSPECTIVE = 45.0
WIDTH_ORTHOGRAPHIC = 10.0

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [models] example - geometric shapes")

    camera = Camera((0.0, 10.0, 10.0), (0.0, 0.0, 0.0), (0.0, 1.0, 0.0), FOVY_PERSPECTIVE, CAMERA_PERSPECTIVE)

    set_target_fps(60)
    
    while not window_should_close():
        if is_key_pressed(KEY_SPACE):
            if camera.projection == CAMERA_PERSPECTIVE:
                camera.fovy  = WIDTH_ORTHOGRAPHIC
                camera.projection  = CAMERA_ORTHOGRAPHIC
            else:
                camera.fovy  = FOVY_PERSPECTIVE
                camera.projection  = CAMERA_PERSPECTIVE

        with drawing():
            clear_background(RAYWHITE)

            with mode3d(camera):
                draw_cube(Vector3(-4.0, 0.0, 2.0), 2.0, 5.0, 2.0, RED)
                draw_cube_wires(Vector3(-4.0, 0.0, 2.0), 2.0, 5.0, 2.0, GOLD)
                draw_cube_wires(Vector3(-4.0, 0.0, -2.0), 3.0, 6.0, 2.0, MAROON)

                draw_sphere(Vector3(-1.0, 0.0, -2.0), 1.0, GREEN)
                draw_sphere_wires(Vector3(1.0, 0.0, 2.0), 2.0, 16, 16, LIME)

                draw_cylinder(Vector3(4.0, 0.0, -2.0), 1.0, 2.0, 3.0, 4, SKYBLUE)
                draw_cylinder_wires(Vector3(4.0, 0.0, -2.0), 1.0, 2.0, 3.0, 4, DARKBLUE)
                draw_cylinder_wires(Vector3(4.5, -1.0, 2.0), 1.0, 1.0, 2.0, 6, BROWN)
                draw_cylinder(Vector3(1.0, 0.0, -4.0), 0.0, 1.5, 3.0, 8, GOLD)
                draw_cylinder_wires(Vector3(1.0, 0.0, -4.0), 0.0, 1.5, 3.0, 8, PINK)

                draw_grid(10, 1.0)

            # end_mode3d()

            draw_text("Press Spacebar to switch camera type", 10, get_screen_height() - 30, 20, DARKGRAY)
            
            if camera.projection == CAMERA_ORTHOGRAPHIC:
                draw_text("ORTHOGRAPHIC", 10, 40, 20, BLACK)
            elif camera.projection == CAMERA_PERSPECTIVE:
                draw_text("PERSPECTIVE", 10, 40, 20, BLACK)

            draw_fps(10, 10)

        # end_drawing()

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
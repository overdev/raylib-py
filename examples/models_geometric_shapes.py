
import sys
import os
from ctypes import byref
from raylibpy import *

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [models] example - geometric shapes")

    camera = Camera()
    camera.position  = Vector3(0.0, 10.0, 10.0)
    camera.target  = Vector3(0.0, 0.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    set_target_fps(60)
    
    while not window_should_close():
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
                draw_capsule(Vector3(-3.0, 1.5, -4.0), Vector3(-4.0, -1.0, -4.0), 1.2, 8, 8, VIOLET)
                draw_capsule_wires(Vector3(-3.0, 1.5, -4.0), Vector3(-4.0, -1.0, -4.0), 1.2, 8, 8, PURPLE)
                draw_grid(10, 1.0)

            # end_mode3d()

            draw_fps(10, 10)

        # end_drawing()

    close_window()
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
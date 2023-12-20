
import sys
import os
from ctypes import byref
from raylibpy import *
# import raymath.h

def main():
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [models] example - drawing billboards")

    camera = Camera()
    camera.position  = Vector3(5.0, 4.0, 5.0)
    camera.target  = Vector3(0.0, 2.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    bill = load_texture("resources/billboard.png")
    billPositionStatic = Vector3(0.0, 2.0, 0.0)
    billPositionRotating = Vector3(1.0, 2.0, 1.0)

    source = Rectangle(0.0, 0.0, bill.width, bill.height)
    billUp = Vector3(0.0, 1.0, 0.0)
    rotateOrigin = Vector2()
    distanceStatic = None
    distanceRotating = None
    rotation = 0.0

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(byref(camera), CAMERA_ORBITAL)

        rotation  += 0.4
        distanceStatic  = camera.position.distance(billPositionStatic)
        distanceRotating  = camera.position.distance(billPositionRotating)

        with drawing():
            clear_background(RAYWHITE)

            with mode3d(camera):

                draw_grid(10, 1.0)
                
                if distanceStatic > distanceRotating:
                    draw_billboard(camera, bill, billPositionStatic, 2.0, WHITE)
                    draw_billboard_pro(camera, bill, source, billPositionRotating, billUp, Vector2(1.0, 1.0), rotateOrigin, rotation, WHITE)
                else:
                    draw_billboard_pro(camera, bill, source, billPositionRotating, billUp, Vector2(1.0, 1.0), rotateOrigin, rotation, WHITE)
                    draw_billboard(camera, bill, billPositionStatic, 2.0, WHITE)

            # end_mode3d()

            draw_fps(10, 10)

        # end_drawing()

    unload_texture(bill)
    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
#*******************************************************************************************
#
#   raylib [core] example - Smooth Pixel-perfect camera
#
#   Example originally created with raylib 3.7, last time updated with raylib 4.0
#   
#   Example contributed by Giancamillo Alessandroni (@NotManyIdeasDev) and
#   reviewed by Ramon Santamaria (@raysan5)
#
#   Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software
#
#   Copyright (c) 2021-2023 Giancamillo Alessandroni (@NotManyIdeasDev) and Ramon Santamaria (@raysan5)
#
#*******************************************************************************************/


import sys
import os
from ctypes import byref
from raylibpy import *
from math import sin as sinf, cos as cosf, atan, atan2


def main():
    """Transpiled function."""
    screenWidth = 800
    screenHeight = 450

    virtualScreenWidth = 160
    virtualScreenHeight = 90
    virtualRatio = screenWidth / virtualScreenWidth

    init_window(screenWidth, screenHeight, "raylib [core] example - smooth pixel-perfect camera")

    worldSpaceCamera = Camera2D()
    worldSpaceCamera.zoom  = 1.0

    screenSpaceCamera = Camera2D()
    screenSpaceCamera.zoom  = 1.0

    target = load_render_texture(virtualScreenWidth, virtualScreenHeight)

    rec01 = Rectangle(70.0, 35.0, 20.0, 20.0)
    rec02 = Rectangle(90.0, 55.0, 30.0, 10.0)
    rec03 = Rectangle(80.0, 65.0, 15.0, 25.0)

    sourceRec = Rectangle(0.0, 0.0, target.texture.width, -target.texture.height)
    destRec = Rectangle(-virtualRatio, -virtualRatio, screenWidth + (virtualRatio * 2), screenHeight + (virtualRatio * 2))

    origin = Vector2(0.0, 0.0)
    rotation = 0.0
    cameraX = 0.0
    cameraY = 0.0

    set_target_fps(60)
    
    while not window_should_close():
        rotation += 60.0 * get_frame_time()

        cameraX = (sinf(get_time()) * 50.0) - 10.0
        cameraY = cosf(get_time()) * 30.0

        screenSpaceCamera.target  = Vector2(cameraX, cameraY)

        worldSpaceCamera.target.x  = screenSpaceCamera.target.x
        screenSpaceCamera.target.x  -= worldSpaceCamera.target.x
        screenSpaceCamera.target.x  *= virtualRatio

        worldSpaceCamera.target.y  = screenSpaceCamera.target.y
        screenSpaceCamera.target.y  -= worldSpaceCamera.target.y
        screenSpaceCamera.target.y  *= virtualRatio

        with texture_mode(target):
            clear_background(RAYWHITE)

            with mode2d(worldSpaceCamera):
                draw_rectangle_pro(rec01, origin, rotation, BLACK)
                draw_rectangle_pro(rec02, origin, -rotation, RED)
                draw_rectangle_pro(rec03, origin, rotation + 45.0, BLUE)

            # end_mode2d()
        # end_texture_mode()

        with drawing():
            clear_background(RED)

            with mode2d(screenSpaceCamera):
                draw_texture_pro(target.texture, sourceRec, destRec, origin, 0.0, WHITE)

            # end_mode2d()

            draw_text(f"Screen resolution: {screenWidth}, {screenHeight}", 10, 10, 20, DARKBLUE)
            draw_text(f"World resolution: {virtualScreenWidth}, {virtualScreenHeight}", 10, 40, 20, DARKGREEN)
            draw_fps(get_screen_width() - 95, 10)

        # end_drawing()

    unload_render_texture(target)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
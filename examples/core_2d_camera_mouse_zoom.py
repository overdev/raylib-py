#*******************************************************************************************
#
#   raylib [core] example - 2d camera mouse zoom
#
#   Example originally created with raylib 4.2, last time updated with raylib 4.2
#
#   Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software
#
#   Copyright (c) 2022-2023 Jeffery Myers (@JeffM2501)
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

    init_window(screenWidth, screenHeight, "raylib [core] example - 2d camera mouse zoom")

    camera = Camera2D()
    camera.zoom  = 1.0

    set_target_fps(60)
    
    while not window_should_close():
        if is_mouse_button_down(MOUSE_BUTTON_RIGHT):
            delta = get_mouse_delta()
            delta  = vector2scale(delta, -1.0 / camera.zoom)
            camera.target  = vector2add(camera.target, delta)

        wheel = get_mouse_wheel_move()
        
        if wheel != 0:
            mouseWorldPos = get_screen_to_world2d(get_mouse_position(), camera)
            camera.offset  = get_mouse_position()
            camera.target  = mouseWorldPos
            zoomIncrement = 0.125
            camera.zoom  += (wheel * zoomIncrement)
            
            if camera.zoom < zoomIncrement:
                camera.zoom  = zoomIncrement

        begin_drawing()

        clear_background(BLACK)

        begin_mode2d(camera)

        rl_push_matrix()
        rl_translatef(0, 25 * 50, 0)
        rl_rotatef(90, 1, 0, 0)
        draw_grid(100, 50)
        rl_pop_matrix()
        draw_circle(100, 100, 50, YELLOW)

        end_mode2d()

        draw_text("Mouse right button drag to move, mouse wheel to zoom", 10, 10, 20, WHITE)

        end_drawing()

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
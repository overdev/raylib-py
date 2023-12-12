#*******************************************************************************************
#
#   raylib [core] example - Mouse input
#
#   Example originally created with raylib 1.0, last time updated with raylib 4.0
#
#   Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software
#
#   Copyright (c) 2014-2023 Ramon Santamaria (@raysan5)
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

    init_window(screenWidth, screenHeight, "raylib [core] example - mouse input")

    ballPosition = Vector2(-100.0, -100.0)
    ballColor = DARKBLUE

    set_target_fps(60)
    
    while not window_should_close():
        ballPosition  = get_mouse_position()
        
        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            ballColor  = MAROON
        elif is_mouse_button_pressed(MOUSE_BUTTON_MIDDLE):
            ballColor  = LIME
        elif is_mouse_button_pressed(MOUSE_BUTTON_RIGHT):
            ballColor  = DARKBLUE
        elif is_mouse_button_pressed(MOUSE_BUTTON_SIDE):
            ballColor  = PURPLE
        elif is_mouse_button_pressed(MOUSE_BUTTON_EXTRA):
            ballColor  = YELLOW
        elif is_mouse_button_pressed(MOUSE_BUTTON_FORWARD):
            ballColor  = ORANGE
        elif is_mouse_button_pressed(MOUSE_BUTTON_BACK):
            ballColor  = BEIGE

        begin_drawing()

        clear_background(RAYWHITE)
        draw_circle_v(ballPosition, 40, ballColor)
        draw_text("move ball with mouse and click mouse button to change color", 10, 10, 20, DARKGRAY)

        end_drawing()

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
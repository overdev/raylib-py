#*******************************************************************************************
#
#   raylib [core] example - Keyboard input
#
#   Example originally created with raylib 1.0, last time updated with raylib 1.0
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

    init_window(screenWidth, screenHeight, "raylib [core] example - keyboard input")

    ballPosition = Vector2(screenWidth / 2, screenHeight / 2)

    set_target_fps(60)
    
    while not window_should_close():
        if is_key_down(KEY_RIGHT):
            ballPosition.x  += 2.0
        
        if is_key_down(KEY_LEFT):
            ballPosition.x  -= 2.0
        
        if is_key_down(KEY_UP):
            ballPosition.y  -= 2.0
        
        if is_key_down(KEY_DOWN):
            ballPosition.y  += 2.0

        begin_drawing()

        clear_background(RAYWHITE)
        draw_text("move the ball with arrow keys", 10, 10, 20, DARKGRAY)
        draw_circle_v(ballPosition, 50, MAROON)

        end_drawing()

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
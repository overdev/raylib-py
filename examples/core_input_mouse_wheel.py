#*******************************************************************************************
#
#   raylib [core] examples - Mouse wheel input
#
#   Example originally created with raylib 1.1, last time updated with raylib 1.3
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

    init_window(screenWidth, screenHeight, "raylib [core] example - input mouse wheel")

    boxPositionY = screenHeight / 2 - 40
    scrollSpeed = 4

    set_target_fps(60)
    
    while not window_should_close():
        boxPositionY -= (get_mouse_wheel_move() * scrollSpeed)

        begin_drawing()

        clear_background(RAYWHITE)
        draw_rectangle(screenWidth / 2 - 40, boxPositionY, 80, 80, MAROON)
        draw_text("Use mouse wheel to move the cube up and down!", 10, 10, 20, GRAY)
        draw_text(f"Box position Y: {boxPositionY}", 10, 40, 20, LIGHTGRAY)

        end_drawing()

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
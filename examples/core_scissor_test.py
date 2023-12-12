#*******************************************************************************************
#
#   raylib [core] example - Scissor test
#
#   Example originally created with raylib 2.5, last time updated with raylib 3.0
#
#   Example contributed by Chris Dill (@MysteriousSpace) and reviewed by Ramon Santamaria (@raysan5)
#
#   Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software
#
#   Copyright (c) 2019-2023 Chris Dill (@MysteriousSpace)
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

    init_window(screenWidth, screenHeight, "raylib [core] example - scissor test")

    scissorArea = Rectangle(0, 0, 300, 300)
    scissorMode = True

    set_target_fps(60)
    
    while not window_should_close():
        if is_key_pressed(KEY_S):
            scissorMode  = not scissorMode

        scissorArea.x  = get_mouse_x() - scissorArea.width / 2
        scissorArea.y  = get_mouse_y() - scissorArea.height / 2

        with drawing():
            clear_background(RAYWHITE)
            
            if scissorMode:
                begin_scissor_mode(scissorArea.x, scissorArea.y, scissorArea.width, scissorArea.height)

            draw_rectangle(0, 0, get_screen_width(), get_screen_height(), RED)
            draw_text("Move the mouse around to reveal this text!", 190, 200, 20, LIGHTGRAY)
            
            if scissorMode:
                end_scissor_mode()

            draw_rectangle_lines_ex(scissorArea, 1, BLACK)
            draw_text("Press S to toggle scissor test", 10, 10, 20, BLACK)

        # end_drawing()

    close_window()
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
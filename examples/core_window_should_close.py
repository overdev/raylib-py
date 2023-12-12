#*******************************************************************************************
#
#   raylib [core] example - Window should close
#
#   Example originally created with raylib 4.2, last time updated with raylib 4.2
#
#   Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software
#
#   Copyright (c) 2013-2023 Ramon Santamaria (@raysan5)
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

    init_window(screenWidth, screenHeight, "raylib [core] example - window should close")
    set_exit_key(KEY_NULL)

    exitWindowRequested = False
    exitWindow = False

    set_target_fps(60)
    
    while not exitWindow:
        if window_should_close() or is_key_pressed(KEY_ESCAPE):
            exitWindowRequested  = True
        
        if exitWindowRequested:
            if is_key_pressed(KEY_Y):
                exitWindow  = True
            elif is_key_pressed(KEY_N):
                exitWindowRequested  = False

        with drawing():

            clear_background(RAYWHITE)
            
            if exitWindowRequested:
                draw_rectangle(0, 100, screenWidth, 200, BLACK)
                draw_text("Are you sure you want to exit program? [Y/N]", 40, 180, 30, WHITE)
            else:
                draw_text("Try to close the window to get confirmation message!", 120, 200, 20, LIGHTGRAY)

        # end_drawing()

    close_window()
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
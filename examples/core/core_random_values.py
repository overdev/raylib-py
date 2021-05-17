# core_random_values.py
# ******************************************************************************************
#
#   raylib [core] example - Generate random values
#
#   This example has been created using raylib 1.1 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2014 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [core] example - generate random values")

    frames_counter: int = 0  # Variable used to count frames

    rand_value: int = get_random_value(-8, 5)  # Get a random integer number between -8 and 5 (both included)

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        frames_counter += 1

        # Every two seconds (120 frames) a new random value is generated
        if ((frames_counter / 120) % 2) == 1:
            rand_value = get_random_value(-8, 5)
            frames_counter = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("Every 2 seconds a new random value is generated:", 130, 100, 20, MAROON)

            draw_text(f"{rand_value}", 360, 180, 80, LIGHTGRAY)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# core_storage_values.py
# ******************************************************************************************
#
#   raylib [core] example - Storage save/load values
#
#   This example has been created using raylib 1.4 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2015 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

# NOTE: Storage positions must start with 0, directly related to file memory layout
STORAGE_POSITION_SCORE = 0
STORAGE_POSITION_HISCORE = 1


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [core] example - storage save/load values")

    score: int = 0
    hiscore: int = 0
    frames_counter: int = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_key_pressed(KEY_R):
            score = get_random_value(1000, 2000)
            hiscore = get_random_value(2000, 4000)

        if is_key_pressed(KEY_ENTER):
            save_storage_value(STORAGE_POSITION_SCORE, score)
            save_storage_value(STORAGE_POSITION_HISCORE, hiscore)
        elif is_key_pressed(KEY_SPACE):
            # NOTE: If requested position could not be found, value 0 is returned
            score = load_storage_value(STORAGE_POSITION_SCORE)
            hiscore = load_storage_value(STORAGE_POSITION_HISCORE)

        frames_counter += 1
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text(f"SCORE: {score}", 280, 130, 40, MAROON)
            draw_text(f"HI-SCORE: {hiscore}", 210, 200, 50, BLACK)

            draw_text(f"frames: {frames_counter}", 10, 10, 20, LIME)

            draw_text("Press R to generate random numbers", 220, 40, 20, LIGHTGRAY)
            draw_text("Press ENTER to SAVE values", 250, 310, 20, LIGHTGRAY)
            draw_text("Press SPACE to LOAD values", 252, 350, 20, LIGHTGRAY)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# shapes_easings_ball_anim.py
# ******************************************************************************************
# 
#   raylib [shapes] example - easings ball anim
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2014-2019 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *
from raylibpy.easings import *


# include "easings.h"                # Required for easing functions

def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - easings ball anim")

    # Ball variable value to be animated with easings
    ball_position_x: float = -100
    ball_radius: float = 20
    ball_alpha: float = 0.0

    state: int = 0
    frames_counter: int = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if state == 0:  # Move ball position X with easing
            frames_counter += 1
            ball_position_x = ease_elastic_out(frames_counter, -100.0, screen_width / 2.0 + 100, 120)

            if frames_counter >= 120:
                frames_counter = 0
                state = 1
        elif state == 1:  # Increase ball radius with easing
            frames_counter += 1
            ball_radius = ease_elastic_in(frames_counter, 20.0, 500.0, 200)

            if frames_counter >= 200:
                frames_counter = 0
                state = 2
        elif state == 2:  # Change ball alpha with easing (background color blending)
            frames_counter += 1
            ball_alpha = ease_cubic_out(frames_counter, 0.0, 1.0, 200)

            if frames_counter >= 200:
                frames_counter = 0
                state = 3
        elif state == 3:  # Reset state to play again
            if is_key_pressed(KEY_ENTER):
                # Reset required variables to play again
                ball_position_x = -100
                ball_radius = 20
                ball_alpha = 0.0
                state = 0

        if is_key_pressed(KEY_R):
            frames_counter = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            if state >= 2:
                draw_rectangle(0, 0, screen_width, screen_height, GREEN)
            draw_circle(ball_position_x, 200, ball_radius, fade(RED, 1.0 - ball_alpha))

            if state == 3:
                draw_text("PRESS [ENTER] TO PLAY AGAIN!", 240, 200, 20, BLACK)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

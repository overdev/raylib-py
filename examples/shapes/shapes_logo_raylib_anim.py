# shapes_logo_raylib_anim.py
# ******************************************************************************************
# 
#   raylib [shapes] example - raylib logo animation
# 
#   This example has been created using raylib 2.3 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2014 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - raylib logo animation")

    logo_position_x: int = screen_width // 2 - 128
    logo_position_y: int = screen_height // 2 - 128

    frames_counter: int = 0
    letters_count: int = 0

    top_side_rec_width: int = 16
    left_side_rec_height: int = 16

    bottom_side_rec_width: int = 16
    right_side_rec_height: int = 16

    state: int = 0  # Tracking animation states (State Machine)
    alpha: float = 1.0  # Useful for fading

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if state == 0:  # State 0: Small box blinking
            frames_counter += 1

            if frames_counter == 120:
                state = 1
                frames_counter = 0  # Reset counter... will be used later...
        elif state == 1:  # State 1: Top and left bars growing
            top_side_rec_width += 4
            left_side_rec_height += 4

            if top_side_rec_width == 256:
                state = 2
        elif state == 2:  # State 2: Bottom and right bars growing
            bottom_side_rec_width += 4
            right_side_rec_height += 4

            if bottom_side_rec_width == 256:
                state = 3
        elif state == 3:  # State 3: Letters appearing (one by one)
            frames_counter += 1

            if frames_counter / 12:  # Every 12 frames, one more letter!
                letters_count += 1
                frames_counter = 0

            if letters_count >= 10:  # When all letters have appeared, just fade out everything
                alpha -= 0.02

                if alpha <= 0.0:
                    alpha = 0.0
                    state = 4
        elif state == 4:  # State 4: Reset and Replay
            if is_key_pressed(KEY_R):
                frames_counter = 0
                letters_count = 0

                top_side_rec_width = 16
                left_side_rec_height = 16

                bottom_side_rec_width = 16
                right_side_rec_height = 16

                alpha = 1.0
                state = 0  # Return to State 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            if state == 0:
                if (frames_counter / 15) % 2:
                    draw_rectangle(logo_position_x, logo_position_y, 16, 16, BLACK)
            elif state == 1:
                draw_rectangle(logo_position_x, logo_position_y, top_side_rec_width, 16, BLACK)
                draw_rectangle(logo_position_x, logo_position_y, 16, left_side_rec_height, BLACK)
            elif state == 2:
                draw_rectangle(logo_position_x, logo_position_y, top_side_rec_width, 16, BLACK)
                draw_rectangle(logo_position_x, logo_position_y, 16, left_side_rec_height, BLACK)

                draw_rectangle(logo_position_x + 240, logo_position_y, 16, right_side_rec_height, BLACK)
                draw_rectangle(logo_position_x, logo_position_y + 240, bottom_side_rec_width, 16, BLACK)
            elif state == 3:
                draw_rectangle(logo_position_x, logo_position_y, top_side_rec_width, 16, fade(BLACK, alpha))
                draw_rectangle(logo_position_x, logo_position_y + 16, 16, left_side_rec_height - 32, fade(BLACK, alpha))

                draw_rectangle(logo_position_x + 240, logo_position_y + 16, 16, right_side_rec_height - 32,
                               fade(BLACK, alpha))
                draw_rectangle(logo_position_x, logo_position_y + 240, bottom_side_rec_width, 16, fade(BLACK, alpha))

                draw_rectangle(screen_width / 2 - 112, screen_height / 2 - 112, 224, 224, fade(RAYWHITE, alpha))

                draw_text(text_subtext("raylib", 0, letters_count), screen_width / 2 - 44, screen_height / 2 + 48, 50,
                          fade(BLACK, alpha))
            elif state == 4:
                draw_text("[R] REPLAY", 340, 200, 20, GRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# shapes_easings_box_anim.py
# ******************************************************************************************
# 
#   raylib [shapes] example - easings box anim
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2014-2019 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.consts import *
from raylibpy.spartan import *
from raylibpy.easings import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - easings box anim")

    # Box variables to be animated with easings
    rec: Rectangle = Rectangle(get_screen_width() / 2, -100, 100, 100)
    rotation: float = 0.0
    alpha: float = 1.0

    state: int = 0
    frames_counter: int = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if state == 0:  # Move box down to center of screen
            frames_counter += 1

            # NOTE: Remember that 3rd parameter of easing function refers to
            #       desired value variation, do not confuse it with expected final value!
            rec.y = ease_elastic_out(frames_counter, -100, get_screen_height() / 2 + 100, 120)

            if frames_counter >= 120:
                frames_counter = 0
                state = 1
        elif state == 1:  # Scale box to an horizontal bar
            frames_counter += 1
            rec.height = ease_bounce_out(frames_counter, 100, -90, 120)
            rec.width = ease_bounce_out(frames_counter, 100, get_screen_width(), 120)

            if frames_counter >= 120:
                frames_counter = 0
                state = 2
        elif state == 2:  # Rotate horizontal bar rectangle
            frames_counter += 1
            rotation = ease_quad_out(frames_counter, 0.0, 270.0, 240)

            if frames_counter >= 240:
                frames_counter = 0
                state = 3
        elif state == 3:  # Increase bar size to fill all screen
            frames_counter += 1
            rec.height = ease_circ_out(frames_counter, 10, get_screen_width(), 120)

            if frames_counter >= 120:
                frames_counter = 0
                state = 4
        elif state == 4:  # fade out animation
            frames_counter += 1
            alpha = ease_sine_out(frames_counter, 1.0, -1.0, 160)

            if frames_counter >= 160:
                frames_counter = 0
                state = 5

        # Reset animation at any moment
        if is_key_pressed(KEY_SPACE):
            rec = Rectangle(get_screen_width() / 2, -100, 100, 100)
            rotation = 0.0
            alpha = 1.0
            state = 0
            frames_counter = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_rectangle_pro(rec, Vector2(rec.width / 2, rec.height / 2), rotation, fade(BLACK, alpha))

            draw_text("PRESS [SPACE] TO RESET BOX ANIMATION!", 10, get_screen_height() - 25, 20, LIGHTGRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

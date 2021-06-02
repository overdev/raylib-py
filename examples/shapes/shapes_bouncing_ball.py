# shapes_bouncing_ball.py
# ******************************************************************************************
# 
#   raylib [shapes] example - bouncing ball
# 
#   This example has been created using raylib 1.0 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2013 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def main() -> int:
    # Initialization
    # ---------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - bouncing ball")

    ball_position: Vector2 = Vector2(get_screen_width() / 2, get_screen_height() / 2)
    ball_speed: Vector2 = Vector2(5.0, 4.0)
    ball_radius: int = 20

    pause: bool = False
    frames_counter: int = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # -----------------------------------------------------
        if is_key_pressed(KEY_SPACE):
            pause = not pause

        if not pause:
            ball_position.x += ball_speed.x
            ball_position.y += ball_speed.y

            # Check walls collision for bouncing
            if ball_position.x >= get_screen_width() - ball_radius or ball_position.x <= ball_radius:
                ball_speed.x *= -1.0
            if ball_position.y >= get_screen_height() - ball_radius or ball_position.y <= ball_radius:
                ball_speed.y *= -1.0
        else:
            frames_counter += 1
        # -----------------------------------------------------

        # Draw
        # -----------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_circle_v(ball_position, ball_radius, MAROON)
            draw_text("PRESS SPACE to PAUSE BALL MOVEMENT", 10, get_screen_height() - 25, 20, LIGHTGRAY)

            # On pause, we draw a blinking message
            if pause and (frames_counter / 30) % 2:
                draw_text("PAUSED", 350, 200, 30, GRAY)

            draw_fps(10, 10)

        # end drawing
        # -----------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

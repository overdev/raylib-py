# core_input_mouse.py
# ******************************************************************************************
#
#   raylib [core] example - Mouse input
#
#   This example has been created using raylib 1.0 (www.raylib.com)
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

    init_window(screen_width, screen_height, "raylib [core] example - mouse input")

    ball_position: Vector2 = Vector2(-100.0, -100.0)
    ball_color: Color = DARKBLUE

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ---------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        ball_position = get_mouse_position()

        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            ball_color = MAROON
        elif is_mouse_button_pressed(MOUSE_BUTTON_MIDDLE):
            ball_color = LIME
        elif is_mouse_button_pressed(MOUSE_BUTTON_RIGHT):
            ball_color = DARKBLUE

        # NOTE: not supported in 3.7:
        # elif is_mouse_button_pressed(MOUSE_BUTTON_SIDE):
        #     ball_color = PURPLE
        # elif is_mouse_button_pressed(MOUSE_BUTTON_EXTRA):
        #     ball_color = YELLOW
        # elif is_mouse_button_pressed(MOUSE_BUTTON_FORWARD):
        #     ball_color = ORANGE
        # elif is_mouse_button_pressed(MOUSE_BUTTON_BACK):
        #     ball_color = BEIGE
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_circle_v(ball_position, 40, ball_color)

            draw_text("move ball with mouse and click mouse button to change color", 10, 10, 20, DARKGRAY)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

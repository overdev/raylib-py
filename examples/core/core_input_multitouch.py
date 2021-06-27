# core_input_multitouch.py
# ******************************************************************************************
#
#   raylib [core] example - Input multitouch
#
#   This example has been created using raylib 2.1 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Example contributed by Berni (@Berni8k) and reviewed by Ramon Santamaria (@raysan5)
#
#   Copyright (c) 2019 Berni (@Berni8k) and Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_TOUCH_POINTS = 10


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [core] example - input multitouch")

    ball_position: Vector2 = Vector2(-100.0, -100.0)
    ball_color: Color = BEIGE

    touch_counter: int = 0
    touch_position: Vector2 = Vector2()

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ---------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        ball_position = get_mouse_position()

        ball_color = BEIGE

        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            ball_color = MAROON
        if is_mouse_button_down(MOUSE_BUTTON_MIDDLE):
            ball_color = LIME
        if is_mouse_button_down(MOUSE_BUTTON_RIGHT):
            ball_color = DARKBLUE

        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            touch_counter = 10
        if is_mouse_button_pressed(MOUSE_BUTTON_MIDDLE):
            touch_counter = 10
        if is_mouse_button_pressed(MOUSE_BUTTON_RIGHT):
            touch_counter = 10

        if touch_counter > 0:
            touch_counter -= 1
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            # Multitouch
            for i in range(MAX_TOUCH_POINTS):
                touch_position = get_touch_position(i)  # Get the touch point

                # Make sure point is not (-1,-1) as this means there is no touch for it
                if touch_position.x >= 0 and touch_position.y >= 0:
                    # Draw circle and touch index number
                    draw_circle_v(touch_position, 34, ORANGE)
                    draw_text(str(i), touch_position.x - 10, touch_position.y - 70, 40, BLACK)

            # Draw the normal mouse location
            draw_circle_v(ball_position, 30 + (touch_counter * 3.0), ball_color)

            draw_text("move ball with mouse and click mouse button to change color", 10, 10, 20, DARKGRAY)
            draw_text("touch the screen at multiple locations to get multiple balls", 10, 30, 20, DARKGRAY)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

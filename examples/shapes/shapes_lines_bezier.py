# shapes_lines_bezier.py
# ******************************************************************************************
# 
#   raylib [shapes] example - Cubic-bezier lines
# 
#   This example has been created using raylib 1.7 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2017 Ramon Santamaria (@raysan5)
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

    set_config_flags(FLAG_MSAA_4X_HINT)
    init_window(screen_width, screen_height, "raylib [shapes] example - cubic-bezier lines")

    start: Vector2 = Vector2(0, 0)
    end: Vector2 = Vector2(screen_width, screen_height)

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            start = get_mouse_position()
        elif is_mouse_button_down(MOUSE_BUTTON_RIGHT):
            end = get_mouse_position()
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("USE MOUSE LEFT-RIGHT CLICK to DEFINE LINE START and END POINTS", 15, 20, 20, GRAY)

            draw_line_bezier(start, end, 2.0, RED)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

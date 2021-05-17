# core_input_mouse_wheel.py
# ******************************************************************************************
#
#   raylib [core] examples - Mouse wheel input
#
#   This test has been created using raylib 1.1 (www.raylib.com)
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

    init_window(screen_width, screen_height, "raylib [core] example - input mouse wheel")

    box_position_y: int = screen_height // 2 - 40
    scroll_speed: int = 4  # Scrolling speed in pixels

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        box_position_y -= (get_mouse_wheel_move() * scroll_speed)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(RAYWHITE)

            draw_rectangle(screen_width // 2 - 40, box_position_y, 80, 80, MAROON)

            draw_text("Use mouse wheel to move the cube up and down!", 10, 10, 20, GRAY)
            draw_text(f"Box position Y: {box_position_y}", 10, 40, 20, LIGHTGRAY)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

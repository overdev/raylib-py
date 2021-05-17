# ******************************************************************************************
#
#   raylib [core] example - Scissor test
#
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Example contributed by Chris Dill (@MysteriousSpace) and reviewed by Ramon Santamaria (@raysan5)
#
#   Copyright (c) 2019 Chris Dill (@MysteriousSpace)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, "raylib [core] example - scissor test")

    scissor_area: Rectangle = Rectangle(0, 0, 300, 300)
    scissor_mode: bool = True

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key

        # Update
        # ----------------------------------------------------------------------------------
        if is_key_pressed(KEY_S):
            scissor_mode = not scissor_mode

        # Centre the scissor area around the mouse position
        scissor_area.x = get_mouse_x() - scissor_area.width / 2
        scissor_area.y = get_mouse_y() - scissor_area.height / 2
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        if scissor_mode:
            begin_scissor_mode(scissor_area.x, scissor_area.y, scissor_area.width, scissor_area.height)

        # Draw full screen rectangle and some text
        # NOTE: Only part defined by scissor area will be rendered
        draw_rectangle(0, 0, get_screen_width(), get_screen_height(), RED)
        draw_text("Move the mouse around to reveal this text!", 190, 200, 20, LIGHTGRAY)

        if scissor_mode:
            end_scissor_mode()

        draw_rectangle_lines_ex(scissor_area, 1, BLACK)
        draw_text("Press S to toggle scissor test", 10, 10, 20, BLACK)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

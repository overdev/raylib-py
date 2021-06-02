# shapes_basic_shapes.py
# ******************************************************************************************
# 
#   raylib [shapes] example - Draw basic shapes 2d (rectangle, circle, line...)
# 
#   This example has been created using raylib 1.0 (www.raylib.com)
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

    init_window(screen_width, screen_height, "raylib [shapes] example - basic shapes drawing")

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # TODO: Update your variables here
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(RAYWHITE)

            draw_text("some basic shapes available on raylib", 20, 20, 20, DARKGRAY)

            # Circle shapes and lines
            draw_circle(screen_width / 5, 120, 35, DARKBLUE)
            draw_circle_gradient(screen_width / 5, 220, 60, GREEN, SKYBLUE)
            draw_circle_lines(screen_width / 5, 340, 80, DARKBLUE)

            # Rectangle shapes and ines
            draw_rectangle(screen_width / 4 * 2 - 60, 100, 120, 60, RED)
            draw_rectangle_gradient_h(screen_width / 4 * 2 - 90, 170, 180, 130, MAROON, GOLD)
            draw_rectangle_lines(screen_width / 4 * 2 - 40, 320, 80, 60,
                                 ORANGE)  # NOTE: Uses QUADS internally, not lines

            # Triangle shapes and lines
            draw_triangle(Vector2(screen_width / 4.0 * 3.0, 80.0),
                          Vector2(screen_width / 4.0 * 3.0 - 60.0, 150.0),
                          Vector2(screen_width / 4.0 * 3.0 + 60.0, 150.0), VIOLET)

            draw_triangle_lines(Vector2(screen_width / 4.0 * 3.0, 160.0),
                                Vector2(screen_width / 4.0 * 3.0 - 20.0, 230.0),
                                Vector2(screen_width / 4.0 * 3.0 + 20.0, 230.0), DARKBLUE)

            # Polygon shapes and lines
            draw_poly(Vector2(screen_width / 4 * 3, 320), 6, 80, 0, BROWN)
            draw_poly_lines(Vector2(screen_width / 4 * 3, 320), 6, 80, 0, BEIGE)

            # NOTE: We draw all LINES based shapes together to optimize internal drawing,
            # this way, all LINES are rendered in a single draw pass
            draw_line(18, 42, screen_width - 18, 42, BLACK)
        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# shapes_colors_palette.py
# ******************************************************************************************
# 
#   raylib [shapes] example - Colors palette
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2014-2019 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/

from typing import List
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_COLORS_COUNT = 21  # Number of colors available


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 600

    init_window(screen_width, screen_height, "raylib [shapes] example - colors palette")

    colors: List[Color] = [
        DARKGRAY, MAROON, ORANGE, DARKGREEN, DARKBLUE, DARKPURPLE, DARKBROWN,
        GRAY, RED, GOLD, LIME, BLUE, VIOLET, BROWN, LIGHTGRAY, PINK, YELLOW,
        GREEN, SKYBLUE, PURPLE, BEIGE]

    color_names: List[str] = [
        "DARKGRAY", "MAROON", "ORANGE", "DARKGREEN", "DARKBLUE", "DARKPURPLE",
        "DARKBROWN", "GRAY", "RED", "GOLD", "LIME", "BLUE", "VIOLET", "BROWN",
        "LIGHTGRAY", "PINK", "YELLOW", "GREEN", "SKYBLUE", "PURPLE", "BEIGE"]

    colors_recs: List[Rectangle] = [Rectangle() for _ in range(MAX_COLORS_COUNT)]  # Rectangles array

    # Fills colorsRecs data (for every rectangle)
    for i in range(MAX_COLORS_COUNT):
        colors_recs[i].x = 20.0 + 100.0 * (i % 7) + 10.0 * (i % 7)
        colors_recs[i].y = 80.0 + 100.0 * (i / 7) + 10.0 * (i / 7)
        colors_recs[i].width = 100.0
        colors_recs[i].height = 100.0

    color_state: List[int] = [int() for _ in range(MAX_COLORS_COUNT)]  # Color state: 0-DEFAULT, 1-MOUSE_HOVER

    mouse_point: Vector2

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        mouse_point = get_mouse_position()

        for i in range(MAX_COLORS_COUNT):
            if check_collision_point_rec(mouse_point, colors_recs[i]):
                color_state[i] = 1
            else:
                color_state[i] = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("raylib colors palette", 28, 42, 20, BLACK)
            draw_text("press SPACE to see all colors", get_screen_width() - 180, get_screen_height() - 40, 10, GRAY)

            for i in range(MAX_COLORS_COUNT):  # Draw all rectangles
                draw_rectangle_rec(colors_recs[i], fade(colors[i], 0.6 if color_state[i] else 1.0))

                if is_key_down(KEY_SPACE) or color_state[i]:
                    draw_rectangle(colors_recs[i].x, colors_recs[i].y + colors_recs[i].height - 26,
                                   colors_recs[i].width, 20, BLACK)
                    draw_rectangle_lines_ex(colors_recs[i], 6, fade(BLACK, 0.3))
                    draw_text(color_names[i],
                              colors_recs[i].x + colors_recs[i].width - measure_text(color_names[i], 10) - 12,
                              colors_recs[i].y + colors_recs[i].height - 20, 10, colors[i])

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

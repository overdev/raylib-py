# shapes_draw_circle_sector.py
# ******************************************************************************************
# 
#   raylib [shapes] example - draw circle sector (with gui options)
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Example contributed by Vlad Adrian (@demizdor) and reviewed by Ramon Santamaria (@raysan5)
# 
#   Copyright (c) 2018 Vlad Adrian (@demizdor) and Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/

import math
from raylibpy.colors import *
from raylibpy.spartan import *

RAYGUI_IMPLEMENTATION = False  # Required for GUI controls


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - draw circle sector")

    center: Vector2 = Vector2((get_screen_width() - 300) / 2, get_screen_height() / 2)

    outer_radius: float = 180.0
    start_angle: float = 0.0
    end_angle: float = 180.0
    segments: int = 0
    min_segments: int

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # NOTE: All variables update happens inside GUI control functions
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(RAYWHITE)

            draw_line(500, 0, 500, get_screen_height(), fade(LIGHTGRAY, 0.6))
            draw_rectangle(500, 0, get_screen_width() - 500, get_screen_height(), fade(LIGHTGRAY, 0.3))

            draw_circle_sector(center, outer_radius, start_angle, end_angle, segments, fade(MAROON, 0.3))
            draw_circle_sector_lines(center, outer_radius, start_angle, end_angle, segments, fade(MAROON, 0.6))

            # Draw GUI controls
            # ------------------------------------------------------------------------------
            start_angle = GuiSliderBar(Rectangle(600, 40, 120, 20), "StartAngle", None, start_angle, 0, 720)
            end_angle = GuiSliderBar(Rectangle(600, 70, 120, 20), "EndAngle", None, end_angle, 0, 720)

            outer_radius = GuiSliderBar(Rectangle(600, 140, 120, 20), "Radius", None, outer_radius, 0, 200)
            segments = GuiSliderBar(Rectangle(600, 170, 120, 20), "Segments", None, segments, 0, 100)
            # ------------------------------------------------------------------------------

            min_segments = math.ceil((end_angle - start_angle) / 90)
            draw_text(f"MODE: {'MANUAL' if segments >= min_segments else 'AUTO'}", 600, 200, 10,
                      MAROON if segments >= min_segments else DARKGRAY)

            draw_fps(10, 10)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

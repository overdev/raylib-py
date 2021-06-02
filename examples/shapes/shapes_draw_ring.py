# shapes_draw_ring.py
# ******************************************************************************************
# 
#   raylib [shapes] example - draw ring (with gui options)
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Example contributed by Vlad Adrian (@demizdor) and reviewed by Ramon Santamaria (@raysan5)
# 
#   Copyright (c) 2018 Vlad Adrian (@demizdor) and Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/

from math import ceil
from raylibpy.colors import *
from raylibpy.spartan import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - draw ring")

    center: Vector2 = Vector2((get_screen_width() - 300) / 2, get_screen_height() / 2)

    inner_radius: float = 80.0
    outer_radius: float = 190.0

    start_angle: float = 0.0
    end_angle: float = 360.0
    segments: int = 0
    min_segments: int

    check_draw_ring: bool = True
    check_draw_ring_lines: bool = False
    check_draw_circle_lines: bool = False

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

            if check_draw_ring:
                draw_ring(center, inner_radius, outer_radius, start_angle, end_angle, segments, fade(MAROON, 0.3))

            if check_draw_ring_lines:
                draw_ring_lines(center, inner_radius, outer_radius, start_angle, end_angle, segments, fade(BLACK, 0.4))

            if check_draw_circle_lines:
                draw_circle_sector_lines(center, outer_radius, start_angle, end_angle, segments, fade(BLACK, 0.4))

            # Draw GUI controls
            # ------------------------------------------------------------------------------
            start_angle = GuiSliderBar(Rectangle(600, 40, 120, 20), "StartAngle", NULL, start_angle, -450, 450)
            end_angle = GuiSliderBar(Rectangle(600, 70, 120, 20), "EndAngle", NULL, end_angle, -450, 450)

            inner_radius = GuiSliderBar(Rectangle(600, 140, 120, 20), "InnerRadius", NULL, inner_radius, 0, 100)
            outer_radius = GuiSliderBar(Rectangle(600, 170, 120, 20), "OuterRadius", NULL, outer_radius, 0, 200)

            segments = GuiSliderBar(Rectangle(600, 240, 120, 20), "Segments", NULL, segments, 0, 100)

            check_draw_ring = GuiCheckBox(Rectangle(600, 320, 20, 20), "Draw Ring", check_draw_ring)
            check_draw_ring_lines = GuiCheckBox(Rectangle(600, 350, 20, 20), "Draw RingLines", check_draw_ring_lines)
            check_draw_circle_lines = GuiCheckBox(Rectangle(600, 380, 20, 20), "Draw CircleLines",
                                                  check_draw_circle_lines)
            # ------------------------------------------------------------------------------

            min_segments: int = ceil((end_angle - start_angle) / 90)
            draw_text(f"MODE: {'MANUAL' if segments >= min_segments else 'AUTO'}", 600, 270, 10,
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

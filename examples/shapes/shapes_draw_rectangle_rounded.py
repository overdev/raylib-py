# shapes_draw_rectangle_rounded.py
# ******************************************************************************************
# 
#   raylib [shapes] example - draw rectangle rounded (with gui options)
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Example contributed by Vlad Adrian (@demizdor) and reviewed by Ramon Santamaria (@raysan5)
# 
#   Copyright (c) 2018 Vlad Adrian (@demizdor) and Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - draw rectangle rounded")

    roundness: float = 0.2
    width: int = 200
    height: int = 100
    segments: int = 0
    line_thick: int = 1

    draw_rect: bool = False
    draw_rounded_rect: bool = True
    draw_rounded_lines: bool = False

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        rec: Rectangle = Rectangle((get_screen_width() - width - 250) / 2, (get_screen_height() - height) / 2, width,
                                   height)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_line(560, 0, 560, get_screen_height(), fade(LIGHTGRAY, 0.6))
            draw_rectangle(560, 0, get_screen_width() - 500, get_screen_height(), fade(LIGHTGRAY, 0.3))

            if draw_rect:
                draw_rectangle_rec(rec, fade(GOLD, 0.6))
            if draw_rounded_rect:
                draw_rectangle_rounded(rec, roundness, segments, fade(MAROON, 0.2))
            if draw_rounded_lines:
                draw_rectangle_rounded_lines(rec, roundness, segments, line_thick, fade(MAROON, 0.4))

            # Draw GUI controls
            # ------------------------------------------------------------------------------
            width = GuiSliderBar(Rectangle(640, 40, 105, 20), "Width", NULL, width, 0, get_screen_width() - 300)
            height = GuiSliderBar(Rectangle(640, 70, 105, 20), "Height", NULL, height, 0, get_screen_height() - 50)
            roundness = GuiSliderBar(Rectangle(640, 140, 105, 20), "Roundness", NULL, roundness, 0.0, 1.0)
            line_thick = GuiSliderBar(Rectangle(640, 170, 105, 20), "Thickness", NULL, line_thick, 0, 20)
            segments = GuiSliderBar(Rectangle(640, 240, 105, 20), "Segments", NULL, segments, 0, 60)

            draw_rounded_rect = GuiCheckBox(Rectangle(640, 320, 20, 20), "DrawRoundedRect", draw_rounded_rect)
            draw_rounded_lines = GuiCheckBox(Rectangle(640, 350, 20, 20), "DrawRoundedLines", draw_rounded_lines)
            draw_rect = GuiCheckBox(Rectangle(640, 380, 20, 20), "DrawRect", draw_rect)
            # ------------------------------------------------------------------------------

            draw_text(f"MODE: {'MANUAL' if segments >= 4 else 'AUTO'}", 640, 280, 10,
                      MAROON if segments >= 4 else DARKGRAY)

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

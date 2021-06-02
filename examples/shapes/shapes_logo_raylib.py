# shapes_logo_raylib.py
# ******************************************************************************************
# 
#   raylib [shapes] example - Draw raylib logo using basic shapes
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

    init_window(screen_width, screen_height, "raylib [shapes] example - raylib logo using shapes")

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

            draw_rectangle(screen_width / 2 - 128, screen_height / 2 - 128, 256, 256, BLACK)
            draw_rectangle(screen_width / 2 - 112, screen_height / 2 - 112, 224, 224, RAYWHITE)
            draw_text("raylib", screen_width / 2 - 44, screen_height / 2 + 48, 50, BLACK)

            draw_text("this is NOT a texture!", 350, 370, 10, GRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

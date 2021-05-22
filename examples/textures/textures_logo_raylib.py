# textures_logo_raylib.py
# ******************************************************************************************
#
#   raylib [textures] example - Texture loading and drawing
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

    init_window(screen_width, screen_height, "raylib [textures] example - texture loading and drawing")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)
    texture: Texture2D = load_texture("resources/raylib_logo.png")  # Texture loading
    # ---------------------------------------------------------------------------------------

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

            draw_texture(texture, screen_width / 2 - texture.width / 2, screen_height / 2 - texture.height / 2, WHITE)

            draw_text("this IS a texture!", 360, 370, 10, GRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(texture)  # Texture unloading

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

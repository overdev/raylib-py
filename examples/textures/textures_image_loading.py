# textures_image_loading.py
# ******************************************************************************************
#
#   raylib [textures] example - Image loading and texture creation
#
#   NOTE: Images are loaded in CPU memory (RAM) textures are loaded in GPU memory (VRAM)
#
#   This example has been created using raylib 1.3 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2015 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - image loading")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)

    image: Image = load_image("resources/raylib_logo.png")  # Loaded in CPU memory (RAM)
    texture: Texture2D = load_texture_from_image(image)  # Image converted to texture, GPU memory (VRAM)

    unload_image(image)  # Once image has been converted to texture and uploaded to VRAM, it can be unloaded from RAM
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

            draw_text("this IS a texture loaded from an image!", 300, 370, 10, GRAY)

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

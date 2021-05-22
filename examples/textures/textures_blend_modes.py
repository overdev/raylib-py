# textures_blend_modes.py
# ******************************************************************************************
#
#   raylib [textures] example - blend modes
#
#   NOTE: Images are loaded in CPU memory (RAM) textures are loaded in GPU memory (VRAM)
#
#   This example has been created using raylib 3.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Example contributed by Karlo Licudine (@accidentalrebel) and reviewed by Ramon Santamaria (@raysan5)
#
#   Copyright (c) 2020 Karlo Licudine (@accidentalrebel)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *
from typing import Union


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - blend modes")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)
    bg_image: Image = load_image("resources/cyberpunk_street_background.png")  # Loaded in CPU memory (RAM)
    bg_texture: Texture2D = load_texture_from_image(bg_image)  # Image converted to texture, GPU memory (VRAM)

    fg_image: Image = load_image("resources/cyberpunk_street_foreground.png")  # Loaded in CPU memory (RAM)
    fg_texture: Texture2D = load_texture_from_image(fg_image)  # Image converted to texture, GPU memory (VRAM)

    # Once image has been converted to texture and uploaded to VRAM, it can be unloaded from RAM
    unload_image(bg_image)
    unload_image(fg_image)

    blend_count_max: int = 4
    blendmode: Union[BlendMode, int] = 0

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_key_pressed(KEY_SPACE):
            if blendmode >= blend_count_max - 1:
                blendmode = 0
            else:
                blendmode += 1
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_texture(bg_texture, screen_width / 2 - bg_texture.width / 2, screen_height / 2 - bg_texture.height / 2,
                         WHITE)

            # Apply the blend mode and then draw the foreground texture
            with blend_mode(blendmode):
                draw_texture(fg_texture, screen_width / 2 - fg_texture.width / 2,
                             screen_height / 2 - fg_texture.height / 2, WHITE)
            # end blend mode

            # Draw the texts
            draw_text("Press SPACE to change blend modes.", 310, 350, 10, GRAY)

            if blendmode == BLEND_ALPHA:
                draw_text("Current: BLEND_ALPHA", (screen_width / 2) - 60, 370, 10, GRAY)
            elif blendmode == BLEND_ADDITIVE:
                draw_text("Current: BLEND_ADDITIVE", (screen_width / 2) - 60, 370, 10, GRAY)
            elif blendmode == BLEND_MULTIPLIED:
                draw_text("Current: BLEND_MULTIPLIED", (screen_width / 2) - 60, 370, 10, GRAY)
            elif blendmode == BLEND_ADD_COLORS:
                draw_text("Current: BLEND_ADD_COLORS", (screen_width / 2) - 60, 370, 10, GRAY)

            draw_text("(c) Cyberpunk Street Environment by Luis Zuno (@ansimuz)", screen_width - 330,
                      screen_height - 20,
                      10, GRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(fg_texture)  # Unload foreground texture
    unload_texture(bg_texture)  # Unload background texture

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

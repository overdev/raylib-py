# textures_image_text.py
# ******************************************************************************************
#
#   raylib [texture] example - Image text drawing using TTF generated spritefont
#
#   This example has been created using raylib 1.8 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2017 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

CHARS = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'0123456789-=´[]~,.;/\\\"!@#$%¨&*()_+`{}^<>:?|"


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [texture] example - image text drawing")

    parrots: Image = load_image("resources/parrots.png")  # Load image in CPU memory (RAM)

    # TTF Font loading with custom generation parameters
    font: Font = load_font_ex("resources/KAISG.ttf", 64, 0, 0)

    # Draw over image using custom font
    image_draw_text_ex(parrots, font, "[Parrots font drawing]", Vector2(20.0, 20.0), font.baseSize, 0.0, RED)

    texture: Texture2D = load_texture_from_image(parrots)  # Image converted to texture, uploaded to GPU memory (VRAM)
    unload_image(parrots)  # Once image has been converted to texture and uploaded to VRAM, it can be unloaded from RAM

    position: Vector2 = Vector2((screen_width / 2 - texture.width / 2), (screen_height / 2 - texture.height / 2 - 20))

    show_font: bool

    set_target_fps(60)
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_key_down(KEY_SPACE):
            show_font = True
        else:
            show_font = False
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            if not show_font:
                # Draw texture with text already drawn inside
                draw_texture_v(texture, position, WHITE)

                # Draw text directly using sprite font
                draw_text_ex(font, "[Parrots font drawing]", Vector2(position.x + 20,
                                                                     position.y + 20 + 280), font.baseSize, 0.0, WHITE)
            else:
                draw_texture(font.texture, screen_width / 2 - font.texture.width / 2, 50, BLACK)

            draw_text("PRESS SPACE to SEE USED SPRITEFONT ", 290, 420, 10, DARKGRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(texture)  # Texture unloading

    unload_font(font)  # Unload custom spritefont

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

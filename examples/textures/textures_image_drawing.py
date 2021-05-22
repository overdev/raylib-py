# textures_image_drawing.py
# ******************************************************************************************
#
#   raylib [textures] example - Image loading and drawing on it
#
#   NOTE: Images are loaded in CPU memory (RAM) textures are loaded in GPU memory (VRAM)
#
#   This example has been created using raylib 1.4 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2016 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - image drawing")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)

    cat: Image = load_image("resources/cat.png")  # Load image in CPU memory (RAM)
    image_crop(cat, Rectangle(100, 10, 280, 380))  # Crop an image piece
    image_flip_horizontal(cat)  # Flip cropped image horizontally
    image_resize(cat, 150, 200)  # Resize flipped-cropped image

    parrots: Image = load_image("resources/parrots.png")  # Load image in CPU memory (RAM)

    # Draw one image over the other with a scaling of 1.5
    image_draw(parrots, cat, Rectangle(0, 0, cat.width, cat.height),
               Rectangle(30, 40, cat.width * 1.5, cat.height * 1.5), WHITE)
    image_crop(parrots, Rectangle(0, 50, parrots.width, parrots.height - 100))  # Crop resulting image

    # Draw on the image with a few image draw methods
    image_draw_pixel(parrots, 10, 10, RAYWHITE)
    image_draw_circle(parrots, 10, 10, 5, RAYWHITE)
    image_draw_rectangle(parrots, 5, 20, 10, 10, RAYWHITE)

    unload_image(cat)  # Unload image from RAM

    # Load custom font for frawing on image
    font: Font = load_font("resources/custom_jupiter_crash.png")

    # Draw over image using custom font
    image_draw_text_ex(parrots, font, "PARROTS & CAT", Vector2(300, 230), font.baseSize, -2, WHITE)

    unload_font(font)  # Unload custom spritefont (already drawn used on image)

    texture: Texture2D = load_texture_from_image(parrots)  # Image converted to texture, uploaded to GPU memory (VRAM)
    unload_image(parrots)  # Once image has been converted to texture and uploaded to VRAM, it can be unloaded from RAM

    set_target_fps(60)
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

            draw_texture(texture, screen_width / 2 - texture.width / 2, screen_height / 2 - texture.height / 2 - 40,
                         WHITE)
            draw_rectangle_lines(screen_width / 2 - texture.width / 2, screen_height / 2 - texture.height / 2 - 40,
                                 texture.width, texture.height, DARKGRAY)

            draw_text("We are drawing only one texture from various images composed!", 240, 350, 10, DARKGRAY)
            draw_text("Source images have been cropped, scaled, flipped and copied one over the other.", 190, 370, 10,
                      DARKGRAY)

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

# textures_image_generation.py
# ******************************************************************************************
#
#   raylib [textures] example - Procedural images generation
#
#   This example has been created using raylib 1.8 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2O17 Wilhem Barbier (@nounoursheureux)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

NUM_TEXTURES = 7  # Currently we have 7 generation algorithms


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - procedural images generation")

    vertical_gradient: Image = gen_image_gradient_v(screen_width, screen_height, RED, BLUE)
    horizontal_gradient: Image = gen_image_gradient_h(screen_width, screen_height, RED, BLUE)
    radial_gradient: Image = gen_image_gradient_radial(screen_width, screen_height, 0.0, WHITE, BLACK)
    checked: Image = gen_image_checked(screen_width, screen_height, 32, 32, RED, BLUE)
    white_noise: Image = gen_image_white_noise(screen_width, screen_height, 0.5)
    perlin_noise: Image = gen_image_perlin_noise(screen_width, screen_height, 50, 50, 4.0)
    cellular: Image = gen_image_cellular(screen_width, screen_height, 32)

    textures: Array[Texture2D] = (Texture2D * NUM_TEXTURES)(*(Texture2D() for _ in range(NUM_TEXTURES)))

    textures[0] = load_texture_from_image(vertical_gradient)
    textures[1] = load_texture_from_image(horizontal_gradient)
    textures[2] = load_texture_from_image(radial_gradient)
    textures[3] = load_texture_from_image(checked)
    textures[4] = load_texture_from_image(white_noise)
    textures[5] = load_texture_from_image(perlin_noise)
    textures[6] = load_texture_from_image(cellular)

    # Unload image data (CPU RAM)
    unload_image(vertical_gradient)
    unload_image(horizontal_gradient)
    unload_image(radial_gradient)
    unload_image(checked)
    unload_image(white_noise)
    unload_image(perlin_noise)
    unload_image(cellular)

    current_texture: int = 0

    set_target_fps(60)
    # ---------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():
        # Update
        # ----------------------------------------------------------------------------------
        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT) or is_key_pressed(KEY_RIGHT):
            current_texture = (current_texture + 1) % NUM_TEXTURES  # Cycle between the textures
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_texture(textures[current_texture], 0, 0, WHITE)

            draw_rectangle(30, 400, 325, 30, fade(SKYBLUE, 0.5))
            draw_rectangle_lines(30, 400, 325, 30, fade(WHITE, 0.5))
            draw_text("MOUSE LEFT BUTTON to CYCLE PROCEDURAL TEXTURES", 40, 410, 10, WHITE)

            if current_texture == 0:
                draw_text("VERTICAL GRADIENT", 560, 10, 20, RAYWHITE)
            elif current_texture == 1:
                draw_text("HORIZONTAL GRADIENT", 540, 10, 20, RAYWHITE)
            elif current_texture == 2:
                draw_text("RADIAL GRADIENT", 580, 10, 20, LIGHTGRAY)
            elif current_texture == 3:
                draw_text("CHECKED", 680, 10, 20, RAYWHITE)
            elif current_texture == 4:
                draw_text("WHITE NOISE", 640, 10, 20, RED)
            elif current_texture == 5:
                draw_text("PERLIN NOISE", 630, 10, 20, RAYWHITE)
            elif current_texture == 6:
                draw_text("CELLULAR", 670, 10, 20, RAYWHITE)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------

    # Unload textures data (GPU VRAM)
    for i in range(NUM_TEXTURES):
        unload_texture(textures[i])

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

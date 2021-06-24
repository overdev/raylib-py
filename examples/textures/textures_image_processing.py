# textures_image_processing.py
# ******************************************************************************************
#
#   raylib [textures] example - Image processing
#
#   NOTE: Images are loaded in CPU memory (RAM) textures are loaded in GPU memory (VRAM)
#
#   This example has been created using raylib 3.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2016 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from typing import List
from enum import IntEnum, auto
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

NUM_PROCESSES = 8


class ImageProcess(IntEnum):
    NONE = 0
    COLOR_GRAYSCALE = auto()
    COLOR_TINT = auto()
    COLOR_INVERT = auto()
    COLOR_CONTRAST = auto()
    COLOR_BRIGHTNESS = auto()
    FLIP_VERTICAL = auto()
    FLIP_HORIZONTAL = auto()


NONE = ImageProcess.NONE
COLOR_GRAYSCALE = ImageProcess.COLOR_GRAYSCALE
COLOR_TINT = ImageProcess.COLOR_TINT
COLOR_INVERT = ImageProcess.COLOR_INVERT
COLOR_CONTRAST = ImageProcess.COLOR_CONTRAST
COLOR_BRIGHTNESS = ImageProcess.COLOR_BRIGHTNESS
FLIP_VERTICAL = ImageProcess.FLIP_VERTICAL
FLIP_HORIZONTAL = ImageProcess.FLIP_HORIZONTAL

processText: List[str] = [
    "NO PROCESSING",
    "COLOR GRAYSCALE",
    "COLOR TINT",
    "COLOR INVERT",
    "COLOR CONTRAST",
    "COLOR BRIGHTNESS",
    "FLIP VERTICAL",
    "FLIP HORIZONTAL"
]


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - image processing")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)

    im_origin: Image = load_image("resources/parrots.png")  # Loaded in CPU memory (RAM)
    # Format image to RGBA 32bit (required for texture update) <-- ISSUE
    image_format(im_origin, PIXELFORMAT_UNCOMPRESSED_R8G8B8A8)
    texture: Texture2D = load_texture_from_image(im_origin)  # Image converted to texture, GPU memory (VRAM)

    im_copy: Image = image_copy(im_origin)

    current_process: int = NONE
    texture_reload: bool = False

    toggle_recs: List[Rectangle] = [Rectangle() for _ in range(NUM_PROCESSES)]
    mouse_hover_rec: int = -1

    for i in range(NUM_PROCESSES):
        toggle_recs[i] = Rectangle(40.0, (50 + 32 * i), 150.0, 30.0)

    set_target_fps(60)
    # ---------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------

        # Mouse toggle group logic
        for i in range(NUM_PROCESSES):
            if check_collision_point_rec(get_mouse_position(), toggle_recs[i]):
                mouse_hover_rec = i

                if is_mouse_button_released(MOUSE_BUTTON_LEFT):
                    current_process = i
                    texture_reload = True
                break
            else:
                mouse_hover_rec = -1

        # Keyboard toggle group logic
        if is_key_pressed(KEY_DOWN):
            current_process += 1
            if current_process > NUM_PROCESSES - 1:
                current_process = 0
            texture_reload = True

        elif is_key_pressed(KEY_UP):
            current_process -= 1
            if current_process < 0:
                current_process = 7
            texture_reload = True

        # Reload texture when required
        if texture_reload:
            unload_image(im_copy)  # Unload image-copy data
            im_copy = image_copy(im_origin)  # Restore image-copy from image-origin

            # NOTE: Image processing is a costly CPU process to be done every frame,
            # If image processing is required in a frame-basis, it should be done
            # with a texture and by shaders

            if current_process == COLOR_GRAYSCALE:
                image_color_grayscale(im_copy)
            elif current_process == COLOR_TINT:
                image_color_tint(im_copy, GREEN)
            elif current_process == COLOR_INVERT:
                image_color_invert(im_copy)
            elif current_process == COLOR_CONTRAST:
                image_color_contrast(im_copy, -40)
            elif current_process == COLOR_BRIGHTNESS:
                image_color_brightness(im_copy, -80)
            elif current_process == FLIP_VERTICAL:
                image_flip_vertical(im_copy)
            elif current_process == FLIP_HORIZONTAL:
                image_flip_horizontal(im_copy)

            pixels: ColorPtr = load_image_colors(im_copy)  # Load pixel data from image (RGBA 32bit)
            update_texture(texture, pixels)  # Update texture with new image data
            unload_image_colors(pixels)  # Unload pixels data from RAM

            texture_reload = False
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("IMAGE PROCESSING:", 40, 30, 10, DARKGRAY)

            # Draw rectangles
            for i in range(NUM_PROCESSES):
                draw_rectangle_rec(toggle_recs[i],
                                   SKYBLUE if i == current_process or i == mouse_hover_rec else LIGHTGRAY)
                draw_rectangle_lines(toggle_recs[i].x, toggle_recs[i].y, toggle_recs[i].width, toggle_recs[i].height,
                                     BLUE if i == current_process or i == mouse_hover_rec else GRAY)
                draw_text(processText[i],
                          toggle_recs[i].x + toggle_recs[i].width / 2 - measure_text(processText[i], 10) / 2,
                          toggle_recs[i].y + 11, 10,
                          DARKBLUE if i == current_process or i == mouse_hover_rec else DARKGRAY)

            draw_texture(texture, screen_width - texture.width - 60, screen_height / 2 - texture.height / 2, WHITE)
            draw_rectangle_lines(screen_width - texture.width - 60,
                                 screen_height / 2 - texture.height / 2,
                                 texture.width,
                                 texture.height, BLACK)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(texture)  # Unload texture from VRAM
    unload_image(im_origin)  # Unload image-origin from RAM
    unload_image(im_copy)  # Unload image-copy from RAM

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# textures_bunnymark.py
# ******************************************************************************************
#
#   raylib [textures] example - Bunnymark
#
#   This example has been created using raylib 1.6 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2014-2019 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *
from ctypes import Structure

MAX_BUNNIES = 50000  # 50K bunnies limit

# This is the maximum amount of elements (quads) per batch
# NOTE: This value is defined in [rlgl] module and can be changed there
MAX_BATCH_ELEMENTS = 8192


class Bunny(Structure):
    _fields_ = [
        ('position', Vector2),
        ('speed', Vector2),
        ('color', Color)
    ]


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - bunnymark")

    # Load bunny texture
    tex_bunny: Texture2D = load_texture("resources/wabbit_alpha.png")

    bunnies: Array = (Bunny * MAX_BUNNIES)(*(Bunny() for _ in range(MAX_BUNNIES)))  # Bunnies array

    bunnies_count: int = 0  # Bunnies counter

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            # Create more bunnies
            for i in range(100):
                if bunnies_count < MAX_BUNNIES:
                    bunnies[bunnies_count].position = get_mouse_position()
                    bunnies[bunnies_count].speed.x = get_random_value(-250, 250) / 60.0
                    bunnies[bunnies_count].speed.y = get_random_value(-250, 250) / 60.0
                    bunnies[bunnies_count].color = Color(get_random_value(50, 240),
                                                         get_random_value(80, 240),
                                                         get_random_value(100, 240), 255)
                    bunnies_count += 1

        # Update bunnies
        for i in range(bunnies_count):
            bunnies[i].position.x += bunnies[i].speed.x
            bunnies[i].position.y += bunnies[i].speed.y

            if (((bunnies[i].position.x + tex_bunny.width / 2) > get_screen_width()) or
                    ((bunnies[i].position.x + tex_bunny.width / 2) < 0)):
                bunnies[i].speed.x *= -1
            if (((bunnies[i].position.y + tex_bunny.height / 2) > get_screen_height()) or
                    ((bunnies[i].position.y + tex_bunny.height / 2 - 40) < 0)):
                bunnies[i].speed.y *= -1
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            for i in range(bunnies_count):
                # NOTE: When internal batch buffer limit is reached (MAX_BATCH_ELEMENTS),
                # a draw call is launched and buffer starts being filled again
                # before issuing a draw call, updated vertex data from internal CPU buffer is send to GPU...
                # Process of sending data is costly and it could happen that GPU data has not been completely
                # processed for drawing while new data is tried to be sent (updating current in-use buffers)
                # it could generates a stall and consequently a frame drop, limiting the number of drawn bunnies
                draw_texture(tex_bunny, bunnies[i].position.x, bunnies[i].position.y, bunnies[i].color)

            draw_rectangle(0, 0, screen_width, 40, BLACK)
            draw_text(f"bunnies: {bunnies_count}", 120, 10, 20, GREEN)
            draw_text(f"batched draw calls: {1 + bunnies_count // MAX_BATCH_ELEMENTS}", 320, 10, 20, MAROON)

            draw_fps(10, 10)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    del bunnies  # Unload bunnies data array

    unload_texture(tex_bunny)  # Unload bunny texture

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

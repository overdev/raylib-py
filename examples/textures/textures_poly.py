# textures_poly.py
# ******************************************************************************************
#
#   raylib [shapes] example - Draw Textured Polygon
#
#   This example has been created using raylib 3.7 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Example contributed by Chris Camacho (@codifies - bedroomcoders.co.uk) and
#   reviewed by Ramon Santamaria (@raysan5)
#
#   Copyright (c) 2021 Chris Camacho (@codifies) and Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from typing import List
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.math import *

MAX_POINTS = 11  # 10 points and back to the start


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    texcoords: List[Vector2] = [
        Vector2(0.75, 0.0),
        Vector2(0.25, 0.0),
        Vector2(0.0, 0.5),
        Vector2(0.0, 0.75),
        Vector2(0.25, 1.0),
        Vector2(0.375, 0.875),
        Vector2(0.625, 0.875),
        Vector2(0.75, 1.0),
        Vector2(1.0, 0.75),
        Vector2(1.0, 0.5),
        Vector2(0.75, 0.0)  # Close the poly
    ]
    points: List[Vector2] = [Vector2() for _ in range(MAX_POINTS)]
    positions: List[Vector2] = [Vector2() for _ in range(MAX_POINTS)]

    # Create the poly coords from the UV's
    # you don't have to do this you can specify
    # them however you want
    for i in range(MAX_POINTS):
        points[i].x = (texcoords[i].x - 0.5) * 256.0
        points[i].y = (texcoords[i].y - 0.5) * 256.0

    init_window(screen_width, screen_height, "raylib [textures] example - textured polygon")

    texture: Texture2D = load_texture("resources/cat.png")

    ang: float = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        ang += 1

        for i in range(MAX_POINTS):
            positions[i] = vector2_rotate(points[i], ang)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("textured polygon", 20, 20, 20, DARKGRAY)

            draw_texture_poly(texture, Vector2(get_screen_width() / 2, get_screen_height() / 2),
                              positions, texcoords, MAX_POINTS, WHITE)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(texture)  # Unload texture

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

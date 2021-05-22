# textures_srcrec_dstrec.py
# ******************************************************************************************
#
#   raylib [textures] example - Texture source and destination rectangles
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

    init_window(screen_width, screen_height, "raylib [textures] examples - texture source and destination rectangles")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)

    scarfy: Texture2D = load_texture("resources/scarfy.png")  # Texture loading

    frame_width: int = scarfy.width / 6
    frame_height: int = scarfy.height

    # Source rectangle (part of the texture to use for drawing)
    source_rec: Rectangle = Rectangle(0.0, 0.0, frame_width, frame_height)

    # Destination rectangle (screen rectangle where drawing part of texture)
    dest_rec: Rectangle = Rectangle(screen_width / 2.0, screen_height / 2.0, frame_width * 2.0, frame_height * 2.0)

    # Origin of the texture (rotation/scale point), it's relative to destination rectangle size
    origin: Vector2 = Vector2(frame_width, frame_height)

    rotation: int = 0

    set_target_fps(60)
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        rotation += 1
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(RAYWHITE)

            # NOTE: Using draw_texture_pro() we can easily rotate and scale the part of the texture we draw
            # sourceRec defines the part of the texture we use for drawing
            # destRec defines the rectangle where our texture part will fit (scaling it to fit)
            # origin defines the point of the texture used as reference for rotation and scaling
            # rotation defines the texture rotation (using origin as rotation point)
            draw_texture_pro(scarfy, source_rec, dest_rec, origin, rotation, WHITE)

            draw_line(dest_rec.x, 0, dest_rec.x, screen_height, GRAY)
            draw_line(0, dest_rec.y, screen_width, dest_rec.y, GRAY)

            draw_text("(c) Scarfy sprite by Eiden Marsal", screen_width - 200, screen_height - 20, 10, GRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(scarfy)  # Texture unloading

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

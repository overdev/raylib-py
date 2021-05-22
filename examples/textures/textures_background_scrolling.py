# textures_background_scrolling.py
# ******************************************************************************************
#
#   raylib [textures] example - Background scrolling
#
#   This example has been created using raylib 2.0 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2019 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - background scrolling")

    # NOTE: Be careful, background width must be equal or bigger than screen width
    # if not, texture should be draw more than two times for scrolling effect
    background: Texture2D = load_texture("resources/cyberpunk_street_background.png")
    midground: Texture2D = load_texture("resources/cyberpunk_street_midground.png")
    foreground: Texture2D = load_texture("resources/cyberpunk_street_foreground.png")

    scrolling_back: float = 0.0
    scrolling_mid: float = 0.0
    scrolling_fore: float = 0.0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        scrolling_back -= 0.1
        scrolling_mid -= 0.5
        scrolling_fore -= 1.0

        # NOTE: Texture is scaled twice its size, so it sould be considered on scrolling
        if scrolling_back <= -background.width * 2:
            scrolling_back = 0
        if scrolling_mid <= -midground.width * 2:
            scrolling_mid = 0
        if scrolling_fore <= -foreground.width * 2:
            scrolling_fore = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(get_color(0x052c46ff))

            # Draw background image twice
            # NOTE: Texture is scaled twice its size
            draw_texture_ex(background, Vector2(scrolling_back, 20), 0.0, 2.0, WHITE)
            draw_texture_ex(background, Vector2(background.width * 2 + scrolling_back, 20), 0.0, 2.0, WHITE)

            # Draw midground image twice
            draw_texture_ex(midground, Vector2(scrolling_mid, 20), 0.0, 2.0, WHITE)
            draw_texture_ex(midground, Vector2(midground.width * 2 + scrolling_mid, 20), 0.0, 2.0, WHITE)

            # Draw foreground image twice
            draw_texture_ex(foreground, Vector2(scrolling_fore, 70), 0.0, 2.0, WHITE)
            draw_texture_ex(foreground, Vector2(foreground.width * 2 + scrolling_fore, 70), 0.0, 2.0, WHITE)

            draw_text("BACKGROUND SCROLLING & PARALLAX", 10, 10, 20, RED)
            draw_text("(c) Cyberpunk Street Environment by Luis Zuno (@ansimuz)", screen_width - 330,
                      screen_height - 20, 10, RAYWHITE)

        # end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(background)  # Unload background texture
    unload_texture(midground)  # Unload midground texture
    unload_texture(foreground)  # Unload foreground texture

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# textures_draw_tiled.py
# ******************************************************************************************
#
#   raylib [textures] example - Draw part of the texture tiled
#
#   This example has been created using raylib 3.0 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2020 Vlad Adrian (@demizdor) and Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def size_of(a):
    return len(a)


OPT_WIDTH = 220  # Max width for the options container
MARGIN_SIZE = 8  # Size for the margins
COLOR_SIZE = 16  # Size of the color select buttons


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    set_config_flags(FLAG_WINDOW_RESIZABLE)  # Make the window resizable
    init_window(screen_width, screen_height, "raylib [textures] example - Draw part of a texture tiled")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)
    tex_pattern: Texture2D = load_texture("resources/patterns.png")
    set_texture_filter(tex_pattern, TEXTURE_FILTER_TRILINEAR)  # Makes the texture smoother when upscaled

    # Coordinates for all patterns inside the texture
    rec_pattern: Sequence[Rectangle] = [
        Rectangle(3, 3, 66, 66),
        Rectangle(75, 3, 100, 100),
        Rectangle(3, 75, 66, 66),
        Rectangle(7, 156, 50, 50),
        Rectangle(85, 106, 90, 45),
        Rectangle(75, 154, 100, 60)
    ]

    # Setup colors
    colors: Sequence[Color] = [BLACK, MAROON, ORANGE, BLUE, PURPLE, BEIGE, LIME, RED, DARKGRAY, SKYBLUE]
    MAX_COLORS = size_of(colors)
    color_rec: Sequence[Rectangle] = [Rectangle() for _ in range(MAX_COLORS)]

    # Calculate rectangle for each color
    x = y = 0
    for i in range(MAX_COLORS):
        color_rec[i].x = 2.0 + MARGIN_SIZE + x
        color_rec[i].y = 22.0 + 256.0 + MARGIN_SIZE + y
        color_rec[i].width = COLOR_SIZE * 2.0
        color_rec[i].height = COLOR_SIZE

        if i == MAX_COLORS / 2 - 1:
            x = 0
            y += COLOR_SIZE + MARGIN_SIZE
        else:
            x += (COLOR_SIZE * 2 + MARGIN_SIZE)

    active_pattern: int = 0
    active_col: int = 0
    scale: float = 1.0
    rotation: float = 0.0

    set_target_fps(60)
    # ---------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        screen_width = get_screen_width()
        screen_height = get_screen_height()

        # Handle mouse
        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            mouse: Vector2 = get_mouse_position()

            # Check which pattern was clicked and set it as the active pattern
            for i in range(size_of(rec_pattern)):
                if check_collision_point_rec(mouse,
                                             Rectangle(
                                                 2 + MARGIN_SIZE + rec_pattern[i].x,
                                                 40 + MARGIN_SIZE + rec_pattern[i].y,
                                                 rec_pattern[i].width,
                                                 rec_pattern[i].height)):
                    active_pattern = i
                    break

            # Check to see which color was clicked and set it as the active color
            for i in range(MAX_COLORS):
                if check_collision_point_rec(mouse, color_rec[i]):
                    active_col = i
                    break

        # Handle keys

        # Change scale
        if is_key_pressed(KEY_UP):
            scale += 0.25
        if is_key_pressed(KEY_DOWN):
            scale -= 0.25
        if scale > 10.0:
            scale = 10.0
        elif scale <= 0.0:
            scale = 0.25

        # Change rotation
        if is_key_pressed(KEY_LEFT):
            rotation -= 25.0
        if is_key_pressed(KEY_RIGHT):
            rotation += 25.0

        # Reset
        if is_key_pressed(KEY_SPACE):
            rotation = 0.0
            scale = 1.0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(RAYWHITE)

            # Draw the tiled area
            draw_texture_tiled(tex_pattern, rec_pattern[active_pattern],
                               Rectangle(OPT_WIDTH + MARGIN_SIZE, MARGIN_SIZE,
                                         screen_width - OPT_WIDTH - 2.0 * MARGIN_SIZE,
                                         screen_height - 2.0 * MARGIN_SIZE),
                               Vector2(0.0, 0.0), rotation, scale, colors[active_col])

            # Draw options
            draw_rectangle(MARGIN_SIZE, MARGIN_SIZE, OPT_WIDTH - MARGIN_SIZE, screen_height - 2 * MARGIN_SIZE,
                           color_alpha(LIGHTGRAY, 0.5))

            draw_text("Select Pattern", 2 + MARGIN_SIZE, 30 + MARGIN_SIZE, 10, BLACK)
            draw_texture(tex_pattern, 2 + MARGIN_SIZE, 40 + MARGIN_SIZE, BLACK)
            draw_rectangle(2 + MARGIN_SIZE + rec_pattern[active_pattern].x,
                           40 + MARGIN_SIZE + rec_pattern[active_pattern].y, rec_pattern[active_pattern].width,
                           rec_pattern[active_pattern].height, color_alpha(DARKBLUE, 0.3))

            draw_text("Select Color", 2 + MARGIN_SIZE, 10 + 256 + MARGIN_SIZE, 10, BLACK)
            for i in range(MAX_COLORS):
                draw_rectangle_rec(color_rec[i], colors[i])
                if active_col == i:
                    draw_rectangle_lines_ex(color_rec[i], 3, color_alpha(WHITE, 0.5))

            draw_text("Scale (UP/DOWN to change)", 2 + MARGIN_SIZE, 80 + 256 + MARGIN_SIZE, 10, BLACK)
            draw_text(f"{scale}", 2 + MARGIN_SIZE, 92 + 256 + MARGIN_SIZE, 20, BLACK)

            draw_text("Rotation (LEFT/RIGHT to change)", 2 + MARGIN_SIZE, 122 + 256 + MARGIN_SIZE, 10, BLACK)
            draw_text(f"{rotation} degrees", 2 + MARGIN_SIZE, 134 + 256 + MARGIN_SIZE, 20, BLACK)

            draw_text("Press [SPACE] to reset", 2 + MARGIN_SIZE, 164 + 256 + MARGIN_SIZE, 10, DARKBLUE)

            # Draw FPS
            draw_text(f"{get_fps()} FPS", 2 + MARGIN_SIZE, 2 + MARGIN_SIZE, 20, BLACK)
        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(tex_pattern)  # Unload texture

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# textures_npatch_drawing.py
# ******************************************************************************************
#
#   raylib [textures] example - N-patch drawing
#
#   NOTE: Images are loaded in CPU memory (RAM) textures are loaded in GPU memory (VRAM)
#
#   This example has been created using raylib 2.0 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Example contributed by Jorge A. Gomes (@overdev) and reviewed by Ramon Santamaria (@raysan5)
#
#   Copyright (c) 2018 Jorge A. Gomes (@overdev) and Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - N-patch drawing")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)
    n_patch_texture: Texture2D = load_texture("resources/ninepatch_button.png")

    mouse_position: Vector2
    origin: Vector2 = Vector2()

    # Position and size of the n-patches
    dst_rec1: Rectangle = Rectangle(480.0, 160.0, 32.0, 32.0)
    dst_rec2: Rectangle = Rectangle(160.0, 160.0, 32.0, 32.0)
    dst_rec_h: Rectangle = Rectangle(160.0, 93.0, 32.0, 32.0)
    dst_rec_v: Rectangle = Rectangle(92.0, 160.0, 32.0, 32.0)

    # A 9-patch (NPATCH_NINE_PATCH) changes its sizes in both axis
    nine_patch_info1: NPatchInfo = NPatchInfo(Rectangle(0.0, 0.0, 64.0, 64.0), 12, 40, 12, 12, NPATCH_NINE_PATCH)
    nine_patch_info2: NPatchInfo = NPatchInfo(Rectangle(0.0, 128.0, 64.0, 64.0), 16, 16, 16, 16, NPATCH_NINE_PATCH)

    # A horizontal 3-patch (NPATCH_THREE_PATCH_HORIZONTAL) changes its sizes along the x axis only
    h3_patch_info: NPatchInfo = NPatchInfo(Rectangle(0.0, 64.0, 64.0, 64.0), 8, 8, 8, 8, NPATCH_THREE_PATCH_HORIZONTAL)

    # A vertical 3-patch (NPATCH_THREE_PATCH_VERTICAL) changes its sizes along the y axis only
    v3_patch_info: NPatchInfo = NPatchInfo(Rectangle(0.0, 192.0, 64.0, 64.0), 6, 6, 6, 6, NPATCH_THREE_PATCH_VERTICAL)

    set_target_fps(60)
    # ---------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        mouse_position = get_mouse_position()

        # Resize the n-patches based on mouse position
        dst_rec1.width = mouse_position.x - dst_rec1.x
        dst_rec1.height = mouse_position.y - dst_rec1.y
        dst_rec2.width = mouse_position.x - dst_rec2.x
        dst_rec2.height = mouse_position.y - dst_rec2.y
        dst_rec_h.width = mouse_position.x - dst_rec_h.x
        dst_rec_v.height = mouse_position.y - dst_rec_v.y

        # Set a minimum width and/or height
        if dst_rec1.width < 1.0:
            dst_rec1.width = 1.0
        if dst_rec1.width > 300.0:
            dst_rec1.width = 300.0
        if dst_rec1.height < 1.0:
            dst_rec1.height = 1.0
        if dst_rec2.width < 1.0:
            dst_rec2.width = 1.0
        if dst_rec2.width > 300.0:
            dst_rec2.width = 300.0
        if dst_rec2.height < 1.0:
            dst_rec2.height = 1.0
        if dst_rec_h.width < 1.0:
            dst_rec_h.width = 1.0
        if dst_rec_v.height < 1.0:
            dst_rec_v.height = 1.0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            # Draw the n-patches
            draw_texture_npatch(n_patch_texture, nine_patch_info2, dst_rec2, origin, 0.0, WHITE)
            draw_texture_npatch(n_patch_texture, nine_patch_info1, dst_rec1, origin, 0.0, WHITE)
            draw_texture_npatch(n_patch_texture, h3_patch_info, dst_rec_h, origin, 0.0, WHITE)
            draw_texture_npatch(n_patch_texture, v3_patch_info, dst_rec_v, origin, 0.0, WHITE)

            # Draw the source texture
            draw_rectangle_lines(5, 88, 74, 266, BLUE)
            draw_texture(n_patch_texture, 10, 93, WHITE)
            draw_text("TEXTURE", 15, 360, 10, DARKGRAY)

            draw_text("Move the mouse to stretch or shrink the n-patches", 10, 20, 20, DARKGRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(n_patch_texture)  # Texture unloading

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

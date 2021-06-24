# shapes_rectangle_scaling.py
# ******************************************************************************************
# 
#   raylib [shapes] example - rectangle scaling by mouse
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Example contributed by Vlad Adrian (@demizdor) and reviewed by Ramon Santamaria (@raysan5)
# 
#   Copyright (c) 2018 Vlad Adrian (@demizdor) and Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MOUSE_SCALE_MARK_SIZE = 12


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - rectangle scaling mouse")

    rec: Rectangle = Rectangle(100, 100, 200, 80)

    mouse_position: Vector2

    mouse_scale_ready: bool
    mouse_scale_mode: bool = False

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        mouse_position = get_mouse_position()

        if (check_collision_point_rec(mouse_position, rec) and
                check_collision_point_rec(mouse_position,
                                          Rectangle(rec.x + rec.width - MOUSE_SCALE_MARK_SIZE,
                                                    rec.y + rec.height - MOUSE_SCALE_MARK_SIZE,
                                                    MOUSE_SCALE_MARK_SIZE,
                                                    MOUSE_SCALE_MARK_SIZE))):
            mouse_scale_ready = True
            if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
                mouse_scale_mode = True
        else:
            mouse_scale_ready = False

        if mouse_scale_mode:
            mouse_scale_ready = True

            rec.width = (mouse_position.x - rec.x)
            rec.height = (mouse_position.y - rec.y)

            if rec.width < MOUSE_SCALE_MARK_SIZE:
                rec.width = MOUSE_SCALE_MARK_SIZE
            if rec.height < MOUSE_SCALE_MARK_SIZE:
                rec.height = MOUSE_SCALE_MARK_SIZE

            if is_mouse_button_released(MOUSE_BUTTON_LEFT):
                mouse_scale_mode = False
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("Scale rectangle dragging from bottom-right corner!", 10, 10, 20, GRAY)

            draw_rectangle_rec(rec, fade(GREEN, 0.5))

            if mouse_scale_ready:
                draw_rectangle_lines_ex(rec, 1, RED)
                draw_triangle(Vector2(rec.x + rec.width - MOUSE_SCALE_MARK_SIZE, rec.y + rec.height),
                              Vector2(rec.x + rec.width, rec.y + rec.height),
                              Vector2(rec.x + rec.width, rec.y + rec.height - MOUSE_SCALE_MARK_SIZE), RED)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# shapes_following_eyes.py
# ******************************************************************************************
# 
#   raylib [shapes] example - following eyes
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2013-2019 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/


from math import atan2, sin, cos
from raylibpy.colors import *
from raylibpy.spartan import *


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - following eyes")

    sclera_left_position: Vector2 = Vector2(get_screen_width() / 2.0 - 100.0, get_screen_height() / 2.0)
    sclera_right_position: Vector2 = Vector2(get_screen_width() / 2.0 + 100.0, get_screen_height() / 2.0)
    sclera_radius: float = 80

    iris_left_position: Vector2 = Vector2(get_screen_width() / 2.0 - 100.0, get_screen_height() / 2.0)
    iris_right_position: Vector2 = Vector2(get_screen_width() / 2.0 + 100.0, get_screen_height() / 2.0)
    iris_radius: float = 24

    angle: float = 0.0
    dx: float = 0.0
    dy: float = 0.0
    dxx: float = 0.0
    dyy: float = 0.0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        iris_left_position = get_mouse_position()
        iris_right_position = get_mouse_position()

        # Check not inside the left eye sclera
        if not check_collision_point_circle(iris_left_position, sclera_left_position, sclera_radius - 20):
            dx = iris_left_position.x - sclera_left_position.x
            dy = iris_left_position.y - sclera_left_position.y

            angle = atan2(dy, dx)

            dxx = (sclera_radius - iris_radius) * cos(angle)
            dyy = (sclera_radius - iris_radius) * sin(angle)

            iris_left_position.x = sclera_left_position.x + dxx
            iris_left_position.y = sclera_left_position.y + dyy

        # Check not inside the right eye sclera
        if not check_collision_point_circle(iris_right_position, sclera_right_position, sclera_radius - 20):
            dx = iris_right_position.x - sclera_right_position.x
            dy = iris_right_position.y - sclera_right_position.y

            angle = atan2(dy, dx)

            dxx = (sclera_radius - iris_radius) * cos(angle)
            dyy = (sclera_radius - iris_radius) * sin(angle)

            iris_right_position.x = sclera_right_position.x + dxx
            iris_right_position.y = sclera_right_position.y + dyy
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_circle_v(sclera_left_position, sclera_radius, LIGHTGRAY)
            draw_circle_v(iris_left_position, iris_radius, BROWN)
            draw_circle_v(iris_left_position, 10, BLACK)

            draw_circle_v(sclera_right_position, sclera_radius, LIGHTGRAY)
            draw_circle_v(iris_right_position, iris_radius, DARKGREEN)
            draw_circle_v(iris_right_position, 10, BLACK)

            draw_fps(10, 10)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

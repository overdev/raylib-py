# shapes_collision_area.py
# ******************************************************************************************
# 
#   raylib [shapes] example - collision area
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2013-2019 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


# include <stdlib.h>     # Required for abs()

def main() -> int:
    # Initialization
    # ---------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - collision area")

    # Box A: Moving box
    box_a: Rectangle = Rectangle(10, get_screen_height() / 2 - 50, 200, 100)
    box_a_speed_x: int = 4

    # Box B: Mouse moved box
    box_b: Rectangle = Rectangle(get_screen_width() / 2 - 30, get_screen_height() / 2 - 30, 60, 60)

    box_collision: Rectangle = Rectangle(0)  # Collision rectangle

    screen_upper_limit: int = 40  # Top menu limits

    pause: bool = False  # Movement pause
    collision: bool  # Collision detection

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # -----------------------------------------------------
        # Move box if not paused
        if not pause:
            box_a.x += box_a_speed_x

        # Bounce box on x screen limits
        if box_a.x + box_a.width >= get_screen_width() or box_a.x <= 0:
            box_a_speed_x *= -1

        # Update player-controlled-box (box02)
        box_b.x = get_mouse_x() - box_b.width / 2
        box_b.y = get_mouse_y() - box_b.height / 2

        # Make sure Box B does not go out of move area limits
        if box_b.x + box_b.width >= get_screen_width():
            box_b.x = get_screen_width() - box_b.width
        elif box_b.x <= 0:
            box_b.x = 0

        if box_b.y + box_b.height >= get_screen_height():
            box_b.y = get_screen_height() - box_b.height
        elif box_b.y <= screen_upper_limit:
            box_b.y = screen_upper_limit

        # Check boxes collision
        collision = check_collision_recs(box_a, box_b)

        # Get collision rectangle (only on collision)
        if collision:
            box_collision = get_collision_rec(box_a, box_b)

        # Pause Box A movement
        if is_key_pressed(KEY_SPACE):
            pause = not pause
        # -----------------------------------------------------

        # Draw
        # -----------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_rectangle(0, 0, screen_width, screen_upper_limit, RED if collision else BLACK)

            draw_rectangle_rec(box_a, GOLD)
            draw_rectangle_rec(box_b, BLUE)

            if collision:
                # Draw collision area
                draw_rectangle_rec(box_collision, LIME)

                # Draw collision message
                draw_text("COLLISION!", get_screen_width() / 2 - measure_text("COLLISION!", 20) / 2,
                          screen_upper_limit / 2 - 10, 20, BLACK)

                # Draw collision area
                draw_text(f"Collision Area: {box_collision.width * box_collision.height}",
                          get_screen_width() / 2 - 100, screen_upper_limit + 10, 20, BLACK)

            draw_fps(10, 10)

        # end drawing
        # -----------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

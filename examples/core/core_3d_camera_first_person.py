# core_3d_camera_first_person.py

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_COLUMNS = 20


def main():
    # Initialization
    # ---------------------------------------------------------------
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, "raylib [core] example - 3d camera 1st person")

    # Define the camera to look into our 3d world (position, target, up vector)
    camera = Camera(
        Vector3(4.0, 2.0, 4.0),
        Vector3(0.0, 1.8, 0.0),
        Vector3(0.0, 1.0, 0.0),
        60.0,
        CAMERA_PERSPECTIVE
    )

    # Generates some random columns
    heights = []
    positions = []
    colors = []

    for i in range(MAX_COLUMNS):
        heights.append(get_random_value(1, 12))
        positions.append(Vector3(
            get_random_value(-15, 15),
            heights[-1] / 2,
            get_random_value(-15, 15)
        )
        )
        colors.append(Color(
            get_random_value(20, 255),
            get_random_value(10, 55),
            30,
            255
        )
        )

    set_camera_mode(camera, CAMERA_FIRST_PERSON)

    set_target_fps(60)
    # ---------------------------------------------------------------

    # Main game loop
    while not window_should_close():

        # Update
        # -----------------------------------------------------------
        update_camera(camera)
        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)

        draw_plane(Vector3(0.0, 0.0, 0.0), Vector2(32.0, 32.0), LIGHTGRAY)
        draw_cube(Vector3(-16.0, 2.5, 0.0), 1.0, 5.0, 32.0, BLUE)
        draw_cube(Vector3(16.0, 2.5, 0.0), 1.0, 5.0, 32.0, LIME)
        draw_cube(Vector3(0.0, 2.5, 16.0), 32.0, 5.0, 1.0, GOLD)

        # Draw some cubes around
        for i, position in enumerate(positions):
            draw_cube(position, 2.0, heights[i], 2.0, colors[i])
            draw_cube_wires(position, 2.0, heights[i], 2.0, MAROON)

        draw_rectangle(camera.target.x, -500, 1, screen_height * 4, GREEN)
        draw_rectangle(-500, camera.target.y, screen_width * 4, 1, GREEN)

        end_mode3d()

        # draw_text(b"SCREEN AREA", 640, 10, 20, RED)

        draw_rectangle(10, 10, 220, 70, fade(SKYBLUE, 0.5))
        draw_rectangle_lines(10, 10, 220, 70, BLUE)

        draw_text("First person camera default controls:", 20, 20, 10, BLACK)
        draw_text("- Move with keys: W, A, S, D", 40, 40, 10, DARKGRAY)
        draw_text("- Mouse move to look around", 40, 60, 10, DARKGRAY)

        end_drawing()
        # -----------------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ---------------------------------------------------------------


if __name__ == '__main__':
    main()

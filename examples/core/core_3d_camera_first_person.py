# core_3d_camera_first_person.py

import raylibpy as rl
from ctypes import byref

MAX_COLUMNS = 20


def main():

    # Initialization
    # ---------------------------------------------------------------
    screen_width = 800
    screen_height = 450

    rl.init_window(screen_width, screen_height, "raylib [core] example - 3d camera 1st person")

    # Define the camera to look into our 3d world (position, target, up vector)
    camera = rl.Camera(
        rl.Vector3(4.0, 2.0, 4.0),
        rl.Vector3(0.0, 1.8, 0.0),
        rl.Vector3(0.0, 1.0, 0.0),
        60.0,
        rl.CAMERA_PERSPECTIVE
    )

    # Generates some random columns
    heights = []
    positions = []
    colors = []

    for i in range(MAX_COLUMNS):
        heights.append(rl.get_random_value(1, 12))
        positions.append(rl.Vector3(
                rl.get_random_value(-15, 15),
                heights[-1] / 2,
                rl.get_random_value(-15, 15)
            )
        )
        colors.append(rl.Color(
                rl.get_random_value(20, 255),
                rl.get_random_value(10, 55),
                30,
                255
            )
        )

    rl.set_camera_mode(camera, rl.CAMERA_FIRST_PERSON)

    rl.set_target_fps(60)
    # ---------------------------------------------------------------

    # Main game loop
    while not rl.window_should_close():

        # Update
        # -----------------------------------------------------------
        rl.update_camera(byref(camera))
        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)

        rl.begin_mode3d(camera)

        rl.draw_plane(rl.Vector3(0.0, 0.0, 0.0), rl.Vector2(32.0, 32.0), rl.LIGHTGRAY)
        rl.draw_cube(rl.Vector3(-16.0, 2.5, 0.0), 1.0, 5.0, 32.0, rl.BLUE)
        rl.draw_cube(rl.Vector3(16.0, 2.5, 0.0), 1.0, 5.0, 32.0, rl.LIME)
        rl.draw_cube(rl.Vector3(0.0, 2.5, 16.0), 32.0, 5.0, 1.0, rl.GOLD)

        # Draw some cubes around
        for i, position in enumerate(positions):
            rl.draw_cube(position, 2.0, heights[i], 2.0, colors[i])
            rl.draw_cube_wires(position, 2.0, heights[i], 2.0, rl.MAROON)

        rl.draw_rectangle(camera.target.x, -500, 1, screen_height * 4, rl.GREEN)
        rl.draw_rectangle(-500, camera.target.y, screen_width * 4, 1, rl.GREEN)

        rl.end_mode3d()

        # rl.draw_text(b"SCREEN AREA", 640, 10, 20, rl.RED)

        rl.draw_rectangle(10, 10, 220, 70, rl.fade(rl.SKYBLUE, 0.5))
        rl.draw_rectangle_lines(10, 10, 220, 70, rl.BLUE)
        
        rl.draw_text("First person camera default controls:", 20, 20, 10, rl.BLACK)
        rl.draw_text("- Move with keys: W, A, S, D", 40, 40, 10, rl.DARKGRAY)
        rl.draw_text("- Mouse move to look around", 40, 60, 10, rl.DARKGRAY)

        rl.end_drawing()
        # -----------------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------------
    rl.close_window()       # Close window and OpenGL context
    # ---------------------------------------------------------------


if __name__ == '__main__':
    main()
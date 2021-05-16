# *******************************************************************************************
#
#   raylib [core] example - 2d camera
#
#   This example has been created using raylib 1.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2016 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_BUILDINGS = 100


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    print('clamp:', clamp(5, 22, 25))

    init_window(screen_width, screen_height, "raylib [core] example - 2d camera")

    player: Rectangle = Rectangle(400, 280, 40, 40)
    buildings: Sequence[Rectangle] = [Rectangle() for _ in range(MAX_BUILDINGS)]
    build_colors: Sequence[Color] = [Color() for _ in range(MAX_BUILDINGS)]

    spacing: int = 0

    for i in range(MAX_BUILDINGS):
        buildings[i].width = float(get_random_value(50, 200))
        buildings[i].height = float(get_random_value(100, 800))
        buildings[i].y = screen_height - 130.0 - buildings[i].height
        buildings[i].x = -6000.0 + spacing

        spacing += int(buildings[i].width)

        # swizzling in the assignment:
        build_colors[i].rgba = get_random_value(200, 240), get_random_value(200, 240), get_random_value(200, 250), 255

    camera: Camera2D = Camera2D(
        Vector2(player.x + 20.0, player.y + 20.0),
        Vector2(screen_width / 2.0, screen_height / 2.0),
        0.0,
        1.0
    )
    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------

        # Player movement
        if is_key_down(KEY_RIGHT):
            player.x += 2
        elif is_key_down(KEY_LEFT):
            player.x -= 2

        # Camera target follows player
        camera.target = Vector2(player.x + 20, player.y + 20)

        # Camera rotation controls
        if is_key_down(KEY_A):
            camera.rotation -= 1.0
        elif is_key_down(KEY_S):
            camera.rotation += 1.0

        # Limit camera rotation to 80 degrees (-40 to 40)
        if camera.rotation > 40:
            camera.rotation = 40
        elif camera.rotation < -40:
            camera.rotation = -40

        # Camera zoom controls
        camera.zoom += float(get_mouse_wheel_move() * 0.05)

        if camera.zoom > 3.0:
            camera.zoom = 3.0
        elif camera.zoom < 0.1:
            camera.zoom = 0.1

        # Camera reset (zoom and rotation)
        if is_key_pressed(KEY_R):
            camera.zoom = 1.0
            camera.rotation = 0.0

        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            with mode2d(camera):
                draw_rectangle(-6000, 320, 13000, 8000, DARKGRAY)

                for i in range(MAX_BUILDINGS):
                    draw_rectangle_rec(buildings[i], build_colors[i])

                draw_rectangle_rec(player, RED)

                draw_line(camera.target.x, -screen_height * 10, camera.target.x, screen_height * 10, GREEN)
                draw_line(-screen_width * 10, camera.target.y, screen_width * 10, camera.target.y, GREEN)

            # end_mode2d()

            draw_text("SCREEN AREA", 640, 10, 20, RED)

            draw_rectangle(0, 0, screen_width, 5, RED)
            draw_rectangle(0, 5, 5, screen_height - 10, RED)
            draw_rectangle(screen_width - 5, 5, 5, screen_height - 10, RED)
            draw_rectangle(0, screen_height - 5, screen_width, 5, RED)

            draw_rectangle(10, 10, 250, 113, fade(SKYBLUE, 0.5))
            draw_rectangle_lines(10, 10, 250, 113, BLUE)

            draw_text("Free 2d camera controls:", 20, 20, 10, BLACK)
            draw_text("- Right/Left to move Offset", 40, 40, 10, DARKGRAY)
            draw_text("- Mouse Wheel to Zoom in-out", 40, 60, 10, DARKGRAY)
            draw_text("- A / S to Rotate", 40, 80, 10, DARKGRAY)
            draw_text("- R to reset Zoom and Rotation", 40, 100, 10, DARKGRAY)

        # end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


# ------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()

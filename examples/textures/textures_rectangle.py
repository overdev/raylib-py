# textures_rectangle.py
# ******************************************************************************************
#
#   raylib [textures] example - Texture loading and drawing a part defined by a rectangle
#
#   This example has been created using raylib 1.3 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2014 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_FRAME_SPEED = 15
MIN_FRAME_SPEED = 1


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [texture] example - texture rectangle")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)
    scarfy: Texture2D = load_texture("resources/scarfy.png")  # Texture loading

    position: Vector2 = Vector2(350.0, 280.0)
    frame_rec: Rectangle = Rectangle(0.0, 0.0, scarfy.width / 6, scarfy.height)
    current_frame: int = 0

    frames_counter: int = 0
    frames_speed: int = 8  # Number of spritesheet frames shown by second

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        frames_counter += 1

        if frames_counter >= (60 / frames_speed):
            frames_counter = 0
            current_frame += 1

            if current_frame > 5:
                current_frame = 0

            frame_rec.x = current_frame * scarfy.width / 6

        if is_key_pressed(KEY_RIGHT):
            frames_speed += 1
        elif is_key_pressed(KEY_LEFT):
            frames_speed -= 1

        if frames_speed > MAX_FRAME_SPEED:
            frames_speed = MAX_FRAME_SPEED
        elif frames_speed < MIN_FRAME_SPEED:
            frames_speed = MIN_FRAME_SPEED
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_texture(scarfy, 15, 40, WHITE)
            draw_rectangle_lines(15, 40, scarfy.width, scarfy.height, LIME)
            draw_rectangle_lines(15 + frame_rec.x, 40 + frame_rec.y, frame_rec.width, frame_rec.height, RED)

            draw_text("FRAME SPEED: ", 165, 210, 10, DARKGRAY)
            draw_text(f"{frames_speed} FPS", 575, 210, 10, DARKGRAY)
            draw_text("PRESS RIGHT/LEFT KEYS to CHANGE SPEED!", 290, 240, 10, DARKGRAY)

            for i in range(MAX_FRAME_SPEED):
                if i < frames_speed:
                    draw_rectangle(250 + 21 * i, 205, 20, 20, RED)
                draw_rectangle_lines(250 + 21 * i, 205, 20, 20, MAROON)

            draw_texture_rec(scarfy, frame_rec, position, WHITE)  # Draw part of the texture

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

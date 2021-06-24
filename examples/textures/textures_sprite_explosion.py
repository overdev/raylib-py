# textures_sprite_explosion.py
# ******************************************************************************************
#
#   raylib [textures] example - sprite explosion
#
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2019 Anata and Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

NUM_FRAMES_PER_LINE = 5
NUM_LINES = 5


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - sprite explosion")

    init_audio_device()

    # Load explosion sound
    fx_boom: Sound = load_sound("resources/boom.wav")

    # Load explosion texture
    explosion: Texture2D = load_texture("resources/explosion.png")

    # Init variables for animation
    frame_width: float = explosion.width / NUM_FRAMES_PER_LINE  # Sprite one frame rectangle width
    frame_height: float = explosion.height / NUM_LINES  # Sprite one frame rectangle height
    current_frame: int = 0
    current_line: int = 0

    frame_rec: Rectangle = Rectangle(0, 0, frame_width, frame_height)
    position: Vector2 = Vector2(0.0, 0.0)

    active: bool = False
    frames_counter: int = 0

    set_target_fps(120)
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------

        # Check for mouse button pressed and activate explosion (if not active)
        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT) and not active:
            position = get_mouse_position()
            active = True

            position.x -= frame_width / 2.0
            position.y -= frame_height / 2.0

            play_sound(fx_boom)

        # Compute explosion animation frames
        if active:
            frames_counter += 1

            if frames_counter > 2:
                current_frame += 1

                if current_frame >= NUM_FRAMES_PER_LINE:
                    current_frame = 0
                    current_line += 1

                    if current_line >= NUM_LINES:
                        current_line = 0
                        active = False

                frames_counter = 0

        frame_rec.x = frame_width * current_frame
        frame_rec.y = frame_height * current_line
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            # Draw explosion required frame rectangle
            if active:
                draw_texture_rec(explosion, frame_rec, position, WHITE)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(explosion)  # Unload texture
    unload_sound(fx_boom)  # Unload sound

    close_audio_device()

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

# textures_sprite_button.py
# ******************************************************************************************
#
#   raylib [textures] example - sprite button
#
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2019 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

NUM_FRAMES = 3  # Number of frames (rectangles) for the button sprite texture


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - sprite button")

    init_audio_device()  # Initialize audio device

    fx_button: Sound = load_sound("resources/buttonfx.wav")  # Load button sound
    button: Texture2D = load_texture("resources/button.png")  # Load button texture

    # Define frame rectangle for drawing
    frame_height: float = button.height / NUM_FRAMES
    source_rec: Rectangle = Rectangle(0, 0, button.width, frame_height)

    # Define button bounds on screen
    btn_bounds: Rectangle = Rectangle(screen_width / 2.0 - button.width / 2.0,
                                      screen_height / 2.0 - button.height / NUM_FRAMES / 2.0,
                                      button.width, frame_height)

    btn_state: int  # Button state: 0-NORMAL, 1-MOUSE_HOVER, 2-PRESSED
    btn_action: bool  # Button action should be activated

    mouse_point: Vector2

    set_target_fps(60)
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        mouse_point = get_mouse_position()
        btn_action = False

        # Check button state
        if check_collision_point_rec(mouse_point, btn_bounds):
            if is_mouse_button_down(MOUSE_BUTTON_LEFT):
                btn_state = 2
            else:
                btn_state = 1

            if is_mouse_button_released(MOUSE_BUTTON_LEFT):
                btn_action = True
        else:
            btn_state = 0

        if btn_action:
            play_sound(fx_button)

            # TODO: Any desired action

        # Calculate button frame rectangle to draw depending on button state
        source_rec.y = btn_state * frame_height
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_texture_rec(button, source_rec, Vector2(btn_bounds.x, btn_bounds.y), WHITE)  # Draw button frame

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(button)  # Unload button texture
    unload_sound(fx_button)  # Unload sound

    close_audio_device()  # Close audio device

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

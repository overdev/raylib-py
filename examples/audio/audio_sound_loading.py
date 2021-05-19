# audio_sound_loading.py
# ******************************************************************************************
# 
#   raylib [audio] example - Sound loading and playing
# 
#   This example has been created using raylib 1.0 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2014 Ramon Santamaria (@raysan5)
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

    init_window(screen_width, screen_height, "raylib [audio] example - sound loading and playing")

    init_audio_device()  # Initialize audio device

    fx_wav: Sound = load_sound("resources/sound.wav")  # Load WAV audio file
    fx_ogg: Sound = load_sound("resources/target.ogg")  # Load OGG audio file

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key

        # Update
        # ----------------------------------------------------------------------------------
        if is_key_pressed(KEY_SPACE):
            play_sound(fx_wav)  # Play WAV sound
        if is_key_pressed(KEY_ENTER):
            play_sound(fx_ogg)  # Play OGG sound
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("Press SPACE to PLAY the WAV sound!", 200, 180, 20, LIGHTGRAY)
            draw_text("Press ENTER to PLAY the OGG sound!", 200, 220, 20, LIGHTGRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_sound(fx_wav)  # Unload sound data
    unload_sound(fx_ogg)  # Unload sound data

    close_audio_device()  # Close audio device

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

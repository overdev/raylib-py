# audio_multichannel_sound.py
# ******************************************************************************************
# 
#   raylib [audio] example - Multichannel sound playing
# 
#   This example has been created using raylib 2.6 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Example contributed by Chris Camacho (@chriscamacho) and reviewed by Ramon Santamaria (@raysan5)
# 
#   Copyright (c) 2019 Chris Camacho (@chriscamacho) and Ramon Santamaria (@raysan5)
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

    init_window(screen_width, screen_height, "raylib [audio] example - Multichannel sound playing")

    init_audio_device()  # Initialize audio device

    fx_wav: Sound = load_sound("resources/sound.wav")  # Load WAV audio file
    fx_ogg: Sound = load_sound("resources/target.ogg")  # Load OGG audio file

    set_sound_volume(fx_wav, 0.2)

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key

        # Update
        # ----------------------------------------------------------------------------------
        if is_key_pressed(KEY_ENTER):
            play_sound_multi(fx_wav)  # Play a new wav sound instance
        if is_key_pressed(KEY_SPACE):
            play_sound_multi(fx_ogg)  # Play a new ogg sound instance
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("MULTICHANNEL SOUND PLAYING", 20, 20, 20, GRAY)
            draw_text("Press SPACE to play new ogg instance!", 200, 120, 20, LIGHTGRAY)
            draw_text("Press ENTER to play new wav instance!", 200, 180, 20, LIGHTGRAY)

            draw_text(f"CONCURRENT SOUNDS PLAYING: {get_sounds_playing()}", 220, 280, 20, RED)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    stop_sound_multi()  # We must stop the buffer pool before unloading

    unload_sound(fx_wav)  # Unload sound data
    unload_sound(fx_ogg)  # Unload sound data

    close_audio_device()  # Close audio device

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

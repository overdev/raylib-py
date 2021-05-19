# audio_music_stream.py
# ******************************************************************************************
# 
#   raylib [audio] example - Music playing (streaming)
# 
#   This example has been created using raylib 1.3 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2015 Ramon Santamaria (@raysan5)
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

    init_window(screen_width, screen_height, "raylib [audio] example - music playing (streaming)")

    init_audio_device()  # Initialize audio device

    music: Music = load_music_stream("resources/country.mp3")

    play_music_stream(music)

    time_played: float
    pause: bool = False

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key

        # Update
        # ----------------------------------------------------------------------------------
        update_music_stream(music)  # Update music buffer with new stream data

        # Restart music playing (stop and play)
        if is_key_pressed(KEY_SPACE):
            stop_music_stream(music)
            play_music_stream(music)

        # Pause/Resume music playing
        if is_key_pressed(KEY_P):

            pause = not pause

            if pause:
                pause_music_stream(music)
            else:
                resume_music_stream(music)

        # Get timePlayed scaled to bar dimensions (400 pixels)
        time_played = get_music_time_played(music) / get_music_time_length(music) * 400

        if time_played > 400:
            stop_music_stream(music)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text("MUSIC SHOULD BE PLAYING!", 255, 150, 20, LIGHTGRAY)

            draw_rectangle(200, 200, 400, 12, LIGHTGRAY)
            draw_rectangle(200, 200, time_played, 12, MAROON)
            draw_rectangle_lines(200, 200, 400, 12, GRAY)

            draw_text("PRESS SPACE TO RESTART MUSIC", 215, 250, 20, LIGHTGRAY)
            draw_text("PRESS P TO PAUSE/RESUME MUSIC", 208, 280, 20, LIGHTGRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_music_stream(music)  # Unload music stream buffers from RAM

    close_audio_device()  # Close audio device (music streaming is automatically stopped)

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

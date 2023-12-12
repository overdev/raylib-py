# -------------------------------------------------------------------------------------------------
# 
#    raylib [audio] example - Music playing (streaming)
# 
#    Example originally created with raylib 1.3, last time updated with raylib 4.0
# 
#    Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#    BSD-like license that allows static linking with closed source software
#
#    This example require some resources to be loaded. To run without loading errors, please,
#    make sure you have the original C raylib examples in your machine. Then, provide the directory
#    path where the original c example source is located:
#
#    $ py audio_music_stream.py path/to/raylib/examples/audio
#
#    Copyright (c) 2015-2023 Ramon Santamaria (@raysan5)
# 
# -------------------------------------------------------------------------------------------------

import sys
import os
from ctypes import byref
from raylibpy import *

def main():
    """Program main entrypoint"""

    # initialization
    # ---------------------------------------------------------------------------------------------
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [audio] example - music playing (streaming)")
    init_audio_device()
    music = load_music_stream("resources/country.mp3")
    play_music_stream(music)
    timePlayed = 0.0
    pause = False

    set_target_fps(30)
    
    # Main Game Loop
    # ---------------------------------------------------------------------------------------------
    while not window_should_close():
        # Update
        # -----------------------------------------------------------------------------------------
        update_music_stream(music)
        
        if is_key_pressed(KEY_SPACE):
            stop_music_stream(music)
            play_music_stream(music)
        
        if is_key_pressed(KEY_P):
            pause  = not pause
            
            if pause:
                pause_music_stream(music)
            else:
                resume_music_stream(music)
        timePlayed  = get_music_time_played(music) / get_music_time_length(music)
        
        if timePlayed > 1.0:
            timePlayed  = 1.0

        # Draw
        # -----------------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)
        draw_text("MUSIC SHOULD BE PLAYING!", 255, 150, 20, LIGHTGRAY)
        draw_rectangle(200, 200, 400, 12, LIGHTGRAY)
        draw_rectangle(200, 200, int(timePlayed * 400.0), 12, MAROON)
        draw_rectangle_lines(200, 200, 400, 12, GRAY)
        draw_text("PRESS SPACE TO RESTART MUSIC", 215, 250, 20, LIGHTGRAY)
        draw_text("PRESS P TO PAUSE/RESUME MUSIC", 208, 280, 20, LIGHTGRAY)

        end_drawing()

    # De-Initialization
    # ---------------------------------------------------------------------------------------------
    unload_music_stream(music)
    close_audio_device()
    close_window()
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
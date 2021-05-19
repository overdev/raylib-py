# audio_module_playing.py
# ******************************************************************************************
# 
#   raylib [audio] example - Module playing (streaming)
# 
#   This example has been created using raylib 1.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2016 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/
from ctypes import Structure, c_float
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *
from typing import Optional

MAX_CIRCLES = 64


class CircleWave(Structure):
    _fields_ = [
        ('position', Vector2),
        ('radius', c_float),
        ('alpha', c_float),
        ('speed', c_float),
        ('color', Color)
    ]

    def __init__(self, position: Optional[Vector2] = None, radius: float = 1.0, alpha: float = 0.0, speed: float = 0.0,
                 color: Optional[Color] = None):
        super().__init__(position if position else Vector2(), radius, alpha, speed, color if color else Color())


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    set_config_flags(FLAG_MSAA_4X_HINT)  # NOTE: Try to enable MSAA 4X

    init_window(screen_width, screen_height, "raylib [audio] example - module playing (streaming)")

    init_audio_device()  # Initialize audio device

    colors: Sequence[Color] = [ORANGE, RED, GOLD, LIME, BLUE, VIOLET, BROWN, LIGHTGRAY, PINK,
                               YELLOW, GREEN, SKYBLUE, PURPLE, BEIGE]

    # Creates ome circles for visual effect
    circles: Sequence[CircleWave] = [CircleWave() for _ in range(MAX_CIRCLES)]

    for i, circle in enumerate(circles):
        circle.alpha = 0.0
        circle.radius = get_random_value(10, 40)
        circle.position.x = get_random_value(circles[i].radius, (screen_width - circles[i].radius))
        circle.position.y = get_random_value(circles[i].radius, (screen_height - circles[i].radius))
        circle.speed = get_random_value(1, 100) / 2000.0
        circle.color = colors[get_random_value(0, 13)]

    music: Music = load_music_stream("resources / mini1111.xm")
    music.looping = False
    pitch: float = 1.0

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

        if is_key_down(KEY_DOWN):
            pitch -= 0.01
        elif is_key_down(KEY_UP):
            pitch += 0.01

        set_music_pitch(music, pitch)

        # Get timePlayed scaled to bar dimensions
        time_played = get_music_time_played(music) / get_music_time_length(music) * (screen_width - 40)

        # Color circles animation
        for i, circle in enumerate(reversed(circles)):
            if pause:
                break

            circle.alpha += circle.speed
            circle.radius += circle.speed * 10.0

            if circle.alpha > 1.0:
                circle.speed *= -1

            if circle.alpha <= 0.0:
                circle.alpha = 0.0
                circle.radius = get_random_value(10, 40)
                circle.position.x = get_random_value(circle.radius, (screen_width - circle.radius))
                circle.position.y = get_random_value(circle.radius, (screen_height - circle.radius))
                circle.color = colors[get_random_value(0, 13)]
                circle.speed = get_random_value(1, 100) / 2000.0

        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            for circle in reversed(circles):
                draw_circle_v(circle.position, circle.radius, fade(circle.color, circle.alpha))

            # Draw time bar
            draw_rectangle(20, screen_height - 20 - 12, screen_width - 40, 12, LIGHTGRAY)
            draw_rectangle(20, screen_height - 20 - 12, time_played, 12, MAROON)
            draw_rectangle_lines(20, screen_height - 20 - 12, screen_width - 40, 12, GRAY)

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

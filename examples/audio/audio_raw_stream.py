# audio_raw_stream.py
# ******************************************************************************************
# 
#   raylib [audio] example - Raw audio streaming
# 
#   This example has been created using raylib 1.6 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Example created by Ramon Santamaria (@raysan5) and reviewed by James Hofmann (@triplefox)
# 
#   Copyright (c) 2015-2019 Ramon Santamaria (@raysan5) and James Hofmann (@triplefox)
# 
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *
from raylibpy.math import PI
from raylibpy._types import Short
from math import sin

MAX_SAMPLES = 512
MAX_SAMPLES_PER_UPDATE = 4096


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [audio] example - raw audio streaming")

    init_audio_device()  # Initialize audio device

    # Init raw audio stream (sample rate: 22050, sample size: 16bit-short, channels: 1-mono)
    stream: AudioStream = init_audio_stream(22050, 16, 1)

    # Buffer for the single cycle waveform we are synthesizing
    data: Array = (Short * MAX_SAMPLES)(*(0 for _ in range(MAX_SAMPLES)))

    # Frame buffer, describing the waveform when repeated over the course of a frame
    write_buf: Array = (Short * MAX_SAMPLES_PER_UPDATE)(*(0 for _ in range(MAX_SAMPLES_PER_UPDATE)))

    play_audio_stream(stream)  # Start processing stream buffer (no data loaded currently)

    # Position read in to determine next frequency
    mouse_position: Vector2  # Vector2(-100.0, -100.0)

    # Cycles per second (hz)
    frequency: float = 440.0

    # Previous value, used to test if sine needs to be rewritten, and to smoothly modulate frequency
    old_frequency: float = 1.0

    # Cursor to read and copy the samples of the sine wave buffer
    read_cursor: int = 0

    # Computed size in samples of the sine wave
    wave_length: int = 1

    position: Vector2 = Vector2()

    set_target_fps(30)  # Set our game to run at 30 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key

        # Update
        # ----------------------------------------------------------------------------------

        # Sample mouse input.
        mouse_position = get_mouse_position()

        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            fp: float = mouse_position.y
            frequency = 40.0 + fp

        # Rewrite the sine wave.
        # Compute two cycles to allow the buffer padding, simplifying any modulation, resampling, etc.
        if frequency != old_frequency:

            # Compute wavelength. Limit size in both directions.
            old_wavelength: int = wave_length
            wave_length = int(22050 // frequency)
            if wave_length > MAX_SAMPLES // 2:
                wave_length = MAX_SAMPLES // 2
            if wave_length < 1:
                wave_length = 1

            # Write sine wave.
            for i in range(wave_length * 2):
                data[i] = int(sin((2 * PI * i / wave_length)) * 32000)

            # Scale read cursor's position to minimize transition artifacts
            read_cursor = read_cursor * (wave_length // old_wavelength)
            old_frequency = frequency

        # Refill audio stream if required
        if is_audio_stream_processed(stream):

            # Synthesize a buffer that is exactly the requested size
            write_cursor: int = 0

            while write_cursor < MAX_SAMPLES_PER_UPDATE:

                # Start by trying to write the whole chunk at once
                write_length: int = MAX_SAMPLES_PER_UPDATE - write_cursor

                # Limit to the maximum readable size
                read_length: int = wave_length - read_cursor

                if write_length > read_length:
                    write_length = read_length

                # Write the slice
                # memcpy(write_buf + write_cursor, data + read_cursor, write_length*sizeof(short))
                write_buf[write_cursor: write_cursor + write_length] = data[read_cursor: read_cursor + write_length]

                # Update cursors and loop audio
                read_cursor = (read_cursor + write_length) % wave_length

                write_cursor += write_length

            # Copy finished frame to audio stream
            update_audio_stream(stream, write_buf, MAX_SAMPLES_PER_UPDATE)

        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_text(f"sine frequency: {frequency}", get_screen_width() - 220, 10, 20, RED)
            draw_text("click mouse button to change frequency", 10, 10, 20, DARKGRAY)

            # Draw the current buffer state proportionate to the screen
            for i in range(screen_width):
                position.x = i
                position.y = 250 + 50 * data[i * MAX_SAMPLES // screen_width] / 32000.0

                draw_pixel_v(position, RED)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    # free(data)                 # Unload sine wave data
    # free(write_buf)             # Unload write buffer

    close_audio_stream(stream)  # Close raw audio stream and delete buffers from RAM
    close_audio_device()  # Close audio device (music streaming is automatically stopped)

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

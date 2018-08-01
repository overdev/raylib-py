# core_dropped_files.py

from raylibpy import *

def main() -> int:

    # Initialization
    # -------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, b"raylibpy [core] example - drop files")

    dropped_files: list = []

    set_target_fps(60)

    # Main game loop
    while not window_should_close():
        # Update
        # ---------------------------------------------------------------------------------
        if is_file_dropped():
            dropped_files = get_dropped_files()
        # ----------------------------------------------------------------------------------

        # Draw
        # ---------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        if len(dropped_files) == 0:
            draw_text(b"Drop your files to this window!", 100, 40, 20, DARKGRAY)
        else:
            draw_text(b"Dropped files:", 100, 40, 20, DARKGRAY)

            for i, drop_file in enumerate(dropped_files):
                if i % 2 == 0:
                    draw_rectangle(0, 85 + 40 * i, screen_width, 40, fade(LIGHTGRAY, .5))
                else:
                    draw_rectangle(0, 85 + 40 * i, screen_width, 40, fade(LIGHTGRAY, .3))

                draw_text(drop_file, 120, 100 + 40 * i, 10, GRAY)

            draw_text(b"Drop new files...", 100, 110 + 40 * len(dropped_files), 20, DARKGRAY)

        end_drawing()
        # ---------------------------------------------------------------------------------

    # De-Initialization
    # -------------------------------------------------------------------------------------
    close_window()
    # -------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()
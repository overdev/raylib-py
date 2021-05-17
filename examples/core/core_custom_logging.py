# core_custom_logging.py
# ******************************************************************************************
#
#   raylib [core] example - Custom logging
#
#   This example has been created using raylib 2.1 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Example contributed by Pablo Marcos Oltra (@pamarcos) and reviewed by Ramon Santamaria (@raysan5)
#
#   Copyright (c) 2018 Pablo Marcos Oltra (@pamarcos) and Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/
import time
from typing import Union
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import (
    TraceLogLevel,
    LOG_ALL,
    LOG_TRACE,
    LOG_DEBUG,
    LOG_INFO,
    LOG_WARNING,
    LOG_ERROR,
    LOG_FATAL,
    LOG_NONE,
)


@TraceLogCallback
def log_custom(msg_type: Union[int, TraceLogLevel], text: bytes) -> None:
    """Custom logging funtion"""
    # char timeStr[64] = { 0 }
    # now: time_t = time(NULL)
    # struct tm *tm_info = localtime(&now)
    #
    # strftime(timeStr, sizeof(timeStr), "%Y-%m-%d %H:%M:%S", tm_info)
    # printf("[%s] ", timeStr)
    #
    # switch (msgType)
    #    case LOG_INFO: printf("[INFO] : ") break
    #    case LOG_ERROR: printf("[ERROR]: ") break
    #    case LOG_WARNING: printf("[WARN] : ") break
    #    case LOG_DEBUG: printf("[DEBUG]: ") break
    #    default: break
    #
    # vprintf(text, args)
    # printf("\n")
    now = time.localtime()
    timestamp = "{}-{:02}-{:02} {:02}:{:02}:{:02}".format(*now)
    loglevel = {
        LOG_ALL: 'ALL',
        LOG_TRACE: 'TRACE',
        LOG_DEBUG: 'DEBUG',
        LOG_INFO: 'INFO',
        LOG_WARNING: 'WARNING',
        LOG_ERROR: 'ERROR',
        LOG_FATAL: 'FATAL',
        LOG_NONE: 'NONE',
    }
    print(f"[{loglevel.get(msg_type, 'NONE')}] {timestamp} : {text.decode('utf8')}")


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    # First thing we do is setting our custom logger to ensure everything raylib logs
    # will use our own logger instead of its internal one
    set_trace_log_callback(log_custom)

    init_window(screen_width, screen_height, "raylib [core] example - custom logging")

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # TODO: Update your variables here
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(RAYWHITE)

            draw_text("Check out the console output to see the custom logger in action!", 60, 200, 20, LIGHTGRAY)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

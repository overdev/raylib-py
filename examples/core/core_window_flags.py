# ******************************************************************************************
#
#   raylib [core] example - window flags
#
#   This example has been created using raylib 3.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2020 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


def main() -> int:
    # Initialization
    # ---------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    # Possible window flags
    """
    FLAG_VSYNC_HINT
    FLAG_FULLSCREEN_MODE    -> not working properly -> wrong scaling!
    FLAG_WINDOW_RESIZABLE
    FLAG_WINDOW_UNDECORATED
    FLAG_WINDOW_TRANSPARENT
    FLAG_WINDOW_HIDDEN
    FLAG_WINDOW_MINIMIZED   -> Not supported on window creation
    FLAG_WINDOW_MAXIMIZED   -> Not supported on window creation
    FLAG_WINDOW_UNFOCUSED
    FLAG_WINDOW_TOPMOST
    FLAG_WINDOW_HIGHDPI     -> errors after minimize-resize, fb size is recalculated
    FLAG_WINDOW_ALWAYS_RUN
    FLAG_MSAA_4X_HINT
    """

    # Set configuration flags for window creation
    # set_config_flags(FLAG_VSYNC_HINT | FLAG_MSAA_4X_HINT | FLAG_WINDOW_HIGHDPI)
    init_window(screen_width, screen_height, "raylib [core] example - window flags")

    ball_position: Vector2 = Vector2(get_screen_width() / 2.0, get_screen_height() / 2.0)
    ball_speed: Vector2 = Vector2(5.0, 4.0)
    ball_radius: float = 20

    frames_counter: int = 0

    # set_target_fps(60)               # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # -----------------------------------------------------
        if is_key_pressed(KEY_F):
            toggle_fullscreen()  # modifies window size when scaling!

        if is_key_pressed(KEY_R):
            if is_window_state(FLAG_WINDOW_RESIZABLE):
                clear_window_state(FLAG_WINDOW_RESIZABLE)
            else:
                set_window_state(FLAG_WINDOW_RESIZABLE)

        if is_key_pressed(KEY_D):
            if is_window_state(FLAG_WINDOW_UNDECORATED):
                clear_window_state(FLAG_WINDOW_UNDECORATED)
            else:
                set_window_state(FLAG_WINDOW_UNDECORATED)

        if is_key_pressed(KEY_H):
            if not is_window_state(FLAG_WINDOW_HIDDEN):
                set_window_state(FLAG_WINDOW_HIDDEN)

            frames_counter = 0

        if is_window_state(FLAG_WINDOW_HIDDEN):
            frames_counter += 1
            if frames_counter >= 240:
                clear_window_state(FLAG_WINDOW_HIDDEN)  # Show window after 3 seconds

        if is_key_pressed(KEY_N):
            if not is_window_state(FLAG_WINDOW_MINIMIZED):
                minimize_window()

            frames_counter = 0

        if is_window_state(FLAG_WINDOW_MINIMIZED):
            frames_counter += 1
            if frames_counter >= 240:
                restore_window()  # Restore window after 3 seconds

        if is_key_pressed(KEY_M):
            # NOTE: Requires FLAG_WINDOW_RESIZABLE enabled!
            if is_window_state(FLAG_WINDOW_MAXIMIZED):
                restore_window()
            else:
                maximize_window()

        if is_key_pressed(KEY_U):
            if is_window_state(FLAG_WINDOW_UNFOCUSED):
                clear_window_state(FLAG_WINDOW_UNFOCUSED)
            else:
                set_window_state(FLAG_WINDOW_UNFOCUSED)

        if is_key_pressed(KEY_T):
            if is_window_state(FLAG_WINDOW_TOPMOST):
                clear_window_state(FLAG_WINDOW_TOPMOST)
            else:
                set_window_state(FLAG_WINDOW_TOPMOST)

        if is_key_pressed(KEY_A):
            if is_window_state(FLAG_WINDOW_ALWAYS_RUN):
                clear_window_state(FLAG_WINDOW_ALWAYS_RUN)
            else:
                set_window_state(FLAG_WINDOW_ALWAYS_RUN)

        if is_key_pressed(KEY_V):
            if is_window_state(FLAG_VSYNC_HINT):
                clear_window_state(FLAG_VSYNC_HINT)
            else:
                set_window_state(FLAG_VSYNC_HINT)

        # Bouncing ball logic
        ball_position.x += ball_speed.x
        ball_position.y += ball_speed.y
        if (ball_position.x >= (get_screen_width() - ball_radius)) or (ball_position.x <= ball_radius):
            ball_speed.x *= -1.0
        if (ball_position.y >= (get_screen_height() - ball_radius)) or (ball_position.y <= ball_radius):
            ball_speed.y *= -1.0
        # -----------------------------------------------------

        # Draw
        # -----------------------------------------------------
        with drawing():

            if is_window_state(FLAG_WINDOW_TRANSPARENT):
                clear_background(BLANK)
            else:
                clear_background(RAYWHITE)

            draw_circle_v(ball_position, ball_radius, MAROON)
            draw_rectangle_lines_ex(Rectangle(0, 0, get_screen_width(), get_screen_height()), 4, RAYWHITE)

            draw_circle_v(get_mouse_position(), 10, DARKBLUE)

            draw_fps(10, 10)

            draw_text(text_format("Screen Size: [%i, %i]", get_screen_width(), get_screen_height()), 10, 40, 10, GREEN)

            # Draw window state info
            draw_text("Following flags can be set after window creation:", 10, 60, 10, GRAY)
            if is_window_state(FLAG_FULLSCREEN_MODE):
                draw_text("[F] FLAG_FULLSCREEN_MODE: on", 10, 80, 10, LIME)
            else:
                draw_text("[F] FLAG_FULLSCREEN_MODE: off", 10, 80, 10, MAROON)
            if is_window_state(FLAG_WINDOW_RESIZABLE):
                draw_text("[R] FLAG_WINDOW_RESIZABLE: on", 10, 100, 10, LIME)
            else:
                draw_text("[R] FLAG_WINDOW_RESIZABLE: off", 10, 100, 10, MAROON)
            if is_window_state(FLAG_WINDOW_UNDECORATED):
                draw_text("[D] FLAG_WINDOW_UNDECORATED: on", 10, 120, 10, LIME)
            else:
                draw_text("[D] FLAG_WINDOW_UNDECORATED: off", 10, 120, 10, MAROON)
            if is_window_state(FLAG_WINDOW_HIDDEN):
                draw_text("[H] FLAG_WINDOW_HIDDEN: on", 10, 140, 10, LIME)
            else:
                draw_text("[H] FLAG_WINDOW_HIDDEN: off", 10, 140, 10, MAROON)
            if is_window_state(FLAG_WINDOW_MINIMIZED):
                draw_text("[N] FLAG_WINDOW_MINIMIZED: on", 10, 160, 10, LIME)
            else:
                draw_text("[N] FLAG_WINDOW_MINIMIZED: off", 10, 160, 10, MAROON)
            if is_window_state(FLAG_WINDOW_MAXIMIZED):
                draw_text("[M] FLAG_WINDOW_MAXIMIZED: on", 10, 180, 10, LIME)
            else:
                draw_text("[M] FLAG_WINDOW_MAXIMIZED: off", 10, 180, 10, MAROON)
            if is_window_state(FLAG_WINDOW_UNFOCUSED):
                draw_text("[G] FLAG_WINDOW_UNFOCUSED: on", 10, 200, 10, LIME)
            else:
                draw_text("[U] FLAG_WINDOW_UNFOCUSED: off", 10, 200, 10, MAROON)
            if is_window_state(FLAG_WINDOW_TOPMOST):
                draw_text("[T] FLAG_WINDOW_TOPMOST: on", 10, 220, 10, LIME)
            else:
                draw_text("[T] FLAG_WINDOW_TOPMOST: off", 10, 220, 10, MAROON)
            if is_window_state(FLAG_WINDOW_ALWAYS_RUN):
                draw_text("[A] FLAG_WINDOW_ALWAYS_RUN: on", 10, 240, 10, LIME)
            else:
                draw_text("[A] FLAG_WINDOW_ALWAYS_RUN: off", 10, 240, 10, MAROON)
            if is_window_state(FLAG_VSYNC_HINT):
                draw_text("[V] FLAG_VSYNC_HINT: on", 10, 260, 10, LIME)
            else:
                draw_text("[V] FLAG_VSYNC_HINT: off", 10, 260, 10, MAROON)

            draw_text("Following flags can only be set before window creation:", 10, 300, 10, GRAY)
            if is_window_state(FLAG_WINDOW_HIGHDPI):
                draw_text("FLAG_WINDOW_HIGHDPI: on", 10, 320, 10, LIME)
            else:
                draw_text("FLAG_WINDOW_HIGHDPI: off", 10, 320, 10, MAROON)
            if is_window_state(FLAG_WINDOW_TRANSPARENT):
                draw_text("FLAG_WINDOW_TRANSPARENT: on", 10, 340, 10, LIME)
            else:
                draw_text("FLAG_WINDOW_TRANSPARENT: off", 10, 340, 10, MAROON)
            if is_window_state(FLAG_MSAA_4X_HINT):
                draw_text("FLAG_MSAA_4X_HINT: on", 10, 360, 10, LIME)
            else:
                draw_text("FLAG_MSAA_4X_HINT: off", 10, 360, 10, MAROON)

        # EndDrawing()
        # -----------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

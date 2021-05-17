# core_input_gestures.py
# ******************************************************************************************
#
#   raylib [core] example - Input Gestures Detection
#
#   This example has been created using raylib 1.4 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2016 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_GESTURE_STRINGS = 20


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [core] example - input gestures")

    touch_position: Vector2 = Vector2()
    touch_area: Rectangle = Rectangle(220, 10, screen_width - 230.0, screen_height - 20.0)

    gestures_count: int = 0
    gesture_strings = ["" for _ in range(MAX_GESTURE_STRINGS)]

    current_gesture: int = GESTURE_NONE
    last_gesture: int = GESTURE_NONE

    # SetGesturesEnabled(0b0000000000001001)   # Enable only some gestures to be detected

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        last_gesture = current_gesture
        current_gesture = get_gesture_detected()
        touch_position = get_touch_position(0)

        if check_collision_point_rec(touch_position, touch_area) and (current_gesture != GESTURE_NONE):
            if current_gesture != last_gesture:
                # Store gesture string
                if current_gesture == GESTURE_TAP:
                    gesture_strings[gestures_count] = "GESTURE TAP"
                elif current_gesture == GESTURE_DOUBLETAP:
                    gesture_strings[gestures_count] = "GESTURE DOUBLETAP"
                elif current_gesture == GESTURE_HOLD:
                    gesture_strings[gestures_count] = "GESTURE HOLD"
                elif current_gesture == GESTURE_DRAG:
                    gesture_strings[gestures_count] = "GESTURE DRAG"
                elif current_gesture == GESTURE_SWIPE_RIGHT:
                    gesture_strings[gestures_count] = "GESTURE SWIPE RIGHT"
                elif current_gesture == GESTURE_SWIPE_LEFT:
                    gesture_strings[gestures_count] = "GESTURE SWIPE LEFT"
                elif current_gesture == GESTURE_SWIPE_UP:
                    gesture_strings[gestures_count] = "GESTURE SWIPE UP"
                elif current_gesture == GESTURE_SWIPE_DOWN:
                    gesture_strings[gestures_count] = "GESTURE SWIPE DOWN"
                elif current_gesture == GESTURE_PINCH_IN:
                    gesture_strings[gestures_count] = "GESTURE PINCH IN"
                elif current_gesture == GESTURE_PINCH_OUT:
                    gesture_strings[gestures_count] = "GESTURE PINCH OUT"

                gestures_count += 1

                # Reset gestures strings
                if gestures_count >= MAX_GESTURE_STRINGS:
                    for i in range(MAX_GESTURE_STRINGS):
                        gesture_strings[i] = ""

                    gestures_count = 0

        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            draw_rectangle_rec(touch_area, GRAY)
            draw_rectangle(225, 15, screen_width - 240, screen_height - 30, RAYWHITE)

            draw_text("GESTURES TEST AREA", screen_width - 270, screen_height - 40, 20, fade(GRAY, 0.5))

            for i in range(gestures_count):
                if i % 2 == 0:
                    draw_rectangle(10, 30 + 20 * i, 200, 20, fade(LIGHTGRAY, 0.5))
                else:
                    draw_rectangle(10, 30 + 20 * i, 200, 20, fade(LIGHTGRAY, 0.3))

                if i < gestures_count - 1:
                    draw_text(gesture_strings[i], 35, 36 + 20 * i, 10, DARKGRAY)
                else:
                    draw_text(gesture_strings[i], 35, 36 + 20 * i, 10, MAROON)

            draw_rectangle_lines(10, 29, 200, screen_height - 50, GRAY)
            draw_text("DETECTED GESTURES", 50, 15, 10, GRAY)

            if current_gesture != GESTURE_NONE:
                draw_circle_v(touch_position, 30, MAROON)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

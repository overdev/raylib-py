# core_input_gamepad.py
# ******************************************************************************************
#
#   raylib [core] example - Gamepad input
#
#   NOTE: This example requires a Gamepad connected to the system
#         raylib is configured to work with the following gamepads:
#                - Xbox 360 Controller (Xbox 360, Xbox One)
#                - PLAYSTATION(R)3 Controller
#         Check raylib.h for buttons configuration
#
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2013-2019 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/
import sys
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

# NOTE: Gamepad name ID depends on drivers and OS
XBOX360_LEGACY_NAME_ID = "Xbox Controller"

PLATFORM_RPI = False
if sys.platform == 'linux':
    try:
        import RPi.GPIO as gpio

        PLATFORM_RPI = True
    except (ImportError, RuntimeError, ModuleNotFoundError):
        pass

if PLATFORM_RPI:
    XBOX360_NAME_ID = "Microsoft X-Box 360 pad"
    PS3_NAME_ID = "PLAYSTATION(R)3 Controller"
else:
    XBOX360_NAME_ID = "Xbox 360 Controller"
    PS3_NAME_ID = "PLAYSTATION(R)3 Controller"


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    set_config_flags(FLAG_MSAA_4X_HINT)  # Set MSAA 4X hint before windows creation

    init_window(screen_width, screen_height, "raylib [core] example - gamepad input")

    tex_ps3_pad: Texture2D = load_texture("resources/ps3.png")
    tex_xbox_pad: Texture2D = load_texture("resources/xbox.png")

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # ...
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            if is_gamepad_available(0):
                draw_text(text_format("GP1: %s", get_gamepad_name(0)), 10, 10, 10, BLACK)

                if is_gamepad_name(0, XBOX360_NAME_ID) or is_gamepad_name(0, XBOX360_LEGACY_NAME_ID):
                    draw_texture(tex_xbox_pad, 0, 0, DARKGRAY)

                    # Draw buttons: xbox home
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_MIDDLE):
                        draw_circle(394, 89, 19, RED)

                    # Draw buttons: basic
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_MIDDLE_RIGHT):
                        draw_circle(436, 150, 9, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_MIDDLE_LEFT):
                        draw_circle(352, 150, 9, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_FACE_LEFT):
                        draw_circle(501, 151, 15, BLUE)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_FACE_DOWN):
                        draw_circle(536, 187, 15, LIME)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_FACE_RIGHT):
                        draw_circle(572, 151, 15, MAROON)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_FACE_UP):
                        draw_circle(536, 115, 15, GOLD)

                    # Draw buttons: d-pad
                    draw_rectangle(317, 202, 19, 71, BLACK)
                    draw_rectangle(293, 228, 69, 19, BLACK)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_FACE_UP):
                        draw_rectangle(317, 202, 19, 26, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_FACE_DOWN):
                        draw_rectangle(317, 202 + 45, 19, 26, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_FACE_LEFT):
                        draw_rectangle(292, 228, 25, 19, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_FACE_RIGHT):
                        draw_rectangle(292 + 44, 228, 26, 19, RED)

                    # Draw buttons: left-right back
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_TRIGGER_1):
                        draw_circle(259, 61, 20, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_TRIGGER_1):
                        draw_circle(536, 61, 20, RED)

                    # Draw axis: left joystick
                    draw_circle(259, 152, 39, BLACK)
                    draw_circle(259, 152, 34, LIGHTGRAY)
                    draw_circle(259 + int(get_gamepad_axis_movement(0, GAMEPAD_AXIS_LEFT_X) * 20),
                                152 + int(get_gamepad_axis_movement(0, GAMEPAD_AXIS_LEFT_Y) * 20), 25, BLACK)

                    # Draw axis: right joystick
                    draw_circle(461, 237, 38, BLACK)
                    draw_circle(461, 237, 33, LIGHTGRAY)
                    draw_circle(461 + int(get_gamepad_axis_movement(0, GAMEPAD_AXIS_RIGHT_X) * 20),
                                237 + int(get_gamepad_axis_movement(0, GAMEPAD_AXIS_RIGHT_Y) * 20), 25, BLACK)

                    # Draw axis: left-right triggers
                    draw_rectangle(170, 30, 15, 70, GRAY)
                    draw_rectangle(604, 30, 15, 70, GRAY)
                    draw_rectangle(170, 30, 15,
                                   int(((1 + get_gamepad_axis_movement(0, GAMEPAD_AXIS_LEFT_TRIGGER)) / 2) * 70), RED)
                    draw_rectangle(604, 30, 15,
                                   int(((1 + get_gamepad_axis_movement(0, GAMEPAD_AXIS_RIGHT_TRIGGER)) / 2) * 70), RED)

                    # draw_text(text_format("Xbox axis LT: %02.02", get_gamepad_axis_movement(0, GAMEPAD_AXIS_LEFT_TRIGGER)), 10, 40, 10, BLACK)
                    # draw_text(text_format("Xbox axis RT: %02.02", get_gamepad_axis_movement(0, GAMEPAD_AXIS_RIGHT_TRIGGER)), 10, 60, 10, BLACK)
                elif is_gamepad_name(0, PS3_NAME_ID):
                    draw_texture(tex_ps3_pad, 0, 0, DARKGRAY)

                    # Draw buttons: ps
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_MIDDLE):
                        draw_circle(396, 222, 13, RED)

                    # Draw buttons: basic
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_MIDDLE_LEFT):
                        draw_rectangle(328, 170, 32, 13, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_MIDDLE_RIGHT):
                        draw_triangle(Vector2(436, 168), Vector2(436, 185), Vector2(464, 177), RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_FACE_UP):
                        draw_circle(557, 144, 13, LIME)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_FACE_RIGHT):
                        draw_circle(586, 173, 13, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_FACE_DOWN):
                        draw_circle(557, 203, 13, VIOLET)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_FACE_LEFT):
                        draw_circle(527, 173, 13, PINK)

                    # Draw buttons: d-pad
                    draw_rectangle(225, 132, 24, 84, BLACK)
                    draw_rectangle(195, 161, 84, 25, BLACK)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_FACE_UP):
                        draw_rectangle(225, 132, 24, 29, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_FACE_DOWN):
                        draw_rectangle(225, 132 + 54, 24, 30, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_FACE_LEFT):
                        draw_rectangle(195, 161, 30, 25, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_FACE_RIGHT):
                        draw_rectangle(195 + 54, 161, 30, 25, RED)

                    # Draw buttons: left-right back buttons
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_LEFT_TRIGGER_1):
                        draw_circle(239, 82, 20, RED)
                    if is_gamepad_button_down(0, GAMEPAD_BUTTON_RIGHT_TRIGGER_1):
                        draw_circle(557, 82, 20, RED)

                    # Draw axis: left joystick
                    draw_circle(319, 255, 35, BLACK)
                    draw_circle(319, 255, 31, LIGHTGRAY)
                    draw_circle(319 + int(get_gamepad_axis_movement(0, GAMEPAD_AXIS_LEFT_X) * 20),
                                255 + int(get_gamepad_axis_movement(0, GAMEPAD_AXIS_LEFT_Y) * 20), 25, BLACK)

                    # Draw axis: right joystick
                    draw_circle(475, 255, 35, BLACK)
                    draw_circle(475, 255, 31, LIGHTGRAY)
                    draw_circle(475 + int(get_gamepad_axis_movement(0, GAMEPAD_AXIS_RIGHT_X) * 20),
                                255 + int(get_gamepad_axis_movement(0, GAMEPAD_AXIS_RIGHT_Y) * 20), 25, BLACK)

                    # Draw axis: left-right triggers
                    draw_rectangle(169, 48, 15, 70, GRAY)
                    draw_rectangle(611, 48, 15, 70, GRAY)
                    draw_rectangle(169, 48, 15,
                                   int(((1 - get_gamepad_axis_movement(0, GAMEPAD_AXIS_LEFT_TRIGGER)) / 2) * 70), RED)
                    draw_rectangle(611, 48, 15,
                                   int(((1 - get_gamepad_axis_movement(0, GAMEPAD_AXIS_RIGHT_TRIGGER)) / 2) * 70), RED)
                else:
                    draw_text("- GENERIC GAMEPAD -", 280, 180, 20, GRAY)

                    # TODO: Draw generic gamepad

                draw_text(text_format("DETECTED AXIS [%i]:", get_gamepad_axis_count(0)), 10, 50, 10, MAROON)

                for i in range(get_gamepad_axis_count(0)):
                    draw_text(text_format("AXIS %i: %.02f", i, get_gamepad_axis_movement(0, i)), 20, 70 + 20 * i, 10,
                              DARKGRAY)

                if get_gamepad_button_pressed() != -1:
                    draw_text(text_format("DETECTED BUTTON: %i", get_gamepad_button_pressed()), 10, 430, 10, RED)
                else:
                    draw_text("DETECTED BUTTON: NONE", 10, 430, 10, GRAY)
            else:
                draw_text("GP1: NOT DETECTED", 10, 10, 10, GRAY)

                draw_texture(tex_xbox_pad, 0, 0, LIGHTGRAY)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(tex_ps3_pad)
    unload_texture(tex_xbox_pad)

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()

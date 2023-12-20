#*******************************************************************************************
#
#   raylib [core] example - 2d camera split screen
#
#   Addapted from the core_3d_camera_split_screen example: 
#       https://github.com/raysan5/raylib/blob/master/examples/core/core_3d_camera_split_screen.c
#
#   Example originally created with raylib 4.5, last time updated with raylib 4.5
#
#   Example contributed by Gabriel dos Santos Sanches (@gabrielssanches) and reviewed by Ramon Santamaria (@raysan5)
#
#   Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
#   BSD-like license that allows static linking with closed source software
#
#   Copyright (c) 2023 Gabriel dos Santos Sanches (@gabrielssanches)
#
#*******************************************************************************************/

import sys
import os
from ctypes import byref
from raylibpy import *

PLAYER_SIZE = 40


def main():
    """Transpiled function."""
    screenWidth = 800
    screenHeight = 440

    init_window(screenWidth, screenHeight, "raylib [core] example - 2d camera split screen")

    red_player = Rectangle(200, 200, PLAYER_SIZE, PLAYER_SIZE)
    blue_player = Rectangle(250, 200, PLAYER_SIZE, PLAYER_SIZE)

    redPlayerCamera = Camera2D()
    redPlayerCamera.target  = Vector2(red_player.x, red_player.y)
    redPlayerCamera.offset  = Vector2(200.0, 200.0)
    redPlayerCamera.rotation  = 0.0
    redPlayerCamera.zoom  = 1.0

    bluePlayerCamera = Camera2D()
    bluePlayerCamera.target  = Vector2(blue_player.x, blue_player.y)
    bluePlayerCamera.offset  = Vector2(200.0, 200.0)
    bluePlayerCamera.rotation  = 0.0
    bluePlayerCamera.zoom  = 1.0

    redPlayerScreenCamera = load_render_texture(screenWidth / 2, screenHeight)
    bluePlayerScreenCamera = load_render_texture(screenWidth / 2, screenHeight)

    splitScreenRect1 = Rectangle(0.0, 0.0, redPlayerScreenCamera.texture.width, redPlayerScreenCamera.texture.height * -1.0)
    splitScreenRect2 = Rectangle(0.0, 0.0, redPlayerScreenCamera.texture.width, redPlayerScreenCamera.texture.height * -1.0)

    set_target_fps(60)

    while not window_should_close():
        if is_key_down(KEY_KP_8):
            red_player.y  += 3.0
        elif is_key_down(KEY_KP_5):
            red_player.y  -= 3.0
        
        if is_key_down(KEY_KP_6):
            red_player.x  += 3.0
        elif is_key_down(KEY_KP_4):
            red_player.x  -= 3.0
        
        if is_key_down(KEY_UP):
            blue_player.y  -= 3.0
        elif is_key_down(KEY_DOWN):
            blue_player.y  += 3.0
        
        if is_key_down(KEY_RIGHT):
            blue_player.x  += 3.0
        elif is_key_down(KEY_LEFT):
            blue_player.x  -= 3.0

        redPlayerCamera.target = red_player.xy
        bluePlayerCamera.target = blue_player.xy

        with texture_mode(redPlayerScreenCamera):
            clear_background(RAYWHITE)

            begin_mode2d(redPlayerCamera)
            draw_rectangle_rec(red_player, RED)
            draw_rectangle_rec(blue_player, GRAY)
            end_mode2d()

            draw_rectangle(0, 0, get_screen_width() / 2, 30, fade(RAYWHITE, 0.6))
            draw_text("RED PLAYER: W/S/A/D to move", 10, 10, 10, MAROON)

        # end_texture_mode()

        with texture_mode(bluePlayerScreenCamera):
            clear_background(RAYWHITE)

            begin_mode2d(bluePlayerCamera)
            draw_rectangle_rec(red_player, GRAY)
            draw_rectangle_rec(blue_player, BLUE)
            end_mode2d()

            draw_text("BLUE", blue_player.x, blue_player.y, 10, DARKBLUE)
            draw_rectangle(0, 0, get_screen_width() / 2, 30, fade(RAYWHITE, 0.6))
            draw_text("BLUE PLAYER: UP/DOWN/LEFT/RIGHT to move", 10, 10, 10, DARKBLUE)

        # end_texture_mode()

        with drawing():

            clear_background(BLACK)
            draw_texture_rec(redPlayerScreenCamera.texture, splitScreenRect1, Vector2(0, 0), WHITE)
            draw_texture_rec(bluePlayerScreenCamera.texture, splitScreenRect2, Vector2(screenWidth / 2.0, 0), WHITE)
            draw_rectangle(get_screen_width() / 2 - 2, 0, 4, get_screen_height(), LIGHTGRAY)

        # end_drawing()

    unload_render_texture(redPlayerScreenCamera)
    unload_render_texture(bluePlayerScreenCamera)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
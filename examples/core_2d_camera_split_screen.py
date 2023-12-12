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

    player1 = Rectangle(200, 200, PLAYER_SIZE, PLAYER_SIZE)
    player2 = Rectangle(250, 200, PLAYER_SIZE, PLAYER_SIZE)

    camera1 = Camera2D(0)
    camera1.target  = Vector2(player1.x, player1.y)
    camera1.offset  = Vector2(200.0, 200.0)
    camera1.rotation  = 0.0
    camera1.zoom  = 1.0

    camera2 = Camera2D(0)
    camera2.target  = Vector2(player2.x, player2.y)
    camera2.offset  = Vector2(200.0, 200.0)
    camera2.rotation  = 0.0
    camera2.zoom  = 1.0

    screenCamera1 = load_render_texture(screenWidth / 2, screenHeight)
    screenCamera2 = load_render_texture(screenWidth / 2, screenHeight)

    splitScreenRect = Rectangle(0.0, 0.0, screenCamera1.texture.width, screenCamera1.texture.height)

    set_target_fps(60)
    
    while not window_should_close():
        if is_key_down(KEY_S):
            player1.y  += 3.0
        elif is_key_down(KEY_W):
            player1.y  -= 3.0
        
        if is_key_down(KEY_D):
            player1.x  += 3.0
        elif is_key_down(KEY_A):
            player1.x  -= 3.0
        
        if is_key_down(KEY_UP):
            player2.y  -= 3.0
        elif is_key_down(KEY_DOWN):
            player2.y  += 3.0
        
        if is_key_down(KEY_RIGHT):
            player2.x  += 3.0
        elif is_key_down(KEY_LEFT):
            player2.x  -= 3.0

        camera1.target  = Vector2(player1.x, player1.y)
        camera2.target  = Vector2(player2.x, player2.y)

        with texture_mode(screenCamera1):
            clear_background(RAYWHITE)

            begin_mode2d(camera1)
            draw_rectangle_rec(player1, RED)
            draw_rectangle_rec(player2, BLUE)
            end_mode2d()

            draw_rectangle(0, 0, get_screen_width() / 2, 30, fade(RAYWHITE, 0.6))
            draw_text("PLAYER1: W/S/A/D to move", 10, 10, 10, MAROON)

        # end_texture_mode()

        with texture_mode(screenCamera2):
            clear_background(RAYWHITE)

            begin_mode2d(camera2)
            draw_rectangle_rec(player1, RED)
            draw_rectangle_rec(player2, BLUE)
            end_mode2d()

            draw_rectangle(0, 0, get_screen_width() / 2, 30, fade(RAYWHITE, 0.6))
            draw_text("PLAYER2: UP/DOWN/LEFT/RIGHT to move", 10, 10, 10, DARKBLUE)

        # end_texture_mode()

        with drawing():

            clear_background(BLACK)
            draw_texture_rec(screenCamera1.texture, splitScreenRect, Vector2(0, 0), WHITE)
            draw_texture_rec(screenCamera2.texture, splitScreenRect, Vector2(screenWidth / 2.0, 0), WHITE)
            draw_rectangle(get_screen_width() / 2 - 2, 0, 4, get_screen_height(), LIGHTGRAY)

        # end_drawing()

    unload_render_texture(screenCamera1)
    unload_render_texture(screenCamera2)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
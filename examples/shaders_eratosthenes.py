
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [shaders] example - Sieve of Eratosthenes")

    target = load_render_texture(screenWidth, screenHeight)
    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/eratosthenes.fs")

    set_target_fps(60)
    
    while not window_should_close():

        begin_texture_mode(target)
        clear_background(BLACK)
        draw_rectangle(0, 0, get_screen_width(), get_screen_height(), BLACK)
        end_texture_mode()

        begin_drawing()
        clear_background(RAYWHITE)

        begin_shader_mode(shader)
        draw_texture_rec(target.texture, Rectangle(0, 0, target.texture.width, -target.texture.height), Vector2(0.0, 0.0), WHITE)
        end_shader_mode()

        end_drawing()

    unload_shader(shader)
    unload_render_texture(target)
    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
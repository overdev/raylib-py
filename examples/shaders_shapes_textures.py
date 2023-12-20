
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [shaders] example - shapes and texture shaders")

    fudesumi = load_texture("resources/fudesumi.png")
    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/grayscale.fs")

    set_target_fps(60)
    
    while not window_should_close():
        begin_drawing()

        clear_background(RAYWHITE)
        draw_text("USING DEFAULT SHADER", 20, 40, 10, RED)
        draw_circle(80, 120, 35, DARKBLUE)
        draw_circle_gradient(80, 220, 60, GREEN, SKYBLUE)
        draw_circle_lines(80, 340, 80, DARKBLUE)

        begin_shader_mode(shader)
        draw_text("USING CUSTOM SHADER", 190, 40, 10, RED)
        draw_rectangle(250 - 60, 90, 120, 60, RED)
        draw_rectangle_gradient_h(250 - 90, 170, 180, 130, MAROON, GOLD)
        draw_rectangle_lines(250 - 40, 320, 80, 60, ORANGE)
        end_shader_mode()

        draw_text("USING DEFAULT SHADER", 370, 40, 10, RED)
        draw_triangle(Vector2(430, 80), Vector2(430 - 60, 150), Vector2(430 + 60, 150), VIOLET)
        draw_triangle_lines(Vector2(430, 160), Vector2(430 - 20, 230), Vector2(430 + 20, 230), DARKBLUE)
        draw_poly(Vector2(430, 320), 6, 80, 0, BROWN)

        begin_shader_mode(shader)
        draw_texture(fudesumi, 500, -30, WHITE)
        end_shader_mode()

        draw_text("(c) Fudesumi sprite by Eiden Marsal", 380, screenHeight - 20, 10, GRAY)

        end_drawing()

    unload_shader(shader)
    unload_texture(fudesumi)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
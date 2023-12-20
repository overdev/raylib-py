
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [shaders] example - texture drawing")

    imBlank = gen_image_color(1024, 1024, BLANK)
    texture = load_texture_from_image(imBlank)
    unload_image(imBlank)

    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/cubes_panning.fs")
    time = 0.0
    timeLoc = get_shader_location(shader, "uTime")
    set_shader_value(shader, timeLoc, byref(Float(time)), SHADER_UNIFORM_FLOAT)

    set_target_fps(60)
    
    while not window_should_close():
        time = get_time()

        set_shader_value(shader, timeLoc, byref(Float(time)), SHADER_UNIFORM_FLOAT)

        with drawing():
            clear_background(RAYWHITE)

            begin_shader_mode(shader)
            draw_texture(texture, 0, 0, WHITE)
            end_shader_mode()

            draw_text("BACKGROUND is PAINTED and ANIMATED on SHADER!", 10, 10, 20, MAROON)

        # end_drawing()

    unload_shader(shader)
    close_window()
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
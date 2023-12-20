
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib - multiple sample2D")

    imRed = gen_image_color(800, 450, Color(255, 0, 0, 255))
    texRed = load_texture_from_image(imRed)
    unload_image(imRed)

    imBlue = gen_image_color(800, 450, Color(0, 0, 255, 255))
    texBlue = load_texture_from_image(imBlue)
    unload_image(imBlue)

    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/color_mix.fs")
    texBlueLoc = get_shader_location(shader, "texture1")
    dividerLoc = get_shader_location(shader, "divider")
    dividerValue = 0.5

    set_target_fps(60)
    
    while not window_should_close():
        if is_key_down(KEY_RIGHT):
            dividerValue  += 0.01
        elif is_key_down(KEY_LEFT):
            dividerValue  -= 0.01
        
        if dividerValue < 0.0:
            dividerValue  = 0.0
        elif dividerValue > 1.0:
            dividerValue  = 1.0

        set_shader_value(shader, dividerLoc, byref(Float(dividerValue)), SHADER_UNIFORM_FLOAT)

        begin_drawing()
        clear_background(RAYWHITE)

        begin_shader_mode(shader)
        set_shader_value_texture(shader, texBlueLoc, texBlue)
        draw_texture(texRed, 0, 0, WHITE)
        end_shader_mode()

        draw_text("Use KEY_LEFT/KEY_RIGHT to move texture mixing in shader!", 80, get_screen_height() - 40, 20, RAYWHITE)

        end_drawing()

    unload_shader(shader)
    unload_texture(texRed)
    unload_texture(texBlue)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
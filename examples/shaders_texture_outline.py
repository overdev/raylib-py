
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [shaders] example - Apply an outline to a texture")

    texture = load_texture("resources/fudesumi.png")
    shdrOutline = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/outline.fs")

    outlineSize = 2.0
    outlineColor = (Float * 4)(1.0, 0.0, 0.0, 1.0)
    textureSize = (Float * 2)(texture.width, texture.height)

    outlineSizeLoc = get_shader_location(shdrOutline, "outlineSize")
    outlineColorLoc = get_shader_location(shdrOutline, "outlineColor")
    textureSizeLoc = get_shader_location(shdrOutline, "textureSize")

    set_shader_value(shdrOutline, outlineSizeLoc, byref(Float(outlineSize)), SHADER_UNIFORM_FLOAT)
    set_shader_value(shdrOutline, outlineColorLoc, outlineColor, SHADER_UNIFORM_VEC4)
    set_shader_value(shdrOutline, textureSizeLoc, textureSize, SHADER_UNIFORM_VEC2)

    set_target_fps(60)
    
    while not window_should_close():
        outlineSize  += get_mouse_wheel_move()
        
        if outlineSize < 1.0:
            outlineSize  = 1.0

        set_shader_value(shdrOutline, outlineSizeLoc, byref(Float(outlineSize)), SHADER_UNIFORM_FLOAT)

        begin_drawing()
        clear_background(RAYWHITE)

        begin_shader_mode(shdrOutline)
        draw_texture(texture, get_screen_width() / 2 - texture.width / 2, -30, WHITE)
        end_shader_mode()

        draw_text("Shader-based\ntexture\noutline", 10, 10, 20, GRAY)
        draw_text("Scroll mouse wheel to\nchange outline size", 10, 72, 20, GRAY)
        draw_text(f"Outline size: {int(outlineSize)} px", 10, 120, 20, MAROON)

        draw_fps(710, 10)

        end_drawing()

    unload_texture(texture)
    unload_shader(shdrOutline)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
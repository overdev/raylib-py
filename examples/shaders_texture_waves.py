
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [shaders] example - texture waves")

    texture = load_texture("resources/space.png")
    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/wave.fs")

    secondsLoc = get_shader_location(shader, "seconds")
    freqXLoc = get_shader_location(shader, "freqX")
    freqYLoc = get_shader_location(shader, "freqY")
    ampXLoc = get_shader_location(shader, "ampX")
    ampYLoc = get_shader_location(shader, "ampY")
    speedXLoc = get_shader_location(shader, "speedX")
    speedYLoc = get_shader_location(shader, "speedY")

    freqX = 25.0
    freqY = 25.0
    ampX = 5.0
    ampY = 5.0
    speedX = 8.0
    speedY = 8.0

    screenSize = (Float * 2)(get_screen_width(), get_screen_height())

    set_shader_value(shader, get_shader_location(shader, "size"), byref(screenSize), SHADER_UNIFORM_VEC2)
    set_shader_value(shader, freqXLoc, byref(Float(freqX)), SHADER_UNIFORM_FLOAT)
    set_shader_value(shader, freqYLoc, byref(Float(freqY)), SHADER_UNIFORM_FLOAT)
    set_shader_value(shader, ampXLoc, byref(Float(ampX)), SHADER_UNIFORM_FLOAT)
    set_shader_value(shader, ampYLoc, byref(Float(ampY)), SHADER_UNIFORM_FLOAT)
    set_shader_value(shader, speedXLoc, byref(Float(speedX)), SHADER_UNIFORM_FLOAT)
    set_shader_value(shader, speedYLoc, byref(Float(speedY)), SHADER_UNIFORM_FLOAT)

    seconds = 0.0

    set_target_fps(60)
    
    while not window_should_close():
        seconds += get_frame_time()

        set_shader_value(shader, secondsLoc, byref(Float(seconds)), SHADER_UNIFORM_FLOAT)

        with drawing():

            clear_background(RAYWHITE)

            with shader_mode(shader):
                draw_texture(texture, 0, 0, WHITE)
                draw_texture(texture, texture.width, 0, WHITE)

            # end_shader_mode()

        # end_drawing()

    unload_shader(shader)
    unload_texture(texture)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())
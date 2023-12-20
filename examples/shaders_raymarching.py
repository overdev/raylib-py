
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    set_config_flags(FLAG_WINDOW_RESIZABLE)

    init_window(screenWidth, screenHeight, "raylib [shaders] example - raymarching shapes")

    camera = Camera()
    camera.position  = Vector3(2.5, 2.5, 3.0)
    camera.target  = Vector3(0.0, 0.0, 0.7)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 65.0
    camera.projection  = CAMERA_PERSPECTIVE

    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/raymarching.fs")
    viewEyeLoc = get_shader_location(shader, "viewEye")
    viewCenterLoc = get_shader_location(shader, "viewCenter")
    runTimeLoc = get_shader_location(shader, "runTime")
    resolutionLoc = get_shader_location(shader, "resolution")
    resolution = (Float * 2)(screenWidth, screenHeight)
    set_shader_value(shader, resolutionLoc, byref(resolution), SHADER_UNIFORM_VEC2)

    runTime = 0.0

    disable_cursor()

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(byref(camera), CAMERA_FIRST_PERSON)

        cameraPos = (Float*3)(camera.position.x, camera.position.y, camera.position.z)
        cameraTarget = (Float*3)(camera.target.x, camera.target.y, camera.target.z)

        deltaTime = get_frame_time()
        runTime  += deltaTime

        set_shader_value(shader, viewEyeLoc, byref(cameraPos), SHADER_UNIFORM_VEC3)
        set_shader_value(shader, viewCenterLoc, byref(cameraTarget), SHADER_UNIFORM_VEC3)
        set_shader_value(shader, runTimeLoc, byref(Float(runTime)), SHADER_UNIFORM_FLOAT)

        if is_window_resized():
            resolution[0] = float(get_screen_width())
            resolution[1] = float(get_screen_height())
            set_shader_value(shader, resolutionLoc, byref(resolution), SHADER_UNIFORM_VEC2)

        begin_drawing()
        clear_background(RAYWHITE)

        begin_shader_mode(shader)
        draw_rectangle(0, 0, get_screen_width(), get_screen_height(), WHITE)
        end_shader_mode()

        draw_text("(c) Raymarching shader by Iñigo Quilez. MIT License.", get_screen_width() - 280, get_screen_height() - 20, 10, BLACK)

        end_drawing()

    unload_shader(shader)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())